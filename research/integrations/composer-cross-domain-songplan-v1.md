# Composer Cross-Domain SongPlan v1

## A. Purpose

Este documento integra `composer-decision-contract-v1.md`,
`composer-knowledge-v1.md` y `composer-genre-pack-v1.md` en un flujo
prospectivo completo para una canción MVP de indie-dance, limitado a una
realización loop/groove-based de electrónica-pop.

No compone la primera canción, no crea una forma definitiva, no modifica
SongPlan ni `music-engine` y no introduce conocimiento nuevo. Define cómo las
decisiones musicales llegan a un SongPlan válido sin pedirle al motor que elija
la música.

El motor actual es **Case A — exact specification**: valida y materializa
eventos explícitos, pero no genera notas desde estilo, energía, emoción,
tonalidad, modo o símbolos de acorde.

## B. Artistic input contract

### Required artistic input

Antes de comenzar, el Project Owner debe proporcionar:

1. intención funcional o carácter deseado;
2. prioridad principal entre continuidad, contraste, novedad, apertura,
   retorno u otra meta explícita;
3. aprobación de una de las dos familias de forma disponibles, o autorización
   para que el compositor elija mediante una prioridad declarada;
4. foco material inicial: melodía, patrón rítmico, marco armónico o combinación
   explícita;
5. grado deseado de persistencia frente a cambio;
6. restricciones artísticas que no deben violarse.

### Optional artistic input

- trayectoria de densidad o registro;
- carácter armónico/melódico preferido;
- preferencia por ciclo persistente o secciones contrastantes;
- prioridad de hook/foco;
- duración o escala formal aproximada;
- realizaciones tímbricas compatibles con el pack.

### Composer may choose

El compositor puede enumerar y filtrar alternativas de seed, representación,
colocación métrica, realización armónica y capas cuando no se haya fijado una
preferencia. Puede aplicar el único `RANK-1` existente solo si el objetivo es
recognition bajo su alcance exacto. En lo demás debe entregar opciones y usar
preferencia artística o un default declarado.

## C. Song-level decision architecture

El flujo mínimo contiene ocho nodos. No son una secuencia universal de dominios;
son puntos de decisión y dependencia.

### N0 — Intent and scope

- **Pregunta:** ¿qué debe intentar hacer la canción y dentro de qué alcance?
- **Dominios:** song-level.
- **Predecesores:** ninguno.
- **Capacidad:** `ENUMERATE`, `FILTER`.
- **Salida:** objetivo, prioridad, alcance, restricciones y criterios activos.
- **Restricción downstream:** todas las decisiones deben poder justificar su
  relación con esta intención.
- **SongPlan:** `name`, `tempo`, `time_signature`, `tonic`, `mode`, `style` solo
  cuando el valor ya haya sido decidido; son valores de serialización y
  metadatos, no generadores musicales.

### N1 — Form and trajectory

- **Pregunta:** ¿qué organización formal mínima sirve a la intención?
- **Dominios:** form/song-level.
- **Predecesores:** N0.
- **Opciones:** ciclo persistente con diferenciación de capas; secciones
  contrastantes sobre marco loop-based.
- **Capacidad:** `ENUMERATE`, `FILTER`; sin ranking.
- **Decisión:** `ARTISTIC PRIORITY` si ambas opciones sobreviven.
- **Salida:** secciones, funciones, recurrencias, fronteras y trayectoria de
  continuidad/cambio.
- **Restricción downstream:** asigna objetivos y rangos temporales, no notas.
- **SongPlan:** `arrangement.sections` con `id`, `start_bar`, `bar_count` y
  energía técnica ya decidida.

### N2 — Identity / focal bundle

- **Pregunta:** ¿qué material debe ser identificable, focal y recurrente?
- **Dominios:** melody, rhythm, hooks.
- **Predecesores:** N0; N1 aporta función y escala.
- **Capacidad:** `ENUMERATE`, `FILTER`; `RANK-1` únicamente para recognition
  bajo CK-CROSS-01.
- **Salida:** material explícito, representación/invariante, rol focal,
  recurrencias y cambios permitidos.
- **Restricción downstream:** desarrollo, densidad de acompañamiento y
  registro deben respetar la identidad y el foco declarados.
- **SongPlan:** motivos explícitos, eventos con pitch/onset/duración y
  `section_assignments`; hook/prominence y rationale permanecen en traza.

### N3 — Groove / harmony bundle

- **Pregunta:** ¿qué marco métrico-rítmico y armónico sostiene las unidades?
- **Dominios:** rhythm/meter, harmony, melody-harmony.
- **Predecesores:** N1 y N2; co-desarrollo permitido.
- **Capacidad:** `ENUMERATE`, `FILTER`; sin `RANK-2`.
- **Salida:** metro, colocaciones, seed/ciclo, selección armónica y
  realizaciones explícitas.
- **Restricción downstream:** compatibilidad con eventos melódicos, registro,
  densidad y textura.
- **SongPlan:** `time_signature`, eventos pitched explícitos, `harmony_assignments`
  como metadato y voicings/bajo como pitches reales en tracks.

### N4 — Section-role / texture bundle

- **Pregunta:** ¿qué capas son focales y cómo cambia la realización por sección?
- **Dominios:** form, texture/arrangement, density, register.
- **Predecesores:** N1, N2 y N3.
- **Capacidad:** `ENUMERATE`, `FILTER`; diagnóstico para conflictos.
- **Salida:** capa focal, apoyo, densidad relativa, entradas/salidas y
  asignación registral.
- **Restricción downstream:** el acompañamiento no debe competir con el foco
  declarado; el cambio de textura puede activar revisión de melodía.
- **SongPlan:** tracks, roles, motifs, `section_assignments`, eventos y
  `sound_intent` cuando sea un valor ya decidido.

### N5 — Recurrence / development bundle

- **Pregunta:** ¿qué permanece, qué cambia, por qué y en qué recurrencia?
- **Dominios:** development, melody, harmony, rhythm, texture.
- **Predecesores:** N2 y N4; N3 puede limitar operaciones.
- **Capacidad:** `ENUMERATE`, `FILTER`; transformaciones del motor solo cuando
  estén explícitamente decididas y soportadas.
- **Salida:** relación preservada, dimensión modificada, ubicación y motivo de
  la variación.
- **Restricción downstream:** no superar silenciosamente la identidad tolerada;
  cualquier conflicto reabre el mínimo nodo afectado.
- **SongPlan:** reuso de motifs, assignments y variaciones documentadas;
  `transpose`, `octave_shift`, `rhythmic_displacement`, `truncate`,
  `retrograde`, `augment`, `diminish` o `invert` solo según el contrato real.

### N6 — Contrast / tension / closure bundle

- **Pregunta:** ¿qué dimensiones se coordinan para contraste, tensión, apertura,
  llegada o cierre?
- **Dominios:** form, texture, harmony, rhythm, melody, tension.
- **Predecesores:** N1, N3, N4 y N5.
- **Capacidad:** `FILTER` y `DIAGNOSTIC ONLY` según el claim; sin scalar ni
  ranking universal.
- **Salida:** estados separados de `arrival`, `closure`, `boundary`, `return`,
  dimensiones de tensión y decisiones de capas/densidad/armonía.
- **Restricción downstream:** no inferir cierre desde tónica, parada, descenso,
  densidad o registro aislados.
- **SongPlan:** secciones, eventos, entradas/salidas y material explícito;
  estados perceptivos y límites quedan en traza.

### N7 — Conflict resolution and SongPlan handoff

- **Pregunta:** ¿todas las decisiones están resueltas o declaradas como
  preferencia/default acotado antes de serializar?
- **Dominios:** cross-domain/song-level.
- **Predecesores:** N0–N6.
- **Capacidad:** `FILTER`; `RANK-1` solo si continúa dentro de su alcance.
- **Salida:** decisión final, restricciones, versión de cada decisión, traza y
  handoff.
- **Restricción downstream:** no serializar valores musicales arbitrarios ni
  pedir al motor que los invente.
- **SongPlan:** plan V2 completo y conforme al contrato; rationale, evidencia,
  preferencia y revisiones se conservan fuera del plan como traza vinculada.

## D. Cross-domain dependency graph

```text
N0 INTENT / SCOPE
 ├──> N1 FORM / TRAJECTORY
 │     └──> N4 SECTION-ROLE / TEXTURE
 │             └──> N6 CONTRAST / TENSION / CLOSURE
 └──> N2 IDENTITY / FOCAL
        ↔ N3 GROOVE / HARMONY
        └──> N5 RECURRENCE / DEVELOPMENT
N3 ↔ N4
N4 --REVISION_TRIGGER--> N2 or N5 when register/density competes with focus
N0–N6 ──> N7 CONFLICT RESOLUTION / SONGPLAN HANDOFF
```

Relaciones explícitas:

1. N1 → N4: `CONSTRAINT`, función y escala limitan la realización seccional.
2. N2 ↔ N3: `CO-DEVELOPMENT`, identidad melódica/rítmica y soporte armónico.
3. N2 → N5: `PREREQUISITE`, la relación preservada precede a la variación.
4. N3 → N4: `CONSTRAINT`, densidad y registro armónicos afectan textura.
5. N4 → N2: `REVISION TRIGGER`, textura puede competir con rango/foco.
6. N4 → N5: `CONSTRAINT`, capas y densidad condicionan la realización.
7. N5 → N6: `DEPENDENT`, recurrencias cambian estados de contraste/apertura.
8. N6 → N1: `REVISION TRIGGER`, una frontera inviable puede reabrir la función.
9. N7 revisa cualquier nodo, pero solo el mínimo necesario.

No se impone un orden universal `forma → armonía → melodía → ritmo`.

## E. Decision bundles

### 1. Identity bundle

Material melódico/rítmico explícito, relación preservada, foco/hook como rol y
expectativa de recurrencia. `HOOK != PROMINENCE != MEMORABILITY`.

### 2. Groove/harmony bundle

Metro, colocación, ciclo armónico, selección y realización. Símbolos de acorde
no sustituyen pitches explícitos.

### 3. Section-role bundle

Función formal, foco, capas, densidad, registro y contraste. El pack prioriza
el cambio cross-domain, no una elevación registral obligatoria.

### 4. Development bundle

Invariante, cambio, ubicación y razón de la recurrencia. La variación es una
decisión, no una obligación de evitar repetición.

## F. Conflict and revision protocol

Ante un conflicto:

`DETECT → IDENTIFY AFFECTED DECISIONS → CLASSIFY PRIORITY → REOPEN MINIMUM →
RE-FILTER → ARTISTIC PRIORITY IF NEEDED → RECORD REVISION`.

La prioridad se clasifica en este orden contextual, no como ley musical:

1. `HARD CONSTRAINT` de formato, representación o intención explícita;
2. dependencia cross-domain necesaria;
3. `GENRE PRIORITY` o `SOFT FILTER`;
4. `ARTISTIC PRIORITY`;
5. `DEFAULT / TIE-BREAK` declarado.

Solo se reabre una decisión si se viola una restricción dura, una dependencia
necesaria se vuelve imposible, un guardrail señala incompatibilidad seria o el
Project Owner cambia la intención. Se conserva la versión anterior, el
disparador, el cambio y el impacto downstream. No hay optimización global ni
bucle ilimitado.

## G. General + genre + artistic layering

Cada decisión integrada debe mostrar tres líneas:

```text
GENERAL: qué permite o restringe el conocimiento general
GENRE: qué prioriza o hace disponible el pack indie-dance acotado
ARTISTIC: qué elige esta canción y qué tradeoff acepta
```

Ejemplo estructural permitido: el conocimiento general permite repetición y
variación; el pack hace disponible sostener un loop y cambiar capas; la
intención elige conservar la melodía y aumentar contraste tímbrico. Esto no
afirma que el cambio produzca interés o energía.

## H. Complete-song coverage matrix

| Necesidad MVP | Nodo/bundle | Resultado permitido |
|---|---|---|
| Intención song-level | N0 | resuelta o preferencia |
| Forma global | N1 | una de dos opciones o elección artística |
| Roles de sección | N1/N4 | funciones y estados declarados |
| Contraste/continuidad | N4/N6 | haz de parámetros + escucha posterior |
| Identidad temática | N2 | relación/invariante explícita |
| Repetición/variación | N2/N5 | opciones y elección trazable |
| Desarrollo | N5 | operación y dimensión cambiada |
| Marco armónico | N3 | seed/ciclo/organización explícitos |
| Realización armónica | N3 | voicing/bajo/pitches explícitos |
| Ritmo/métrica | N3 | posiciones y duraciones explícitas |
| Apertura/cierre | N6 | estados separados, no inferencia automática |
| Hook/foco | N2/N4 | recurrencia y jerarquía sin claim de memorabilidad |
| Textura | N4 | capas, foco, densidad y registro mínimos |
| Tensión/release | N6 | dimensiones coordinadas, sin scalar |
| Dependencias cross-domain | D | constraints y co-development visibles |
| Revisión | F | reapertura local y versionada |

**Complete-song needs covered: 16 / 16.**

## I. SongPlan mapping

La integración usa exclusivamente campos y estructuras verificadas de
SongPlanV2, `schema_version: "2.0"`.

### Direct SongPlan values — 7

1. identidad nominal del plan y metadatos root ya decididos;
2. tempo y compás;
3. tonic y mode como metadatos ya resueltos;
4. style como etiqueta descriptiva ya elegida;
5. secciones con rangos de compases y energía ya decidida;
6. tracks, roles, motifs y asignaciones;
7. eventos explícitos: pitches, bar, beat, duration, velocity y campos válidos.

### Indirect / pre-serialization mappings — 7

1. intención y prioridad → decisiones concretas antes de serializar;
2. función y contraste → secciones, assignments y eventos coordinados;
3. identidad → motif explícito y reutilización;
4. desarrollo → variation soportada sobre motif;
5. realización armónica → eventos pitched, no solo harmony label;
6. jerarquía focal → roles, capas y densidad de tracks;
7. restricciones cross-domain → filtros previos y registro de handoff.

### Trace-only decisions — 5

1. evidencia, clase epistemológica y alcance;
2. criterio activo y resultado de filtro/ranking;
3. preferencia artística y tradeoff;
4. incertidumbre y claims structure→perception→composition;
5. motivo de revisión y decisiones descartadas.

### Not representable as musical generation in current SongPlan

El rationale, la evidencia y la preferencia no son campos musicales del plan,
pero sí pueden conservarse en una traza externa. No existe un gap de
representación P0 para materializar una canción: todos los valores musicales
necesarios pueden llegar como eventos, tracks, motifs, assignments y secciones
explícitos.

**True SongPlan representation gaps: 0.**

## J. SongPlan representation-gap policy

Si una decisión no tiene campo propio:

1. convertirla primero en restricción de generación;
2. resolverla antes de serializar;
3. representar su consecuencia musical mediante estructuras existentes;
4. conservar la razón en la traza;
5. proponer cambio de schema solo si la consecuencia no puede materializarse.

No se propone cambio de schema en Unit 4.

## K. Defaults audit

| Default | Clasificación | Regla |
|---|---|---|
| `schema_version: "2.0"` | TECHNICAL DEFAULT | no es una decisión musical |
| conversión beat/duration y ticks | TECHNICAL DEFAULT | usa contrato del motor; no cambia intención |
| orden determinista de eventos/MIDI | TECHNICAL DEFAULT | no es criterio compositivo |
| `mode: ionian` para mayor diatónico en runtime verificado | TECHNICAL REPRESENTATION DEFAULT | se registra como compatibilidad del runtime |
| selección de centro, tempo, registro, densidad o voicing | MUSICAL DEFAULT | no puede rellenarse silenciosamente |
| persistencia de loop | GENRE DEFAULT candidate | solo si el pack y la intención lo aceptan |
| cambio por capas en vez de melodía | GENRE PRIORITY | opción acotada, no requisito |
| valor de estilo o energía | METADATA / TECHNICAL HANDOFF | no genera notas |
| tie-break ante varias opciones | ARTISTIC DEFAULT | debe declararse antes de serializar |

Un default técnico no puede disfrazarse como conocimiento musical. Si falta un
valor musical requerido, el plan permanece pendiente o bloqueado.

## L. Decision trace contract

Cada nodo debe registrar como mínimo:

```text
decision_id / version
level + domain(s)
artistic_goal + decision_question
scope + context
candidate_options
hard_constraints + soft_filters
general_knowledge_basis
genre_input
capability + actionability
active_criterion
selected_option + selection_basis
artistic_preference / tradeoff
uncertainty
expected structural/perceptual/compositional effect
cross-domain dependencies
SongPlan target
revision history
```

La traza debe responder por qué se eligió la forma, por qué recurre el
material, por qué cambia una sección, por qué aumenta o disminuye la textura y
por qué se retuvo una realización armónica. No se permite una justificación
post-hoc.

## M. Unit-5 dry-run contract

Unit 5 debe instanciar **un brief artístico hipotético**, no la primera canción
definitiva, y ejecutar N0–N7 con material suficiente para probar el handoff.
Debe producir:

1. brief y prioridades explícitas;
2. decisiones completas por nodo/bundle;
3. alternativas filtradas y elecciones artísticas;
4. conflictos y, si existe, una revisión local;
5. traza auditable;
6. arquitectura completa de canción;
7. SongPlanV2 válido y explícito, sin inventar campos.

### Recommended mode: B

Unit 5 debe crear y validar un SongPlan válido, **sin renderizar todavía**.

La validación del plan prueba el handoff y el uso correcto del contrato. El
render MIDI es una comprobación posterior de materialización, no es necesario
para demostrar la arquitectura en esta unidad. No se debe presentar la
validación como evidencia de calidad musical o corrección estilística.

Si Unit 5 necesita una realización no expresable con pitches, onsets,
duraciones, tracks, motifs, assignments o transformaciones documentadas, debe
detenerse y registrar el gap; no debe pedir al motor que invente la música.

## N. Remaining blockers

Los P0 arquitectónicos de integración quedan cerrados. Persisten límites no
P0:

- el genre pack sigue siendo provisional y acotado;
- no existe ranking multiobjetivo ni ranking general de realizaciones;
- textura, hooks, tensión y percepción de forma dependen de preferencia,
  diagnóstico y escucha;
- SongPlan no conserva por sí solo rationale científico, pero la traza externa
  cubre esa necesidad de auditoría;
- todavía no existe una canción completa ni una evaluación artística.

No se requiere nueva investigación ni experimento para Unit 5.

## O. MVP readiness after Unit 4

**A — CROSS-DOMAIN FLOW AND SONGPLAN HANDOFF READY FOR FULL-SONG DRY RUN**

Resumen de verificación:

- Major decision nodes: **8**
- Decision bundles: **4**
- Cross-domain dependencies: **9**
- Artistic-priority handoffs: **8**
- Revision triggers: **4**
- SongPlan direct mappings: **7**
- SongPlan indirect/pre-serialization mappings: **7**
- Trace-only decisions: **5**
- True SongPlan representation gaps: **0**
- Technical defaults distinguished from musical defaults: **PASS**
- General/genre/artistic layers separated: **PASS**
- Hook/prominence/memorability distinction preserved: **PASS**
- Multidimensional tension preserved: **PASS**
- 12 integration success cases: **12 / 12 PASS**

Conocimiento nuevo inventado: **NONE**. Nueva investigación: **NONE**.
Experimentos: **NONE**. Código: **NONE**. `music-engine` modificado: **NO**.
