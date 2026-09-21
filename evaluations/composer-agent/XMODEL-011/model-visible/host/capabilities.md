# Capacidades host visibles — XMODEL-011

Estos datos describen capacidad técnica disponible; no determinan una decisión musical.

## `drums` y `DrumExternalMap`

Los tracks `drums` expresan eventos mediante `drum_voice`. Para validación host está aprobado el mapa `song001_r1_steven_slate_map`, registrado en `host/song001_r1_steven_slate_map.yaml`. Identificadores de voz disponibles: `kick`, `snare`, `rimshot`, `closed_hat`, `open_hat`, `pedal_hat`, `low_tom`, `mid_tom`, `high_tom`, `crash`, `ride`, `ride_bell`, `cowbell`. El SongPlan no lleva `kit_id` ni `map_id` en este caso.

## `percussion` y `PercussionMap`

Los tracks `percussion` requieren sus propios `kit_id` y `map_id`, con eventos expresados por `instrument` y `sounding_articulation`. No hay ningún PercussionMap aprobado disponible para XMODEL-011. No inventes ni sustituyas identificadores; si la decisión compositiva requiere esa dependencia, el gate host la bloqueará. El mapa de drums no es un PercussionMap.
