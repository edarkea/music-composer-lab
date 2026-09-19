# XMODEL-008 Compliance Audit

## Resultado principal

**B ? VALID TEST; PARTIAL TRANSFER, NO MATERIALIZABLE SONGPLAN**

La ejecuci?n preservada permite evaluar transferencia estructural hasta los puntos alcanzados. No demuestra calidad musical, conocimiento compositivo ni validez SongPlanV2 completa.

## Integridad y procedencia

- Identidad: `XMODEL-008`; condici?n `NO-EXAMPLE`; Interface `composer-interface-v1.1`.
- Brief id?ntico: s?. SHA256 `464AE4378BCB7236F0FB36DA52EB65DCB03735197284E3A6899B8686D51EDE0B`.
- Modelos: `qwen3:14b` y `ministral-3:14b`.
- Par?metros sim?tricos: temperatura 0, seed 41, top_p 1, top_k 40, repeat_penalty 1, num_ctx 32768; `num_predict` 4096/8192/8192 por etapa.
- Los payloads Stage 1 son id?nticos: SHA256 `7D5B2578BC224DA788D1885E1711D408BE845F1F1633D077F84BFA46F7749721`.
- No se encontraron modificaciones en XMODEL-005, XMODEL-006 o XMODEL-007.
- El `run-manifest.yaml` conserva el estado de preparaci?n (`PREPARED_NOT_EXECUTED`) aunque existen capturas posteriores; es una inconsistencia documental de estado, no evidencia de mezcla de corridas.
- Las capturas actuales est?n bajo `XMODEL-008/`; las capturas anteriores de XMODEL-007 permanecen bajo `XMODEL-007/` con sus propios payloads y hashes. No se relabelaron ni mezclaron.
- No hay archivos persistidos de gate para esta corrida; los resultados reportados se verificaron ejecutando el gate en lectura sobre las salidas preservadas.

## Evidencia por artefacto

| Modelo | Etapa/intento | Artefacto | Evidencia |
|---|---|---|---|
| Qwen | S1/A1 | `qwen3-14b/outputs/stage-1/attempt-1/capture-manifest.json` + `raw-output.txt` | `stop`, 2120 tokens; gate PASS |
| Qwen | S2/A1 | `qwen3-14b/outputs/stage-2/attempt-1/capture-manifest.json` + `raw-output.txt` | `stop`, 1697 tokens; raw JSON; gate PASS |
| Qwen | S3/A1 | `qwen3-14b/outputs/stage-3/attempt-1/` | raw JSON; gate: sections 0?2 sin `section_id`, track 2 sin `kit_id`/`map_id` |
| Qwen | S3/A2 | `qwen3-14b/outputs/stage-3/attempt-2/` | mismo diagn?stico; `stop`, 1005 tokens; retry conserv? schema |
| Qwen | S3/A3 | `qwen3-14b/outputs/stage-3/attempt-3/` | mismo diagn?stico; `stop`, 1359 tokens; retry conserv? schema |
| Ministral | S1/A1?A2 | `ministral-3-14b/outputs/stage-1/attempt-{1,2}/` | JSON truncado; `length`, 4096 tokens |
| Ministral | S1/A3 | `ministral-3-14b/outputs/stage-1/attempt-3/` | `stop`, 3475 tokens; gate PASS |
| Ministral | S2/A1?A3 | `ministral-3-14b/outputs/stage-2/attempt-{1,2,3}/` | wrapper ```json persistente; gate FAIL en los tres |

## Auditor?a Qwen

Stage 1 y Stage 2 pasan el gate local. En Stage 3 los tres intentos son JSON completos y parseables, con `structured_output_schema` transmitido. Los tres contienen `arrangement.sections[i].id`, no `section_id`, y el track de percusi?n ?ndice 2 carece de `kit_id` y `map_id`. No se observ? anidamiento alternativo ni nombres equivalentes.

Los retries A2 y A3 repiten exactamente los cinco diagn?sticos:

- `$.arrangement.sections[0].section_id`
- `$.arrangement.sections[1].section_id`
- `$.arrangement.sections[2].section_id`
- `$.tracks[2].kit_id`
- `$.tracks[2].map_id`

El prompt y el gate exig?an salida cruda y esas rutas. Sin embargo, el contrato autoritativo SongPlanV2 conservado (`songplan-v2-contract.yaml`) define secciones con `id`, no `section_id`. Por tanto, la ausencia de `section_id` demuestra incumplimiento del gate de esta corrida, pero tambi?n revela una discrepancia gate/contrato que limita la atribuci?n al modelo. La ausencia de `kit_id`/`map_id` s? coincide con el contrato para tracks de percusi?n.

El JSON de Qwen es identificable como candidato SongPlanV2, pero no debe repararse ni aceptarse. No produjo un SongPlanV2 localmente aceptado.

## Auditor?a Ministral

Stage 1 pasa en A3 despu?s de dos respuestas truncadas por `done_reason=length`.

Stage 2 falla en A1, A2 y A3 con:

- `markdown wrapper is not valid structured output`
- diagn?stico de serializaci?n raw JSON.

Los tres empiezan con ```` ```json```` y contienen comentarios no v?lidos como `// Placeholder`; la extracci?n offline tampoco produce JSON parseable completo. El wrapper persiste pese a retries. El prompt prohib?a Markdown y prose de forma literal, por lo que este resultado es principalmente incumplimiento de formato del modelo bajo un contrato claro. El gate no pudo evaluar requisitos estructurales o sem?nticos posteriores.

Stage 3 no se ejecut? por la regla de avance condicional.

## Auditor?a sem?ntica

- Cumplimiento estructural: establecido solo para los gates PASS de Stage 1 y Stage 2.
- Disciplina de conocimiento/evidencia: no establecida globalmente.
- Ranking: no evaluable en el resultado final.
- Artistic Priority/Owner attribution: no evaluable globalmente.
- Coherencia compositiva: no demostrada.
- Integridad SongPlanV2: no aceptada para ning?n modelo.
- Calidad musical/perceptual: no evaluada; no se gener? MIDI ni se escuch? material.

## Comparaci?n

| Dimensi?n | Qwen | Ministral |
|---|---|---|
| Etapa m?s lejana | Stage 3 | Stage 2 |
| Etapas aceptadas | S1, S2 | S1 |
| Retries consumidos | S3: 3 | S1: 3; S2: 3 |
| Primer bloqueo final | Campos estructurales Stage 3 | Wrapper Markdown Stage 2 |
| Serializaci?n | raw JSON en S3 | Markdown persistente en S2 |
| Completitud estructural | incompleta seg?n gate; `kit_id/map_id` ausentes | no examinable por parseo rechazado |
| SongPlanV2 v?lido | no | no |
| Intervenci?n del adaptador | 0 | 0 |

La comparaci?n con XMODEL-007 es v?lida solo para parseabilidad/progresi?n y etapa alcanzada. XMODEL-008 incorpor? hardening Stage 2/3; la mejora de serializaci?n no demuestra mejor razonamiento musical.

## Diagn?stico siguiente

- Qwen: requiere resolver la discrepancia no sem?ntica entre `section_id` del gate y `id` del contrato autoritativo, adem?s de conservar la exigencia real de `kit_id/map_id`.
- Ministral: muestra una limitaci?n de cumplimiento de formato bajo un prompt expl?cito; no se justifica modificar Composer Knowledge.
- No se demostr? una brecha musical, epistemol?gica ni de ranking.
- No se justifica m?s ejecuci?n con el mismo contrato sin corregir primero la discrepancia gate/contrato y decidir si se mantiene o elimina el requisito `section_id`.

## Estado final

- SongPlanV2 v?lido Qwen: **NO**
- SongPlanV2 v?lido Ministral: **NO**
- Elegibilidad de materializaci?n Qwen: **NO**
- Elegibilidad de materializaci?n Ministral: **NO**
- Decisiones musicales del adaptador: **0**
- Brecha de conocimiento demostrada: **NO**
- Modelos ejecutados durante esta auditor?a: **NO**
- Artefactos hist?ricos modificados: **NO**
- Composer Knowledge cambiado: **NO**
- Genre pack cambiado: **NO**
- XMODEL-009 preparado: **NO**

Siguiente acci?n t?cnica: reconciliar el nombre de campo de secci?n entre el contrato SongPlanV2 autoritativo y el gate, sin cambiar sem?ntica musical, antes de dise?ar otra corrida prospectiva.
