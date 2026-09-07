# EXP-003 — Stage-1 pilot activation v1

## Estado

**B — IMPLEMENTATION COMPLETED BUT ONE ACTIVATION GATE REMAINS**

La implementación técnica participant-facing fue publicada como una revisión nueva basada en `deployment-freeze-v3.md`. El piloto permanece deshabilitado hasta congelar el mapping nominal P001–P012.

## Base técnica histórica

- `backend-remote-validation-v3.md`: SHA-256 `2ED9C6F9B4CD9D409A41ED1197724A898EF4A6A514188B218595DBD1A2C2BB25`.
- `deployment-freeze-v3.md`: SHA-256 `599F6D793D98B647B8D0363C8F7DF72339E1AD58FC45541DD95406881B06D099`.
- Commit técnico base histórico: `472b59e6c09d15c67fcfe484f92df7776f260f77`.

## Causa corregida

El backend persistía `technical_test: true` para todos los registros. Ahora la clasificación persistida procede del estado de la sesión creada por el servidor:

- sesión `technical_test=true` → registros técnicos;
- sesión `technical_test=false` → registros de piloto.

El payload de finalización no puede cambiar `participant_id`, `cell_id` ni `technical_test` de la sesión. Un payload inconsistente es rechazado.

## Entry architecture

La entrada requiere `entry_token`. El servidor resuelve el token contra `server/private-stage1-allocation.json` y determina `participant_id`, `cell_id`, `stage` y `technical_test`. No existe selector de participante, celda, lista, orden o estado técnico en la interfaz.

La entrada técnica habilitada para smoke es:

`tech-exp003-smoke-7f4c9a` → `TECHTEST-900` → `A-O1` → `technical-test` → `technical_test=true`.

Las entradas piloto permanecen vacías y deshabilitadas hasta el freeze del Owner.

## Participant allocation

La especificación aceptada solo fija la regla de Stage 1: N=12, dos participantes por cada celda y un bloque de seis celdas:

`A-O1`, `B-O1`, `A-O2`, `B-O2`, `A-O3`, `B-O3`.

No se encontró un mapping nominal P001–P012 previamente congelado. Por tanto:

**ALLOCATION MAPPING REQUIRES OWNER FREEZE**

No se inventó una asignación y no se habilitó ningún ID P001–P012.

## Participant-information page

Antes del headphone gate se muestra:

> Es un piloto de escucha musical.
>
> Escucharás ejemplos sonoros breves y darás valoraciones.
>
> Debes usar auriculares.
>
> La participación es voluntaria y puedes detenerte en cualquier momento.
>
> Las respuestas se almacenan bajo un identificador seudónimo del estudio.
>
> No hay respuestas musicales correctas o incorrectas.

No se revelan `LOW/HIGH`, motion, family identity, condition identity ni la dirección de la hipótesis. La necesidad de wording institucional aprobado queda como prerrequisito del Owner.

## Frozen procedure

No cambiaron los assets, wording de la pregunta, escala 1–7, timing, política de replay, listas, órdenes, counterbalancing, 12 trials experimentales, 2 prácticas, diagnóstico ni hipótesis.

## Local validation

- Missing token: PASS; rechazo seguro.
- Unknown token: PASS; rechazo seguro.
- Token técnico válido: PASS; resolución server-side correcta.
- Intento de cambiar `cell_id`: PASS; la sesión conserva `A-O1`.
- Intento de cambiar `technical_test`: PASS; clasificación server-side no cambia y payload inconsistente se rechaza.
- Persistencia de clasificación al completar: PASS.
- Duplicate/restart behavior: PASS; semántica existente conservada.
- Private allocation HTTP access: PASS; no servido.
- Private scientific map HTTP access: PASS; no servido.
- UI blinding/static participant surface: PASS.
- P001–P012 allocation coverage: PENDING OWNER FREEZE.

No se analizaron ratings ni efectos de tratamiento.

## Remote smoke

Resultado: **PASS**.

- Remote deployment: `ef8f5b41-1acb-4d19-a648-1d4704ab1017`.
- HTTPS/UI: cargan correctamente.
- Information page: presente en el flujo participant-facing.
- Headphone gate: permanece después de la información.
- Technical token: resuelve `TECHTEST-900`, `A-O1`, `technical_test=true`.
- Durable save ACK: PASS.
- `/server/private-scientific-map.json`: HTTP 404.
- `/private-stage1-allocation.json`: HTTP 404.
- Client classification override: no altera la sesión.
- P001–P012: no utilizados.

## Deployment identity

- Git commit de implementación: `5ab825ab99a65659d1c4be0eedbfb47c6f16f662`.
- Repositorio: `edarkea/music-composer-lab`.
- Railway domain: `https://music-composer-lab-production.up.railway.app`.
- Railway deployment ID: `ef8f5b41-1acb-4d19-a648-1d4704ab1017`.
- Remote Node.js: `v24.19.0`.
- Railway volume: `music-composer-lab-volume`.
- Volume mount / `DATA_DIR`: `/data`.
- Persistent store: `/data/sessions.json`.

## Files changed

- `tools/exp003/pilot-deployment/experiment.js`
- `tools/exp003/pilot-deployment/server/server.js`
- `tools/exp003/pilot-deployment/server/private-stage1-allocation.json`

No se modificaron `backend-remote-validation-v3.md`, `deployment-freeze-v3.md`, audio, assets, manifests ni metodología.

## Scientific and ethical status

Esta activación produce **NO perceptual evidence**, **NO hypothesis support** y **NO candidate update**. No hubo participantes reales ni datos de piloto.

El requisito institucional/ético permanece **UNRESOLVED**: el Owner debe confirmar si se requiere wording institucional de consentimiento, revisión ética u otra aprobación antes de habilitar P001–P012.

## Authorization

**READY FOR STAGE-1 PILOT: NO** — falta el mapping nominal P001–P012 y la confirmación institucional aplicable.

**PILOT AUTHORIZED: NO**
