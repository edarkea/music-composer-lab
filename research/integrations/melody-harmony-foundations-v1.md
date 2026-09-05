# Melody + Harmony Foundations v1

## Purpose and Scope

Esta integración reintegra los resultados sintetizados de `RQ-MEL-009` en la
integración conjunta de Melody y Harmony. No es nueva investigación, auditoría
de candidatos, manual, regla ni conclusión aprobada. No modifica el snapshot
histórico v0 ni cambia estados de candidatos, RQ, síntesis o verificación.

La pregunta principal es: ¿puede el sistema comenzar con una intención local y
un contexto declarado, construir un candidato melódico inicial, declarar
invariantes utilizables y entregarlo a la selección y realización armónicas?
La pregunta complementaria es: ¿en qué etapa deja de existir una elección
justificada?

Alcance heredado: tradiciones tonales/modales occidentales y prácticas próximas
ya investigadas. No se generaliza fuera de ese alcance.

## Epistemic Status

Documento de integración de investigación, candidato a revisión metodológica.
Los candidatos siguen siendo candidatos. `CAND-MEL-031`–`034` son
`POSSIBLE_WITH_SCOPE` tras auditoría; `CAND-MEL-035` y `CAND-MEL-036` son
`DEFERRED / NOT AUDITABLE`. `CAND-MEL-018` permanece `REJECTED`.

Las etiquetas de capacidad de este documento no son estados epistemológicos:

- `CAN ENUMERATE OPTIONS`: puede producir alternativas explícitas.
- `CAN FILTER OPTIONS WITH CRITERIA`: puede descartar alternativas por
  restricciones y condiciones declaradas.
- `CAN RANK OPTIONS FOR A GOAL`: puede justificar comparativamente cuál sirve
  mejor al objetivo.

`CAN GENERATE` no equivale a `CAN CHOOSE WELL`.

## What Changed Since Melody + Harmony Foundations v0

El estado sin material melódico ya no está casi completamente bloqueado. La
integración puede ahora:

- condicionar la construcción a un objetivo posterior, sin convertirlo en una
  determinación única (`CAND-MEL-031`);
- representar una semilla mediante pitch exacto, pitch class, intervalos,
  contorno, ritmo/onsets, duración y trayectoria registral, según proceda
  (`CAND-MEL-032`);
- separar construcción, presentación/recurrencia y establecimiento perceptivo
  (`CAND-MEL-033`);
- declarar relaciones manipulables, preservables o transformables para una
  operación concreta (`CAND-MEL-034`).

Por ello `CAN ENUMERATE` mejora de forma material y `CAN FILTER` mejora con
alcance. `CAN RANK` continúa bloqueado. Los candidatos 035/036 siguen siendo
deuda de evidencia: no autorizan una política general sobre extremos abiertos
o cerrados ni sobre la necesidad de una progresión armónica explícita.

## Core Composer Architecture

La arquitectura conjunta mejor sustentada pasa provisionalmente a ser:

`COMPOSITIONAL INTENT / LOCAL GOAL`
→ `INITIAL MELODIC CONSTRUCTION`
→ `MELODIC CANDIDATE + DECLARED INVARIANTS`
→ `HARMONIC CONTEXT / SELECTION`
→ `HARMONIC REALIZATION`
→ `TIMING / ARRIVAL / PHRASE CONTEXT`
→ `REVISION / TRANSFORMATION`

No se adopta como secuencia obligatoria. La selección armónica puede informar
la revisión melódica, y timing, forma y realización pueden obligar a volver a
pasos anteriores. Lo que sí se sostiene es una separación de decisiones: una
semilla puede existir como candidato antes de establecerse por recurrencia;
una representación puede declarar una invariante sin predecir identidad
perceptiva; una melodía fija puede restringir, pero no determinar, la armonía.

### Construction != Establishment != Transformation

1. **Initial construction:** se especifica material candidato, sus límites y
   sus relaciones.
2. **Formal presentation / recurrence:** el material se repite, se restatea o
   retorna como decisión formal.
3. **Perceptual establishment:** el oyente reconoce o codifica una identidad;
   no se deduce automáticamente de la recurrencia.
4. **Later transformation:** una relación se conserva, altera, fragmenta,
   transpone o combina.

La repetición exacta es una operación disponible para establecer o reforzar en
marcos acotados, no requisito de existencia de un motivo ni garantía de
reconocimiento.

## Composer From Zero

Partimos de objetivo local, centro/colección tonal-modal opcional y
restricciones prácticas de registro, sin material melódico previo.

| Decisión | Enumerate | Filter | Rank | Bloqueador principal |
|---|---|---|---|---|
| qué relación especificar | Sí | Sí, respecto de la operación prevista | No | falta evidencia comparativa entre relaciones |
| representación de trabajo | Sí | Sí, según la invariante buscada | No | no existe representación primaria universal |
| extensión de la semilla | Sí | Parcial | No | no hay tamaño óptimo de notas, compases o duración |
| pitches a instanciar | Sí | Sí, por colección, rango y relación declarados | No | objetivo insuficiente para elegir alturas concretas |
| ritmo a instanciar | Sí | Sí, con tempo/metro/contexto declarados | No | no hay criterio general de efecto musical |
| registro | Sí | Sí, por tesitura y ejecutabilidad | No para energía o emoción | confundidores de dinámica, timbre y arreglo |
| recurrencia/contraste interno | Sí | Parcial, por operación local | No | función formal no determinada |
| comportamiento del final | Sí | Parcial, con contexto | No | 035 diferido; apertura/cierre perceptivos no predichos |
| invariantes | Sí | Sí, si la operación está declarada | No sobre su valor artístico | una relación útil no es necesariamente preferible |
| operación posterior objetivo | Sí | Sí, como intención | No | goal-conditioned no es goal-determined |
| momento de repetir/presentar | Sí | Parcial, por marco formal | No | dosis y efecto perceptivo sin ranking |
| entrega a Harmony | Sí | Sí, por incompatibilidades y restricciones | No | melodía fija subdetermina selección |

Resultado: el sistema puede producir candidatos intencionales y trazables,
pero no una elección única justificada desde cero. La primera arbitrariedad
general aparece al escoger entre candidatos compatibles cuando no existe un
criterio comparativo específico. En muchos casos prácticos, la instancia más
concreta es elegir alturas o ritmos exactos; en otros, aparece antes al elegir
extensión, representación o finalidad formal.

## Goal-Conditioned Seed Construction

`CAND-MEL-031` respalda una heurística de planificación: declarar la operación
posterior puede orientar qué relación conviene hacer explícita y qué
restricciones filtrar. No respalda que el objetivo determine un seed único ni
que una semilla orientada al desarrollo sea superior.

Flujo seguro:

1. declarar la operación pretendida;
2. identificar qué relación podría necesitar sobrevivir;
3. instanciar varias alternativas;
4. comprobar restricciones explícitas;
5. conservar alternativas si falta criterio de ranking.

Operaciones que el conocimiento existente permite inspeccionar con alcance:
repetición exacta, cambio de final, transposición, fragmentación,
reinterpretación armónica, recurrencia de loop, transformación registral y
retorno seccional. La disponibilidad es operativa, no un juicio de calidad.

## Seed Representations

Las representaciones son separables para declarar invariantes, pero no son
independientes y no tienen jerarquía universal. La elección depende de lo que se
quiera conservar:

| Representación | Invariante que puede declarar | Operación compatible | Límite |
|---|---|---|---|
| pitch exacto | alturas concretas | repetición, pedal, reaplicación | restringe más la armonización |
| pitch class / grados | pertenencia o relación tonal | recontextualización acotada | depende del centro/colección |
| intervalos | distancias sucesivas | transposición, secuencia | registro y marco pueden cambiar el resultado |
| contorno | dirección local | transformación de magnitudes | no basta para identidad |
| ritmo/onsets/duración | organización temporal | repetición o variación temporal | depende de metro, tempo y acento |
| registro/ trayectoria | zona y desplazamiento | expansión, contracción, contraste | altura no implica emoción |

`SEPARABLE` no significa `INDEPENDENT`. La notación exacta y las abstracciones
relacionales deben coexistir cuando la operación lo necesite; no se impone
pitch-first ni rhythm-first.

## Construction vs Establishment

El sistema puede distinguir una semilla especificada pero aún no establecida de
material que ya funciona como identidad recurrente dentro de un contexto. La
distinción cambia la pregunta de trabajo: antes de repetir se pregunta qué
material se construyó; después se puede preguntar qué se mantiene, qué se
varía y qué ha sido formalmente presentado. El establecimiento perceptivo
requiere escucha o evidencia específica; no se marca por decreto al crear o
repetir el material.

## Transformable Relations

El vocabulario seguro es `MANIPULABLE`, `PRESERVABLE` y `TRANSFORMABLE`.
Intervalos, ritmo, fragmento, relación de final, pitch exacto o registro pueden
declararse como relaciones operativas cuando están explícitos. Eso permite
preparar una operación posterior, pero no permite inferir que el material sea
`GOOD`, `STRONG`, `MEMORABLE` o `DEVELOPABLE` en sentido perceptivo.

## Deferred Initial-Idea Knowledge

`CAND-MEL-035` — **DEFERRED / NOT AUDITABLE**: open vs bounded seed. No se
establece una política general de final abierto, cerrado o loopable. Sí pueden
manipularse, cuando el contexto lo permite, pitch final, duración final,
silencio, continuación y cambio de final.

`CAND-MEL-036` — **DEFERRED / NOT AUDITABLE**: melody-first without explicit
harmonic progression. No puede afirmarse que la armonía explícita sea
innecesaria para construir una semilla. Sólo puede decirse que un centro,
colección o scaffold proporcionado puede servir para filtrar y que la pregunta
de dependencia queda abierta.

## Melodic Invariants

La salida mínima de una construcción debe declarar, cuando sea pertinente:
`representation`, `exact_material`, `intended_invariants`, `local_goal`,
`later_operation_target`, `center_or_collection`, `open_closed_intention` y
`uncertainties`. Un invariante es una decisión sobre qué se conservará, no una
predicción de reconocimiento. La armonía puede restringir pitch y facilitar el
filtro; también puede reducir posibilidades de reinterpretación.

## Handoff to Melody Operations

| Operación heredada | ¿La semilla permite entrar? | Condición |
|---|---|---|
| `ESTABLISH` | Parcialmente | material delimitado y presentación elegida; efecto perceptivo abierto |
| `CONTINUE` | Parcialmente | relación de arranque y contexto de frase |
| `REPEAT` | Sí, estructuralmente | material exacto disponible; no garantiza identidad |
| `VARY` | Sí, con alcance | invariante y dimensión variable declaradas |
| `DEVELOP` | Parcialmente | tradición y operación concreta; no sinónimo de calidad |
| `CONTRAST` | Parcialmente | requiere forma, ritmo, arreglo o contexto adicional |
| `ARRIVE` | Parcialmente | objetivo melódico; llegada no equivale a cierre |
| `CLOSE / OPEN` | Parcialmente | armonía, métrica y forma siguen siendo necesarias |
| `RETURN / REUSE` | Sí, estructuralmente | material identificable; función del retorno no garantizada |

RQ-MEL-009 mejora la entrada a estas operaciones, no las vuelve igualmente
disponibles ni rankeables.

## Handoff to Harmony Selection

La interfaz queda expresada como:

`INITIAL MELODIC CANDIDATE + DECLARED INVARIANTS + LOCAL GOAL`
→ `HARMONIC SELECTION`
→ `HARMONIC REALIZATION`.

La melodía puede constreñir por pitch exacto, colección, rango, timing u
objetivo, y puede sugerir varias lecturas. `CAND-HAR-047` impide inferir una
selección única desde una melodía fija. El sistema puede enumerar y filtrar
selecciones contextuales; el ranking requiere objetivo comparativo y evidencia
que no está disponible de forma general.

## Handoff to Harmonic Realization

Una vez elegida una identidad o relación armónica, la semilla puede ser
realizada con alternativas de bajo, inversión, voicing, spacing,
doubling/omission, asignación de voces y registro. `CAND-HAR-043`, `049` y la
separación root/bass sostienen la multiplicidad de realizaciones. La
realización puede cumplir restricciones físicas y de tesitura, pero mínima
distancia, conducción de voces, bajo común o una sonoridad concreta no son
objetivos universales. La calidad de la realización sigue necesitando contexto
y escucha.

## From Zero to Harmonized Candidate Test

**GOAL:** material corto reutilizable para una reutilización con final cambiado.
**CONTEXT:** centro/colección declarados y registro práctico.

| Paso | Enumerate | Filter | Rank | Resultado |
|---|---|---|---|---|
| 1. construir semillas | Sí | Sí, por restricciones declaradas | No | múltiples candidatos compatibles |
| 2. declarar invariantes | Sí | Sí, por cambio de final | No | núcleo y punto modificable explícitos |
| 3. filtrar para la operación | Sí | Sí | No | se eliminan candidatos incompatibles |
| 4. escoger candidato | Sí | Sí | **Bloqueado** | primera elección no justificada en general |
| 5. seleccionar apoyo armónico | Sí | Sí, por colección, pitch y objetivo | No | varias lecturas posibles |
| 6. realizar armonía | Sí | Sí, por bajo, voicing, rango y voces | No | realizaciones admisibles múltiples |
| 7. inspeccionar voice leading/bajo/timing | Sí | Sí, estructuralmente | No | diagnóstico, no preferencia general |
| 8. probar el final cambiado | Sí | Sí, por relación conservada | No | operación comprobable; efecto perceptivo abierto |

La arbitrariedad aparece por primera vez, de modo general, en el paso 4. Puede
reaparecer en 5 y 6 incluso si un candidato fue elegido por preferencia
artística. El pipeline ya puede llegar a un candidato armonizado justificable
como compatible con restricciones; no puede justificar que sea el mejor.

## Same Melody / Different Harmony

El mismo material melódico puede conservarse mientras cambia el bajo, la
sonoridad, la función, la colección, el timing o el voicing. Esto demuestra
posibilidad estructural y disponibilidad compositiva, no desarrollo,
reinterpretación perceptiva, mayor expresividad ni memorabilidad. Una nota
tenida puede funcionar como tono común, pedal, suspensión-tipo o relación
reinterpretada según el marco; la lectura analítica no garantiza la experiencia
del oyente.

## Timing and Arrival

Se mantienen separados onset, duración, IOI, posición métrica, cambio armónico,
duración armónica, llegada melódica, llegada armónica y frontera formal. La
melodía puede llegar antes, después o mientras la armonía permanece abierta.
Alargar un final o dejar silencio puede contribuir al cierre sólo coordinado
con armonía, métrica y forma. La alineación temporal no es una regla de cierre.

## Selection / Realization / Revision Loop

El flujo operativo es iterativo:

`CONSTRUCT` → `DECLARE INVARIANTS` → `SELECT` → `REALIZE` → `INSPECT` →
`REVISE / TRANSFORM`.

La revisión puede modificar la semilla si el voicing, bajo, tesitura, timing o
objetivo formal la vuelven impracticable. Una modificación no demuestra que la
versión final sea superior; demuestra sólo que satisface mejor las
restricciones adoptadas.

## Candidate Coverage Matrix

La cobertura es de trazabilidad, no reauditoría. Todos los IDs asignados
aparecen aquí; no se alteran sus estados.

### Melody

`CAND-MEL-001`–`017`: candidatos heredados para transposición, identidad,
ritmo, repetición, variación, frase, contorno y llegada; siguen `candidate` y
su alcance no autoriza ranking general.

`CAND-MEL-018`: **REJECTED**; no se utiliza como evidencia.

`CAND-MEL-019`–`030`: candidatos heredados para registro, tesitura, contraste,
prominencia, retorno, métrica, anticipación, síncopa, silencio y densidad;
siguen `candidate`, con filtros contextuales pero sin ranking universal.

`CAND-MEL-031`–`034`: `candidate`, auditoría completada, `REVISE`,
`POSSIBLE_WITH_SCOPE`.

`CAND-MEL-035`–`036`: **DEFERRED / NOT AUDITABLE**; no reciben readiness.

### Harmony

`CAND-HAR-001`–`045`: candidatos asignados y heredados para centro, función,
selección, persistencia, timing, cromatismo, bajo, inversión, voicing y
realización; permanecen con su readiness heredado.

`CAND-HAR-046`–`052`: candidatos auditados como material de interacción; sus
resultados heredados se conservan: 046 `REVISE`, 047 `REVISE`, 048 `KEEP_AS_IS`,
049 `REVISE`, 050 `REVISE`, 051 `REVISE`, 052 `REVISE`.

Cobertura confirmada: `CAND-MEL-001`–`036` (36/36) y
`CAND-HAR-001`–`052` (52/52).

Inventario explícito: `CAND-MEL-001`, `002`, `003`, `004`, `005`, `006`,
`007`, `008`, `009`, `010`, `011`, `012`, `013`, `014`, `015`, `016`, `017`,
`018`, `019`, `020`, `021`, `022`, `023`, `024`, `025`, `026`, `027`, `028`,
`029`, `030`, `031`, `032`, `033`, `034`, `035`, `036`; y
`CAND-HAR-001`, `002`, `003`, `004`, `005`, `006`, `007`, `008`, `009`,
`010`, `011`, `012`, `013`, `014`, `015`, `016`, `017`, `018`, `019`, `020`,
`021`, `022`, `023`, `024`, `025`, `026`, `027`, `028`, `029`, `030`, `031`,
`032`, `033`, `034`, `035`, `036`, `037`, `038`, `039`, `040`, `041`, `042`,
`043`, `044`, `045`, `046`, `047`, `048`, `049`, `050`, `051`, `052`.

## Interaction-Specific Candidate Map

| Candidatos | Relación conjunta | Límite |
|---|---|---|
| MEL-031 ↔ HAR-047 | objetivo condicionado orienta una semilla; melodía fija subdetermina selección | no crear una selección única |
| MEL-032 ↔ HAR-043/049 | invariantes y representación informan qué realizaciones siguen disponibles | separable no significa independiente |
| MEL-033 ↔ MEL-007/008/011/012 + HAR-051 | construcción y establecimiento se distinguen de repetir bajo armonía cambiada | repetición no prueba reconocimiento ni desarrollo |
| MEL-034 ↔ MEL-009/010 + HAR-048/051 | relaciones preservables pueden ser transformadas o reinterpretadas | transformable no significa mejor ni desarrollable |
| MEL-019/020/022/023 ↔ HAR-041/045 | registro y bajo/spacing se coordinan | no se infiere emoción o preferencia |
| MEL-025–030 ↔ HAR-021–026 | timing melódico y armónico se pueden separar y coordinar | no hay sincronización universal |
| MEL-016/017/028 ↔ HAR-027–032/050 | llegada y cierre requieren diagnóstico conjunto | llegada no equivale a cierre |

No se crean afirmaciones combinadas nuevas: el mapa sólo ubica dependencias y
límites de afirmaciones ya integradas.

## Capability Ladder

| Stage | Enumerate | Filter | Rank | Main evidence | Main blocker |
|---|---|---|---|---|---|
| choose seed representation | Sí | Sí | No | MEL-032 | sin jerarquía universal |
| choose seed extent | Sí | Parcial | No | RQ-MEL-009 | tamaño/tiempo óptimo desconocido |
| choose pitch relations | Sí | Sí | No | MEL-001–005, 031–034 | objetivo no compara resultados |
| choose exact pitches | Sí | Sí | No | colección, rango, invariantes | C4-E4-D4 vs C4-D4-G4 sin criterio |
| choose rhythm | Sí | Sí con metro/tempo | No | MEL-006, 025–030 | efecto aislado no establecido |
| choose register | Sí | Sí por tesitura | No | MEL-019–023 | confundidores estilísticos |
| choose internal recurrence | Sí | Parcial | No | MEL-007, 010–012 | función y dosis |
| choose ending behavior | Sí | Parcial | No | MEL-008, 017, 028; 035 diferido | apertura/cierre perceptivo |
| choose invariants | Sí | Sí para una operación | No | MEL-031/032/034 | valor relativo no medido |
| choose later-operation target | Sí | Sí como intención | No | MEL-031 | no determina la semilla |
| establish by recurrence | Sí | Parcial | No | MEL-007/033 | recurrencia no garantiza reconocimiento |
| select harmony | Sí | Sí por contexto y melodía | No | HAR-047/048 | subdeterminación y múltiples metas |
| realize harmony | Sí | Sí estructuralmente | No | HAR-040–045/049 | preferencia de voicing no general |
| coordinate timing | Sí | Sí por restricciones | No | MEL-025–030, HAR-021–026 | forma/arreglo/metro faltantes |
| coordinate arrival | Sí | Sí por estados declarados | No | HAR-050, MEL-016/017/028 | cierre cross-domain |
| revise seed after realization | Sí | Sí por conflicto | No | arquitectura iterativa | criterio de mejora no definido |

## Diagnostic vs Generative Power

| Área | Diagnostic power | Generative power | Razón |
|---|---|---|---|
| initial seed construction | HIGH | MEDIUM | decisiones e invariantes explícitas; no ranking |
| motif establishment | HIGH | LOW-MEDIUM | se distinguen construcción, recurrencia y percepción |
| melodic transformation | HIGH | MEDIUM | operaciones y relaciones manipulables |
| harmonic selection | HIGH | LOW-MEDIUM | alternativas y filtros; melodía no determina |
| harmonic realization | HIGH | LOW-MEDIUM | restricciones y realizaciones enumerables |
| melody–harmony interaction | HIGH | LOW-MEDIUM | interfaz descrita; efectos no ponderados |
| timing | HIGH | LOW-MEDIUM | variables separables; pesos contextuales faltantes |
| arrival/closure | HIGH | LOW | estados distinguibles; convergencia cross-domain pendiente |

El aumento generativo es real pero acotado: el sistema ahora puede construir
intencionalmente candidatos y entregarlos a Harmony. La capacidad generativa no
incluye elección artística justificada.

## Enumerate / Filter / Rank Matrix

En conjunto: **CAN ENUMERATE OPTIONS: sí**, **CAN FILTER OPTIONS WITH CRITERIA:
sí, con alcance**, **CAN RANK OPTIONS FOR A GOAL: no de forma general**.

El filtro es sólido para restricciones explícitas —rango, colección declarada,
invariante, compatibilidad con una transformación, representación y
ejecutabilidad—, pero no para efectos como memorabilidad, hook, energía,
emoción o calidad. Un filtro estructural no es un ranking estético.

## What Blocks Ranking

La brecha no es simplemente “percepción”. Se descompone así:

- **A. Objective not specified:** sin objetivo no hay criterio de comparación.
- **B. Goal specified but no comparative evidence:** incluso con objetivo, no
  sabemos qué estructura lo logra mejor.
- **C. Multiple goals conflict:** identidad/flexibilidad, continuidad/contraste,
  apertura/cierre y estabilidad/novedad pueden competir.
- **D. Style / genre required:** el ranking depende del idioma y de la práctica.
- **E. Cross-domain required:** forma, ritmo, arreglo, interpretación, letra y
  prosodia pueden cambiar la función de la misma semilla.
- **F. Perceptual measure missing:** estructura descrita no predice por sí sola
  reconocimiento, prominencia, energía o cierre.
- **G. Artistic preference:** la decisión final puede ser deliberadamente
  subjetiva y no debe sustituirse por una falsa objetividad.

No toda brecha es un experimento pendiente. Algunas requieren objetivo más
preciso, conocimiento de otro dominio o una decisión artística.

## Ranking Target Taxonomy

Posibles objetivos de ranking y estado actual:

| Objetivo | Estado |
|---|---|
| servir a repetición exacta | parcialmente estructurable; preferencia entre candidatos, abierta |
| transformabilidad | filtrable por relación declarada; ranking perceptivo no apoyado |
| continuación | requiere forma/frase; actualmente cross-domain |
| flexibilidad armónica | investigable estructuralmente; facilidad perceptiva abierta |
| función de frase | depende de Form y contexto |
| memorabilidad / hook status | constructo insuficientemente definido; no usar como objetivo único |
| ajuste de estilo | genre-specific |
| calidad global | demasiado amplio; no es pregunta válida en esta forma |

## Composer Capability Check

El sistema actual sí puede razonar: “este candidato conserva el intervalo
declarado y entra en el rango previsto, por lo que es compatible con
transposición”. No puede afirmar: “este candidato es mejor que el alternativo
porque será más memorable”. La salida responsable conserva múltiples
alternativas, explicita el criterio utilizado y marca la preferencia humana
cuando sea el desempate.

## Integrated Tradeoffs

Conservar más información puede facilitar identidad estructural u operación,
pero restringir armonía o transformación. Conservar menos puede abrir
posibilidades, pero no garantiza continuidad perceptiva. La repetición puede
reforzar disponibilidad formal y también resultar mecánica. Un scaffold
armónico puede filtrar pitch y limitar reinterpretación. Un registro extremo
puede producir contraste o inviabilidad. Ninguno de estos intercambios tiene
ganador universal.

## Cross-Domain Dependencies

Form aporta función de frase, continuación, retorno, llegada y cierre. Rhythm /
Meter aporta pesos de onset, duración, acento y sincronización. Arrangement /
Production aporta timbre, mezcla, prominencia y realización. Lyrics / Prosody
puede reordenar restricciones melódicas. Genre limita la transferencia. La
modulación y el cambio de centro siguen dependiendo de `RQ-HAR-007`; no se
investigan aquí.

## Initial Harmonic Progression Gap

La nueva capacidad melódica hace más visible un hueco simétrico: desde objetivo
local + centro/colección el sistema puede enumerar apoyos y filtrar por
restricciones, pero no crea ni rankea generalmente una progresión armónica
inicial con estructura justificada. Este hueco es real, aunque aún debe
compararse con Form: no se investiga en esta integración.

## RQ-HAR-007 Dependency

La construcción y selección local dentro de un centro asumido no requieren
resolver modulación. Confirmar un nuevo centro, distinguir tonicización de
modulación fuera de marcos delimitados, elegir pivote y razonar retornos tras un
cambio de centro sí permanecen como dependencia de `RQ-HAR-007`. Su ausencia no
explica el primer fallo del pipeline local.

## Integrated Anti-Rules

| Anti-regla | Razonamiento seguro |
|---|---|
| `GOOD MOTIF = SHORT` / `FEW NOTES` | la extensión se declara y filtra por función; no hay tamaño universal |
| `ONE DISTINCTIVE LEAP CREATES IDENTITY` | un salto es una variable; su efecto depende de contexto y demás relaciones |
| `RHYTHM-FIRST IS BETTER` / `PITCH-FIRST IS BETTER` | elegir la representación por la invariante y objetivo, sin jerarquía universal |
| `REPETITION ESTABLISHES RECOGNITION AUTOMATICALLY` | puede presentar o reforzar; establecimiento perceptivo requiere escucha |
| `TRANSFORMABLE = DEVELOPABLE = BETTER` | manipulabilidad es propiedad operativa, no calidad ni desarrollo perceptivo |
| `GOAL DETERMINES SEED` | el objetivo condiciona restricciones; no selecciona una semilla única |
| `CONTOUR ALONE DEFINES IDENTITY` | puede contribuir, pero no es necesario ni suficiente |
| `INITIAL IDEA MUST ALREADY BE CLOSED` | el endpoint sigue contextual y 035 está diferido |

No se reitera aquí la lista anti-regla completa de los documentos de dominio.

## Unsupported / Deferred Knowledge

Siguen sin apoyo suficiente: tamaño óptimo, proporción de repetición, jerarquía
pitch-ritmo, receta de alturas, receta rítmica, endpoint universal,
memorabilidad, hook status, emoción por registro, desarrollo perceptivo,
selección armónica única y voicing mejor en general. `CAND-MEL-035/036` no se
integran como conocimiento positivo.

## Joint Manual Readiness

**YES, con alcance y sujeto a revisión metodológica.** Ahora existe un flujo
coherente enseñable desde objetivo → candidato inicial → invariantes →
transformación → selección armónica → realización, siempre que el manual
marque explícitamente los puntos sin ranking y no convierta heurísticas en
reglas. Esto no promueve material a `manual/`.

## Joint Rule Readiness

**NO** como conjunto de reglas compositivas. Sí hay subproductos aptos para
validación estructural futura: invariante retenida, relación interválica
preservada, pitch en rango y transformación aplicada conforme a especificación.
Una restricción comprobable por máquina no es una regla de composición ni
demuestra calidad.

## Highest-Leverage Next Research

| Dirección | Decisiones bloqueadas | Leverage | Riesgo | Juicio |
|---|---|---|---|---|
| FORM Foundations | función de frase, continuación, llegada, retorno, cierre | alto y transversal | medio; debe evitar “buena forma” | **mejor siguiente paso** |
| RHYTHM / METER Foundations | onset, acento, duración, sincronización, groove | alto local | alto si se reduce a energía/groove | segundo |
| RQ-HAR-007 — Modulation | nuevo centro, pivotes, retorno modulante | importante pero episódico | acumulación taxonómica | no primero |
| Initial harmonic progression | material armónico desde cero | alto y simétrico | objetivo aún poco delimitado | investigar después de precisar Form |
| Precise ranking research | elección comparativa | potencialmente alto | riesgo de “qué melodía es mejor” | no válido sin objetivo estrecho |
| Resolve MEL-035/036 | endpoint y dependencia armónica | posiblemente relevante | evidencia insuficiente y alcance incierto | no primero |

Form domina porque aporta la información de función que actualmente falta para
rankear continuación, cierre, retorno, final cambiado y reutilización. También
puede decir si la construcción desde cero debe servir a loop, frase o
progresión dirigida. Esta recomendación es una decisión de prioridad, no una
conclusión de que Form resolverá el ranking.

## Recommended Next Step

**Iniciar una investigación de `FORM Foundations`**, formulada alrededor de cómo
la función local (continuar, llegar, cerrar, retornar o contrastar) proporciona
criterios de selección para material melódico y armónico ya enumerado.

No iniciar esa investigación automáticamente en este documento. La pregunta
no debe ser “qué forma es buena”, sino qué información formal permite filtrar o
rankear decisiones concretas y bajo qué contextos.

## Questions for the Music/Methodology Director

No queda una pregunta bloqueante adicional para esta reintegración. La decisión
que requiere revisión externa es si se acepta `FORM Foundations` como la
siguiente dirección de investigación, con la formulación estrecha indicada, y
no como una búsqueda de “buena forma”.

## Final Report

### What I changed

Se creó únicamente esta integración v1. `melody-harmony-foundations-v0.md`,
los documentos fuente, candidatos, RQ, manuales, reglas, géneros,
experimentos y estado de verificación no fueron modificados.

### v0 → v1 capability delta

El sistema pasó de estar bloqueado ante la ausencia de material a poder
enumerar y filtrar candidatos melódicos iniciales con objetivo, representación,
invariantes y restricciones. El ranking continúa bloqueado.

### Core composer architecture

La secuencia útil es intención → construcción → invariantes → selección →
realización → timing/llegada → revisión, con iteración permitida y sin
confundir construcción, establecimiento y transformación.

### From-zero capability

`CAN ENUMERATE`: sí. `CAN FILTER`: sí, con alcance. `CAN RANK`: no de forma
general. El primer fallo general aparece al elegir entre candidatos compatibles.

### Goal-conditioned construction result

El objetivo posterior mejora la trazabilidad y la selección de restricciones;
no determina una semilla única.

### Seed representation result

Pitch, pitch class, intervalo, contorno, ritmo, duración y registro pueden
declararse separadamente según la invariante. No existe jerarquía universal.

### Construction vs establishment result

Una semilla puede ser construida antes de ser presentada o reconocida. La
recurrencia está disponible, pero no garantiza establecimiento perceptivo.

### Transformability result

Las relaciones pueden ser manipulables, preservables o transformables. Esto no
demuestra calidad, desarrollo ni identidad percibida.

### Melody → Harmony handoff

El candidato y sus invariantes permiten filtrar selecciones y realizaciones
armónicas, pero una melodía fija sigue subdeterminando la armonía y el voicing.

### From-zero-to-harmonized-candidate test

El pipeline completo puede enumerar, filtrar, realizar e inspeccionar. La
elección del candidato y luego la selección/realización preferidas siguen sin
ranking general.

### Main positive compositional capabilities

Declarar objetivos e invariantes, construir múltiples candidatos, preservar
relaciones para operaciones futuras, filtrar por restricciones y entregar una
semilla explícita a Melody/Harmony.

### Manipulable-but-unranked decisions

Extensión, alturas exactas, ritmo, registro, recurrencia, endpoint, selección
armónica, voicing, bajo, timing y llegada pueden manipularse o filtrarse, pero
no ordenarse universalmente para un objetivo artístico.

### Diagnostic vs generative power

El diagnóstico es alto en la mayoría de las interfaces; la generación es
media para la semilla y baja-media para selección, realización e interacción.
Llegada/cierre permanecen especialmente dependientes de dominios ausentes.

### Candidate coverage

Confirmados `CAND-MEL-001–036` y `CAND-HAR-001–052`. `CAND-MEL-018` permanece
`REJECTED`; `CAND-MEL-035/036` permanecen `DEFERRED / NOT AUDITABLE`, sin
readiness.

### What blocks ranking

Objetivo ausente, evidencia comparativa insuficiente, conflictos entre metas,
dependencia de estilo, dependencias cross-domain, medidas perceptivas faltantes
y preferencias artísticas explican el bloqueo.

### Initial harmonic progression gap

Ahora destaca como posible cuello de botella simétrico: construir y elegir una
progresión inicial desde objetivo + centro/colección sigue sin soporte fuerte.

### Cross-domain blockers

Form, ritmo/métrica, arreglo/producción, letra/prosodia y género aportan
variables que pueden cambiar el ranking. Modulación queda delimitada a
`RQ-HAR-007`.

### Joint manual readiness

**YES**, como workflow provisional con límites explícitos; no implica promoción
de conocimiento a `manual/`.

### Joint rule readiness

**NO** para reglas compositivas. Algunas validaciones estructurales podrían
formalizarse posteriormente, separadas del juicio musical.

### Highest-leverage next research comparison

Form ofrece el mejor leverage inmediato sobre función y objetivos; Rhythm/Meter
es segundo por timing; HAR-007 es más episódico; progresión armónica inicial es
un gap importante aún por delimitar; ranking sólo es válido con una pregunta
falsable y estrecha; 035/036 no deben adelantarse sin evidencia.

### Recommended next research step

**FORM Foundations**, centrada en cómo la función formal local puede aportar
criterios de filtro o ranking para decisiones de Melody + Harmony.
