# RQ-HAR-005 — Cadencia armónica, llegada, cierre y alternativas cíclicas

## Status

SYNTHESIZED (direct source verification: PARTIAL — see below;
candidate_audit_evidence_gate: PASS (see gate section);
candidate_audit_status: COMPLETED (audit performed 2026-09-04:
CAND-HAR-027–032 audited, all REVISE → POSSIBLE_WITH_SCOPE,
no rejections, no new candidates; closure-model wording corrected);
lifecycle unchanged: no promotion to manual/ or rules/; NOT solved).

## Central Question

"What harmonic configurations and contextual relationships contribute to
arrival, cadential function, perceived completion, phrase/section closure,
or deliberate non-closure, and how do cyclic/modal/popular-music
organizations achieve boundary or return when classical directed cadence is
weak or absent?"

Formulación orientada a composición:

"¿Cómo puede un compositor contribuir armónicamente a una llegada, cierre,
suspensión, apertura o retorno, qué mecanismos tienen apoyo dentro de
tradiciones concretas, y qué alternativas existen cuando la música no se
organiza mediante cadencias funcionales clásicas?"

## Scope

Conocimiento general dentro de la música popular tonal/modal occidental y
tradiciones estrechamente relacionadas (common practice, pop, rock,
electrónica/dance, prácticas modales, songwriting, cognición musical).
`general` NO significa universal para toda la música humana.

Toda la evidencia perceptiva reseñada utiliza oyentes enculturados en la
tradición tonal occidental salvo indicación explícita. Ver síntesis en
`research/domain/harmony/cadence-closure-arrival.md`.

Restricciones del encargo aplicadas:

- NO promociones a `manual/` ni `rules/`.
- NO iniciar RQ-HAR-006 (expansión cromática solo como dependencia).
- NO experimentos (EXP-002 sigue PAUSED; ningún EXP-HAR).
- NO music-engine; NO MIDI/audio.
- NO modificar CAND-HAR-001–026, RQ-HAR-001/002/003/004, EXP-001/002,
  Melody candidates/integration.
- Melody Foundations (`research/integrations/melody-foundations-v0.md`)
  consultada solo donde es materialmente relevante (CAND-MEL-008 finales
  cambiados, CAND-MEL-009 fragmentación/liquidación, CAND-MEL-014
  aditividad, CAND-MEL-016 pico/culminación, CAND-MEL-017 descenso !=
  cierre, CAND-MEL-028 alargamiento/silencio). Ningún candidato MEL
  modificado.
- Requisito metodológico absoluto: CADENCE, CLOSURE, ARRIVAL, RESOLUTION,
  COMPLETION y ENDING no se usan como sinónimos; cada claim mayor declara
  qué constructo invoca.

## Existing Research Incorporated

- `research/ROADMAP.md` (workflow por pregunta, clases de evidencia,
  regla epistémica STRUCTURE → PERCEPTION → COMPOSITION; soporte ortogonal
  `support_basis`).
- `research/domain/harmony/README.md` (fronteras del dominio).
- `research/domain/harmony/HARMONY-ROADMAP.md` (RQ-HAR-005 como cierre con
  alternativas pop desde el inicio; riesgos: cadencia = últimos dos
  acordes, exigir cadencia funcional en cada frase pop, juzgar loops como
  armonía defectuosa, importar tipologías clásicas sin comprobar).
- `research/domain/harmony/stability-center.md` y
  `research/questions/RQ-HAR-001.md` (vocabulario ESTABLISH / CONFIRM /
  MAINTAIN / WEAKEN / AMBIGUATE; final chord != centro; tónicas
  frágiles/emergentes/ausentes; loops como contraevidencia).
- `research/domain/harmony/direction-function.md` y
  `research/questions/RQ-HAR-002.md` (doce mecanismos de dirección;
  función != etiqueta; V→I acotado CAND-HAR-008; loops CAND-HAR-011;
  dominante != tensión CAND-HAR-012; pre-tónica como expectativa).
- `research/domain/harmony/voice-leading.md` y
  `research/questions/RQ-HAR-003.md` (conducción como ejecución;
  ^7→^1 acotado CAND-HAR-015; continuidad != función CAND-HAR-018).
- `research/domain/harmony/harmonic-rhythm-prolongation.md` y
  `research/questions/RQ-HAR-004.md` (ritmo armónico != prolongación;
  aceleración acotada a sentence clásica CAND-HAR-023; duración !=
  importancia CAND-HAR-022; persistencia cíclica CAND-HAR-026).
- `research/integrations/melody-foundations-v0.md` (GAP-08: cierre
  melódico aislado como máximo parcial; armonía como cuello de botella;
  llegada/culminación cross-domain).
- Fuentes ya registradas y reutilizadas aquí:
  SRC-ACADEMIC-009 (Krumhansl; jerarquía tonal),
  SRC-ACADEMIC-012 (Huron; expectativa),
  SRC-ACADEMIC-028 (Spicer 2017; tónicas frágiles/ausentes, soul-dominant,
  giros modales, retransición ♭VII–I, efecto Sísifo),
  SRC-ACADEMIC-029 (Everett 2004; seis sistemas tonales, aserción),
  SRC-ACADEMIC-030 (Temperley 2011 scalar shift; supermodo),
  SRC-ACADEMIC-031 (de Clercq 2018; reseña de Doll: esquemas, pre-tónica,
  ambigüedad en loops, intuición-vs-corpus),
  SRC-ACADEMIC-032 (Nobile 2016; marco sintáctico, PARCIAL),
  SRC-ACADEMIC-033 (Biamonte 2010; patrones modales, PARCIAL por puntos),
  SRC-CORPUS-007 (Doll 2017; vía reseña),
  SRC-CORPUS-009 (de Clercq & Temperley 2011; distribuciones),
  SRC-THEORETICAL-002 (Caplin 1998; forma clásica y función cadencial),
  SRC-THEORETICAL-005 (GTTM), SRC-THEORETICAL-006 (Schenker),
  SRC-THEORETICAL-007 (Temperley; cognición/probabilidad),
  SRC-THEORETICAL-010 (Lerdahl TPS; solo-marco),
  SRC-EMPIRICAL-010/011 (Margulis silencios; Kragness & Trainor límites),
  SRC-EMPIRICAL-012 (Palmer & Krumhansl 1990; metro).

## Source Set (this RQ)

Full text directly inspected (VERIFIED, heredado de RQ-HAR-001–004):
SRC-ACADEMIC-028, SRC-ACADEMIC-029, SRC-ACADEMIC-030, SRC-ACADEMIC-031
(reseña; el libro SRC-CORPUS-007 sigue PARCIAL vía reseña),
SRC-ACADEMIC-009, SRC-ACADEMIC-012, SRC-PEDAGOGICAL-001,
SRC-THEORETICAL-002.

Marcos reutilizados sin reabrir (PARCIAL o marco genérico, sin claim
citable nuevo): SRC-THEORETICAL-005/006/007/010, SRC-PEDAGOGICAL-005–008,
SRC-CORPUS-009, SRC-ACADEMIC-018, SRC-EMPIRICAL-010/011/012/015,
SRC-ACADEMIC-032/033/034/036/037.

Nuevos records creados en esta RQ (red externa disponible en esta sesión;
búsqueda web + 1 fetch de página; fetch directo a MTO/UC Press devolvió
403, igual que en sesiones anteriores; ningún texto completo inspeccionado):

- SRC-EMPIRICAL-016 (Sears / Caplin / McAdams 2014, percepción de la
  cadencia clásica; PARTIAL: metadatos + resultados sustantivos vía
  extractos detallados de ResearchGate/JSTOR/McGill; texto completo
  pendiente).
- SRC-ACADEMIC-041 (Sears 2015, capítulo sobre cierre cadencial en
  "What is a cadence?"; PARTIAL: extractos de la revisión + índice).
- SRC-EMPIRICAL-017 (Smit et al. 2020, arousal/valence de cadencias;
  PARTIAL: abstract + resultados vía extractos; constructo = emoción
  percibida, NO cierre).
- SRC-ACADEMIC-042 (Temperley 2011, "The Cadential IV in Rock", MTO;
  PARTIAL: extractos sustantivos con estadísticas RS200 + acuerdo
  inter-juez; texto completo pendiente por 403 en fetch).
- SRC-THEORETICAL-016 (Caplin 2024, Cadence: A Study of Closure in Tonal
  Music, vía reseña Feng/ZGMTH; PARTIAL de segundo nivel: stages,
  contrapuntal vs. prolongational closure, negación de plagal cadence,
  evaded/abandoned; libro no inspeccionado).
- SRC-PEDAGOGICAL-009 (Open Music Theory, Modal Schemas, Lavengood;
  PARTIAL: extractos sustantivos + fetch de estructura de página;
  Aeolian cadence, double plagal, shuttles).
- SRC-CORPUS-010 (Brown 2020, pre-dominant function corpus Mozart, MTO;
  PARTIAL: abstract + taxonomía de cadencias + hallazgo de dependencia
  por tipo; dataset no inspeccionado).

Ningún metadato se inventa: los records nuevos omiten lo no verificado.
Ver tabla "Sources" en
`research/domain/harmony/cadence-closure-arrival.md` y records en
`research/sources/`.

Marcos nombrados sin record dedicado (no citar hasta registrar):
Hepokoski/Darcy (EEC/MC), Aldwell/Schachter (cadencias), Gjerdingen
esquemas de cierre (Prinner etc.), Neuwirth/Bergé (edición What is a
cadence?), literatura de fade-out (existencia por verificar),
literatura de priming/expectativa continua (Sears et al. 2018–2020 como
existencia confirmada sin extractos inspeccionados salvo mención).

## Candidate Claims Produced

- CAND-HAR-027 (cadencia como proceso contextual con posición formal,
  no lookup de dos acordes; THEORY acotada + heurística negativa).
- CAND-HAR-028 (llegada tónica != cierre; la armonía puede contribuir al
  cierre sin suficiencia contextual ni necesidad universal demostradas;
  COMPOSITION HEURISTIC negativa; wording corregido en auditoría 2026-09-04).
- CAND-HAR-029 (jerarquía analítica de fuerza cadencial != ranking
  perceptivo; dependencia de formación y rasgos retóricos; HYPOTHESIS
  con alcance clásico).
- CAND-HAR-030 (llegadas plagales/modales como fórmulas de repertorio
  acotado, no cadencia plagal universal; GENRE OBSERVATION + THEORY con
  scope).
- CAND-HAR-031 (retorno de loop != cadencia; frontera por parada/arreglo;
  costura recurrente vs. terminal; GENRE OBSERVATION).
- CAND-HAR-032 (tónica final sin cadencia y finales no-tónicos como
  estados legítimos acotados; tónica final no garantiza cierre;
  COMPOSITION HEURISTIC negativa + GENRE OBSERVATION).

IDs 001–026 no reutilizados. Ningún claim pasa a `manual/` ni `rules/`
sin revisión y aprobación del Project Owner y del Music/Methodology
Director.

## Unresolved Issues

- Ponderación perceptiva entre armonía, melodía, metro, duración y
  posición formal en juicios de cierre (Sears: regresión por voces pero
  sin diseño que aísle cada dominio).
- Si la jerarquía PAC>IAC>HC se sostiene fuera de Mozart/teclado/clásico
  y fuera de oyentes enculturados occidentales (sin evidencia).
- Criterios formalizados de función cadencial interna en loops
  (asignación interna sigue abierta; hereda GAP de HAR-002/004).
- Si la desaceleración/alargamiento final es dispositivo con teoría o
  solo correlato (sin teoría inspeccionada; CAND-MEL-028 como contexto).
- Condiciones bajo las cuales una parada de loop se escucha como cierre
  vs. corte (sin medida; solo análisis).
- Efecto perceptivo del fade-out (GAP total: sin literatura localizada).
- Si la "prolongational closure" capliniana tiene correlatos perceptivos
  o es solo distinción analítica (sin medida).
- Transferencia de stages cadenciales (Caplin 2024) fuera de práctica
  común (libro no inspeccionado; alcance declarado clásico).
- Curva corpus→cierre: si las estadísticas de cierres predicen juicios
  de completitud en pop (GAP empírico).
- Vocabulario de metas de llegada (ARRIVE/EVADE/DEFER…): no adoptado;
  prosa provisional solamente.

## Further External Research Needed

Inspección directa pendiente (ordenada por leverage para HAR-005):

1. Sears / Caplin / McAdams 2014, texto completo (Music Perception
   31/5:397–417; DOI verificado; detalles de N, estímulos, subtypes).
2. Sears 2015, capítulo Leuven (pp.251–283; modelo de fuerza + contexto
   formal).
3. Temperley 2011 "Cadential IV", texto completo MTO (tablas RS200,
   plagal stop, grand plagal, deceptive IV).
4. Caplin 2024, texto (stages, contrapuntal cadence, evaded/abandoned,
   alcance histórico declarado).
5. Doll 2017, texto completo (esquemas de cierre, cap.6 ambigüedad).
6. Nobile 2016 + Nobile Form-as-Harmony (cadence and closure cap.;
   relación función sintáctica vs. cierre).
7. Biamonte 2010, texto completo (cadencia eolia y patrones).
8. de Clercq 2017 JMT (detalles seccionales; armonía-forma).
9. Brown 2020, dataset + texto (pre-dominante por tipo de cadencia).
10. Sears et al. 2018–2020 (modelos probabilísticos y expectancy
    continua de cadencias).
11. Literatura de fade-out y finales por producción (localizar; GAP).
12. Corpus pop/rock de finales con juicios de cierre por oyentes (GAP;
    excede esta RQ pero se registra).

## Further Experiment Currently Justified

NO. Ningún experimento propio en esta tarea (prohibido por el encargo;
EXP-002 sigue PAUSED). La síntesis alcanza estado SYNTHESIZED con
confianza provisional/baja-media según claim. Futuras preguntas
falsables candidatas se registran en la sección "Need for Experiment"
de la síntesis sin diseñar ningún experimento.

## Evidence-Sufficiency Gate (for later candidate audit)

- Claims con apoyo directo suficiente para auditar: CAND-HAR-027
  (stages Caplin vía reseña sustantiva + efecto de contexto formal Sears
  + taxonomía Brown + Caplin 1998 repo), CAND-HAR-028 (Sears 2014:
  regresión bajo/soprano + disonancia/trill/duración + split HC
  músicos/no-músicos + convergencia Melody CAND-MEL-017/028),
  CAND-HAR-029 (Sears 2014: ranking PAC>IAC>HC>DC>EV músicos + efecto
  formación en DC/EV + R² .84/.53 + rhetorical features),
  CAND-HAR-030 (Temperley RS200 59%/32%/18.5% + OMT modal schemas +
  negación capliniana vía reseña + Biamonte por puntos),
  CAND-HAR-031 (Doll cap.6 vía reseña + Spicer VERIFIED + Temperley 41%
  sin sectional cadence + CAND-HAR-011/026 heredados),
  CAND-HAR-032 (Spicer tónicas ausentes VERIFIED + Temperley finales
  sin cadencia + Smit 2020 como límite emoción!=cierre +
  CAND-HAR-004 heredado).
- Records PARTIAL nuevos: ninguno sostiene por sí solo un claim
  positivo universal; todos delimitan alcance (clásico / rock / tarea
  concreta). La cautela "sin texto completo" se registra por candidato.
- Gate: PASS con alcance declarado (ver sección "Direct-Source Audit
  Gate" en la síntesis). Audit de candidatos NO realizado en esta tarea.
