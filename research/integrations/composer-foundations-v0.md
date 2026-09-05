# Composer Foundations v0

## Estado y alcance

Esta es una integracion conceptual entre Melody Foundations, Harmony Foundations,
Melody+Harmony Foundations y la sintesis auditada de Form Foundations. No es
manual, regla, genero, experimento, motor musical ni conocimiento aprobado.

No se modifican las integraciones de origen ni candidatos existentes. No se
abre `RQ-HAR-007`. La cobertura declarada es:

- `CAND-MEL-001`--`036`.
- `CAND-HAR-001`--`052`.
- `CAND-FORM-001`--`008`.

Los estados se heredan; esta integracion no realiza una nueva auditoria.

## Primary question

Puede el corpus actual sostener un flujo de razonamiento compositivo desde una
intencion artistica/formal local hasta material inicial, decisiones melodicas y
armonicas, realizacion, timing y revision, y en que decisiones falla todavia el
ranking justificado?

## Metodo de integracion

Se conserva la separacion:

`STRUCTURE -> PERCEPTION -> COMPOSITION`

Tambien se separan:

- `ARTISTIC GOAL`: lo que el compositor quiere.
- `FORMAL GOAL`: el rol que un tramo debe cumplir.
- `STRUCTURAL MEANS`: operaciones disponibles.
- `PERCEPTUAL EFFECT`: lo que el oyente puede experimentar.

Ninguna de estas capas determina automaticamente la siguiente.

## Core composer architecture

La arquitectura mas defendible es:

```text
ARTISTIC INTENT
    -> FORMAL GOAL / ROLE / SCALE
    -> INITIAL MATERIAL CONSTRUCTION
    -> DECLARED INVARIANTS
    -> MELODIC OPERATIONS
    -> HARMONIC SELECTION
    -> HARMONIC REALIZATION
    -> TIMING / ARRIVAL / BOUNDARY
    -> REVISION / CONTINUATION / RETURN
```

Estado de los enlaces:

| Enlace | Estado | Limite |
|---|---|---|
| artistic intent -> formal goal | PROVISIONAL | el objetivo artistico no queda formalizado por defecto |
| formal goal -> initial material constraints | PROVISIONAL | Form aporta objetivo, no contenido determinado |
| initial material -> declared invariants | SUPPORTED WITH SCOPE | la representacion y la invariante pueden declararse |
| invariants -> melodic operations | SUPPORTED WITH SCOPE | operaciones enumerables y filtrables, sin ranking general |
| melody -> harmonic selection | SUPPORTED WITH SCOPE | una melodia fija subdetermina la armonia |
| harmonic selection -> realization | SUPPORTED WITH SCOPE | bajo, voicing y registro dejan varias realizaciones |
| formal goal -> timing/arrival/boundary | CROSS_DOMAIN_REQUIRED | metro, armonia, arreglo y escucha siguen siendo necesarios |
| local decisions -> song-level coherence | PROVISIONAL | no hay composicion automatica de funciones locales |
| revision from conflict | SUPPORTED WITH SCOPE | falta criterio general de mejora |

## What Form added

Antes de Form, muchos objetivos eran locales o estaban implicitos. Despues de
Form puede declararse:

- rol formal;
- escala `LOCAL`, `SECTIONAL` o `SONG-LEVEL`;
- estado buscado: establish, continue, prepare, arrive, remain open, contrast,
  return/recurrence.

La ganancia es real pero acotada:

- Form mejora **GOAL INFORMATION**.
- Form mejora **ENUMERATE** y **FILTER** con alcance.
- Form no aporta una operacion obligatoria.
- Form no aporta una funcion de ranking general.
- `FORM-003` continuation y `FORM-006` contrast permanecen `NOT_READY`.

## Formal roles as goal information

| Rol | Operaciones con apoyo directo acotado | Asociaciones o hipotesis | Filter | Rank |
|---|---|---|---|---|
| establish/presentation | repeticion o respuesta dentro de marcos clasicos; material ya construido | reconocimiento perceptivo, dosis y transferencia pop | IMPROVES | DOES NOT IMPROVE |
| continue | fragmentacion/liquidacion/aceleracion en sentence clasica | conservar invariante mientras cambia otra dimension | UNCERTAIN fuera del marco | DOES NOT IMPROVE |
| prepare/transition | haces de groove, fraseo, textura, timbre, armonia y ritmo en pop/rock | urgencia, tension o inevitabilidad | IMPROVES WITH SCOPE | DOES NOT IMPROVE |
| arrive | estados de llegada y procesos dependientes del marco | reforzamiento perceptivo de una llegada | IMPROVES negativamente | DOES NOT IMPROVE |
| remain open | persistencia, elision, loop o centro no concluyente en contextos delimitados | apertura percibida desde un medio aislado | IMPROVES WITH SCOPE | DOES NOT IMPROVE |
| contrast | diferencias analiticas entre varios parametros | contraste percibido o nueva seccion | UNCERTAIN | DOES NOT IMPROVE |
| return/recurrence | reaparicion de material o posicion en repertorios delimitados | preferencia entre retorno exacto y cambiado | IMPROVES WITH SCOPE | DOES NOT IMPROVE |

### Goal information versus means-end information

`FORMAL ROLE -> GOAL INFORMATION` es el resultado mas fuerte.

`FORMAL ROLE -> OPERATION` es solo directo en marcos limitados o una asociacion
de repertorio. No se debe leer:

- continuation = fragmentation + faster harmony;
- preparation = harmonic acceleration;
- contrast = register shift;
- arrival = tonic reinforcement;
- return = exact repetition;
- section differentiation = texture change.

La mayoria de esas relaciones son `PROVISIONAL`, `GENRE_SPECIFIC` o
`CROSS_DOMAIN_REQUIRED`, no reglas generales.

## Smallest composer decision record

La unidad conceptual minima que ahora parece justificable es:

```text
ARTISTIC INTENT:
FORMAL SCALE: LOCAL | SECTIONAL | SONG-LEVEL
FORMAL ROLE:
CURRENT MATERIAL:
INVARIANTS:
CURRENT CENTER/COLLECTION:
AVAILABLE OPERATIONS:
MELODY DECISION:
HARMONY SELECTION:
HARMONY REALIZATION:
TIMING:
ARRIVAL/BOUNDARY STATE:
TRADEOFFS:
UNRESOLVED RANKING:
CROSS-DOMAIN DEPENDENCIES:
```

Esto es un registro de razonamiento no ejecutable, no un schema ni una
implementacion.

## Local, sectional and song-level reasoning

No se adopta una jerarquia universal. Una misma operacion puede tener roles
distintos:

- llegada local dentro de una seccion que continua;
- repeticion melodica dentro de una seccion que contrasta globalmente;
- retorno armonico sin retorno completo de la cancion;
- recurrencia de loop con diferenciacion seccional por otros dominios.

La escala debe declararse antes de usar la funcion como filtro.

## From-zero pipeline

| Etapa | Enumerate | Filter | Rank | Bloqueador exacto |
|---|---|---|---|---|
| 1. elegir representacion de semilla | IMPROVES | IMPROVES | DOES NOT IMPROVE | no existe jerarquia entre pitch, ritmo, contorno, registro y relaciones |
| 2. generar semillas | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE | MEL-035/036 siguen diferidos; no hay estrategia positiva suficiente desde cero |
| 3. filtrar semillas | IMPROVES | IMPROVES | DOES NOT IMPROVE | se filtra por restricciones e invariantes, no por valor artistico |
| 4. seleccionar una semilla | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE | primer punto mayor de seleccion justificada; el objetivo no determina el candidato |
| 5. presentar/establecer | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE | establecimiento estructural no equivale a reconocimiento |
| 6. repetir/variar/continuar | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE | FORM-003 no listo; funcion y efecto perceptivo no estan comparados |
| 7. seleccionar apoyo armonico | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE | melodias fijas admiten varias lecturas y metas |
| 8. realizar armonia | IMPROVES | IMPROVES | DOES NOT IMPROVE | multiples bajos, voicings y registros admisibles; preferencia no general |
| 9. coordinar timing | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE | metro, tempo, arreglo y prosodia faltan |
| 10. coordinar llegada/frontera | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE | llegada, boundary, cadencia y cierre no convergen automaticamente |
| 11. decidir continuation/return/contrast | IMPROVES | UNCERTAIN | DOES NOT IMPROVE | FORM-003/006, percepcion y escala song-level bloquean |
| 12. revisar | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE | falta criterio comparativo de mejora |

Form no desplaza el primer fallo: la primera seleccion justificada sigue
fallando en la etapa 4.

## Formal-role ranking test

| Decision | Form provides goal | Form filters options | Form ranks options |
|---|---|---|---|
| opening material intended to return | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE |
| repetition vs variation | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE |
| changed ending: continuation vs arrival | IMPROVES | UNCERTAIN | DOES NOT IMPROVE |
| harmonic persistence vs change | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE |
| directed vs cyclic harmony | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE |
| arrival vs openness | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE |
| register change for contrast | IMPROVES | UNCERTAIN | DOES NOT IMPROVE |
| silence for boundary/arrival | IMPROVES | UNCERTAIN | DOES NOT IMPROVE |
| exact, varied or reharmonized return | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE |
| timing of melody/harmony change | IMPROVES | IMPROVES WITH SCOPE | DOES NOT IMPROVE |

## Main positive composer capabilities

El corpus actual puede:

- declarar intencion y rol formal sin confundirlos;
- enumerar semillas, invariantes, operaciones melodicas y realizaciones;
- filtrar por rango, coleccion, invariante, compatibilidad y estados formales;
- mantener multiples opciones cuando no existe ranking justificado;
- separar seleccion armonica de realizacion armonica;
- diagnosticar divergencias entre llegada melodica, armonica y cierre;
- tratar repeticion, variacion, retorno y loop como operaciones distintas;
- revisar conflictos entre dominios de manera trazable.

## Main manipulable-but-unranked decisions

Siguen manipulables, pero sin ranking general:

- eleccion de la semilla;
- pitches exactos y ritmo inicial;
- repeticion frente a variacion;
- final cambiado;
- continuation fuera de la sentence clasica;
- seleccion de progresion inicial;
- persistencia frente a cambio armonico;
- voicing, bajo y registro;
- timing de cambios;
- llegada, apertura y cierre;
- contraste seccional;
- retorno exacto, variado o reharmonizado;
- diferenciacion formal en loops.

## Compositional tradeoffs

| Tradeoff | Estado | Limite |
|---|---|---|
| identity vs contrast | PROVISIONAL | Form declara la tension; no ordena el compromiso |
| local closure vs global continuation | SUPPORTED WITH SCOPE | los estados pueden divergir por escala |
| exact repetition vs return variation | PROVISIONAL | no hay preferencia general |
| harmonic persistence vs section differentiation | GENRE_SPECIFIC / CROSS_DOMAIN_REQUIRED | otros dominios pueden cambiar la seccion |
| motivic invariance vs formal development | PROVISIONAL | conservar una relacion no demuestra desarrollo |
| melodic continuity vs arrival emphasis | CROSS_DOMAIN_REQUIRED | armonia, metro y posicion formal pesan |
| voicing continuity vs register/section contrast | CROSS_DOMAIN_REQUIRED | bajo, spacing, timbre y arreglo intervienen |
| loop continuity vs formal boundary | GENRE_SPECIFIC / PROVISIONAL | boundary no equivale a cadencia o cierre |

## Diagnostic versus generative power

| Area | Diagnostic power | Generative power | Razon |
|---|---|---|---|
| initial construction | HIGH | MEDIUM | se explicitan variables e invariantes, pero no se elige la semilla |
| melodic development | HIGH | LOW-MEDIUM | operaciones disponibles; MEL-035/036 y percepcion limitan |
| harmonic selection | HIGH | LOW-MEDIUM | filtros estructurales; progresion preferida no resuelta |
| harmonic realization | HIGH | LOW-MEDIUM | realizaciones enumerables; ranking de voicing ausente |
| formal goal selection | MEDIUM | LOW | el objetivo artistico sigue siendo humano y underspecified |
| continuation | MEDIUM | LOW | Caplin es acotado; FORM-003 not ready |
| arrival | HIGH | LOW | estados separables; cierre perceptivo no determinado |
| contrast | MEDIUM | LOW | FORM-006 not ready; haz de parametros no causal |
| return | HIGH | LOW-MEDIUM | recurrencia manipulable; funcion y preferencia abiertas |
| section differentiation | MEDIUM | LOW-MEDIUM | loops y pop aportan opciones; arreglo y percepcion faltan |

## Means-end debt map

| Goal X | Operation Y | Intended effect Z | Estado |
|---|---|---|---|
| establish | repetition/response | disponibilidad o reconocimiento | PROVISIONAL |
| continue | fragmentation/liquidation | continuation | NOT_READY fuera del marco clasico |
| continue | changed ending | parentesco con avance | PROVISIONAL |
| prepare | groove/register/timbre/harmonic change | orientacion hacia llegada | GENRE_SPECIFIC / PROVISIONAL |
| contrast | register shift | contraste percibido | NOT_READY |
| contrast | texture change | nueva seccion o diferencia | CROSS_DOMAIN_REQUIRED |
| arrive | harmonic reinforcement | llegada o cierre | PROVISIONAL; arrival != closure |
| remain open | persistent harmony/loop | apertura | GENRE_SPECIFIC / PROVISIONAL |
| return | exact repetition | regreso reconocible | PROVISIONAL |
| return | changed/reharmonized return | recurrencia con novedad | PROVISIONAL |
| section differentiation | texture/timbre change | funcion seccional percibida | CROSS_DOMAIN_REQUIRED |
| boundary | silence/stop | frontera o cierre | CROSS_DOMAIN_REQUIRED |

## What blocks ranking now?

- **A. Formal goal underspecified:** la intencion artistica no siempre se
  traduce a una funcion y escala concretas.
- **B. Means-end evidence missing:** muchas relaciones son asociaciones de
  repertorio, no comparaciones de medios.
- **C. Perceptual effect unmeasured:** continuidad, contraste, retorno y cierre
  no tienen medidas conjuntas suficientes.
- **D. Genre/style required:** pre-coro, loop, retorno y contraste cambian por
  estilo.
- **E. Arrangement/production required:** textura, timbre, capas y mezcla pueden
  portar la funcion.
- **F. Rhythm/meter required:** timing, acento, densidad y posición métrica
  siguen sin ranking.
- **G. Lyrics/prosody required:** el texto puede cambiar la función melódica y
  temporal.
- **H. Multiple goals conflict:** identidad, contraste, apertura, llegada y
  flexibilidad armonica pueden competir.
- **I. Artistic preference:** incluso con restricciones satisfechas puede no
  existir un ganador objetivo.

No todo bloqueo es un gap perceptivo: algunos son falta de objetivo, dependencia
de dominio, conflicto de metas o preferencia artistica.

## Candidate coverage

| Corpus | Cobertura | Excepciones preservadas |
|---|---|---|
| Melody | `CAND-MEL-001`--`036` | MEL-018 `REJECTED`; MEL-035/036 `DEFERRED / NOT AUDITABLE` |
| Harmony | `CAND-HAR-001`--`052` | HAR-002/005/019 `NOT_READY`; no se abre HAR-007 |
| Form | `CAND-FORM-001`--`008` | FORM-003/006 `NOT_READY`; no se crea FORM-009 |

La cobertura no equivale a aprobacion epistemologica.

## Composer manual readiness

**YES, provisionalmente.** Form fortalece el flujo porque añade rol y escala,
mejora el filtro y hace visibles los bloqueos. La integracion sigue incompleta y
requiere revision futura; no autoriza editar `manual/`.

## Rule readiness

**NO.** Las restricciones estructurales y los estados declarados pueden servir
para validacion futura, pero no constituyen reglas de composicion ni ranking de
calidad.

## Highest-leverage next research comparison

| Opcion | Bloqueadores atendidos | Leverage | Riesgo | Evaluacion |
|---|---:|---|---|---|
| A. FORM-002/deeper means-end | 2 | medio | seguir en vocabulario formal sin decision comparativa | no primera |
| B. RHYTHM/METER | 3 | alto local | reducir ritmo a energia/groove | segunda |
| C. ARRANGEMENT/PRODUCTION | 3 | alto seccional | depender de realizacion y mezcla | posterior |
| D. INITIAL HARMONIC PROGRESSION FROM ZERO | 2 | alto y transversal | no resuelve la primera seleccion de semilla | **mejor siguiente comparacion** |
| E. RQ-HAR-007 Modulation | 1 | medio | leverage episodico y scope separado | no primera |
| F. precise GOAL-MEANS ranking | muchos en abstracto | incierto | pregunta vaga sobre “mejor” | no valida todavia |
| G. genre specialization | varios | medio | prematura sin bases generales | posterior |
| H. Lyrics/Prosody | 2 | condicionado | solo alto si la voz/texto es central | posterior |

## Recommended next research step

Investigar **INITIAL HARMONIC PROGRESSION FROM ZERO**, con una pregunta
estrecha sobre como un objetivo formal y un centro/coleccion pueden enumerar y
filtrar progresiones iniciales, sin asumir que puedan rankearse universalmente.

No comenzar automaticamente esta investigacion.

