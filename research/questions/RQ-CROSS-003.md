# RQ-CROSS-003 - Exact Return vs Controlled Varied Return for Melodic Identity

## Status

- `status: SYNTHESIZED`
- `scope: short melodic material returning within declared local/phrase context`
- `candidate_audit_status: COMPLETED`
- `candidate_audit_evidence_gate: PASS`
- `next_unused_candidate_id: CAND-CROSS-004`
- `phase: Phase 2`
- `experiment_gate: NOT JUSTIFIED`

## Central question

Cuando material melodico previamente establecido retorna, que evidencia apoya
la recurrencia exacta frente a una variacion controlada si el criterio es
reconocimiento o preservacion de identidad melodica perceptible?

La formulacion compositiva es: si el compositor quiere que el material
posterior se oiga como la misma idea o como una idea claramente relacionada,
que cambios pueden introducirse sin perder reconocimiento bajo una tarea y
alcance declarados?

## Construct check

El criterio no es una sola variable:

- `recognition`: identificar o discriminar material como previamente escuchado;
- `similarity`: juzgar grado de parecido;
- `same/different`: decidir identidad bajo una instruccion concreta;
- `familiarity`: experiencia o sensacion de conocimiento;
- `memory accuracy`: rendimiento de recuerdo o discriminacion;
- `motivic identity`: categoria analitica/compositiva;
- `formal return`: funcion de reaparicion en una forma;
- `memorability`: facilidad de recuerdo;
- `liking`: preferencia o agrado.

No se tratan como sinonimos.

Resultado del target construct: **READY WITH SCOPED OPERATIONALIZATION**.
Existe evidencia directa de reconocimiento y de similitud, pero son criterios
distintos. La comparacion positiva puede intentarse solo para una dimension de
variacion, una tarea y una representacion especificadas.

## Exact-return definition

`Exact return` no se fija en una unica representacion universal. Puede
significar, segun la fuente:

- mismos pitches absolutos;
- mismos intervalos bajo transposicion;
- mismo contorno;
- mismo ritmo y duraciones;
- mismos onsets;
- mismo registro;
- misma armonia.

En esta RQ, la baseline experimental debe describirse por el nivel realmente
comparado. “Exacto” significa igualdad respecto de esa representacion, no
igualdad simultanea de todas las dimensiones.

## Controlled varied return

`Controlled varied return` es una variante que cambia una dimension declarada
manteniendo invariantes declaradas. No es una condicion homogenea. Las
dimensiones posibles son pitch/interval, contour, rhythm/onset/duration,
register, transposition, ending, ornamentation y harmony, pero solo se
consideran comparables donde exista evidencia directa.

## Empirical source table

| Source | Stimulus / exposure | Exact/variant manipulation | Preserved invariants | Task | Dependent measure | Result | Scope | Directness |
|---|---|---|---|---|---|---|---|---|
| SRC-EMPIRICAL-027 | melodias breves y folk familiares; memoria corta y larga | igual, transpuesta, mismo contorno, contorno + intervalos relativos, base armonica | depende de la condicion; ritmo y longitud se controlan en parte | same/different y reconocimiento de distorsiones | reconocimiento correcto | transposicion cambia la representacion util; en folk, intacta > contorno+intervalos relativos > contorno solo > base armonica | memoria melodica, no forma | PARTIAL |
| SRC-EMPIRICAL-028 | melodias nuevas ensenadas | altura, contorno y chroma preservados o violados | condiciones separan cues de pitch | reconocimiento de transformaciones | reconocimiento y errores | contorno + chroma preservados supera condiciones con solo contorno; violar altura y contorno deteriora fuertemente | laboratorio, melodias nuevas | PARTIAL |
| SRC-ACADEMIC-007 | 17 melodias nuevas | contour, tonality, rhythm y meter manipulados factorialmente | dimensiones manipuladas por separado | ratings de similitud | similitud percibida | en una condicion ritmo fue mayor contribuyente; con contexto y tempo cambiados contorno dominó; efectos flexibles | similitud, no identidad | INDIRECT |
| SRC-EMPIRICAL-019 | cadenas melodicas simples | pitch/interval, contour y rhythm manipulados en paradigmas de reconocimiento | depende del paradigma | reconocimiento | discriminacion/reconocimiento | apoya separar representaciones y tareas, sin receta de retorno | memoria melodica | PARTIAL |
| SRC-ACADEMIC-005 | melodias familiares y memoria larga | informacion interválica frente a contorno en condiciones de memoria | representacion cambia con familiaridad | reconocimiento | reconocimiento | intervalos ganan importancia en memoria larga bajo el alcance registrado | repertorio y fuente acotados | PARTIAL |
| SRC-ACADEMIC-046 | revision de estudios y ejemplos de variacion | cambios de pitch, duracion, espacio, timbre y relaciones | depende de cada estudio | varias tareas reportadas | similitud, reconocimiento, correspondencia | exact repetition tiene maxima similitud fisica; la similitud perceptiva depende de tarea, contexto y representacion | revision, no una comparacion unica | INDIRECT |

## Variation-dimension matrix

| Dimension | What changes | What is preserved | Recognition evidence | Similarity evidence | Formal-return evidence | Can FILTER? | Can RANK? | Scope |
|---|---|---|---|---|---|---|---|---|
| transposition | pitch absolute | interval/contour, a menudo ritmo | `PARTIAL`: reconocimiento puede sobrevivir, tarea importa | `PARTIAL` | no directa | YES WITH SCOPE | RANK SPECIFIC ONLY | memoria melodica |
| pitch substitution | uno o mas pitches | depende del diseño | `PARTIAL`: Massaro/Dowling muestran efectos de cues | no aislada de forma general | no | YES WITH SCOPE | RANK SPECIFIC ONLY | melodias de laboratorio |
| interval change | tamanos interválicos | contorno posible | `PARTIAL`: intervalos relativos añaden reconocimiento en folk familiar | no independiente de recognition | no | YES WITH SCOPE | RANK SPECIFIC ONLY | familiaridad y tarea |
| contour-preserving change | pitch/interval magnitudes | ups/downs | `PARTIAL`: contorno sostiene parte del reconocimiento | `PARTIAL` | no | YES WITH SCOPE | no ranking universal | transposicion/contour |
| rhythm change | duraciones/onsets | pitch o contour posible | INSUFFICIENT direct identity evidence | `PARTIAL` via Prince similarity | no | UNCERTAIN | NO | rhythm no aislado para identity |
| metric displacement | posicion temporal/acento | pitch puede conservarse | no evidencia directa suficiente | no evidencia directa suficiente para identity | no | NO | NO | alcance abierto |
| register change | octava/tesitura | relaciones intervalicas posibles | no evidencia separada suficiente | no evidencia separada suficiente | no | UNCERTAIN | NO | gap |
| changed ending | final distinto | opening/body posible | no comparacion directa suficiente | no | no | UNCERTAIN | NO | gap |
| ornamentation | notas decorativas | estructura hipotetica | no fuente directa inspeccionada suficiente | no | no | NO | NO | gap |
| harmonic recontextualization | armonia bajo la misma melodia | melodia | no fuente directa suficiente | no fuente directa suficiente | no | NO | NO | melody != harmony |

La matriz no establece que las dimensiones sean independientes ni ordena su
importancia universal.

## Exact versus controlled variant

| Comparison | Criterion | Result |
|---|---|---|
| intact melody vs contour + relative-interval distortion | recognition | `RANK SUPPORTED WITH SCOPE`: la version intacta fue mas reconocible en el paradigma de folk familiar |
| contour + relative intervals vs contour-only distortion | recognition | `RANK SUPPORTED WITH SCOPE`: el registro inspeccionado reporta mayor reconocimiento para preservar tambien relaciones intervalicas |
| exact transposition vs same-contour variant | recognition | `FILTER / PARTIAL`: la representacion y la tarea cambian; no ranking universal |
| contour + chroma preserved vs contour-only / height-violating variants | recognition | `RANK SUPPORTED WITH SCOPE`: Massaro reporta mejor reconocimiento cuando se preservan contour y chroma |
| exact vs rhythm-changed return | recognition | `INSUFFICIENT`: Prince mide similarity, no identity |
| exact vs varied return generally | recognition | `INSUFFICIENT`: “varied return” no es una manipulacion unica |

Estos resultados rankean una variante especifica bajo una tarea y alcance; no
demuestran que exact return sea mejor musica, mas memorable o formalmente
preferible.

## Pitch, rhythm and contour findings

`Pitch vs rhythm` no permite una conclusion unica sobre identity con las
fuentes inspeccionadas. Prince factorialmente manipula pitch contour,
tonality, rhythm y meter, pero mide similarity. Sus resultados cambian con
tempo, prefijo armonico y condiciones de escucha; por eso no se convierten en
ranking de recognition.

Dowling y Fujitani muestran que contorno e intervalos relativos pueden apoyar
reconocimiento bajo transposicion/distorsion, pero la contribucion depende de
memoria, familiaridad y tarea. Massaro muestra que tone height, contour y
chroma contribuyen de manera diferenciable en melodias aprendidas.

No se establece que rhythm domine pitch, que pitch domine rhythm, ni que
preservar una sola dimension garantice identidad.

## Transposition, register and representation

`ABSOLUTE-PITCH IDENTITY != MELODIC-RELATIONAL IDENTITY`.

La transposicion puede preservar relaciones intervalicas y contorno mientras
cambia alturas absolutas. Dowling y Fujitani muestran que la tarea cambia con
transposicion; no se debe etiquetar automaticamente como exact return o
varied return.

El efecto separado de registro/octava no queda suficientemente aislado en el
material inspeccionado. No se infiere que misma pitch-class structure implique
misma identidad perceptiva.

## Changed ending, ornamentation and harmony

No se encontró evidencia directa suficiente para rankear un final cambiado,
ornamentacion o recontextualizacion armonica como variantes de identity.

Puede ser razonable conservar un opening/body mientras cambia el ending como
operacion compositiva, pero eso sigue siendo una hipotesis compositiva, no un
resultado de recognition en esta RQ. `MELODY IDENTITY != HARMONIC IDENTITY`.

## Exposure, delay and scale

El reconocimiento depende de exposure, familiaridad, memoria corta/larga,
delay e intervening material. Las fuentes no justifican un umbral universal de
repeticiones ni una distancia temporal fija.

La evidencia se concentra en eventos y fragmentos melodicos aislados. No se
transfiere automaticamente a:

- recurrence local inmediata;
- retorno de frase;
- retorno de seccion;
- retorno a escala de cancion.

`FORMAL RETURN != PERCEPTUAL RECOGNITION`, y recognition tampoco prueba una
funcion formal de return.

## Structure -> perception -> composition

- **Structure:** relacion melodica exacta o variante y dimensiones preservadas.
- **Perception:** recognition, same/different o similarity bajo una tarea.
- **Composition:** elegir exact return o una variante controlada.

No se hace el puente silencioso `recognition -> better return -> better music`.
El ranking, cuando existe, es solo sobre el criterio de recognition bajo el
alcance declarado.

## Source-to-target transfer

| Source result | Target composition decision | Transfer |
|---|---|---|
| laboratory recognition | elegir exact vs variante especifica | `PARTIAL` |
| similarity rating | identidad de recurrencia | `INDIRECT` |
| contour/interval recognition | decidir que relacion preservar | `PARTIAL`, requiere representacion declarada |
| formal return analysis | recognition perceptiva | `NOT ESTABLISHED` |
| recognition of isolated melodies | song-level return | `UNKNOWN TRANSFER` |

## Capability result

- `CAN ENUMERATE VARIANTS`: **YES WITH SCOPE**.
- `CAN FILTER VARIANTS`: **YES WITH SCOPE**, para dimensiones y tareas
  declaradas.
- `CAN RANK EXACT vs VARIANT ON RECOGNITION`: **YES WITH SCOPE**, pero solo
  frente a variantes especificas, no frente a “variation generally”.

## Phase-2 result

**YES, partially positive.** La RQ produce conocimiento comparativo positivo
acotado:

1. intact melody > contour + relative-interval distortion en el paradigma
   inspeccionado de reconocimiento de melodias familiares;
2. contour + relative intervals > contour-only distortion bajo ese alcance;
3. contour + chroma preserved > variantes que violan esos cues en Massaro.

No produce una preferencia global por exact return ni una jerarquia universal
de pitch, rhythm, contour o interval.

## Candidate result

Se crea un unico candidato positivo y especifico: `CAND-CROSS-003`.

## Candidate audit evidence gate

**PASS.** El candidato se audita como **REVISE / POSSIBLE_WITH_SCOPE**. El
contraste positivo sobrevive para comparaciones especificas de recognition.
La condicion intacta de la fuente no se convierte en “exact return” sin una
calificacion: es una baseline de laboratorio cuya transferencia a una
recurrencia compositiva es parcial.

La comparacion `contorno + intervalos relativos > contorno solo` es directa en
el paradigma de melodias folk familiares inspeccionado. El resultado de
Massaro se conserva como apoyo separado para melodias nuevas aprendidas: no se
fusiona con el resultado de familiaridad larga ni se usa para crear una
jerarquia universal.

`Recognition` no se convierte en `perceptible identity`, `similarity`,
`memory accuracy`, `memorability` ni `formal return`. Prince aporta solo
contexto de similarity; McAdams/Matzkin aporta marco conceptual, no una nueva
comparacion primaria.

La auditoria no encuentra soporte para rankear ritmo, registro, final
cambiado, ornamentacion o recontextualizacion armonica, ni para retorno de
frase, seccion o cancion. La transferencia fuente -> composicion es
**PARTIAL**; la transferencia a retorno formal es **NOT ESTABLISHED**.

El candidato conserva `COMPARATIVE_DECISION_KNOWLEDGE` descriptivo porque
contiene objetivo, contexto, alternativa A/B, criterio de recognition,
resultado y alcance. Su valor es comparativo y condicionado, no una
preferencia global de composicion.

## Experiment gate

**NOT JUSTIFIED.** Aunque existen comparaciones directas, quedan abiertas la
transferencia a retorno formal, el papel de rhythm, la escala de frase/seccion
y la separación entre identity y similarity. `EXP-002` permanece pausado.

## Comparison-first test

**YES, parcialmente.** Fue apropiado como primer paso porque recognition tiene
operacionalizaciones más claras que local arrival. La RQ aún necesitó
operacionalizacion por dimensión; no valida “varied return” como condición
unitaria.

## Impact on prior knowledge

- Melody initial construction: clarifica que relaciones preservables no son
  automaticamente relaciones identity-preserving.
- Repetition/variation: añade comparaciones acotadas, sin regla de calidad.
- `CAND-MEL-031`--`034`: no se modifican; la RQ aporta el puente perceptivo
  pendiente solo en dimensiones concretas.
- `FORM-007`: return/recurrence sigue siendo categoria formal; no se redefine.
- Composer Foundations v4: potencialmente mejora `WITHIN-DOMAIN MATERIAL
  RANKING` de `FILTER ONLY` a `RANK WITH SCOPE` para variantes especificas.

## What remains unsupported

- exact vs varied return en general;
- rhythm-preserving superiority para recognition;
- changed-ending recognition;
- ornamentation;
- harmonic recontextualization;
- register/octave effect aislado;
- retorno formal de frase, seccion o cancion;
- identidad = memorability, liking, hook o formal success.

## Recommended next step

Presentar `CAND-CROSS-003` para integracion metodologica posterior en
Composer Foundations, sin actualizarlo automaticamente y sin iniciar
experimento ni nueva RQ.
