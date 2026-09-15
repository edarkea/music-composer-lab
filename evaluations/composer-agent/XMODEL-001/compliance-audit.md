# XMODEL-001 — Auditoría de cumplimiento de interfaz externa

## Veredicto

**C — Ambos modelos requieren reparación / fallan la puerta de transferencia.** Esta es una evaluación de transferencia de interfaz y cumplimiento de contrato, no una evaluación de escucha ni de calidad musical. Ningún candidato pasa la puerta de materialización; no se generó MIDI.

## Condiciones del ensayo y preservación

- **Condición:** `NO-EXAMPLE TRANSFER CONDITION`.
- **Misma entrada:** **SÍ, verificada** a nivel de artefactos congelados. `run-manifest.yaml` declara `same_prompt_for_both: true`; existe un único `frozen-prompt.txt` que contiene el paquete de interfaz, contrato, brief y tarea. No hay registro de prompts individuales divergentes.
- **Ejemplos suministrados:** **NO**. El manifiesto declara `examples_in_prompt: false`; el prompt congelado incluye referencias/listado de archivos opcionales, pero no el contenido de los cuatro ejemplos.
- Esta condición no invalida el ensayo. La mención de SONG-002/SONG-003 dentro de una salida se evalúa como material no provisto, no como ejemplo autorizado.

SHA256 de los archivos crudos, que se conservaron sin cambios:

| Modelo | Archivo | SHA256 |
|---|---|---|
| Qwen3-14B | `qwen3-14b/raw-output.txt` | `AA13E9374A32D37E33413FCC891E1BCDDB5B9F0A24D9CF522D7336A44DC3B8F3` |
| Ministral-3-14B | `ministral-3-14b/raw-output.txt` | `5B4B96CCF428FC60F74E1501399FB1FE975D4D6F6FDF31E42689146C69841226` |

No se generaron reemplazos, prompts corregidos ni materiales musicales nuevos. La única derivada es la extracción literal del objeto `songplan_candidate` de Qwen en [`qwen3-14b/songplan-candidate.yaml`](qwen3-14b/songplan-candidate.yaml), con hash y ruta del original en comentarios. No se creó `decision-trace.yaml` ni una salida normalizada: el resto del texto contiene edición/captura de terminal y campos dañados, y reconstruirlos requeriría reparación semántica. Ministral entrega extractos marcados como tales, con texto alterado por la captura y una salida truncada; no es seguro fabricar derivadas.

## Comparación resumida

| Dimensión | Qwen3-14B | Ministral-3-14B |
|---|---|---|
| Contrato de salida | **FAIL** — formato y decisión incompletos; `READY_FOR_VALIDATION` contradice los pendientes | **FAIL** — declara `BLOCKED`, pero ofrece extractos y un candidato no conforme/incompleto |
| Cobertura de decisiones | **FAIL** — solo centro/modo y tempo/groove; faltan forma explícita en compases, foco/lead, bajo, textura, N3-P, desarrollo y final resueltos | **FAIL** — decisiones parciales/contradictorias; la mayoría de los dominios del brief quedan sin resolver |
| Disciplina de alcance | **FAIL** — presenta como conocimiento y efecto soportado criterios no presentes en el paquete | **FAIL** — incorpora material sobre SONG-002/003 no suministrado y atribuciones de Owner sin fuente |
| ENUMERATE / FILTER / RANK | **FAIL** — declara `rank: true` y `rank_2_scope` sin soporte; filtrado declarado falso pese a reducir alternativas | **PASS, limitado a la declaración explícita** — declara `rank: false`/N/A y transfiere un tradeoff; esto no corrige los demás incumplimientos |
| RANK-1 / RANK-2 inventado | **SÍ / SÍ** — asigna criterio de ranking de tempo y alcance RANK-2 sin procedimiento ni soporte | **NO / NO** — no declara uso de RANK-1/2; sí presenta criterios y conocimiento no sustentados |
| Artistic Priority | **FAIL** — handoffs aparecen `resolved_by_owner` sin decisión del Owner y con tradeoffs inventados | **FAIL** — contiene un handoff pendiente útil, pero también atribuye al Owner preferencias que no constan y declara una prioridad por su cuenta |
| N3-P | **INVALID** — no decide arquitectura; hi-hats/drum machines en el candidato no sustituyen N3-P | **INVALID** — no instancia N3-P ni asigna outcome |
| General vs. género | **FAIL** — atribuye decisiones a knowledge/genre sin referencias válidas ni capas separadas | **FAIL** — convierte una supuesta recomendación de género en claim y mezcla análisis/general/género |
| Claims musicales sin soporte | **2** según el criterio de conteo explicado abajo | **9** según el mismo criterio |
| Incertidumbre | **FAIL** — un valor numérico arbitrario (`0.2`) y una incertidumbre limitada; incompleto | **PARTIAL en contenido; FAIL en contrato** — lista incertidumbres, algunas creadas por sus propios supuestos; no cubre la traza completa |
| Guardrails | **FAIL** — declara GR-011/GR-012 PASS sin evidencia suficiente; omite los restantes | **FAIL** — usa GR-011 para una infracción de modo/knowledge, aunque GR-011 es de etiqueta/voicing; GR-012 también se marca PASS frente a claims añadidos |
| SongPlanV2 | **FAIL** — el YAML genérico se extrae y parsea, pero el runtime lo rechaza como SongPlanV2 | **NOT EXTRACTABLE** — bloque parcial con estructura ajena al schema, segmentos malformados y sin objeto completo |
| Reparación requerida | **SÍ** | **SÍ** |
| Puerta de materialización | **BLOCKED** | **BLOCKED** |

Los dos modelos bloquearon o debieron bloquear la salida antes de materializar. No hay comparación artística en este informe.

## Auditoría por modelo

### Qwen3-14B

**Contrato y cobertura.** Entrega claves que parecen cubrir DecisionTrace, decisiones resueltas, handoffs, capacidades, guardrails, incertidumbres y candidato, pero no satisface la estructura completa requerida. Solo desarrolla dos decisiones. Marca el resultado global `READY_FOR_VALIDATION`, aunque declara ambigüedad de modo y atribuye decisiones al Owner sin autorización. El candidato deja forma en duraciones de reloj, sin longitudes de compás, sin SongPlanV2 root contract y sin tracks/events explícitos.

**Ranking y prioridad artística.** La declaración `capability: rank` para tempo, `rank_1_scope` y `rank_2_scope` no está respaldada por conocimiento comparativo, tarea válida o procedimiento. Contradice el límite RANK-2 del paquete. Declara `filter: false` pero elimina D Dorian de una lista al proponer supervivientes distintos, sin registrar filtro. Los handoffs de D-001/D-002 dicen `resolved_by_owner` pese a que no existe respuesta del Owner; el texto inventa tradeoffs aceptados. Ranking: **FAIL**. Artistic Priority: **FAIL**.

**N3-P y guardrails.** No aparece una decisión explícita FULL/MINIMAL/DELEGATED/INTENTIONALLY_ABSENT, ni análisis de su relación con bajo, foco, secciones o desarrollo. La mención de hi-hats y drum machines como elementos no resuelve N3-P. GR-011 se marca PASS pese a que no hay pitches/voicings explícitos que comparar; GR-012 se marca PASS mientras la salida presenta afirmaciones perceptivas no sustentadas. No separa general, género y preferencia en la evidencia declarada.

**Claims sin soporte: 2.** Conteo conservador de afirmaciones de efecto musical, excluyendo materiales elegidos como preferencias compositivas: (1) “C minor provides dark, tense foundation suitable for hypnotic motion”; (2) “128 BPM provides energetic yet controlled foundation”. Ambas asignan efecto/adecuación sin soporte del paquete o de una escucha. El “0.2” de incertidumbre es precisión numérica arbitraria, pero no se cuenta como claim musical. También hay atribuciones imprecisas de fuente y pases de guardrail no demostrados; se registran como incumplimientos, no se duplican en este conteo.

**SongPlan.** Se extrajo literalmente la propiedad del candidato sin alterar su contenido y se validó con el runtime local. El validador respondió `PARSE_FAILURE`, indicando `schema_version '2.0' is unsupported` para esa estructura. El objeto contiene `format`, `schema`, `structure`, `harmonic_progression` y listas de elementos, en vez de los campos explícitos requeridos por SongPlanV2 (`name`, `tempo`, `time_signature`, `tonic`, `mode`, `style`, `arrangement`, `tracks`, eventos y pitches). Por tanto, YAML parseable no equivale a SongPlanV2 válido. No se corrigió.

**Outcome por modelo:** output contract FAIL; cobertura FAIL; N3-P INVALID/no; ranking FAIL; Artistic Priority FAIL; claims sin soporte 2; SongPlan FAIL; reparación SÍ; materialización BLOCKED.

### Ministral-3-14B

**Contrato y cobertura.** La salida declara `BLOCKED`, lo cual evita afirmar que está lista; sin embargo, DecisionTrace está marcada como extracto, las decisiones resueltas son contradictorias con unresolved/pending, y el texto termina a mitad de la sección de bloqueos. La propuesta usa estructuras propias (`metadata`, `sections`, `harmonic_labels`, `development`, `release`) y placeholders `UNRESOLVED`; no constituye un candidato completo SongPlanV2. Incorpora secciones verso/pre-coro/coro que no vienen del brief congelado, a la vez que mantiene decisiones relacionadas sin resolver.

**Ranking y prioridad artística.** La declaración de capacidad de ejemplo dice `rank: false`, `rank_1_scope: N/A`, `rank_2_scope: N/A`; no hay un uso explícito de RANK-1 o RANK-2. En esa dimensión estrecha respeta el no-ranking y propone handoff. Sin embargo, afirma una preferencia del Owner por evitar tonos usados en referencias, y redacta una prioridad de maximizar coherencia sin base ni autorización. Su handoff de HARMONIC-001 pide decisión del Owner y deja `PENDING_OWNER`, pero no remedia las atribuciones no autorizadas ni las contradicciones posteriores. Ranking: **PASS limitado**. Artistic Priority: **FAIL**.

**N3-P y guardrails.** N3-P no se instancia ni se selecciona outcome. No hay justificación sobre groove, bajo, jerarquía focal, secciones o desarrollo. La salida marca GR-011 por incluir una opción Lydian supuestamente no documentada; el GR-011 del paquete se refiere a integridad entre etiqueta armónica y pitches/voicing, no a exclusión modal. Tampoco presenta pitches concretas con las que evaluar esa integridad. GR-012 se marca PASS pese a claims no proporcionados. General knowledge, genre pack y análisis de una canción previa no quedan separados.

**Claims sin soporte: 9.** Conteo conservador de afirmaciones factuales/prescriptivas musicales y de procedencia, excluyendo opciones musicales que por sí solas podrían ser decisiones artísticas: (1) evitar progresiones “cliché” como I–V–vi–IV; (2) priorizar séptima menor en dominante para producir tensión; (3) evitar modulación abrupta; (4) definir “hipnosis” como repetición con variación armónica sutil; (5) atribuir al genre pack la recomendación de armonías densas con espacio; (6) atribuir a LF-022 de SONG-002 evidencia de acumulación armónica, aunque ese hallazgo trata una inconsistencia etiqueta/voicing; (7) decir que La♯ mayor/C natural con #4 evita una colisión musical con SONG-003; (8) atribuir al Owner preferencia por tonos no usados en referencias; (9) afirmar que 4/4 implica swing. Las menciones de SONG-002/003 son especialmente fuera de condición: sus ejemplos no fueron suministrados en el prompt congelado.

**SongPlan.** No se extrajo derivada. El propio modelo lo llama excerpt; el contenido visible está parcialmente corrupto/truncado y usa campos no admitidos, pitches no especificadas/placeholders y armonía unresolved. La normalización exigiría reconstruir texto y decisiones. Estado: **NOT EXTRACTABLE**, sin validación contra el runtime.

**Outcome por modelo:** output contract FAIL; cobertura FAIL; N3-P INVALID/no; ranking PASS limitado; Artistic Priority FAIL; claims sin soporte 9; SongPlan NOT EXTRACTABLE; reparación SÍ; materialización BLOCKED.

## Cumplimiento de conocimiento y lectura comparativa

Ambos modelos encontraron decisiones subdeterminadas por el conocimiento, pero ninguno conservó con consistencia el procedimiento: representar supervivientes, explicar que no hay ranking aplicable y transferir la decisión al Owner. Qwen falsea resolución del Owner y declara ranking; Ministral incluye un handoff razonable, pero lo contamina con preferencias atribuidas y material de género/obras previas no recibido.

Los dos outputs mencionan estructura, percepción y composición, pero no preservan el puente de manera disciplinada. En particular, describen carácter emocional/hipnótico o causalidad entre armonía, tempo, disonancia y efecto sin soporte identificado. Ninguno completa guardrails, decisiones principales, incertidumbres y SongPlanV2 al nivel requerido. Esto constituye un resultado negativo de transferencia/contrato para ambos en la condición sin ejemplos; no demuestra incapacidad musical general ni compara su calidad artística.

## Puerta de materialización

| Modelo | Resultado | Motivo |
|---|---|---|
| Qwen3-14B | **BLOCKED BEFORE MATERIALIZATION** | El candidato no valida como SongPlanV2; además persisten incumplimientos de N3-P, ranking, atribución de Owner y guardrails. |
| Ministral-3-14B | **BLOCKED BEFORE MATERIALIZATION** | No existe candidato completo extraíble/validable; salida incompleta, N3-P ausente y guardrails mal aplicados. |

No se materializó MIDI, no se generó audio y no se hizo evaluación de escucha.

## Integridad del ensayo y siguiente acción

- Raw Qwen y Ministral: **sin cambios**; hashes registrados arriba.
- Composer Knowledge, genre pack, reglas y arquitectura: **sin cambios**.
- SongPlan/MIDI de canciones existentes: **sin cambios**.
- Ejemplos ausentes no invalidan XMODEL-001; el resultado se etiqueta como transferencia sin ejemplos.
- **Siguiente acción única:** revisar y corregir el adaptador de salida del modelo que se quiera volver a evaluar, y ejecutar una nueva corrida identificada separadamente con exactamente el mismo paquete congelado; no modificar ni reutilizar los outputs crudos de XMODEL-001 como si fueran nuevos.
