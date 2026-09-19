# Frontera Stage 3 → music-engine 4.0.0

## Estado

**A — PROSPECTIVE SONGPLANV2 VALIDATION BOUNDARY READY**

La aceptación de Stage 3 exige ahora, en orden:

1. JSON crudo único sin Markdown ni texto adicional.
2. Rechazo de claves duplicadas antes del parseo, con ruta exacta.
3. Gate local alineado con el contrato SongPlanV2 real.
4. Parseo y validación mediante el `music_engine` 4.0.0 instalado.
5. Resolución de configuración host aprobada, sin sustituir `kit_id` ni `map_id`.

El gate no materializa Song ni MIDI. Si el engine no está disponible, el estado
es `BLOCK` por dependencia/runtime y nunca `PASS`.

## Categorías de resultado

- `invalid_songplan_structure`: codec no puede parsear el plan.
- `musical_semantic_validation_failure`: el plan parsea, pero falla validación
  del engine, por ejemplo escala, referencias o variaciones.
- `host_configuration_failure`: falta o es inválido un mapa host requerido.
- `runtime_dependency_failure`: no se puede importar o invocar el engine.
- `engine_songplan_validation`: plan y host configuration válidos.

## Host configuration

El recurso aprobado para futuros inputs es:

- `integrations/music-engine/host-config.yaml`
- `integrations/music-engine/host-maps/song001_r1_steven_slate_map.yaml`

Solo registra el `DrumExternalMap` Steven Slate aprobado. No registra los
identificadores retrospectivos `hi-hats`, `default_map` o `hi-hats_map` de
XMODEL-008 como recursos aprobados o model-visible. Un futuro track
`percussion` requiere un `PercussionMap` aprobado antes de poder pasar la
frontera.

## Contrato Stage 3

El esquema transmitido usa el esquema real instalado del engine:

- `time_signature` es string, por ejemplo `"4/4"`.
- eventos `effect` usan `bar`, `beat`, `duration` e `id` opcional.
- `drums` usa `drum_voice` y no exige `kit_id`/`map_id` en el track.
- `percussion` exige `kit_id`/`map_id` y eventos semánticos.
- pitches fuera de la escala requieren `chromatic: true`.
- campos desconocidos y claves duplicadas son inválidos.

## Verificación offline

Fixtures sintéticos: **49/49 PASS**.

Incluyen claves duplicadas, `effect.position`, `time_signature` objeto, plan
válido, pitch fuera de escala, host inválido, engine no disponible, invocación
real del validator y ausencia de decisiones musicales del adaptador.

No se ejecutaron modelos, no se generó MIDI, no se modificaron outputs
históricos, no se modificó Composer Knowledge o genre pack y no se creó
XMODEL-009.
