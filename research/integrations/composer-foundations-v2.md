# Composer Foundations v2

## Estado y alcance

Esta es una integracion conceptual de Composer Foundations v1 con los
hallazgos auditados de `RQ-RHY-001`. No es manual, regla, genero,
experimento, motor musical ni conocimiento aprobado.

Esta version no modifica `composer-foundations-v0.md` ni
`composer-foundations-v1.md`. La cobertura actual es:

- `CAND-MEL-001`--`036`;
- `CAND-HAR-001`--`059`;
- `CAND-FORM-001`--`008`;
- `CAND-RHY-001`--`009`.

Los estados se heredan y no se cambian en esta integracion.

## Checkpoint de Fase 1

La pregunta de checkpoint es si el proyecto ha extraido suficiente estructura
general para que el cuello de botella principal ya no sea la ausencia de
variables, sino la falta de conocimiento comparativo `GOAL -> MEANS -> EFFECT`.

Conclusión:

**GENERAL STRUCTURAL FOUNDATIONS - PHASE 1: PROVISIONALLY COMPLETE = YES**

Este cierre es de gestion de fase, no una promocion epistemica. Significa que
ya existe una base suficientemente amplia para dejar de abrir dominios
estructurales generales por defecto. No significa que Rhythm, Harmony, Form o
Melody esten completos ni que existan reglas universales.

## Criterio de cierre provisional

La fase cumple provisionalmente porque el proyecto puede:

1. generar candidatos melodicos, armonicos y temporales;
2. representar variables y niveles de decision distintos;
3. expresar objetivos locales y formales;
4. filtrar incompatibilidades estructurales con alcance;
5. coordinar Melody, Harmony y timing sin imponer un orden universal;
6. conservar incertidumbre y distinguir filtro de ranking;
7. localizar la primera eleccion no justificada entre alternativas validas.

El problema dominante ya no es que falte toda una variable basica. Es que
varias alternativas estructuralmente validas quedan sin evidencia para
preferir una sobre otra.

## Arquitectura actual del compositor

```text
ARTISTIC INTENT
        |
FORMAL ROLE / SCALE
        |
INITIAL MATERIAL STRATEGY
       / \\
MELODIC SEED   HARMONIC SEED
       \ /
CROSS-FILTERING
        |
MELODY <-> HARMONY COORDINATION
        |
HARMONIC REALIZATION
        |
RHYTHMIC / METRIC PLACEMENT
        |
ARRIVAL / BOUNDARY / FORMAL CONTEXT
        |
REVISION / RECURRENCE / RETURN
        |
ARTISTIC COMMITMENT
```

No es una secuencia estrictamente lineal. El compositor puede volver a seeds,
restricciones, timing o realizacion cuando una decision posterior revele un
conflicto. `MELODY-FIRST != HARMONY-FIRST != CO-DEVELOPMENT`.

| Relacion | Estado | Limite |
|---|---|---|
| artistic intent -> formal role | PROVISIONAL | el objetivo artistico requiere interpretacion |
| formal role -> initial material | SUPPORTED WITH SCOPE | informa metas y filtros, no medios unicos |
| seed -> represented variables | SUPPORTED WITH SCOPE | algunas representaciones siguen sin criterio de eleccion |
| melodic seed -> harmonic candidates | SUPPORTED WITH SCOPE | subdetermina, no determina |
| harmonic seed -> melodic candidates | SUPPORTED WITH SCOPE | restringe, no determina |
| metric context -> placement alternatives | SUPPORTED WITH SCOPE | no determina prominencia ni funcion |
| Melody/Harmony timing coordination | CROSS_DOMAIN_REQUIRED | no hay sincronizacion preferida |
| selection -> realization | SUPPORTED WITH SCOPE | varias realizaciones siguen disponibles |
| timing -> arrival/boundary | CROSS_DOMAIN_REQUIRED | no hay cue suficiente aislado |
| local operations -> song-level coherence | PROVISIONAL | la agregacion global sigue abierta |
| surviving options -> artistic commitment | ARTISTIC PREFERENCE / BLOCKED GENERALMENTE | falta comparacion medio-efecto |

## v1 -> v2 delta

Rhythm/Meter añade una capa estructural explícita:

- onset, duration, IOI y density se distinguen como variables manipulables;
- metric position puede filtrar colocaciones bajo un marco declarado;
- syncopation y anticipation quedan como relaciones temporales distintas y
  acotadas a repertorios populares inspeccionados;
- Melody y Harmony tienen coordenadas temporales separables;
- la sincronizacion no se convierte en requisito;
- `FILTER` mejora con contexto metrico y temporal;
- `RANK` no mejora generalmente;
- `HAR-057` permanece bloqueado;
- `FORM-003` y `FORM-006` permanecen bloqueados;
- el fallo persistente despues de añadir Rhythm fortalece la hipotesis de que
  el cuello de botella principal es comparativo, no solo estructural.

## Melody capability

| Capability | Estado |
|---|---|
| `CAN ENUMERATE` | YES |
| `CAN FILTER` | YES WITH SCOPE |
| `CAN RANK` | NO GENERAL METHOD |

Melody puede construir seeds, declarar invariantes, enumerar repeticion,
variacion, registro, rango, ritmo y contorno, y filtrar por restricciones.
La seleccion entre alternativas compatibles sigue sin criterio general.

## Harmony capability

| Capability | Estado |
|---|---|
| `CAN ENUMERATE` | YES |
| `CAN FILTER` | YES WITH SCOPE |
| `CAN RANK` | NO GENERAL METHOD |

Harmony puede iniciar desde organizacion dirigida, ciclica, persistente o
material condicionado por centro/coleccion. La seleccion permanece separada de
realizacion. `HAR-057` sigue `NOT_READY`.

## Form capability

| Capability | Estado |
|---|---|
| `GOAL INFORMATION` | IMPROVES |
| `FILTER` | IMPROVES WITH SCOPE |
| `MEANS-END` | UNCERTAIN |
| `RANK` | NO GENERAL METHOD |

Form puede declarar escala y rol. No entrega una realizacion obligatoria ni
una preferencia general entre operaciones.

## Rhythm/Meter capability

| Capability | Estado |
|---|---|
| `CAN ENUMERATE` | IMPROVES |
| `CAN FILTER` | IMPROVES WITH SCOPE |
| `MEANS-END` | UNCERTAIN |
| `CAN RANK` | NO GENERAL METHOD |

Los hallazgos positivos auditados son solamente:

- `RHY-001`: variables temporales separables para construccion y filtrado;
- `RHY-002`: posicion metrica como contexto de colocacion;
- `RHY-005`: desplazamiento/anticipacion con alcance popular;
- `RHY-006`: coordinacion temporal Melody-Harmony.

`RHY-003/004/007/008/009` no se convierten en capacidades positivas.

## Composer decision funnel

```text
GENERATE
   -> FILTER STRUCTURALLY
   -> FILTER BY FORMAL ROLE
   -> FILTER BY METRIC/TEMPORAL CONTEXT
   -> FILTER CROSS-DOMAIN
   -> FILTER REALIZATION CONSTRAINTS
   -> SURVIVING OPTIONS
   -> RANK?
   -> ARTISTIC COMMITMENT
```

| Stage | Estado epistemico | Enumerate | Filter | Rank |
|---|---|---|---|---|
| generate | SUPPORTED WITH SCOPE | YES | — | — |
| structural filter | SUPPORTED WITH SCOPE | YES | YES WITH SCOPE | NO GENERAL |
| formal-role filter | SUPPORTED WITH SCOPE | YES | YES WITH SCOPE | NO GENERAL |
| metric/temporal filter | SUPPORTED WITH SCOPE | YES | YES WITH SCOPE | NO GENERAL |
| cross-domain filter | CROSS_DOMAIN_REQUIRED | YES | YES WITH SCOPE | NO GENERAL |
| realization filter | SUPPORTED WITH SCOPE | YES | YES WITH SCOPE | NO GENERAL |
| survivors -> rank | BLOCKED GENERALMENTE | YES | PARTIAL | NO GENERAL |
| artistic commitment | ARTISTIC PREFERENCE | — | — | Project Owner |

## Four ranking frontiers

El timing merece una frontera propia. Algunas decisiones de timing pertenecen
a realizacion, pero otras ocurren antes, afectan la seleccion y coordinan
capas. Colapsarlas en realizacion ocultaria la deuda de timing.

| Frontier | Question | Estado |
|---|---|---|
| within-domain material ranking | seed melodico A vs B; seed armonico A vs B | NO GENERAL METHOD |
| cross-domain pair ranking | par Melody-Harmony A vs B | NO GENERAL METHOD |
| temporal-placement ranking | onset, duration, metric placement, sync vs anticipation | NO GENERAL METHOD |
| realization ranking | bass, inversion, voicing, register, revoicing | NO GENERAL METHOD |

Estas fronteras pueden compartir criterios, pero no deben tratarse como una
sola deuda. Un filtro temporal puede eliminar pares sin rankearlos. Una
realizacion puede ser compatible sin ser preferible.

## Ranking definition

`CAN RANK` significa:

> Dado un objetivo G, un alcance S, candidatos A y B y un criterio C, la
> evidencia disponible permite preferir A sobre B respecto de C.

El soporte debe conservar su base: teorica, pedagogica, corpus, repertorio,
perceptiva/empirica, genre-specific o artistic preference. No equivale a
superioridad artistica universal.

## FILTER vs RANK matrix

| Decision | Enumerate | Filter | Rank | Why rank remains blocked |
|---|---|---|---|---|
| choose melodic seed | YES | YES WITH SCOPE | NO GENERAL | identity, novelty, goal and style conflict |
| choose harmonic seed | YES | YES WITH SCOPE | NO GENERAL | organization and center do not choose quality |
| choose Melody/Harmony pair | YES | CROSS-DOMAIN | NO GENERAL | compatibility is not preference |
| choose exact pitch | YES | YES WITH SCOPE | NO GENERAL | harmony, register, contour and goal interact |
| choose rhythm | YES | YES WITH SCOPE | NO GENERAL | no general goal-effect comparison |
| choose metric placement | YES | YES WITH SCOPE | NO GENERAL | metric expectation is not importance |
| choose chord-change position | YES | YES WITH SCOPE | NO GENERAL | persistence, phrase and meter permit alternatives |
| choose sync vs anticipation | YES | GENRE-SCOPED | NO GENERAL | popular observation is not universal preference |
| choose bass | YES | YES WITH SCOPE | NO GENERAL | root, bass, center and realization diverge |
| choose inversion | YES | YES WITH SCOPE | NO GENERAL | framework and sonority criteria vary |
| choose voicing | YES | YES WITH SCOPE | NO GENERAL | instrument and perceptual criteria unresolved |
| choose continuation operation | YES | PARTIAL | NO GENERAL | common-practice association is bounded |
| choose contrast operation | YES | UNCERTAIN | NO GENERAL | `FORM-006 NOT_READY` |
| choose arrival configuration | YES | PARTIAL | NO GENERAL | no temporal cue is sufficient |
| choose return variant | YES | YES WITH SCOPE | NO GENERAL | exact, changed and reharmonized goals differ |

## What counts as means-end knowledge?

Means-end knowledge is an evidence-backed relation:

```text
GOAL -> MEANS -> EFFECT / CRITERION
```

Hay que separar:

| Level | Statement | Value for ranking |
|---|---|---|
| A. Structural compatibility | el medio es posible | permite enumerar o filtrar |
| B. Analytical association | el medio aparece asociado a una funcion | informa el contexto, no prescribe |
| C. Composition heuristic | el medio puede usarse hacia un objetivo | orienta, pero puede no comparar |
| D. Comparative evidence | A sirve mejor que B para C bajo S | mejora directamente `CAN RANK` |

El proyecto tiene bastante A, algo de B y C bajo alcance, y muy poco D. No
toda decision necesita D; una preferencia artistica puede ser valida sin
pretender ser conocimiento general. Pero D es lo que falta para convertir
muchos supervivientes en una eleccion justificada.

## Means-end debt map

| Area | Goal -> means question | Estado |
|---|---|---|
| initial Melody | goal -> seed property | PROVISIONAL / FILTER WITH SCOPE |
| initial Harmony | goal -> seed organization | SUPPORTED WITH SCOPE / no rank |
| Form | formal role -> local operation | PROVISIONAL / MEANS-END UNCERTAIN |
| Rhythm | formal role -> temporal operation | NOT_READY as positive mapping |
| Melody-Harmony | goal -> pair selection | CROSS_DOMAIN_REQUIRED |
| realization | goal -> bass/inversion/voicing | CROSS_DOMAIN_REQUIRED |
| continuation | goal -> fragmentation/rate/change | NOT_READY generally; bounded classical association |
| contrast | goal -> changed dimensions | NOT_READY (`FORM-006`) |
| arrival | goal -> cue configuration | NOT_READY as comparative model |
| return | goal -> exact/variant/reharmonized recurrence | PROVISIONAL / no rank |
| loop form | goal -> differentiation method | GENRE-SCOPED / CROSS_DOMAIN_REQUIRED |

## What Rhythm added

Rhythm added structural decomposition that is genuinely useful for filtering:

- onset, duration, IOI and density are no longer interchangeable;
- metric placement becomes an explicit context rather than an implicit label;
- Melody and Harmony timing can be coordinated without forced synchrony;
- popular anticipation and syncopation can be represented with scope;
- timing can be located before realization as well as inside realization.

## What Rhythm failed to unlock

Rhythm did not create validated means-end mappings for:

- rests as segmentation or closure;
- rhythmic invariants as perceived identity;
- formal role to temporal operation;
- temporal continuation outside bounded classical theory;
- multi-cue temporal arrival/boundary models.

This failure is informative: adding variables did not produce comparative
knowledge.

### HAR-057

**MORE CONTEXT + STILL BLOCKED.**

Rhythm distinguishes number of harmonic events, duration, harmonic rhythm,
change rate and persistence. It does not provide criteria for selecting among
them. The blocker is mainly missing means-end evidence and cross-domain context,
not a missing variable name.

### FORM-003

**MORE CONTEXT + STILL BLOCKED.**

Rhythm clarifies which temporal operations may appear in a bounded classical
continuation analysis. It does not establish continuation as a general
perceptual or compositional function. The blockers are tradition dependence,
means-end evidence and an unmeasured perceptual construct.

### FORM-006

**MORE CONTEXT + STILL BLOCKED.**

Rhythmic change is now visible as one possible contrast dimension, but no
evidence shows that it produces perceived sectional contrast or ranks better
than changes in harmony, register, texture or arrangement. The blockers are
cross-domain dependence, genre dependence and missing perceptual/comparative
criteria.

## Phase-transition test

| Question | Result |
|---|---|
| Can we generate candidate material? | YES WITH SCOPE |
| Can we represent relevant variables? | YES WITH SCOPE |
| Can we express local/formal goals? | YES WITH SCOPE |
| Can we filter structural incompatibilities? | YES WITH SCOPE |
| Can we coordinate domains? | YES WITH SCOPE / CROSS_DOMAIN_REQUIRED |
| Can we preserve uncertainty? | YES |
| Are major decisions blocked because a variable is literally missing? | SOME CONTEXT-DEPENDENT CASES, not dominant |
| Are major decisions blocked because several valid alternatives remain? | YES, predominantly |

La diagnosis es **MOSTLY COMPARATIVE**. El proyecto todavía tiene huecos
estructurales locales —especialmente arreglo/texture, prosodia y modulation—,
pero la mayoría de decisiones centrales ya pueden expresarse y filtrarse. La
falla repetida es elegir entre opciones que sobreviven.

## General structural-domain inventory

| Domain | ¿Bloquea muchas decisiones por falta de estructura? | Diagnosis |
|---|---|---|
| arrangement/orchestration/texture | No de forma general; aparece en realizacion, contraste y pop | principalmente means-end/genre layer |
| lyrics/prosody | Puede bloquear canciones con texto | cross-domain/context-dependent, no requisito instrumental general |
| tension | No falta una variable basica unica; falta modelo comparativo | riesgo de vague quality research |
| hooks | Hook, prominence y memorability siguen separados | goal-specific/genre-specific means-end |
| broader development | variables disponibles; relaciones de efecto insuficientes | means-end debt |
| song-level architecture | escala y roles existen, agregacion global incompleta | later integration, no primer structural gap |
| genre | puede cambiar rankings y medios | specialization layer, no base general faltante |
| `RQ-HAR-007` modulation | solo decisiones que requieren nuevo centro | boundary/narrow dependency, no dominant blocker |

### Texture / Arrangement check

Arrangement/production cruza contraste, secciones, sonoridad y loops. Sin
embargo, el compositor ya puede representar esas variables como restricciones y
marcarlas `CROSS_DOMAIN_REQUIRED`. El hueco actual es principalmente saber qué
medio produce qué efecto bajo un estilo y objetivo, no la ausencia de toda
representacion estructural. No se abre ahora como siguiente objetivo.

### Lyrics / Prosody check

Prosody puede determinar onset, duracion, stress y frase en musica cantada.
No impide un workflow general instrumental; debe entrar como restriccion
opcional y dependencia cross-domain cuando exista texto.

### Tension check

Abrir ahora Tension Foundations probablemente mezclaria energia, expectativa,
disonancia, sorpresa y cierre en un modelo vago. No hay base para un escalar
unico ni para mejorar `RANK` con una investigacion amplia.

### Hook check

Hook no es prominence ni memorability. La pregunta es de objetivo especifico y
probablemente genre-sensitive, no una variable estructural previa necesaria
para el workflow general.

### Modulation check

`RQ-HAR-007` sigue siendo la frontera para nuevos centros establecidos. Algunas
decisiones la requieren, pero no bloquea la mayoria de construcciones iniciales,
filtrado o coordinacion actuales. No se prioriza automaticamente.

## Composer manual readiness

**YES - FIRST-FOUNDATIONS MANUAL READY, provisionally.**

Existe un workflow coherente para enseñar:

- especificar objetivos y alcance;
- generar candidatos;
- representar variables separadas;
- filtrar estructuralmente;
- filtrar por forma, metro y cross-domain constraints;
- separar seleccion y realizacion;
- declarar incertidumbre;
- detenerse cuando el ranking no este justificado.

Esto no significa que el manual este completo ni autoriza modificar `manual/`.

## Composer rule readiness

**NO.**

Debe distinguirse entre:

- **structural validators:** comprueban restricciones observables;
- **generative heuristics:** proponen alternativas bajo contexto;
- **comparative rules:** prefieren A sobre B con evidencia.

La investigacion actual no justifica convertir los dos ultimos grupos en reglas
generales. No se modifica `rules/`.

## Candidate coverage

| Domain | Coverage and preserved states |
|---|---|
| Melody | `CAND-MEL-001`--`036`; `MEL-018 REJECTED`; `MEL-035/036 DEFERRED / NOT AUDITABLE` |
| Harmony | `CAND-HAR-001`--`059`; `HAR-002/005/019/054/057 NOT_READY` |
| Form | `CAND-FORM-001`--`008`; `FORM-003/006 NOT_READY` |
| Rhythm | `CAND-RHY-001`--`009`; `RHY-001/002/005/006 POSSIBLE_WITH_SCOPE`; `RHY-003/004/007/008/009 NOT_READY` |

## Next-target comparison

| Option | Blocked decisions unlocked | FILTER -> RANK potential | Leverage | Main risk |
|---|---|---|---|---|
| precise arrival means-end question | arrival, silence, duration, timing, Form/Melody/Harmony interface | high if criterion is narrow | high cross-domain | overclaiming closure |
| Arrangement/Texture Foundations | realization, contrast, loop differentiation | medium | high | mostly genre/production effects |
| Lyrics/Prosody Foundations | sung onset, stress, phrase and form | medium-high for songs | conditional | not general instrumental |
| broad Tension | many stated goals | unknown | broad | vague scalar quality model |
| Hooks/memorability | hook decisions | high only for specific tasks | medium | conflating constructs |
| `RQ-HAR-007` modulation | new-center decisions | narrow | medium | not dominant current blocker |
| FORM-002 | continuation/contrast | medium | medium | overlaps existing debts |
| another Rhythm RQ | timing details | low-medium | medium | structural accumulation before comparison |
| genre specialization | style-specific ranking | high in one genre | variable | premature specialization |

## Recommended next research target

La siguiente pregunta debe ser una investigacion precisa de medios y efectos:

> **Para una llegada melodica local, breve y no equivalente a cierre total, en
> una frase tonal/modal con metro declarado, aporta el alargamiento del evento
> final seguido de silencio una ventaja frente a duracion no alargada sin
> silencio respecto del criterio de juicio de llegada local, manteniendo
> armonia, posicion metrica, registro y arreglo dentro de un alcance declarado?**

Decision: duracion/silencio final.

Goal: llegada local sin afirmar cierre total.

Alternatives: alargamiento + silencio versus duracion no alargada + ausencia de
silencio, con otras variables controladas.

Criterion: juicio declarado de llegada local, separado de closure, tension y
memorability.

Scope: frases tonales/modalmente relacionadas, metro declarado y tarea
perceptiva/compositiva especifica; no universalizar a todos los generos.

Evidence needed: comparar fuentes perceptivas y compositivas directamente
relevantes, conservar diferencias entre deteccion de frontera y juicio de
llegada, y buscar contraejemplos donde la llegada no use alargamiento o
silencio.

No se inicia esta investigacion en este documento ni se diseña experimento.
`EXP-002` permanece pausado.
