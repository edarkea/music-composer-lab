"""Immutable capture runner for staged composer prompts.

This runner only calls Ollama and stores raw bytes plus hashes. It does not
repair, normalize, or decide musical content.
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, os, socket, time
from urllib.error import HTTPError, URLError
from pathlib import Path
from urllib.request import Request, urlopen
from staged_harness import preflight

SETTINGS = {"temperature": 0, "seed": 41, "top_p": 1, "top_k": 40,
            "repeat_penalty": 1, "num_ctx": 32768}

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def exclusive(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as f:
        f.write(data); f.flush(); os.fsync(f.fileno())

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
            result["transport_status"] = "INCOMPLETE_RESPONSE"
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
    transport = transport_request(req_bytes, a.ollama_url, a.http_timeout)
    transport_meta = {k: v for k, v in transport.items() if k != "response_bytes"}
    if transport["transport_status"] != "COMPLETE_RESPONSE":
        out = a.output_dir
        out.mkdir(parents=True, exist_ok=True)
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
    except Exception as exc:
        out = a.output_dir
        out.mkdir(parents=True, exist_ok=True)
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
            "request_id": request_id,
            "input_sha256":sha(prompt_bytes), "payload_sha256":sha(prompt_bytes), "brief_sha256":sha(brief_bytes),
            "generation_parameters":settings, "request_sha256":sha(req_bytes),
            "structured_output_schema":str(a.format_schema) if a.format_schema else None,
            "raw_api_response_sha256":sha(api_bytes), "raw_output_sha256":sha(content.encode()),
            "semantic_repair_performed":False, "done_reason":api.get("done_reason"),
            "eval_count":api.get("eval_count"), "prompt_eval_count":api.get("prompt_eval_count"),
            "transport_status": transport["transport_status"],
            "elapsed_seconds": transport["elapsed_seconds"],
            "http_timeout_seconds": a.http_timeout}
    exclusive(out / "capture-manifest.json", (json.dumps(meta, ensure_ascii=False, indent=2)+"\n").encode())
    print(json.dumps(meta, ensure_ascii=False))

if __name__ == "__main__":
    main()
