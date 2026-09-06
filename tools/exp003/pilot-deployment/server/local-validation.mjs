import assert from "node:assert/strict";
import { spawn, execFileSync } from "node:child_process";
import { mkdtempSync, readFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";

const here=path.dirname(new URL(import.meta.url).pathname.replace(/^\//,""));
const dataDir=mkdtempSync(path.join(tmpdir(),"exp003-backend-"));
const port=8781, base=`http://127.0.0.1:${port}`;
const child=spawn(process.execPath,[path.join(here,"server.js")],{env:{...process.env,EXP003_PORT:String(port),EXP003_DATA_DIR:dataDir},stdio:["ignore","pipe","inherit"]});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
for(let i=0;i<50;i++){try{if((await fetch(`${base}/api/health`)).ok)break;}catch{} await sleep(50);}
const call=async(path,body,method="POST")=>{const r=await fetch(base+path,{method,headers:{"content-type":"application/json"},body:body===undefined?undefined:JSON.stringify(body)});return {status:r.status,body:await r.json()};};
const manifest=JSON.parse(readFileSync(path.join(here,"..","public-deployment-manifest.json"),"utf8"));
const privateMap=JSON.parse(readFileSync(path.join(here,"private-scientific-map.json"),"utf8")).entries;
const payload=(cell,id="TECHTEST-001",technical_test=true)=>({participant_id:id,cell_id:cell,technical_test,records:[...manifest.entries.filter(x=>x.cell_id===cell).map(x=>({record_type:"EXPERIMENTAL",serial_position:x.serial_position,opaque_stimulus_id:x.opaque_stimulus_id,rating_1_7:4,playback_completed:true,technical_error:null})),{record_type:"PRACTICE",serial_position:1,rating_1_7:4,playback_completed:true},{record_type:"PRACTICE",serial_position:2,rating_1_7:4,playback_completed:true},{record_type:"POST_TASK_DIAGNOSTIC",response:"TECHNICAL_TEST"}]});
const start=async(id,cell="A-O1",technical_test=true,restart_of)=>{const x=await call("/api/session/start",{participant_id:id,cell_id:cell,technical_test,restart_of});assert.equal(x.status,201);return x.body.session;};
const complete=async(s,p=payload(s.cell_id,s.participant_id,s.technical_test))=>call(`/api/session/${s.session_id}/complete`,p);
const results={};
let s=await start("TECHTEST-001"); let x=await complete(s); assert.equal(x.status,201); results.T1="PASS";
s=await start("TECHTEST-002"); x=await call(`/api/session/${s.session_id}/abort`,{}); assert.equal(x.body.status,"ABORTED"); results.T2="PASS";
s=await start("TECHTEST-003"); await call(`/api/session/${s.session_id}/abort`,{}); const restart=await start("TECHTEST-003","A-O2",true,s.session_id); x=await complete(restart); assert.equal(x.status,201); results.T3="PASS";
const dup1=await start("TESTER-004","A-O3",false); x=await complete(dup1,payload("A-O3","TESTER-004",false)); assert.equal(x.status,201); const dup2=await start("TESTER-004","A-O3",false); x=await complete(dup2,payload("A-O3","TESTER-004",false)); assert.equal(x.status,409); assert.equal(x.body.error.code,"DUPLICATE"); results.T4="PASS";
x=await complete(dup1,payload("A-O3","TESTER-004",false)); assert.equal(x.body.idempotent,true); results.T5="PASS";
const conflict=await start("TESTER-005","A-O1",false); x=await complete(conflict,payload("A-O1","TESTER-005",false)); assert.equal(x.status,201); const changed=payload("A-O1","TESTER-005",false); changed.records.find(r=>r.record_type==="EXPERIMENTAL").rating_1_7=5; x=await complete(conflict,changed); assert.equal(x.status,409); assert.equal(x.body.error.code,"COMPLETED_CONFLICT"); results.T6="PASS";
const malformed=await start("TECHTEST-007"); x=await complete(malformed,{participant_id:"TECHTEST-007",cell_id:"A-O1",technical_test:true,records:[]}); assert.equal(x.status,422); results.T7="PASS";
for(const [i,cell] of ["A-O1","A-O2","A-O3","B-O1","B-O2","B-O3"].entries()){const q=await start(`TECHTEST-${String(100+i).padStart(3,"0")}`,cell);x=await complete(q);assert.equal(x.status,201);}
for(const cell of ["A-O1","A-O2","A-O3","B-O1","B-O2","B-O3"]){const rows=manifest.entries.filter(r=>r.cell_id===cell);assert.equal(rows.length,12);for(const row of rows){const match=privateMap.find(p=>p.opaque_presentation_id===row.opaque_stimulus_id);assert(match);assert.equal(match.record_type,"EXPERIMENTAL");}}
const csv=execFileSync(process.execPath,[path.join(here,"export.js")],{env:{...process.env,EXP003_DATA_DIR:dataDir},encoding:"utf8"});assert.match(csv,/session_id,participant_id,cell_id/);results.T8="PASS";
child.kill(); console.log(JSON.stringify({results,six_cells:"6/6 PASS",server_validation:"PASS",export:"PASS",private_join:"72/72 PASS",data_dir:dataDir}));
