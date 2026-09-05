# Composer Foundations v1

## Estado y alcance

Esta es una integracion conceptual de los hallazgos auditados de Melody,
Harmony, Melody+Harmony, Form y `RQ-HAR-010`. No es manual, regla, genero,
experimento, motor musical ni conocimiento aprobado.

Esta version no modifica el snapshot historico
`composer-foundations-v0.md`. La cobertura declarada es:

- `CAND-MEL-001`--`036`.
- `CAND-HAR-001`--`059`.
- `CAND-FORM-001`--`008`.

Se preservan los estados existentes, incluido `MEL-018 = REJECTED`,
`MEL-035/036 = DEFERRED / NOT AUDITABLE`, `HAR-002/005/019/054/057 =
NOT_READY` y `FORM-003/006 = NOT_READY`.

## Pregunta principal

Puede el compositor construir material melodico y armonico inicial desde un
objetivo o contexto declarado, coordinarlos, filtrarlos, realizarlos y
revisarlos sin fingir que existe un ranking general de calidad?

La respuesta actual es parcial:

- ambos dominios pueden enumerar candidatos;
- ambos pueden filtrar con alcance declarado;
- ninguno dispone de un metodo general para elegir el mejor candidato;
- la coordinacion Melody-Harmony añade nuevas restricciones, pero no elimina
  automaticamente la deuda de ranking.

## Arquitectura de compositor

La arquitectura mas defendible es:

```text
ARTISTIC INTENT
        |
FORMAL ROLE + SCALE
        |
INITIAL MATERIAL STRATEGY
       / \\
MELODIC SEED   HARMONIC SEED
       \ /
DECLARED CROSS-CONSTRAINTS
        |
MELODY <-> HARMONIC SELECTION
        |
HARMONIC REALIZATION
        |
TIMING / ARRIVAL / BOUNDARY
        |
REVISION / RECURRENCE / RETURN
```

Es una arquitectura de razonamiento, no un orden obligatorio de composicion.
`MELODY-FIRST != HARMONY-FIRST != CO-DEVELOPMENT`. La evidencia no justifica
que uno de estos modos sea universalmente superior.

| Enlace | Estado | Limite |
|---|---|---|
| artistic intent -> formal role | PROVISIONAL | el objetivo artistico no se formaliza por defecto |
| formal role -> initial melodic constraints | SUPPORTED WITH SCOPE | el rol informa la meta, no fija una melodia |
| formal role -> initial harmonic constraints | SUPPORTED WITH SCOPE | puede filtrar organizacion/material, no determinar una progresion |
| initial seed -> declared invariants | SUPPORTED WITH SCOPE | las invariantes deben declararse y pueden ser parciales |
| melody -> harmonic selection | SUPPORTED WITH SCOPE | una melodia fija subdetermina la armonia |
| harmony -> melodic construction | SUPPORTED WITH SCOPE | una semilla armonica restringe, pero no determina, la melodia |
| melody <-> harmony cross-filter | CROSS_DOMAIN_REQUIRED | elimina incompatibilidades, pero no resuelve preferencia |
| harmonic selection -> realization | SUPPORTED WITH SCOPE | varias realizaciones pueden corresponder al mismo material |
| formal goal -> timing/arrival/boundary | CROSS_DOMAIN_REQUIRED | requiere ritmo, metro, armonia, arreglo y contexto |
| local operations -> song-level coherence | PROVISIONAL | no hay composicion automatica de funciones locales |
| revision after conflict | SUPPORTED WITH SCOPE | falta criterio general de mejora |

## Delta respecto de Composer Foundations v0

`RQ-HAR-010` cambia el punto de partida armonico. Harmony ya no se describe
principalmente como seleccion de una progresion ya dada. Puede construirse un
seed abstracto como:

- relacion dirigida;
- unidad ciclica;
- persistencia o recurrencia;
- material condicionado por centro/coleccion;
- loop, vamp o pedal como ejemplos distintos y acotados;
- relaciones que permanezcan disponibles para operaciones posteriores.

La ganancia es:

- Harmony `CAN ENUMERATE`: mejora materialmente;
- Harmony `CAN FILTER`: mejora con alcance;
- Harmony `CAN RANK`: sigue bloqueado;
- centro y coleccion adquieren una funcion explicita de filtrado constructivo;
- recurrencia o persistencia ya no implican terminalidad;
- Harmony y Melody desde cero quedan aproximadamente simetricos;
- `HAR-054` y `HAR-057` exponen deudas de representacion y timing;
- la aptitud para manipulacion posterior queda separada de calidad y desarrollo.

## Melody-from-zero capability

| Decision | Enumerate | Filter | Rank | Limite |
|---|---|---|---|---|
| seed melodico | YES | YES WITH SCOPE | NO GENERAL METHOD | no existe criterio universal de mejor semilla |
| invariante | YES | YES WITH SCOPE | NO GENERAL METHOD | identidad y novedad pueden entrar en conflicto |
| repeticion/variacion | YES | YES WITH SCOPE | NO GENERAL METHOD | repeticion, retorno y exactitud no son equivalentes |
| continuacion/contraste | YES | PARTIAL | NO GENERAL METHOD | dependencia formal, ritmica y estilistica |
| registro, rango y ritmo | YES | YES WITH SCOPE | NO GENERAL METHOD | el efecto perceptivo no se sigue de una variable aislada |

La construccion melodica puede empezar desde una meta y generar alternativas
filtrables. La primera eleccion entre alternativas compatibles permanece sin
ranking general.

## Harmony-from-zero capability

| Decision | Enumerate | Filter | Rank | Limite |
|---|---|---|---|---|
| organizacion inicial | YES | PARTIAL | NO GENERAL METHOD | dirigida, ciclica y persistente no forman taxonomia exhaustiva |
| centro/coleccion | YES | YES WITH SCOPE | NO GENERAL METHOD | centro no equivale a coleccion ni a acorde tonico |
| relaciones iniciales | YES | YES WITH FRAMEWORK | NO GENERAL METHOD | funcion, etiqueta, raiz y bajo divergen |
| recurrencia/persistencia | YES | GENRE-SCOPED | NO GENERAL METHOD | loop, vamp y pedal no son sinonimos |
| llegada o apertura | YES | PARTIAL | NO GENERAL METHOD | llegada, cadencia y cierre divergen |
| extension/ritmo armonico | YES | PARTIAL | NO GENERAL METHOD | `HAR-057` permanece `NOT_READY` |
| aptitud para operaciones futuras | YES | PARTIAL | NO GENERAL METHOD | `HAR-059` es provisional |

El material inicial armonico no tiene que ser una progresion completamente
realizada. La seleccion abstracta permanece separada de bajo, inversion,
voicing, registro, spacing, duplicacion y asignacion de voces.

## Melody <-> Harmony desde cero

El sistema puede comenzar con:

1. una semilla melodica;
2. una semilla armonica;
3. una restriccion ya dada de cualquiera de los dos dominios;
4. co-desarrollo de ambas semillas.

Una semilla melodica puede filtrar candidatos armonicos. Una semilla armonica
puede filtrar candidatos melodicos. Ninguna determina generalmente a la otra.
`HAR-047` y `HAR-049` apoyan la subdeterminacion de seleccion y realizacion.
Esto no revive `CAND-MEL-036`.

### Diferencia entre tres tipos de ranking

| Frontera | Pregunta | Estado actual |
|---|---|---|
| within-domain ranking | que semilla melodica o armonica elegir | NO GENERAL METHOD |
| cross-domain ranking | que par Melody-Harmony elegir entre supervivientes | NO GENERAL METHOD |
| realization ranking | que bajo, inversion, voicing, registro o timing elegir | NO GENERAL METHOD |

El cross-filter puede eliminar pares incompatibles, pero no convierte los pares
supervivientes en una preferencia ordenada. El ranking de seeds, de pares y de
realizaciones puede tener criterios diferentes y no debe colapsarse en un unico
`CAN RANK`.

## Dual-seed pipeline

Prueba abstracta desde cero:

| Stage | Enumerate | Filter | Rank | Diagnostico |
|---|---|---|---|---|
| 1. generar seeds melodicos | YES | YES WITH SCOPE | NO GENERAL METHOD | primer bloqueo posible dentro de Melody |
| 2. generar seeds armonicos | YES | YES WITH SCOPE | NO GENERAL METHOD | primer bloqueo posible dentro de Harmony |
| 3. cross-filter Melody/Harmony | YES | YES WITH SCOPE | NO GENERAL METHOD | elimina incompatibilidades declaradas |
| 4. elegir un par | YES | PARTIAL | NO GENERAL METHOD | nueva frontera de preferencia entre pares |
| 5. realizar la armonia | YES | YES WITH SCOPE | NO GENERAL METHOD | seleccion y realizacion permanecen separadas |
| 6. coordinar bajo, voces y registro | YES | PARTIAL | NO GENERAL METHOD | dependencias de instrumento y sonoridad |
| 7. coordinar timing | YES | PARTIAL | NO GENERAL METHOD | depende de metro, frase, arreglo y forma |
| 8. coordinar llegada/frontera | YES | PARTIAL | NO GENERAL METHOD | llegada no equivale a cierre |
| 9. revision, recurrencia, variacion y retorno | YES | PARTIAL | NO GENERAL METHOD | exacto, cambiado y rearmonizado no se ordenan generalmente |

### First ranking failure

La primera falla puede ocurrir antes de la interaccion Melody-Harmony: elegir
una semilla entre alternativas compatibles dentro de cualquiera de los dos
dominios. Si ambas listas llegan a sobrevivientes, aparece una segunda falla al
seleccionar el par. La realizacion introduce una tercera frontera de ranking.

El cross-filter mejora la eliminacion estructural, no la eleccion artistica.

## Filtering sources

| Fuente de filtrado | Puede eliminar | No puede demostrar |
|---|---|---|
| Melody | invariantes, rango, registro, transformacion, repeticion o retorno declarado | que una variante sea mejor |
| Harmony | centro, coleccion, organizacion, recurrencia, persistencia, llegada/apertura declarada | que una progresion sea preferible |
| Form | rol y escala local, sectional o song-level | un medio armonico o melodico obligatorio |
| Interaction | compatibilidad de alturas, invariantes, bajo/voicing, timing | que el par superviviente sea el mejor |
| Realization | restricciones de registro, instrumento, voces y sonoridad | una preferencia universal de realizacion |

Filtrar es reducir el espacio por restricciones. No es ordenar los resultados.

## Composer decision funnel

```text
GENERATE
   -> FILTER STRUCTURALLY
   -> FILTER BY FORMAL GOAL
   -> FILTER CROSS-DOMAIN
   -> FILTER REALIZATION CONSTRAINTS
   -> SURVIVORS
   -> RANK?
   -> ARTISTIC COMMITMENT
```

| Arrow | Estado |
|---|---|
| generate -> structural filter | SUPPORTED WITH SCOPE |
| structural filter -> formal-goal filter | SUPPORTED WITH SCOPE |
| formal-goal filter -> cross-domain filter | CROSS_DOMAIN_REQUIRED |
| cross-domain filter -> realization filter | SUPPORTED WITH SCOPE |
| survivors -> rank | BLOCKED GENERALLY; possible only with declared criterion and scope |
| rank -> artistic commitment | ARTISTIC PREFERENCE / PROJECT OWNER |

El funnel es una arquitectura conceptual, no una receta de orden obligatorio.

## Goal information versus means-end information

Form mejora la informacion de meta y el filtrado con alcance. No proporciona
por si sola un medio preferido.

| Goal | Puede ayudar a enumerar/filtrar | No permite concluir |
|---|---|---|
| establish | material que presenta o hace disponible relaciones | que deba comenzar en tónica |
| continue | relaciones que mantienen parentesco o continuidad | que deba haber mas cambios o aceleracion |
| prepare/transition | relaciones orientadas a una meta declarada | que deba aparecer dominante |
| arrive | candidatos con relacion de llegada | que haya cadencia o cierre |
| remain open | persistencia, recurrencia o terminalidad diferida | que un medio produzca apertura percibida |
| contrast | otras organizaciones o dimensiones modificables | que deba cambiar la tonalidad |
| return | reaparicion exacta o transformada | que una opcion sea mejor que otra |

Para Harmony, el objetivo puede filtrar tipos relevantes de material inicial.
`GOAL-CONDITIONED != GOAL-DETERMINED`.

Ejemplo: `remain open` puede permitir enumerar persistencia, recurrencia o
relaciones no terminales. No permite ordenar cual produce mejor apertura
percibida. `return` puede admitir retorno exacto, cambiado o rearmonizado, pero
no los rankea.

## Means-end debt map

| Area | Relation under investigation | Status |
|---|---|---|
| Initial Melody | goal -> seed property | PROVISIONAL / FILTER WITH SCOPE |
| Initial Harmony | goal -> organization or relation | SUPPORTED WITH SCOPE for filtering |
| Melody-Harmony | goal -> pair choice | CROSS_DOMAIN_REQUIRED |
| Realization | goal -> bass/inversion/voicing | CROSS_DOMAIN_REQUIRED |
| Form | goal -> operation | UNCERTAIN / scope-dependent |
| Timing | goal -> onset/duration/change placement | NOT_READY / rhythm-meter dependency |
| Arrival/Closure | goal -> cue configuration | CROSS_DOMAIN_REQUIRED |
| Contrast | goal -> changed dimension(s) | PROVISIONAL; `FORM-006` NOT_READY |
| Return | goal -> exact/variant/reharmonized return | PROVISIONAL; no general ranking |

`HAR-054` no aporta una arquitectura de representacion integrada: solo deja
claro que los niveles de abstraccion y realizacion deben distinguirse.
`HAR-057` no aporta criterios positivos de extension o ritmo armonico desde
cero.

## Ranking blocker taxonomy

Se conservan solo los bloqueadores necesarios:

- **A. GOAL UNDERSPECIFIED:** el objetivo no distingue entre alternativas.
- **B. MEANS-END EVIDENCE MISSING:** no sabemos que medio sirve mejor al fin.
- **C. PERCEPTUAL EFFECT UNMEASURED:** la estructura esta descrita, pero el
  efecto perceptivo no esta comprobado.
- **D. GENRE / STYLE REQUIRED:** loops, vamps, modalidad y realizaciones
  dependen del contexto estilístico.
- **E. RHYTHM / METER REQUIRED:** timing, duracion, cambio y frase requieren
  variables ritmicas aun no integradas.
- **F. ARRANGEMENT / PRODUCTION REQUIRED:** textura, registro y sonoridad
  pueden cambiar la lectura de la misma estructura.
- **H. MULTIPLE GOALS CONFLICT:** continuidad, contraste, llegada y apertura
  pueden exigir operaciones incompatibles.
- **I. ARTISTIC PREFERENCE:** una decision puede ser intencional sin ser una
  conclusion general.
- **J. REPRESENTATION / DECISION LEVEL UNCLEAR:** no esta claro si se elige
  region, relacion, acorde o sonoridad.
- **K. DOMAIN ORDER / CO-DEVELOPMENT UNRESOLVED:** no hay orden universal entre
  Melody-first, Harmony-first y co-desarrollo.

`G. LYRICS / PROSODY` no es necesario para esta integracion, aunque puede
adquirir importancia en decisiones song-level futuras.

## What would count as CAN RANK

`CAN RANK` no significa encontrar la mejor musica universal. Significa:

> Dado un objetivo G y un alcance S, la evidencia permite preferir A sobre B
> usando un criterio C declarado.

El criterio puede ser teorico dentro de un marco, perceptivo/empirico,
corpus-informed con cautela, genre-specific, pedagogico o una preferencia
artistica. Debe conservarse la base de la preferencia y no mezclarse con las
demás.

## Positive Composer Test

| Scenario | Capability |
|---|---|
| Melody-first: goal + center, luego armonizacion | CAN REASON WITH SCOPE; ranking melódico y de pares bloqueado |
| Harmony-first: goal + center, luego melodia | CAN REASON WITH SCOPE; ranking armonico y de pares bloqueado |
| Co-constrained: generar ambos y cruzar filtros | CAN REASON WITH SCOPE; mejora eliminacion, no eleccion |
| Loop song: seed recurrente + hook + rol formal | CAN REASON WITH SCOPE; loop, hook y retorno no se ordenan generalmente |
| Arrival: material local para llegada sin cierre total | CAN REASON WITH SCOPE; puede filtrar, no escoger cue optimo |
| Return: exacto, variado o rearmonizado | PARTIALLY; la distincion es clara, la preferencia depende de objetivo y estilo |

## Diagnostic versus generative power

| Area | Diagnostic | Generative | Explanation |
|---|---|---|---|
| Initial Melody | HIGH | MEDIUM | describe variables y genera candidatos con restricciones |
| Initial Harmony | HIGH | MEDIUM | añade seeds dirigidos, ciclicos y persistentes con alcance |
| Melody-Harmony pairing | MEDIUM | LOW-MEDIUM | puede cruzar compatibilidad, no elegir pares |
| Harmonic realization | HIGH | MEDIUM | enumera realizaciones, pero depende de instrumento y sonoridad |
| Formal goal | HIGH | LOW-MEDIUM | aporta meta y filtro, no medios determinados |
| Timing | MEDIUM | LOW | depende de Rhythm/Meter y de contexto formal |
| Arrival | MEDIUM | LOW | estructura, percepcion y cierre permanecen separados |
| Return | HIGH | LOW-MEDIUM | distingue exacto, cambiado y rearmonizado sin ranking general |
| Contrast | MEDIUM | LOW | `FORM-006` sigue `NOT_READY` |
| Loop-based differentiation | MEDIUM | LOW-MEDIUM | recurrencia y diferencia se pueden describir, no ordenar |

## Manual readiness

**YES, provisionalmente.**

El conocimiento actual puede enseñar a:

- formular decisiones;
- enumerar alternativas;
- filtrar por restricciones declaradas;
- separar selección y realización;
- distinguir estructura, percepción y composición;
- identificar cuándo el ranking no está justificado.

No requiere una funcion universal de ranking para ser util. Esta integracion no
autoriza modificar `manual/`.

## Rule readiness

**NO.**

Las capacidades descritas son conocimiento conceptual con alcance, no reglas
compositivas universales. Tampoco se crean validadores estructurales nuevos.

## Candidate coverage

La integracion hereda, sin modificar, toda la cobertura declarada:

| Domain | Coverage | Explicit exceptions |
|---|---|---|
| Melody | `CAND-MEL-001`--`036` | `MEL-018 REJECTED`; `MEL-035/036 DEFERRED / NOT AUDITABLE` |
| Harmony | `CAND-HAR-001`--`059` | `HAR-002/005/019/054/057 NOT_READY` |
| Form | `CAND-FORM-001`--`008` | `FORM-003/006 NOT_READY` |

Los nuevos hallazgos de Harmony se integran con el siguiente alcance:

- `HAR-053`: objetivo formal/local como filtro de material inicial;
- `HAR-054`: unresolved; no es capacidad positiva;
- `HAR-055`: dirigido, cíclico y persistente como posibilidades no equivalentes;
- `HAR-056`: centro y colección como filtros constructivos distintos;
- `HAR-057`: unresolved; variables temporales distinguidas, sin criterio nuevo;
- `HAR-058`: recurrencia/persistencia sin inferir cadencia, retorno o cierre;
- `HAR-059`: grados de libertad manipulables como hipótesis acotada.

## Highest-leverage next research comparison

| Option | Blockers addressed | Filter -> Rank | Cross-domain leverage | Main risk |
|---|---|---|---|---|
| precise means-end/ranking | potentially many | high if narrowly falsifiable | high | vague quality research |
| Rhythm/Meter Foundations | timing, extent, phrase and change placement | medium-high prerequisite value | very high | becoming a new universal rhythm theory |
| Arrangement/Production | realization, contrast, section identity | medium | high | confounding structure with sound |
| deeper Form continuation/contrast | formal means-end | medium | medium-high | repeating existing Form scope |
| Modulation | center change | narrow | medium | outside current construction bottleneck |
| Genre specialization | style ranking | high within genre | variable | premature specialization |
| Lyrics/Prosody | song-level melody/form | potentially high | high for songs | scope expansion |
| Initial-seed ranking | direct ranking | unknown | high | question remains underspecified |

The comparison favors **Rhythm/Meter Foundations**, narrowly focused on how
onset, meter, duration and harmonic/melodic change placement constrain initial
material and cross-domain filtering. It addresses a recurring blocker, has
prerequisite value for timing and phrase decisions, and is more falsifiable than
asking which initial seed is better in general.

## Structural-domain versus means-end bottleneck

**PARTIALLY.**

The main bottleneck is now missing comparative decision knowledge, not a lack of
basic Melody or Harmony structure. However, Rhythm/Meter remains an unresolved
structural dependency that affects both domains, Form, timing and pair choice.
Adding an arbitrary structural domain would be less valuable than narrow
means-end research; adding Rhythm/Meter first is justified because it supplies a
shared prerequisite for those means-end decisions.

## Recommended next research target

`Rhythm/Meter Foundations`: investigar de forma acotada cómo las restricciones
de onset, metro, duracion y colocacion de cambios afectan la construccion y el
filtrado inicial de Melody y Harmony, sin intentar resolver todavía un ranking
general de calidad.

No se inicia esa investigación en este documento. `EXP-002` permanece pausado.
