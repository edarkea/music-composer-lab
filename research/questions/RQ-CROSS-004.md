# RQ-CROSS-004 - Constructo para continuidad entre realizaciones armonicas

## Estado

- `id: RQ-CROSS-004`
- `status: SYNTHESIZED`
- `phase: Phase 2`
- `frontier: REALIZATION RANKING`
- `mode: CONSTRUCT-FIRST`
- `scope: transiciones sucesivas entre sonoridades realizadas con contexto armonico declarado`
- `candidate_audit_status: COMPLETED`
- `candidate_audit_evidence_gate: PASS`
- `next_unused_candidate_id: CAND-CROSS-005`
- `experiment_gate: NOT JUSTIFIED`

## Pregunta y decision objetivo

La pregunta era que constructo podria servir para comparar realizaciones
alternativas cuando la meta compositiva es continuidad entre sonoridades
sucesivas. La decision futura mantiene declarado el contexto armonico y,
cuando proceda, el contexto melodico, y varia bajo, inversion, registro,
spacing, asignacion de voces, retencion de tonos comunes y movimiento
individual.

## Hallazgo central

Ninguna fuente inspeccionada mide simultaneamente perceived distance y
continuity, define continuity mediante distance ni valida que menor distance
implique mayor continuidad compositiva. Por tanto:

`perceived distance -> continuity: NOT ESTABLISHED`

Perceived musical distance entre sonoridades sucesivas es, no obstante, un
objetivo perceptivo mas estrecho y operacionalizable con alcance limitado.
Declarar ese objetivo no equivale a operacionalizar continuity.

Rogers y Callender presentan pares sucesivos de trichords sinteticos y piden
ratings de distance. En sus paradigmas, el movimiento total y la retencion de
tonos comunes se relacionan con esos ratings, pero la taxicab distance no
funciona como metrica lineal suficiente: importan tambien direccion, numero de
voces, afinacion y tamano del desplazamiento. El estudio no compara
realizaciones alternativas de la misma seleccion armonica en textura completa.

Wall et al. miden expectativa y procesamiento mediante priming y tiempos de
reaccion en secuencias polifonicas occidentales; no miden continuity,
smoothness o connectedness. Milne y Holland comparan modelos contra juicios de
triadic distance; esto permite estudiar distance, no continuity ni un ranking
compositivo. Eerola y Lahdelma estudian acordes aislados: registro, roughness y
sharpness son una cautela sobre la sonoridad estatica, no sobre una transicion.

## Matriz de transferencia

| Fuente | Objetivo declarado | Resultado de transferencia |
|---|---|---|
| Voice-leading distance analitica | Perceived distance | `PARTIAL`, con alcance de la tarea |
| Common-tone retention | Perceived distance | `PARTIAL`, en el paradigma de trichords |
| Perceived distance | Continuity | `NOT ESTABLISHED` |
| Voice-leading distance | Continuity | `NOT ESTABLISHED` |
| Common-tone retention | Continuity | `NOT ESTABLISHED` |
| Smoothness | Continuity | `NOT ESTABLISHED`; no hay tarea homogenea establecida |
| Roughness | Continuity | `NOT ESTABLISHED`; evidencia inspeccionada estatica |
| Similarity | Continuity | `NOT ESTABLISHED`; similarity es objetivo alternativo |
| Voice-stream continuity | Continuidad armonica global | `NOT ESTABLISHED`; seguimiento local sin puente validado |
| Expectancy / processing fluency | Continuity | `NOT ESTABLISHED` |
| Preference | Continuity | `INVALID FOR CURRENT PURPOSE`; responde a otra pregunta |

`PARTIAL` solo sobrevive cuando existe correspondencia observada entre el
constructo fuente y perceived distance dentro del alcance de una tarea. No se
usa por proximidad conceptual, vocabulario compartido o plausibilidad teorica.

## Correcciones de alcance

- Propiedad estatica de sonoridad no es propiedad secuencial de transicion.
- Common-tone retention no equivale a continuidad ni a mejor voicing.
- Root no es bass; inversion, registro, spacing, bajo y pitch-class deben
  registrarse por separado.
- Una metrica analitica puede correlacionarse con un juicio sin ser el
  constructo perceptivo; no se afirma que los oyentes perciban taxicab distance.
- Los resultados dependen de registro, afinacion, numero de voces, asignacion,
  timbre, armonia, timing y contexto tonal.
- No se inspecciono un paradigma con top-line melodica fija y realizaciones
  alternativas comparables.

## Resultado de la auditoria de CAND-CROSS-004

- `audit_outcome: REVISE`
- `promotion_readiness: POSSIBLE_WITH_SCOPE`
- `phase2_candidate_type: CONSTRUCT_TRANSFER_CONSTRAINT`
- `split_required: NO`

El candidato contiene una sola restriccion coherente: no transferir
automaticamente constructos adyacentes a continuity y declarar, si se desea,
perceived distance como criterio alternativo. No rankea A frente a B y por eso
no es `COMPARATIVE_DECISION_KNOWLEDGE`.

## Capacidades separadas

| Capacidad | Resultado |
|---|---|
| Enumerar opciones de realizacion | `YES` |
| Filtrar opciones musicales | `PARTIAL`, por variables y contexto declarados |
| Filtrar evidencia | `YES` |
| Filtrar transferencias invalidas | `YES` |
| Operacionalizar continuity amplia | `NO` |
| Operacionalizar perceived distance | `YES WITH SCOPE` |
| Rankear realizaciones para continuity | `NO` |
| Rankear realizaciones para perceived distance | `NO` todavia; criterio listo, comparacion no realizada |

## Frontera y experimento

`REALIZATION RANKING FOR BROAD CONTINUITY: CONSTRUCT-FIRST BLOCKED`

`REALIZATION RANKING FOR PERCEIVED DISTANCE: READY FOR COMPARISON-FIRST`

El segundo estado significa que existe un criterio declarado y una familia de
tareas relevante; no significa que la literatura ya rankee voicings ni que
Rogers/Callender haya aislado realizacion con armonia constante.

El gate de experimento permanece `NOT JUSTIFIED`. El siguiente paso apropiado
es formular una RQ comparison-first y revisar la comparacion literaria antes de
diseñar un experimento propio.

## Diversificacion

`DIVERSIFY: YES`. La investigacion abrio una frontera distinta y aclaro un
criterio mas estrecho sin forzar un ranking positivo ni cambiar silenciosamente
el objetivo de continuidad.

## Recommended next step

Formular, sin iniciarla automaticamente, una RQ comparison-first con:

- `GOAL`: reducir o controlar perceived musical distance entre sonoridades sucesivas;
- `CONTEXT`: relacion armonica declarada y registro, timing, timbre, numero de voces y melodica fija cuando proceda;
- `OPTIONS`: realizaciones A/B elegidas despues de revisar la evidencia disponible;
- `CRITERION`: juicio de perceived distance;
- `RISK`: chord-pair distance no equivale a ranking de realizaciones.

No integrar todavia en Composer Foundations.
