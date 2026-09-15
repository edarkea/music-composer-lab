# XMODEL-002 — Auditoría de cumplimiento de transferencia

## Veredicto

**C — Ambos modelos siguen fallando la puerta XMODEL-002.** Qwen entrega JSON
completo, pero marca `READY_FOR_VALIDATION` con cobertura decisional incompleta
y un SongPlanV2 inválido. Ministral mejora la cobertura y la decisión N3-P, pero
la generación termina por límite de longitud dentro del candidato; su JSON no se
puede parsear ni su SongPlan extraer. Ambos quedan **BLOCKED BEFORE
MATERIALIZATION**.

Esta es una auditoría de contrato y transferencia, no una evaluación de escucha,
calidad artística ni ranking entre modelos. No se invocó music-engine, no se
generó MIDI y no se editaron respuestas crudas.

## Validez de condiciones y preservación

| Comprobación | Resultado |
|---|---|
| Brief igual a XMODEL-001 | **SÍ** — los archivos son byte por byte iguales; SHA256 `464AE4378BCB7236F0FB36DA52EB65DCB03735197284E3A6899B8686D51EDE0B`. |
| Mismo prompt entre modelos | **SÍ** — ambos manifiestos de captura registran `f98bed243462602eaf5de7a1e34de53e7d4e261bfbb71916ed68cc2b165e2ab5`. |
| Condición NO-EXAMPLE | **SÍ** — no se suministran ejemplos ni aparecen SONG-001..004 en el prompt congelado. |
| Interfaz | **SÍ** — ambas capturas identifican `composer-interface-v1.1`. |
| Parámetros iguales | **SÍ** — temperatura 0, seed 41, top_p 1, top_k 40, repeat_penalty 1, num_ctx 32768, num_predict 8192. |
| Corridas independientes | **SÍ** — IDs de modelos distintos y timestamps de captura separados. |
| UTF-8/captura | **SÍ** — `raw-output.txt` coincide byte por byte con `message.content` de la respuesta API; hashes de manifiesto coinciden. El texto generado por Ministral está correctamente preservado en UTF-8. |
| Salida estructurada | **SÍ, según el runner/manifiestos** — se registra el schema JSON v1.1. El cuerpo del request no fue archivado por separado, así que la verificación independiente se limita a la configuración del runner y sus metadatos. Qwen termina con `done_reason: stop`; Ministral con `done_reason: length`. |
| SHA256 Qwen | `eaf53702cce48908df35d4312fce73f67199f3441182c0ca0f8fc6e8524ac7c1` — coincide. |
| SHA256 Ministral | `c6e980195956cc8f199e67fd71285eafebfc37abe3288b0b4bfa73f2943c1184` — coincide. |

**Condición válida.** Existe, sin embargo, una inconsistencia de registro: el
`run-manifest.yaml` compartido sigue diciendo `PREPARED_NOT_EXECUTED` y
`xmodel_002_run_count: 0`. No se modificó ese registro histórico. Las condiciones
se verifican a partir de las capturas individuales: brief, hash de prompt,
versión, configuración y metadatos de modelo.

## Qwen3-14B

**Formato: PASS.** Es JSON UTF-8 completo y contiene la envolvente requerida. El
`run_id` que el modelo emite (`XMODEL-001-OUTPUT`) es falso para esta corrida.

| Decisión requerida | Estado | Hallazgo |
|---|---|---|
| FORM | Resolved | ABABCB con segmentos de ocho compases. |
| SECTION ROLES | Unresolved | El checklist lista verse/pre-chorus/chorus/bridge/outro, pero el plan está rotulado A/B/C y no enlaza esos roles. |
| HARMONIC FRAMEWORK | Resolved en intención | C Ionian, marco diatónico/intercambio modal y etiquetas C Ionian/G Mixolydian. No hay voicings explícitos ligados a esas etiquetas. |
| FOCAL IDENTITY | Resolved, con conflicto | Declara lead melody, pero también que hi-hats mantienen el foco rítmico; la jerarquía no se reconcilia. |
| LEAD / MOTIF BEHAVIOR | Resolved en intención | Declara persistencia y variación gradual; el candidato no especifica una transformación V2 admitida que realice la variación. |
| BASS ROLE | Resolved | Bajo como base del groove, alineado con kick. |
| GROOVE | Resolved | 4/4 sincopado a 120 BPM. |
| N3-P | **FULL** | Decisión explícita con estrategias, base, outcome e interacciones de bajo, foco, secciones y desarrollo. |
| TEXTURE | Resolved | Capas con variación seccional. |
| DEVELOPMENT | Resolved en intención | Variación de motivo y textura; handoff incompleto. |
| ENERGY / TENSION / RELEASE | Resolved en intención | Build por capas; los valores `energy` del plan son strings, incompatibles con el contrato. |
| ENDING | Unresolved | Declara fade-out y resolución final en checklist, pero no los representa en SongPlan. |
| CROSS-DOMAIN CONFLICTS | Unresolved | La compatibilidad groove/armonía se declara genéricamente y queda sin resolver la jerarquía lead/hi-hat. |
| SONGPLAN HANDOFF | Unresolved | Hay candidato, pero no es SongPlanV2 válido. |

**Cobertura obligatoria: FAIL.** El checklist tiene 14/14 filas etiquetadas
RESOLVED, pero `decision_trace` y `resolved_major_decisions` solo desarrollan
FORM y N3-P. Varias filas contradicen o no están sustentadas por el handoff. El
`READY_FOR_VALIDATION` no pasa la puerta.

**Artistic Priority: FAIL en el conjunto.** TEXTURE es un ejemplo correcto del
procedimiento v1.1: muestra opciones supervivientes, intención/tradeoff,
selección, no declara superioridad y continúa sin invocar al Owner. En cambio,
N3-P enumera FULL/MINIMAL/DELEGATED y elige FULL con `EXPORTED_KNOWLEDGE_FILTER`
sin mostrar filtros que eliminen las otras opciones. Esa selección debía usar
ARTISTIC_PRIORITY o aportar filtros trazables.

**Ranking: PASS.** RANK-1 figura como no usado, RANK-2 como UNAVAILABLE y no se
crea scope propio. Llamar FILTER a selecciones sin filtro demostrado no equivale
a declarar una capacidad de ranking, aunque sí debilita la trazabilidad.

**Owner attribution: PASS.** No atribuye preferencias ni decisiones al Owner y
no usa `resolved_by_owner`. El run_id incorrecto es una atribución de corrida,
no una afirmación sobre el Owner.

**N3-P: FULL; requisito explícito PASS.** La arquitectura contiene decisión,
estrategias, outcome y relaciones requeridas. Su base está sobredeclarada como
FILTER; eso afecta Artistic Priority y claims, no la presencia de la decisión.

**Guardrails: FAIL.** GR-011 aparece PASS con afirmación de que etiquetas y
pitches/voicings son consistentes. El plan no contiene voicings de acordes
asociados a las etiquetas; solo hay pitches de lead y bajo. No se podía verificar
integridad. GR-001 también aparece PASS aunque la respuesta convierte relaciones
perceptivas no demostradas en afirmaciones de efecto.

**Afirmaciones no sustentadas: 8.** Conteo conservador de afirmaciones
perceptivas, causales, de género, evidencia o procedencia; no cuenta elecciones
de material ni intenciones artísticas. Se cuentan: (1) ABABCB “enables” contraste
y movimiento hacia delante; (2) que el genre pack sustenta que ABABCB equilibra
repetición/desarrollo; (3) que el desarrollo es suficiente para carácter
hipnótico; (4) que capas de percusión mantienen movimiento hipnótico; (5) que
indie-dance necesita textura electrónica; (6) comparación “simpler than ABABCB
with bridge”, sin criterio coherente; (7) declaración infundada de cumplimiento
GR-001; y (8) el run_id XMODEL-001 inventado en la salida.

**SongPlanV2: FAIL.** La raíz tiene los campos correctos, pero el contenido
nested incluye `energy` como strings; asignaciones armónicas con
`section_id_or_start_bar_bar_count` en vez de `section_id` o
`start_bar`/`bar_count`; track de tipo percussion sin `kit_id` y `map_id`; y
`variation: {register: "+2"}`, que no es una operación V2 admitida. Además no
hay pitches/voicings armónicos que respalden GR-011. No se corrigió ni validó con
music-engine.

**Completion gate: FAIL. Materialización: BLOCKED BEFORE MATERIALIZATION.**

**Comparación con XMODEL-001:** formato, checklist nominal, Artistic Priority en
TEXTURE, ranking, atribución del Owner y N3-P mejoran. La cobertura trazable,
guardrails, SongPlan y materialización siguen fallando. Esta auditoría cuenta
ocho instancias no sustentadas; el conteo XMODEL-001 para Qwen se limitó a
efectos musicales y no es cardinalmente idéntico. Aplicando la misma categoría
sustantiva, en XMODEL-002 aparecen más afirmaciones de efecto/alcance, además de
fallos de procedencia. **Transferencia: IMPROVED, con fallo de puerta y regresión
en claims no sustentados.** El resultado es consistente con una mejora parcial,
no demuestra causalidad.

## Ministral-3-14B

**Formato: FAIL.** El texto crudo termina dentro de un evento del candidato
(`"events": [{"bar`) y no es JSON parseable. La respuesta API dice
`done_reason: length`; el capturador sí preservó fielmente la salida generada.

| Decisión requerida | Estado | Hallazgo |
|---|---|---|
| FORM | Resolved | Loop A, cambio de textura/densidad B y desarrollo C; 8/4/8 compases. |
| SECTION ROLES | Resolved | A establish, B prepare, C arrive. |
| HARMONIC FRAMEWORK | Resolved en traza | Cmaj7–G/B–Am7–Fmaj7 en A/B; Cmaj7–C6/9–Cmaj7 en C. No se completan voicings explícitos. |
| FOCAL IDENTITY | Resolved en checklist | Lead melody, apoyada por bajo y drums. |
| LEAD / MOTIF BEHAVIOR | Resolved en intención | Persistencia cíclica con contorno invariante. |
| BASS ROLE | Resolved en checklist | Groove support + harmonic foundation; falta handoff de bajo completo. |
| GROOVE | Resolved en checklist | Kick/snare/hi-hat y patrón declarados. |
| N3-P | **FULL** | Decisión explícita con FULL/MINIMAL, base ARTISTIC_PRIORITY e interacciones requeridas. |
| TEXTURE | Resolved en checklist | Shaker/claps en B/C y lead focal. |
| DEVELOPMENT | Resolved en intención | Desarrollo armónico en C. |
| ENERGY / TENSION / RELEASE | Resolved en checklist, handoff débil | Declara release armónico/textural en C; el candidato incompleto no permite realizarlo y sus valores `energy` visibles son strings. |
| ENDING | Unresolved | Describe B→C como iteración de llegada, no define un final. |
| CROSS-DOMAIN CONFLICTS | Unresolved | Declara `conflicts: []`, aunque sus filtros N3-P y armonía introducen conflictos no sustentados. |
| SONGPLAN HANDOFF | Unresolved | Se declara ready, pero termina a mitad del candidato. |

La lista visible de Ministral sí contiene las 14 decisiones del checklist; el
fallo no es una fila ausente. **Cobertura obligatoria: FAIL** porque ENDING y
CROSS-DOMAIN CONFLICTS no están realmente resueltos y SONGPLAN_HANDOFF no
existe completo, pese a marcar las filas RESOLVED y declarar READY.

**Artistic Priority: PASS para la decisión N3-P explícita.** FULL y MINIMAL
figuran como supervivientes; el modelo elige FULL por intención y tradeoff,
marca `superiority_claim: false` y continúa sin pedir decisión del Owner. La
selección armónica se atribuye a filtros con justificaciones débiles; eso queda
registrado como fallo de guardrails/claims, no como falsa atribución al Owner.

**Ranking: PASS.** RANK-1 no usado, RANK-2 no disponible, sin scope autoasignado.

**Owner attribution: PASS respecto a preferencias/decisiones.** No atribuye
elecciones al Owner. Sí fabrica un registro de corrida dentro de su respuesta:
run_id de XMODEL-001, timestamp anterior, hash de brief ficticio
`a1b2c3d4e5f6...` e identificador de modelo distinto al reportado por la
captura. Es una afirmación falsa de procedencia, no una preferencia del Owner.

**N3-P: FULL; requisito explícito PASS.** Incluye estrategias, outcome, base,
interacción bajo/groove, jerarquía focal, secciones y desarrollo. No se infiere
de los eventos solos.

**Guardrails: FAIL.** GR-011 se aplica a reajustes rítmicos y riesgo para el
bajo, que no son su propósito, y se marca PASS sin voicings explícitos. GR-010
se usa para afirmar que DELEGATED arriesga perder groove; GR-008 para declarar
que INTENTIONALLY_ABSENT contradice movimiento persistente. Esos guardrails no
establecen esas reglas musicales.

**Afirmaciones no sustentadas: 12.** Se aplica el mismo criterio conservador;
se excluyen opciones musicales, pero se cuentan reglas, efectos, atribuciones
de evidencia y procedencia inventados. Los 12 son: (1) regla de que desarrollo
audible requiere cambios en al menos dos dominios; (2) priorizar continuidad de
groove sobre variación melódica atribuida a GP-01; (3) afirmar que desarrollo
audible depende de contraste no melódico y atribuirlo a GP-01/GP-04; (4) decir
que el brief prioriza movimiento persistente sobre desarrollo melódico; (5) que
expansión modal es más audible que cambio de acordes, atribuida a GP-04; (6)
usar GR-011 como filtro de reajuste rítmico; (7) atribuir a GR-011 el riesgo de
OPT-C para el bajo; (8) atribuir a GR-010 pérdida de groove a DELEGATED; (9)
atribuir a GR-008 conflicto con movimiento persistente a INTENTIONALLY_ABSENT;
(10) declarar verificada integridad GR-011 sin voicings; (11) afirmar
cumplimiento de alcance GR-008 pese a esos usos; y (12) el bloque de metadatos
XMODEL-001/fecha/hash/modelo falsos.

**SongPlanV2: NOT EXTRACTABLE.** La generación termina a mitad de un evento;
no existe objeto completo para validar. No se reconstruyó ni completó.

**Completion gate: FAIL. Materialización: BLOCKED BEFORE MATERIALIZATION.**

**Comparación con XMODEL-001:** Artistic Priority, atribución del Owner y N3-P
mejoran; ranking permanece correcto. La cobertura se amplía hasta el checklist
completo, aunque conserva estados READY falsos; el output continúa incompleto.
Persisten fallos de guardrails y SongPlan. Claims no sustentados suben de 9 a
12. **Transferencia: IMPROVED, con salida incompleta, fallo de puerta y
regresión en claims no sustentados.** Consistente con mejora parcial, no prueba
causalidad.

## Comparación resumida

| Dimensión | Qwen3-14B | Ministral-3-14B |
|---|---|---|
| Completitud de salida | **IMPROVED** — JSON completo frente a salida incompleta en XMODEL-001 | **UNCHANGED** — respuesta y candidato siguen incompletos; el capturador ahora preserva el texto fielmente |
| Cobertura decisional | **IMPROVED** nominalmente, pero aún insuficiente para READY | **IMPROVED** — las 14 filas aparecen, aunque ending/conflictos/handoff no están resueltos |
| Artistic Priority | **IMPROVED** para TEXTURE; falla en la ruta N3-P | **IMPROVED** para N3-P |
| Ranking | **IMPROVED** | **UNCHANGED** — limitado en XMODEL-001 y respetado aquí |
| Atribución del Owner | **IMPROVED** | **IMPROVED** — sin preferencias inventadas; la procedencia de corrida sí se inventa |
| N3-P | **IMPROVED** — FULL explícito | **IMPROVED** — FULL explícito |
| Semántica de guardrails | **UNCHANGED** — GR-011 pasa sin voicings; GR-001 minimiza claims | **UNCHANGED** — GR-011 aplicado a ritmo y pasa sin voicings |
| Claims no sustentados | **WORSE** — 2 → 8 | **WORSE** — 9 → 12 |
| SongPlanV2 | **UNCHANGED** — candidato no válido | **UNCHANGED** — no extraíble |
| Puerta de materialización | **UNCHANGED** — bloqueado | **UNCHANGED** — bloqueado |

Los cambios son consistentes con transferencia parcialmente mejorada en
Artistic Priority, Owner attribution y N3-P. Los fallos y regresiones restantes
impiden atribuir causalidad o declarar que v1.1 ya supera la puerta.

## Puerta de materialización

| Modelo | Resultado | Motivo |
|---|---|---|
| Qwen3-14B | **BLOCKED BEFORE MATERIALIZATION** | `energy` no numérico, asignación armónica con campos no admitidos, track percussion sin `kit_id`/`map_id`, operación `register` no soportada y READY falso. |
| Ministral-3-14B | **BLOCKED BEFORE MATERIALIZATION** | JSON y SongPlan terminan incompletos; ending y handoff no están resueltos. |

No se llamó al motor y no se generó MIDI.

## Siguiente acción

Preparar una corrida nueva de Ministral con mayor presupuesto de salida,
conservando brief, prompt v1.1, NO-EXAMPLE y los mismos parámetros entre modelos;
no reemplazar las capturas de XMODEL-002.
