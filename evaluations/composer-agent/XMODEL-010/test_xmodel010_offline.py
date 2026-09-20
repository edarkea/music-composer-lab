"""Offline-only XMODEL-010 contract and provenance regression tests."""
import json, re, sys, tempfile, unittest
import contextlib, io
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'integrations/composer-agent'))
import staged_harness as h
import staged_runner as r
import test_staged_harness as baseline_fixtures
from music_engine.domain import Duration, Position
PKG=ROOT/'evaluations/composer-agent/XMODEL-010'
SCHEMA=json.loads((PKG/'stage-3-songplan-format-schema-v1.2.json').read_text(encoding='utf-8'))
DURATION_PATTERN=SCHEMA['$defs']['pitchedEvent']['properties']['duration']['pattern']

def plan():
    return {"schema_version":"2.0","name":"fixture","tempo":120,"time_signature":"4/4","tonic":"C","mode":"ionian","style":"indie-dance",
      "arrangement":{"sections":[{"id":"A","start_bar":1,"bar_count":4,"energy":0.5}],"harmony_assignments":[]},
      "tracks":[{"id":"lead","type":"pitched","role":"lead","motifs":[{"id":"m","events":[{"bar":1,"beat":"1","duration":"1/4","pitches":["C4"]}]}],"section_assignments":[{"section_id":"A","motif_id":"m"}]},
       {"id":"drums","type":"drums","role":"groove","motifs":[{"id":"dm","events":[{"bar":1,"beat":"1","duration":"1/4","drum_voice":"kick"}]}],"section_assignments":[{"section_id":"A","motif_id":"dm"}]}]}

def gate_plan(x):
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'output.json'; p.write_text(json.dumps(x),encoding='utf-8'); return h.gate(3,p)

class XModel010Offline(unittest.TestCase):
    def test_01_duplicate_json_keys_rejected_with_path(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'x.json'; p.write_text('{"outer":{"duration":"1/4","duration":"1/2"}}')
            _,errors=h.parse_output(p)
            self.assertTrue(any('duplicate JSON object key at $.outer.duration' in e for e in errors))
    def test_02_effect_position_rejected(self):
        x=plan(); x['tracks'].append({"id":"fx","type":"effect","role":"texture","motifs":[{"id":"f","events":[{"bar":1,"beat":"1","duration":"1/4","position":"1"}]}],"section_assignments":[]})
        self.assertTrue(any('unsupported field' in e and '.position' in e for e in gate_plan(x)['errors']))
    def test_03_invalid_time_signature_type_rejected(self):
        x=plan(); x['time_signature']={"numerator":4,"denominator":4}
        self.assertTrue(any('time_signature' in e for e in gate_plan(x)['errors']))
    def test_04_valid_synthetic_plan_passes_real_engine(self):
        result=gate_plan(plan()); self.assertTrue(result['pass'],result); self.assertTrue(result['engine_validation']['engine_invoked'])
    def test_05_out_of_scale_fails_without_chromatic(self):
        x=plan(); x['tonic']='D'; x['tracks'][0]['motifs'][0]['events'][0]['pitches']=['F4']
        y=gate_plan(x); self.assertFalse(y['pass']); self.assertEqual(y['engine_validation']['category'],'musical_semantic_validation_failure')
    def test_06_explicit_chromatic_allows_out_of_scale(self):
        x=plan(); x['tonic']='D'; e=x['tracks'][0]['motifs'][0]['events'][0]; e['pitches']=['F4']; e['chromatic']=True
        self.assertTrue(gate_plan(x)['pass'])
    def test_07_bad_host_configuration_distinguished(self):
        x=plan(); x['tracks'].append({"id":"perc","type":"percussion","role":"texture","kit_id":"unknown","map_id":"unknown","motifs":[],"section_assignments":[]})
        y=gate_plan(x); self.assertFalse(y['pass']); self.assertEqual(y['engine_validation']['category'],'host_configuration_failure')
    def test_08_engine_validation_is_invoked(self):
        y=gate_plan(plan()); self.assertTrue(y['engine_validation']['engine_invoked'])
    def test_09_unavailable_engine_blocks_not_pass(self):
        with patch.object(h,'_load_engine_api',side_effect=ImportError('offline fixture')):
            y=h.validate_with_engine(plan()); self.assertEqual(y['status'],'BLOCK'); self.assertFalse(y['engine_invoked'])
    def test_10_gate_never_reports_adapter_decision(self):
        y=gate_plan(plan()); self.assertFalse(y['semantic_repair_performed'])
    def test_11_failed_stage1_blocks_stage2(self):
        self.assertFalse(h.can_advance({'pass':False,'stage':1},2))
    def test_12_fraction_contract_preserves_engine_forms(self):
        accepted=['1/4','2/4','3/8','1/6','1.25','.25','1.','1e-3',' 1/4 ','1_000/2','+1/2',' 0.25 ']
        self.assertTrue(all(re.fullmatch(DURATION_PATTERN,v) for v in accepted))
    def test_13_fraction_contract_rejects_malformed_forms(self):
        rejected=['1 / 4','1//2','1/2/3','1__0/2','NaN','Infinity','?/?']
        self.assertTrue(all(not re.fullmatch(DURATION_PATTERN,v) for v in rejected))
    def test_14_engine_rejects_nonpositive_duration(self):
        x=plan(); x['tracks'][0]['motifs'][0]['events'][0]['duration']='0'
        self.assertEqual(h.validate_with_engine(x)['status'],'FAIL')
    def test_15_request_id_collision_fails_before_network(self):
        with tempfile.TemporaryDirectory() as td:
            base=Path(td); manifest={'request_sha256':'abc','experiment_id':'XMODEL-010','model':'qwen3:14b','stage':'stage-1','attempt':1}
            first=r.reserve_capture(base/'registry','req-1',base/'out-1',manifest)
            self.assertTrue((first/'request-manifest.json').exists())
            with self.assertRaises(FileExistsError): r.reserve_capture(base/'registry','req-1',base/'out-2',manifest)
            r.journal_state(first,'SENT')
            with self.assertRaisesRegex(ValueError,'already sent'):
                r.reserve_capture(base/'registry','req-2',base/'out-2',manifest)
    def test_16_output_directory_reuse_fails(self):
        with tempfile.TemporaryDirectory() as td:
            base=Path(td); (base/'out').mkdir()
            with self.assertRaises(FileExistsError): r.reserve_capture(base/'registry','req-2',base/'out',{})
    def test_17_retry_must_branch_from_original_and_is_exclusive(self):
        with tempfile.TemporaryDirectory() as td:
            base=Path(td); original=base/'original.txt'; original.write_text('FROZEN ORIGINAL')
            first=base/'retry-1.txt'; h.build_retry_payload(original,['gate diagnostic'],first)
            with self.assertRaises(ValueError): h.build_retry_payload(first,['next diagnostic'],base/'retry-2.txt')
            with self.assertRaises(FileExistsError): h.build_retry_payload(original,['new'],first)
    def test_18_duration_and_beat_fraction_edge_cases_match_engine(self):
        for value in ('1/4','2/4','1.25','.25','1.','1e-3',' 1/4 ','1_000/2','+1/2'):
            self.assertGreater(Duration(value).whole_notes,0)
        for value in ('0','-1/2','1/0','1 / 4','1//2','1/2/3'):
            with self.assertRaises((ValueError,ZeroDivisionError)): Duration(value)
        self.assertEqual(Position(1,' 3/2 ').beat.numerator,3)
        with self.assertRaises(ValueError): Position(1,'0')
        with self.assertRaises(ValueError): Position(1,'1 / 2')
    def test_19_stage2_schema_is_semantic_neutral_object_only(self):
        obj=json.loads((PKG/'stage-2-json-object-format-v1.0.json').read_text())
        self.assertEqual(obj,{'type':'object'})
    def test_20_x009_source_package_untouched_by_test_setup(self):
        self.assertTrue((ROOT/'evaluations/composer-agent/XMODEL-009/run-manifest.yaml').exists())
    def test_21_runner_journals_prepared_and_sent_before_capture(self):
        with tempfile.TemporaryDirectory() as td:
            base=Path(td); out=base/'attempt-1'; registry=base/'registry'
            def fake_transport(req,url,timeout):
                hist=(registry/'req-1'/'state-history.jsonl').read_text().splitlines()
                self.assertEqual([json.loads(x)['state'] for x in hist],['PREPARED','SENT'])
                prepared=json.loads((registry/'req-1'/'request-manifest.json').read_text())
                self.assertTrue(any(x.endswith('/stage-1-output-schema-v1.1-n3-canonical.json') for x in prepared['resolved_record_ids']))
                self.assertEqual(len(prepared['required_records']),2)
                self.assertEqual(prepared['request_kind'],'evaluable_attempt')
                sent=json.loads(hist[1]);self.assertEqual(sent['model_request_count_increment'],1)
                body=json.dumps({'model':'qwen3:14b','message':{'content':'{}'},'done':True,'done_reason':'stop'}).encode()
                return {'transport_status':'COMPLETE_RESPONSE','http_status':200,'elapsed_seconds':0.0,'response_bytes':body,'error_type':None,'error':None}
            payload=PKG/'outputs/qwen3-14b/stage-1-payload.txt'
            brief=PKG/'brief.yaml'; instruction=PKG/'stage-1-prompt-v1.2.txt'; schema=PKG/'stage-1-output-schema-v1.1-n3-canonical.json'
            args=['staged_runner.py','--model','qwen3:14b','--stage','stage-1','--attempt','1','--request-id','req-1','--experiment-id','XMODEL-010','--request-registry',str(registry),'--input',str(payload),'--brief',str(brief),'--output-dir',str(out),'--num-predict','4096','--stage-number','1','--instruction',str(instruction),'--format-schema',str(schema),'--required-record',str(schema),'--required-record',str(PKG/'model-visible-host-capabilities.md')]
            with patch.object(sys,'argv',args),patch.object(r,'transport_request',side_effect=fake_transport),contextlib.redirect_stdout(io.StringIO()):
                self.assertIsNone(r.main())
            states=[json.loads(x)['state'] for x in (registry/'req-1'/'state-history.jsonl').read_text().splitlines()]
            self.assertEqual(states,['PREPARED','SENT','CAPTURED'])
    def test_22_later_stage_model_visible_payload_assembly_with_synthetic_priors(self):
        with tempfile.TemporaryDirectory(dir=PKG) as td:
            temp=Path(td); prior1=temp/'accepted-stage1.json'; prior1.write_text(json.dumps(baseline_fixtures.valid_trace()),encoding='utf-8')
            stage2_prompt=PKG/'stage-2-prompt-v1.2.txt'; stage2_map=PKG/'stage-2-contract-validation-map-v1.1.md'; s2format=PKG/'stage-2-json-object-format-v1.0.json'
            s2dir=temp/'stage2'; s2dir.mkdir(); s2payload=s2dir/'stage2.txt'
            s2=h.assemble(2,PKG/'brief.yaml',stage2_prompt,s2payload,prior1,[stage2_map,s2format])
            self.assertTrue(s2['preflight']['pass'],s2)
            prior2=temp/'accepted-stage2.json'; prior2.write_text(json.dumps(baseline_fixtures.valid_stage2()),encoding='utf-8')
            s3prompt=PKG/'stage-3-prompt-v1.2.txt'; s3format=PKG/'stage-3-songplan-format-schema-v1.2.json'; engine_schema=PKG/'engine-songplan-v2.schema-music-engine-4.0.0.json'
            s3dir=temp/'stage3'; s3dir.mkdir(); s3payload=s3dir/'stage3.txt'
            s3=h.assemble(3,PKG/'brief.yaml',s3prompt,s3payload,prior2,[s3format,engine_schema])
            self.assertTrue(s3['preflight']['pass'],s3)
    def test_23_unknown_songplan_field_fails_real_codec(self):
        x=plan(); x['tracks'][0]['unapproved_field']='x'
        self.assertEqual(h.validate_with_engine(x)['category'],'invalid_songplan_structure')
    def test_24_percussion_without_approved_map_blocks_host(self):
        x=plan(); x['tracks'].append({"id":"perc","type":"percussion","role":"texture","kit_id":"candidate_kit","map_id":"candidate_map","motifs":[{"id":"pm","events":[{"bar":1,"beat":"1","duration":"1/8","instrument":"hi-hat","sounding_articulation":"open"}]}],"section_assignments":[{"section_id":"A","motif_id":"pm"}]})
        self.assertEqual(h.validate_with_engine(x)['category'],'host_configuration_failure')
    def test_25_invalid_section_reference_fails_engine_semantics(self):
        x=plan(); x['tracks'][0]['section_assignments'][0]['section_id']='MISSING'
        self.assertEqual(h.validate_with_engine(x)['category'],'musical_semantic_validation_failure')
        self.assertFalse(gate_plan(x)['pass'])
    def test_26_malformed_pitch_fails_real_codec(self):
        x=plan(); x['tracks'][0]['motifs'][0]['events'][0]['pitches']=['H4']
        self.assertEqual(h.validate_with_engine(x)['category'],'invalid_songplan_structure')
    def test_27_chromatic_field_misuse_fails_real_codec(self):
        x=plan(); x['tracks'][0]['motifs'][0]['events'][0]['chromatic']='true'
        self.assertEqual(h.validate_with_engine(x)['category'],'invalid_songplan_structure')
    def test_28_missing_required_field_fails_real_codec(self):
        x=plan(); del x['time_signature']
        self.assertEqual(h.validate_with_engine(x)['category'],'invalid_songplan_structure')
    def test_29_valid_decimal_duration_passes_real_engine(self):
        x=plan(); x['tracks'][0]['motifs'][0]['events'][0]['duration']='1.25'
        self.assertTrue(gate_plan(x)['pass'])
    def test_30_engine_rejects_time_signature_object(self):
        x=plan(); x['time_signature']={'numerator':4,'denominator':4}
        self.assertEqual(h.validate_with_engine(x)['category'],'invalid_songplan_structure')
    def test_31_engine_rejects_effect_position(self):
        x=plan(); x['tracks'].append({"id":"fx","type":"effect","role":"texture","motifs":[{"id":"f","events":[{"bar":1,"beat":"1","duration":"1/4","position":"1"}]}],"section_assignments":[]})
        self.assertEqual(h.validate_with_engine(x)['category'],'invalid_songplan_structure')
    def test_32_owner_approved_steven_slate_drum_map_is_exact(self):
        from music_engine.songplan.percussion import load_drum_external_map
        loaded=load_drum_external_map(ROOT/'integrations/music-engine/host-maps/song001_r1_steven_slate_map.yaml')
        self.assertEqual(loaded.id,'song001_r1_steven_slate_map')
        self.assertEqual(dict(loaded.mappings),{'kick':36,'snare':38,'rimshot':40,'closed_hat':44,'open_hat':46,'pedal_hat':42,'low_tom':41,'mid_tom':45,'high_tom':48,'crash':55,'ride':51,'ride_bell':53,'cowbell':50})
    def test_33_unavailable_engine_blocks_stage3_gate(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'song.json'; p.write_text(json.dumps(plan()),encoding='utf-8')
            with patch.object(h,'_load_engine_api',side_effect=ImportError('synthetic unavailable engine')):
                result=h.gate(3,p)
            self.assertFalse(result['pass']); self.assertEqual(result['engine_validation']['status'],'BLOCK')
    def test_34_incomplete_api_response_never_writes_gateable_output(self):
        with tempfile.TemporaryDirectory() as td:
            base=Path(td);registry=base/'registry';out=base/'output'
            payload=PKG/'outputs/qwen3-14b/stage-1-payload.txt';brief=PKG/'brief.yaml';instruction=PKG/'stage-1-prompt-v1.2.txt';schema=PKG/'stage-1-output-schema-v1.1-n3-canonical.json'
            body=json.dumps({'model':'qwen3:14b','message':{'content':'{}'},'done':False,'done_reason':'length'}).encode()
            args=['staged_runner.py','--model','qwen3:14b','--stage','stage-1','--attempt','1','--request-id','req-incomplete','--experiment-id','XMODEL-010','--request-registry',str(registry),'--input',str(payload),'--brief',str(brief),'--output-dir',str(out),'--num-predict','4096','--stage-number','1','--instruction',str(instruction),'--format-schema',str(schema),'--required-record',str(schema),'--required-record',str(PKG/'model-visible-host-capabilities.md')]
            with patch.object(sys,'argv',args),patch.object(r,'transport_request',return_value={'transport_status':'COMPLETE_RESPONSE','http_status':200,'elapsed_seconds':0.0,'response_bytes':body,'error_type':None,'error':None}),contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(RuntimeError): r.main()
            self.assertFalse((out/'raw-output.txt').exists());self.assertFalse((out/'capture-manifest.json').exists())
            states=[json.loads(x)['state'] for x in (registry/'req-incomplete'/'state-history.jsonl').read_text().splitlines()]
            self.assertEqual(states,['PREPARED','SENT','INVALID_API_RESPONSE'])

if __name__=='__main__': unittest.main(verbosity=2)
