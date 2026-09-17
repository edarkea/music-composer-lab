import copy, json, tempfile, unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from staged_harness import ROOT, INTERFACE, REQUIRED, assemble, can_advance, gate, preflight

BRIEF = ROOT / "evaluations/composer-agent/XMODEL-005/brief.yaml"
PROMPT = ROOT / "evaluations/composer-agent/XMODEL-005/frozen-prompt-stage-1.txt"

def valid_trace():
    out = {}
    for name in REQUIRED:
        out[name] = {"selected_option":"OPTION_A", "selection_basis":"ARTISTIC_PRIORITY",
                     "active_intention":"structural test", "tradeoff":"structural test",
                     "trace_reference":"synthetic-record"}
    out["N3-P_PERCUSSION_ARCHITECTURE"] = {
        "decision_id":"N3-P-TEST", "candidate_strategies":["FULL","MINIMAL"],
        "selected_outcome":"MINIMAL", "selection_basis":"ARTISTIC_PRIORITY",
        "bass_groove_interaction":"declared", "focal_hierarchy_interaction":"declared",
        "section_behavior":"declared", "development_behavior":"declared"}
    return out

class HarnessTests(unittest.TestCase):
    def test_a_missing_brief_preflight_fail(self):
        r = preflight("payload", 1, ROOT/"missing-brief.yaml", PROMPT); self.assertFalse(r["pass"])
    def test_b_missing_record_preflight_fail(self):
        r = preflight(read_text(BRIEF)+read_text(PROMPT), 1, BRIEF, PROMPT); self.assertFalse(r["pass"])
    def test_c_forbidden_example_preflight_fail(self):
        r = preflight(read_text(BRIEF)+read_text(PROMPT)+" SONG-001", 1, BRIEF, PROMPT); self.assertFalse(r["pass"])
    def test_d_malformed_output_fail(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.txt"; p.write_text("{bad",encoding="utf-8"); self.assertFalse(gate(1,p)["pass"])
    def test_e_missing_decision_fail(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_trace(); x.pop("FORM"); p.write_text(json.dumps(x),encoding="utf-8"); self.assertFalse(gate(1,p)["pass"])
    def test_f_invalid_n3_fail(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_trace(); x["N3-P_PERCUSSION_ARCHITECTURE"]["selected_outcome"]="BAD"; p.write_text(json.dumps(x),encoding="utf-8"); self.assertFalse(gate(1,p)["pass"])
    def test_g_rank_fail(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_trace(); x["FORM"]["rank"]="RANK-2"; p.write_text(json.dumps(x),encoding="utf-8"); self.assertFalse(gate(1,p)["pass"])
    def test_h_ready_like_incomplete_fail(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_trace(); x["FORM"].pop("selected_option"); p.write_text(json.dumps(x),encoding="utf-8"); self.assertFalse(gate(1,p)["pass"])
    def test_i_valid_structural_fixture_pass(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; p.write_text(json.dumps(valid_trace()),encoding="utf-8"); self.assertTrue(gate(1,p)["pass"])
    def test_j_failed_stage_cannot_advance(self):
        self.assertFalse(can_advance({"pass":False,"stage":1},2))
    def test_k_no_adapter_musical_decisions(self):
        x=valid_trace(); before=copy.deepcopy(x); _=gate_stage1_for_test(x); self.assertEqual(x,before)

def read_text(p): return p.read_text(encoding="utf-8-sig") if p.exists() else ""
def gate_stage1_for_test(x):
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/"o.json"; p.write_text(json.dumps(x),encoding="utf-8"); return gate(1,p)

if __name__ == "__main__": unittest.main()
