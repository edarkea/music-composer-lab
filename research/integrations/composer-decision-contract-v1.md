# Composer Decision Contract v1

## A. Purpose

Este documento define el contrato mínimo para convertir una intención
compositiva en una decisión musical trazable y transferible a un `SongPlan`.
Es una arquitectura de decisión, no un manual, una regla, un genre pack ni un
esquema de software.

El contrato obliga a separar:

`INTENCIÓN → CONTEXTO → PREGUNTA → OPCIONES → FILTRO → RANKING ACOTADO,
SI EXISTE → PREFERENCIA / TRADEOFF → DECISIÓN → FUNCIÓN ESPERADA →
DEPENDENCIAS → SongPlan → TRAZA`

El contrato no presupone que exista una mejor opción musical global.

## B. Definitions

### Composition decision

Una elección explícita entre alternativas musicales, o una declaración
explícita de que no se puede elegir todavía. Toda decisión debe responder qué
se intenta lograr, qué puede cambiar el compositor, qué opciones sobreviven,
qué conocimiento se aplica y qué parte queda a la preferencia artística.

### Scope

El alcance de validez de una afirmación: tradición, género, nivel temporal,
representación, contexto, objetivo, criterio y condiciones relevantes. Una
afirmación fuera de su alcance no puede reutilizarse como evidencia.

### Evidence basis

La base epistemológica de un filtro o comparación. Debe conservar la clase de
conocimiento y sus fuentes o referencias internas. `candidate`, `provisional`,
`genre-specific` y `diagnostic` no se convierten silenciosamente en
conocimiento aprobado.

### Expected effect

Una consecuencia esperada, siempre marcada como estructural, perceptiva o
compositiva. Un hecho estructural no prueba por sí solo un efecto perceptivo ni
una recomendación compositiva.

## C. Decision capability levels

Estos niveles describen capacidad disponible para la decisión concreta, no
calidad musical global:

| Nivel | Significado | Qué no permite afirmar |
|---|---|---|
| `ENUMERATE` | Presentar alternativas musicalmente plausibles | Que alguna sea preferible |
| `FILTER` | Retener o descartar opciones mediante restricciones o criterios explícitos | Que una superviviente sea la mejor |
| `RANK-1` | Preferir A sobre B en un criterio, objetivo y alcance definidos | Un ranking global o multiobjetivo |
| `RANK-2` | Resolver varios criterios mediante un procedimiento justificado | Que el procedimiento sea universal |

`RANK-2` no se presume disponible. El estado actual del proyecto contiene al
menos un ranking local acotado, pero no un método general de tradeoff.

## D. Minimal decision contract

El registro mínimo debe conservar estos conceptos. Los nombres no son un
schema obligatorio:

| Concepto | Pregunta que responde |
|---|---|
| `decision_id` + `level` | ¿Qué decisión es y en qué escala ocurre? |
| `domain` + `question` | ¿Qué dimensión musical se decide y cuál es la pregunta? |
| `intent` + `goal` | ¿Qué intención y objetivo compositivo la motivan? |
| `scope` + `context` | ¿Dónde y bajo qué condiciones se aplica? |
| `options` | ¿Qué alternativas concretas se consideran? |
| `constraints` | ¿Qué debe cumplirse y qué criterios son blandos? |
| `capability` + `actionability` | ¿Puede enumerar, filtrar, rankear o solo diagnosticar? |
| `evidence` | ¿Qué conocimiento respalda el filtro o ranking? |
| `active_criterion` | ¿En qué criterio se compara, si procede? |
| `selection` + `basis` | ¿Qué se eligió y por qué base? |
| `preference` + `uncertainty` | ¿Qué decidió artísticamente el usuario y qué permanece abierto? |
| `role` + `dependencies` | ¿Qué papel se espera y qué otros dominios afecta? |
| `handoff` + `trace` | ¿Qué pasa a SongPlan y cómo se reconstruye la decisión? |

Un registro puede combinar conceptos cuando no se pierde la distinción. No
debe añadir campos administrativos para aparentar precisión.

### Decision levels

La jerarquía mínima para una canción completa es:

1. `SONG`: intención global, trayectoria y restricciones generales.
2. `SECTION`: función, contraste, continuidad, densidad y roles por sección.
3. `UNIT`: frase, motivo, patrón o unidad equivalente.
4. `LOCAL_EVENT`: evento puntual de altura, duración, acorde, entrada, salida,
   registro o textura.
5. `RELATIONSHIP`: relación entre unidades, como repetición, variación,
   transformación, retorno o contraste.

No se exige recorrerlos en orden fijo. `RELATIONSHIP` es un nivel transversal,
no un paso final obligatorio.

## E. Selection and ranking semantics

El proceso operativo mínimo es:

1. declarar intención, objetivo y pregunta;
2. declarar contexto y alcance;
3. enumerar alternativas reales;
4. aplicar restricciones duras;
5. aplicar filtros sustentados y registrar descartes;
6. declarar el criterio activo;
7. aplicar `RANK-1` solo si la evidencia compara opciones compatibles;
8. registrar criterios en conflicto;
9. resolver el compromiso mediante preferencia, género, necesidad estructural
   o una regla de decisión justificada;
10. seleccionar, documentar consecuencias y transferir a SongPlan.

Bases de selección permitidas:

- `EVIDENCE-BASED FILTER`
- `EVIDENCE-BASED LOCAL RANK`
- `ARTISTIC PREFERENCE`
- `GENRE PRIORITY`
- `STRUCTURAL NECESSITY`
- `CROSS-DOMAIN CONSTRAINT`
- `DEFAULT / TIE-BREAK`

`chosen because it sounds better` solo es válido si se registra como juicio
artístico del responsable de la decisión, no como evidencia.

## F. Artistic preference

La preferencia artística es una salida legítima del contrato cuando varias
opciones aceptables sobreviven, los criterios entran en conflicto, la decisión
es estilística o la evidencia no permite ranking global.

Debe indicar al menos:

- qué prioridad activa: continuidad, contraste, apertura, retorno, novedad,
  densidad u otra intención declarada;
- quién o qué intención la establece;
- qué alternativa favorece;
- qué criterio acepta sacrificar, si corresponde;
- si la elección es provisional o un compromiso artístico.

La preferencia puede escoger una opción que no sea localmente superior en un
criterio. Eso no contradice `RANK-1`: significa que el criterio local no es el
único objetivo compositivo.

## G. Uncertainty behavior

| Situación | Comportamiento obligatorio |
|---|---|
| Solo `ENUMERATE` | Declarar que no hay filtro sustentado; presentar opciones y solicitar o aplicar prioridad artística |
| `FILTER` sin ranking | Conservar supervivientes; no inventar orden; elegir mediante preferencia o tie-break declarado |
| Criterios en conflicto | Exponer el conflicto y la prioridad; no producir score compuesto no justificado |
| Género ausente | Aplicar solo conocimiento general dentro de alcance; marcar la realización estilística como abierta |
| Consecuencia cross-domain no resuelta | Registrar dependencia y mantener alternativas o activar revisión |
| Evidencia diagnóstica | Usarla para describir o advertir, nunca para elegir directamente |
| Conocimiento fuera de alcance | Declarar límite; no transferir la afirmación; bloquear o pedir una decisión explícita |
| Sin conocimiento adecuado | Estado `BLOCKED`; no rellenar el vacío con una regla inventada |

La secuencia por defecto es:

`DECLARAR LÍMITE → MOSTRAR OPCIONES → PEDIR/APLICAR PRIORIDAD → ELEGIR SIN
FALSA AFIRMACIÓN DE EVIDENCIA`.

## H. Structure → perception → composition

Cuando una decisión usa una consecuencia perceptiva, la traza debe contener
tres capas separadas:

```text
STRUCTURE: operación o rasgo musical controlable
PERCEPTION: consecuencia posible, medida o hipótesis con alcance
COMPOSITION: por qué esa consecuencia sirve al objetivo actual
```

Ejemplo estructural hipotético, sin convertirlo en regla:

```text
STRUCTURE: aumentar la separación registral entre dos secciones
PERCEPTION: puede favorecer diferenciación perceptiva bajo el alcance indicado
COMPOSITION: se elige porque la intención prioriza contraste seccional
```

Si la capa perceptiva no está sustentada, debe decir `hypothesis` o
`diagnostic`; la decisión puede seguir siendo una preferencia artística, pero
no una deducción automática.

## I. Cross-domain dependencies

Las dependencias se registran por relación, no por una secuencia universal de
dominios:

- `PREREQUISITE`: una decisión necesita otra información previa;
- `CONSTRAINT`: una decisión limita opciones posteriores;
- `CO-DEVELOPMENT`: dos decisiones se construyen conjuntamente;
- `REVISION_TRIGGER`: una decisión posterior puede reabrir la anterior.

Ejemplos de interfaz:

| Decisión | Dependencia posible |
|---|---|
| Forma | limita duraciones y funciones disponibles por sección (`CONSTRAINT`) |
| Rango melódico | limita registro y espacio de textura (`CONSTRAINT`) |
| Identidad del hook | condiciona cuánto puede cambiar el desarrollo (`CONSTRAINT`) |
| Ritmo armónico | condiciona densidad de eventos melódicos (`CONSTRAINT`) |
| Jerarquía focal | condiciona densidad del acompañamiento (`CONSTRAINT`) |
| Textura posterior | puede obligar a revisar el registro melódico (`REVISION_TRIGGER`) |

No se impone `armonía → melodía → ritmo`. El contrato permite relaciones
iterativas y decisiones co-desarrolladas.

## J. Revision mechanism

Una decisión puede reabrirse solo mediante un registro de revisión que indique:

1. `reopened_decision`: identificador y versión anterior;
2. `trigger`: conflicto o nueva restricción concreta;
3. `affected_domain`: qué decisión posterior produjo el problema;
4. `changed_context_or_constraint`: qué cambió;
5. `new_options_or_selection`: alternativas revisadas;
6. `decision_basis`: nueva preferencia, filtro o evidencia;
7. `downstream_impact`: qué otros registros deben revisarse.

La revisión no es un bucle de optimización ilimitado. Se detiene cuando se
resuelve el conflicto dentro del alcance, se declara un compromiso artístico o
la decisión pasa a `BLOCKED`.

## K. Genre interface

El género entra como especialización declarada, nunca como sustituto del
conocimiento general:

```text
GENERAL COMPOSITION KNOWLEDGE
+ GENRE SPECIALIZATION
+ ARTISTIC INTENT
→ CONCRETE DECISION
```

El registro debe indicar si la influencia del género funciona como:

- prioridad;
- restricción;
- ponderación de opciones;
- evitación;
- preferencia de realización.

También debe conservar el alcance del repertorio y separar `GENRE OBSERVATION`
de `COMPOSITION HEURISTIC`. En esta unidad no se crea ni se congela ningún
genre pack.

## L. SongPlan interface

El contrato no rediseña SongPlan. Define qué debe salir de la capa de decisión:

| Tipo de información | Destino |
|---|---|
| Material elegido, forma, secciones, roles, timing, registro y restricciones operativas | Campos directos de SongPlan, cuando el formato existente los admita |
| Dependencias, invariantes, límites de realización y condiciones por sección | Restricciones o instrucciones para la generación posterior |
| Objetivo, alternativas descartadas, evidencia, alcance, preferencia, incertidumbre y revisiones | Metadatos de traza, referencias externas o registro de decisión |

La salida debe ser suficientemente concreta para materializar la canción, pero
no debe serializar como hecho una justificación que solo era hipótesis o
preferencia. `Composition knowledge != SongPlan serialization`.

## M. Decision trace

La traza debe permitir responder:

- ¿Cuál era el objetivo?
- ¿Qué criterio estaba activo?
- ¿Qué opciones fueron consideradas y filtradas?
- ¿Qué alcance y base de conocimiento se usaron?
- ¿Se aplicó una preferencia artística?
- ¿Qué incertidumbre permanecía?
- ¿Qué consecuencia cross-domain se aceptó?
- ¿Por qué se reabrió o mantuvo una decisión?

La justificación debe registrarse en el momento de decidir. No se permite
inventar una razón post hoc.

## N. Worked structural examples

Los siguientes ejemplos validan la forma del contrato; no promueven claims ni
introducen reglas compositivas.

### Melody — variation choice

`UNIT / melody`: objetivo = conservar una relación declarada y explorar cambio;
opciones = repetición, final cambiado, transformación específica; capacidad =
`FILTER`; selección = preferencia artística; incertidumbre = el efecto sobre
calidad o continuidad percibida no está garantizado.

### Harmony — support choice

`SECTION / harmony`: objetivo = sostener una sección abierta; opciones = varias
organizaciones armónicas dentro del marco declarado; capacidad = `ENUMERATE` +
`FILTER`; selección = `ARTISTIC PREFERENCE` o `GENRE PRIORITY`; no se afirma que
una etiqueta armónica produzca apertura automáticamente.

### Rhythm — event placement

`LOCAL_EVENT / rhythm`: objetivo = decidir posición de un evento; opciones =
posiciones compatibles con metro y timing; capacidad = `FILTER`; selección =
preferencia o necesidad de coordinación con melodía; el diagnóstico temporal no
se transforma por sí solo en ranking.

### Form — sectional role

`SECTION / form`: objetivo = declarar `continuation`, `arrival`, `openness` o
`return`; opciones = operaciones compatibles; capacidad = `FILTER` con escala y
contexto; selección = preferencia si sobreviven varias. La función no determina
un medio único.

### Development — preserved relation

`RELATIONSHIP / development`: objetivo = desarrollar sin perder la relación
declarada; opciones = repetición, fragmentación, extensión o cambio parcial;
capacidad = `ENUMERATE` + `FILTER`; la percepción de continuidad queda marcada
como dependiente del contexto.

### Tension — diagnostic use

`SECTION / tension`: objetivo = describir contribuyentes que se desean mantener
o retirar; capacidad = `DIAGNOSTIC ONLY`; la traza puede informar, pero la
elección requiere intención y preferencia explícitas.

### Hooks — prominence choice

`RELATIONSHIP / hooks`: objetivo = declarar material focal; opciones = varios
materiales recurrentes; capacidad = `ENUMERATE`; selección = preferencia
artística; hook, prominence y memorability permanecen separados.

### Texture — revision trigger

`SECTION / texture`: objetivo = asignar capas y jerarquía focal; una nueva
densidad o registro puede activar `REVISION_TRIGGER` sobre una decisión
melódica. El contrato conserva la relación sin afirmar un efecto universal.

## O. Success-case validation

| Caso | Representación |
|---|---|
| 1. Filtra pero no rankea | `FILTER` + supervivientes + `ARTISTIC PREFERENCE` |
| 2. A > B en un criterio | `RANK-1` + objetivo, criterio y alcance explícitos |
| 3. Criterios en conflicto | criterios separados + prioridad declarada + tradeoff |
| 4. Género recomienda una realización | `GENRE PRIORITY` o `GENRE REALIZATION PREFERENCE`, sin reemplazar lo general |
| 5. Intención elige una opción no superior localmente | `ARTISTIC PREFERENCE` + criterio sacrificado + motivo explícito |
| 6. Textura fuerza revisión melódica | `REVISION_TRIGGER` + conflicto + versión nueva |
| 7. Conocimiento diagnóstico | `DIAGNOSTIC ONLY` sin selección automática |
| 8. Sin conocimiento adecuado | `BLOCKED` + límite declarado + decisión pendiente |

**Validación: 8 / 8 casos representables.**

## P. Boundaries / non-claims

- No existe un ranking general de calidad compositiva.
- `RANK-1` no equivale a “mejor canción”.
- No se crea un score multiobjetivo ni un `RANK-2` ficticio.
- La estructura no implica automáticamente percepción ni recomendación.
- Las observaciones de género no son leyes generales.
- La preferencia artística no se presenta como evidencia científica.
- El contrato no promueve candidatos, escribe manuales ni crea reglas.
- No se congela una forma concreta: la instancia de forma se difiere a una
  unidad posterior salvo aprobación explícita.
- No se diseña ni ejecuta un experimento en esta unidad.
- No se modifica SongPlan, `music-engine`, código, EXP-003 ni metodología.

## Q. Requirements for Unit 2

La siguiente unidad debe poblar este contrato con un subconjunto pequeño y
revisado de conocimiento existente. Para cada entrada debe conservarse:

1. estado epistemológico y alcance;
2. dominio y variable compositiva;
3. operación o alternativas que realmente permite enumerar;
4. filtro permitido, si existe;
5. `RANK-1` únicamente si la comparación y el criterio son compatibles;
6. límites de transferencia estructura→percepción→composición;
7. dependencias cross-domain;
8. tratamiento de incertidumbre y preferencia;
9. destino SongPlan, si corresponde;
10. trazabilidad a la fuente o al candidato revisado.

Unit 2 no debe interpretar la existencia de este contrato como aprobación
automática del contenido que lo poblará.

## Estado de esta unidad

**DECISION CONTRACT READY FOR KNOWLEDGE POPULATION**

Conocimiento promovido: ninguno. Nueva investigación: ninguna. Experimentos:
ninguno. Código: ninguno.
