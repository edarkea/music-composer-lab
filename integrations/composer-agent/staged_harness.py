"""Executable context assembler and deterministic gates for staged runs.

The harness may reject or retry model output, but never inserts or repairs
musical decisions. It is intentionally dependency-free (stdlib only).
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INTERFACE = ROOT / "datasets/composer-interface-v1.1"
REQUIRED = ["FORM","SECTION_ROLES","HARMONIC_FRAMEWORK","FOCAL_IDENTITY",
            "LEAD_MOTIF_BEHAVIOR","BASS_ROLE","GROOVE",
            "N3-P_PERCUSSION_ARCHITECTURE","TEXTURE","DEVELOPMENT",
            "ENERGY_TENSION_RELEASE","ENDING","CROSS_DOMAIN_CONFLICTS"]
N3 = {"FULL","MINIMAL","DELEGATED","INTENTIONALLY_ABSENT"}
# XMODEL identifiers are test metadata; only composition-example identifiers
# are forbidden in NO-EXAMPLE payloads.
FORBIDDEN_EXAMPLES = re.compile(r"SONG[-_ ]?00[1-4]\b", re.I)

def digest(data: bytes) -> str: return hashlib.sha256(data).hexdigest()
def read(path: Path) -> str: return path.read_text(encoding="utf-8-sig")

def records(stage: int):
    common = [
        ROOT / "integrations/composer-agent/system-contract-v1.1.md",
        INTERFACE / "decision-schema.yaml", INTERFACE / "guardrails.yaml",
        INTERFACE / "completion-checklist.yaml",
        INTERFACE / "knowledge/approved-composition-knowledge.yaml",
        INTERFACE / "genres/indie-dance.yaml",
        INTERFACE / "knowledge/n3-p-percussion-architecture.yaml",
    ]
    if stage == 1:
        return common + [ROOT / "integrations/composer-agent/stage-1-decision-trace-schema.yaml"]
    if stage == 2:
        return common + [ROOT / "integrations/composer-agent/stage-2-musical-material-schema.yaml"]
    return [ROOT / "integrations/composer-agent/system-contract-v1.1.md",
            INTERFACE / "songplan-v2-contract.yaml",
            ROOT / "integrations/music-engine/integration-contract.md",
            ROOT / "integrations/composer-agent/stage-3-songplan-serialization-schema.yaml"]

def assemble(stage: int, brief: Path, instruction: Path, out: Path,
             prior: Path | None = None) -> dict:
    brief, instruction, out = brief.resolve(), instruction.resolve(), out.resolve()
    prior = prior.resolve() if prior else None
    files = [brief] + records(stage) + [instruction]
    if prior: files.append(prior)
    missing = [str(p) for p in files if not p.exists()]
    if missing: raise FileNotFoundError("missing required records: " + ", ".join(missing))
    blocks = ["STAGED EXECUTION v1 — MODEL-VISIBLE PAYLOAD",
              f"STAGE: {stage}", "INTERFACE VERSION: composer-interface-v1.1",
              "CONDITION: NO-EXAMPLE", "" * 8]
    resolved = []
    for p in files:
        text = read(p)
        blocks += [f"BEGIN RECORD: {p.as_posix()}", text, f"END RECORD: {p.as_posix()}"]
        resolved.append({"path": str(p.relative_to(ROOT)), "sha256": digest(p.read_bytes())})
    payload = "\n\n".join(blocks) + "\n"
    result = preflight(payload, stage, brief, instruction, prior, resolved)
    if not result["pass"]: raise ValueError(json.dumps(result, ensure_ascii=False))
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text(payload, encoding="utf-8", newline="")
    manifest = {"payload_path": str(out.relative_to(ROOT)), "payload_sha256": digest(payload.encode()),
                "brief_sha256": digest(brief.read_bytes()), "interface_version":"composer-interface-v1.1",
                "stage": stage, "resolved_records": resolved, "preflight": result}
    (out.parent / "payload-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    return manifest

def preflight(payload: str, stage: int, brief: Path, instruction: Path,
              prior: Path | None = None, resolved=None) -> dict:
    errors=[]
    brief_text=read(brief) if brief.exists() else ""
    instruction_text=read(instruction) if instruction.exists() else ""
    if not brief.exists() or brief_text not in payload: errors.append("exact brief missing from payload")
    if not instruction.exists() or instruction_text not in payload: errors.append("stage instruction missing from payload")
    if stage > 1 and (not prior or not prior.exists() or read(prior) not in payload): errors.append("prior accepted output missing from payload")
    if FORBIDDEN_EXAMPLES.search(payload): errors.append("forbidden composition example marker present")
    required = records(stage)
    for p in required:
        if not p.exists() or read(p) not in payload: errors.append(f"required record missing from payload: {p.relative_to(ROOT)}")
    return {"pass": not errors, "stage": stage, "errors": errors,
            "resolved_record_count": len(resolved or required)}

def parse_output(path: Path):
    raw = path.read_text(encoding="utf-8-sig")
    if raw.lstrip().startswith("```"): return None, ["markdown wrapper is not valid structured output"]
    try: return json.loads(raw), []
    except Exception as e: return None, [f"output does not parse as complete JSON: {e}"]

def gate(stage: int, output: Path, trace: dict | None = None, material: dict | None = None) -> dict:
    data, errors = parse_output(output)
    if errors: return {"pass":False,"stage":stage,"errors":errors,"semantic_repair_performed":False}
    if not isinstance(data, dict): errors.append("structured output root must be object")
    if stage == 1: errors += gate_stage1(data)
    elif stage == 2: errors += gate_stage2(data, trace)
    elif stage == 3: errors += gate_stage3(data, trace, material)
    return {"pass":not errors,"stage":stage,"errors":errors,"semantic_repair_performed":False}

def can_advance(previous_gate: dict, next_stage: int) -> bool:
    """Stage progression is mechanical; a failed prior gate always blocks."""
    return bool(previous_gate.get("pass") is True and next_stage == int(previous_gate.get("stage", 0)) + 1)

def decisions(data):
    if isinstance(data.get("decisions"), list):
        return {str(x.get("decision_id", x.get("decision"))): x for x in data["decisions"] if isinstance(x,dict)}
    return {k:v for k,v in data.items() if k in REQUIRED and isinstance(v,dict)}

def gate_stage1(data):
    errors=[]; ds=decisions(data)
    for name in REQUIRED:
        d=ds.get(name)
        if not d: errors.append(f"missing mandatory decision: {name}"); continue
        if not any(k in d for k in ("selected_option","selected","selected_outcome","selected_resolution","selected_resolutions")): errors.append(f"decision unresolved: {name}")
        basis=d.get("selection_basis")
        if isinstance(basis,dict): errors.append(f"selection_basis must be declared enum: {name}")
        elif basis and basis not in {"EXPORTED_KNOWLEDGE_FILTER","ARTISTIC_PRIORITY","RANK-1_AUTHORIZED","NOT_APPLICABLE"}: errors.append(f"invalid selection_basis: {name}")
    n3=ds.get("N3-P_PERCUSSION_ARCHITECTURE") or data.get("n3_p_decision")
    if not isinstance(n3,dict): errors.append("N3-P decision missing")
    else:
        if n3.get("selected_outcome") not in N3: errors.append("N3-P selected_outcome invalid or missing")
        for k in ("decision_id","candidate_strategies","selection_basis","bass_groove_interaction","focal_hierarchy_interaction","section_behavior","development_behavior"):
            if not n3.get(k): errors.append(f"N3-P required field missing: {k}")
    text=json.dumps(data,ensure_ascii=False)
    if re.search(r"RANK[-_ ]?2",text,re.I): errors.append("unsupported RANK-2 declaration")
    if "RANK-1_AUTHORIZED" in text and "CK-CROSS-01" not in text: errors.append("RANK-1 lacks authorized CK-CROSS-01 scope")
    if re.search(r"owner\s*(selected|prefers|said|requested)",text,re.I): errors.append("unsupported Owner attribution claim")
    return errors

def gate_stage2(data, trace):
    errors=[]
    for k in ("frozen_decision_trace_hash","sections","layers","material_events","realization_notes"):
        if k not in data: errors.append(f"Stage 2 required field missing: {k}")
    if trace and data.get("frozen_decision_trace_hash") != trace.get("trace_hash"): errors.append("frozen DecisionTrace hash mismatch")
    return errors

def gate_stage3(data, trace, material):
    errors=[]; required={"schema_version","name","tempo","time_signature","tonic","mode","style","arrangement","tracks"}
    if set(data) != required: errors.append("SongPlanV2 root fields do not match exact contract")
    if data.get("schema_version") != "2.0": errors.append("SongPlanV2 schema_version must be 2.0")
    arr=data.get("arrangement")
    if not isinstance(arr,dict): errors.append("arrangement must be object")
    else:
        sections=arr.get("sections"); ha=arr.get("harmony_assignments")
        if not isinstance(sections,list): errors.append("arrangement.sections must be array")
        else:
            for i,s in enumerate(sections):
                if not isinstance(s,dict) or not {"section_id","start_bar","bar_count"} <= set(s): errors.append(f"section {i} missing section_id/start_bar/bar_count")
        if not isinstance(ha,list): errors.append("arrangement.harmony_assignments must be array")
        else:
            for i,h in enumerate(ha):
                if not isinstance(h,dict) or "harmony" not in h or not ("section_id" in h or {"start_bar","bar_count"} <= set(h)): errors.append(f"harmony assignment {i} missing address or label")
    tracks=data.get("tracks")
    if not isinstance(tracks,list): errors.append("tracks must be array")
    else:
        for i,t in enumerate(tracks):
            if not isinstance(t,dict) or not {"id","type","role","motifs","section_assignments"} <= set(t): errors.append(f"track {i} missing required fields")
            elif t.get("type") not in {"pitched","drums","percussion","effect"}: errors.append(f"track {i} invalid type")
            elif t.get("type") in {"drums","percussion"} and not {"kit_id","map_id"} <= set(t): errors.append(f"track {i} percussion requires kit_id/map_id")
    if trace and data.get("frozen_decision_trace_hash") not in (None, trace.get("trace_hash")): errors.append("serialization changed frozen trace")
    return errors

def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="cmd",required=True)
    a=sub.add_parser("assemble"); a.add_argument("--stage",type=int,choices=[1,2,3],required=True); a.add_argument("--brief",type=Path,required=True); a.add_argument("--instruction",type=Path,required=True); a.add_argument("--out",type=Path,required=True); a.add_argument("--prior",type=Path)
    g=sub.add_parser("gate"); g.add_argument("--stage",type=int,choices=[1,2,3],required=True); g.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    if args.cmd=="assemble": print(json.dumps(assemble(args.stage,args.brief,args.instruction,args.out,args.prior),ensure_ascii=False,indent=2)); return 0
    result=gate(args.stage,args.output); print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result["pass"] else 1
if __name__ == "__main__": main()
