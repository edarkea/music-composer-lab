# Corrección de auditoría — XMODEL-011 Stage 1, recovery-002

## Clasificación corregida

`XMODEL-011-CODEX-STAGE1-A1-LAUNCH-RECOVERY-002` es un fallo técnico de validación del esquema, no un intento compositivo evaluable ni un fallo de la gate Stage 1.

La captura JSONL conserva `thread.started`, `turn.started`, `error` y `turn.failed`. El servicio recibió la solicitud y rechazó `text.format.schema` con HTTP 400, código `invalid_json_schema`. No hay `turn.completed` ni `final-output.txt`. Por ello queda evidenciado el inicio del turno y el rechazo de la solicitud por el servicio, pero no una respuesta de composición generada. La clasificación histórica `inference_event_evidence=true` en el manifiesto de captura no demuestra generación compositiva y permanece intacta como evidencia original; esta corrección separada establece la interpretación auditada.

Totales actuales: tres solicitudes de lanzamiento de CLI; cero respuestas de composición completas; cero intentos musicales evaluables; cero ejecuciones de la gate Stage 1. Recovery-002 no consumió un intento evaluable.

## Inspección del esquema congelado

Archivo: `model-visible/stage-1/output-schema.json`  
SHA256: `fd097161e6b35c6c3aae4c2cbbfe7146a550e56cfe33be36575358b6aa8e76f5`

Esquemas que describen objetos:

| Ruta JSON Schema | `additionalProperties` | Campos requeridos | Campos opcionales |
|---|---|---|---|
| `$` | `false` | `decision_trace` | ninguno |
| `$defs/common` | ausente | `decision_id`, `options_considered`, `selection_basis`, `active_intention`, `tradeoff`, `trace_reference` | `selected_option`, `surviving_options`, `superiority_claim` |
| `$defs/generic_decision` | `false` | `decision_id`, `options_considered`, `selection_basis`, `active_intention`, `tradeoff`, `trace_reference`, `selected_option` | `surviving_options`, `superiority_claim` |
| `$defs/n3_decision` | `false` | `decision_id`, `options_considered`, `selected_outcome`, `candidate_strategies`, `selection_basis`, `active_intention`, `tradeoff`, `trace_reference`, `bass_groove_interaction`, `focal_hierarchy_interaction`, `section_behavior`, `development_behavior` | `surviving_options`, `superiority_claim` |
| `$defs/generic_decision.not` (objeto de restricción) | ausente | ninguno | `decision_id` |

`$defs/common` no está referenciado por el árbol de `$ref`, pero sí contiene un objeto incompleto. Otros problemas estructurales confirmados:

- `oneOf` en `$defs/decision` y `not` en `$defs/generic_decision`; `not` no pertenece al subconjunto admitido por Structured Outputs estricto.
- Los arreglos `options_considered`, `candidate_strategies` y `surviving_options` carecen de `items`.
- Los esquemas `{}` de `tradeoff`, `selected_option`, `section_behavior` y `development_behavior` no definen una representación tipada compatible con la salida estricta.
- En objetos genéricos y N3-P, `surviving_options` y `superiority_claim` son opcionales; Structured Outputs estricto requiere que todas las propiedades se declaren en `required`. Representar opcionales como campos requeridos nullable también modificaría los valores aceptados por el esquema original, que no permite `null` en esas propiedades.
- La gate Stage 1 local está en `integrations/composer-agent/staged_harness.py`; `gate_capture.py` exige una captura completa y un evento terminal antes de invocarla. Ambos archivos quedaron sin modificar.

La documentación oficial de OpenAI confirma que Structured Outputs estricto exige `additionalProperties:false` en cada objeto y todos los campos en `required`, usa `null` para emular opcionales y no admite `not`. También exige que las ramas de `anyOf` cumplan el subconjunto admitido. [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)

El error HTTP dice `context=()` aunque el archivo local tiene `additionalProperties:false` en la raíz. Los artefactos de recovery-002 no guardan el cuerpo de solicitud ni el hash/ruta del esquema efectivamente transmitido, así que no es posible demostrar qué nodo exacto produjo el mensaje en el servicio. `$defs/common` es un nodo concreto que incumple directamente el requisito; en cualquier caso, corregir solo ese nodo o solo la raíz no resolvería los demás bloqueos estructurales enumerados.

## Decisión de compatibilidad

No se creó un esquema de compatibilidad ni se preparó recovery-003. Para ser aceptado por la respuesta estricta habría que resolver, entre otros puntos, los tipos de los cuatro campos abiertos, el tipo de elementos de los arreglos, la selección entre `oneOf` y una composición admitida, y la presencia/representación de campos opcionales. El contrato actual no permite establecer sin suposición si acotar esos valores a cadenas/arreglos de cadenas conserva todas las representaciones intencionadas; hacer obligatorios los opcionales también estrecha la aceptación original. No se elige ni se aplica esa reinterpretación técnica.

No cambia ni se debilita la gate local. No se agregan valores por defecto, decisiones musicales, ni se eliminan campos de salida. Una siguiente recuperación requiere primero resolver la representación de esos campos en el contrato de salida o autorizar un modo de transporte distinto del esquema estricto y verificar que la gate original siga siendo suficiente.

## Integridad y estado

- Payload Stage 1 sin cambios: `58646fd9fbef25c17b6b5cc7f846490989316f25d5084469d2b8b4cb074a423d`.
- Esquema original sin cambios: `fd097161e6b35c6c3aae4c2cbbfe7146a550e56cfe33be36575358b6aa8e76f5`.
- Capturas y tres registros históricos sin cambios.
- Sin inferencia Codex ejecutada durante esta auditoría; sin salida compositiva; sin MIDI.
- Recovery-003: no preparado; Stage 1 permanece sin intentos evaluables consumidos.

## Comprobaciones locales

- Hash del payload congelado coincide con el esperado: PASS.
- Hash del esquema original coincide con el registro anterior: PASS.
- Estructura JSON legible y rutas de objetos/propiedades enumeradas: PASS.
- Gate de captura rechaza datos incompletos antes de llamar a la gate: inspección estática PASS; no se ejecutó una prueba de captura nueva contra archivos históricos.
- Regresión de recovery-002: 9/9 PASS; regresión offline XMODEL-011: 23/23 PASS; regresión staged harness: 54/54 PASS.
- Validación local con `jsonschema`: NOT RUN; la dependencia no está instalada en `.venv`.
- Esquema de compatibilidad, launcher y pruebas de aceptación remota: NO CREADOS / NO EJECUTADOS.
