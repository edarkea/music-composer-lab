#!/usr/bin/env node
const fs=require("node:fs"),path=require("node:path");
const file=path.resolve(process.env.EXP003_DATA_DIR||path.join(__dirname,"data"),"sessions.json");
const db=JSON.parse(fs.readFileSync(file,"utf8"));
const cols=["session_id","participant_id","cell_id","session_status","technical_test","record_type","record_index","serial_position","opaque_stimulus_id","rating_1_7","playback_completed","technical_error"];
const esc=x=>`"${String(x??"").replaceAll('"','""')}"`;
console.log(cols.join(",")); for(const r of db.records) console.log(cols.map(c=>esc(r[c])).join(","));
