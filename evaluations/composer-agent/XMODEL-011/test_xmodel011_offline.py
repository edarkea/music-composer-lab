from __future__ import annotations
import hashlib, json, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import subprocess
import shutil

ROOT=Path(__file__).resolve().parent

import codex_composer_runner as runner
from prepare_payload import assemble, retry
import accept_output
import manual_capture
import sys
sys.path.insert(0,str(ROOT.parent.parent.parent/'integrations/composer-agent'))
import staged_harness as engine_gate
import test_staged_harness as gate_fixtures
import yaml

class XModel011OfflineTests(unittest.TestCase):
    def _write_synthetic_accepted(self,path:Path, data:bytes, stage:int=1):
        path.parent.mkdir(parents=True,exist_ok=True); path.write_bytes(data)
        digest=hashlib.sha256(data).hexdigest()
        proof={'status':'ACCEPTED_COPY_CREATED','gate_pass':True,'stage':stage,'source_sha256':digest,
               'accepted_sha256':digest,'byte_identical':True}
        path.with_name(path.name+'.acceptance.json').write_text(json.dumps(proof),encoding='utf-8')

    def test_inventory_hashes_and_history_exclusion(self):
        inv=json.loads((ROOT/'model-visible-inventory.json').read_text(encoding='utf-8'))
        self.assertEqual(inv['file_count'],len(inv['files']))
        for item in inv['files']:
            data=(ROOT/'model-visible'/item['path']).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(),item['sha256'])
        joined='\n'.join(x['path'] for x in inv['files'])
        self.assertNotRegex(joined,r'XMODEL-00[9]|XMODEL-010|failed|audit|ledger|test_')
        self.assertEqual(hashlib.sha256((ROOT/'model-visible/brief.yaml').read_bytes()).hexdigest(),
                         '464ae4378bcb7236f0fb36da52eb65dcb03735197284e3a6899b8686d51ede0b')

    def test_stage_one_payload_exact_brief_schema_and_manifest(self):
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/'stage-1/payload/attempt-1.txt'
            m=assemble(1,1,out)
            payload=out.read_bytes()
            self.assertIn((ROOT/'model-visible/brief.yaml').read_bytes(),payload)
            self.assertIn((ROOT/'model-visible/stage-1/output-schema.json').read_bytes(),payload)
            self.assertTrue(m['preflight']['pass'])
            self.assertTrue(out.with_name('payload-manifest.json').is_file())

    def test_exact_prepared_stage1_passes_runner_preflight_without_cli_call(self):
        payload=ROOT/'outputs/codex/stage-1/payload/revision-2/attempt-1-payload.txt'
        with tempfile.TemporaryDirectory() as td:
            req=runner.validate_request(experiment_id='XMODEL-011',stage=1,attempt=1,
                request_id='XMODEL-011-CODEX-STAGE1-A1',request_kind='evaluable_attempt',
                input_path=payload,output_dir=Path(td)/'capture',registry_dir=Path(td)/'registry')
            self.assertEqual(req['manifest']['payload_sha256'],hashlib.sha256(payload.read_bytes()).hexdigest())
            self.assertEqual(req['record']['status'],'RESERVED_NOT_SENT')

    def test_stage_payload_manifests_are_stage_isolated(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td)
            fake_root=d/'XMODEL-011'; shutil.copytree(ROOT/'model-visible',fake_root/'model-visible')
            shutil.copyfile(ROOT/'model-visible-inventory.json',fake_root/'model-visible-inventory.json')
            with patch('prepare_payload.ROOT',fake_root), patch('prepare_payload.MV',fake_root/'model-visible'):
                p1=fake_root/'outputs/codex/stage-1/payload/attempt-1/payload.txt'; assemble(1,1,p1)
                prior1=fake_root/'outputs/codex/stage-1/accepted/accepted-output.json'; self._write_synthetic_accepted(prior1,b'{"synthetic_structure":true}')
                p2=fake_root/'outputs/codex/stage-2/payload/attempt-1/payload.txt'; assemble(2,1,p2,prior1=prior1)
                prior2=fake_root/'outputs/codex/stage-2/accepted/accepted-output.json'; self._write_synthetic_accepted(prior2,b'{"synthetic_structure":true}',stage=2)
                p3=fake_root/'outputs/codex/stage-3/payload/attempt-1/payload.txt'; assemble(3,1,p3,prior1=prior1,prior2=prior2)
            self.assertEqual(len(list(fake_root.rglob('payload-manifest.json'))),3)
            self.assertIn(b'accepted-stage-1-output.json',p2.read_bytes())
            self.assertIn(b'accepted-stage-2-output.json',p3.read_bytes())

    def test_retry_is_original_plus_literal_diagnostic_and_caps_at_three(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td); original=d/'attempt-1.txt'; assemble(1,1,original)
            orig=original.read_bytes(); retry_path=d/'attempt-2/retry-input.txt'
            m=retry(1,2,original,'literal gate error: field absent',retry_path)
            self.assertTrue(retry_path.read_bytes().startswith(orig))
            self.assertIn(b'literal gate error: field absent',retry_path.read_bytes())
            self.assertFalse(m['preflight']['musical_suggestion_inserted'])
            with self.assertRaises(ValueError): retry(1,4,original,'x',d/'attempt-4.txt')

    def _request(self, td, suffix='A1'):
        d=Path(td); payload=d/'payload.txt'; payload.write_text('synthetic structural fixture only',encoding='utf-8')
        m={'stage':1,'attempt':1,'payload_sha256':hashlib.sha256(payload.read_bytes()).hexdigest(),
           'brief_sha256':'464ae4378bcb7236f0fb36da52eb65dcb03735197284e3a6899b8686d51ede0b',
           'preflight':{'pass':True}}
        payload.with_name('payload-manifest.json').write_text(json.dumps(m),encoding='utf-8')
        return dict(experiment_id='XMODEL-011',stage=1,attempt=1,request_id=f'XMODEL-011-CODEX-STAGE1-{suffix}',
                    request_kind='evaluable_attempt',input_path=payload,output_dir=d/'capture',registry_dir=d/'registry')

    def test_mock_cli_complete_capture_separates_events_final_and_stderr(self):
        with tempfile.TemporaryDirectory() as td:
            args=self._request(td); work=Path(td)/'isolated-workspace'
            fake=type('Args',(),{'experiment_id':args['experiment_id'],'stage':args['stage'],'attempt':args['attempt'],
                'request_id':args['request_id'],'request_kind':args['request_kind'],'input':str(args['input_path']),
                'output_dir':str(args['output_dir']),'request_registry':str(args['registry_dir']),
                'codex':'mock-codex','model':None,'execution_workspace':str(work),'timeout':10})()
            def fake_run(cmd, **kwargs):
                if cmd==['mock-codex','--version']:
                    return subprocess.CompletedProcess(cmd,0,'codex-cli mock-1\n','')
                prompt=kwargs['input']; self.assertEqual(prompt,args['input_path'].read_bytes())
                output=Path(cmd[cmd.index('--output-last-message')+1]); output.write_bytes(b'{"mock":true}')
                return subprocess.CompletedProcess(cmd,0,b'{"type":"turn.completed","server_model":"mock-served-model"}\n',b'operational log\n')
            with patch.object(runner,'verify_host_parent_history_isolation',return_value={'status':'PASS','historical_tree':'ABSENT'}), \
                 patch.object(runner,'verify_tool_sandbox_isolation',return_value={'status':'PASS','model_invoked':False}), \
                 patch.object(runner.subprocess,'run',side_effect=fake_run): result=runner.execute(fake)
            self.assertEqual(result['capture_status'],'CAPTURED')
            self.assertEqual(result['model_reported'],'mock-served-model')
            self.assertTrue(result['terminal_success_event_observed'])
            self.assertEqual((Path(td)/'capture/cli-events.jsonl').read_bytes(),b'{"type":"turn.completed","server_model":"mock-served-model"}\n')
            self.assertEqual((Path(td)/'capture/cli-stderr.txt').read_bytes(),b'operational log\n')
            self.assertTrue((work/'output-schema.json').is_file())
            with self.assertRaises((FileExistsError,ValueError)): runner.validate_request(**args)

    def test_failed_filesystem_preflight_stops_before_attempt_reservation(self):
        with tempfile.TemporaryDirectory() as td:
            args=self._request(td,'A1'); work=Path(td)/'isolated-workspace'
            fake=type('Args',(),{'experiment_id':args['experiment_id'],'stage':args['stage'],'attempt':args['attempt'],
                'request_id':args['request_id'],'request_kind':args['request_kind'],'input':str(args['input_path']),
                'output_dir':str(args['output_dir']),'request_registry':str(args['registry_dir']),
                'codex':'mock-codex','model':None,'execution_workspace':str(work),'timeout':10})()
            def fake_run(cmd, **kwargs):
                return subprocess.CompletedProcess(cmd,0,'codex-cli mock-1\n','')
            with patch.object(runner,'verify_host_parent_history_isolation',return_value={'status':'PASS','historical_tree':'ABSENT'}), \
                 patch.object(runner,'verify_tool_sandbox_isolation',side_effect=RuntimeError('synthetic access leak')), \
                 patch.object(runner.subprocess,'run',side_effect=fake_run) as mocked:
                with self.assertRaisesRegex(RuntimeError,'synthetic access leak'):
                    runner.execute(fake)
            self.assertEqual(mocked.call_count,1)  # --version only; no model request
            self.assertFalse((Path(td)/'registry').exists())
            self.assertFalse((Path(td)/'capture').exists())
            self.assertFalse(work.exists())

    def test_missing_terminal_event_never_counts_as_capture(self):
        with tempfile.TemporaryDirectory() as td:
            args=self._request(td,'A1'); work=Path(td)/'isolated-workspace'
            fake=type('Args',(),{'experiment_id':args['experiment_id'],'stage':args['stage'],'attempt':args['attempt'],
                'request_id':args['request_id'],'request_kind':args['request_kind'],'input':str(args['input_path']),
                'output_dir':str(args['output_dir']),'request_registry':str(args['registry_dir']),
                'codex':'mock-codex','model':None,'execution_workspace':str(work),'timeout':10})()
            def fake_run(cmd, **kwargs):
                if cmd==['mock-codex','--version']:
                    return subprocess.CompletedProcess(cmd,0,'codex-cli mock-1\n','')
                Path(cmd[cmd.index('--output-last-message')+1]).write_bytes(b'{"partial":')
                return subprocess.CompletedProcess(cmd,0,b'{"type":"item.completed"}\n',b'')
            with patch.object(runner,'verify_host_parent_history_isolation',return_value={'status':'PASS','historical_tree':'ABSENT'}), \
                 patch.object(runner,'verify_tool_sandbox_isolation',return_value={'status':'PASS','model_invoked':False}), \
                 patch.object(runner.subprocess,'run',side_effect=fake_run): result=runner.execute(fake)
            self.assertEqual(result['capture_status'],'CLI_FAILED_OR_INCOMPLETE')

    def test_nonzero_cli_exit_never_counts_as_capture(self):
        with tempfile.TemporaryDirectory() as td:
            args=self._request(td,'A1'); work=Path(td)/'isolated-workspace'
            fake=type('Args',(),{'experiment_id':args['experiment_id'],'stage':args['stage'],'attempt':args['attempt'],
                'request_id':args['request_id'],'request_kind':args['request_kind'],'input':str(args['input_path']),
                'output_dir':str(args['output_dir']),'request_registry':str(args['registry_dir']),
                'codex':'mock-codex','model':None,'execution_workspace':str(work),'timeout':10})()
            def fake_run(cmd, **kwargs):
                if cmd==['mock-codex','--version']:
                    return subprocess.CompletedProcess(cmd,0,'codex-cli mock-1\n','')
                return subprocess.CompletedProcess(cmd,7,b'',b'failed')
            with patch.object(runner,'verify_host_parent_history_isolation',return_value={'status':'PASS','historical_tree':'ABSENT'}), \
                 patch.object(runner,'verify_tool_sandbox_isolation',return_value={'status':'PASS','model_invoked':False}), \
                 patch.object(runner.subprocess,'run',side_effect=fake_run): result=runner.execute(fake)
            self.assertEqual(result['capture_status'],'CLI_FAILED_OR_INCOMPLETE')

    def test_generic_model_label_is_not_reported_as_served_identity(self):
        self.assertIsNone(runner.model_from_events(b'{"type":"turn.completed","model":"configured-alias"}\n'))

    def test_isolation_probe_fails_closed_when_any_read_boundary_is_open(self):
        fields={'IDENTITY':'steve\\codexsandboxoffline','REPO':'READABLE','HISTORICAL':'DENIED',
                'CODEX_HOME':'DENIED','WORKSPACE':'READABLE','SCHEMA':'READABLE','SCHEMA_SHA256':'hash'}
        failures=runner.isolation_probe_failures(fields,'hash')
        self.assertTrue(failures)
        self.assertTrue(any('REPO' in error for error in failures))

    def test_isolation_probe_accepts_only_closed_history_and_matching_schema(self):
        fields={'IDENTITY':'steve\\codexsandboxonline','REPO':'DENIED','HISTORICAL':'DENIED',
                'CODEX_HOME':'DENIED','WORKSPACE':'READABLE','SCHEMA':'READABLE','SCHEMA_SHA256':'hash'}
        self.assertEqual(runner.isolation_probe_failures(fields,'hash'),[])

    def test_filesystem_probe_targets_history_auth_and_stage_workspace(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td)
            script=runner.isolation_probe_script(d/'repo',d/'XMODEL-010'/'run-manifest.yaml',
                d/'codex-home',d/'workspace',d/'workspace'/'output-schema.json')
            self.assertIn("REPO=",script)
            self.assertIn("HISTORICAL=",script)
            self.assertIn("CODEX_HOME=",script)
            self.assertIn("WORKSPACE=",script)
            self.assertIn("SCHEMA_SHA256=",script)

    def test_host_parent_must_not_enumerate_a_historical_tree(self):
        with tempfile.TemporaryDirectory() as td:
            base=Path(td); history=base/'evaluations/composer-agent/XMODEL-010'
            history.mkdir(parents=True); (history/'synthetic-sentinel.txt').write_text('synthetic only')
            with self.assertRaisesRegex(RuntimeError,'codex exec parent can enumerate'):
                runner.verify_host_parent_history_isolation(base)
            (history/'synthetic-sentinel.txt').unlink(); history.rmdir()
            self.assertEqual(runner.verify_host_parent_history_isolation(base)['historical_tree'],'ABSENT')

    def test_accepted_output_copy_is_byte_identical_and_exclusive(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td); raw=d/'raw.txt'; raw.write_bytes(b'{"synthetic":true}\r\n')
            data=raw.read_bytes(); accepted=d/'accepted.json'
            capture={'capture_status':'CAPTURED','terminal_success_event_observed':True,
                'final_output_path':str(raw),'final_output_sha256':hashlib.sha256(data).hexdigest()}
            capfile=d/'capture.json'; capfile.write_text(json.dumps(capture),encoding='utf-8')
            gate=d/'gate.json'; gate.write_text(json.dumps({'pass':True,'stage':1,'semantic_repair_performed':False}),encoding='utf-8')
            proof=accept_output.accept(capfile,gate,accepted)
            self.assertEqual(accepted.read_bytes(),raw.read_bytes())
            self.assertTrue(proof['byte_identical'])
            self.assertTrue(accepted.with_name('accepted.json.acceptance.json').is_file())
            with self.assertRaises(FileExistsError):
                accept_output.accept(capfile,gate,accepted)

    def test_model_visible_does_not_have_historical_failed_plans(self):
        text='\n'.join(p.read_text(encoding='utf-8',errors='ignore') for p in (ROOT/'model-visible').rglob('*') if p.is_file())
        self.assertNotIn('XMODEL-009',text); self.assertNotIn('XMODEL-010',text)
        self.assertIn('song001_r1_steven_slate_map',text)
        self.assertIn('No PercussionMap identifiers are approved for XMODEL-011.',text)

    def test_manual_capture_reservation_and_complete_response_verification(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td)/'stage-1'; out=d/'attempts/attempt-1/capture'; registry=d/'request-registry'
            args=type('Args',(),{'stage':1,'attempt':1,'request_id':'XMODEL-011-CODEX-STAGE1-A1',
                'capture_dir':str(out),'registry_dir':str(registry)})()
            reserved=manual_capture.reserve(args)
            self.assertEqual(reserved['status'],'RESERVED_MANUAL_NOT_SENT')
            reg=registry/'XMODEL-011-CODEX-STAGE1-A1.json'
            manual_capture.mark_sent(type('Args',(),{'registry':str(reg)})())
            (out/'cli-events.jsonl').write_text('{"type":"turn.completed","server_model":"unit-fixture"}\n',encoding='utf-8')
            (out/'cli-stderr.txt').write_text('',encoding='utf-8')
            (out/'final-output.txt').write_text('{"synthetic_structure_only":true}',encoding='utf-8')
            manual_capture.record(type('Args',(),{'registry':str(reg),'exit_code':0,'cli_version':'fixture'})())
            verified=manual_capture.verify(type('Args',(),{'capture_manifest':str(out/'capture-manifest.json')})())
            self.assertTrue(verified['pass'])
            with self.assertRaises(FileExistsError): manual_capture.reserve(args)

    def test_manual_capture_incomplete_response_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td)/'stage-1'; out=d/'attempts/attempt-1/capture'; registry=d/'request-registry'
            args=type('Args',(),{'stage':1,'attempt':1,'request_id':'XMODEL-011-CODEX-STAGE1-A1',
                'capture_dir':str(out),'registry_dir':str(registry)})()
            manual_capture.reserve(args)
            reg=registry/'XMODEL-011-CODEX-STAGE1-A1.json'
            manual_capture.mark_sent(type('Args',(),{'registry':str(reg)})())
            (out/'cli-events.jsonl').write_text('{"type":"item.completed"}\n',encoding='utf-8')
            (out/'cli-stderr.txt').write_text('interrupted',encoding='utf-8')
            (out/'final-output.txt').write_text('{"partial":',encoding='utf-8')
            manifest=manual_capture.record(type('Args',(),{'registry':str(reg),'exit_code':130,'cli_version':'fixture'})())
            self.assertEqual(manifest['capture_status'],'CLI_FAILED_OR_INCOMPLETE')
            self.assertFalse(manual_capture.verify(type('Args',(),{'capture_manifest':str(out/'capture-manifest.json')})())['pass'])

    def test_all_included_schemas_and_yaml_parse(self):
        for p in (ROOT/'model-visible').rglob('*.json'):
            with self.subTest(path=str(p.relative_to(ROOT))): json.loads(p.read_text(encoding='utf-8'))
        for p in (ROOT/'model-visible').rglob('*.yaml'):
            with self.subTest(path=str(p.relative_to(ROOT))): self.assertIsNotNone(yaml.safe_load(p.read_text(encoding='utf-8')))

    def test_gate_capture_helper_calls_external_stage1_gate(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td); output=d/'synthetic-stage1.json'; result=d/'gate-result.json'
            output.write_text(json.dumps(gate_fixtures.valid_trace()),encoding='utf-8')
            events=d/'events.jsonl'; events.write_text('{"type":"turn.completed"}\n',encoding='utf-8')
            import manual_capture
            cap=d/'capture-manifest.json'
            manifest={'capture_status':'CAPTURED','stage':1,'final_output_path':str(output),
                'final_output_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
                'cli_events_path':str(events)}
            cap.write_text(json.dumps(manifest),encoding='utf-8')
            command=[sys.executable,str(ROOT/'gate_capture.py'),'--stage','1','--output',str(output),
                '--capture-manifest',str(cap),'--result',str(result)]
            proc=subprocess.run(command,capture_output=True,text=True,check=False)
            self.assertEqual(proc.returncode,0,proc.stdout+proc.stderr)
            self.assertTrue(json.loads(result.read_text(encoding='utf-8'))['pass'])

    def test_gate_capture_refuses_incomplete_or_unmanifested_capture(self):
        with tempfile.TemporaryDirectory() as td:
            d=Path(td); output=d/'synthetic-stage1.json'; result=d/'gate-result.json'
            output.write_text(json.dumps(gate_fixtures.valid_trace()),encoding='utf-8')
            command=[sys.executable,str(ROOT/'gate_capture.py'),'--stage','1','--output',str(output),
                '--capture-manifest',str(d/'missing.json'),'--result',str(result)]
            proc=subprocess.run(command,capture_output=True,text=True,check=False)
            self.assertEqual(proc.returncode,2)
            self.assertFalse(result.exists())

    def test_owner_command_is_manual_stage1_only_and_hash_pinned(self):
        text=(ROOT/'prepared-commands.ps1.txt').read_text(encoding='utf-8')
        self.assertIn("'exec --ephemeral",text)
        self.assertIn("'58646fd9fbef25c17b6b5cc7f846490989316f25d5084469d2b8b4cb074a423d'",text)
        self.assertIn('manual_capture.py\') mark-sent',text)
        self.assertIn('manual_capture.py\') verify',text)
        self.assertNotIn('codex_composer_runner.py',text)
        self.assertNotIn('--stage 2',text)
        self.assertNotIn('--stage 3',text)

    def test_real_engine_and_approved_drums_host_pass_unapproved_percussion_blocks(self):
        cfg=ROOT/'model-visible/host/host-config.yaml'
        with tempfile.TemporaryDirectory() as td:
            d=Path(td); valid=d/'valid-songplan.json'
            valid.write_text(json.dumps(gate_fixtures.valid_songplan()),encoding='utf-8')
            passed=engine_gate.gate(3,valid,host_config=cfg)
            self.assertTrue(passed['pass'],passed)
            self.assertEqual(passed['engine_validation']['status'],'PASS')
            plan=gate_fixtures.valid_songplan(); drum=plan['tracks'][1]
            drum['type']='percussion'; drum['kit_id']='synthetic-kit'; drum['map_id']='unapproved-map'
            for motif in drum['motifs']:
                for event in motif['events']:
                    event.pop('drum_voice',None); event['instrument']='hi-hat'; event['sounding_articulation']='open'
            blocked=d/'unapproved-percussion.json'; blocked.write_text(json.dumps(plan),encoding='utf-8')
            failed=engine_gate.gate(3,blocked,host_config=cfg)
            self.assertFalse(failed['pass'])
            self.assertIn('host_configuration_failure',failed['category'])
            self.assertFalse(any(d.rglob('*.mid')))

if __name__=='__main__': unittest.main(verbosity=2)
