# XMODEL-008 — Validación del music-engine 4.0.0

## Resultado

**B — ENGINE VALIDATION AVAILABLE; HOST CONFIGURATION AND REPRESENTATION ALIGNMENT PENDING**

La integración real del motor está instalada y puede ejecutar validación
estructural sin generar MIDI. La validación no permite declarar transferibilidad
de los candidatos Qwen: los tres artefactos preservados fallan antes de la
validación semántica del motor y no hay mapas host aprobados para resolver los
identificadores de percusión declarados.

## Runtime verificado

- Wheel: `.vendor/music_engine-4.0.0-py3-none-any.whl`
- Versión instalada: `4.0.0`
- SHA256 verificado: `110E987A1E102C1CF3D29FEC1CCC68583459030F40748E10D66CE1F8E4819FE1`
- Lockfile: `integrations/music-engine/runtime-lock.yaml`
- CLI disponible: `music-midi songplan validate --json INPUT`
- API identificada: `music_engine.songplan.v2.codec.load_song_plan_v2` y
  `music_engine.songplan.validation.validate_song_plan`
- Fixture de integración: validación `SUCCESS`, `valid: true`, sin incidencias.

No se ejecutaron modelos y no se generó MIDI durante esta auditoría.

## Candidatos Qwen preservados

Se validaron copias temporales de los tres `raw-output.txt`; los artefactos
históricos no fueron modificados.

| Candidato | Gate local corregido | music-engine 4.0.0 | Diagnóstico |
|---|---:|---:|---|
| Stage 3 / attempt 1 | PASS | `PARSE_FAILURE` | El evento `effect` contiene el campo no reconocido `position`. El codec real usa `bar`, `beat` y `duration` para eventos.
| Stage 3 / attempt 2 | PASS | `PARSE_FAILURE` | `time_signature` se transmite como objeto; el codec instalado exige una cadena, por ejemplo `"4/4"`.
| Stage 3 / attempt 3 | PASS | `PARSE_FAILURE` | `time_signature` se transmite como objeto; el codec instalado exige una cadena, por ejemplo `"4/4"`.

Al producirse el fallo de parseo no se alcanza la resolución de mapas ni la
validación semántica del plan. Por tanto no se debe interpretar el resultado
como evidencia musical ni como fallo de conocimiento.

## Discrepancias local/engine

1. El gate local corregido acepta la forma de `time_signature` documentada como
   objeto o forma de codec; el parser 4.0.0 instalado exige la forma string.
2. El contrato de integración describe eventos `effect` con `position`; el
   codec 4.0.0 instalado rechaza ese campo y acepta la representación temporal
   común (`bar`, `beat`, `duration`).
3. El gate local comprueba presencia estructural de `kit_id`/`map_id` en tracks
   `percussion`, pero no puede resolver mapas host. El motor requiere archivos de
   mapa externos y sus identificadores no deben inventarse.

Estas son discrepancias técnicas de representación/host. No requieren cambios
en Composer Knowledge, genre pack ni en la semántica musical de Interface v1.1.

## Mapas y configuración host

El mecanismo de resolución está disponible mediante archivos `<map-id>.yaml` o
`.json` y `--drum-map-dir`. El único mapa encontrado en el repositorio es
`compositions/SONG-001-R1/maps/song001_r1_steven_slate_map.yaml`; es específico
de esa composición y no se reutiliza como configuración de XMODEL-008 sin
decisión explícita del Owner. Los IDs `default`, `default_kit`, `default_map`,
`electronic_kit` y `hi-hats_map` de los candidatos no tienen archivos host
aprobados en el contexto actual.

## Confirmación del mapa Steven Slate

El Owner confirmó que permanece vigente el mapa aprobado de SONG-001-R1. Se
cargó con `load_drum_external_map` del engine 4.0.0 y fue aceptado por el
codec:

- `id`: `song001_r1_steven_slate_map`
- formato: `schema_version: "1.0"`, `id`, `mappings`
- voces cubiertas: `kick`, `snare`, `rimshot`, `closed_hat`, `open_hat`,
  `pedal_hat`, `low_tom`, `mid_tom`, `high_tom`, `crash`, `ride`, `ride_bell`,
  `cowbell`
- valores MIDI: exactamente los aprobados por el Owner.

Este mapa es suficiente como referencia host para un track de tipo `drums`:
los eventos usan `drum_voice` y el CLI lo registra mediante
`--drum-map-dir` y `--drum-map-id song001_r1_steven_slate_map`. En SongPlan V2
el campo opcional `drum_kit_profile_id` puede asociarse al perfil generado por
ese mapa; no se debe inventar otro identificador.

No es un mapa válido para tracks de tipo `percussion`. Esos tracks requieren
`kit_id` y `map_id` propios y una `PercussionMap` con asignaciones exactas de
`instrument` + `sounding_articulation` a pitch. El mapa Steven Slate no contiene
esas claves semánticas. Por ello no resuelve los tracks `percussion` de los
candidatos Qwen (por ejemplo `hi-hats` con `map_id` `hi-hats`, `default_map` o
`hi-hats_map`). No se encontraron archivos aprobados con esos IDs.

Conclusión de configuración: el Owner-approved map es suficiente para la parte
`drums`, pero se requiere información técnica adicional y autorización para
cualquier parte `percussion`: un `kit_id`, un `map_id` existente y su archivo
`PercussionMap` completo, o una decisión explícita de no materializar ese
track. No se asignaron IDs ni se creó ningún mapa durante esta revisión.

## Decisiones pendientes del Owner

- Autorizar/proporcionar los mapas host y sus IDs para una futura validación de
  percusión; no crear IDs ni mapas por inferencia.
- Decidir si la interfaz técnica y el gate deben alinearse con el codec 4.0.0
  (`time_signature` string y eventos `effect` con `bar`/`beat`). Esto no cambia
  decisiones musicales, pero sí la representación ejecutable.

## Preservación y alcance

- XMODEL-008 histórico: preservado.
- Composer Knowledge: sin cambios.
- Genre pack: sin cambios.
- Interface musical: sin cambios.
- Modelos ejecutados: no.
- MIDI generado: no.
- XMODEL-009 creado: no.
