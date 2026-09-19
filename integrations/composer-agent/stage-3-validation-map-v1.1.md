# SongPlanV2 validation map

Fuente autoritativa: `datasets/composer-interface-v1.1/songplan-v2-contract.yaml` y `integrations/music-engine/integration-contract.md`.

| Contrato | Gate local | Representaci?n |
|---|---|---|
| ra?z exacta y `schema_version: "2.0"` | `gate_stage3` root checks | `$` |
| section identifier | requiere `id`, string no vac?o, ?nico | `$.arrangement.sections[i].id` |
| section range | `start_bar`, `bar_count` enteros positivos | `$.arrangement.sections[i].start_bar/bar_count` |
| section energy | n?mero | `$.arrangement.sections[i].energy` |
| harmony assignment | `harmony` + `section_id` o rango expl?cito | `$.arrangement.harmony_assignments[i]` |
| track common fields | `id`, `type`, `role`, `motifs`, `section_assignments` | `$.tracks[i]` |
| track type | `pitched`, `drums`, `percussion`, `effect` | `$.tracks[i].type` |
| percussion resources | `kit_id` y `map_id` requeridos para `percussion`; `drums` usa `drum_voice` y mapa externo | `$.tracks[i].kit_id/map_id` |
| time signature | cadena no vacía `numerator/denominator`; denominador potencia de dos | `$.time_signature` |
| effect events | `bar`, `beat`, `duration`, `id` opcional; `position` no permitido | `$.tracks[i].motifs[j].events[k]` |
| scale validation | pitch dentro de la escala declarada salvo `chromatic: true` | engine validator |
| duplicate keys | rechazadas antes de parsear | raw JSON object path |
| motif envelope | `id` y `events` | `$.tracks[i].motifs[j]` |

`section_id` no es un campo de secci?n; es v?lido en asignaciones.


