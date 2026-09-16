# XMODEL-003 — Auditoría del control de presupuesto

## Veredicto

**C — Ambos modelos siguen fallando; el confound de presupuesto fue eliminado.**

XMODEL-003 mantuvo brief, prompt congelado, interfaz v1.1, condición NO-EXAMPLE,
schema y parámetros de generación de XMODEL-002, cambiando únicamente
`num_predict: 8192 → 12288`. Ambos modelos terminaron naturalmente. Qwen produjo
exactamente la misma salida que en XMODEL-002; Ministral produjo una respuesta
JSON completa, pero conserva incumplimientos semánticos, de cobertura,
guardrails y SongPlanV2. No se ejecutó music-engine ni se generó MIDI.

## Validez de la prueba

| Condición | Resultado |
|---|---|
| Brief igual a XMODEL-002/XMODEL-001 | **PASS** — SHA256 `464AE4378BCB7236F0FB36DA52EB65DCB03735197284E3A6899B8686D51EDE0B`. |
| Prompt igual a XMODEL-002 | **PASS** — SHA256 `F98BED243462602EAF5DE7A1E34DE53E7D4E261BFBB71916ED68CC2B165E2AB5`. |
| NO-EXAMPLE | **PASS** — no se suministran ejemplos. |
| Interfaz y schema | **PASS** — v1.1 y schema con SHA256 `7D334387404BD312A300460D2986E7E19AD8D885E842701A219EE91D935E332B`. |
| Parámetros comunes | **PASS** — temperatura 0, seed 41, top_p 1, top_k 40, repeat_penalty 1, num_ctx 32768 y num_predict 12288. |
| Captura UTF-8 | **PASS** — cada `raw-output.txt` coincide con `message.content` del API y con su hash de captura. |
| Outputs modificados | **NO** — preservados sin normalización ni reparación. |

## Auditoría de terminación

- Qwen3-14B: `done_reason: stop`, `prompt_eval_count: 16820`, `eval_count: 5467`.
- Ministral-3-14B: `done_reason: stop`, `prompt_eval_count: 17473`, `eval_count: 10064`.

**OUTPUT LENGTH CONFOUND: REMOVED** para ambos runs. Esto solo demuestra que no
terminaron por el límite de salida; no demuestra corrección musical ni de
interfaz.

## Qwen3-14B

Raw SHA256: `eaf53702cce48908df35d4312fce73f67199f3441182c0ca0f8fc6e8524ac7c1`.

El hash y los bytes son idénticos a XMODEL-002. El output JSON sigue declarando
`READY_FOR_VALIDATION`, pero solo desarrolla FORM y N3-P en `decision_trace`; el
checklist nominal de 14 filas no aporta trazas completas para las demás
decisiones. N3-P queda explícito como **FULL**, con estrategias, base e
interacciones requeridas. Ranking y atribución del Owner pasan: no inventa
RANK-1/RANK-2 ni atribuye una decisión al Owner. Artistic Priority sigue fallando
en la ruta N3-P, que selecciona FULL mediante FILTER sin demostrar que el filtro
elimine las alternativas; el handoff TEXTURE sí usa correctamente prioridad
artística.

GR-011 se marca PASS sin voicings armónicos explícitos que permitan comparar
etiquetas y pitches; por tanto la integridad no está demostrada. El candidato
SongPlanV2 falla por `energy` textual, claves de asignación armónica no
autorizadas, track `percussion` sin `kit_id`/`map_id` y variación
`register: "+2"` no admitida. La puerta de completitud falla y queda
**BLOCKED BEFORE MATERIALIZATION**.

Unsupported claims: **8**, igual que en la auditoría XMODEL-002. Incluyen
efectos atribuidos a ABABCB, suficiencia para carácter hipnótico, supuesta
necesidad de textura electrónica de género, claims de percusión hipnótica,
cumplimiento infundado de GR-001/GR-011 y el `run_id` falso de XMODEL-001.

**Comparación con XMODEL-002:** UNCHANGED en bytes, formato, cobertura, claims,
guardrails, SongPlanV2 y materialización. El fallo restante es **SEMANTIC /
INTERFACE APPLICATION**, no truncamiento. El presupuesto aumentado no tuvo
efecto observable en Qwen; esto no demuestra determinismo universal.

## Ministral-3-14B

Raw SHA256: `a7ed92993dc6c9712e73196f07d181b79f1b37c714c7c27539e5566a09f22209`.

**Previously truncated: YES. Now complete generation: YES.** El JSON termina
correctamente y contiene las 14 filas del checklist. Sin embargo, la fila
`LEAD_MOTIF_BEHAVIOR` se marca `NOT_APPLICABLE` aunque el brief permite y el
candidate contiene melodía; `SONGPLAN_HANDOFF` declara conformidad sin validación
real; y varias decisiones apuntan a trazas incompletas. Por ello la cobertura y
la puerta READY siguen fallando.

N3-P queda explícito como **FULL**: considera estrategias, selecciona por
`ARTISTIC_PRIORITY`, declara interacciones bajo/groove, foco, secciones y
desarrollo, y no atribuye la decisión al Owner. Ranking pasa: RANK-1 no usado y
RANK-2 no disponible. Artistic Priority pasa para FORM, HARMONY y N3-P en cuanto
a procedimiento formal, aunque algunas razones de filtrado no están respaldadas.

Guardrails fallan. GR-011 se aplica a riesgo rítmico/bajo y se marca PASS sin
voicings explícitos suficientes; GR-010 y GR-008 se convierten en supuestas
reglas contra DELEGATED/INTENTIONALLY_ABSENT. La selección armónica incluye
“progresión menos común para evitar clichés”, un claim de género no suministrado.

Unsupported claims: **10**, contando solo afirmaciones de regla, efecto,
alcance, evidencia o procedencia no respaldadas, no las notas elegidas como
material. Incluyen la regla de cambios obligatorios en dos dominios, priorizar
groove sobre melodía como prescripción, superioridad perceptiva de expansión
modal, filtros basados en GR-008/GR-010/GR-011, PASS de integridad sin voicings,
y los metadatos de corrida falsos heredados de XMODEL-001.

SongPlanV2: **FAIL**. Aunque ahora es extraíble y completo, usa `energy` textual;
asignaciones con `bar_range` no admitido; variaciones libres como strings
(`add_hi_hat_offbeats`, `double_snare_on_4`, `add_slide_to_C3_on_last_beat`);
track percussion sin `kit_id`/`map_id`; y no contiene una realización armónica
explícita que respalde GR-011. Queda **BLOCKED BEFORE MATERIALIZATION**.

**Comparación con XMODEL-002:** IMPROVED en completitud de JSON y extracción del
candidate; el progreso es atribuible al presupuesto suficiente para terminar la
respuesta, no a una solución de los problemas semánticos. Artistic Priority,
ranking, Owner attribution y N3-P permanecen aproximadamente iguales; guardrails,
claims y SongPlanV2 siguen fallando. La terminación completa permite observar el
fallo semántico que antes estaba mezclado con truncamiento.

## Resumen comparativo

| Dimensión | Qwen | Ministral |
|---|---|---|
| Longitud / formato | UNCHANGED; completo | IMPROVED; ahora completo |
| Cobertura obligatoria | UNCHANGED; FAIL | IMPROVED en cantidad, FAIL semántico |
| Artistic Priority | UNCHANGED; FAIL parcial | UNCHANGED; PASS procedimental |
| Ranking | UNCHANGED; PASS | UNCHANGED; PASS |
| Owner attribution | UNCHANGED; PASS | UNCHANGED; PASS para Owner |
| N3-P | UNCHANGED; FULL | UNCHANGED; FULL |
| Guardrails | UNCHANGED; FAIL | UNCHANGED; FAIL |
| Claims no sustentados | UNCHANGED; 8 | IMPROVED respecto a XMODEL-002 en forma completa, pero aún 10 |
| SongPlanV2 | UNCHANGED; FAIL | IMPROVED en extracción, FAIL en validez |
| Materialización | BLOCKED | BLOCKED |

No se infiere causalidad universal. La evidencia sí permite separar el problema
de truncamiento de los fallos semánticos restantes en Ministral.

## Resultado final

**C — BOTH MODELS STILL FAIL; OUTPUT-BUDGET CONFOUND REMOVED**

Qwen: `stop`, 5467 tokens, raw igual a XMODEL-002: **YES**, semantic compliance
**FAIL**, SongPlanV2 **FAIL**, materialización **BLOCKED**, failure class
**SEMANTIC / INTERFACE APPLICATION**.

Ministral: `stop`, 10064 tokens, previamente truncado: **YES**, ahora generación
completa: **YES**, semantic compliance **FAIL**, SongPlanV2 **FAIL**,
materialización **BLOCKED**, failure class **SEMANTIC / INTERFACE APPLICATION**.

## Siguiente acción

Realizar una revisión semántica dirigida de los outputs completos de Ministral y
Qwen para decidir si hace falta una corrección mínima del contrato; no cambiar
Composer Knowledge ni materializar MIDI todavía.
