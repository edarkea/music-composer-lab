# Validación remota del backend — EXP-003

## Resultado

**T8: PASS**

La validación se ejecutó offline sobre el snapshot técnico remoto:

`remote-technical-sessions.json`

El snapshot se trató como solo lectura y no fue modificado.

## Comprobaciones

- T1: PASS. Sesión `s_mtpzyhwc_29b3147e808c8d72` (`TECHTEST-001`, `A-O1`).
- T1 `payload_hash` conocido: `2DB9768E51F1886391B13D25749DCEC5206D0FBE0093F40ACCAE06C367B1EA9B`.
- Export existente `server/export.js`: PASS.
- CSV técnico generado: `remote-technical-export.csv`.
- Filas exportadas: 180.
- Join offline contra `server/private-scientific-map.json`: PASS.
- Sesiones técnicas objetivo: `TECHTEST-100` a `TECHTEST-105`.
- Filas experimentales reconstruidas: 72/72.
- Reconstrucción: 100%.

## Alcance

La reconstrucción relacionó cada `opaque_stimulus_id` con su entrada privada correspondiente y recuperó los campos internos de familia, condición, asset, ruta canónica y hash WAV.

Este resultado valida la integridad técnica del almacenamiento, exportación y join offline. No constituye análisis del efecto científico, no incluye participantes reales y no establece conclusiones musicales.

## Artefactos

- `remote-technical-sessions.json` — snapshot remoto, solo lectura.
- `remote-technical-export.csv` — export técnico producido por el exportador existente.
- `server/private-scientific-map.json` — mapa privado utilizado únicamente offline.

