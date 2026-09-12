import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";

const base=process.env.EXP003_REMOTE_BASE || "https://music-composer-lab-production.up.railway.app";
const root=path.dirname(new URL(import.meta.url).pathname.replace(/^\//,""));
const manifest=JSON.parse(readFileSync(path.join(root,"public-deployment-manifest.json"),"utf8"));
const call=async(endpoint,body,method="POST")=>{const r=await fetch(base+endpoint,{method,headers:{"content-type":"application/json"},body:body===undefined?undefined:JSON.stringify(body)});return {status:r.status,body:await r.json()};};
const payload=(cell,id,rating=4)=>({participant_id:id,cell_id:cell,technical_test:true,records:[...manifest.entries.filter(x=>x.cell_id===cell).map(x=>({record_type:"EXPERIMENTAL",serial_position:x.serial_position,opaque_stimulus_id:x.opaque_stimulus_id,rating_1_7:rating,playback_completed:true,technical_error:null})),{record_type:"PRACTICE",serial_position:1,rating_1_7:4,playback_completed:true},{record_type:"PRACTICE",serial_position:2,rating_1_7:4,playback_completed:true},{record_type:"POST_TASK_DIAGNOSTIC",response:"TECHNICAL_TEST"}]});
const start=async(id,cell="A-O1",restart_of)=>{const r=await call("/api/session/start",{participant_id:id,cell_id:cell,technical_test:true,restart_of});assert.equal(r.status,201);return r.body.session;};
const complete=async(s,p=payload(s.cell_id,s.participant_id))=>call(`/api/session/${s.session_id}/complete`,p);
const out={};
assert.equal((await call("/api/health",undefined,"GET")).status,200);
let s=await start("TECHTEST-002");let r=await call(`/api/session/${s.session_id}/abort`,{});assert.equal(r.body.status,"ABORTED");out.T2={status:"PASS",session_id:s.session_id};
s=await start("TECHTEST-003");await call(`/api/session/${s.session_id}/abort`,{});const old=s;const replacement=await start("TECHTEST-003","A-O2",old.session_id);r=await complete(replacement);assert.equal(r.status,201);assert.equal(replacement.restart_of,old.session_id);out.T3={status:"PASS",old_session_id:old.session_id,new_session_id:replacement.session_id};
const d1=await start("TECHTEST-004","A-O3");r=await complete(d1);assert.equal(r.status,201);const d2=await start("TECHTEST-004","A-O3");r=await complete(d2);assert.equal(r.status,409);assert.equal(r.body.error.code,"DUPLICATE");out.T4={status:"PASS",duplicate_session_id:d2.session_id};
const same=await start("TECHTEST-005");const samePayload=payload("A-O1","TECHTEST-005");r=await complete(same,samePayload);assert.equal(r.status,201);const firstHash=r.body.payload_hash;r=await complete(same,samePayload);assert.equal(r.status,200);assert.equal(r.body.idempotent,true);out.T5={status:"PASS",payload_hash:firstHash};
const conflict=await start("TECHTEST-006");r=await complete(conflict);assert.equal(r.status,201);const changed=payload("A-O1","TECHTEST-006",5);r=await complete(conflict,changed);assert.equal(r.status,409);assert.equal(r.body.error.code,"COMPLETED_CONFLICT");out.T6={status:"PASS",http_status:r.status,error_code:r.body.error.code};
const bad=await start("TECHTEST-007");const invalid=payload("A-O1","TECHTEST-007");invalid.records=invalid.records.filter(x=>x.record_type!=="PRACTICE" || x.serial_position!==2);r=await complete(bad,invalid);assert.equal(r.status,422);out.T7={status:"PASS",http_status:r.status,error_code:r.body.error.code};
for(const [i,cell] of ["A-O1","A-O2","A-O3","B-O1","B-O2","B-O3"].entries()){const q=await start(`TECHTEST-${String(100+i).padStart(3,"0")}`,cell);r=await complete(q);assert.equal(r.status,201);}
out.six_cells={status:"PASS",count:6};
for(const endpoint of ["/api/export","/api/export.csv","/api/admin/export.csv"]){const e=await call(endpoint,undefined,"GET");out[endpoint]={status:e.status};}
console.log(JSON.stringify(out));
