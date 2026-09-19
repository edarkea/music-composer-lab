# Diagnóstico retrospectivo de configuración host

Estos tres archivos son configuraciones de diagnóstico para los `map_id` que
ya aparecen literalmente en los candidatos Qwen preservados de XMODEL-008.

Cada archivo contiene únicamente la asignación aprobada por el Owner:

`(instrument: hi-hat, sounding_articulation: open) -> MIDI 46`

No se añadieron articulaciones, instrumentos ni eventos musicales. Los
identificadores `kit_id` de los candidatos se conservan como etiquetas de kit
host y no requieren archivos separados en el codec V2; el motor construye el
kit a partir de las parejas usadas por el track. Los tres `map_id` requieren un
archivo `PercussionMap` con el mismo `id`, por eso se preparó uno por cada
identificador histórico:

- `hi-hats.yaml` para `kit_id: default`, `map_id: hi-hats`.
- `default_map.yaml` para `kit_id: default_kit`, `map_id: default_map`.
- `hi-hats_map.yaml` para `kit_id: electronic_kit`, `map_id: hi-hats_map`.

La carga mediante `music_engine.songplan.percussion.load_percussion_map` y la
comprobación del par mediante `pitch_for` pasan para los tres archivos.
