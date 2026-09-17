"""Immutable capture runner for staged composer prompts.

This runner only calls Ollama and stores raw bytes plus hashes. It does not
repair, normalize, or decide musical content.
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, os
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

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True)
    p.add_argument("--stage", required=True, choices=["stage-1", "stage-2", "stage-3"])
    p.add_argument("--attempt", type=int, required=True)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--brief", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--num-predict", type=int, required=True)
    p.add_argument("--stage-number", type=int, choices=[1,2,3], required=True)
    p.add_argument("--instruction", type=Path, required=True)
    p.add_argument("--prior", type=Path)
    p.add_argument("--format-schema", type=Path, help="Stage-specific JSON Schema for Ollama structured output")
    p.add_argument("--ollama-url", default="http://127.0.0.1:11434/api/chat")
    a = p.parse_args()
    prompt_bytes = a.input.read_bytes(); brief_bytes = a.brief.read_bytes()
    prompt = prompt_bytes.decode("utf-8")
    pf = preflight(prompt, a.stage_number, a.brief.resolve(), a.instruction.resolve(), a.prior.resolve() if a.prior else None)
    if not pf["pass"]:
        raise ValueError("preflight failed: " + json.dumps(pf, ensure_ascii=False))
    settings = dict(SETTINGS); settings["num_predict"] = a.num_predict
    schema = json.loads(a.format_schema.read_text(encoding="utf-8")) if a.format_schema else None
    req_obj = build_request(a.model, prompt, settings, schema)
    req_bytes = json.dumps(req_obj, ensure_ascii=False, separators=(",", ":")).encode()
    with urlopen(Request(a.ollama_url, data=req_bytes,
                         headers={"Content-Type":"application/json; charset=utf-8"},
                         method="POST"), timeout=3600) as response:
        api_bytes = response.read()
    api = json.loads(api_bytes.decode("utf-8")); content = api["message"]["content"]
    if not isinstance(content, str): raise TypeError("message.content is not text")
    out = a.output_dir
    exclusive(out / "raw-api-response.json", api_bytes)
    exclusive(out / "raw-output.txt", content.encode("utf-8"))
    meta = {"capture_status":"CAPTURED", "captured_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
            "model_identifier_requested":a.model, "model_identifier_reported":api.get("model"),
            "interface_version":"composer-interface-v1.1", "stage":a.stage, "attempt":a.attempt,
            "input_sha256":sha(prompt_bytes), "payload_sha256":sha(prompt_bytes), "brief_sha256":sha(brief_bytes),
            "generation_parameters":settings, "request_sha256":sha(req_bytes),
            "structured_output_schema":str(a.format_schema) if a.format_schema else None,
            "raw_api_response_sha256":sha(api_bytes), "raw_output_sha256":sha(content.encode()),
            "semantic_repair_performed":False, "done_reason":api.get("done_reason"),
            "eval_count":api.get("eval_count"), "prompt_eval_count":api.get("prompt_eval_count")}
    exclusive(out / "capture-manifest.json", (json.dumps(meta, ensure_ascii=False, indent=2)+"\n").encode())
    print(json.dumps(meta, ensure_ascii=False))

if __name__ == "__main__":
    main()
