"""Assemble isolated XMODEL-011 stage prompts and literal-diagnostic retries."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
MV=ROOT/'model-visible'
BRIEF_SHA='464ae4378bcb7236f0fb36da52eb65dcb03735197284e3a6899b8686d51ede0b'
NO_EXAMPLES=re.compile(r'\bSONG[-_ ]?00[1-4]\b|XMODEL-00[9]|XMODEL-010',re.I)
COMMON=['brief.yaml','system-contract-v1.1.md','interface/decision-schema.yaml',
 'interface/guardrails.yaml','interface/completion-checklist.yaml',
 'interface/approved-composition-knowledge.yaml','interface/indie-dance.yaml',
 'interface/n3-p-percussion-architecture.yaml']
STAGE_RECORDS={
 1: COMMON+['stage-1/prompt.txt','stage-1/output-schema.json','host/capabilities.md',
           'host/host-config.yaml','host/song001_r1_steven_slate_map.yaml'],
 2: COMMON+['stage-2/prompt.txt','stage-2/output-schema.json',
           'stage-2/musical-material-schema.yaml','stage-2/contract-validation-map.md'],
 3: ['brief.yaml','system-contract-v1.1.md','interface/songplan-v2-contract.yaml',
      'interface/guardrails.yaml','interface/approved-composition-knowledge.yaml',
      'interface/indie-dance.yaml','interface/n3-p-percussion-architecture.yaml',
      'stage-3/prompt.txt','stage-3/output-schema.json',
      'stage-3/engine-songplan-v2.schema.json','stage-3/serialization-contract.yaml',
      'host/capabilities.md','host/host-config.yaml','host/song001_r1_steven_slate_map.yaml']}

def h(b): return hashlib.sha256(b).hexdigest()
def inv_hash(): return h((ROOT/'model-visible-inventory.json').read_bytes())
def block(label,content):
 body=content if content.endswith('\n') else content+'\n'
 return f'\n\n===== BEGIN {label} =====\n{body}===== END {label} =====\n'
def verify_accepted(path:Path,stage:int):
 expected=(ROOT/f'outputs/codex/stage-{stage}/accepted/accepted-output.json').resolve()
 if path.resolve()!=expected: raise ValueError(f'prior Stage {stage} must be XMODEL-011 accepted-output.json')
 proof_path=path.with_name(path.name+'.acceptance.json')
 if not proof_path.is_file(): raise ValueError(f'prior Stage {stage} lacks external gate acceptance manifest')
 proof=json.loads(proof_path.read_text(encoding='utf-8'))
 data=path.read_bytes()
 if proof.get('status')!='ACCEPTED_COPY_CREATED' or proof.get('gate_pass') is not True:
  raise ValueError(f'prior Stage {stage} is not accepted')
 if proof.get('stage')!=stage: raise ValueError(f'prior acceptance proof is for another stage, expected {stage}')
 if proof.get('accepted_sha256')!=h(data) or proof.get('source_sha256')!=h(data) or proof.get('byte_identical') is not True:
  raise ValueError(f'prior Stage {stage} acceptance hash mismatch')
def assemble(stage:int,attempt:int,out:Path,prior1:Path|None=None,prior2:Path|None=None):
 if stage not in (1,2,3) or not (1<=attempt<=3): raise ValueError('invalid stage/attempt')
 if stage>1 and not prior1: raise ValueError('accepted Stage 1 output is required')
 if stage==3 and not prior2: raise ValueError('accepted Stage 2 output is required')
 if prior1: verify_accepted(prior1,1)
 if prior2: verify_accepted(prior2,2)
 out=out.resolve(); mf=out.with_name('payload-manifest.json')
 if out.exists() or mf.exists(): raise FileExistsError('refusing to overwrite frozen payload or manifest')
 required=STAGE_RECORDS[stage]
 pieces=[f'XMODEL-011 composer request. Stage {stage}, attempt {attempt}.\n'
         'Use only these supplied records. Return only the requested stage output.\n']
 resolved=[]
 for rel in required:
  p=MV/rel
  if not p.is_file(): raise FileNotFoundError(f'required model-visible record missing: {rel}')
  data=p.read_bytes(); content=data.decode('utf-8')
  pieces.append(block(rel,content)); resolved.append({'path':f'model-visible/{rel}','sha256':h(data)})
 if prior1:
  b=prior1.read_bytes(); pieces.append(block('accepted-stage-1-output.json',b.decode('utf-8')))
  resolved.append({'path':str(prior1.resolve()),'sha256':h(b),'role':'accepted_prior_stage_1'})
 if prior2:
  b=prior2.read_bytes(); pieces.append(block('accepted-stage-2-output.json',b.decode('utf-8')))
  resolved.append({'path':str(prior2.resolve()),'sha256':h(b),'role':'accepted_prior_stage_2'})
 payload=''.join(pieces).encode('utf-8')
 # Mechanical context check: exact brief and prompt bytes are present.
 brief=(MV/'brief.yaml').read_bytes(); prompt=(MV/f'stage-{stage}/prompt.txt').read_bytes()
 errors=[]
 if brief not in payload: errors.append('exact frozen brief absent')
 if prompt not in payload: errors.append('stage instruction absent')
 try: text=payload.decode('utf-8')
 except UnicodeDecodeError: errors.append('payload is not UTF-8'); text=''
 if NO_EXAMPLES.search(text): errors.append('historical example reference detected')
 if stage>1 and not prior1: errors.append('accepted Stage 1 output absent')
 if stage==3 and not prior2: errors.append('accepted Stage 2 output absent')
 if errors: raise ValueError('; '.join(errors))
 out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('xb') as f:f.write(payload)
 manifest={'experiment_id':'XMODEL-011','stage':stage,'attempt':attempt,
  'payload_path':str(out),'payload_sha256':h(payload),'payload_bytes':len(payload),
  'brief_sha256':h(brief),'interface_version':'composer-interface-v1.1',
  'model_visible_inventory_sha256':inv_hash(),'resolved_records':resolved,
  'prior_stage_1_sha256':h(prior1.read_bytes()) if prior1 else None,
  'prior_stage_2_sha256':h(prior2.read_bytes()) if prior2 else None,
  'preflight':{'pass':True,'errors':[],'exact_brief_present':True,
   'stage_instruction_present':True,'required_records_resolved':True,
   'forbidden_historical_examples_absent':True,
   'prior_stage_1_present_when_required':stage==1 or bool(prior1),
   'prior_stage_2_present_when_required':stage<3 or bool(prior2)}}
 with mf.open('xb') as f:f.write((json.dumps(manifest,indent=2,ensure_ascii=False)+'\n').encode())
 return manifest

def retry(stage:int,attempt:int,original:Path,diagnostic:str,out:Path):
 if attempt not in (2,3): raise ValueError('retries are only attempts 2 or 3')
 if not diagnostic or '\n' in diagnostic or '\r' in diagnostic: raise ValueError('diagnostic must be one literal line')
 original=original.resolve(); source_manifest=original.with_name('payload-manifest.json')
 if not source_manifest.is_file(): raise ValueError('original payload manifest missing')
 source_meta=json.loads(source_manifest.read_text(encoding='utf-8'))
 source_bytes=original.read_bytes()
 if source_meta.get('stage')!=stage or source_meta.get('attempt')!=1:
  raise ValueError('retries must branch from the frozen Stage attempt-1 payload')
 if source_meta.get('payload_sha256')!=h(source_bytes): raise ValueError('original payload hash mismatch')
 orig=source_bytes; text=orig.decode('utf-8')
 suffix=block('literal previous external gate diagnostic',diagnostic)
 payload=(text+suffix).encode('utf-8'); out=out.resolve(); mf=out.with_name('payload-manifest.json')
 if out.exists() or mf.exists(): raise FileExistsError('refusing overwrite')
 out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('xb') as f:f.write(payload)
 m=json.loads(original.with_name('payload-manifest.json').read_text(encoding='utf-8'))
 m.update({'attempt':attempt,'payload_path':str(out),'payload_sha256':h(payload),
  'payload_bytes':len(payload),'retry_of_payload_sha256':h(orig),
  'original_payload_path':str(original),
  'literal_gate_diagnostic':diagnostic,'preflight':{'pass':True,'errors':[],
  'original_frozen_payload_present':True,'literal_previous_diagnostic_present':diagnostic in text+suffix,
  'musical_suggestion_inserted':False}})
 with mf.open('xb') as f:f.write((json.dumps(m,indent=2,ensure_ascii=False)+'\n').encode())
 return m

def main():
 p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='cmd',required=True)
 a=sub.add_parser('assemble'); a.add_argument('--stage',type=int,required=True); a.add_argument('--attempt',type=int,default=1); a.add_argument('--prior-stage-1',type=Path); a.add_argument('--prior-stage-2',type=Path); a.add_argument('--out',type=Path,required=True)
 r=sub.add_parser('retry'); r.add_argument('--stage',type=int,required=True); r.add_argument('--attempt',type=int,required=True); r.add_argument('--original',type=Path,required=True); r.add_argument('--diagnostic',required=True); r.add_argument('--out',type=Path,required=True)
 x=p.parse_args()
 try:
  result=assemble(x.stage,x.attempt,x.out,x.prior_stage_1,x.prior_stage_2) if x.cmd=='assemble' else retry(x.stage,x.attempt,x.original,x.diagnostic,x.out)
  print(json.dumps(result,indent=2,ensure_ascii=False)); return 0
 except Exception as e: print(json.dumps({'pass':False,'error':f'{type(e).__name__}: {e}'},indent=2)); return 1
if __name__=='__main__': raise SystemExit(main())
