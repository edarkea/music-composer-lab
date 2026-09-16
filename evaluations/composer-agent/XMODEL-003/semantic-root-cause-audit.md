# XMODEL-003 — Auditoría semántica de causas raíz

## Alcance y veredicto

Se revisaron las salidas completas de Qwen3-14B y Ministral-3-14B capturadas con presupuesto suficiente para terminar de forma natural. El confusor de truncamiento queda eliminado: Qwen terminó con `stop` y 5.467 tokens de salida; Ministral terminó con `stop` y 10.064. Aun así, persisten fallos de semántica, trazabilidad y serialización.

**Resultado:** la evidencia no demuestra una carencia de conocimiento canónico ni exige un modelo más grande. Demuestra que la interfaz v1.1 se está ejecutando como una tarea de una sola pasada demasiado cargada y que el validador actual comprueba principalmente formato. La recomendación acotada es conservar la semántica v1.1 y añadir una ejecución por etapas con una compuerta determinista antes de aceptar la salida.

## Fallos compartidos

| ID | Comportamiento esperado e instrucción | Salida observada | Tipo y causa probable | Confianza |
|---|---|---|---|---|
| S-01 | `READY_FOR_VALIDATION` solo después de resolver todas las decisiones requeridas, justificar `NOT_APPLICABLE` y entregar un SongPlan válido. La checklist y el contrato de salida lo exigen. | Ambos marcan las 14 filas como resueltas y declaran READY aunque sus trazas no cubren todas las decisiones y sus SongPlan no pasan el contrato v2. | C: contrato/adaptador permite un estado contradictorio; F/E: autoverificación semántica insuficiente. | Alta |
| S-02 | Serializar exactamente el SongPlan v2: energía numérica, asignaciones por `section_id` o rango explícito, operaciones de variación permitidas y campos obligatorios de tracks. | Ambos usan campos o valores fuera del contrato; Ministral omite además `kit_id`/`map_id` en percusión. | D: dificultad de serialización; C/B: contrato anidado y carga de ejecución. | Alta |
| S-03 | GR-011 solo puede ser PASS cuando la etiqueta armónica concuerda con pitches/voicing explícitos o documenta la semántica de omisión/adición. | Ambos declaran PASS sin evidencia suficiente de voicings armónicos explícitos ni semántica de realización. | G/F: PASS no sustentado y aplicación incorrecta de guardrail; C: falta de comprobación de evidencia. | Alta |
| S-04 | La frontera creativa permite material candidato, pero prohíbe presentar reglas, efectos perceptuales, afirmaciones de género, evidencia o atribuciones como hechos no respaldados. | Ambos generan afirmaciones sobre indie-dance, desarrollo, tensión, superioridad o conocimiento exportado que no están justificadas por el paquete. | G: conocimiento no sustentado; E: razonamiento semántico y control de afirmaciones. | Alta |
| S-05 | La decisión, la traza, la checklist, los guardrails y el SongPlan deben referirse al mismo contenido. | En ambos hay desacoplamiento entre lo que se marca resuelto, lo que se traza y lo que se serializa. | B/C/F: carga de una sola pasada y falta de referencias deterministas. | Alta |
| S-06 | Una salida completa debe conservar metadatos de captura coherentes con la ejecución. | Ambos incluyen metadatos internos no fiables; en Ministral aparecen `run_id`, timestamp, hash de brief y modelo de una ejecución anterior o inventada. | H/G: alucinación de procedencia; el contrato no exige validar esos campos contra el manifiesto. | Alta |

## Fallos específicos de Qwen

| ID | Esperado / instrucción exacta | Actual | Causa probable | Confianza |
|---|---|---|---|---|
| Q-01 | Enumerar, filtrar y, si sobreviven alternativas, aplicar AP y registrar selección; GR-009 separa esas operaciones. | Selecciona `FORM` y `N3-P` mediante `EXPORTED_KNOWLEDGE_FILTER`; no registra AP para N3-P aunque sobreviven FULL/MINIMAL/DELEGATED. | F: confunde filtro de conocimiento con selección AP; B: demasiadas operaciones en una pasada. | Alta |
| Q-02 | Trazar todas las decisiones requeridas, incluidos roles de sección, armonía, lead, bajo, textura, desarrollo y cierre. | La `decision_trace` solo contiene FORM y N3-P, mientras la checklist declara 14 decisiones RESOLVED. | C/F: el contrato no obliga correspondencia traza-checklist. | Alta |
| Q-03 | La salida debe usar SongPlan v2 y representar cualquier evidencia armónica necesaria para GR-011. | Usa energía textual, `bar_range`, variaciones libres y no ofrece voicings armónicos explícitos. | D/C; la información estructural estaba disponible, pero no la realización armónica necesaria. | Alta |
| Q-04 | Sustentar las afirmaciones sobre género y efectos como conocimiento delimitado o hipótesis. | Presenta “indie-dance”, “controlled contrast” y necesidades de textura electrónica como razones de selección; se conservan ocho hallazgos de afirmación no sustentada. | G/E. | Alta |
| Q-05 | Aumentar presupuesto debe permitir completar la misma tarea de forma semánticamente mejor. | La salida es byte-identical a XMODEL-002 pese al presupuesto mayor. | H/F: patrón estable de generación; el presupuesto no ataca la compuerta de validación. | Alta |

## Fallos específicos de Ministral

| ID | Esperado / instrucción exacta | Actual | Causa probable | Confianza |
|---|---|---|---|---|
| M-01 | Toda decisión aplicable debe resolverse; `NOT_APPLICABLE` requiere una razón compatible con el brief y el material. | Marca `LEAD_MOTIF_BEHAVIOR` como `NOT_APPLICABLE` porque el brief no especifica melodía líder, aunque el brief deja libertad melódica y el candidato contiene melodía. | F/E: interpreta “no prescrito” como “no aplicable”. | Alta |
| M-02 | AP debe registrar alternativas supervivientes, selección, intención y trade-off, sin afirmar superioridad no respaldada. | FORM, HARMONY y N3-P tienen trazas AP completas; esto es correcto. Sin embargo, filtra opciones por reglas no autorizadas (“no cíclica”, falta de movimiento, falta de groove explícito) y usa la afirmación estilística de una progresión “menos común”. | F/G: AP bien formado en superficie, pero filtros y razones exceden el alcance. | Alta |
| M-03 | `N3-P` requiere arquitectura explícita, base de elección y realización en SongPlan; la elección puede ser FULL. | N3-P FULL está explícito y perceptualmente razonado, pero se apoyan filtros no exigidos por el brief. | G/F; el estado N3-P en sí está presente. | Media-alta |
| M-04 | SongPlan v2 exige energía numérica, operaciones de variación soportadas, `kit_id`/`map_id` y asignaciones válidas. | Usa `bar_range`, energías como `medium/high/low/peak`, variaciones libres y omite `kit_id`/`map_id`; las etiquetas armónicas carecen de voicing explícito. | D/C/F. | Alta |
| M-05 | La procedencia debe ser coherente con la captura real. | Incluye `XMODEL-001-20260914-001`, hash de brief falso y modelo/fecha no correspondientes; se conservan diez hallazgos conservadores de afirmación o metadato no sustentado. | H/G. | Alta |

## Artistic Priority y frontera creativa

La semántica AP de v1.1 es explícita: `ENUMERATE → FILTER → AP → SELECTION → CONTINUE`. También exige registrar alternativas supervivientes, opción elegida, intención, trade-off y ausencia de afirmación de superioridad. Por ello **no hay una ambigüedad conceptual de AP**. Hay una carga operacional alta: Qwen convierte FILTER en sustituto de AP, mientras Ministral ejecuta AP pero inventa criterios de filtrado no autorizados. La interfaz debe conservar estas operaciones; la compuerta debe comprobarlas.

La frontera de generación creativa también está explícita. Los modelos pueden elegir material candidato, pero no pueden convertir una preferencia o una hipótesis en regla de género, hecho perceptual, evidencia, atribución al Owner o superioridad. Los incumplimientos son de aplicación del modelo y de ausencia de validación, no una autorización ambigua del contrato.

No se observan atribuciones falsas al Project Owner ni uso efectivo de RANK-1/RANK-2. Qwen deja RANK-1 sin usar y RANK-2 no disponible; Ministral hace lo mismo. No aparece un requisito genuino de ranking.

## N3-P y guardrails

Ambos modelos declaran `N3-P = FULL`, con campos de arquitectura y realización. En consecuencia, **la cobertura de decisión N3-P está presente**. Qwen, sin embargo, no documenta AP para las alternativas supervivientes; Ministral sí lo hace. La salida Ministral añade razones de descarte que no proceden de los guardrails. Esto es un problema de semántica de selección, no evidencia de que FULL sea una mala arquitectura.

El problema de guardrails es mixto: las definiciones v1.1 son suficientemente explícitas, pero el modelo puede marcar PASS sin la evidencia requerida y el validador no verifica aplicabilidad, evidencia ni referencias. GR-011 es el caso más claro: no debe aceptarse PASS sin pitches/voicing o semántica documentada.

## Checklist y SongPlan

La checklist no es conceptualmente ambigua, pero su estado es autorreportado. El adaptador actual comprueba nombres, estados y algunas claves, no la correspondencia entre traza, checklist, guardrails y SongPlan. Por eso el problema es **MIXTO: ejecución/instrucción del modelo y diseño de validación**.

Qwen tenía información suficiente para serializar una estructura parcial válida, pero no produjo voicings armónicos ni decisiones trazadas suficientes para una handoff íntegra. Ministral tenía material explícito suficiente para una estructura SongPlan válida y pitches de bajo/melodía, pero no para justificar GR-011 sin añadir o declarar voicings armónicos; además serializó campos inválidos. En ambos casos una reparación determinista puede detectar y bloquear, pero no puede inventar pitches, voicings, decisiones AP o justificaciones musicales.

## Carga de una sola pasada

La tarea combina comprensión de conocimiento, enumeración, filtros, AP, selección, guardrails, material creativo, serialización SongPlan y autoauditoría. La repetición de fallos entre XMODEL-001/002/003, incluso con terminación natural, aporta evidencia de **carga de ejecución probable**, aunque no demuestra que sea la única causa.

Responsabilidades seguras para un adaptador determinista:

- validar JSON, claves exactas y todo el SongPlan v2 anidado;
- comprobar energía numérica, operaciones de variación, rangos, tracks y referencias;
- comprobar que cada decisión requerida tiene una traza única y que `NOT_APPLICABLE` contiene razón;
- comprobar campos y enums N3-P;
- impedir GR-011 PASS sin evidencia de voicing/pitches o semántica explícita;
- comprobar referencias de guardrails, AP y ausencia de ranking no autorizado;
- comparar metadatos de captura con el manifiesto;
- derivar READY solo después de pasar estas comprobaciones.

No es seguro que el adaptador elija AP, rellene decisiones, agregue pitches/voicings, corrija etiquetas armónicas, invente claims o infiera efectos perceptuales.

## Capacidad del modelo y decisión v1.2

El resultado no justifica modificar Composer Knowledge, el genre pack, la arquitectura musical ni iniciar investigación. Tampoco justifica concluir que un modelo más fuerte resolverá el problema: Ministral completa más contenido, pero conserva fallos de semántica y serialización; Qwen no cambia con mayor presupuesto.

**Decisión v1.2: B — mantener la semántica de la interfaz v1.1 y cambiar la arquitectura de ejecución/validación.** La siguiente mejora acotada es separar la generación de decisiones y trazas de la serialización SongPlan, con una compuerta determinista entre ambas. No se recomienda cambiar ahora la semántica AP, N3-P o la base de conocimiento.

## Informe final

- **Outcome:** causas raíz identificadas; v1.1 semánticamente utilizable, pero no aceptable sin compuerta de validación.
- **Shared semantic failures:** 6 — S-01 estado READY no sustentado; S-02 SongPlan inválido; S-03 GR-011 PASS no sustentado; S-04 claims no sustentados; S-05 desacoplamiento traza/checklist/material; S-06 procedencia no fiable.
- **Qwen-specific:** 5 — Q-01/Q-02 AP y cobertura de traza; Q-03 serialización; Q-04 claims; Q-05 salida idéntica pese al presupuesto.
- **Ministral-specific:** 5 — M-01 `NOT_APPLICABLE` incorrecto; M-02 filtros AP no autorizados; M-03 razones N3-P excesivas; M-04 serialización; M-05 procedencia/claims.
- **Primary failure classes:** C/D/F/G, con B como factor probable y H en procedencia de salida.
- **AP ambiguity:** NO conceptual; carga de ejecución y validación insuficiente.
- **Creative-generation boundary:** NO ambigua; incumplida en la aplicación.
- **Completion-checklist problem:** MIXTO, modelo + contrato/adaptador.
- **Guardrail problem:** MIXTO, modelo + ausencia de comprobación de evidencia.
- **SongPlan failure Qwen:** MIXTO, serialización y handoff armónico incompleto.
- **SongPlan failure Ministral:** MIXTO, serialización inválida y handoff armónico incompleto.
- **Could deterministic adapter remove failures:** SÍ, los fallos de formato, referencias, estados y evidencia; NO, las decisiones creativas o voicings faltantes.
- **Safe adapter responsibilities:** validación estructural/semántica referencial, guardrails basados en evidencia, procedencia y derivación de READY.
- **One-pass burden:** probable, no demostrado como causa única.
- **Canonical/genre gaps:** ninguno nuevo; la base existente delimita conocimiento y claims.
- **v1.2 justified:** sí, como cambio de ejecución y validación, no como rediseño semántico.
- **One bounded recommendation:** introducir una compuerta determinista y dos etapas (decisiones/traza → SongPlan) antes de volver a ejecutar XMODEL.
