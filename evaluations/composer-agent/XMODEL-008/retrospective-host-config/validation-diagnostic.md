# XMODEL-008 — Diagnóstico retrospectivo de PercussionMap

## Resultado

La correspondencia aprobada `(hi-hat, open) -> MIDI 46` se aplicó en tres
archivos host de diagnóstico, conservando literalmente los `map_id` producidos
por Qwen. Los archivos son nuevas configuraciones diagnósticas y no modifican
ningún output histórico.

## Validación de mapas

Los tres archivos pasan el codec real de music-engine 4.0.0 mediante
`load_percussion_map`. Cada uno tiene exactamente `schema_version`, `id` y
`assignments`, y `pitch_for(PercussionInstrument("hi-hat"),
PercussionSoundingArticulation("open"))` devuelve MIDI 46.

| Candidato | `kit_id` preservado | `map_id` preservado | Map file | Identificador host |
|---|---|---|---|---|
| Attempt 1 | `default` | `hi-hats` | `hi-hats.yaml` | resuelto |
| Attempt 2 | `default_kit` | `default_map` | `default_map.yaml` | resuelto |
| Attempt 3 | `electronic_kit` | `hi-hats_map` | `hi-hats_map.yaml` | resuelto |

El codec no exige un registro de kit externo para estos tracks V2: el engine
construye el `PercussionKit` desde las parejas semánticas del track y conserva
el `kit_id` como identificador. Se comprobó la construcción de los tres kits
con los valores originales y la pareja aprobada.

## Validación de SongPlanV2 con el engine real

Se validaron copias temporales con extensión JSON. Los originales no se
editaron.

| Candidato | Resultado | Motivo |
|---|---|---|
| Attempt 1 | FAIL | El parser rechaza `position` en un evento `effect` y el documento contiene claves `duration` duplicadas.
| Attempt 2 | FAIL | `time_signature` es un objeto; el codec 4.0.0 exige una cadena como `"4/4"`.
| Attempt 3 | FAIL | El parser rechaza `position` en un evento `effect` y el documento contiene claves `duration` duplicadas.

La configuración host de percusión queda resuelta para los identificadores
históricos, pero la validación completa de cada SongPlan sigue bloqueada por
errores de parseo preexistentes. No se corrigieron esos errores porque hacerlo
alteraría la representación histórica.

## Alcance

- Correspondencia aprobada aplicada: **sí**.
- `PercussionMap` válido: **sí**, los tres archivos.
- Identificadores históricos resueltos: **sí**, por candidato, a nivel host.
- Validación completa del SongPlan: **FAIL**, por candidato, antes de resolver
  materialización.
- Decisiones musicales del adaptador: **0**.
- Outputs históricos modificados: **NO**.
- Modelos ejecutados: **NO**.
- MIDI generado: **NO**.
