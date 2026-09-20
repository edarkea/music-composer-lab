"""Immutable capture runner for staged composer prompts.

This runner only calls Ollama and stores raw bytes plus hashes. It does not
repair, normalize, or decide musical content.
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, os, re, socket, time
from urllib.error import HTTPError, URLError
from pathlib import Path
from urllib.request import Request, urlopen
from staged_harness import preflight

SETTINGS = {"temperature": 0, "seed": 41, "top_p": 1, "top_k": 40,
            "repeat_penalty": 1, "num_ctx": 32768}
REQUEST_STATES = {"PREPARED","SENT","CAPTURED","TIMEOUT","CONNECTION_FAILURE",
                  "HTTP_ERROR","INTERRUPTED_OR_INCOMPLETE","INVALID_API_RESPONSE"}

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def payload_record_ids(prompt: str) -> list[str]:
    return re.findall(r"(?m)^BEGIN RECORD: (.+)$", prompt)

def exclusive(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as f:
        f.write(data); f.flush(); os.fsync(f.fileno())

def journal_state(registry: Path, state: str, details: dict | None = None) -> None:
    if state not in REQUEST_STATES:
        raise ValueError(f"unsupported request state: {state}")
    row = {"state":state,"at_utc":dt.datetime.now(dt.timezone.utc).isoformat(), **(details or {})}
    with (registry / "state-history.jsonl").open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
        f.flush(); os.fsync(f.fileno())

def reserve_capture(registry_root: Path, request_id: str, output_dir: Path,
                   manifest: dict) -> Path:
    """Exclusively reserve request/output identities and persist PREPARED first."""
    if not request_id or any(c in request_id for c in "/\\"):
        raise ValueError("request-id must be a non-empty path-safe identifier")
    registry_root.mkdir(parents=True, exist_ok=True)
    identity = (manifest.get("experiment_id"), manifest.get("model"),
                manifest.get("stage"), manifest.get("attempt"))
    if all(value is not None for value in identity):
        for prior_manifest in registry_root.glob("*/request-manifest.json"):
            try:
                prior = json.loads(prior_manifest.read_text(encoding="utf-8"))
                prior_identity = (prior.get("experiment_id"),prior.get("model"),
                                  prior.get("stage"),prior.get("attempt"))
                history = prior_manifest.parent / "state-history.jsonl"
                sent = history.exists() and any(json.loads(line).get("state") == "SENT"
                                                 for line in history.read_text(encoding="utf-8").splitlines() if line)
            except Exception:
                # An unreadable registry entry makes reuse ambiguous; fail closed.
                raise ValueError(f"cannot verify prior request registry entry: {prior_manifest}")
            if prior_identity == identity and sent:
                raise ValueError("stage attempt identity already sent; choose the next unused attempt number")
    registry = registry_root / request_id
    registry.mkdir()  # fails on any reused request ID
    try:
        output_dir.mkdir(parents=True, exist_ok=False)  # never overwrite captures
    except Exception:
        registry.rmdir()  # reservation is safe to release: HTTP has not been called
        raise
    exclusive(registry / "request-manifest.json",
              (json.dumps({**manifest,"state":"PREPARED"},ensure_ascii=False,indent=2)+"\n").encode())
    journal_state(registry,"PREPARED",{"request_sha256":manifest.get("request_sha256")})
    return registry

def build_request(model: str, prompt: str, settings: dict, format_schema: dict | None = None) -> dict:
    request = {"model": model, "messages":[{"role":"user","content":prompt}],
               "stream":False, "options":settings}
    if format_schema is not None:
        request["format"] = format_schema
    return request

def transport_request(request_bytes: bytes, url: str, timeout: float,
                      opener=urlopen) -> dict:
    """Perform one non-streaming HTTP request with auditable transport state.

    This function deliberately does not interpret model content.  The opener
    argument is injectable so timeout, HTTP-error, and incomplete-response
    handling can be tested without contacting Ollama.
    """
    started = time.monotonic()
    result = {"transport_status": None, "http_status": None,
              "elapsed_seconds": None, "response_bytes": b"",
              "error_type": None, "error": None}
    try:
        response = opener(Request(url, data=request_bytes,
                                  headers={"Content-Type":"application/json; charset=utf-8"},
                                  method="POST"), timeout=timeout)
        result["http_status"] = getattr(response, "status", None)
        try:
            body = response.read()
        except (TimeoutError, socket.timeout) as exc:
            partial = getattr(exc, "partial", b"")
            if isinstance(partial, (bytes, bytearray)): result["response_bytes"] = bytes(partial)
            result["transport_status"] = "TIMEOUT"
            result["error_type"] = type(exc).__name__
            result["error"] = str(exc) or "socket timeout"
            result["elapsed_seconds"] = time.monotonic() - started
            return result
        except Exception as exc:
            partial = getattr(exc, "partial", b"")
            if isinstance(partial, (bytes, bytearray)): result["response_bytes"] = bytes(partial)
            result["transport_status"] = "INTERRUPTED_OR_INCOMPLETE"
            result["error_type"] = type(exc).__name__
            result["error"] = str(exc)
            result["elapsed_seconds"] = time.monotonic() - started
            return result
        if not isinstance(body, (bytes, bytearray)):
            result["transport_status"] = "INTERRUPTED_OR_INCOMPLETE"
            result["error_type"] = "invalid_body_type"
            result["error"] = "HTTP response body was not bytes"
        else:
            result["response_bytes"] = bytes(body)
            result["transport_status"] = "COMPLETE_RESPONSE"
    except HTTPError as exc:
        result["http_status"] = exc.code
        try: result["response_bytes"] = exc.read()
        except Exception: result["response_bytes"] = b""
        result["transport_status"] = "HTTP_ERROR"
        result["error_type"] = "HTTPError"
        result["error"] = str(exc)
    except (TimeoutError, socket.timeout) as exc:
        result["transport_status"] = "TIMEOUT"
        result["error_type"] = type(exc).__name__
        result["error"] = str(exc) or "socket timeout"
    except (ConnectionError, URLError, OSError) as exc:
        result["transport_status"] = "CONNECTION_FAILURE"
        result["error_type"] = type(exc).__name__
        result["error"] = str(exc)
    except Exception as exc:
        result["transport_status"] = "INTERRUPTED_OR_INCOMPLETE"
        result["error_type"] = type(exc).__name__
        result["error"] = str(exc)
    result["elapsed_seconds"] = time.monotonic() - started
    return result

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True)
    p.add_argument("--stage", required=True, choices=["stage-1", "stage-2", "stage-3"])
    p.add_argument("--attempt", type=int, required=True)
    p.add_argument("--request-id", default=None,
                   help="separate transport request identity, useful for recovery captures")
    p.add_argument("--request-kind", default="evaluable_attempt",
                   choices=["evaluable_attempt","transport_recovery"])
    p.add_argument("--experiment-id", default="UNSPECIFIED")
    p.add_argument("--request-registry", type=Path,
                   help="directory for exclusive request-ID reservation and state history")
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--brief", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--num-predict", type=int, required=True)
    p.add_argument("--stage-number", type=int, choices=[1,2,3], required=True)
    p.add_argument("--instruction", type=Path, required=True)
    p.add_argument("--prior", type=Path)
    p.add_argument("--format-schema", type=Path, help="Stage-specific JSON Schema for Ollama structured output")
    p.add_argument("--required-record", type=Path, action="append", default=[], help="Additional record required in the model-visible payload")
    p.add_argument("--ollama-url", default="http://127.0.0.1:11434/api/chat")
    p.add_argument("--http-timeout", type=float, default=3600,
                   help="socket timeout in seconds for the Ollama request")
    a = p.parse_args()
    request_id = a.request_id or f"{a.stage}-attempt-{a.attempt}"
    prompt_bytes = a.input.read_bytes(); brief_bytes = a.brief.read_bytes()
    prompt = prompt_bytes.decode("utf-8")
    pf = preflight(prompt, a.stage_number, a.brief.resolve(), a.instruction.resolve(), a.prior.resolve() if a.prior else None, extras=a.required_record)
    if not pf["pass"]:
        raise ValueError("preflight failed: " + json.dumps(pf, ensure_ascii=False))
    settings = dict(SETTINGS); settings["num_predict"] = a.num_predict
    schema = json.loads(a.format_schema.read_text(encoding="utf-8")) if a.format_schema else None
    req_obj = build_request(a.model, prompt, settings, schema)
    req_bytes = json.dumps(req_obj, ensure_ascii=False, separators=(",", ":")).encode()
    # Reserve both identities before any network call. Existing output paths or
    # request IDs are evidence and must never be reused or overwritten.
    registry_root = (a.request_registry or (a.output_dir.parent / "request-registry")).resolve()
    out = a.output_dir.resolve()
    schema_bytes = a.format_schema.read_bytes() if a.format_schema else b""
    prior_bytes = a.prior.read_bytes() if a.prior else b""
    prepared = {"state":"PREPARED", "prepared_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
        "experiment_id":a.experiment_id,"request_id":request_id,"request_kind":a.request_kind,"model":a.model,"stage":a.stage,
        "stage_number":a.stage_number,"attempt":a.attempt,"payload_path":str(a.input.resolve()),
        "payload_sha256":sha(prompt_bytes),"brief_path":str(a.brief.resolve()),"brief_sha256":sha(brief_bytes),
        "schema_path":str(a.format_schema.resolve()) if a.format_schema else None,
        "schema_sha256":sha(schema_bytes) if schema_bytes else None,
        "prior_path":str(a.prior.resolve()) if a.prior else None,"prior_sha256":sha(prior_bytes) if prior_bytes else None,
        "generation_parameters":settings,"timeout_seconds":a.http_timeout,"output_dir":str(out),
        "ollama_url":a.ollama_url,"request_sha256":sha(req_bytes),"interface_version":"composer-interface-v1.1",
        "resolved_record_ids":payload_record_ids(prompt),
        "required_records":[{"path":str(p.resolve()),"sha256":sha(p.read_bytes())} for p in a.required_record],
        "preflight":pf}
    registry = reserve_capture(registry_root, request_id, out, prepared)
    journal_state(registry, "SENT", {"sent_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
                                     "request_kind":a.request_kind,"model_request_count_increment":1})
    transport = transport_request(req_bytes, a.ollama_url, a.http_timeout)
    transport_meta = {k: v for k, v in transport.items() if k != "response_bytes"}
    if transport["transport_status"] != "COMPLETE_RESPONSE":
        status = transport["transport_status"]
        journal_state(registry, status, transport_meta)
        if transport["response_bytes"]:
            exclusive(out / "raw-api-response.partial.json", transport["response_bytes"])
        exclusive(out / "transport-manifest.json",
                  (json.dumps({**transport_meta, "request_sha256": sha(req_bytes),
                               "model": a.model, "stage": a.stage,
                               "attempt": a.attempt, "request_id": request_id,
                               "capture_status": "NOT_CAPTURED"},
                              ensure_ascii=False, indent=2)+"\n").encode())
        raise RuntimeError("transport failed: " + json.dumps(transport_meta, ensure_ascii=False))
    api_bytes = transport["response_bytes"]
    try:
        api = json.loads(api_bytes.decode("utf-8")); content = api["message"]["content"]
        if not isinstance(content, str): raise TypeError("message.content is not text")
        if api.get("done") is not True: raise ValueError("API response is incomplete: done is not true")
    except Exception as exc:
        journal_state(registry, "INVALID_API_RESPONSE", {"error_type":type(exc).__name__,"error":str(exc)})
        exclusive(out / "raw-api-response.partial.json", api_bytes)
        exclusive(out / "transport-manifest.json",
                  (json.dumps({**transport_meta, "transport_status":"INVALID_API_RESPONSE",
                               "request_sha256": sha(req_bytes), "response_sha256": sha(api_bytes),
                               "model": a.model, "stage": a.stage, "attempt": a.attempt,
                               "request_id": request_id,
                               "capture_status":"NOT_CAPTURED", "error_type":type(exc).__name__,
                               "error":str(exc)}, ensure_ascii=False, indent=2)+"\n").encode())
        raise RuntimeError("invalid API response: " + str(exc)) from exc
    out = a.output_dir
    exclusive(out / "raw-api-response.json", api_bytes)
    exclusive(out / "raw-output.txt", content.encode("utf-8"))
    meta = {"capture_status":"CAPTURED", "captured_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
            "model_identifier_requested":a.model, "model_identifier_reported":api.get("model"),
            "interface_version":"composer-interface-v1.1", "stage":a.stage, "attempt":a.attempt,
            "experiment_id":a.experiment_id, "request_id": request_id,
            "request_kind":a.request_kind,"model_request_count":1,
            "payload_path":str(a.input.resolve()),
            "resolved_record_ids":payload_record_ids(prompt),
            "input_sha256":sha(prompt_bytes), "payload_sha256":sha(prompt_bytes), "brief_sha256":sha(brief_bytes),
            "generation_parameters":settings, "request_sha256":sha(req_bytes),
            "structured_output_schema":str(a.format_schema.resolve()) if a.format_schema else None,
            "structured_output_schema_sha256":sha(schema_bytes) if schema_bytes else None,
            "prior_path":str(a.prior.resolve()) if a.prior else None,
            "prior_sha256":sha(prior_bytes) if prior_bytes else None,
            "raw_api_response_sha256":sha(api_bytes), "raw_output_sha256":sha(content.encode()),
            "semantic_repair_performed":False, "done_reason":api.get("done_reason"),
            "eval_count":api.get("eval_count"), "prompt_eval_count":api.get("prompt_eval_count"),
            "transport_status": transport["transport_status"],
            "elapsed_seconds": transport["elapsed_seconds"],
            "http_timeout_seconds": a.http_timeout}
    exclusive(out / "capture-manifest.json", (json.dumps(meta, ensure_ascii=False, indent=2)+"\n").encode())
    journal_state(registry, "CAPTURED", {"capture_manifest":str(out / "capture-manifest.json"),"raw_output_sha256":meta["raw_output_sha256"]})
    print(json.dumps(meta, ensure_ascii=False))

if __name__ == "__main__":
    main()
