"""Offline-testable, non-musical Codex CLI capture wrapper for XMODEL-011.

The wrapper never materializes MIDI and never edits composer output. A successful
CLI process is captured byte-for-byte; gate acceptance is a separate operation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time
import base64
from datetime import datetime, timezone


ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[2]
MAX_ATTEMPTS = 3


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def exclusive_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as f:
        f.write(data)


def has_terminal_success_event(data: bytes) -> bool:
    """Fail closed unless CLI JSONL proves the turn completed."""
    for line in data.decode("utf-8", errors="replace").splitlines():
        try:
            event = json.loads(line)
        except Exception:
            continue
        if isinstance(event, dict) and event.get("type") == "turn.completed":
            return True
    return False


def model_from_events(data: bytes) -> str | None:
    """Return a literal model identifier only if the CLI event supplies one."""
    for line in data.decode("utf-8", errors="replace").splitlines():
        try:
            event=json.loads(line)
        except Exception:
            continue
        if not isinstance(event,dict):
            continue
        for key in ("server_model",):
            value=event.get(key)
            if isinstance(value,str) and value.strip():
                return value.strip()
    return None


def _manifest_for_input(input_path: Path) -> dict:
    path = input_path.with_name("payload-manifest.json")
    if not path.is_file():
        raise ValueError(f"payload manifest missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def isolation_probe_script(repo_root: Path, historical_file: Path,
                           codex_home: Path, workspace: Path,
                           schema: Path) -> str:
    """Create a read-only probe executed by the same Windows sandbox identity."""
    values = [repo_root, historical_file, codex_home, workspace, schema]
    encoded = [str(p).replace("'", "''") for p in values]
    return r'''$ErrorActionPreference = 'Stop'
function Read-Probe($Path) {
  try { Get-Content -LiteralPath $Path -TotalCount 1 -ErrorAction Stop | Out-Null; return 'READABLE' }
  catch [System.UnauthorizedAccessException] { return 'DENIED' }
  catch [System.Security.SecurityException] { return 'DENIED' }
  catch { return 'ERROR:' + $_.Exception.GetType().Name }
}
function List-Probe($Path) {
  try { Get-ChildItem -LiteralPath $Path -ErrorAction Stop | Out-Null; return 'READABLE' }
  catch [System.UnauthorizedAccessException] { return 'DENIED' }
  catch [System.Security.SecurityException] { return 'DENIED' }
  catch { return 'ERROR:' + $_.Exception.GetType().Name }
}
$repo = ''' + "'" + encoded[0] + "'" + r'''
$historic = ''' + "'" + encoded[1] + "'" + r'''
$codexHome = ''' + "'" + encoded[2] + "'" + r'''
$workspace = ''' + "'" + encoded[3] + "'" + r'''
$schema = ''' + "'" + encoded[4] + "'" + r'''
$identity = (whoami).Trim().ToLowerInvariant()
$repoResult = List-Probe $repo
$historicalResult = Read-Probe $historic
$codexResult = List-Probe $codexHome
$markerResult = Read-Probe (Join-Path $workspace '.xmodel011-workspace-marker')
$schemaResult = Read-Probe $schema
$schemaHash = if ($schemaResult -eq 'READABLE') { (Get-FileHash -LiteralPath $schema -Algorithm SHA256).Hash.ToLowerInvariant() } else { '' }
Write-Output ('IDENTITY=' + $identity)
Write-Output ('REPO=' + $repoResult)
Write-Output ('HISTORICAL=' + $historicalResult)
Write-Output ('CODEX_HOME=' + $codexResult)
Write-Output ('WORKSPACE=' + $markerResult)
Write-Output ('SCHEMA=' + $schemaResult)
Write-Output ('SCHEMA_SHA256=' + $schemaHash)
'''


def isolation_probe_failures(fields: dict, expected_schema_hash: str) -> list[str]:
    expected = {
        "REPO": "DENIED", "HISTORICAL": "DENIED", "CODEX_HOME": "DENIED",
        "WORKSPACE": "READABLE", "SCHEMA": "READABLE",
        "SCHEMA_SHA256": expected_schema_hash,
    }
    failures = [f"{key}: expected {value!r}, got {fields.get(key)!r}"
                for key, value in expected.items() if fields.get(key) != value]
    if not fields.get("IDENTITY", "").endswith(("\\codexsandboxoffline", "\\codexsandboxonline")):
        failures.append(f"unexpected restricted identity: {fields.get('IDENTITY')!r}")
    return failures


def verify_host_parent_history_isolation(repo_root: Path = REPO_ROOT) -> dict:
    """Require the codex exec parent itself to lack the historical XMODEL tree."""
    historical_root = repo_root / "evaluations/composer-agent/XMODEL-010"
    try:
        entries = list(historical_root.iterdir())
    except FileNotFoundError:
        return {"status": "PASS", "historical_tree": "ABSENT"}
    except PermissionError:
        return {"status": "PASS", "historical_tree": "ACCESS_DENIED"}
    if entries:
        raise RuntimeError("full-process isolation failed: the codex exec parent can enumerate XMODEL-010")
    return {"status": "PASS", "historical_tree": "EMPTY"}


def verify_tool_sandbox_isolation(cli_path: str, workspace: Path,
                                  schema: Path) -> dict:
    """Fail closed unless the restricted Windows tool sandbox cannot read history or secrets."""
    repo_root = REPO_ROOT.resolve(strict=True)
    codex_home = (Path.home() / ".codex").resolve(strict=True)
    historical = repo_root / "evaluations/composer-agent/XMODEL-010/run-manifest.yaml"
    if not historical.is_file():
        raise ValueError(f"historical isolation sentinel missing: {historical}")
    script = isolation_probe_script(repo_root, historical, codex_home,
                                    workspace.resolve(strict=True), schema.resolve(strict=True))
    encoded = base64.b64encode(script.encode("utf-16le")).decode("ascii")
    cmd = [cli_path, "sandbox", "--permission-profile", ":read-only",
           "powershell.exe", "-NoLogo", "-NoProfile",
           "-EncodedCommand", encoded]
    result = subprocess.run(cmd, capture_output=True, check=False, text=True,
                            timeout=30, cwd=str(workspace))
    if result.returncode != 0:
        raise RuntimeError("restricted Windows sandbox probe failed: " +
                           (result.stderr.strip() or result.stdout.strip()))
    fields = {}
    for line in result.stdout.splitlines():
        if "=" in line:
            key, value = line.strip().split("=", 1)
            fields[key] = value
    failures = isolation_probe_failures(fields, sha256(schema.read_bytes()))
    report = {"status": "PASS" if not failures else "FAIL",
              "identity": fields.get("IDENTITY"), "checks": fields,
              "errors": failures, "model_invoked": False}
    if failures:
        raise RuntimeError("filesystem isolation preflight failed: " + json.dumps(report))
    return report


def validate_request(*, experiment_id: str, stage: int, attempt: int,
                     request_id: str, request_kind: str, input_path: Path,
                     output_dir: Path, registry_dir: Path) -> dict:
    if experiment_id != "XMODEL-011":
        raise ValueError("experiment_id must be XMODEL-011")
    if stage not in (1, 2, 3):
        raise ValueError("stage must be 1, 2, or 3")
    if not 1 <= attempt <= MAX_ATTEMPTS:
        raise ValueError(f"attempt must be between 1 and {MAX_ATTEMPTS}")
    if request_kind != "evaluable_attempt":
        raise ValueError("request_kind must be evaluable_attempt")
    if not request_id.startswith(f"XMODEL-011-CODEX-STAGE{stage}-A{attempt}"):
        raise ValueError("request_id does not match experiment/stage/attempt")
    input_path = input_path.resolve(strict=True)
    output_dir = output_dir.resolve()
    registry_dir = registry_dir.resolve()
    if output_dir.exists() and any(output_dir.iterdir()):
        raise ValueError(f"output directory is not empty: {output_dir}")
    pm = _manifest_for_input(input_path)
    prompt = input_path.read_bytes()
    if sha256(prompt) != pm.get("payload_sha256"):
        raise ValueError("payload hash differs from its manifest")
    if pm.get("stage") != stage:
        raise ValueError("payload stage does not match request stage")
    if pm.get("attempt") != attempt:
        raise ValueError("payload attempt does not match request attempt")
    if pm.get("brief_sha256") != "464ae4378bcb7236f0fb36da52eb65dcb03735197284e3a6899b8686d51ede0b":
        raise ValueError("brief hash differs from frozen XMODEL-011 brief")
    if not pm.get("preflight", {}).get("pass"):
        raise ValueError("payload preflight is not PASS")
    if attempt > 1:
        if not pm.get("retry_of_payload_sha256") or not pm.get("literal_gate_diagnostic"):
            raise ValueError("retry payload must declare its original payload hash and literal previous gate diagnostic")
        original_path=Path(pm.get("original_payload_path", ""))
        original=original_path.read_bytes()
        if sha256(original)!=pm.get("retry_of_payload_sha256") or not prompt.startswith(original):
            raise ValueError("retry payload is not derived from the original frozen stage payload")
        if pm.get("preflight", {}).get("musical_suggestion_inserted") is not False:
            raise ValueError("retry preflight does not establish zero musical suggestions")
    registry_dir.mkdir(parents=True, exist_ok=True)
    registry_file = registry_dir / f"{request_id}.json"
    record = {
        "experiment_id": experiment_id, "request_id": request_id,
        "request_kind": request_kind, "stage": stage, "attempt": attempt,
        "payload_path": str(input_path), "payload_sha256": sha256(prompt),
        "status": "RESERVED_NOT_SENT", "created_at_utc": utcnow(),
    }
    exclusive_write(registry_file, (json.dumps(record, indent=2) + "\n").encode())
    return {"payload": prompt, "manifest": pm, "registry_file": registry_file,
            "record": record, "output_dir": output_dir}


def execute(args) -> dict:
    parent_isolation = verify_host_parent_history_isolation()
    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    registry_dir = Path(args.request_registry)
    cli = args.codex or shutil.which("codex")
    if not cli:
        raise RuntimeError("Codex CLI executable not found")
    cli_path = str(Path(cli).resolve()) if Path(cli).exists() else cli
    version = subprocess.run([cli_path, "--version"], capture_output=True,
                             check=False, timeout=20, text=True)
    if version.returncode != 0:
        raise RuntimeError("Codex CLI version query failed")
    stage_dir = output_dir.parent.parent
    stage_schema = ROOT / "model-visible" / f"stage-{args.stage}" / "output-schema.json"
    sandbox_cwd = Path(args.execution_workspace).resolve()
    if sandbox_cwd == ROOT or ROOT in sandbox_cwd.parents or sandbox_cwd in ROOT.parents:
        raise ValueError("execution workspace must be outside the repository tree")
    # CLI output schema is a transport/serialization constraint only. It does not
    # inject a musical decision. CLI logs and the final answer remain separate.
    sandbox_cwd.mkdir(parents=True, exist_ok=False)
    exclusive_write(sandbox_cwd / ".xmodel011-workspace-marker",
                    b"XMODEL-011 isolated per-request working directory.\n")
    isolated_schema = sandbox_cwd / "output-schema.json"
    exclusive_write(isolated_schema, stage_schema.read_bytes())
    try:
        isolation = verify_tool_sandbox_isolation(cli_path, sandbox_cwd, isolated_schema)
    except Exception:
        isolated_schema.unlink(missing_ok=True)
        (sandbox_cwd / ".xmodel011-workspace-marker").unlink(missing_ok=True)
        if sandbox_cwd.exists() and not any(sandbox_cwd.iterdir()):
            sandbox_cwd.rmdir()
        raise
    req = validate_request(experiment_id=args.experiment_id, stage=args.stage,
        attempt=args.attempt, request_id=args.request_id,
        request_kind=args.request_kind, input_path=input_path,
        output_dir=output_dir, registry_dir=registry_dir)
    final_path = output_dir / "final-output.txt"
    stdout_path = output_dir / "cli-events.jsonl"
    stderr_path = output_dir / "cli-stderr.txt"
    capture_path = output_dir / "capture-manifest.json"
    for path in (final_path, stdout_path, stderr_path, capture_path):
        if path.exists():
            raise FileExistsError(f"capture path already exists: {path}")
    output_dir.mkdir(parents=True, exist_ok=False)
    started = utcnow()
    start_perf = time.monotonic()
    rec = req["record"]
    rec.update({"status": "SENT", "started_at_utc": started,
                "codex_executable": cli_path, "codex_version": version.stdout.strip(),
                "model_requested": args.model, "sandbox": "read-only",
                "tool_sandbox_preflight": isolation,
                "host_parent_isolation": parent_isolation,
                "working_directory": str(sandbox_cwd)})
    req["registry_file"].write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    cmd = [cli_path, "exec", "--ephemeral", "--ignore-user-config", "--ignore-rules",
           "--sandbox", "read-only", "--ask-for-approval", "never", "--cd", str(sandbox_cwd),
           "--json", "--output-schema", str(isolated_schema), "--output-last-message",
           str(final_path)]
    if args.model:
        cmd.extend(["--model", args.model])
    cmd.append("-")
    timed_out = False
    try:
        result = subprocess.run(cmd, input=req["payload"], capture_output=True,
                                timeout=args.timeout, check=False, cwd=str(sandbox_cwd))
        rc = result.returncode
        stdout = result.stdout
        stderr = result.stderr
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        rc = None
        stdout = exc.stdout or b""
        stderr = exc.stderr or b""
    ended = utcnow()
    elapsed = round(time.monotonic() - start_perf, 3)
    exclusive_write(stdout_path, stdout if isinstance(stdout, bytes) else stdout.encode())
    exclusive_write(stderr_path, stderr if isinstance(stderr, bytes) else stderr.encode())
    final = final_path.read_bytes() if final_path.is_file() else b""
    terminal_success = has_terminal_success_event(stdout if isinstance(stdout,bytes) else stdout.encode())
    model_reported = model_from_events(stdout if isinstance(stdout,bytes) else stdout.encode())
    status = "CAPTURED" if (not timed_out and rc == 0 and final and terminal_success) else "CLI_FAILED_OR_INCOMPLETE"
    schema_bytes = stage_schema.read_bytes()
    metadata = {"capture_status": status, "experiment_id": args.experiment_id,
        "request_id": args.request_id, "request_kind": args.request_kind,
        "stage": args.stage, "attempt": args.attempt, "started_at_utc": started,
        "ended_at_utc": ended, "elapsed_seconds": elapsed,
        "codex_executable": cli_path, "codex_version": version.stdout.strip(),
        "model_requested": args.model, "model_reported": model_reported,
        "tool_sandbox_preflight": isolation,
        "host_parent_isolation": parent_isolation,
        "model_reported_note": None if model_reported else "No literal model identifier was found in CLI JSONL.",
        "payload_path": str(input_path.resolve()), "payload_sha256": sha256(req["payload"]),
        "brief_sha256": req["manifest"]["brief_sha256"],
        "cli_exit_status": rc, "timed_out": timed_out,
        "terminal_success_event_observed": terminal_success,
        "output_schema_path": str(isolated_schema),
        "output_schema_sha256": sha256(schema_bytes),
        "invocation_arguments": cmd,
        "final_output_path": str(final_path) if final else None,
        "final_output_sha256": sha256(final) if final else None,
        "cli_events_sha256": sha256(stdout if isinstance(stdout,bytes) else stdout.encode()),
        "cli_stderr_sha256": sha256(stderr if isinstance(stderr,bytes) else stderr.encode()),
        "semantic_repair_performed": False, "midi_generated": False}
    exclusive_write(capture_path, (json.dumps(metadata, indent=2) + "\n").encode())
    rec.update({"status": status, "ended_at_utc": ended, "capture_manifest": str(capture_path),
                "cli_exit_status": rc, "final_output_sha256": metadata["final_output_sha256"]})
    req["registry_file"].write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    return metadata


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--experiment-id", required=True)
    p.add_argument("--stage", type=int, choices=(1,2,3), required=True)
    p.add_argument("--attempt", type=int, required=True)
    p.add_argument("--request-id", required=True)
    p.add_argument("--request-kind", default="evaluable_attempt")
    p.add_argument("--input", required=True)
    p.add_argument("--output-dir", required=True)
    p.add_argument("--request-registry", required=True)
    p.add_argument("--execution-workspace", required=True)
    p.add_argument("--codex")
    p.add_argument("--model")
    p.add_argument("--timeout", type=int, default=21600)
    args = p.parse_args()
    try:
        result = execute(args)
        print(json.dumps(result, indent=2))
        return 0 if result["capture_status"] == "CAPTURED" else 2
    except Exception as exc:
        print(json.dumps({"capture_status":"NOT_SENT_OR_PREFLIGHT_FAILED",
                          "error":f"{type(exc).__name__}: {exc}"}, indent=2))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
