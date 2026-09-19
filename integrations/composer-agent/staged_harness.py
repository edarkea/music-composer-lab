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
HOST_CONFIG = ROOT / "integrations/music-engine/host-config.yaml"

class JSONObject(dict):
    """JSON object retaining source pairs so duplicate keys remain observable."""
    def __init__(self, pairs):
        super().__init__(pairs)
        self.pairs = pairs

def _json_object_hook(pairs): return JSONObject(pairs)

def _duplicate_paths(value, path="$", out=None):
    out = [] if out is None else out
    if isinstance(value, JSONObject):
        seen = {}
        for key, child in value.pairs:
            seen[key] = seen.get(key, 0) + 1
            if seen[key] > 1:
                out.append(f"{path}.{key} (occurrence {seen[key]})")
            _duplicate_paths(child, f"{path}.{key}", out)
    elif isinstance(value, list):
        for i, child in enumerate(value): _duplicate_paths(child, f"{path}[{i}]", out)
    return out

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
            ROOT / "integrations/composer-agent/stage-3-songplan-serialization-schema.yaml",
            HOST_CONFIG,
            ROOT / "integrations/music-engine/host-maps/song001_r1_steven_slate_map.yaml"]

def assemble(stage: int, brief: Path, instruction: Path, out: Path,
             prior: Path | None = None, extras: list[Path] | None = None) -> dict:
    brief, instruction, out = brief.resolve(), instruction.resolve(), out.resolve()
    prior = prior.resolve() if prior else None
    extras = [p.resolve() for p in (extras or [])]
    files = [brief] + records(stage) + [instruction]
    files += extras
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
    result = preflight(payload, stage, brief, instruction, prior, resolved, extras)
    if not result["pass"]: raise ValueError(json.dumps(result, ensure_ascii=False))
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text(payload, encoding="utf-8", newline="")
    manifest = {"payload_path": str(out.relative_to(ROOT)), "payload_sha256": digest(payload.encode()),
                "brief_sha256": digest(brief.read_bytes()), "interface_version":"composer-interface-v1.1",
                "stage": stage, "resolved_records": resolved, "preflight": result}
    (out.parent / "payload-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    return manifest

def preflight(payload: str, stage: int, brief: Path, instruction: Path,
              prior: Path | None = None, resolved=None, extras: list[Path] | None = None) -> dict:
    errors=[]
    brief_text=read(brief) if brief.exists() else ""
    instruction_text=read(instruction) if instruction.exists() else ""
    if not brief.exists() or brief_text not in payload: errors.append("exact brief missing from payload")
    if not instruction.exists() or instruction_text not in payload: errors.append("stage instruction missing from payload")
    if stage > 1 and (not prior or not prior.exists() or read(prior) not in payload): errors.append("prior accepted output missing from payload")
    if FORBIDDEN_EXAMPLES.search(payload): errors.append("forbidden composition example marker present")
    required = records(stage)
    required += [p.resolve() for p in (extras or [])]
    for p in required:
        if not p.exists() or read(p) not in payload: errors.append(f"required record missing from payload: {p.relative_to(ROOT)}")
    return {"pass": not errors, "stage": stage, "errors": errors,
            "resolved_record_count": len(resolved or required)}

def build_retry_payload(original_payload: Path, diagnostics: list[str], out: Path) -> dict:
    """Re-send complete original context plus diagnostics, without raw output."""
    original = original_payload.read_text(encoding="utf-8-sig")
    diag = "\n".join(["DETERMINISTIC GATE DIAGNOSTICS — RETRY", *diagnostics])
    payload = original.rstrip() + "\n\n" + diag + "\n"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(payload, encoding="utf-8", newline="")
    result = {"payload_path": str(out), "payload_sha256": digest(payload.encode()),
              "original_payload_sha256": digest(original.encode()),
              "previous_raw_output_embedded": False, "diagnostics": diagnostics}
    (out.parent / "retry-payload-manifest.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    return result

def parse_output(path: Path):
    raw = path.read_text(encoding="utf-8-sig")
    serialization = "Return exactly one raw JSON object. No Markdown, no code fences, no prose before or after JSON."
    if raw.lstrip().startswith("```"): return None, ["markdown wrapper is not valid structured output", serialization]
    try:
        data = json.loads(raw, object_pairs_hook=_json_object_hook)
        duplicates = _duplicate_paths(data)
        if duplicates:
            return None, [f"duplicate JSON object key at {p}" for p in duplicates] + [serialization]
        return data, []
    except Exception as e: return None, [f"output does not parse as complete JSON: {e}", serialization]

def _load_engine_api():
    from music_engine.songplan.v2.codec import song_plan_v2_from_dict
    from music_engine.songplan.v2.validation import validate_song_plan_v2
    from music_engine.songplan.percussion import (load_drum_external_map,
        load_percussion_map, PercussionInstrument, PercussionSoundingArticulation,
        PercussionKit)
    return song_plan_v2_from_dict, validate_song_plan_v2, load_drum_external_map, load_percussion_map, PercussionInstrument, PercussionSoundingArticulation, PercussionKit

def _host_path(value):
    p = Path(value)
    return p if p.is_absolute() else ROOT / p

def validate_host_configuration(plan, host_config: Path | None = None):
    """Validate only host mappings; never change the plan or invent identifiers."""
    try:
        _, _, load_drum, load_perc, PercussionInstrument, PercussionArticulation, PercussionKit = _load_engine_api()
    except Exception as exc:
        return {"status":"RUNTIME_FAILURE", "category":"engine_dependency_failure", "message":str(exc)}
    cfg_path = (host_config or HOST_CONFIG).resolve()
    if not cfg_path.exists():
        return {"status":"HOST_CONFIGURATION_INVALID", "category":"host_configuration_failure", "message":f"host config missing: {cfg_path}"}
    try:
        import yaml
        cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        return {"status":"HOST_CONFIGURATION_INVALID", "category":"host_configuration_failure", "message":f"host config unreadable: {exc}"}
    drum_cfg = cfg.get("drums") or {}
    perc_cfg = cfg.get("percussion") or {}
    for track in plan.tracks:
        typ = getattr(track.type, "value", track.type)
        if typ == "drums":
            events = [e for m in track.motifs for e in m.events]
            if not events: continue
            map_id = drum_cfg.get("map_id")
            map_dir = drum_cfg.get("map_dir")
            if not map_id or not map_dir:
                return {"status":"HOST_CONFIGURATION_INVALID", "category":"host_configuration_failure", "message":f"drums track '{track.id}' requires approved drum map configuration"}
            path = _host_path(map_dir) / f"{map_id}.yaml"
            if not path.exists(): path = _host_path(map_dir) / f"{map_id}.json"
            try: mapping = load_drum(path)
            except Exception as exc:
                return {"status":"HOST_CONFIGURATION_INVALID", "category":"host_configuration_failure", "message":f"invalid DrumExternalMap '{map_id}': {exc}"}
            missing = sorted({e.drum_voice.id for e in events if mapping.pitch_for(e.drum_voice.id) is None})
            if missing:
                return {"status":"HOST_CONFIGURATION_INVALID", "category":"host_configuration_failure", "message":f"DrumExternalMap '{map_id}' lacks voices: {', '.join(missing)}"}
        elif typ == "percussion":
            map_id = track.map_id
            map_dir = perc_cfg.get("map_dir")
            if not map_dir:
                return {"status":"HOST_CONFIGURATION_INVALID", "category":"host_configuration_failure", "message":f"percussion track '{track.id}' map_id '{map_id}' has no approved map directory"}
            path = _host_path(map_dir) / f"{map_id}.yaml"
            if not path.exists(): path = _host_path(map_dir) / f"{map_id}.json"
            try: mapping = load_perc(path)
            except Exception as exc:
                return {"status":"HOST_CONFIGURATION_INVALID", "category":"host_configuration_failure", "message":f"invalid PercussionMap '{map_id}': {exc}"}
            pairs = {(e.instrument.id, e.sounding_articulation.id) for m in track.motifs for e in m.events}
            unresolved = [f"{i}.{a}" for i, a in sorted(pairs) if mapping.pitch_for(PercussionInstrument(i), PercussionArticulation(a)) is None]
            if unresolved:
                return {"status":"HOST_CONFIGURATION_INVALID", "category":"host_configuration_failure", "message":f"PercussionMap '{map_id}' unresolved: {', '.join(unresolved)}"}
    return {"status":"PASS", "category":"host_configuration", "message":"approved host mappings resolved"}

def validate_with_engine(data, host_config: Path | None = None):
    """Run engine parse/validation only; never materialize or write MIDI."""
    try:
        song_plan_v2_from_dict, validate_song_plan_v2, *_ = _load_engine_api()
    except Exception as exc:
        return {"status":"BLOCK", "category":"runtime_dependency_failure", "message":str(exc), "engine_invoked":False}
    try:
        plan = song_plan_v2_from_dict(data)
    except Exception as exc:
        return {"status":"FAIL", "category":"invalid_songplan_structure", "message":str(exc), "engine_invoked":True}
    result = validate_song_plan_v2(plan)
    if not result.valid:
        return {"status":"FAIL", "category":"musical_semantic_validation_failure", "message":"; ".join(f"{x.code}: {x.path}: {x.message}" for x in result.issues), "engine_invoked":True}
    host = validate_host_configuration(plan, host_config)
    if host["status"] != "PASS": return {**host, "engine_invoked":True}
    return {"status":"PASS", "category":"engine_songplan_validation", "message":"SongPlanV2 and host configuration valid; no MIDI materialized", "engine_invoked":True}

def gate(stage: int, output: Path, trace: dict | None = None, material: dict | None = None,
         host_config: Path | None = None) -> dict:
    data, errors = parse_output(output)
    if errors: return {"pass":False,"stage":stage,"category":"serialization_failure","errors":errors,"semantic_repair_performed":False}
    if not isinstance(data, dict): errors.append("structured output root must be object")
    if stage == 1: errors += gate_stage1(data)
    elif stage == 2: errors += gate_stage2(data, trace)
    elif stage == 3: errors += gate_stage3(data, trace, material)
    result = {"pass":not errors,"stage":stage,"category":"contract_failure" if errors else "contract_validation","errors":errors,"semantic_repair_performed":False}
    if stage == 3 and not errors:
        engine = validate_with_engine(data, host_config)
        result["engine_validation"] = engine
        result["category"] = engine["category"]
        if engine["status"] != "PASS":
            result["pass"] = False
            result["errors"].append(f"engine validation {engine['status']}: {engine['category']}: {engine['message']}")
    return result

def can_advance(previous_gate: dict, next_stage: int) -> bool:
    """Stage progression is mechanical; a failed prior gate always blocks."""
    return bool(previous_gate.get("pass") is True and next_stage == int(previous_gate.get("stage", 0)) + 1)

def decisions(data):
    if isinstance(data.get("decision_trace"), list):
        return {str(x.get("decision_id", x.get("decision"))): x for x in data["decision_trace"] if isinstance(x,dict)}
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
        nested = n3.get("selected_option") if isinstance(n3.get("selected_option"), dict) else {}
        for field in ("selected_outcome","candidate_strategies","bass_groove_interaction","focal_hierarchy_interaction","section_behavior","development_behavior"):
            if field in nested:
                errors.append(f"N3-P field path invalid: expected decision_trace[i].{field}; found decision_trace[i].selected_option.{field}")
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
    required=("frozen_decision_trace_hash","sections","layers","material_events","realization_notes")
    for k in required:
        if k not in data: errors.append(f"missing required field: $.{k}")
    if trace and data.get("frozen_decision_trace_hash") != trace.get("trace_hash"): errors.append("frozen DecisionTrace hash mismatch: $.frozen_decision_trace_hash")
    sections=data.get("sections")
    if sections is not None:
        if not isinstance(sections,list): errors.append("invalid type: $.sections must be array")
        else:
            for i,s in enumerate(sections):
                if not isinstance(s,dict): errors.append(f"invalid type: $.sections[{i}] must be object"); continue
                for k in ("section_id","start_bar","bar_count","decision_references"):
                    if k not in s: errors.append(f"missing required field: $.sections[{i}].{k}")
                if "start_bar" in s and (not isinstance(s["start_bar"],int) or isinstance(s["start_bar"],bool)): errors.append(f"invalid type: $.sections[{i}].start_bar")
                if "bar_count" in s and (not isinstance(s["bar_count"],int) or isinstance(s["bar_count"],bool)): errors.append(f"invalid type: $.sections[{i}].bar_count")
    layers=data.get("layers")
    if layers is not None:
        if not isinstance(layers,list): errors.append("invalid type: $.layers must be array")
        else:
            allowed={"pitched","drums","percussion","effect","texture"}
            for i,l in enumerate(layers):
                if not isinstance(l,dict): errors.append(f"invalid type: $.layers[{i}] must be object"); continue
                for k in ("layer_id","type","role","section_assignments"):
                    if k not in l: errors.append(f"missing required field: $.layers[{i}].{k}")
                if l.get("type") is not None and l.get("type") not in allowed: errors.append(f"invalid enum: $.layers[{i}].type")
                if "section_assignments" in l and not isinstance(l["section_assignments"],list): errors.append(f"invalid type: $.layers[{i}].section_assignments")
    events=data.get("material_events")
    if events is not None and not isinstance(events,(dict,list)): errors.append("invalid type: $.material_events must be object or array")
    if "realization_notes" in data and not isinstance(data["realization_notes"],(dict,list,str)): errors.append("invalid type: $.realization_notes")
    return errors

def gate_stage3(data, trace, material):
    errors=[]; required={"schema_version","name","tempo","time_signature","tonic","mode","style","arrangement","tracks"}
    if set(data) != required: errors.append("SongPlanV2 root fields do not match exact contract")
    if data.get("schema_version") != "2.0": errors.append("SongPlanV2 schema_version must be 2.0")
    for field in ("name","tonic","style"):
        if field in data and (not isinstance(data[field],str) or not data[field]): errors.append(f"invalid value: $.{field}")
    if "tempo" in data and (not isinstance(data["tempo"],(int,float)) or isinstance(data["tempo"],bool) or data["tempo"] <= 0): errors.append("invalid value: $.tempo")
    if data.get("mode") not in {"ionian","dorian","phrygian","lydian","mixolydian","aeolian","locrian"}: errors.append("invalid enum: $.mode")
    ts=data.get("time_signature")
    if not isinstance(ts,str) or not ts: errors.append("invalid type: $.time_signature; SongPlanV2 requires a non-empty string such as '4/4'")
    arr=data.get("arrangement")
    if not isinstance(arr,dict): errors.append("arrangement must be object")
    else:
        sections=arr.get("sections"); ha=arr.get("harmony_assignments")
        if not isinstance(sections,list): errors.append("arrangement.sections must be array")
        else:
            ids=set()
            for i,s in enumerate(sections):
                if not isinstance(s,dict): errors.append(f"invalid type: $.arrangement.sections[{i}]"); continue
                for field in ("id","start_bar","bar_count","energy"):
                    if field not in s: errors.append(f"missing required field: $.arrangement.sections[{i}].{field}")
                if "id" in s:
                    if not isinstance(s["id"],str) or not s["id"]: errors.append(f"invalid section identifier: $.arrangement.sections[{i}].id")
                    elif s["id"] in ids: errors.append(f"duplicate section identifier: $.arrangement.sections[{i}].id")
                    else: ids.add(s["id"])
                for field in ("start_bar","bar_count"):
                    if field in s and (not isinstance(s[field],int) or isinstance(s[field],bool) or s[field] < 1): errors.append(f"invalid value: $.arrangement.sections[{i}].{field}")
                if "energy" in s and (not isinstance(s["energy"],(int,float)) or isinstance(s["energy"],bool)): errors.append(f"invalid type: $.arrangement.sections[{i}].energy")
        if not isinstance(ha,list): errors.append("arrangement.harmony_assignments must be array")
        else:
            for i,h in enumerate(ha):
                if not isinstance(h,dict) or "harmony" not in h or not ("section_id" in h or {"start_bar","bar_count"} <= set(h)): errors.append(f"harmony assignment {i} missing address or label")
                elif "section_id" in h and isinstance(sections,list) and h["section_id"] not in ids: errors.append(f"invalid section reference: $.arrangement.harmony_assignments[{i}].section_id")
    tracks=data.get("tracks")
    if not isinstance(tracks,list): errors.append("tracks must be array")
    else:
        track_ids=set()
        for i,t in enumerate(tracks):
            if not isinstance(t,dict): errors.append(f"invalid type: $.tracks[{i}]"); continue
            for field in ("id","type","role","motifs","section_assignments"):
                if field not in t: errors.append(f"missing required field: $.tracks[{i}].{field}")
            if "id" in t:
                if not isinstance(t["id"],str) or not t["id"]: errors.append(f"invalid track identifier: $.tracks[{i}].id")
                elif t["id"] in track_ids: errors.append(f"duplicate track identifier: $.tracks[{i}].id")
                else: track_ids.add(t["id"])
            if t.get("type") not in {"pitched","drums","percussion","effect"}: errors.append(f"invalid type: $.tracks[{i}].type")
            if "motifs" in t and not isinstance(t["motifs"],list): errors.append(f"invalid type: $.tracks[{i}].motifs")
            if "section_assignments" in t and not isinstance(t["section_assignments"],list): errors.append(f"invalid type: $.tracks[{i}].section_assignments")
            if t.get("type") == "percussion":
                for field in ("kit_id","map_id"):
                    if field not in t: errors.append(f"missing required field: $.tracks[{i}].{field}")
            motifs=t.get("motifs"); motif_ids=set()
            if isinstance(motifs,list):
                for j,m in enumerate(motifs):
                    if not isinstance(m,dict) or not {"id","events"} <= set(m): errors.append(f"missing required field: $.tracks[{i}].motifs[{j}].id/events")
                    elif m["id"] in motif_ids: errors.append(f"duplicate motif identifier: $.tracks[{i}].motifs[{j}].id")
                    elif isinstance(m.get("id"),str): motif_ids.add(m["id"])
                    if not isinstance(m,dict) or not isinstance(m.get("events"),list): continue
                    for k,e in enumerate(m["events"]):
                        if not isinstance(e,dict): errors.append(f"invalid type: $.tracks[{i}].motifs[{j}].events[{k}]"); continue
                        typ=t.get("type")
                        common_event = ("bar","beat","duration")
                        for field in common_event:
                            if field not in e: errors.append(f"missing required field: $.tracks[{i}].motifs[{j}].events[{k}].{field}")
                        allowed_event = {
                            "pitched":{"bar","beat","duration","pitches","velocity","chromatic","articulation","id","instrument_articulation"},
                            "drums":{"bar","beat","duration","drum_voice","velocity","articulation","id"},
                            "percussion":{"bar","beat","duration","instrument","sounding_articulation","velocity","id"},
                            "effect":{"bar","beat","duration","id"},
                        }.get(typ, set())
                        for field in sorted(set(e) - allowed_event): errors.append(f"unsupported field: $.tracks[{i}].motifs[{j}].events[{k}].{field}")
                        if typ=="pitched" and ("pitches" not in e or not isinstance(e.get("pitches"),list) or not e.get("pitches")): errors.append(f"missing required field: $.tracks[{i}].motifs[{j}].events[{k}].pitches")
                        if typ=="drums" and "drum_voice" not in e: errors.append(f"missing required field: $.tracks[{i}].motifs[{j}].events[{k}].drum_voice")
                        if typ=="percussion":
                            for field in ("instrument","sounding_articulation"):
                                if field not in e: errors.append(f"missing required field: $.tracks[{i}].motifs[{j}].events[{k}].{field}")
                        if typ=="effect": pass
            assignments=t.get("section_assignments")
            if isinstance(assignments,list):
                for j,a in enumerate(assignments):
                    if not isinstance(a,dict) or not {"section_id","motif_id"} <= set(a): errors.append(f"missing required field: $.tracks[{i}].section_assignments[{j}].section_id/motif_id")
                    elif isinstance(sections,list) and a["section_id"] not in ids: errors.append(f"invalid section reference: $.tracks[{i}].section_assignments[{j}].section_id")
                    elif isinstance(motifs,list) and a["motif_id"] not in motif_ids: errors.append(f"invalid motif reference: $.tracks[{i}].section_assignments[{j}].motif_id")
    if trace and data.get("frozen_decision_trace_hash") not in (None, trace.get("trace_hash")): errors.append("serialization changed frozen trace")
    return errors

def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="cmd",required=True)
    a=sub.add_parser("assemble"); a.add_argument("--stage",type=int,choices=[1,2,3],required=True); a.add_argument("--brief",type=Path,required=True); a.add_argument("--instruction",type=Path,required=True); a.add_argument("--out",type=Path,required=True); a.add_argument("--prior",type=Path); a.add_argument("--extra-record",type=Path,action="append",default=[])
    r=sub.add_parser("retry-payload"); r.add_argument("--original",type=Path,required=True); r.add_argument("--out",type=Path,required=True); r.add_argument("--diagnostic",action="append",required=True)
    g=sub.add_parser("gate"); g.add_argument("--stage",type=int,choices=[1,2,3],required=True); g.add_argument("--output",type=Path,required=True); g.add_argument("--host-config",type=Path)
    args=p.parse_args()
    if args.cmd=="assemble": print(json.dumps(assemble(args.stage,args.brief,args.instruction,args.out,args.prior,args.extra_record),ensure_ascii=False,indent=2)); return 0
    if args.cmd=="retry-payload": print(json.dumps(build_retry_payload(args.original,args.diagnostic,args.out),ensure_ascii=False,indent=2)); return 0
    result=gate(args.stage,args.output,host_config=args.host_config); print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result["pass"] else 1
if __name__ == "__main__": main()
