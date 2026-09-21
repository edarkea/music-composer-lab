"""Make a byte-identical accepted-output copy only after a passing external gate."""
import argparse, hashlib, json
from pathlib import Path

def accept(capture_manifest:Path, gate_result:Path, output:Path):
 cap=json.loads(capture_manifest.read_text(encoding='utf-8')); gate=json.loads(gate_result.read_text(encoding='utf-8'))
 if cap.get('capture_status')!='CAPTURED' or cap.get('terminal_success_event_observed') is not True: raise ValueError('capture is not complete')
 if gate.get('pass') is not True or gate.get('semantic_repair_performed') is not False: raise ValueError('external gate did not PASS without semantic repair')
 src=Path(cap['final_output_path']); data=src.read_bytes(); digest=hashlib.sha256(data).hexdigest()
 if digest!=cap.get('final_output_sha256'): raise ValueError('raw output hash mismatch')
 output.parent.mkdir(parents=True,exist_ok=True)
 with output.open('xb') as f: f.write(data)
 proof={'status':'ACCEPTED_COPY_CREATED','gate_pass':True,'stage':gate.get('stage'),'gate_result_sha256':hashlib.sha256(gate_result.read_bytes()).hexdigest(),
  'source_path':str(src.resolve()),'source_sha256':digest,'accepted_path':str(output.resolve()),
  'accepted_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'byte_identical':output.read_bytes()==data}
 with output.with_name(output.name+'.acceptance.json').open('xb') as f:f.write((json.dumps(proof,indent=2)+'\n').encode())
 if not proof['byte_identical']: raise ValueError('accepted output differs from source')
 return proof

def main():
 p=argparse.ArgumentParser(); p.add_argument('--capture-manifest',required=True,type=Path); p.add_argument('--gate-result',required=True,type=Path); p.add_argument('--output',required=True,type=Path); a=p.parse_args()
 try: print(json.dumps(accept(a.capture_manifest,a.gate_result,a.output),indent=2)); return 0
 except Exception as e: print(json.dumps({'status':'BLOCKED','error':f'{type(e).__name__}: {e}'},indent=2)); return 1
if __name__=='__main__': raise SystemExit(main())
