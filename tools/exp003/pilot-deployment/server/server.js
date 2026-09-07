#!/usr/bin/env node
const http = require("node:http");
const fs = require("node:fs");
const path = require("node:path");
const crypto = require("node:crypto");
const { URL } = require("node:url");

const PORT = Number(process.env.EXP003_PORT || 8770);
const DATA_DIR = path.resolve(process.env.DATA_DIR || path.join(__dirname, "data"));
const STORE_PATH = path.join(DATA_DIR, "sessions.json");
const CELL_IDS = new Set(["A-O1", "A-O2", "A-O3", "B-O1", "B-O2", "B-O3"]);
const PUBLIC_MANIFEST_PATH = path.join(__dirname, "..", "public-deployment-manifest.json");
const PRIVATE_ALLOCATION_PATH = path.join(__dirname, "private-stage1-allocation.json");

function readJson(file, fallback) { try { return JSON.parse(fs.readFileSync(file, "utf8")); } catch { return fallback; } }
function store() { return readJson(STORE_PATH, {sessions: [], records: []}); }
function canonical(value) {
  if (Array.isArray(value)) return `[${value.map(canonical).join(",")}]`;
  if (value && typeof value === "object") return `{${Object.keys(value).sort().map(k => `${JSON.stringify(k)}:${canonical(value[k])}`).join(",")}}`;
  return JSON.stringify(value);
}
function hash(value) { return crypto.createHash("sha256").update(canonical(value)).digest("hex").toUpperCase(); }
function allocation() { return readJson(PRIVATE_ALLOCATION_PATH, {pilot_status:"owner_freeze_required",pilot_entries:[],technical_entries:[]}); }
function resolveEntry(token) {
  if (typeof token !== "string" || token.length < 8 || token.length > 128) return null;
  const a = allocation();
  return [...(a.pilot_entries || []), ...(a.technical_entries || [])].find(x => x.opaque_entry_token === token && x.enabled === true) || null;
}
function persist(db) {
  fs.mkdirSync(DATA_DIR, {recursive: true});
  const tmp = `${STORE_PATH}.tmp-${process.pid}`;
  fs.writeFileSync(tmp, JSON.stringify(db, null, 2) + "\n", "utf8");
  fs.renameSync(tmp, STORE_PATH);
}
function send(res, status, body) { res.writeHead(status, {"content-type": "application/json; charset=utf-8", "cache-control": "no-store", "access-control-allow-origin": "*", "access-control-allow-headers": "content-type", "access-control-allow-methods": "GET,POST,OPTIONS"}); res.end(JSON.stringify(body)); }
function fail(res, status, code, message) { send(res, status, {ok: false, error: {code, message}}); }
function body(req) { return new Promise((resolve, reject) => { let raw=""; req.on("data", c => { raw += c; if (raw.length > 2_000_000) reject(new Error("too_large")); }); req.on("end", () => { try { resolve(raw ? JSON.parse(raw) : {}); } catch { reject(new Error("invalid_json")); } }); req.on("error", reject); }); }
function validId(x) { return typeof x === "string" && /^[A-Za-z0-9_-]{3,64}$/.test(x); }
function sessionId() { return `s_${Date.now().toString(36)}_${crypto.randomBytes(8).toString("hex")}`; }
function expectedForCell(cell) {
  const manifest = readJson(PUBLIC_MANIFEST_PATH, {entries: []});
  return manifest.entries.filter(x => x.cell_id === cell).sort((a,b) => a.serial_position-b.serial_position);
}
function validateCompletion(payload, session) {
  if (!payload || payload.participant_id !== session.participant_id || payload.cell_id !== session.cell_id) return "invalid_payload";
  if (payload.technical_test !== session.technical_test || !Array.isArray(payload.records)) return "invalid_payload";
  const experimental = payload.records.filter(x => x.record_type === "EXPERIMENTAL");
  const practice = payload.records.filter(x => x.record_type === "PRACTICE");
  const diagnostic = payload.records.filter(x => x.record_type === "POST_TASK_DIAGNOSTIC");
  const expected = expectedForCell(session.cell_id);
  if (experimental.length !== 12 || practice.length !== 2 || diagnostic.length !== 1 || expected.length !== 12) return "invalid_payload";
  const positions = experimental.map(x => x.serial_position).sort((a,b)=>a-b);
  if (positions.some((x,i) => x !== i+1)) return "invalid_payload";
  for (const row of experimental) {
    const e = expected[row.serial_position-1];
    if (row.opaque_stimulus_id !== e.opaque_stimulus_id || !Number.isInteger(row.rating_1_7) || row.rating_1_7 < 1 || row.rating_1_7 > 7 || row.playback_completed !== true) return "invalid_payload";
  }
  if (new Set(experimental.map(x=>x.opaque_stimulus_id)).size !== 12) return "invalid_payload";
  return null;
}
function serveParticipantFile(req, res, pathname) {
  const relative = pathname === "/" ? "index.html" : pathname.slice(1);
  const allowed = relative === "index.html" || relative === "pilot.css" || relative === "experiment.js" || relative === "public-deployment-manifest.json" || relative.startsWith("media/");
  if (!allowed || relative.includes("..")) return false;
  const file = path.resolve(__dirname, "..", relative);
  if (!file.startsWith(path.resolve(__dirname, "..") + path.sep) || !fs.existsSync(file) || !fs.statSync(file).isFile()) return false;
  const type = file.endsWith(".html") ? "text/html; charset=utf-8" : file.endsWith(".css") ? "text/css; charset=utf-8" : file.endsWith(".js") ? "text/javascript; charset=utf-8" : file.endsWith(".json") ? "application/json; charset=utf-8" : "audio/wav";
  res.writeHead(200, {"content-type":type,"cache-control":"no-store"}); res.end(fs.readFileSync(file)); return true;
}
async function handle(req, res) {
  const u = new URL(req.url, `http://${req.headers.host}`);
  if (req.method === "OPTIONS") { res.writeHead(204, {"access-control-allow-origin":"*", "access-control-allow-headers":"content-type", "access-control-allow-methods":"GET,POST,OPTIONS"}); return res.end(); }
  if (req.method === "GET" && !u.pathname.startsWith("/api/")) return serveParticipantFile(req, res, u.pathname) || fail(res, 404, "NOT_FOUND", "Recurso no encontrado.");
  if (req.method === "GET" && u.pathname === "/api/health") return send(res, 200, {ok:true, service:"exp003-pilot-backend", persistence:"json-file", storage_path:"server/data/sessions.json"});
  if (req.method === "POST" && u.pathname === "/api/session/start") {
    let p; try { p=await body(req); } catch { return fail(res,400,"INVALID_PAYLOAD","JSON inválido."); }
    if (!validId(p.participant_id) || !CELL_IDS.has(p.cell_id) || typeof p.technical_test !== "boolean") return fail(res,400,"INVALID_SESSION_START","participant_id, cell_id o technical_test inválido.");
    if (p.entry_token === undefined && p.technical_test !== true) return fail(res,403,"INVALID_ENTRY","No se pudo validar la entrada.");
    if (p.technical_test && !/^TECHTEST-[0-9]{3,}$/.test(p.participant_id)) return fail(res,400,"INVALID_SESSION_START","Los technical tests requieren un ID TECHTEST-.");
    const entry = resolveEntry(p.entry_token);
    if (p.entry_token !== undefined) {
      if (!entry || !validId(entry.participant_id) || !CELL_IDS.has(entry.cell_id) || typeof entry.technical_test !== "boolean" || typeof entry.stage !== "string") return fail(res,403,"INVALID_ENTRY","No se pudo validar la entrada.");
      const db=store(); const id=sessionId(); const s={session_id:id,participant_id:entry.participant_id,cell_id:entry.cell_id,status:"STARTED",technical_test:entry.technical_test,stage:entry.stage,started_at:new Date().toISOString(),completed_at:null,restart_of:validId(p.restart_of)?p.restart_of:null,payload_hash:null}; db.sessions.push(s); persist(db); return send(res,201,{ok:true,session:s});
    }
    return fail(res,403,"INVALID_ENTRY","No se pudo validar la entrada.");
  }
  const m=u.pathname.match(/^\/api\/session\/([^/]+)\/(complete|abort)$/); if (!m) return fail(res,404,"NOT_FOUND","Ruta no encontrada.");
  const db=store(); const s=db.sessions.find(x=>x.session_id===m[1]); if (!s) return fail(res,404,"SESSION_NOT_FOUND","Sesión no encontrada.");
  if (m[2] === "abort") { if (s.status === "STARTED") { s.status="ABORTED"; s.completed_at=new Date().toISOString(); persist(db); } return send(res,200,{ok:true,status:s.status,session_id:s.session_id}); }
  let p; try { p=await body(req); } catch { return fail(res,400,"INVALID_PAYLOAD","JSON inválido."); }
  const pHash=hash(p);
  if (s.status === "COMPLETE") { if (s.payload_hash===pHash) return send(res,200,{ok:true,idempotent:true,status:"COMPLETE",session_id:s.session_id}); return fail(res,409,"COMPLETED_CONFLICT","La sesión ya está completada con otro payload."); }
  if (s.status !== "STARTED") return fail(res,409,"SESSION_NOT_ACTIVE","La sesión no está activa.");
  const error=validateCompletion(p,s); if (error) { s.status="INVALID"; s.completed_at=new Date().toISOString(); persist(db); return fail(res,422,"INVALID_PAYLOAD","El payload no cumple el contrato de EXP-003."); }
  const duplicate=db.sessions.some(x=>x.participant_id===s.participant_id && x.status==="COMPLETE" && !s.restart_of && x.session_id!==s.session_id);
  s.payload_hash=pHash; s.completed_at=new Date().toISOString(); s.status=duplicate?"DUPLICATE":"COMPLETE"; db.records.push(...p.records.map((r,i)=>({...r,session_id:s.session_id,participant_id:s.participant_id,cell_id:s.cell_id,technical_test:s.technical_test,stage:s.stage,session_status:s.status,record_index:i+1}))); persist(db);
  return send(res, duplicate?409:201,{ok:!duplicate,status:s.status,session_id:s.session_id,payload_hash:pHash,error:duplicate?{code:"DUPLICATE",message:"Sesión completa duplicada."}:null});
}
const server=http.createServer((req,res)=>handle(req,res).catch(e=>fail(res,500,"STORAGE_FAILURE",e.message)));
server.listen(PORT,"0.0.0.0",()=>console.log(`EXP-003 backend listening on http://0.0.0.0:${PORT}`));
