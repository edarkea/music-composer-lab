from __future__ import annotations
import hashlib,json,subprocess,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import manual_launch_recovery_002 as r

class Recovery002Tests(unittest.TestCase):
    def test_global_approval_order_skip_git_and_readonly(self):
        args=r.build_args('cwd','schema','final')
        self.assertTrue(r.validate_cli_order(args))
        self.assertFalse(r.validate_cli_order(['exec','--ephemeral','--ask-for-approval','never']))
        self.assertIn('--skip-git-repo-check',args)
        self.assertEqual(args[args.index('--sandbox')+1],'read-only')
        self.assertNotIn('--dangerously-bypass-approvals-and-sandbox',args)
        self.assertNotIn('--model',args)

    def test_payload_hash_unchanged(self):
        self.assertEqual(r.sha(r.PAYLOAD.read_bytes()),r.EXPECTED_PAYLOAD)

    def test_request_id_is_unique_and_same_evaluable_attempt_one(self):
        self.assertEqual(r.RID,'XMODEL-011-CODEX-STAGE1-A1-LAUNCH-RECOVERY-002')
        self.assertNotEqual(r.RID,r.OLD1_ID)
        self.assertNotEqual(r.RID,r.REC1_ID)

    def test_historical_launches_preserved_and_zero_attempts_consumed(self):
        s=r.historical_snapshot()
        self.assertEqual(s['evaluable_attempts_consumed'],0)
        self.assertEqual(s['request_1']['sha256'],r.OLD1_EXPECTED)
        self.assertEqual(s['request_2']['sha256'],r.REC1_EXPECTED)
        self.assertEqual(s['request_2']['classification'],'PRE_INFERENCE_TECHNICAL_FAILURE; CLI_TRUSTED_DIRECTORY_CHECK_FAILURE')
        self.assertFalse(s['request_2']['inference_event_evidence'])

    def test_prepared_command_has_skip_git_and_correct_order(self):
        text=(r.ROOT/'prepared-commands-recovery-002.ps1.txt').read_text(encoding='utf-8')
        line=next(x for x in text.splitlines() if x.startswith('$cliArgs ='))
        self.assertTrue(line.index('--ask-for-approval never') < line.index('exec'))
        self.assertIn('--skip-git-repo-check',line)
        self.assertIn('--sandbox read-only',line)
        self.assertNotIn('--model',line)

    def _fixtures(self,td):
        d=Path(td); old1=d/'old1'; old1cap=old1/'capture'; old1cap.mkdir(parents=True)
        old1reg=old1/'registry.json'; old1reg.write_text(json.dumps({'request_id':r.OLD1_ID,'status':'SENT_MANUAL'}),encoding='utf-8')
        (old1cap/'cli-events.jsonl').write_bytes(b'')
        (old1cap/'cli-stderr.txt').write_text("error: unexpected argument '--ask-for-approval' found\n",encoding='utf-8')
        rec1=d/'recovery-001'; cap1=rec1/'capture'; cap1.mkdir(parents=True)
        rec1reg=rec1/'request-record.json'; rec1reg.write_text(json.dumps({'request_id':r.REC1_ID,'cli_exit_status':1}),encoding='utf-8')
        (cap1/'cli-events.jsonl').write_bytes(b'')
        (cap1/'cli-stderr.txt').write_text('Not inside a trusted directory and --skip-git-repo-check was not specified.\n',encoding='utf-8')
        m={'request_id':r.REC1_ID,'cli_exit_status':1,'inference_event_evidence':False,'terminal_success_event_observed':False}
        (cap1/'capture-manifest.json').write_text(json.dumps(m),encoding='utf-8')
        recovery=d/'recovery-002'
        old1expect={'registry':r.sha(old1reg.read_bytes()),'events':r.sha((old1cap/'cli-events.jsonl').read_bytes()),'stderr':r.sha((old1cap/'cli-stderr.txt').read_bytes())}
        rec1expect={'record':r.sha(rec1reg.read_bytes()),'events':r.sha((cap1/'cli-events.jsonl').read_bytes()),'stderr':r.sha((cap1/'cli-stderr.txt').read_bytes()),'manifest':r.sha((cap1/'capture-manifest.json').read_bytes())}
        vals={'OLD1_REG':old1reg,'OLD1_CAP':old1cap,'OLD1_EXPECTED':old1expect,'REC1':rec1,'REC1_EXPECTED':rec1expect,'RECOVERY':recovery,'CAPTURE':recovery/'capture','RECORD':recovery/'request-record.json'}
        return vals

    def test_new_request_prepared_exclusively_and_counter_zero(self):
        with tempfile.TemporaryDirectory() as td:
            vals=self._fixtures(td)
            with patch.multiple(r,**vals):
                rec=r.prepare(None)
                self.assertEqual(rec['status'],'PREPARED_NOT_SENT')
                self.assertEqual(rec['evaluable_attempts_consumed'],0)
                self.assertEqual(rec['cli_launch_requests_before_this_recovery'],2)
                self.assertEqual(rec['cli_launch_requests_if_owner_sends_this_recovery'],3)
                self.assertTrue(r.CAPTURE.is_dir())
                self.assertEqual(list(r.CAPTURE.iterdir()),[])
                with self.assertRaises(FileExistsError): r.prepare(None)

    def test_mark_sent_creates_new_unique_capture_only(self):
        with tempfile.TemporaryDirectory() as td:
            vals=self._fixtures(td)
            with patch.multiple(r,**vals):
                r.prepare(None); r.mark_sent(None)
                self.assertTrue(r.CAPTURE.is_dir())
                with self.assertRaises(ValueError): r.mark_sent(None)

    def test_no_terminal_event_or_output_cannot_pass_gate(self):
        with tempfile.TemporaryDirectory() as td:
            vals=self._fixtures(td)
            with patch.multiple(r,**vals):
                r.prepare(None); r.mark_sent(None)
                (r.CAPTURE/'cli-events.jsonl').write_text('{"type":"turn.started"}\n',encoding='utf-8')
                (r.CAPTURE/'cli-stderr.txt').write_text('interrupted',encoding='utf-8')
                m=r.record(type('Args',(),{'exit_code':1})())
                self.assertTrue(m['inference_event_evidence'])
                self.assertFalse(m['terminal_success_event_observed'])
                v=r.verify(type('Args',(),{'manifest':str(r.CAPTURE/'capture-manifest.json')})())
                self.assertFalse(v['pass'])
                cmd=[sys.executable,str(r.ROOT/'gate_capture.py'),'--stage','1','--output',str(r.CAPTURE/'final-output.txt'),
                     '--capture-manifest',str(r.CAPTURE/'capture-manifest.json'),'--result',str(r.RECOVERY/'gate-result.json')]
                gate=subprocess.run(cmd,capture_output=True,text=True,check=False)
                self.assertEqual(gate.returncode,2)
                self.assertFalse((r.RECOVERY/'gate-result.json').exists())

    def test_pre_inference_empty_events_is_classified(self):
        with tempfile.TemporaryDirectory() as td:
            vals=self._fixtures(td)
            with patch.multiple(r,**vals):
                r.prepare(None); r.mark_sent(None)
                (r.CAPTURE/'cli-events.jsonl').write_bytes(b'')
                (r.CAPTURE/'cli-stderr.txt').write_text('Not inside a trusted directory',encoding='utf-8')
                m=r.record(type('Args',(),{'exit_code':1})())
                self.assertEqual(m['classification'],'PRE_INFERENCE_TECHNICAL_FAILURE; CLI_TRUSTED_DIRECTORY_CHECK_FAILURE')
                self.assertFalse(m['inference_event_evidence'])

if __name__=='__main__': unittest.main(verbosity=2)
