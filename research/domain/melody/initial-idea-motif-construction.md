# Síntesis Melody — Construcción de la idea inicial y del motivo candidato

## Estado y pregunta

Esta síntesis corresponde a `RQ-MEL-009`. Es conocimiento candidato, no
manual ni regla aprobada. La pregunta no es qué hace buena a una melodía, sino
cómo especificar una primera unidad para tomar decisiones posteriores.

## Resultado ejecutivo

La construcción inicial puede tratarse como una selección condicionada por
objetivo de representación, relaciones internas, extensión, registro, ritmo,
silencios y comportamiento del final. El resultado principal es generativo sólo
en sentido limitado: permite enumerar y filtrar candidatos con restricciones
declaradas. No permite rankear una semilla como mejor, más memorable, más
catchy o de mayor calidad.

La unidad inicial no debe identificarse automáticamente con motivo, hook, tema,
frase o gesto. La identidad potencial y la aptitud para una operación posterior
son constructos distintos. Una recurrencia posterior puede establecer una
unidad en ciertos marcos; no es requisito universal de composición.

## Estructura → percepción → composición

La teoría y pedagogía de Schoenberg describen operaciones sobre material
motívico —repetición, derivación, reducción y transformación—; Caplin describe
la basic idea y su presentación dentro del estilo clásico. Los estudios de
reconocimiento de Dowling y trabajos relacionados muestran que contorno,
intervalos, altura/tone chroma y ritmo pueden contribuir según tarea y
condiciones. Ninguno de estos pasos autoriza la inferencia “usar X produce una
buena o memorable idea”.

La implicación compositiva más segura es declarar qué relación se quiere
conservar antes de la operación: pitch exacto, intervalo, contorno, ritmo,
registro o una combinación. La representación elegida determina qué se puede
transformar con claridad; no existe una representación primaria universal.

## Construcción, identidad y uso posterior

### Construcción

Se pueden enumerar candidatos pitch-first, rhythm-first o acoplados; también
semillas derivadas de centro/colección o de un scaffold armónico. El contexto
armónico facilita filtrar alturas, pero no es indispensable para enumerar una
idea y no resuelve la progresión inicial.

### Identidad

Contorno, ritmo, intervalo, registro y pitch absoluto son variables separables.
La evidencia existente impide declarar que cualquiera de ellas baste por sí
sola. La identidad puede estar distribuida y puede hacerse más clara por
recurrencia, sin confundirse con memorabilidad.

### Aptitud para operaciones

Una relación explícita puede ser manipulable: una célula interválica admite
transposición o secuencia; un punto de final identificable puede admitir cambio
de ending; una relación local puede admitir fragmentación. “Desarrollable” se
usa aquí operacionalmente, no como adjetivo de calidad.

## Hallazgos y anti-reglas

No hay soporte suficiente para un tamaño óptimo, 3–5 notas, dos compases,
inicio/final en tónica, predominio de pasos, un salto obligatorio, ritmo simple,
contorno suficiente, repetición interna necesaria, simetría=calidad,
syncopation=catchiness, rango estrecho=coherencia, chord tones=buena semilla o
hook=motivo fuerte. Estas afirmaciones pueden ser heurísticas locales en marcos
concretos, pero no principios generales del repositorio.

## Goal → seed constraint

| Objetivo | Restricción potencial | Límite |
|---|---|---|
| repetición | material y límites explícitos | no demuestra memorabilidad |
| cambio de final | núcleo y punto de salida distinguibles | no garantiza cierre |
| fragmentación | relación interna localizable | no hace mejor al material |
| transposición | intervalos separables de pitch absoluto | registro/tonalidad pueden cambiar el resultado |
| reharmonización | no fijar toda identidad a una función armónica | no garantiza ambigüedad perceptiva |
| loop | compatibilidad entre extremos | no implica hook |

## Potencia diagnóstica y generativa

Diagnóstica: media-alta para separar representación, invariantes, dependencia
armónica, intención de final y operación posterior. Generativa: parcial; puede
producir un candidato con justificación de restricciones, no justificar por qué
es mejor que alternativas sin definir un objetivo y una evaluación adecuados.

## Handoff a Melody + Harmony

Sin modificar el schema existente, la salida conceptual debe poder expresar:

`INITIAL MELODIC CANDIDATE` con `representation`, `exact_material`,
`intended_invariants`, `local_goal`, `later_operation_target`,
`center_or_collection`, `open_closed_intention` y `uncertainties`.

Esto mejora `CAN ENUMERATE` y `CAN FILTER` con alcance; `CAN RANK` permanece
bloqueado. El gap de construcción inicial queda **PARTIALLY ADVANCED**.

## Candidatos creados

- `CAND-MEL-031`: construcción condicionada por objetivo.
- `CAND-MEL-032`: representaciones separables sin jerarquía universal.
- `CAND-MEL-033`: construcción distinta de establecimiento por recurrencia.
- `CAND-MEL-034`: relaciones preservables para operaciones posteriores.
- `CAND-MEL-035`: diferido del conjunto material de auditoría; queda como gap sobre
  endpoint, continuación y cierre.
- `CAND-MEL-036`: diferido del conjunto material de auditoría; queda como gap
  sobre construcción melody-first frente a construcción harmony-constrained.

## Riesgos y preguntas abiertas

La transferencia entre tradiciones, la percepción de apertura/cierre, la
interacción pitch–ritmo, el peso relativo de invariantes y la facilidad real de
reharmonización siguen sin ranking. No se realizó experimento; `EXP-002` sigue
pausado. No se actualizan manuales, reglas, integraciones ni candidatos previos.

## Resultado de la auditoría de candidatos

La auditoría epistemológica del conjunto `CAND-MEL-031`–`034` está completada.
Los cuatro candidatos fueron revisados como material candidato y permanecen en
estado `candidate`, con resultado `REVISE` y readiness `POSSIBLE_WITH_SCOPE`.
No hay promoción a `manual/` ni `rules/`.

La construcción condicionada por objetivo queda limitada a una relación de
planificación: puede orientar qué hacer explícito para una operación posterior,
pero no determina la semilla ni permite rankearla. Las representaciones de
pitch, intervalo, contorno, ritmo y registro se mantienen separables para
describir invariantes, sin tratarlas como independientes ni establecer una
jerarquía. La construcción, la presentación/recurrencia y el establecimiento
perceptivo permanecen separados. Las relaciones transformables son
restricciones operativas, no indicadores de calidad, desarrollo o identidad
percibida.

## Direct-source verification and audit gate

Las tres fuentes nuevas fueron verificadas mediante páginas o copias
inspeccionables y sus límites se registraron. Sin embargo, los seis candidatos
combinan apoyo directo con inferencias metodológicas y no se ha realizado aún
la auditoría individual solicitada.

El triage de evidencia no constituye la auditoría epistemológica. `CAND-MEL-031`
–`034` tienen soporte directo suficiente para entrar en ella. `CAND-MEL-035` y
`036` no permanecen en el conjunto material de candidatos auditables.

`candidate_audit_evidence_gate: PASS`

`candidate_audit_status: COMPLETED` para el conjunto auditable 031–034. La
síntesis sigue siendo conocimiento candidato y no debe promoverse todavía a
conocimiento provisional, `manual/` ni `rules/`.

`CAND-MEL-035` y `CAND-MEL-036` siguen `DEFERRED / NOT AUDITABLE` por brecha de
evidencia directa. No reciben resultado epistemológico de esta auditoría y sus
IDs no se reutilizan.

## Final audit report

### Construction / identity / establishment corrections

La especificación inicial, la presentación o recurrencia formal y el eventual
reconocimiento perceptivo no son el mismo evento. La repetición puede ser una
estrategia de establecimiento en marcos acotados, pero no es requisito universal
ni sinónimo de memorabilidad.

### Goal-conditioned-construction corrections

El resultado defendible es `goal-conditioned`, no `goal-determined`: declarar
una operación posterior puede orientar la selección de relaciones e invariantes,
pero no identifica una semilla óptima.

### Representation corrections

Las representaciones separables permiten hacer explícito qué se conserva o
modifica. La evidencia perceptiva de Dowling se mantiene ligada a sus tareas y
no se convierte en preferencia compositiva ni en independencia de variables.

### Transformability / developability corrections

Se usa `manipulable`, `transformable` o `preservable relation` para operaciones
concretas. No se usa `developability` como sinónimo de calidad, desarrollo o
reconocimiento.

### Major epistemic corrections

La cadena estructura → percepción → composición no se cierra automáticamente:
cada puente debe conservar su evidencia y alcance. La síntesis permite
enumerar y filtrar con alcance; el ranking continúa bloqueado.

### Cross-candidate consistency

031 no convierte transformación en desarrollo; 032 no establece jerarquía
pitch–ritmo; 033 no hace necesaria la repetición; 034 no predice calidad ni
identidad. Los cuatro son compatibles con la integración existente, que sigue
separando generación/filtro de ranking.

### Source limitations preserved

Schoenberg y Caplin respaldan marcos pedagógicos o formales acotados; Dowling
respalda tareas de reconocimiento, no construcción desde cero ni calidad. No
se reabrió el triage de evidencia ni se creó un experimento.

### Promotion-readiness recommendations

- `STRONG_CANDIDATE`: ninguno.
- `POSSIBLE_WITH_SCOPE`: CAND-MEL-031, CAND-MEL-032, CAND-MEL-033, CAND-MEL-034.
- `NOT_READY`: ninguno del conjunto auditable.
- `REJECTED`: ninguno.
- `DEFERRED / NOT AUDITABLE`: CAND-MEL-035, CAND-MEL-036.

### Initial-idea gap status

**MATERIALLY ADVANCED**: ahora se puede describir construcción condicionada,
representación, separación entre establecimiento y construcción, y relaciones
operativas; no se puede rankear ni validar calidad perceptiva general.

### From-zero capability

`CAN ENUMERATE`: mejorada. `CAN FILTER`: mejorada con alcance. `CAN RANK`:
bloqueada.

### Ready to update Melody + Harmony integration

**YES**.

### Recommended next step

`Update the joint Melody + Harmony integration with the audited initial-idea
findings before selecting the next research domain.`
