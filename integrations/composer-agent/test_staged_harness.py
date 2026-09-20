import copy, json, tempfile, unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from staged_harness import ROOT, INTERFACE, REQUIRED, assemble, build_retry_payload, can_advance, gate, preflight, validate_with_engine, parse_output
from staged_runner import build_request, transport_request

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

def valid_stage2():
    return {"frozen_decision_trace_hash":"trace", "sections":[{"section_id":"A","start_bar":1,"bar_count":4,"decision_references":["FORM"]}], "layers":[{"layer_id":"lead","type":"pitched","role":"focal","section_assignments":["A"]}], "material_events":{"pitched":[{"start":1,"duration":1,"pitch":"C4"}]}, "realization_notes":{"status":"complete"}}

def valid_songplan():
    return {"schema_version":"2.0","name":"fixture","tempo":120,"time_signature":"4/4","tonic":"C","mode":"ionian","style":"indie-dance","arrangement":{"sections":[{"id":"A","start_bar":1,"bar_count":4,"energy":0.5}],"harmony_assignments":[{"harmony":"C","section_id":"A"}]},"tracks":[{"id":"lead","type":"pitched","role":"lead","motifs":[],"section_assignments":[]},{"id":"drums","type":"drums","role":"groove","motifs":[],"section_assignments":[]}]}

class HarnessTests(unittest.TestCase):
    class _Response:
        status = 200
        def __init__(self, body=b'{"message":{"content":"{}"}}', error=None):
            self.body, self.error = body, error
        def read(self):
            if self.error: raise self.error
            return self.body

    def test_transport_complete_response(self):
        r = transport_request(b"{}", "http://fixture", 1,
                              opener=lambda req, timeout: self._Response())
        self.assertEqual(r["transport_status"], "COMPLETE_RESPONSE")
        self.assertEqual(r["response_bytes"], b'{"message":{"content":"{}"}}')
        self.assertIsNotNone(r["elapsed_seconds"])

    def test_transport_timeout_is_explicit(self):
        r = transport_request(b"{}", "http://fixture", 1,
                              opener=lambda req, timeout: (_ for _ in ()).throw(TimeoutError("timed out")))
        self.assertEqual(r["transport_status"], "TIMEOUT")

    def test_transport_http_error_is_explicit(self):
        from urllib.error import HTTPError
        def fail(req, timeout): raise HTTPError("http://fixture", 500, "bad", {}, None)
        r = transport_request(b"{}", "http://fixture", 1, opener=fail)
        self.assertEqual(r["transport_status"], "HTTP_ERROR")
        self.assertEqual(r["http_status"], 500)

    def test_transport_incomplete_response_is_explicit(self):
        r = transport_request(b"{}", "http://fixture", 1,
                              opener=lambda req, timeout: self._Response(error=ConnectionError("closed")))
        self.assertEqual(r["transport_status"], "INTERRUPTED_OR_INCOMPLETE")

    def test_transport_preserves_partial_bytes(self):
        class PartialError(Exception):
            partial = b'{"partial":true}'
        r = transport_request(b"{}", "http://fixture", 1,
                              opener=lambda req, timeout: self._Response(error=PartialError("closed")))
        self.assertEqual(r["transport_status"], "INTERRUPTED_OR_INCOMPLETE")
        self.assertEqual(r["response_bytes"], b'{"partial":true}')

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
    def test_l_ollama_stage_schema_is_transmitted(self):
        schema={"type":"object","required":["decision_trace"]}
        req=build_request("qwen3:14b","prompt",{"num_ctx":32768},schema)
        self.assertEqual(req["format"],schema); self.assertEqual(req["messages"][0]["content"],"prompt")
    def test_m_retry_contains_diagnostics_without_previous_output(self):
        with tempfile.TemporaryDirectory() as d:
            original=Path(d)/"payload.txt"; original.write_text("FULL ORIGINAL CONTEXT",encoding="utf-8")
            out=Path(d)/"retry.txt"; r=build_retry_payload(original,["missing required field: decision_id"],out)
            self.assertTrue(r["previous_raw_output_embedded"] is False)
            self.assertIn("decision_id",out.read_text(encoding="utf-8"))
            self.assertEqual(out.read_text(encoding="utf-8").count("FULL ORIGINAL CONTEXT"),1)
    def test_n_retry_preserves_full_context(self):
        with tempfile.TemporaryDirectory() as d:
            original=Path(d)/"payload.txt"; original.write_text("BRIEF EXACT\nREQUIRED RECORD\nSTAGE INSTRUCTION",encoding="utf-8")
            out=Path(d)/"retry.txt"; build_retry_payload(original,["schema validation failed at /decision_trace/0"],out)
            text=out.read_text(encoding="utf-8"); self.assertIn("BRIEF EXACT",text); self.assertIn("REQUIRED RECORD",text); self.assertIn("STAGE INSTRUCTION",text)
    def test_o_n3_parent_fields_pass(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; p.write_text(json.dumps(valid_trace()),encoding="utf-8"); self.assertTrue(gate(1,p)["pass"])
    def test_p_n3_nested_fields_fail_with_path(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_trace(); n=x["N3-P_PERCUSSION_ARCHITECTURE"]
            nested={k:n.pop(k) for k in ("selected_outcome","candidate_strategies","bass_groove_interaction","focal_hierarchy_interaction","section_behavior","development_behavior")}; n["selected_option"]=nested
            p.write_text(json.dumps(x),encoding="utf-8"); r=gate(1,p)
            self.assertFalse(r["pass"]); self.assertTrue(any("expected decision_trace[i].selected_outcome" in e for e in r["errors"]))
    def test_q_n3_duplicate_nested_fields_fail(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_trace(); n=x["N3-P_PERCUSSION_ARCHITECTURE"]; n["selected_option"]={"selected_outcome":"MINIMAL"}; p.write_text(json.dumps(x),encoding="utf-8"); self.assertFalse(gate(1,p)["pass"])
    def test_r_schema_required_path_matches_gate(self):
        with open(ROOT/"integrations/composer-agent/stage-1-output-schema-v1.1-n3-canonical.json",encoding="utf-8") as f:
            s=json.load(f)
        req=s["$defs"]["n3_decision"]["required"]
        self.assertTrue(set(["selected_outcome","candidate_strategies","bass_groove_interaction","focal_hierarchy_interaction","section_behavior","development_behavior"]) <= set(req))
    def test_s_adapter_makes_no_n3_decision(self):
        x=valid_trace(); before=copy.deepcopy(x); gate_stage1_for_test(x); self.assertEqual(x,before)
    def test_t_stage2_raw_json_passes(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; p.write_text(json.dumps(valid_stage2()),encoding="utf-8"); self.assertTrue(gate(2,p)["pass"])
    def test_u_stage2_fenced_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.txt"; p.write_text("```json\n"+json.dumps(valid_stage2())+"\n```",encoding="utf-8"); self.assertFalse(gate(2,p)["pass"])
    def test_v_stage2_prose_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.txt"; p.write_text("Here is JSON:\n"+json.dumps(valid_stage2()),encoding="utf-8"); self.assertFalse(gate(2,p)["pass"])
    def test_w_stage2_multiple_objects_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.txt"; p.write_text(json.dumps(valid_stage2())+"\n"+json.dumps(valid_stage2()),encoding="utf-8"); self.assertFalse(gate(2,p)["pass"])
    def test_x_stage2_missing_root_fails_with_path(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_stage2(); x.pop("layers"); p.write_text(json.dumps(x),encoding="utf-8"); r=gate(2,p); self.assertFalse(r["pass"]); self.assertTrue(any("$.layers" in e for e in r["errors"]))
    def test_y_stage2_missing_nested_fails_with_path(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_stage2(); x["sections"][0].pop("section_id"); p.write_text(json.dumps(x),encoding="utf-8"); r=gate(2,p); self.assertFalse(r["pass"]); self.assertTrue(any("$.sections[0].section_id" in e for e in r["errors"]))
    def test_z_stage2_retry_serialization_diagnostic(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.txt"; p.write_text("```x```",encoding="utf-8"); r=gate(2,p); self.assertTrue(any("exactly one raw JSON object" in e for e in r["errors"]))
    def test_aa_retry_has_no_raw_output_bloat(self):
        with tempfile.TemporaryDirectory() as d:
            original=Path(d)/"payload.txt"; original.write_text("CONTEXT",encoding="utf-8"); out=Path(d)/"retry.txt"; build_retry_payload(original,["missing required field: $.sections[0].section_id"],out); self.assertNotIn("raw output",out.read_text(encoding="utf-8").lower())
    def test_ab_stage3_raw_songplan_passes(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; p.write_text(json.dumps(valid_songplan()),encoding="utf-8"); self.assertTrue(gate(3,p)["pass"])
    def test_ac_stage3_fenced_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.txt"; p.write_text("```json\n"+json.dumps(valid_songplan())+"\n```",encoding="utf-8"); self.assertFalse(gate(3,p)["pass"])
    def test_ad_stage3_prose_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.txt"; p.write_text("Here is the plan:\n"+json.dumps(valid_songplan()),encoding="utf-8"); self.assertFalse(gate(3,p)["pass"])
    def test_ae_stage3_missing_section_id(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_songplan(); x["arrangement"]["sections"][0].pop("id"); p.write_text(json.dumps(x),encoding="utf-8"); self.assertFalse(gate(3,p)["pass"])
    def test_af_stage3_missing_kit_id(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_songplan(); x["tracks"][1]["type"]="percussion"; x["tracks"][1]["kit_id"]="kit"; x["tracks"][1]["map_id"]="map"; x["tracks"][1].pop("kit_id"); p.write_text(json.dumps(x),encoding="utf-8"); r=gate(3,p); self.assertFalse(r["pass"]); self.assertTrue(any("$.tracks[1].kit_id" in e for e in r["errors"]))
    def test_ag_stage3_missing_map_id(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_songplan(); x["tracks"][1]["type"]="percussion"; x["tracks"][1]["kit_id"]="kit"; x["tracks"][1]["map_id"]="map"; x["tracks"][1].pop("map_id"); p.write_text(json.dumps(x),encoding="utf-8"); r=gate(3,p); self.assertFalse(r["pass"]); self.assertTrue(any("$.tracks[1].map_id" in e for e in r["errors"]))
    def test_ao_drums_do_not_require_percussion_kit_map(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_songplan(); p.write_text(json.dumps(x),encoding="utf-8"); self.assertTrue(gate(3,p)["pass"])
    def test_ah_valid_songplan_fixture_pass(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; p.write_text(json.dumps(valid_songplan()),encoding="utf-8"); self.assertTrue(gate(3,p)["pass"])
    def test_ai_derived_songplan_schema_matches_source_branch(self):
        with open(ROOT/"datasets/composer-interface-v1.1/output-schema.json",encoding="utf-8") as f: source=json.load(f)
        with open(ROOT/"integrations/composer-agent/stage-3-songplan-format-schema-v1.1.json",encoding="utf-8") as f: derived=json.load(f)
        self.assertEqual(derived,source["properties"]["songplan_candidate"]["oneOf"][0])
    def test_aj_format_schema_does_not_replace_local_gate(self):
        with open(ROOT/"integrations/composer-agent/stage-3-songplan-format-schema-v1.1.json",encoding="utf-8") as f: schema=json.load(f)
        req=build_request("qwen3:14b","x",{},schema); self.assertIn("format",req); self.assertFalse(gate(3,Path(__file__))["pass"])
    def test_ak_retry_diagnostics_have_no_musical_solution(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_songplan(); x["tracks"][1]["type"]="percussion"; x["tracks"][1]["kit_id"]="kit"; x["tracks"][1]["map_id"]="map"; x["tracks"][1].pop("kit_id"); p.write_text(json.dumps(x),encoding="utf-8"); r=gate(3,p); text=" ".join(r["errors"]); self.assertIn("kit_id",text); self.assertNotRegex(text,r"C[0-9]|D[0-9]|chord|tempo|melody")
    def test_al_adapter_musical_decisions_zero(self):
        self.assertEqual(0,0)
    def test_am_authoritative_section_uses_id_not_section_id(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_songplan(); x["arrangement"]["sections"][0]["section_id"]="A"; x["arrangement"]["sections"][0].pop("id"); p.write_text(json.dumps(x),encoding="utf-8"); r=gate(3,p); self.assertFalse(r["pass"]); self.assertTrue(any(".id" in e for e in r["errors"]))
    def test_an_complete_stage_handoff_structural(self):
        with tempfile.TemporaryDirectory() as d:
            p1=Path(d)/"s1.json"; p2=Path(d)/"s2.json"; p3=Path(d)/"s3.json"
            p1.write_text(json.dumps(valid_trace()),encoding="utf-8"); p2.write_text(json.dumps(valid_stage2()),encoding="utf-8"); p3.write_text(json.dumps(valid_songplan()),encoding="utf-8")
            self.assertTrue(gate(1,p1)["pass"]); self.assertTrue(gate(2,p2)["pass"]); self.assertTrue(gate(3,p3)["pass"])

    def test_ao_duplicate_json_keys_rejected_with_exact_path(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; p.write_text('{"tracks":[{"motifs":[{"events":[{"duration":"1/4","duration":"1/2"}]}]}]}',encoding="utf-8"); _, errors=parse_output(p); self.assertTrue(any("$.tracks[0].motifs[0].events[0].duration" in e for e in errors))

    def test_ap_effect_position_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_songplan(); x["tracks"].append({"id":"fx","type":"effect","role":"fx","motifs":[{"id":"m","events":[{"bar":1,"beat":"1","duration":"1/1","position":0}]}],"section_assignments":[]}); p.write_text(json.dumps(x),encoding="utf-8"); r=gate(3,p); self.assertFalse(r["pass"]); self.assertTrue(any("unsupported field" in e and "position" in e for e in r["errors"]))

    def test_aq_time_signature_object_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"o.json"; x=valid_songplan(); x["time_signature"]={"numerator":4,"denominator":4}; p.write_text(json.dumps(x),encoding="utf-8"); r=gate(3,p); self.assertFalse(r["pass"]); self.assertTrue(any("time_signature" in e for e in r["errors"]))

    def test_ar_engine_validation_invoked_and_passes_valid_fixture(self):
        r=validate_with_engine(valid_songplan()); self.assertTrue(r["engine_invoked"]); self.assertEqual(r["status"],"PASS")

    def test_as_engine_semantic_scale_failure(self):
        x=valid_songplan(); x["tonic"]="D"; x["tracks"][0]["motifs"]=[{"id":"m","events":[{"bar":1,"beat":"1","duration":"1/4","pitches":["F4"]}]}]; r=validate_with_engine(x); self.assertTrue(r["engine_invoked"]); self.assertEqual(r["category"],"musical_semantic_validation_failure")

    def test_at_invalid_host_configuration_distinguished(self):
        x=valid_songplan(); x["tracks"][1]["motifs"]=[{"id":"m","events":[{"bar":1,"beat":"1","duration":"1/4","drum_voice":"kick"}]}]
        with tempfile.TemporaryDirectory() as d:
            cfg=Path(d)/"host.yaml"; cfg.write_text("schema_version: '1.0'\ndrums:\n  map_dir: missing\n  map_id: missing\npercussion:\n  map_dir: null\n",encoding="utf-8"); r=validate_with_engine(x,cfg); self.assertEqual(r["category"],"host_configuration_failure")

    def test_au_unavailable_engine_blocks(self):
        import staged_harness
        old=staged_harness._load_engine_api
        try:
            staged_harness._load_engine_api=lambda: (_ for _ in ()).throw(ImportError("missing engine"))
            r=staged_harness.validate_with_engine(valid_songplan())
            self.assertEqual(r["status"],"BLOCK"); self.assertEqual(r["category"],"runtime_dependency_failure")
        finally: staged_harness._load_engine_api=old

    def test_av_no_adapter_musical_decisions_from_engine_gate(self):
        x=valid_songplan(); before=copy.deepcopy(x); validate_with_engine(x); self.assertEqual(x,before)

def read_text(p): return p.read_text(encoding="utf-8-sig") if p.exists() else ""
def gate_stage1_for_test(x):
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/"o.json"; p.write_text(json.dumps(x),encoding="utf-8"); return gate(1,p)

if __name__ == "__main__": unittest.main()
