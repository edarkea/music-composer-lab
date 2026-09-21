"""Reserve and verify Owner-run Codex CLI captures; this tool never invokes Codex."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAYLOAD = ROOT / "outputs/codex/stage-1/payload/revision-2/attempt-1-payload.txt"
SCHEMA = ROOT / "model-visible/stage-1/output-schema.json"
BRIEF_SHA256 = "464ae4378bcb7236f0fb36da52eb65dcb03735197284e3a6899b8686d51ede0b"
EXPECTED_PAYLOAD_SHA256 = "58646fd9fbef25c17b6b5cc7f846490989316f25d5084469d2b8b4cb074a423d"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_events(path: Path) -> tuple[bool, str | None, int]:
    complete = False
    model = None
    valid_lines = 0
    for line in path.read_bytes().splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
        valid_lines += 1
        if not isinstance(event, dict):
            continue
        if event.get("type") == "turn.completed":
            complete = True
        if model is None and isinstance(event.get("server_model"), str) and event["server_model"].strip():
            model = event["server_model"].strip()
    return complete, model, valid_lines


def reserve(args) -> dict:
    if args.stage != 1 or args.attempt not in (1, 2, 3):
        raise ValueError("Stage 1 admite únicamente intentos 1–3")
    expected_id = f"XMODEL-011-CODEX-STAGE1-A{args.attempt}"
    if args.request_id != expected_id:
        raise ValueError(f"request-id debe ser exactamente {expected_id}")
    payload = PAYLOAD.read_bytes()
    if digest(payload) != EXPECTED_PAYLOAD_SHA256:
        raise ValueError("el payload congelado no coincide con el hash esperado")
    out = Path(args.capture_dir)
    regdir = Path(args.registry_dir)
    regdir.mkdir(parents=True, exist_ok=True)
    reg = regdir / f"{args.request_id}.json"
    if reg.exists():
        raise FileExistsError(f"request identity already exists: {reg}")
    out.mkdir(parents=True, exist_ok=False)
    record = {
        "experiment_id": "XMODEL-011", "stage": 1, "attempt": args.attempt,
        "request_id": args.request_id, "status": "RESERVED_MANUAL_NOT_SENT",
        "payload_path": str(PAYLOAD), "payload_sha256": digest(payload),
        "brief_sha256": BRIEF_SHA256, "capture_dir": str(out),
        "reserved_at_utc": now(),
    }
    with reg.open("xb") as f:
        f.write((json.dumps(record, indent=2) + "\n").encode("utf-8"))
    return {"status": record["status"], "request_id": args.request_id,
            "registry": str(reg), "capture_dir": str(out),
            "payload_sha256": digest(payload)}


def record(args) -> dict:
    reg = Path(args.registry)
    rec = json.loads(reg.read_text(encoding="utf-8"))
    if rec.get("status") != "SENT_MANUAL":
        raise ValueError("el intento no está marcado SENT_MANUAL o ya fue registrado")
    out = Path(rec["capture_dir"])
    events, stderr, final = (out / "cli-events.jsonl", out / "cli-stderr.txt", out / "final-output.txt")
    for p in (events, stderr, final):
        if not p.is_file():
            raise FileNotFoundError(f"captura requerida ausente: {p}")
    terminal, model, valid_events = read_events(events)
    final_bytes = final.read_bytes()
    status = "CAPTURED" if args.exit_code == 0 and terminal and final_bytes else "CLI_FAILED_OR_INCOMPLETE"
    manifest = {
        "capture_status": status, "experiment_id": "XMODEL-011", "stage": 1,
        "attempt": rec["attempt"], "request_id": rec["request_id"],
        "recorded_at_utc": now(), "cli_exit_status": args.exit_code,
        "payload_path": rec["payload_path"], "payload_sha256": digest(PAYLOAD.read_bytes()),
        "expected_payload_sha256": EXPECTED_PAYLOAD_SHA256,
        "brief_sha256": BRIEF_SHA256, "interface_version": "composer-interface-v1.1",
        "cli_version": args.cli_version, "model_requested": None,
        "generation_parameters": {"model_selection": "Codex CLI default; no --model argument",
                                   "sampling": "CLI defaults; not set or exposed by this package"},
        "output_schema_path": str(SCHEMA),
        "output_schema_sha256": digest(SCHEMA.read_bytes()),
        "invocation_arguments": ["exec", "--ephemeral", "--ignore-user-config", "--ignore-rules",
            "--sandbox", "read-only", "--ask-for-approval", "never", "--cd", "<unique-temp-workspace>",
            "--json", "--output-schema", str(SCHEMA), "--output-last-message", str(final), "-",
            "stdin: frozen Stage 1 payload"],
        "model_reported": model,
        "model_reported_note": None if model else "La salida JSONL no declara server_model; identidad servida desconocida.",
        "terminal_success_event_observed": terminal, "valid_jsonl_event_count": valid_events,
        "final_output_path": str(final), "final_output_sha256": digest(final_bytes),
        "cli_events_path": str(events), "cli_events_sha256": digest(events.read_bytes()),
        "cli_stderr_path": str(stderr), "cli_stderr_sha256": digest(stderr.read_bytes()),
        "semantic_repair_performed": False, "midi_generated": False,
    }
    cap = out / "capture-manifest.json"
    with cap.open("xb") as f:
        f.write((json.dumps(manifest, indent=2) + "\n").encode("utf-8"))
    rec.update({"status": status, "recorded_at_utc": manifest["recorded_at_utc"],
                "capture_manifest": str(cap), "cli_exit_status": args.exit_code})
    reg.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    return manifest


def mark_sent(args) -> dict:
    reg = Path(args.registry)
    rec = json.loads(reg.read_text(encoding="utf-8"))
    if rec.get("status") != "RESERVED_MANUAL_NOT_SENT":
        raise ValueError("solo una reserva nueva puede marcarse SENT_MANUAL")
    if digest(PAYLOAD.read_bytes()) != EXPECTED_PAYLOAD_SHA256:
        raise ValueError("el payload congelado cambió después de reservar")
    rec.update({"status": "SENT_MANUAL", "sent_marked_at_utc": now(),
                "payload_sha256": EXPECTED_PAYLOAD_SHA256})
    reg.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    return rec


def verify(args) -> dict:
    cap = Path(args.capture_manifest)
    m = json.loads(cap.read_text(encoding="utf-8"))
    errors = []
    if m.get("capture_status") != "CAPTURED": errors.append("capture_status no es CAPTURED")
    if m.get("stage") != 1 or m.get("attempt") != 1: errors.append("la captura no corresponde a Stage 1 intento 1")
    if m.get("request_id") != "XMODEL-011-CODEX-STAGE1-A1": errors.append("request_id inesperado")
    if m.get("cli_exit_status") != 0: errors.append("Codex CLI terminó con código distinto de cero")
    if m.get("payload_sha256") != EXPECTED_PAYLOAD_SHA256: errors.append("hash del payload no coincide")
    if m.get("brief_sha256") != BRIEF_SHA256: errors.append("hash del brief no coincide")
    if m.get("terminal_success_event_observed") is not True: errors.append("falta evento turn.completed")
    for path_key, hash_key in (("final_output_path", "final_output_sha256"),
                               ("cli_events_path", "cli_events_sha256"),
                               ("cli_stderr_path", "cli_stderr_sha256")):
        p = Path(m.get(path_key, ""))
        if not p.is_file(): errors.append(f"falta archivo {path_key}")
        elif digest(p.read_bytes()) != m.get(hash_key): errors.append(f"hash incorrecto: {path_key}")
    final = Path(m.get("final_output_path", ""))
    if final.is_file() and not final.stat().st_size: errors.append("respuesta final vacía")
    events_path = Path(m.get("cli_events_path", ""))
    if events_path.is_file():
        terminal, _, _ = read_events(events_path)
        if not terminal: errors.append("JSONL no contiene evento terminal turn.completed")
    registry = cap.parent.parent.parent.parent / "request-registry" / "XMODEL-011-CODEX-STAGE1-A1.json"
    if not registry.is_file():
        errors.append("falta registro exclusivo del intento")
    else:
        try:
            rr = json.loads(registry.read_text(encoding="utf-8"))
            if rr.get("status") != "CAPTURED": errors.append("registro del intento no está CAPTURED")
            if rr.get("request_id") != m.get("request_id"): errors.append("registro e manifiesto discrepan")
        except Exception:
            errors.append("registro del intento no es JSON válido")
    result = {"pass": not errors, "errors": errors, "capture_manifest": str(cap)}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("reserve"); r.add_argument("--stage", type=int, required=True); r.add_argument("--attempt", type=int, required=True); r.add_argument("--request-id", required=True); r.add_argument("--capture-dir", required=True); r.add_argument("--registry-dir", required=True)
    s = sub.add_parser("mark-sent"); s.add_argument("--registry", required=True)
    c = sub.add_parser("record"); c.add_argument("--registry", required=True); c.add_argument("--exit-code", type=int, required=True); c.add_argument("--cli-version", required=True)
    v = sub.add_parser("verify"); v.add_argument("--capture-manifest", required=True)
    a = p.parse_args()
    try:
        result = reserve(a) if a.cmd == "reserve" else mark_sent(a) if a.cmd == "mark-sent" else record(a) if a.cmd == "record" else verify(a)
        if a.cmd != "verify": print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if a.cmd != "verify" or result["pass"] else 1
    except Exception as exc:
        print(json.dumps({"pass": False, "error": f"{type(exc).__name__}: {exc}"}, ensure_ascii=False, indent=2))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
