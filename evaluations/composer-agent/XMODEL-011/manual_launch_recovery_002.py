"""Offline bookkeeping for XMODEL-011 CLI launch recovery 002; never invokes Codex."""
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
STAGE=ROOT/'outputs/codex/stage-1'
PAYLOAD=STAGE/'payload/revision-2/attempt-1-payload.txt'
EXPECTED_PAYLOAD='58646fd9fbef25c17b6b5cc7f846490989316f25d5084469d2b8b4cb074a423d'
OLD1_ID='XMODEL-011-CODEX-STAGE1-A1'
OLD1_REG=STAGE/'request-registry'/f'{OLD1_ID}.json'
OLD1_CAP=STAGE/'attempts/attempt-1/capture'
OLD1_EXPECTED={'registry':'261efd0b945e1266d57373b896243de08a97e0029d58386ec41cbe6bc77f9658',
    'events':'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
    'stderr':'c206a405769cb087010d604fab55fd38b0612d2dfc6435797cfba6df5240b7e7'}
REC1=STAGE/'technical-recoveries/launch-recovery-001'
REC1_ID='XMODEL-011-CODEX-STAGE1-A1-LAUNCH-RECOVERY-001'
REC1_EXPECTED={'record':'b1cc9e4b63b6d404b8e8d9240326837aabd5b94c046a18549d9c99cac25e2936',
    'events':'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
    'stderr':'dd701e712037bba81445e9a92376e3d3af69acac5f0187ec904e9ed3c401324d',
    'manifest':'b37b20b6c3348a8d12f2f4546a6e0e5c8778307809c8ee1855a498aacd5bad00'}
RID='XMODEL-011-CODEX-STAGE1-A1-LAUNCH-RECOVERY-002'
RECOVERY=STAGE/'technical-recoveries/launch-recovery-002'
CAPTURE=RECOVERY/'capture'
RECORD=RECOVERY/'request-record.json'

def sha(b:bytes)->str: return hashlib.sha256(b).hexdigest()
def now()->str: return datetime.now(timezone.utc).isoformat()

def build_args(workspace:str,schema:str,final:str)->list[str]:
    return ['--ask-for-approval','never','exec','--ephemeral','--ignore-user-config','--ignore-rules',
        '--sandbox','read-only','--skip-git-repo-check','--cd',workspace,'--json',
        '--output-schema',schema,'--output-last-message',final,'-']

def validate_cli_order(args:list[str])->bool:
    try: return args.index('--ask-for-approval')<args.index('exec') and args.index('--skip-git-repo-check')>args.index('exec')
    except ValueError: return False

def _file_hash(p:Path)->str: return sha(p.read_bytes())

def historical_snapshot()->dict:
    if sha(PAYLOAD.read_bytes())!=EXPECTED_PAYLOAD: raise ValueError('frozen payload hash mismatch')
    r1=json.loads(OLD1_REG.read_text(encoding='utf-8'))
    e1=OLD1_CAP/'cli-events.jsonl'; s1=OLD1_CAP/'cli-stderr.txt'
    if r1.get('status')!='SENT_MANUAL' or e1.stat().st_size!=0 or "unexpected argument '--ask-for-approval' found" not in s1.read_text(encoding='utf-8',errors='replace'):
        raise ValueError('historical A1 parse failure evidence changed')
    if (OLD1_CAP/'final-output.txt').exists() or (OLD1_CAP/'capture-manifest.json').exists(): raise ValueError('unexpected A1 output/manifest')
    h1={'registry':_file_hash(OLD1_REG),'events':_file_hash(e1),'stderr':_file_hash(s1)}
    if h1!=OLD1_EXPECTED: raise ValueError('historical A1 hashes changed')
    rr=json.loads((REC1/'request-record.json').read_text(encoding='utf-8'))
    m1=json.loads((REC1/'capture/capture-manifest.json').read_text(encoding='utf-8'))
    e2=REC1/'capture/cli-events.jsonl'; s2=REC1/'capture/cli-stderr.txt'
    err=s2.read_text(encoding='utf-8',errors='replace')
    if rr.get('request_id')!=REC1_ID or rr.get('cli_exit_status')!=1: raise ValueError('recovery-001 request record changed')
    if m1.get('request_id')!=REC1_ID or m1.get('cli_exit_status')!=1 or m1.get('inference_event_evidence') is not False or m1.get('terminal_success_event_observed') is not False: raise ValueError('recovery-001 failure manifest changed')
    if e2.stat().st_size!=0 or 'Not inside a trusted directory and --skip-git-repo-check was not specified.' not in err: raise ValueError('recovery-001 failure evidence changed')
    if (REC1/'capture/final-output.txt').exists(): raise ValueError('unexpected recovery-001 final output')
    h2={'record':_file_hash(REC1/'request-record.json'),'events':_file_hash(e2),'stderr':_file_hash(s2),'manifest':_file_hash(REC1/'capture/capture-manifest.json')}
    if h2!=REC1_EXPECTED: raise ValueError('recovery-001 hashes changed')
    return {
      'request_1':{'request_id':OLD1_ID,'classification':'CLI_ARGUMENT_PARSE_FAILURE; PRE_INFERENCE_TECHNICAL_FAILURE','model_inference_evidence':'NONE','sha256':h1},
      'request_2':{'request_id':REC1_ID,'classification':'PRE_INFERENCE_TECHNICAL_FAILURE; CLI_TRUSTED_DIRECTORY_CHECK_FAILURE','cli_exit_status':1,'inference_event_evidence':False,'terminal_success_event_observed':False,'events_bytes':0,'stderr':err.strip(),'final_output_exists':False,'sha256':h2},
      'evaluable_attempts_consumed':0
    }

def prepare(args)->dict:
    snap=historical_snapshot()
    if RECOVERY.exists(): raise FileExistsError('recovery-002 path already exists; do not overwrite')
    RECOVERY.mkdir(parents=True,exist_ok=False)
    CAPTURE.mkdir(parents=True,exist_ok=False)
    r={'experiment_id':'XMODEL-011','stage':1,'evaluable_attempt':1,'request_id':RID,
       'request_kind':'technical_launch_recovery','status':'PREPARED_NOT_SENT','counts_as_evaluable_attempt':False,
       'cli_launch_requests_before_this_recovery':2,'cli_launch_requests_if_owner_sends_this_recovery':3,
       'evaluable_attempts_consumed':0,'payload_path':str(PAYLOAD),'payload_sha256':EXPECTED_PAYLOAD,
       'historical_failures':snap,'cli_version':'codex-cli 0.154.0-alpha.6.2','model_requested':None,
       'approved_cli_option_order':'codex --ask-for-approval never exec ... --skip-git-repo-check ...',
       'sandbox':'read-only','created_at_utc':now()}
    with RECORD.open('xb') as f: f.write((json.dumps(r,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
    return r

def mark_sent(args)->dict:
    r=json.loads(RECORD.read_text(encoding='utf-8'))
    if r.get('request_id')!=RID or r.get('status')!='PREPARED_NOT_SENT': raise ValueError('request not fresh PREPARED_NOT_SENT')
    historical_snapshot()
    if sha(PAYLOAD.read_bytes())!=EXPECTED_PAYLOAD: raise ValueError('payload changed')
    if not CAPTURE.is_dir() or any(CAPTURE.iterdir()): raise FileExistsError('recovery-002 capture path missing or not empty')
    r.update({'status':'SENT_MANUAL','sent_marked_at_utc':now()})
    RECORD.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return r

def record(args)->dict:
    r=json.loads(RECORD.read_text(encoding='utf-8'))
    if r.get('status')!='SENT_MANUAL': raise ValueError('request is not newly sent')
    ev,err,final=CAPTURE/'cli-events.jsonl',CAPTURE/'cli-stderr.txt',CAPTURE/'final-output.txt'
    for p in (ev,err):
        if not p.is_file(): raise FileNotFoundError(f'missing capture: {p}')
    eb,sb=ev.read_bytes(),err.read_bytes(); fb=final.read_bytes() if final.is_file() else b''
    parsed=[]
    for line in eb.splitlines():
        try:
            v=json.loads(line)
            if isinstance(v,dict): parsed.append(v)
        except Exception: pass
    terminal=any(e.get('type')=='turn.completed' for e in parsed)
    activity=any(e.get('type') in ('turn.started','item.started','item.completed','turn.completed') for e in parsed)
    complete=args.exit_code==0 and terminal and bool(fb)
    stderr_text=sb.decode('utf-8','replace')
    if len(eb)==0 and args.exit_code!=0 and 'Not inside a trusted directory' in stderr_text:
        classification='PRE_INFERENCE_TECHNICAL_FAILURE; CLI_TRUSTED_DIRECTORY_CHECK_FAILURE'
    elif len(eb)==0 and args.exit_code!=0: classification='PRE_INFERENCE_TECHNICAL_FAILURE'
    elif complete: classification='TECHNICAL_RECOVERY_COMPLETE_RESPONSE_READY_FOR_GATE'
    else: classification='INCOMPLETE_TECHNICAL_FAILURE; inference activity recorded from events'
    m={'capture_status':'CAPTURED' if complete else 'CLI_FAILED_OR_INCOMPLETE','experiment_id':'XMODEL-011',
       'stage':1,'attempt':1,'request_id':RID,'request_kind':'technical_launch_recovery',
       'classification':classification,'cli_exit_status':args.exit_code,'model_requested':None,
       'model_reported':next((e.get('server_model') for e in parsed if isinstance(e.get('server_model'),str)),None),
       'inference_event_evidence':activity,'terminal_success_event_observed':terminal,
       'payload_path':str(PAYLOAD),'payload_sha256':sha(PAYLOAD.read_bytes()),
       'brief_sha256':'464ae4378bcb7236f0fb36da52eb65dcb03735197284e3a6899b8686d51ede0b',
       'final_output_path':str(final) if final.is_file() else None,'final_output_sha256':sha(fb) if final.is_file() else None,
       'cli_events_path':str(ev),'cli_events_sha256':sha(eb),'cli_stderr_path':str(err),'cli_stderr_sha256':sha(sb),
       'historical_failures_unchanged':historical_snapshot(),'evaluable_attempts_consumed_before_gate':0,
       'evaluable_attempt_candidate':complete,'semantic_repair_performed':False,'midi_generated':False,'recorded_at_utc':now()}
    mp=CAPTURE/'capture-manifest.json'
    with mp.open('xb') as f: f.write((json.dumps(m,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
    r.update({'status':m['capture_status'],'classification':classification,'cli_exit_status':args.exit_code,'capture_manifest':str(mp)})
    RECORD.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return m

def verify(args)->dict:
    m=json.loads(Path(args.manifest).read_text(encoding='utf-8')); errors=[]
    if m.get('capture_status')!='CAPTURED': errors.append('capture is incomplete')
    if m.get('request_id')!=RID or m.get('stage')!=1 or m.get('attempt')!=1: errors.append('wrong recovery identity/stage/attempt')
    if m.get('payload_sha256')!=EXPECTED_PAYLOAD: errors.append('payload hash mismatch')
    if m.get('cli_exit_status')!=0 or m.get('terminal_success_event_observed') is not True: errors.append('successful exit/terminal event missing')
    for pk,hk in [('final_output_path','final_output_sha256'),('cli_events_path','cli_events_sha256'),('cli_stderr_path','cli_stderr_sha256')]:
        p=Path(m.get(pk) or '')
        if not p.is_file(): errors.append(f'missing {pk}')
        elif sha(p.read_bytes())!=m.get(hk): errors.append(f'hash mismatch {pk}')
    ep=Path(m.get('cli_events_path') or '')
    if ep.is_file():
        terminal=False
        for line in ep.read_bytes().splitlines():
            try:
                ev=json.loads(line)
                if isinstance(ev,dict) and ev.get('type')=='turn.completed': terminal=True
            except Exception: pass
        if not terminal: errors.append('raw JSONL has no turn.completed event')
    fp=Path(m.get('final_output_path') or '')
    if fp.is_file() and fp.stat().st_size==0: errors.append('empty final output')
    if m.get('evaluable_attempts_consumed_before_gate')!=0: errors.append('counter must be zero before gate')
    out={'pass':not errors,'errors':errors,'manifest':str(args.manifest)}
    print(json.dumps(out,ensure_ascii=False,indent=2)); return out

def main()->int:
    p=argparse.ArgumentParser(); s=p.add_subparsers(dest='cmd',required=True)
    s.add_parser('prepare'); s.add_parser('mark-sent')
    x=s.add_parser('record'); x.add_argument('--exit-code',type=int,required=True)
    v=s.add_parser('verify'); v.add_argument('--manifest',required=True)
    a=p.parse_args()
    try:
        z=prepare(a) if a.cmd=='prepare' else mark_sent(a) if a.cmd=='mark-sent' else record(a) if a.cmd=='record' else verify(a)
        if a.cmd!='verify': print(json.dumps(z,ensure_ascii=False,indent=2))
        return 0 if a.cmd!='verify' or z['pass'] else 1
    except Exception as e:
        print(json.dumps({'pass':False,'error':f'{type(e).__name__}: {e}'},ensure_ascii=False,indent=2)); return 2
if __name__=='__main__': raise SystemExit(main())
