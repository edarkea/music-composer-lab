# XMODEL-008 corrected-contract offline diagnostic

Este documento no modifica los gate results hist?ricos ni acepta salidas retroactivamente. Reeval?a ?nicamente los raw outputs preservados con la representaci?n autoritativa reconciliada.

## Qwen Stage 3

Los tres raw outputs son JSON completos. Bajo el gate hist?rico, cada intento report? tres campos `section_id` ausentes y `kit_id`/`map_id` ausentes porque el gate exig?a esos campos en el track `drums` ?ndice 2.

Bajo el contrato autoritativo corregido:

- `arrangement.sections[*].id` es correcto.
- `section_id` solo aparece en asignaciones de secciones.
- `kit_id` y `map_id` son obligatorios para el track `percussion` ?ndice 3; ese track los contiene.
- El track `drums` ?ndice 2 no requiere `kit_id`/`map_id`; usa `drum_voice` y mapa externo.

Los tres intentos pasan el gate local corregido (`PASS`). Esto es un resultado diagn?stico retrospectivo; el gate hist?rico de XMODEL-008 no se reescribe y no se presenta como resultado prospectivo aceptado. La validaci?n del runtime real sigue pendiente.

## Ministral Stage 2

Los tres outputs conservan wrapper Markdown y comentarios no JSON. La reconciliaci?n de campos SongPlanV2 no cambia este resultado; Stage 2 no alcanza validaci?n de material.

## Limitaci?n

La validaci?n real de `music-engine` no est? instalada en el entorno (`music_engine`/`music-midi` no disponibles). La comprobaci?n es la del contrato p?blico y gate local; no se ejecut? music-engine ni MIDI.
