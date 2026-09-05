# Composer Foundations v5

## Estado y alcance

Integración conceptual de `Composer Foundations v4` con `RQ-CROSS-003` y
`CAND-CROSS-003`. No es manual, regla, género, experimento ni conocimiento
aprobado. Se preservan v0, v1, v2, v3 y v4. No se modifican RQs, candidatos,
fuentes ni documentos anteriores.

## Estado de fases

**GENERAL STRUCTURAL FOUNDATIONS - PHASE 1: PROVISIONALLY COMPLETE = YES**

**PHASE 2: ACTIVE.** El cuello de botella sigue siendo `MOSTLY COMPARATIVE`,
pero ya existe un ranking local condicionado por criterio.

Estados Cross-domain preservados:

| Candidate | Outcome | Readiness | Type |
|---|---|---|---|
| `CAND-CROSS-001` | `REVISE` | `POSSIBLE_WITH_SCOPE` | `COMPARATIVE_DECISION_CONSTRAINT` |
| `CAND-CROSS-002` | `REVISE` | `POSSIBLE_WITH_SCOPE` | `CONSTRUCT_TRANSFER_CONSTRAINT` |
| `CAND-CROSS-003` | `REVISE` | `POSSIBLE_WITH_SCOPE` | `COMPARATIVE_DECISION_KNOWLEDGE` |

Next unused Cross-domain candidate: `CAND-CROSS-004`.

## First audited positive rank with scope

`CAND-CROSS-003` es el primer caso auditado de `COMPARATIVE_DECISION_KNOWLEDGE`.

| Element | Resultado acotado |
|---|---|
| **GOAL** | Preservar reconocimiento de material melódico |
| **CONTEXT** | Tarea de reconocimiento, representación y exposición/familiaridad declaradas |
| **A** | Material intacto, o contorno + relaciones interválicas relativas preservados en la comparación específica |
| **B** | Distorsión específica que preserva solo contorno, o la alternativa concreta del diseño |
| **CRITERION** | Reconocimiento/discriminación |
| **EVIDENCE** | Comparación empírica directa |
| **RESULT** | `A > B WITH SCOPE` |
| **LIMIT** | Solo sobre `recognition` bajo el contexto experimental correspondiente |

El resultado no dice que el retorno exacto sea mejor que la variación en
general, ni que una condición intacta de laboratorio sea un retorno exacto
compositivo. El resultado separado de Massaro sobre melodías nuevas, contorno
y *tone chroma* no se fusiona con el de melodías familiares.

## Arquitectura `CAN RANK`

### A. General / universal ranking

¿Puede el proyecto escoger la opción musical generalmente mejor? **NO.**

### B. Goal-conditioned local ranking

Dado un objetivo, criterio y alcance precisos, ¿puede la evidencia preferir A
sobre B? **SOMETIMES YES.** `CAND-CROSS-003` demuestra un caso.

### C. Multi-objective composition ranking

¿Puede combinar identidad, novedad, contraste, continuación y estilo en un
ranking total justificado? **NO GENERAL METHOD.**

```text
RANK ON CRITERION C != GLOBAL COMPOSITION RANK
```

Más reconocimiento no significa mejor composición. La intención artística
puede elegir menor reconocimiento por novedad, contraste, transformación,
sorpresa, estilo o preferencia.

La intención artística tiene ahora dos roles: seleccionar el criterio activo
y resolver tradeoffs entre criterios. La evidencia puede ordenar respecto del
primero; la preferencia artística decide su importancia relativa.

## Tres niveles de ranking

Este es un marco del proyecto, no una taxonomía científica universal.

- **Level 0 - NO RANK:** varias opciones sobreviven sin evidencia comparativa.
- **Level 1 - RANK ON ONE CRITERION:** `A > B` sobre `C` bajo `S`; `CROSS-003` alcanza este nivel.
- **Level 2 - MULTI-CRITERION TRADEOFF:** las opciones difieren en identidad, novedad, contraste, estilo, etc.; no hay método general.

## Funnel actualizado

```text
COMPOSITIONAL INTENT
  ↓ DECLARE GOAL
  ↓ DECLARE TARGET CONSTRUCT
  ↓ OPERATIONALIZATION CHECK
  ↓ GENERATE OPTIONS
  ↓ MUSICAL-OPTION FILTERING
  ↓ EVIDENCE FILTERING
  ↓ SOURCE→TARGET TRANSFER CHECK
  ↓ DECLARE COMPARISON CRITERION
  ↓ COMPARATIVE EVIDENCE
  ↓ RANK ON CRITERION IF JUSTIFIED
  ↓ CHECK OTHER ACTIVE CRITERIA
  ↓ TRADEOFF / ARTISTIC COMMITMENT
```

Es un marco de razonamiento, no una ejecución determinista.

## Progresión de Phase 2

| Candidate | Goal / alternatives / criterion | What it enables | What it blocks | Rank |
|---|---|---|---|---|
| `CROSS-001` | Medios de llegada local; criterio no suficientemente validado | Filtrar inferencias comparativas | Phrase-boundary no rankea automáticamente medios de local arrival | No |
| `CROSS-002` | Local arrival frente a boundary/completion/closure | Filtrar transferencias de constructo | No sustituir silenciosamente el constructo objetivo | No |
| `CROSS-003` | Variantes melódicas bajo recognition | Comparar una A y B concretas | No convertir recognition en calidad, formal return o preferencia global | Sí, Level 1 |

`CROSS-001` es una restricción comparativa; `CROSS-002`, una restricción de
transferencia; `CROSS-003`, conocimiento comparativo positivo.

## Comparison-first y transferencia

`RQ-CROSS-003`: **COMPARISON-FIRST = YES, PARTIALLY**. Recognition ofrece
tareas más utilizables, transformaciones controlables, alternativas
comparables y evidencia discriminante. Persisten `recognition != formal
return`, melodía aislada `!=` forma de canción y melodía familiar `!=` motivo
recién establecido automáticamente.

```text
SOURCE: laboratory recognition / memory of transformed melodies
TARGET: choose a transformation when recognition is active
TRANSFER: PARTIAL
```

La heurística es válida solo cuando tarea, representación, exposición,
alternativas y objetivo se alinean. No hay transferencia directa a retorno
formal.

## Impactos Phase 1

### MEL-032

Añade evidencia comparativa a la separabilidad de pitch, intervalos, contorno,
ritmo y registro:

```text
representation separability != perceptual ranking
```

### MEL-034

Añade posibles consecuencias de recognition a relaciones preservables:

```text
transformability != recognition != quality
```

### FORM-007

Se mantiene:

```text
recurrence != formal return != exact repetition
```

Recognition puede ser un criterio dentro de un contexto formal; no convierte
el resultado en ley de retorno.

## Fronteras actuales de ranking

| Frontier | Estado |
|---|---|
| Within-domain material ranking | **AT LEAST ONE POSITIVE SCOPED RANK** |
| Cross-domain pair ranking | **NO POSITIVE RANK YET** |
| Temporal-placement ranking | **NO POSITIVE RANK YET** |
| Realization ranking | **NO POSITIVE RANK YET** |

Dentro del dominio melódico: `specific transformation ranking = YES WITH
SCOPE`; ranking general de semillas y estrategias de retorno = `NO`.
Ritmo, registro, final cambiado, ornamentación, armonía y escala formal siguen
sin ranking positivo.

## Ranking-readiness matrix

| Decision | Criterion | State | Unresolved |
|---|---|---|---|
| Exact vs specified varied return | recognition | **FIRST POSITIVE SCOPED COMPARATIVE RESULT** | escala formal y transferencia |
| Exact vs varied generally | identidad + múltiples metas | No general rank | heterogeneidad y tradeoffs |
| Rhythm/pitch variant | recognition/similarity | No positive rank | criterio y confounds |
| Changed ending | recurrence/continuation | No positive rank | evidencia directa |
| Register change | identity/contrast | No positive rank | efecto aislado |
| Melody-Harmony pair | compatibility/fit | No positive rank | constructo `fit` |
| Onset placement | grouping/expectancy | No positive rank | género y metro |
| Voicing/voice-leading | continuity/roughness | No positive rank | criterio y comparación integrada |
| Local arrival | arrival | No positive rank | constructo no operacionalizado |

## Single criterion y deuda multiobjetivo

La evidencia puede mostrar:

```text
Variant A > Variant B on recognition
```

No muestra `A > B overall`. Deuda actual: identity/novelty,
identity/contrast, identity/continuation, identity/style, voice-leading
continuity/register contrast y closure/continuation. No se crean fórmulas de
preferencia.

## Readiness

### Composer manual

**YES, provisionally.** La arquitectura futura puede organizarse como:

1. construir el espacio de decisión;
2. filtrar opciones;
3. declarar el criterio activo;
4. rankear cuando exista evidencia;
5. resolver tradeoffs y compromiso artístico;
6. reconocer cuándo la evidencia no aplica.

No se modifica `manual/`.

### Rules

**NO.** El resultado acotado no es una regla general. Una formalización futura
requeriría meta, representación, criterio equivalente, comparación específica
y alcance compatible.

## Estado y siguiente frontera

Phase 2 debe continuar. **DIVERSIFY**, no profundizar inmediatamente la misma
frontera: ya existe un resultado positivo en recognition melódico y conviene
probar si el método funciona fuera de ella.

La frontera de mayor leverage actual es **REALIZATION RANKING**. v4 ya la
identifica como relevante y potencialmente operacionalizable mediante
continuidad, connectedness o roughness, aunque no existe aún un resultado
comparativo integrado.

### Recommended next Phase-2 RQ

- **GOAL:** elegir entre realizaciones de la misma identidad armónica.
- **CONTEXT:** misma armonía y melodía, dos alternativas controladas de voicing/voice-leading, con registro e instrumentación declarados.
- **OPTIONS:** realización A frente a realización B, cambiando variables especificadas.
- **CRITERION:** un único constructo definido, por ejemplo continuity, connectedness o roughness; no tratarlos como sinónimos.
- **OPERATIONAL READINESS:** prometedora pero no lista; requiere construct-first research.
- **SOURCE→TARGET RISK:** juicios de laboratorio sobre roughness/connectedness pueden no transferir directamente a una textura compositiva completa.
- **EXPECTED RANKING FRONTIER:** realization ranking.
- **EXPECTED CAPABILITY GAIN:** obtener un segundo ranking acotado fuera de recognition melódico o una nueva construct-transfer constraint.

El par Melody-Harmony sigue siendo importante, pero `fit/compatibility` está
menos preparado operacionalmente y no debe elegirse solo por importancia
teórica.

## Experiment policy

`RQ-CROSS-003` permanece `NOT JUSTIFIED`; `EXP-002` permanece `PAUSED`. No se
propone experimento por la mera existencia de variantes no resueltas.

## Recommended next action

Investigar primero el constructo de realization ranking; no iniciar
automáticamente esa RQ, un experimento, una edición del manual ni una regla.
