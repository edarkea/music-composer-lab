# RQ-CROSS-005 - Menor vs mayor movimiento con armonia fija

## Estado

- `id: RQ-CROSS-005`
- `status: SYNTHESIZED`
- `phase: Phase 2`
- `frontier: REALIZATION RANKING`
- `mode: COMPARISON-FIRST`
- `criterion: PERCEIVED MUSICAL DISTANCE BETWEEN SUCCESSIVE SONORITIES`
- `candidate_audit_status: COMPLETED`
- `candidate_audit_evidence_gate: PASS`
- `next_unused_candidate_id: CAND-CROSS-006`
- `experiment_gate: JUSTIFIED`

## Decision precisa

`GOAL`: reducir perceived musical distance entre sonoridades sucesivas.

`CONTEXT`: misma seleccion armonica declarada; mismo numero de voces,
afinacion, timbre, timing y loudness cuando proceda; registro y spacing
declarados; melodia fija solo si la evidencia permite ese control.

`A`: realizacion con menor movimiento analitico.

`B`: realizacion con mayor movimiento analitico.

`CRITERION`: juicio directo de perceived musical distance.

La pregunta no es sobre broad continuity, preference, smoothness, roughness,
consonance o expectancy.

## Resultado de auditoria

`CAND-CROSS-005: REVISE / POSSIBLE_WITH_SCOPE`

Tipo final: `COMPARATIVE_DECISION_CONSTRAINT`.

Claim revisado: en la evidencia inspeccionada, los estudios que relacionan
voice leading con distance o procesamiento armonico no aislan adecuadamente
realizaciones lower-motion frente a higher-motion de la MISMA seleccion
armonica con perceived distance como medida dependiente. No justifican aun un
ranking de realizaciones. Esta ausencia acotada no implica que el efecto no
exista.

El resultado es accionable: impide escoger lower-motion por defecto a partir de
literatura que estudia chord-pair distance, similarity, expectancy,
discrimination o evaluacion de sonoridades.

## Evidencia por fuente

| Source | Seleccion armonica | Realizacion | Metrica / tarea | Resultado | Source classification | Directness |
|---|---|---|---|---|---|---|
| SRC-EMPIRICAL-029 | Parcial; cambian estructuras de trichord y relaciones | motion, voces moviles, direccion, tonos comunes y tuning | suma de desplazamientos; rating directo de distance | mas movimiento suele aumentar distance, con interacciones | `HARMONY + REALIZATION CONFOUNDED` | `PARTIAL` |
| SRC-EMPIRICAL-031 | No como realizacion; cambian pares de triadas | modelos standard y minimal | p-norm; similarity + fit promediados como triadic distance | compara modelos, no voicings A/B | `NOT A REALIZATION COMPARISON` | `INDIRECT` |
| SRC-EMPIRICAL-033 | No; se reemplaza un acorde | salida algoritmica de cuatro voces | suma de semitonos; discriminacion de secuencias | voice leading contribuye al procesamiento; cambia la armonia | `HARMONY + REALIZATION CONFOUNDED` | `INDIRECT` |
| SRC-EMPIRICAL-034 | Parcial dentro de set-class | voicing, span, transposicion y consonancia no independientes | acorde divergente y adjetivos; no distance secuencial directa | voicing puede afectar evaluacion, sin ranking objetivo | `PARTIALLY ISOLATED` | `INDIRECT` |

## Controles y limitaciones

| Factor | Estado en la evidencia | Consecuencia |
|---|---|---|
| harmonic identity / root relation / quality | varied or partial | no aislamiento limpio de seleccion |
| root vs bass / inversion | restringido en algunas fuentes, no factor independiente | posible confound de bajo e inversion |
| voice count / assignment | varied, real o matematicamente optimizada | total motion no representa necesariamente streaming |
| common-tone retention | varia en Rogers; no aislada del movimiento | puede ser factor de realizacion separado |
| aggregate vs maximum motion | metricas no equivalentes; distribucion no aislada | no se sabe si importa el total o un salto individual |
| register / spacing / span / crossing | reducidos, variados o embebidos en voicing | no atribuir efectos solo a motion |
| melody / soprano | ausente o no privilegiada | transferencia a cancion con melodia fija limitada |
| timing / timbre / loudness | controlados dentro de cada estudio | no garantizan transferencia entre texturas |

No se crea una metrica oficial. Se mantienen separados sum of displacements,
p-norm, minimum motion, maximum displacement, number of moving voices y
optimized assignment.

## Distinciones epistemicas

- `analytical motion != perceived distance` automaticamente.
- `similarity != distance` automaticamente. Milne/Holland construye una medida
  especifica combinando similarity y fit; eso no crea equivalencia general.
- `expectancy / discrimination != perceived distance`.
- Propiedad estatica de sonoridad no es juicio secuencial de transicion.
- `total motion != distribution of motion`.
- `mathematical voice assignment != perceived voice correspondence`.
- No se agrega una flecha hacia continuity, preference o quality.

## Source to composition transfer

`SOURCE`: tareas de distancia, evaluacion o procesamiento de pares/secuencias
armonicas bajo el alcance de cada estudio.

`TARGET`: escoger entre realizaciones de material armonico fijo cuando
perceived distance es el criterio activo.

Transferencia: `PARTIAL` o `INDIRECT`, nunca suficiente para ranking A/B. La
transferencia a popular song permanece `UNKNOWN TRANSFER` por melodia, arreglo,
timbre, bajo, registro y contexto temporal.

## Blocker classification

- `COMPARATIVE-EVIDENCE BLOCKER`
- `CONFOUND / IDENTIFICATION BLOCKER`
- `GENRE TRANSFER BLOCKER` para transferencia a cancion popular

No es un `TARGET-CONSTRUCT BLOCKER`: perceived distance conserva una
operacionalizacion acotada.

## Capacidades y frontera

- `CAN ENUMERATE REALIZATIONS`: `YES WITH SCOPE`
- `CAN FILTER STRUCTURALLY`: `YES WITH SCOPE`
- `CAN FILTER EVIDENCE`: `YES`
- `CAN RANK LOWER vs HIGHER MOTION ON PERCEIVED DISTANCE`: `NO`
- `CAN RANK REALIZATIONS GENERALLY`: `NO`
- `CAN RANK FOR BROAD CONTINUITY`: `NO`
- `REALIZATION RANKING FOR PERCEIVED DISTANCE`: `NO POSITIVE RANK YET`

## Experiment eligibility

`experiment_gate: JUSTIFIED` para consideracion.

La justificacion es:

- target construct estable con alcance;
- decision A/B precisa;
- manipulacion posible en un par armonico declarado;
- confounds identificables y potencialmente controlables o declarables;
- gap comparativo preciso;
- resultado relevante para una eleccion real de realizacion.

`JUSTIFIED` no significa required ni autoriza disenar o ejecutar el
experimento. La siguiente decision debe comparar el valor informativo de una
nueva busqueda bibliografica muy directa frente a un experimento propio. En
esta RQ no se disena ninguno y `EXP-002` permanece `PAUSED`.

## Diversification and split

`DIVERSIFY: YES`. CROSS-005 no repite CROSS-004: CROSS-004 separa perceived
distance de broad continuity; CROSS-005 prueba si el criterio estrecho permite
discriminar realizaciones.

`split_required: NO`. La restriccion de gap y la accion negativa pertenecen al
mismo claim. No se crea `CAND-CROSS-006`.

## Ready for Composer Foundations integration

`NO`.

## Recommended next action

Solicitar al Project Owner y al Music/Methodology Director una decision sobre
autorizar una investigacion experimental acotada del gap identificado; no
disenarla ni ejecutarla automaticamente.
