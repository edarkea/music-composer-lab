# Composer MVP v1 — Readiness Audit

## A. Executive verdict

**NOT READY — SPECIFIC BLOCKERS**

El repositorio contiene una base amplia de investigación, candidatos y marcos de integración, pero todavía no contiene suficiente conocimiento aprobado y conectado para construir una primera canción completa defendible. La limitación principal no es la ausencia de teoría: es la distancia entre conocimiento investigado, decisión compositiva coordinada y un `SongPlan` auditable.

Este audit es de readiness, no una promoción de candidatos. `composer-foundations-v5.md` declara explícitamente que no es conocimiento aprobado; los candidatos siguen siendo candidatos; los archivos vacíos de `manual/`, `rules/` y `genres/` no constituyen contenido aprobado.

## B. Audit scope and evidence discipline

Se revisaron:

- `research/ROADMAP.md`.
- `research/domain/` en melody, harmony, rhythm y cross-domain.
- `research/candidates/` y sus estados epistemológicos.
- `research/integrations/composer-foundations-v0.md` a `composer-foundations-v5.md`.
- Integraciones de melody, harmony, form y melody-harmony.
- `manual/`, `rules/` y `genres/`.
- SongPlans existentes, incluido el canary técnico de EXP-003.
- `integrations/music-engine/runtime-lock.yaml`.

Observaciones estructurales relevantes:

- `manual/01-melody.md` a `manual/06-evaluation.md` están vacíos; el único contenido melódico heredado está en `manual/drafts/melody-v1.md`, que es material candidato para auditoría.
- `rules/melody.yaml`, `rules/harmony.yaml` y `rules/evaluation.yaml` están vacíos.
- Los archivos de `genres/indie-dance/` están vacíos.
- Los SongPlans existentes son de experimentos/canaries, no un plan composer-facing de canción completa.
- `music-engine` está fijado como backend determinista de materialización; no aporta criterio de composición.

## C. Current compositional capability map

| Domain | ENUMERATE | FILTER | RANK-1 | RANK-2 | Actionability now |
|---|---|---|---|---|---|
| Melody | Sí, con representaciones explícitas | Sí, con alcance | Sí, solo en un caso de recognition acotado | No | ACTIONABLE WITH SCOPE |
| Harmony | Sí, varios seeds/organizaciones | Sí, con marco y contexto | No general | No | ACTIONABLE WITH SCOPE |
| Rhythm / meter | Sí, variables temporales | Sí, con contexto | No positivo general | No | ACTIONABLE WITH SCOPE |
| Form | Sí, roles y organizaciones | Parcial, con función declarada | No general | No | ACTIONABLE WITH SCOPE |
| Development | Sí, operaciones transformacionales | Sí, mediante invariantes declaradas | No general | No | ACTIONABLE WITH SCOPE |
| Tension / release | Sí, contribuyentes separados | Parcial, sin scalar único | No | No | DIAGNOSTIC ONLY |
| Hooks / prominence | Conceptos separados | Insuficiente | No | No | DIAGNOSTIC ONLY |
| Texture / arrangement | Sí, en el mapa conceptual | Parcial | No | No | BLOCKED AS INTEGRATED DECISION |
| Melody–harmony | Sí, relaciones posibles | Sí, para incompatibilidades declaradas | No positivo | No | ACTIONABLE WITH SCOPE |
| Song-level | Sí, preguntas y trayectorias | No integrado | No | No | BLOCKED |

`CAN GENERATE` aparece en varios marcos como capacidad para producir candidatos o representaciones. No equivale a `CAN CHOOSE WELL`.

## D. Decision inventory by domain

### Melody

Decisiones: construir una semilla, declarar qué relación se conserva, repetir, variar, cambiar el final, fragmentar, elegir registro/rango y ubicar un cierre. El repositorio permite enumerar y filtrar con heurísticas acotadas. `CAND-CROSS-003` aporta un `RANK-1` sobre recognition bajo condiciones explícitas, no una preferencia global entre variantes.

**Estado:** ACTIONABLE WITH SCOPE. No es conocimiento aprobado en `manual/`.

### Harmony

Decisiones: escoger centro/colección, organización dirigida o cíclica, seed, ritmo armónico, persistencia, bajo, inversión, voicing y relación con la melodía. Hay lenguaje de filtros y restricciones, pero las propias integraciones marcan que la realización y la elección entre alternativas siguen sin ranking positivo integrado.

**Estado:** ENUMERATE/FILTER con alcance; muchas decisiones son DIAGNOSTIC ONLY o BLOCKED para una preferencia prospectiva general.

### Rhythm / meter

Decisiones: establecer pulso, subdivisión, densidad, acento, síncopa, silencio, posición métrica, anticipación y cambio de ritmo armónico. El material distingue variables y evita causalidad automática, pero no establece qué opción sirve mejor a una meta compositiva general.

**Estado:** ACTIONABLE WITH SCOPE para restricciones y preferencias declaradas; no hay RANK general.

### Form

Decisiones: definir roles de sección, continuidad, transición, llegada, apertura, retorno y contraste. La teoría y las observaciones permiten describir y filtrar incompatibilidades, pero `FORM-003` y `FORM-006` continúan marcados como no listos en las integraciones.

**Estado:** ACTIONABLE WITH SCOPE para una forma declarada; BLOCKED para un método general medio→efecto de contraste/continuación.

### Development

Decisiones: cuándo repetir, variar, fragmentar, extender, reducir, recombinar, transformar, acumular u omitir. Hay operaciones disponibles y heurísticas con marco, pero la selección depende de una intención y de tradeoffs que no están resueltos por ranking.

**Estado:** ACTIONABLE WITH SCOPE, no como regla universal.

### Tension / release

Decisiones: qué contribuyentes activar, mantener o retirar y cómo coordinar sus trayectorias. El roadmap exige separar melodía, armonía, ritmo, registro, densidad, timing, expectativa y forma; no existe una medida o modelo compositivo único aprobado.

**Estado:** DIAGNOSTIC ONLY para gran parte de la relación estructura→percepción; una estrategia MVP debe declarar intención y usar preferencias, no puntuar tensión como scalar.

### Hooks / prominence

El repositorio correctamente mantiene separados hook, prominence y memorability. Esa separación es metodológicamente sólida, pero deja sin criterio prospectivo suficiente decisiones como qué material convertir en hook o cómo hacerlo recurrir sin monotonía.

**Estado:** DIAGNOSTIC ONLY; no constituye un P0 independiente si el MVP declara el foco material mediante preferencia artística.

### Texture / arrangement

Decisiones: qué capa entra o sale, qué queda en foreground/background, densidad, registro, instrumentación y apoyo del material focal. El roadmap enumera las variables, pero `genres/` está vacío y no hay integración composer-facing que coordine acompañamiento con melodía, armonía y forma.

**Estado:** BLOCKED AS INTEGRATED DECISION; puede reducirse en MVP mediante una paleta y roles explícitos.

### Cross-domain and song-level

Existen documentos sólidos para no confundir dominios y para detectar transferencias inválidas. Falta convertirlos en una secuencia concreta donde una decisión de melodía limite armonía, ritmo, forma y textura, y donde las decisiones locales se agreguen en una canción completa.

**Estado:** BLOCKED en integración, no necesariamente por falta de conocimiento dentro de cada dominio.

## E. Structure → perception → composition audit

La disciplina está bien formulada en el roadmap y en las integraciones, pero todavía no está materializada en una interfaz de decisión aprobada. Los puentes que no deben tratarse como hechos son, entre otros:

- registro alto → emoción o clímax;
- densidad → energía;
- descenso → cierre;
- dominante → tensión;
- repetición → memorabilidad o calidad;
- contorno → función formal;
- movimiento mínimo → mejor conducción;
- reconocimiento → mejor composición;
- retorno exacto → mejor retorno formal.

La estructura puede describirse, la percepción puede ser una consecuencia medida o hipotética y la decisión compositiva requiere además una meta, contexto y alternativa. El MVP debe conservar esas tres capas en cada decisión.

## F. Actionability assessment

### ACTIONABLE WITH SCOPE

- Construir una semilla melódica declarando invariantes y objetivo.
- Enumerar seeds armónicos y filtrar por centro, marco, registro y compatibilidad explícita.
- Diseñar ritmos con restricciones de metro, densidad y timing declaradas.
- Elegir una forma prefijada y asignar funciones locales de continuación, llegada, apertura o retorno.
- Aplicar transformaciones desarrolladoras cuando la relación preservada y la intención estén declaradas.

### DIAGNOSTIC ONLY

- Explicar por qué una estructura podría ser percibida como tensa, prominente, memorable o cerrada sin usar la explicación como regla.
- Diagnosticar incompatibilidades de melody–harmony y realización.
- Describir hook, prominence y memorability como constructos distintos.

### BLOCKED

- Ranking multiobjetivo de identidad, novedad, contraste, estilo y continuidad.
- Elegir una realización armónica sobre otra con un criterio compositivo integrado.
- Coordinar trayectorias de textura, tensión, forma y material a escala de canción.
- Producir una canción completa con trazabilidad desde intención hasta SongPlan.

## G. Cross-domain integration assessment

**Cross-domain blocker: YES.**

El repositorio ya contiene conocimiento cross-domain suficiente para evitar errores de transferencia, pero la capacidad está principalmente en `FILTER`, cautela y diagnóstico. No existe todavía un contrato operativo que resuelva, por ejemplo:

`objetivo formal → semilla → melodía/armonía → ritmo → textura → desarrollo → retorno`

con criterios explícitos y puntos donde la preferencia artística decide. Añadir más hechos aislados no resolvería este bloqueo.

## H. SongPlan translation assessment

**SongPlan translation blocker: YES.**

La arquitectura conceptual existe:

`knowledge → objective → candidates → filter/rank → decision → SongPlan → music-engine`.

Pero no hay un artefacto composer-facing que especifique, para una canción completa:

- objetivo e intención por sección;
- candidatos considerados y descartados;
- criterio activo y alcance de evidencia;
- decisiones melódicas, armónicas, rítmicas y texturales coordinadas;
- incertidumbre y preferencias artísticas;
- trazabilidad de cada decisión al SongPlan.

Los SongPlans encontrados materializan canaries o experimentos existentes; no prueban que el sistema pueda planificar una canción desde cero.

## I. Genre assessment

**Genre-pack blocker: YES, si el MVP pretende una realización estilística defendible.**

`genres/indie-dance/` existe como estructura, pero sus documentos están vacíos. El proyecto no necesita muchos géneros: necesita uno definido, aunque sea mínimo, que declare tempo/metro o alternativas, forma, paleta, textura, tratamiento de loops, roles de bajo y criterios de realización sin convertir observaciones en leyes generales.

Esto no exige nueva investigación amplia antes de empezar. Puede construirse con decisiones artísticas explícitas y observaciones claramente marcadas, pero actualmente no existe.

## J. Genuine MVP blockers

### P0-1 — Approved decision layer missing

No hay contenido aprobado en `manual/`, `rules/` o `genres/` que convierta la investigación en una base de decisiones reutilizable. Las integraciones no aprobadas y los candidatos no pueden tratarse silenciosamente como conocimiento aprobado.

### P0-2 — Cross-domain song workflow missing

No existe un flujo operativo que coordine melodía, armonía, ritmo, forma, desarrollo y textura a escala de canción con intención, criterios y límites explícitos.

### P0-3 — SongPlan composer handoff missing

No existe un `SongPlan` composer-facing con trazabilidad de decisiones, alternativas, incertidumbre y preferencias antes de la materialización determinista.

### P0-4 — Minimal genre realization missing

No existe ningún genre pack utilizable para limitar y justificar la realización de una primera canción estilísticamente coherente.

Estos cuatro bloqueadores son genuinos porque sin ellos el primer flujo completo dependería de decisiones silenciosas o arbitrarias. La ausencia de RANK-2, de un modelo único de tensión o de evidencia experimental sobre cada operación no es por sí sola P0: puede declararse como incertidumbre y resolverse mediante preferencia artística en el MVP.

## K. Non-blocking gaps

- Ranking general entre alternativas melódicas, armónicas, rítmicas y de realización: P1.
- Medio→efecto de contraste, continuación y llegada: P1.
- Hook frente a memorability y prominence: P1/P2.
- Modelo integrado de tensión y release: P1/P2.
- Modulación, cromatismo y realizaciones más sofisticadas: P2.
- Transferencia cross-cultural y generalidad fuera del alcance occidental tonal/modal popular: P3 para este MVP.

No se propone experimento para estos gaps durante este audit.

## L. Experiment necessity assessment

**New experiment required before first song: NO.**

La brecha crítica actual es de integración y aprobación, no una decisión concreta que solo un experimento pueda resolver. Las alternativas pueden filtrarse con alcance, preferencia artística y declaración explícita de incertidumbre. El resultado `CAND-CROSS-003` tampoco debe generalizarse: es un ranking local sobre recognition bajo condiciones específicas.

No se abre ningún experimento y `EXP-003`/`EXP-002` no forman parte de este camino crítico.

## M. Minimal Composer MVP v1 specification

El MVP mínimo defendible debería incluir:

1. **Scope:** una canción instrumental o vocal con alcance estilístico explícito dentro de Western tonal/modal popular music; si se usan letras, añadir una decisión separada de prosodia.
2. **Required domains:** melody, harmony, rhythm/meter, form, development y texture/arrangement mínima.
3. **Decision record:** cada decisión registra objetivo, variables, alternativas, filtro, criterio, evidencia, incertidumbre y preferencia artística.
4. **Capability policy:** `ENUMERATE` y `FILTER` como mínimo; `RANK-1` solo cuando el criterio y alcance estén justificados; nunca inventar ranking global.
5. **Cross-domain minimum:** semilla y objetivo compartidos entre melodía y armonía; coordinación explícita de ritmo, forma y textura por sección.
6. **One genre pack:** una realización mínima y separada de conocimiento general, preferiblemente indie-dance solo si se completa y se etiqueta como genre-specific.
7. **Uncertainty behavior:** mantener opciones o declarar preferencia; no rellenar huecos con reglas universales.
8. **Artistic-preference interface:** permitir elegir metas como continuidad, contraste, apertura, retorno, densidad o novedad y resolver tradeoffs de manera explícita.
9. **SongPlan handoff:** producir un plan completo por secciones, tracks/roles, materiales, asignaciones, timing y referencias de decisión antes de llamar a `music-engine`.
10. **Audit capability:** conservar decisiones, alternativas rechazadas, fuente/estado epistemológico y cualquier inferencia no demostrada.

El MVP no necesita una teoría universal, un ranking multiobjetivo, un scalar de tensión ni validación experimental de cada decisión.

## N. Exact next work sequence

1. Crear un contrato de decisión composer-facing, sin convertirlo aún en reglas automáticas.
2. Seleccionar y revisar un subconjunto pequeño de conocimiento existente para melody, harmony, rhythm, form, development y texture.
3. Redactar un único genre pack mínimo con alcance explícito y preferencias separadas.
4. Diseñar el registro cross-domain por secciones y el handoff a SongPlan.
5. Hacer un dry-run de trazabilidad con material hipotético, sin publicar una canción ni abrir un experimento.
6. Solicitar revisión humana y del Music/Methodology Director antes de promover contenido a `manual/` o `rules/`.

## O. First-song readiness decision

**NOT READY — SPECIFIC BLOCKERS.**

La primera canción será defendible cuando los cuatro P0 anteriores estén cubiertos: una capa aprobada mínima, integración cross-domain, SongPlan composer-facing auditable y un genre pack de una sola especialización. No hace falta esperar a resolver todos los gaps P1–P3 ni abrir un experimento antes de esa primera composición.

## Recommended next action

Diseñar el contrato mínimo de decisión composer-facing que conecte intención, candidatos, filtro, incertidumbre, preferencia artística y SongPlan para una sola forma y un solo genre pack.

## Audit limits

Este documento no promueve candidatos, no modifica manuales, reglas, géneros ni music-engine, no abre experimentos y no compone una canción. `EXP-003` permanece **PAUSED — READY TO RESUME** y fuera del critical path de Composer MVP v1.
