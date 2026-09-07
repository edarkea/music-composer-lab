# Deployment freeze v3 — EXP-003

## Decisión

**A — REMOTE DEPLOYMENT FREEZE V3 ACCEPTED**

Este documento incorpora únicamente la identidad Railway verificada directamente por el Project Owner. Los resultados técnicos y hashes congelados de v2 permanecen sin cambios.

## Identidad exacta congelada

| Campo | Valor |
|---|---|
| Railway domain | `https://music-composer-lab-production.up.railway.app` |
| Railway deployment ID | `bd0b6855-6572-44a3-8711-29b030791f19` |
| GitHub repository | `edarkea/music-composer-lab` |
| Git commit deployed | `472b59e6c09d15c67fcfe484f92df7776f260f77` |
| Git branch | `master` |
| Remote Node.js | `v24.19.0` |
| Railway volume | `music-composer-lab-volume` |
| Volume mount | `/data` |
| `DATA_DIR` | `/data` |
| Persistent store | `/data/sessions.json` |
| Replica ID | `7c9ebd50-5d3f-4254-9ec8-1d8377c7a898` |
| Replica region | `iad` |
| Single-instance policy | `YES` — 1 réplica confirmada por el Project Owner |

La identidad remota autoritativa de almacenamiento es `/data/sessions.json`. El valor `server/data/sessions.json` de documentación anterior era solamente una cadena hardcoded del endpoint de health y no forma parte de este freeze.

## Validación congelada

- T1–T8: **PASS**.
- Six operational cells: **6 / 6 PASS**.
- Scientific offline reconstruction: **72 / 72 PASS**.
- Canonical WAV correspondence: **24 / 24 PASS**.
- Private scientific map non-public: **PASS**.
- Public manifest blinding: **PASS**.

## Hashes congelados

- Canonical asset manifest: `9B23143B7EEE384E5454056F0617E22DD2242C85848CD62920C109ABB6DDA1F0`.
- Public deployment manifest: `881E0161D664AFADE2C4D69BCF2CCBEE731D51C92D80642D27AA9155EEE53507`.
- Private scientific map: `E2DE38C1A0C8CCDE525036611921C802CF601FF1B9A5EE37356F9F84C0AA2FF7`.
- Remote snapshot: `D026721386A53F0E3BCE47923AE30CA9FAE1AC76676B305FE2EA2FBCACBF8A9A`.
- Remote technical CSV: `53D52191CCCF06DD799E4C5B5C91484F7440745F5AD2E2B394B4CC3C307740BD`.

## Inmutabilidad y alcance

No se modificaron v2, código, backend state, assets, audio, manifests ni metodología. No se generaron nuevas sesiones técnicas. El mapa científico permanece separado y la identidad científica se reconstruye únicamente offline.

Los datos remotos son exclusivamente `TECHNICAL_TEST`: no contienen participantes reales, participantes de piloto ni evidencia científica. El análisis de efectos no forma parte de este freeze.

## Autorización

**REMOTE DEPLOYMENT FROZEN: YES**

**READY FOR STAGE-1 PILOT AUTHORIZATION: NO** — requiere revisión del Music/Methodology Director.

**PILOT AUTHORIZED: NO**

