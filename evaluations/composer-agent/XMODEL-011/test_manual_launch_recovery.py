from __future__ import annotations
import hashlib, json, tempfile, unittest, subprocess, sys
from pathlib import Path
from unittest.mock import patch
import manual_launch_recovery as recovery

class ManualLaunchRecoveryTests(unittest.TestCase):
    def test_global_approval_option_order_rejects_historical_shape(self):
        self.assertFalse(recovery.approval_order_is_valid(["exec","--ephemeral","--ask-for-approval","never"]))
        self.assertTrue(recovery.approval_order_is_valid(recovery.recovery_cli_args("cwd","schema","final")))

    def test_corrected_command_keeps_frozen_sandbox_and_no_model_or_bypass(self):
        args=recovery.recovery_cli_args("C:/tmp/work","C:/schema.json","C:/final.txt")
        self.assertEqual(args[:3],["--ask-for-approval","never","exec"])
        self.assertIn("--sandbox",args); self.assertEqual(args[args.index("--sandbox")+1],"read-only")
        self.assertNotIn("--model",args)
        self.assertNotIn("--dangerously-bypass-approvals-and-sandbox",args)

    def test_recovery_id_is_unique_technical_request_not_attempt_two(self):
        self.assertEqual(recovery.RECOVERY_ID,"XMODEL-011-CODEX-STAGE1-A1-LAUNCH-RECOVERY-001")
        self.assertIn("LAUNCH-RECOVERY",recovery.RECOVERY_ID)

    def test_historical_failed_launch_hashes_and_classification_unchanged(self):
        snapshot=recovery.historical_snapshot()
        self.assertEqual(snapshot["classification"],"CLI_ARGUMENT_PARSE_FAILURE; PRE_INFERENCE_TECHNICAL_FAILURE")
        self.assertEqual(snapshot["model_inference_evidence"],"NONE; zero-byte events, parser rejected CLI arguments before turn")
        self.assertEqual(snapshot["evaluable_attempt_count"],0)
        self.assertEqual(snapshot["registry_sha256"],"261efd0b945e1266d57373b896243de08a97e0029d58386ec41cbe6bc77f9658")
        self.assertEqual(snapshot["events_sha256"],"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
        self.assertEqual(snapshot["stderr_sha256"],"c206a405769cb087010d604fab55fd38b0612d2dfc6435797cfba6df5240b7e7")

    def test_payload_frozen_hash_unchanged(self):
        self.assertEqual(recovery.sha(recovery.PAYLOAD.read_bytes()),recovery.EXPECTED_PAYLOAD)

    def _fixture_paths(self, td):
        d=Path(td); oldcap=d/'old/capture'; oldreg=d/'old/registry.json'; oldcap.mkdir(parents=True)
        oldreg.write_text(json.dumps({'request_id':recovery.OLD_ID,'status':'SENT_MANUAL'}),encoding='utf-8')
        (oldcap/'cli-events.jsonl').write_bytes(b'')
        (oldcap/'cli-stderr.txt').write_text("error: unexpected argument '--ask-for-approval' found\n",encoding='utf-8')
        rec=d/'recovery'; payload=recovery.PAYLOAD
        values={'RECOVERY':rec,'CAPTURE':rec/'capture','RECORD':rec/'request-record.json',
                'OLD_REG':oldreg,'OLD_CAPTURE':oldcap,'PAYLOAD':payload}
        return d,values

    def test_prepared_request_has_zero_evaluable_attempts_and_new_launch_count(self):
        with tempfile.TemporaryDirectory() as td:
            d,values=self._fixture_paths(td)
            with patch.multiple(recovery,**values):
                r=recovery.init(None)
                self.assertEqual(r['status'],'PREPARED_NOT_SENT')
                self.assertEqual(r['total_cli_launch_requests_before_recovery'],1)
                self.assertEqual(r['total_cli_launch_requests_if_owner_sends_recovery'],2)
                self.assertEqual(r['evaluable_composer_attempts_before_response_and_gate'],0)
                self.assertFalse((recovery.CAPTURE).exists())

    def test_prepared_command_documents_correct_order_and_exclusive_paths(self):
        text=(recovery.ROOT/'prepared-commands-recovery-001.ps1.txt').read_text(encoding='utf-8')
        self.assertIn("$cliArgs = '--ask-for-approval never exec",text)
        self.assertIn("A1-LAUNCH-RECOVERY-001",text)
        self.assertIn("technical-recoveries/launch-recovery-001",text)
        self.assertIn("- < \"{3}\" 1> \"{4}\" 2> \"{5}\"",text)
        self.assertNotIn("--dangerously-bypass-approvals-and-sandbox",text)
        cli_line=next(line for line in text.splitlines() if line.startswith("$cliArgs ="))
        self.assertNotIn("--model",cli_line)

    def test_mark_sent_is_single_use_and_fresh_capture_path(self):
        with tempfile.TemporaryDirectory() as td:
            _,values=self._fixture_paths(td)
            with patch.multiple(recovery,**values):
                recovery.init(None); recovery.mark_sent(None)
                self.assertTrue(recovery.CAPTURE.is_dir())
                with self.assertRaises(ValueError): recovery.mark_sent(None)

    def test_missing_final_output_is_not_gateable(self):
        with tempfile.TemporaryDirectory() as td:
            _,values=self._fixture_paths(td)
            with patch.multiple(recovery,**values):
                recovery.init(None); recovery.mark_sent(None)
                (recovery.CAPTURE/'cli-events.jsonl').write_text('',encoding='utf-8')
                (recovery.CAPTURE/'cli-stderr.txt').write_text('parser failure',encoding='utf-8')
                m=recovery.record(type('Args',(),{'exit_code':2})())
                self.assertEqual(m['classification'],'TECHNICAL_FAILURE; inference status recorded from available events')
                self.assertFalse(recovery.verify(type('Args',(),{'manifest':str(recovery.CAPTURE/'capture-manifest.json')})())['pass'])
                cmd=[sys.executable,str(recovery.ROOT/'gate_capture.py'),'--stage','1',
                    '--output',str(recovery.CAPTURE/'final-output.txt'),
                    '--capture-manifest',str(recovery.CAPTURE/'capture-manifest.json'),
                    '--result',str(recovery.RECOVERY/'gate-result.json')]
                gate=subprocess.run(cmd,capture_output=True,text=True,check=False)
                self.assertEqual(gate.returncode,2)
                self.assertFalse((recovery.RECOVERY/'gate-result.json').exists())

    def test_terminal_event_required_and_midturn_failure_is_recorded(self):
        with tempfile.TemporaryDirectory() as td:
            _,values=self._fixture_paths(td)
            with patch.multiple(recovery,**values):
                recovery.init(None); recovery.mark_sent(None)
                (recovery.CAPTURE/'cli-events.jsonl').write_text('{"type":"turn.started"}\n',encoding='utf-8')
                (recovery.CAPTURE/'cli-stderr.txt').write_text('transport error',encoding='utf-8')
                (recovery.CAPTURE/'final-output.txt').write_text('{"partial":',encoding='utf-8')
                m=recovery.record(type('Args',(),{'exit_code':1})())
                self.assertTrue(m['inference_event_evidence'])
                self.assertFalse(m['terminal_success_event_observed'])
                self.assertEqual(m['capture_status'],'CLI_FAILED_OR_INCOMPLETE')

    def test_duplicate_recovery_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            _,values=self._fixture_paths(td)
            with patch.multiple(recovery,**values):
                recovery.init(None)
                with self.assertRaises(FileExistsError): recovery.init(None)

if __name__=='__main__': unittest.main(verbosity=2)
