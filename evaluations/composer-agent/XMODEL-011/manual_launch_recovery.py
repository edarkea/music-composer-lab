"""Offline bookkeeping for XMODEL-011's Owner-run CLI argument recovery.

Never starts Codex. It reserves, records and verifies files produced by the Owner.
"""
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STAGE = ROOT / "outputs/codex/stage-1"
PAYLOAD = STAGE / "payload/revision-2/attempt-1-payload.txt"
EXPECTED_PAYLOAD = "58646fd9fbef25c17b6b5cc7f846490989316f25d5084469d2b8b4cb074a423d"
OLD_ID = "XMODEL-011-CODEX-STAGE1-A1"
RECOVERY_ID = "XMODEL-011-CODEX-STAGE1-A1-LAUNCH-RECOVERY-001"
RECOVERY = STAGE / "technical-recoveries/launch-recovery-001"
CAPTURE = RECOVERY / "capture"
RECORD = RECOVERY / "request-record.json"
OLD_REG = STAGE / "request-registry" / f"{OLD_ID}.json"
OLD_CAPTURE = STAGE / "attempts/attempt-1/capture"

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def utc() -> str:
    return datetime.now(timezone.utc).isoformat()

def approval_order_is_valid(argv: list[str]) -> bool:
    """The installed CLI exposes --ask-for-approval globally, before `exec`."""
    try: return argv.index("--ask-for-approval") < argv.index("exec")
    except ValueError: return False

def recovery_cli_args(workspace: str, schema: str, final: str) -> list[str]:
    return ["--ask-for-approval", "never", "exec", "--ephemeral",
        "--ignore-user-config", "--ignore-rules", "--sandbox", "read-only",
        "--cd", workspace, "--json", "--output-schema", schema,
        "--output-last-message", final, "-"]

def historical_snapshot() -> dict:
    reg = json.loads(OLD_REG.read_text(encoding="utf-8"))
    events = OLD_CAPTURE / "cli-events.jsonl"
    err = OLD_CAPTURE / "cli-stderr.txt"
    final = OLD_CAPTURE / "final-output.txt"
    manifest = OLD_CAPTURE / "capture-manifest.json"
    if reg.get("status") != "SENT_MANUAL":
        raise ValueError("historical request registry differs from expected SENT_MANUAL")
    if events.stat().st_size != 0:
        raise ValueError("historical JSONL is not empty")
    stderr = err.read_text(encoding="utf-8", errors="replace")
    if "unexpected argument '--ask-for-approval' found" not in stderr:
        raise ValueError("historical parser diagnostic differs from expected failure")
    if final.exists() or manifest.exists():
        raise ValueError("unexpected historical final output or capture manifest exists")
    return {
        "request_id": OLD_ID,
        "classification": "CLI_ARGUMENT_PARSE_FAILURE; PRE_INFERENCE_TECHNICAL_FAILURE",
        "request_kind": "technical-launch-failure; not evaluable composer attempt",
        "model_inference_evidence": "NONE; zero-byte events, parser rejected CLI arguments before turn",
        "registry_sha256": sha(OLD_REG.read_bytes()),
        "events_sha256": sha(events.read_bytes()),
        "stderr_sha256": sha(err.read_bytes()),
        "final_output_exists": False,
        "capture_manifest_exists": False,
        "gate_run": False,
        "evaluable_attempt_count": 0,
    }

def init(args) -> dict:
    if sha(PAYLOAD.read_bytes()) != EXPECTED_PAYLOAD:
        raise ValueError("frozen payload hash mismatch")
    snapshot = historical_snapshot()
    if RECOVERY.exists() or RECORD.exists() or CAPTURE.exists():
        raise FileExistsError("recovery path already exists; do not overwrite or reuse")
    RECOVERY.mkdir(parents=True, exist_ok=False)
    record = {
        "experiment_id": "XMODEL-011", "stage": 1,
        "evaluable_attempt": 1,
        "request_id": RECOVERY_ID,
        "request_kind": "technical_launch_recovery",
        "status": "PREPARED_NOT_SENT",
        "counts_as_evaluable_attempt": False,
        "total_cli_launch_requests_before_recovery": 1,
        "total_cli_launch_requests_if_owner_sends_recovery": 2,
        "evaluable_composer_attempts_before_response_and_gate": 0,
        "payload_path": str(PAYLOAD), "payload_sha256": EXPECTED_PAYLOAD,
        "brief_sha256": "464ae4378bcb7236f0fb36da52eb65dcb03735197284e3a6899b8686d51ede0b",
        "historical_failed_launch": snapshot,
        "cli_option_order": "codex --ask-for-approval never exec ...",
        "cli_version": "codex-cli 0.154.0-alpha.6.2",
        "model_requested": None,
        "created_at_utc": utc(),
    }
    RECORD.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return record

def mark_sent(args) -> dict:
    r = json.loads(RECORD.read_text(encoding="utf-8"))
    if r.get("request_id") != RECOVERY_ID or r.get("status") != "PREPARED_NOT_SENT":
        raise ValueError("recovery is not a fresh prepared request")
    if sha(PAYLOAD.read_bytes()) != EXPECTED_PAYLOAD:
        raise ValueError("frozen payload changed")
    historical_snapshot()  # reassert historical evidence remains intact before send
    if CAPTURE.exists():
        raise FileExistsError("recovery capture path already exists")
    CAPTURE.mkdir(parents=True, exist_ok=False)
    r.update({"status": "SENT_MANUAL", "sent_marked_at_utc": utc()})
    RECORD.write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return r

def record(args) -> dict:
    r = json.loads(RECORD.read_text(encoding="utf-8"))
    if r.get("status") != "SENT_MANUAL":
        raise ValueError("recovery request is not marked sent or already recorded")
    ev, err, final = CAPTURE/"cli-events.jsonl", CAPTURE/"cli-stderr.txt", CAPTURE/"final-output.txt"
    for p in (ev, err):
        if not p.is_file(): raise FileNotFoundError(f"required transport capture absent: {p}")
    ev_bytes = ev.read_bytes(); err_bytes = err.read_bytes()
    final_exists = final.is_file(); final_bytes = final.read_bytes() if final_exists else b""
    events = []
    for line in ev_bytes.splitlines():
        try:
            e = json.loads(line)
            if isinstance(e, dict): events.append(e)
        except Exception: pass
    terminal = any(e.get("type") == "turn.completed" for e in events)
    response_started = any(e.get("type") in ("turn.started", "item.started", "item.completed", "turn.completed") for e in events)
    parser_reject = len(ev_bytes) == 0 and "unexpected argument '--ask-for-approval' found" in err_bytes.decode("utf-8", "replace")
    complete = args.exit_code == 0 and terminal and final_exists and bool(final_bytes)
    if parser_reject:
        status, classification = "CLI_ARGUMENT_PARSE_FAILURE", "PRE_INFERENCE_TECHNICAL_FAILURE"
    elif complete:
        status, classification = "COMPLETE_RESPONSE_READY_FOR_GATE", "TECHNICAL_RECOVERY_COMPLETE"
    else:
        status, classification = "CLI_FAILED_OR_INCOMPLETE", "TECHNICAL_FAILURE; inference status recorded from available events"
    capture = {
        "capture_status": "CAPTURED" if complete else status,
        "experiment_id": "XMODEL-011", "stage": 1, "attempt": 1,
        "request_id": RECOVERY_ID, "request_kind": "technical_launch_recovery",
        "classification": classification, "cli_exit_status": args.exit_code,
        "model_requested": None, "model_reported": next((e.get("server_model") for e in events if isinstance(e.get("server_model"), str)), None),
        "inference_event_evidence": response_started,
        "terminal_success_event_observed": terminal,
        "payload_path": str(PAYLOAD), "payload_sha256": sha(PAYLOAD.read_bytes()),
        "brief_sha256": r["brief_sha256"],
        "final_output_path": str(final) if final_exists else None,
        "final_output_sha256": sha(final_bytes) if final_exists else None,
        "cli_events_path": str(ev), "cli_events_sha256": sha(ev_bytes),
        "cli_stderr_path": str(err), "cli_stderr_sha256": sha(err_bytes),
        "historical_launch_unchanged": historical_snapshot(),
        "evaluable_attempt_count_before_gate": 0,
        "evaluable_attempt_candidate": bool(complete),
        "semantic_repair_performed": False, "midi_generated": False,
        "recorded_at_utc": utc(),
    }
    manifest = CAPTURE/"capture-manifest.json"
    with manifest.open("xb") as f: f.write((json.dumps(capture, ensure_ascii=False, indent=2)+"\n").encode("utf-8"))
    r.update({"status": status, "classification": classification, "cli_exit_status": args.exit_code,
              "capture_manifest": str(manifest), "recorded_at_utc": capture["recorded_at_utc"]})
    RECORD.write_text(json.dumps(r, ensure_ascii=False, indent=2)+"\n",encoding="utf-8")
    return capture

def verify(args) -> dict:
    m = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    errors=[]
    if m.get("capture_status") != "CAPTURED": errors.append("capture is not complete")
    if m.get("request_id") != RECOVERY_ID: errors.append("unexpected recovery request ID")
    if m.get("stage") != 1 or m.get("attempt") != 1: errors.append("wrong stage/attempt")
    if m.get("payload_sha256") != EXPECTED_PAYLOAD: errors.append("payload hash mismatch")
    if m.get("cli_exit_status") != 0 or not m.get("terminal_success_event_observed"): errors.append("missing successful exit/terminal event")
    for pk,hk in (("final_output_path","final_output_sha256"),("cli_events_path","cli_events_sha256"),("cli_stderr_path","cli_stderr_sha256")):
        p=Path(m.get(pk) or "")
        if not p.is_file(): errors.append(f"missing {pk}")
        elif sha(p.read_bytes()) != m.get(hk): errors.append(f"hash mismatch: {pk}")
    fp=Path(m.get("final_output_path") or "")
    if fp.is_file() and fp.stat().st_size == 0: errors.append("empty final response")
    if m.get("evaluable_attempt_count_before_gate") != 0: errors.append("evaluable counter must remain zero before gate")
    result={"pass":not errors,"errors":errors,"manifest":str(args.manifest)}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result

def main() -> int:
    p=argparse.ArgumentParser(); s=p.add_subparsers(dest="cmd",required=True)
    s.add_parser("prepare")
    q=s.add_parser("mark-sent"); q.add_argument("--request-record",default=str(RECORD))
    q=s.add_parser("record"); q.add_argument("--exit-code",type=int,required=True)
    q=s.add_parser("verify"); q.add_argument("--manifest",required=True)
    a=p.parse_args()
    try:
        result=init(a) if a.cmd=="prepare" else mark_sent(a) if a.cmd=="mark-sent" else record(a) if a.cmd=="record" else verify(a)
        if a.cmd!="verify": print(json.dumps(result,ensure_ascii=False,indent=2))
        return 0 if a.cmd!="verify" or result["pass"] else 1
    except Exception as e:
        print(json.dumps({"pass":False,"error":f"{type(e).__name__}: {e}"},ensure_ascii=False,indent=2)); return 2

if __name__ == "__main__": raise SystemExit(main())
