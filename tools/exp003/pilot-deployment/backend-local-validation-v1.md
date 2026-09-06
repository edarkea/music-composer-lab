# EXP-003 — validación local del backend v1

## Resultado

**A — MINIMAL BACKEND LOCALLY VERIFIED; READY FOR REMOTE DEPLOYMENT**

Esto autoriza seleccionar/configurar hosting y realizar pruebas remotas técnicas. No autoriza el piloto ni cambia el estatus científico de EXP-003.

## Pruebas

El script `server/local-validation.mjs` ejecutó T1–T8 con datos `TECHNICAL_TEST`:

- T1 normal: PASS.
- T2 incompleto/abort: PASS.
- T3 restart separado: PASS.
- T4 duplicate completion: PASS.
- T5 retry idéntico: PASS; respuesta idempotente sin filas duplicadas.
- T6 retry conflictivo: PASS; rechazo `COMPLETED_CONFLICT`.
- T7 payload malformado: PASS; sesión `INVALID`.
- T8 join científico offline: PASS, 72/72 filas de las seis celdas reconstruidas determinísticamente.

Cobertura de celdas: `A-O1`, `A-O2`, `A-O3`, `B-O1`, `B-O2`, `B-O3` — **6/6 PASS**.

También se verificó un smoke test del cliente jsPsych contra el backend: preload, gating, 12 experimentales, 2 prácticas, diagnóstico y pantalla de éxito posterior al ACK del servidor.

## Integridad y hashes

- Manifest público: `public-deployment-manifest.json` — `881E0161D664AFADE2C4D69BCF2CCBEE731D51C92D80642D27AA9155EEE53507`.
- Mapa privado: `server/private-scientific-map.json` — `E2DE38C1A0C8CCDE525036611921C802CF601FF1B9A5EE37356F9F84C0AA2FF7`.
- `practice-01.wav`: `26C878EC1B2709577FAC80022893CB730FFF77D7AD6E85DA77ABD3544DCD5F89`.
- `practice-02.wav`: `7351B411EB4E64F2C77C05542B2E763F1323A1A9B016E03716F7DC97BF5481B9`.
- `volume-check.wav`: `B39658C83E2B1EC34E231AE8D1F31A6B43B662D5F08A50BAB08463D84DB8`.
- WAV experimentales canónicos/copias: **24/24 PASS**.
- Manifest canónico: `9B23143B7EEE384E5454056F0617E22DD2242C85848CD62920C109ABB6DDA1F0`.

## Requisitos para despliegue remoto

Node.js con filesystem persistente, HTTPS y configuración de variables `EXP003_PORT`/`EXP003_DATA_DIR`. No se seleccionó proveedor de hosting. Los exports técnicos deben permanecer separados de datos de piloto y análisis científicos.
