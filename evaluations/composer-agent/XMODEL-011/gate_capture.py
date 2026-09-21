"""Persist an external staged_harness gate result as UTF-8 JSON without BOM."""
import argparse, hashlib, json, sys
from pathlib import Path

REPO=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(REPO/'integrations/composer-agent'))
import staged_harness
import manual_capture

def main():
 p=argparse.ArgumentParser(); p.add_argument('--stage',type=int,choices=(1,2,3),required=True); p.add_argument('--output',type=Path,required=True); p.add_argument('--result',type=Path,required=True); p.add_argument('--host-config',type=Path); p.add_argument('--capture-manifest',type=Path,required=True); a=p.parse_args()
 if not a.capture_manifest.is_file(): print('refusing gate: capture manifest missing',file=sys.stderr); return 2
 try: capture=json.loads(a.capture_manifest.read_text(encoding='utf-8'))
 except Exception as exc: print(f'refusing gate: invalid capture manifest: {exc}',file=sys.stderr); return 2
 event_path=Path(capture.get('cli_events_path',''))
 terminal=manual_capture.read_events(event_path)[0] if event_path.is_file() else False
 if not a.output.is_file() or capture.get('capture_status')!='CAPTURED' or capture.get('stage')!=a.stage or capture.get('final_output_sha256')!=hashlib.sha256(a.output.read_bytes()).hexdigest() or capture.get('final_output_path')!=str(a.output) or not terminal:
  print('refusing gate: capture is incomplete, wrong stage, or output hash mismatch',file=sys.stderr); return 2
 if a.result.exists(): print('refusing to overwrite gate result',file=sys.stderr); return 2
 result=staged_harness.gate(a.stage,a.output,host_config=a.host_config)
 a.result.parent.mkdir(parents=True,exist_ok=True)
 with a.result.open('xb') as f: f.write((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
 print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result.get('pass') else 1
if __name__=='__main__': raise SystemExit(main())
