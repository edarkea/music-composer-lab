# RQ-CROSS-004 - Constructo para continuidad entre realizaciones armónicas

## Estado

- `id: RQ-CROSS-004`
- `status: SYNTHESIZED`
- `phase: Phase 2`
- `frontier: REALIZATION RANKING`
- `mode: CONSTRUCT-FIRST`
- `scope: transiciones sucesivas entre sonoridades realizadas con contexto armónico declarado`
- `candidate_audit_status: NOT_STARTED`
- `candidate_audit_evidence_gate: PASS`
- `next_unused_candidate_id: CAND-CROSS-005`
- `experiment_gate: NOT JUSTIFIED`

## Pregunta central

Cuando un compositor quiere mantener continuidad entre dos sonoridades
armónicas realizadas, ¿qué constructo medible u operacionalizable podría
servir para comparar realizaciones alternativas sin confundir distancia,
roughness, similarity, expectativa, conectividad o preferencia con
continuidad compositiva?

## Decisión compositiva objetivo

La decisión futura es:

```text
same / declared harmonic context
+ same / declared melodic context where necessary
+ realization A vs realization B
```

Las variables potenciales son bajo, inversión, registro, spacing, asignación
de voces, retención de tonos comunes y movimiento individual. Esta RQ no
determina todavía qué variables deben combinarse ni compara A contra B.

## Distinciones obligatorias

```text
voice-leading distance != perceived continuity
minimum total motion != universal optimum
common-tone retention != connectedness automatically
small semitone motion != smoothness automatically
smoothness != continuity
continuity != similarity
similarity != identity
roughness != dissonance != tension
roughness != voice-leading quality
low roughness != continuity
consonance != stability
bass motion != root motion
chord distance != voice-leading distance necessarily
analytical parsimony != perceptual preference
perceptual preference != compositional quality
static sonority property != sequential transition property
```

## Resultado de investigación

La evidencia permite operacionalizar de forma directa un constructo más
estrecho: **perceived musical distance entre sonoridades sucesivas**.

Rogers y Callender hicieron escuchar pares de trichords en sucesión y
solicitaron ratings de distancia. El total de desplazamiento se relacionó con
mayor distancia percibida y los tonos comunes redujeron la distancia; sin
embargo, los desplazamientos no se combinaron como una métrica lineal única y
los efectos dependieron de dirección, número de voces y afinación.

Esto no demuestra que menor distancia sea mayor continuidad compositiva.
Constituye una medida secuencial relevante y un puente parcial, no una
validación de `voice-leading distance -> perceived continuity`.

Wall et al. encontraron que voice leading y armonía influyen conjuntamente en
la expectativa durante secuencias polifónicas occidentales. La tarea fue de
priming y tiempo de reacción, no de rating de continuidad o smoothness. Aporta
evidencia de procesamiento/expectativa, no una medida directa del objetivo.

Milne y Holland compararon modelos de distancia triádica percibida,
incluyendo voice-leading distance, Tonnetz, distancia espectral y conteo de
tonos comunes. Esto permite comparar modelos de distancia bajo un criterio
declarado, pero no convierte distancia percibida en continuidad.

Eerola y Lahdelma muestran que registro afecta ratings de consonancia mediante
roughness y sharpness. Es evidencia acústico-perceptiva estática sobre una
sonoridad, no evidencia de continuidad entre realizaciones sucesivas.

## Inventario de constructos

| Construct | Definition / level | Task / measure | Static or sequential | Directness | Readiness |
|---|---|---|---|---|---|
| Voice-leading distance | Distancia analítica entre alturas/voices | Métrica y juicio de distancia | Sequential | `PARTIAL` | `READY WITH SCOPED OPERATIONALIZATION` para distance |
| Common-tone retention | Tonos literalmente conservados | Conteo y manipulación | Sequential | `PARTIAL` | `READY WITH SCOPED OPERATIONALIZATION` para distance |
| Parsimony / total motion | Suma de desplazamientos o movimiento mínimo | Modelo y ratings de distancia | Sequential | `PARTIAL` | No metric single optimum |
| Perceived connectedness | Sensación de conexión entre eventos | No tarea estable directa identificada | Sequential | `NOT ESTABLISHED` | `NEEDS MORE CONSTRUCT-FIRST` |
| Smoothness | Término teórico/pedagógico o rating posible | No paradigma homogéneo verificado | Sequential | `NOT ESTABLISHED` | `UNRESOLVED` |
| Voice-stream continuity | Seguimiento de líneas auditivas | Streaming e integración/segregación | Sequential | `PARTIAL` local | `ADJACENT MEASURES ONLY` |
| Roughness | Interacción acústica de parciales | Modelos y ratings de consonancia | Usually static | `NOT ESTABLISHED` | Solo para consonance acotada |
| Similarity | Parecido entre sonoridades | Ratings de similarity/distance | Pairwise | `PARTIAL` | Solo similarity |
| Preference | Agrado o elección | Rating/preference | Either | `UNSUITABLE` | Separar del objetivo |

## Analítico, acústico, perceptivo y compositivo

Voice displacement, common tones, parsimonious movement, voice crossing,
spacing e inversión describen la realización analíticamente. Roughness,
spectral interaction, harmonicity, register y sharpness describen propiedades
acústicas de la señal o sonoridad. Distance ratings, expectancy, streaming,
consonance y similarity son resultados perceptivos dependientes de tarea.

“Hacer que esta transición armónica se sienta continua” es el objetivo
compositivo; la literatura inspeccionada no lo equipara de forma estable con
ningún constructo anterior.

## Parsimony y tonos comunes

La suma de desplazamientos tiene soporte como predictor parcial de juicios de
distancia en pares de trichords. No justifica minimizar siempre el movimiento.
El juicio también responde a tonos comunes, tamaño de movimiento, dirección,
relación entre voces y afinación.

La retención de tonos comunes tiene evidencia directa para reducir distancia
percibida en ese paradigma, pero no demuestra que más tonos comunes produzcan
mejor continuidad global.

## Voice-stream, bajo, inversión, registro y spacing

La proximidad de pitch y otros indicios de auditory scene analysis pueden
favorecer el seguimiento de una línea, pero continuidad de una voz individual
no equivale a continuidad armónica global.

El bajo debe tratarse separadamente: `ROOT != BASS`. No se infiere una
jerarquía universal de root position. Registro y spacing pueden alterar
roughness, consonancia, sharpness, streaming y similitud sin cambiar la
identidad abstracta del acorde; son posibles confounds, no criterios
automáticos de continuidad.

## Roughness, similitud y preferencia

Roughness es más maduro como constructo acústico-perceptivo que continuity,
pero la evidencia inspeccionada se refiere principalmente a consonancia o
estabilidad de una sonoridad. `LOW ROUGHNESS != CONTINUITY`.

Similarity puede ser medible, pero `SIMILARITY != CONTINUITY`. Preference no
es el criterio por defecto: que una realización guste más no identifica qué
aspecto produjo continuidad ni establece calidad compositiva.

## Matrix de transferencia constructo → objetivo

| Source construct | Target: perceived continuity | Result |
|---|---|---|
| Voice-leading distance | Continuidad percibida | `PARTIAL`; validado para distance |
| Common-tone retention | Continuidad percibida | `PARTIAL`; reduce distance en alcance acotado |
| Smoothness | Continuidad percibida | `NOT ESTABLISHED` |
| Roughness | Continuidad percibida | `NOT ESTABLISHED`; medida estática |
| Similarity | Continuidad percibida | `PARTIAL`, no proxy automático |
| Voice-stream continuity | Continuidad armónica global | `PARTIAL`; seguimiento local |
| Expectancy / processing fluency | Continuidad | `PARTIAL`; Wall mide expectativa |
| Preference | Continuidad | `INVALID FOR CURRENT PURPOSE` |

La ausencia de validación no demuestra ausencia de relación; impide la
transferencia automática.

## Repertorio y alcance

- Rogers/Callender: trichords sintéticos en Shepard tones; registro y spacing
  reducidos; alcance específico de distance.
- Milne/Holland: modelos y juicios de distancia triádica.
- Wall et al.: secuencias polifónicas de tradición tonal occidental; priming y
  expectativa.
- Eerola/Lahdelma: acordes aislados en distintos registros; consonance,
  roughness y sharpness.

No hay todavía un puente directo hacia una regla de voicing de popular song.
La transferencia a realización en textura popular es `UNKNOWN TRANSFER`.

## Readiness para comparación futura

El mejor candidato no es `continuity` en sentido amplio, sino **PERCEIVED
MUSICAL DISTANCE BETWEEN SUCCESSIVE SONORITIES**.

Estado: **READY WITH SCOPED OPERATIONALIZATION**.

Una RQ posterior podría comparar realizaciones solo si fija progresión
armónica, timing, timbre, registro relevante, número de voces y melodía cuando
proceda, y usa ratings de distance o una medida de continuity validada. No se
escoge A/B todavía.

La frontera `REALIZATION RANKING` permanece **CONSTRUCT-FIRST BLOCKED** para
continuity amplia, aunque queda mejor preparada para una comparación estrecha
de perceived distance.

## Candidate result

Se crea un único candidato porque la conclusión aporta una restricción de
transferencia reutilizable y una operacionalización más estrecha:
`CAND-CROSS-004`, `CONSTRUCT_TRANSFER_CONSTRAINT`, `POSSIBLE_WITH_SCOPE`.

La auditoría queda pendiente. El gate de evidencia para auditarlo es `PASS`;
`PASS` no implica promoción.

## Capabilities

| Capability | Result |
|---|---|
| Define realization target | `PARTIAL` |
| Operationalize target | `YES WITH SCOPE` for perceived distance; `NO` for broad continuity |
| Transfer analytical metrics | `PARTIAL` |
| Filter future criteria | `IMPROVES` |
| Rank realizations now | `NO` |

## Experiment policy

No se diseña experimento. `EXP-002` permanece `PAUSED` y el gate de esta RQ
es `NOT JUSTIFIED`.

## Recommended next step

Auditar `CAND-CROSS-004` antes de abrir una comparación de realizaciones.
