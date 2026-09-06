# EXP-003 — Auditoría de preparación de despliegue del piloto v1

## Outcome

**A — DEPLOYMENT PLAN READY FOR IMPLEMENTATION**

La preparación está suficientemente especificada para una futura
implementación, pero la plataforma aún no está seleccionada y el piloto no está
autorizado.

## Base autoritativa

- Asset manifest: `experiments/EXP-003/EXP-003-asset-manifest-v1.yaml`
- SHA-256: `9B23143B7EEE384E5454056F0617E22DD2242C85848CD62920C109ABB6DDA1F0`
- Pool: `CANONICAL_ASSET_POOL_FROZEN`
- Participant assets, practice audio y volume-check audio: **NO CREADOS**.

Las decisiones de assignment, order, timing de interfaz, escala, wording,
auriculares, práctica y diagnóstico proceden de la especificación de
implementación aceptada.

## Platform requirements

La futura plataforma debe demostrar antes de pilot authorization:

- reproducir los WAV originales sin transcodificación, normalización o gain
  automático;
- impedir respuesta hasta terminar el playback;
- ejecutar exactamente una reproducción automática por trial;
- mostrar escala ordinal 1–7 con etiquetas solo en 1/4/7;
- asignar las seis celdas predefinidas sin usar respuestas;
- ocultar condición, familia, motion y filenames técnicos;
- soportar 2 prácticas, 12 trials y una pregunta libre post-tarea;
- exportar el schema estructurado y registrar errores técnicos.

## Platform candidates

| ruta | clasificación | evaluación |
|---|---|---|
| `jsPsych + Pavlovia` | `SUITABLE_WITH_LIMITATIONS` | El plugin de audio permite precarga y puede habilitar botones después del final del audio; Pavlovia proporciona ejecución y exportación de datos. Requiere implementación propia para una sola reproducción, opaque IDs, gating exacto, ocultación de metadata y logging. |
| Qualtrics con JavaScript personalizado | `SUITABLE_WITH_LIMITATIONS` | Permite media embebida, pero el autoplay, la reproducción única y el gating dependen de permisos, JavaScript y políticas del navegador; aumenta el riesgo de controles o nombres expuestos. |
| Aplicación web propia + hosting controlado | `SUITABLE_WITH_LIMITATIONS` | Ofrece el máximo control sobre estados, IDs y logging, pero exige escribir software, elegir hosting y verificar almacenamiento/playback; no existe todavía en el repositorio. |

La documentación oficial de jsPsych describe precarga y respuesta posterior al
audio en su plugin de audio [jsPsych audio-button-response](https://www.jspsych.org/6.3/plugins/jspsych-audio-button-response/), y la documentación de Pavlovia describe el flujo de proyecto, pilot y exportación [Running jsPsych experiments from Pavlovia](https://pavlovia.org/docs/experiments/create-jsPsych). La documentación de Qualtrics confirma que el media embebido depende de permisos HTML/JavaScript y configuración del servicio [Insert Media](https://www.qualtrics.com/support/survey-platform/survey-module/editing-questions/rich-content-editor/insert-media/).

## Recommendation

Ruta recomendada: **`jsPsych + Pavlovia`**, con estado **OPEN**, no
`SELECTED`. Es la opción más alineada con la tarea de audio secuencial, gating
de respuesta y exportación estructurada sin crear una plataforma propia. La
recomendación no constituye autorización de compra, cuenta, proyecto o
despliegue.

## Audio-delivery audit

La plataforma no debe convertir ni reexportar los WAV. Los assets deben servirse
como archivos originales y validarse por SHA-256 antes del despliegue. El
navegador puede decodificar el WAV y el dispositivo puede hacer resampling en
la salida física; por eso el hash garantiza la identidad del archivo servido,
no una identidad acústica idéntica entre hardware.

La implementación debe usar preload, no mostrar controles de descarga, bloquear
pause/seek/replay y registrar `playback_started` y `playback_completed`. La
política de autoplay requiere una interacción previa del participante en la
pantalla READY; el WAV no debe comenzar antes de esa interacción. Cualquier
transcodificación, normalización, cambio de gain, control visible o replay
inesperado es un bloqueo de despliegue, no un motivo para modificar el asset.

## Opaque IDs and blinding

El participante verá únicamente el estado de trial y, si procede, un token de
sesión no informativo. Formato interno propuesto:

`PILOT-<session_token>-TRIAL-<serial_position:02d>`

El token no contiene familia, condición, motion ni nombre técnico. El mapping
privado debe conservar:

```text
opaque_presentation_id
↔ internal_asset_id
↔ canonical_wav_path
↔ canonical_wav_sha256
↔ family_id
↔ condition
```

La tabla privada no se exporta a la pantalla ni se incorpora a mensajes de
error. Los URLs, `title`, `aria-label`, headers, download names y errores deben
usar el token opaco o un mensaje genérico.

Blinding audit: **PASS WITH CAUTION**. La arquitectura es suficiente, pero
requiere dry run para verificar que HTML/media metadata, URLs y errores reales
no filtren la identidad técnica.

## Allocation schedule

Stage 1 usa 12 slots, con dos participantes por cada celda:

| slots | cell |
|---:|---|
| 1–2 | A×O1 |
| 3–4 | B×O1 |
| 5–6 | A×O2 |
| 7–8 | B×O2 |
| 9–10 | A×O3 |
| 11–12 | B×O3 |

No se asigna según respuestas, ratings, playback o efecto observado.

Si se extiende a N=24, los slots 13–24 repiten exactamente el mismo patrón:

| slots | cell |
|---:|---|
| 13–14 | A×O1 |
| 15–16 | B×O1 |
| 17–18 | A×O2 |
| 19–20 | B×O2 |
| 21–22 | A×O3 |
| 23–24 | B×O3 |

La especificación de cada cell está congelada en
`EXP-003-pilot-implementation-spec-v1.md`.

## Participant IDs

El analytical `participant_id` será un token pseudónimo generado al crear la
sesión, por ejemplo `PILOT-7K4M2Q`. No contendrá nombre ni email. Si existe
algún vínculo de contacto o compensación, se conservará fuera del dataset
analítico con control de acceso separado. No se crearán IDs participant-facing
de stimulus en esta fase.

## Volume-check asset

Se requiere un único asset neutral separado de las 24 familias: un sonido
estable de nivel cómodo, sin transición R1→R2 ni contraste de movimiento, sin
extremos de registro y sin feedback correcto/incorrecto. Debe tener ID propio,
spec propia, SHA-256 y validación técnica.

Usar el mismo timbre sintético general puede facilitar familiarización de nivel,
siempre que el asset no imite una familia experimental ni enseñe que cierto
movimiento corresponde a cierta respuesta. No se genera ahora.

Estado: **OPEN DEPLOYMENT DEPENDENCY**.

## Practice assets

Se requieren exactamente dos assets de práctica, ambos fuera de F01–F12. Deben
usar la misma interfaz, escala 1–7 y playback único; no deben tener feedback,
extremos de distancia o un patrón que enseñe `LOW = pequeña distancia`. Deben
recibir IDs y SHA-256 propios y quedar excluidos del manifest canónico y del
análisis experimental.

Estado: **OPEN DEPLOYMENT DEPENDENCY**. No se componen ni renderizan ahora.

## Practice/volume freeze policy

Cuando se creen, cada asset de práctica o volumen tendrá una especificación
separada, validación objetiva, SHA-256 y provenance. Nunca se añadirá al
manifest de los 24 assets canónicos ni se usará como participante stimulus
experimental.

## Export schema

Cada fila experimental requiere:

```text
record_type: EXPERIMENTAL
participant_id
pilot_stage
assignment_list
order_sequence
serial_position
opaque_presentation_id
internal_family_id
condition
canonical_asset_reference
canonical_asset_sha256
rating
playback_started
playback_completed
technical_error
response_recorded
```

Las filas de práctica usan `record_type: PRACTICE`; el texto libre usa
`record_type: CONSTRUCT_DIAGNOSTIC`. Internal family/condition quedan en el
dataset privado de provenance y nunca en la superficie participant-facing.

## Session integrity

Una sesión completa requiere 12 filas experimentales, 12 familias únicas, 6
LOW, 6 HIGH, una cell válida, order válido, ratings 1–7, un playback completado
y una respuesta por trial. No se reparan silenciosamente registros inválidos.

## Headphone gate

Auriculares: **REQUIRED** por autoconfirmación del participante. Si declara que
no puede usarlos, la sesión no continúa. No se inventará detección automática.
Se registrarán tipo de auricular, dispositivo, navegador y problemas de audio.

## Failure and recovery policy

- Audio-load failure: registrar error, detener la sesión y no sustituir el WAV.
- Browser refresh: marcar sesión como interrumpida; no reanudar
  automáticamente ni duplicar trials.
- Network interruption: conservar el error y estado local disponible; si la
  integridad de exportación no puede confirmarse, marcar sesión incompleta.
- Duplicate submission: rechazar idempotentemente la misma combinación
  `session_id + serial_position`; no crear una segunda respuesta válida.
- Partial session: conservar como `INCOMPLETE`, sin completar filas faltantes ni
  incluirla como sesión completa.

Todo fallo debe ser auditable y no debe cambiar condición, asset, gain o
timing.

## Future dry run (not executed)

Antes de pilot authorization se ejecutará un dry run sin participantes reales
que compruebe, para las seis cells y al menos un trial de cada tipo:

1. asignación correcta y 6/6 LOW/HIGH;
2. IDs opacos y mapping privado recuperable;
3. ausencia de leaks en filenames, URLs, metadata, headers y errores;
4. una sola reproducción y respuesta bloqueada hasta playback complete;
5. delays de 1000 ms;
6. logging de playback, errores y respuesta;
7. export schema y validación de sesión;
8. gate de auriculares;
9. dos prácticas y diagnóstico post-tarea;
10. hash del WAV servido igual al canonical SHA y ausencia de transcodificación
    o gain automático.

El dry run no usará datos reales ni producirá participant assets permanentes.

## Final status

- Canonical assets unchanged: **YES**.
- Implementation spec unchanged: **YES**.
- New code: **NO**.
- Participant assets: **NO**.
- Practice/volume audio: **NO**.
- Pilot executed: **NO**.
- Platform status: **OPEN**.
- READY FOR DEPLOYMENT IMPLEMENTATION: **YES**, sujeto a dependencias abiertas.
- PILOT AUTHORIZED: **NO**.
