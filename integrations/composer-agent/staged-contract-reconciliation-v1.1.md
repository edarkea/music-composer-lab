# Reconciliaci?n del contrato staged v1.1

## Autoridad SongPlanV2

La autoridad p?blica conservada es:

- `datasets/composer-interface-v1.1/songplan-v2-contract.yaml`
- `integrations/music-engine/integration-contract.md`

El runtime `music-engine` no est? instalado en este entorno (`music_engine` y `music-midi` no est?n disponibles). No se ejecut? el motor.

| Elemento | Representaci?n autoritativa | Requisito |
|---|---|---|
| identificador de secci?n | `$.arrangement.sections[i].id` | requerido, string no vac?o, ?nico |
| direcci?n de armon?a | `$.arrangement.harmony_assignments[i].section_id` o rango | condicional: una de las dos formas |
| asignaci?n de pista | `$.tracks[i].section_assignments[j].section_id` + `motif_id` | requerido por asignaci?n |
| kit de percusi?n | `$.tracks[i].kit_id` | requerido para `percussion` |
| mapa de percusi?n | `$.tracks[i].map_id` | requerido para `percussion` |
| pitched events | `bar`, `beat`, `duration`, `pitches` | requerido; `pitches` lista no vac?a |
| drum events | `bar`, `beat`, `duration`, `drum_voice` | requerido |
| percussion events | `bar`, `beat`, `duration`, `instrument`, `sounding_articulation` | requerido |
| effect events | `position`, `duration` | requerido |

`section_id` es v?lido en referencias a secciones, pero no sustituye `id` dentro del objeto de secci?n.

## Correcciones implementadas

- `gate_stage3` ahora exige `id` para secciones y deja de exigir el campo incorrecto `section_id` en ese nivel.
- Se validan rangos de secci?n, energ?a, modo, tempo, firma m?trica y campos ra?z.
- Se validan IDs de track ?nicos, tipos de pista, envoltorios de motifs y requisitos de evento por tipo.
- Se conservan `kit_id` y `map_id` como requisitos condicionales de `percussion`; `drums` usa `drum_voice` y mapa externo.
- Los wrappers Markdown/prosa siguen siendo FAIL.
- Stage 2 conserva enforcement local derivado del contrato YAML; Ollama `format` sigue desactivado.
- Stage 3 conserva el schema candidato derivado de `songplan_candidate`; la validaci?n local autoritativa permanece obligatoria.

## Auditor?a de XMODEL-008 corregida

El resultado hist?rico no cambia. En diagn?stico offline, los tres Qwen Stage 3 dejan de fallar por `section_id` cuando se aplica el contrato autoritativo; el track `percussion` índice 3 contiene `kit_id` y `map_id`, por lo que los tres outputs pasan el gate corregido. Ministral sigue bloqueado antes de esa validaci?n por wrappers Markdown/comentarios no JSON.

## Alcance y discrepancias restantes

- El schema JSON candidato de Stage 3 es deliberadamente una ayuda de forma: su rama `songplan_candidate` no expresa todos los campos anidados del contrato. El gate local es la autoridad final.
- El contrato Stage 2 sigue siendo YAML descriptivo; no se inventa un JSON Schema ni se activa `format`.
- La validaci?n real del wheel de `music-engine` queda pendiente porque no est? instalado.
- No hay cambio sem?ntico musical.



## Disponibilidad de identificadores de materialización

El contrato exige IDs, pero no define un vocabulario aprobado de `kit_id`/`map_id` ni incluye un mapa host suministrado dentro del contexto visible al modelo. Los ejemplos `drum_test_kit` y `example-map` de la documentación son ilustrativos, no una selección aprobada para una nueva composición. El mapa existente de SONG-001-R1 tampoco se expone bajo la condición NO-EXAMPLE. Por ello, la validez estructural local puede comprobar presencia y forma, pero la elegibilidad real de materialización sigue bloqueada hasta disponer de una dependencia/mapa host autorizado.

## Preflight end-to-end offline

La fixture sintética completa pasa Stage 1 → Stage 2 → Stage 3 con 41/41 regresiones. Los gates rechazan cada etapa inválida y no introducen decisiones del adaptador. La elegibilidad de engine queda `NOT RUN`: el wheel/runtime bloqueado por `integrations/music-engine/runtime-lock.yaml` (`music_engine` 4.0.0, wheel SHA256 `110E987A1E102C1CF3D29FEC1CCC68583459030F40748E10D66CE1F8E4819FE1`) no está instalado.
