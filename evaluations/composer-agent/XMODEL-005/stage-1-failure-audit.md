# XMODEL-005 — Auditoría de fallos de Stage 1

## Veredicto

**D — MIXED: MODEL COMPLIANCE + CONTRACT/HARNESS ERGONOMICS**

XMODEL-005 sigue siendo un test prospectivo negativo válido. No revela un defecto semántico de Composer Interface v1.1 ni exige cambios en conocimiento canónico o genre pack. Sí revela dos necesidades no musicales: hacer explícita la forma de Stage 1 con un esquema estructurado aplicable y activar enforcement JSON en el runner.

## Payloads visibles

Los payloads de Qwen y Ministral son byte-identical (`06132699e004ddc09c12591093c15ece5f2916953aa8951921b9dc7cd4ce0278`). Cada uno contiene el brief exacto, `system-contract-v1.1.md`, `decision-schema.yaml`, `guardrails.yaml`, `completion-checklist.yaml`, conocimiento aprobado, genre pack indie-dance, referencia N3-P, `stage-1-decision-trace-schema.yaml` y la instrucción congelada. No se enviaron meras rutas: los textos están delimitados como `BEGIN RECORD ... END RECORD` dentro del payload. El preflight de ambos payloads fue PASS y el hash del brief coincide con XMODEL-003.

La condición NO-EXAMPLE se mantiene: el paquete transmitido no contiene identificadores de composición SONG-001..004 ni casos históricos. `XMODEL-001` en `test_id` es metadato del brief, no un ejemplo compositivo.

## Qwen

### Requisitos visibles

Sí, `decision_id` estaba explícitamente requerido:

- `datasets/composer-interface-v1.1/decision-schema.yaml` contiene `decision_trace_required: [decision_id, ...]`.
- `integrations/composer-agent/stage-1-decision-trace-schema.yaml` contiene `decision_fields: [decision_id, ...]`.
- `completion-checklist.yaml` exige `decision_id` en cada entrada y `n3_p_required_fields` lo exige específicamente para N3-P.

La estructura N3-P también estaba explícita, con los cuatro outcomes permitidos y los campos `decision_id`, `candidate_strategies`, `selected_outcome`, `selection_basis`, `bass_groove_interaction`, `focal_hierarchy_interaction`, `section_behavior` y `development_behavior`. Por tanto, el nombre exacto sí estaba visible en el payload, en más de un registro.

Los retries 1 y 2 señalaron respectivamente JSON incompleto/mal formado, bases inválidas y campos N3-P faltantes. El retry 3 exigió un único objeto y un `selected_outcome` válido, pero **no dijo explícitamente que faltaba `decision_id`**. Qwen corrigió la envoltura Markdown del intento 1 y los fragmentos JSON múltiples del intento 2; en el intento 3 dejó un único JSON, pero omitió ese campo N3-P.

### Clasificación

| Intento | Hallazgo | Clase | Interpretación |
|---|---|---|---|
| 1 | Cerca Markdown alrededor de una respuesta estructurada | D — FORMAT | Incumplimiento de salida estructurada; terminó con `stop`. |
| 2 | Varios objetos JSON consecutivos / datos extra | D — FORMAT | Corrigió la cerca, pero no produjo una raíz única. Terminó con `stop`. |
| 3 | N3-P sin `decision_id` | C — CONTRACT REPRESENTATION | El contrato era claro y el modelo omitió un campo obligatorio; el diagnóstico no nombró ese campo. |

No hay evidencia de A (musical/knowledge), ni de E (output-budget) en Qwen. Los claims no sustentados que puedan aparecer en el contenido siguen siendo HUMAN AUDIT y no fueron la causa mecánica del bloqueo final. La causa primaria es cumplimiento de formato/contrato, con ergonomía de retry como factor secundario.

## Ministral

### Requisitos visibles

La instrucción congelada decía `Return only the stage-1 schema object`; el contrato exigía una salida estructurada. Eso hace legítimo rechazar Markdown, pero la prohibición literal de `code fences` no aparecía en el primer prompt. Sí fue añadida explícitamente en los retries 1 y 2: `Do not use Markdown fences, headings, commentary...`. Ministral no la obedeció.

No se suministró ni aplicó un JSON Schema de Stage 1 en la llamada API. `staged_runner.py` solo envía `model`, `messages` y `options`; no envía el campo Ollama `format`. El esquema YAML de Stage 1 es una especificación estructural, no un JSON Schema aplicado por el runner. El modelo recibió los registros textuales, pero no una restricción de decodificación.

### Clasificación

| Intento | Hallazgo | Clase | Interpretación |
|---|---|---|---|
| 1 | Markdown, texto explicativo y cerca JSON; captura limitada por longitud | D + E | Fallo de formato y exceso de verbosidad bajo `num_predict: 4096`. |
| 2 | Sigue generando Markdown y texto voluminoso; captura limitada por longitud | D + E | El retry identifica las cercas, pero el modelo no modifica la forma y el contexto acumulado crece. |
| 3 | Sigue generando Markdown; `done_reason: length` | D + E | Agotó el máximo de tres intentos sin una salida parseable. |

El agotamiento de longitud proviene principalmente de la verbosidad del modelo y, secundariamente, de reenviar el payload completo más la salida previa y diagnósticos en cada retry. El presupuesto fijo de 4096 no cambió. No es una causa musical ni de conocimiento. No se observó una reparación estructural suficiente en respuesta a los diagnostics.

## Runner y enforcement estructurado

Ollama admite `format` con JSON Schema y el runner v1.1 existente (`ollama_runner.py`) ya tiene una ruta técnica para enviarlo. `staged_runner.py` no la utiliza. El uso de un JSON Schema **específico de Stage 1**, limitado a la raíz DecisionTrace, decisiones obligatorias y N3-P, sería enforcement técnico: restringiría sintaxis, tipos, enums y campos requeridos; no escogería notas, acordes, forma, groove, N3-P ni AP, y no repararía semántica.

No debe aplicarse directamente `datasets/composer-interface-v1.1/output-schema.json` completo en Stage 1, porque ese contrato de envolvente también exige checklist, guardrails y candidato SongPlan de etapas posteriores. La opción segura es un esquema JSON de Stage 1 derivado de los requisitos ya congelados, sin cambiar su significado musical.

## Estrictez del gate

- `decision_id` es genuinamente obligatorio en el contrato congelado, especialmente para N3-P. El rechazo de Qwen es correcto.
- Rechazar Markdown es genuinamente necesario para un gate mecánico que recibe un objeto JSON. El primer prompt lo comunica de forma indirecta (`solo objeto`); la ergonomía sería mejor con una frase literal y una restricción `format`.
- Ningún gate está imponiendo una decisión musical. Las afirmaciones no estructurales permanecen HUMAN AUDIT.

## Cambios necesarios

| Área | ¿Cambio? | Decisión |
|---|---|---|
| Composer Knowledge | No | Sin evidencia nueva. |
| Genre pack | No | Sin evidencia nueva. |
| Semántica de Interface v1.1 | No | Los nombres y requisitos son suficientes. |
| Runner / serialización | Sí | Ensamblar y enviar un JSON Schema específico de Stage 1 mediante `format`; conservar payload y hash. |
| Prompt Stage 1 | Sí, aclaración menor | Añadir literalmente “exactly one JSON object; no Markdown/code fences/commentary”. No cambia semántica. |
| Presupuesto de salida | No por ahora | Mantenerlo para comparabilidad; medir después del enforcement. |

## Decisiones finales solicitadas

- **Qwen:** fallo primario de cumplimiento C/D bajo contrato claro; ergonomía de retry contribuyó porque el último diagnóstico no nombró `decision_id`.
- **Ministral:** fallo D/E de cumplimiento de salida y verbosidad, agravado por ausencia de enforcement JSON; retries explícitos no fueron obedecidos.
- **Cambio de conocimiento canónico requerido:** no.
- **Cambio de genre pack requerido:** no.
- **Cambio de versión semántica de interfaz requerido:** no.
- **Enforcement structured-output del runner recomendado:** sí.
- **Aclaración del prompt Stage 1 recomendada:** sí, solo textual y no semántica.
- **Cambio de output-budget recomendado:** no en esta fase.
- **XMODEL-006 justificado:** no todavía. Primero debe implementarse y probarse la corrección técnica del runner/esquema; después podrá decidirse una nueva corrida.
