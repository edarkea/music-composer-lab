"""Model-neutral Ollama capture runner. It never edits model content."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import sys
from urllib.request import Request, urlopen


SETTINGS = {
    "temperature": 0,
    "seed": 41,
    "top_p": 1,
    "top_k": 40,
    "repeat_penalty": 1,
    "num_ctx": 32768,
    "num_predict": 8192,
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return parsed


def create_exclusive(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True)
    parser.add_argument("--input", required=True, type=Path, help="Frozen prompt UTF-8 text")
    parser.add_argument("--brief", required=True, type=Path, help="Frozen brief used for its hash")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--interface-version", default="composer-interface-v1.1")
    parser.add_argument("--ollama-url", default="http://127.0.0.1:11434/api/chat")
    parser.add_argument("--schema", type=Path, default=Path("datasets/composer-interface-v1.1/output-schema.json"))
    parser.add_argument("--num-predict", type=positive_int, default=SETTINGS["num_predict"], help="Maximum generated tokens (default preserves the v1.1/XMODEL-002 setting)")
    args = parser.parse_args()

    prompt_bytes = args.input.read_bytes()
    brief_bytes = args.brief.read_bytes()
    output_paths = [args.output_dir / name for name in ("raw-api-response.json", "raw-output.txt", "capture-manifest.json")]
    occupied = [str(path) for path in output_paths if path.exists()]
    if occupied:
        raise FileExistsError("Refusing to overwrite immutable capture file(s): " + ", ".join(occupied))
    # Decode solely to ensure the frozen inputs are valid UTF-8; preserve source bytes.
    prompt = prompt_bytes.decode("utf-8")
    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    generation_settings = dict(SETTINGS)
    generation_settings["num_predict"] = args.num_predict
    request_object = {
        "model": args.model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "format": schema,
        "options": generation_settings,
    }
    request_bytes = json.dumps(request_object, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    request = Request(args.ollama_url, data=request_bytes, headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
    with urlopen(request, timeout=3600) as response:
        api_bytes = response.read()
    api_obj = json.loads(api_bytes.decode("utf-8"))
    content = api_obj["message"]["content"]
    if not isinstance(content, str):
        raise TypeError("Ollama response message.content is not a string")
    content_bytes = content.encode("utf-8")

    # Exclusive creation prevents reruns from replacing any captured artifact.
    create_exclusive(args.output_dir / "raw-api-response.json", api_bytes)
    create_exclusive(args.output_dir / "raw-output.txt", content_bytes)
    metadata = {
        "capture_status": "CAPTURED",
        "captured_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "model_identifier_requested": args.model,
        "model_identifier_reported": api_obj.get("model"),
        "interface_version": args.interface_version,
        "brief_sha256": sha256(brief_bytes),
        "prompt_input_sha256": sha256(prompt_bytes),
        "request_sha256": sha256(request_bytes),
        "raw_api_response_sha256": sha256(api_bytes),
        "raw_output_sha256": sha256(content_bytes),
        "generation_parameters": generation_settings,
        "structured_output_schema": str(args.schema),
        "semantic_repair_performed": False,
        "note": "Parámetros de generación iguales no garantizan igualdad bit a bit entre hardware/backends.",
    }
    create_exclusive(args.output_dir / "capture-manifest.json", (json.dumps(metadata, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    print(json.dumps({"status": "CAPTURED", "output_dir": str(args.output_dir), "raw_output_sha256": metadata["raw_output_sha256"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"capture failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(2)
