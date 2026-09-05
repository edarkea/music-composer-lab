# Rhythmic / Metric Placement as Compositional Decision Context

## Estado

Sintesis de `RQ-RHY-001`. No es manual, regla, genero ni auditoria de
candidatos. El dominio Rhythm permanece en estado candidato.

## Conclusion

La organizacion temporal permite construir y filtrar alternativas de onset,
duracion, IOI, rests, posicion metrica, densidad y cambios Melody/Harmony bajo
restricciones declaradas. La evidencia no aporta un ranking general de estas
alternativas para prominencia, tension, energia, continuacion, cierre o calidad.

El avance principal es estructural y de filtrado: Rhythm/Meter hace visibles
variables que antes aparecian mezcladas como tempo, densidad, ritmo armonico,
acento o forma. El ranking sigue dependiendo de tarea, genero, prosodia,
metro, arreglo, percepcion y preferencia artistica.

## Construction variables

### Onset, duration, IOI and density

Onset indica cuando comienza un evento; duration cuanto permanece; IOI separa
inicios sucesivos; density cuenta o distribuye eventos en una ventana declarada.
Tempo puede cambiar el tiempo real sin cambiar una relacion notada. Ninguna
variable equivale automaticamente a energia, tension o importancia.

La construccion puede enumerar patrones y filtrar por metro, prosodia,
ventana, frase o compatibilidad cross-domain. Las fuentes revisadas no
justifican un ranking general ni umbrales de longitud, densidad o IOI.

### Meter and metric position

El metro puede ofrecer una jerarquia esperada de posiciones y agrupaciones bajo
marcos perceptivos y tradiciones declaradas. Palmer/Krumhansl y London apoyan
que existen representaciones metricas y expectativas acotadas; Müllensiefen et
al. muestran que el acento percibido de melodias pop depende de varios rasgos.

Esto permite filtrar eventos por una relacion metrica deseada o deliberadamente
desplazada. No permite inferir que una posicion fuerte sea siempre importante,
estable o formalmente prominente.

### Syncopation and anticipation

La sincopa debe definirse en relacion con un metro o representacion subyacente.
Temperley y Tan/Lustig/Temperley aportan evidencia de anticipacion y
desplazamiento en repertorios rock/pop delimitados. Witek aporta una curva de
groove para estimulos de bateria funk, no una regla sobre melodias, energia o
continuacion.

La anticipacion puede ser una alternativa estructural y genre-scoped; no es
automaticamente tension, groove, energia o gancho.

### Rest and silence

Un rest puede aparecer dentro de una celula, antes o despues de un onset, cerca
de una llegada, en una frontera o en un loop. Margulis muestra que el contexto
modula como se detecta y caracteriza un silencio; no demuestra que el silencio
produzca frontera o cierre.

El silencio puede filtrar segmentacion o separacion cuando el objetivo lo
declara, pero `REST != BOUNDARY != CLOSURE`.

### Rhythmic identity

Onset pattern, duration pattern, IOI, posicion metrica y pitch pueden
representarse por separado. Esto permite conservar una relacion mientras se
cambia otra, como en un seed melodico con ritmo preservado y alturas nuevas.
Dowling apoya separar dimensiones en tareas de reconocimiento; no demuestra
que conservar ritmo conserve identidad motivica o reconocimiento en general.

### Melody and Harmony timing

Los onsets melodicos y armonicos pueden coincidir, anticiparse o divergir. Es
posible describir:

- melodia anticipa armonia;
- armonia anticipa melodia;
- melodia sostenida sobre armonia cambiante;
- armonia sostenida bajo melodia movil;
- cambio armonico durante un rest melodico;
- revoicing sin cambio de identidad armonica.

Estas relaciones mejoran la enumeracion y el filtrado de pares. No hay base
para imponer sincronizacion, cambios de acorde en tiempos fuertes o una unica
relacion anticipatoria.

### Formal roles and timing

Form aporta objetivo, no un medio obligatorio. Timing puede filtrar opciones
compatibles con un rol, pero no entrega un ranking general.

| Rol | Puede filtrar | No queda justificado |
|---|---|---|
| establish | patrones que presentan o hacen disponible una unidad | onset fuerte como regla universal |
| continue | conservar una relacion y cambiar otra bajo marco delimitado | notas mas rapidas = continuacion |
| prepare | colocaciones orientadas a una meta declarada | anticipacion o aceleracion obligatoria |
| arrive | duracion, onset, silencio y cambio coordinables | nota larga = llegada o cierre |
| remain open | persistencia, rest diferido o seam no terminal | silencio = apertura automatica |
| contrast | cambio de dimension ritmica como una opcion | cambio ritmico = contraste percibido |
| return | repeticion o variacion de una relacion temporal | repeticion ritmica = memorabilidad |

`FORM-003` y `FORM-006` permanecen `NOT_READY`.

### Continuation

Caplin describe en la sentence clasica la relacion entre continuation,
fragmentacion, liquidacion y aceleracion armonica. Schoenberg ofrece pedagogia
de reduccion/condensacion y tratamiento motivico. Estas relaciones son
tradition-specific y no establecen que aumentar el rate melodico o armonico
produzca continuacion, tension, energia o desarrollo en otros estilos.

### Arrival and boundary

Alargamiento, silencio, posicion metrica, reduccion de densidad y timing
armonico pueden formar parte de una configuracion de llegada o frontera. La
evidencia de Kragness/Trainor, Margulis y Sears et al. es de tareas y
repertorios delimitados; no convierte ningun cue en suficiente.

`ARRIVAL != CADENCE != CLOSURE`, y `BOUNDARY != CLOSURE`.

## Operation matrix

| Variable | Composer can manipulate | Structural constraints | Formal relevance | Perceptual evidence | Enumerate | Filter | Rank | Scope |
|---|---|---|---|---|---|---|---|---|
| onset | inicio, anticipacion, retraso, solapamiento | metro, IOI, prosodia, evento previo | frase, entrada, llegada | expectativas metricas; funciones abiertas | YES | YES WITH SCOPE | NO GENERAL | metro/tarea declarados |
| duration | duracion notada/sounding y sustain | onset siguiente, metro, instrumento | continuidad, llegada, borde | alargamiento de limites en tareas acotadas | YES | YES WITH SCOPE | NO GENERAL | tonal/phrase scopes |
| IOI | separacion entre ataques | tempo, ventana, metro | densidad y relacion local | no ranking universal inspeccionado | YES | YES WITH SCOPE | NO GENERAL | unidad declarada |
| rest | ausencia antes/despues/dentro | contexto y duracion | segmentacion, seam, borde | contexto cambia deteccion/juicio | YES | PARTIAL | NO GENERAL | tareas de silencio |
| metric position | fuerte/debil, desplazada, anticipada | meter y subdivision | onset, frase, llegada | jerarquia y acento multidimensional | YES | YES WITH SCOPE | NO GENERAL | tradiciones metricas |
| density | cantidad/distribucion de eventos | ventana, tempo, IOI | trayectoria local | groove global acotado; no energia general | YES | PARTIAL | NO GENERAL | audio/groove scopes |
| melodic change placement | cambio de pitch/rhythm en el tiempo | identidad, metro, frase | continuation/return | efecto dependiente de contexto | YES | YES WITH SCOPE | NO GENERAL | Melody cross-domain |
| harmonic change placement | cambio, persistencia, revoicing | chord identity, meter, phrase | arrival, loop, boundary | no cue unico suficiente | YES | YES WITH SCOPE | NO GENERAL | Harmony cross-domain |
| arrival placement | coordinacion de cues temporales | melody, harmony, form, meter | llegada local | evidence bounded | YES | PARTIAL | NO GENERAL | no cierre total |
| boundary silence | rest, stop, sustain, onset siguiente | frase, arreglo, contexto | boundary/open/closure | no equivalencia automatica | YES | PARTIAL | NO GENERAL | cross-domain |

## Role -> timing matrix

| Formal role | Timing operations considered | Evidence | Filter gained? | Rank gained? | Scope | Main uncertainty |
|---|---|---|---|---|---|---|
| establish | onset/pattern recurrence | theory/corpus bounded | YES WITH SCOPE | NO | local/pattern | recognition not measured |
| continue | fragmentation, density/IOI change, harmonic rate | Caplin only for sentence | PARTIAL | NO | common-practice | transfer to popular music |
| prepare | anticipation, change placement, density trajectory | repertoire/context | PARTIAL | NO | declared goal | means-end missing |
| arrive | lengthening, metric placement, silence, harmonic change | empirical/theory bounded | PARTIAL | NO | local arrival | cues not sufficient |
| remain open | persistence, delayed terminal cue, loop seam | popular/repertoire | PARTIAL | NO | loop/section | openness perception |
| contrast | altered rhythmic dimension | Form analytic | UNCERTAIN | NO | sectional | `FORM-006 NOT_READY` |
| return | exact/changed rhythmic relation | form/melody candidates | YES WITH SCOPE | NO | recurrence/return | recognition vs function |

## Melody/Harmony coordination matrix

| Melody timing | Harmony timing | Structural relationship | What can be inferred | What cannot be inferred |
|---|---|---|---|---|
| simultaneous onset | simultaneous chord change | aligned event | compatibility can be checked | stronger arrival or importance |
| melody anticipates | harmony changes later | anticipatory relation | describable/filterable under meter | tension, groove or forward motion universally |
| harmony anticipates | melody enters later | harmonic support precedes event | timing divergence is available | that melody will sound more stable |
| held melody | changing harmony | melodic duration spans harmonic events | selection/realization can be separated | that harmony creates development |
| moving melody | held harmony | surface motion over persistence | density and support can be distinguished | that persistence is static or dull |
| melody rest | harmonic change | change occurs in silence | can expose harmonic timing | that rest marks boundary or closure |
| same harmony | revoicing event | sonority changes without identity change | realization timing is distinct | that revoicing is harmonic development |

## Ranking-gain test

| Decision | Composer v1 before Rhythm | With Rhythm/Meter context |
|---|---|---|
| initial melodic rhythm | ENUMERATE / FILTER WITH SCOPE / NO GENERAL RANK | same; metric/prosodic filtering becomes more explicit |
| initial harmonic rhythm | ENUMERATE / FILTER WITH SCOPE / NO GENERAL RANK | same; event count and timing remain unresolved |
| exact pitch onset | ENUMERATE / FILTER WITH SCOPE / NO GENERAL RANK | same; metric position adds filter context |
| chord-change position | ENUMERATE / FILTER WITH SCOPE / NO GENERAL RANK | FILTER improves with meter/phrase context; rank blocked |
| rest placement | ENUMERATE / PARTIAL FILTER / NO GENERAL RANK | PARTIAL FILTER improves through context; rank blocked |
| arrival placement | ENUMERATE / PARTIAL FILTER / NO GENERAL RANK | PARTIAL FILTER improves; no cue ranking |
| repetition timing | ENUMERATE / FILTER WITH SCOPE / NO GENERAL RANK | same; onset/duration invariants explicit |
| changed-ending timing | ENUMERATE / PARTIAL FILTER / NO GENERAL RANK | PARTIAL FILTER; no preferred ending timing |
| loop seam | ENUMERATE / GENRE-SCOPED FILTER / NO GENERAL RANK | seam timing describable; no seam=closure or optimality |
| Melody-Harmony divergence | ENUMERATE / CROSS-DOMAIN FILTER / NO GENERAL RANK | cross-filter gains; pair ranking remains blocked |

Rhythm/Meter improves structural information and some filtering. It does not
produce general ranking information.

## Generative capability test

| Scenario | Result |
|---|---|
| A. melodic seed: meter + role + center | CAN REASON WITH SCOPE; attack patterns, durations, rests and positions can be enumerated and filtered |
| B. harmonic seed: meter + role + center | PARTIALLY; change positions and persistence can be enumerated, but `HAR-057` remains unresolved |
| C. melody anticipates harmony | CAN REASON WITH SCOPE; relation is structurally describable, selection depends on meter/prosody/context |
| D. local arrival | CAN REASON WITH SCOPE; duration, silence and metric placement can filter, no cue is sufficient |
| E. continuation | PARTIALLY; positive relation is bounded to common-practice frameworks |
| F. loop seam | CAN REASON WITH SCOPE; recurrence timing can be specified without closure inference |
| G. cross-domain pair | CAN REASON WITH SCOPE; timing may eliminate pairs, not generally rank them |

## Composer Timing Test

| Stage | Enumerate | Filter | Rank | First failure note |
|---|---|---|---|---|
| choose onset representation | YES | YES WITH SCOPE | NO GENERAL | representation/goal choice |
| place melodic attacks | YES | YES WITH SCOPE | NO GENERAL | prosody and metric scope |
| choose durations | YES | YES WITH SCOPE | NO GENERAL | no duration-to-function rule |
| place rests | YES | PARTIAL | NO GENERAL | context-dependent silence |
| place harmonic changes | YES | YES WITH SCOPE | NO GENERAL | meter does not choose rate |
| choose synchronization/divergence | YES | CROSS-DOMAIN | NO GENERAL | pair criteria incomplete |
| place arrival | YES | PARTIAL | NO GENERAL | arrival/cadence/closure distinct |
| place boundary | YES | PARTIAL | NO GENERAL | rest and boundary diverge |
| test recurrence | YES | YES WITH SCOPE | NO GENERAL | repetition not memorability |
| revise | YES | PARTIAL | NO GENERAL | no comparative improvement criterion |

The first ranking failure is still the choice among compatible timing
alternatives, before a universal timing procedure can select one.

## Anti-rules not justified

The evidence does not justify:

- important notes must fall on strong beats;
- chord changes must occur on strong beats;
- phrases must start on beat one or end on a strong beat;
- long notes create arrival or importance;
- rests create boundaries, tension or closure automatically;
- faster notes create continuation;
- faster harmonic rhythm creates momentum;
- syncopation creates groove, tension or energy universally;
- more density creates energy or less density creates calm;
- rhythmic repetition creates memorability;
- melody and harmony should change together;
- loop seams must align with barlines;
- four-bar hypermeter or 4/4 is universal.

## Existing candidate impact

- `HAR-057`: **MORE CONTEXT**, not more readiness. Rhythm clarifies event count,
  duration, change rate and persistence as distinct variables, but does not
  supply new positive construction criteria.
- `FORM-003`: **MORE CONTEXT** only. Continuation has a bounded temporal model
  in common-practice theory; it remains `NOT_READY` generally.
- `FORM-006`: **MORE CONTEXT** only. Rhythmic difference is one possible
  contrast dimension; perceived contrast remains unsupported.
- `CAND-MEL-025/026/028/029/030`: **MORE CONTEXT**, not status changes.

## Composer Foundations impact

### STRUCTURAL INFORMATION

**Improves.** Onset, duration, IOI, density, metric position, rests and change
placement are now separated across event, pattern, metric, phrase, harmonic and
formal levels.

### GOAL INFORMATION

**Limited improvement.** Formal roles can condition which timing alternatives
are relevant, but do not specify a preferred temporal means.

### MEANS-END INFORMATION

**Remains uncertain.** Only bounded relations, such as sentence continuation
and selected arrival tasks, survive; no universal cue bundle is supported.

### FILTERING INFORMATION

**Improves with scope.** Meter, prosody, phrase, center, harmonic identity,
formal role and cross-domain compatibility can eliminate alternatives.

### RANKING INFORMATION

**No general improvement.** No timing variable or combination supports a
general preference for onset, duration, density, syncopation, harmonic change
placement or seam timing.

## Strongest supported findings

1. Temporal variables must be separated before they can inform a decision.
2. Meter can constrain expected positions without determining function or
   prominence.
3. Melody and Harmony onset/change timing are separable and coordinable.
4. Silence is context-sensitive and cannot be equated with boundary or closure.
5. Popular-music anticipations and syncopations are valuable bounded examples,
   not universal timing rules.
6. Rhythm/Meter improves filtering more than ranking.

## Evidence gaps

- No direct general evidence ranks timing alternatives for compositional goals.
- Existing perceptual studies often measure accent, groove, detection or
  completion, not composition or formal function.
- Popular corpus evidence is descriptive and genre-limited.
- Common-practice continuation does not establish transfer to pop, loops or
  other traditions.
- Hypermeter was not promoted to a candidate capability; no universal bar-span
  assumption is adopted.
- Prosody, arrangement and production remain cross-domain dependencies.

## Candidate audit gate

**PASS.** La auditoria se completo sin promocion y sin crear `CAND-RHY-010`.
`CAND-RHY-001`, `002`, `005` y `006` quedan como `POSSIBLE_WITH_SCOPE` tras
revision. `CAND-RHY-003`, `004`, `007`, `008` y `009` quedan `NOT_READY` por
duplicacion, accion principalmente diagnostica o insuficiencia del puente
estructura-percepcion-composicion.

Las correcciones principales son:

- onset/duration/IOI/density se conservan como variables separables, no como
  independencia perceptiva;
- metric position filtra colocacion bajo un marco declarado, no prominencia;
- syncopation y anticipation se mantienen como relaciones distintas y
  popular/genre-scoped;
- timing Melody-Harmony se integra como coordinacion, no sincronizacion
  preferida;
- roles formales no producen recetas temporales;
- continuation temporal queda acotada a la sentence clasica;
- cues de llegada/frontera no forman un modelo multi-cue validado.

`HAR-057` recibe **MORE CONTEXT + STILL BLOCKED**. `FORM-003` y `FORM-006`
reciben **MORE CONTEXT + STILL BLOCKED**. Ningun readiness previo se modifica.

## Audit status

`RQ-RHY-001` queda en `SYNTHESIZED` con `candidate_audit_status:
COMPLETED`. No se modifica Composer Foundations en esta tarea.

## Recommended next step

Audit `CAND-RHY-001`--`009` before updating Composer Foundations.
