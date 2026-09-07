# Validación remota del backend — EXP-003 — v3

## Resultado

**A — REMOTE DEPLOYMENT FREEZE V3 ACCEPTED**

La validación técnica permanece PASS y la identidad del despliegue remoto fue verificada directamente por el Project Owner mediante `railway ssh`.

## Identidad del despliegue

- Railway HTTPS domain: `https://music-composer-lab-production.up.railway.app`
- Railway deployment ID: `bd0b6855-6572-44a3-8711-29b030791f19`
- Git commit SHA desplegado: `472b59e6c09d15c67fcfe484f92df7776f260f77`
- Git branch: `master`
- Git repository: `edarkea/music-composer-lab`
- Remote Node.js: `v24.19.0`
- Replica ID: `7c9ebd50-5d3f-4254-9ec8-1d8377c7a898`
- Replica region: `iad`
- Single instance: `YES` — 1 réplica confirmada por el Project Owner en la configuración del servicio Railway.

## Persistencia

- Railway volume: `music-composer-lab-volume`
- Volume mount path: `/data`
- `DATA_DIR`: `/data`
- Persistent store observado: `/data/sessions.json`
- Store exists: `YES`

`server/data/sessions.json` no se considera la identidad remota autoritativa; era el valor de una cadena de diagnóstico hardcoded anterior. La ruta autoritativa observada es `/data/sessions.json`.

## Resultados técnicos

- T1 normal remote completion: **PASS**.
- Persistence across restart: **PASS**.
- T2 abort/incomplete: **PASS**.
- T3 restart: **PASS**.
- T4 duplicate: **PASS**.
- T5 identical retry: **PASS**.
- T6 conflicting retry: **PASS**.
- T7 malformed payload: **PASS**.
- T8 remote export + offline scientific join: **PASS**.
- Six operational cells: **6 / 6 PASS**.
- Scientific offline reconstruction: **72 / 72 PASS**.
- Canonical WAV correspondence: **24 / 24 PASS**.
- Private scientific map non-public: **PASS**.
- Public manifest blinding: **PASS**.

## Integridad congelada

- Canonical asset manifest: `9B23143B7EEE384E5454056F0617E22DD2242C85848CD62920C109ABB6DDA1F0`.
- Public deployment manifest: `881E0161D664AFADE2C4D69BCF2CCBEE731D51C92D80642D27AA9155EEE53507`.
- Private scientific map: `E2DE38C1A0C8CCDE525036611921C802CF601FF1B9A5EE37356F9F84C0AA2FF7`.
- Remote snapshot: `D026721386A53F0E3BCE47923AE30CA9FAE1AC76676B305FE2EA2FBCACBF8A9A`.
- Remote technical CSV: `53D52191CCCF06DD799E4C5B5C91484F7440745F5AD2E2B394B4CC3C307740BD`.

## Alcance y límites

El snapshot remoto se obtuvo administrativamente desde el volumen Railway y no fue modificado. El CSV fue derivado mediante el `server/export.js` existente. No se introdujo un endpoint HTTP público de exportación.

Todos los registros usados en la validación son `TECHNICAL_TEST`. No hay participantes reales, participantes de piloto ni evidencia científica. No se analizaron efectos de tratamiento.

No se realizaron cambios de backend, código, audio, assets, manifests ni metodología.

## Decisión

La identidad remota está suficientemente documentada para aceptar el freeze técnico v3. El piloto continúa sin autorización y queda pendiente de revisión del Music/Methodology Director.

