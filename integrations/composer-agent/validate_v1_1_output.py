"""Read-only contract gate for a captured JSON response; never repairs it."""
from __future__ import annotations
import json
from pathlib import Path
import sys

REQUIRED = {
    "FORM", "SECTION_ROLES", "HARMONIC_FRAMEWORK", "FOCAL_IDENTITY",
    "LEAD_MOTIF_BEHAVIOR", "BASS_ROLE", "GROOVE", "N3-P_PERCUSSION_ARCHITECTURE",
    "TEXTURE", "DEVELOPMENT", "ENERGY_TENSION_RELEASE", "ENDING",
    "CROSS_DOMAIN_CONFLICTS", "SONGPLAN_HANDOFF",
}
ROOT_KEYS = {"schema_version", "name", "tempo", "time_signature", "tonic", "mode", "style", "arrangement", "tracks"}
N3_KEYS = {"decision_id", "candidate_strategies", "selected_outcome", "selection_basis", "bass_groove_interaction", "focal_hierarchy_interaction", "section_behavior", "development_behavior"}

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_v1_1_output.py raw-output.txt", file=sys.stderr)
        return 2
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors = []
    checklist = data.get("completion_checklist")
    if not isinstance(checklist, list):
        errors.append("completion_checklist must be an array")
        checklist = []
    by_name = {entry.get("decision"): entry for entry in checklist if isinstance(entry, dict)}
    missing = REQUIRED - by_name.keys()
    extra_duplicates = len(by_name) != len(checklist)
    if missing:
        errors.append("missing required checklist decisions: " + ", ".join(sorted(missing)))
    if extra_duplicates:
        errors.append("duplicate or malformed checklist entries")
    if data.get("status") == "READY_FOR_VALIDATION":
        unresolved = [name for name in REQUIRED if name in by_name and by_name[name].get("status") not in {"RESOLVED", "NOT_APPLICABLE"}]
        if unresolved:
            errors.append("READY_FOR_VALIDATION with unresolved decisions: " + ", ".join(sorted(unresolved)))
        for name, entry in by_name.items():
            if entry.get("status") == "NOT_APPLICABLE" and not entry.get("selected_option_or_block_reason"):
                errors.append(f"NOT_APPLICABLE lacks reason: {name}")
        plan = data.get("songplan_candidate")
        if not isinstance(plan, dict) or set(plan) != ROOT_KEYS:
            errors.append("READY_FOR_VALIDATION requires SongPlanV2 candidate with exact root keys")
        elif plan.get("schema_version") != "2.0":
            errors.append("SongPlanV2 schema_version must be 2.0")
    n3 = data.get("n3_p_decision")
    if not isinstance(n3, dict) or not N3_KEYS <= n3.keys():
        errors.append("N3-P decision is missing required fields")
    elif not n3.get("candidate_strategies") or any(not n3.get(key) for key in ("decision_id", "selection_basis", "bass_groove_interaction", "focal_hierarchy_interaction", "section_behavior", "development_behavior")):
        errors.append("N3-P required decision values must be explicit and non-empty")
    if data.get("status") not in {"READY_FOR_VALIDATION", "BLOCKED"}:
        errors.append("invalid status")
    if errors:
        print(json.dumps({"status":"REJECTED","errors":errors}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps({"status":"STRUCTURE_AND_GATE_PASS","semantic_repair_performed":False}, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
