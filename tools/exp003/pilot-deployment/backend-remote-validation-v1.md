# EXP-003 — validación remota Railway v1

## Outcome

**B — REMOTE BACKEND REQUIRES TECHNICAL REVISION**

La persistencia y la validación remotas pasan, pero el export administrativo real no está disponible por HTTP y no se pudo recuperar el contenido del volumen Railway mediante una ruta admin autenticada. No se declara readiness para Stage 1.

## Identidad y runtime

- Servicio Railway: `https://music-composer-lab-production.up.railway.app`.
- Fuente GitHub localmente identificada: `edarkea/music-composer-lab`, branch `master`.
- Commit de trabajo identificado: `472b59e6c09d15c67fcfe484f92df7776f260f77`.
- Railway deployment ID y timestamp: no expuestos por el endpoint público.
- Node remoto: no expuesto por el endpoint público.
- T1 previamente verificado: `s_mtpzyhwc_29b3147e808c8d72`, `COMPLETE`, payload hash `2DB9768E51F1886391B13D25749DCEC5206D0FBE0093F40ACCAE06C367B1EA9B`.
- Volumen `/data`: preservó T1 antes y después del restart/redeploy, según evidencia remota proporcionada y estado verificado.

## Tests remotos

- T2 abort/incomplete: **PASS** — sesión `s_mtq0utb1_819b51467f62f513` quedó `ABORTED`.
- T3 restart: **PASS** — `s_mtq0utg3_82c17349613d7c8d` preservada; reemplazo `s_mtq0utl2_73c9196877d4c99d` enlazado mediante `restart_of`.
- T4 duplicate: **PASS** — segundo complete de `TECHTEST-004` rechazado con HTTP 409 y `DUPLICATE`.
- T5 identical retry: **PASS** — retry exacto idempotente, con payload hash estable `8A92791933A8E0C90F0D83C7906576E6436E90F240975946E9B07F95DE1257AE`.
- T6 conflicting retry: **PASS** — HTTP 409, `COMPLETED_CONFLICT`.
- T7 malformed payload: **PASS** — HTTP 422, `INVALID_PAYLOAD`.
- Validación server-side de cells: **6/6 PASS** para `A-O1`, `A-O2`, `A-O3`, `B-O1`, `B-O2`, `B-O3`.

Todas las sesiones nuevas usaron IDs `TECHTEST-*` y `technical_test=true`. No se inspeccionaron efectos de tratamiento.

## Export y join

Las rutas públicas probadas `/api/export`, `/api/export.csv` y `/api/admin/export.csv` devolvieron `404`. Esto evita exponer datos, pero significa que el export real desde el store persistente no fue recuperado. El script offline `server/export.js` requiere acceso administrativo al filesystem `/data`; dicho acceso no estaba disponible durante esta validación.

Por tanto, T8 — export remoto y join científico offline — queda **FAIL / NO VERIFICABLE**. El join local sigue validado sobre el manifest y mapa privados, pero no se presenta como join de un CSV remoto.

## Boundary e integridad

- `/server/private-scientific-map.json`: HTTP `404`.
- Manifest público remoto: no contiene `family_id`, `condition`, `LOW`, `HIGH` ni nombres científicos internos.
- WAV opacos remotos: **24/24 SHA PASS** contra las referencias privadas locales.
- Manifest público: `881E0161D664AFADE2C4D69BCF2CCBEE731D51C92D80642D27AA9155EEE53507`.
- Mapa privado: `E2DE38C1A0C8CCDE525036611921C802CF601FF1B9A5EE37356F9F84C0AA2FF7`.
- Manifest canónico: `9B23143B7EEE384E5454056F0617E22DD2242C85848CD62920C109ABB6DDA1F0`.

## Estado final

El backend remoto demuestra health, persistencia, validación, idempotencia, conflictos, restart y frontera pública/privada. Falta un procedimiento administrativo autenticado para exportar el store y realizar el join offline sobre datos remotos reales. No se creó `deployment-freeze-v2` porque no se cumplen todos los criterios remotos.

## Siguiente acción

Proporcionar acceso administrativo seguro al volumen Railway o implementar un mecanismo de exportación autenticado fuera de las rutas públicas, recuperar el CSV técnico y repetir únicamente T8 antes de autorizar Stage 1.
