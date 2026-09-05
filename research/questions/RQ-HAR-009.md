# RQ-HAR-009 — Melody–Harmony Interaction

## Status

INVESTIGATED + SYNTHESIZED (direct source verification: PARTIAL — see below;
candidate_audit_evidence_gate: PASS (see gate section);
candidate_audit_status: NOT STARTED (audit of CAND-HAR-046–052 not performed in this task);
lifecycle unchanged: no promotion to manual/ or rules/; NOT solved).

## Central Question

"How do melodic pitch, scale-degree interpretation, register, rhythm, phrase
position, repetition, and local melodic motion interact with harmonic
identity, bass, inversion, voicing, harmonic rhythm, tonal/modal center,
and arrival, and which relationships are structurally constrained,
perceptually supported, stylistically conventional, or compositionally
actionable?"

Formulación orientada a composición:

"Dada una melodía concreta, ¿cómo puede un compositor elegir y realizar una
armonía que la apoye, reinterprete, contraste o deje abierta; y dada una
armonía concreta, qué decisiones melódicas siguen disponibles sin reducir la
relación melodía–armonía a una tabla chord-tone/non-chord-tone?"

## Scope

Conocimiento general dentro de la música popular tonal/modal occidental y
tradiciones estrechamente relacionadas (common practice, pop, rock,
electrónica/dance, prácticas modales, songwriting, cognición musical).
`general` NO significa universal para toda la música humana.

Toda la evidencia perceptiva reseñada utiliza oyentes enculturados en la
tradición tonal occidental salvo indicación explícita. Ver síntesis en
`research/domain/harmony/melody-harmony-interaction.md`.

Restricciones del encargo aplicadas:

- NO iniciar RQ-HAR-007 (modulación solo como dependencia/frontera;
  todo caso que establezca genuinamente un nuevo centro se marca
  CROSS-RQ DEPENDENCY: RQ-HAR-007).
- NO modificar Harmony Foundations v0/v1
  (`research/integrations/harmony-foundations-v0.md`,
  `research/integrations/harmony-foundations-v1.md`): son snapshots previos.
- NO modificar CAND-HAR-001–045, archivos Melody, ni RQ-HAR anteriores.
- NO promociones a `manual/` ni `rules/`.
- NO `genres/`, NO `experiments` (EXP-002 sigue PAUSED; ningún EXP-HAR).
- NO music-engine; NO MIDI/audio.
- Skills `.agents/skills/research-music-concept/SKILL.md` y
  `.agents/skills/audit-music-knowledge/SKILL.md` aplicadas manualmente.

## Absolute Core Principle (preserved throughout)

```
MELODY and HARMONY are interacting layers, not lookup tables.
```

Do NOT assume melodic pitch → one harmonic interpretation, or chord label
→ one melodic interpretation. Todas las distinciones obligatorias del
encargo se conservan explícitamente en la síntesis (CHORD TONE != MELODIC
STABILITY; NON-CHORD TONE != disonancia/tensión automáticas; MELODIC
ARRIVAL != HARMONIC ARRIVAL; TOP NOTE != MELODY; BASS != MELODIC ROOT;
etc.). Ninguna se colapsa.

## Existing Research Incorporated

- `research/ROADMAP.md` (workflow, clases de evidencia, regla
  STRUCTURE → PERCEPTION → COMPOSITION; `support_basis` ortogonal).
- `research/domain/harmony/README.md` y `HARMONY-ROADMAP.md`
  (RQ-HAR-009 como interfaz última, dependiente de todo Harmony
  Foundations + Melody Foundations).
- Síntesis Harmony 001–006 y 008 (`research/domain/harmony/*.md`) y
  `research/questions/RQ-HAR-001–006, 008.md` (CAND-HAR-001–045;
  bloqueos 002/005/019 preservados; eje SELECTION vs REALIZATION de v1).
- Síntesis Melody (`research/domain/melody/*.md`) y
  `research/questions/RQ-MEL-001, 002, 003, 005, 006.md`
  (CAND-MEL-001–030; CAND-MEL-018 REJECTED permanente).
- `research/integrations/melody-foundations-v0.md` (flujo decisional,
  cierre melódico como máximo parcial, armonía como cuello de botella).
- `research/integrations/harmony-foundations-v1.md` (SELECTION vs
  REALIZATION como eje; §19 readiness de interfaz; §20 dependencias
  HAR-007; §25 decisión HAR-009 frente a HAR-007; representación §13).

## Source Set (this RQ)

Sin inspección externa nueva en esta sesión: ninguna fuente primaria
nueva fue inspeccionada a texto completo más allá del capital ya
verificado del repositorio. La síntesis descansa en fuentes ya
inspeccionadas y registradas en las RQs previas, reutilizadas solo en
su alcance declarado, más delimitaciones de marco. Ningún metadato se
inventa. Ningún nombre se cita como apoyo salvo en el alcance ya
registrado en su RQ de origen.

Texto ya inspeccionado y reutilizado directamente (alcance heredado,
sin reabrir, sin elevar estatus):

- SRC-ACADEMIC-028 (Spicer 2017, VERIFIED): tónicas frágiles por
  inversión; pedal que fija/engaña; vamp §12 (acento duracional, pedal,
  alturas melódicas enfatizadas, orden); convergencia melodía-sobre-bajo.
- SRC-ACADEMIC-029 (Everett 2004, VERIFIED): pedal/drone modal;
  seis sistemas tonales.
- SRC-ACADEMIC-030 (Temperley 2011, VERIFIED): CENTER != COLLECTION
  (scalar shift); divorce melodía-armonía citado.
- SRC-ACADEMIC-031 (de Clercq 2018 reseña de Doll 2017, VERIFIED como
  reseña): mismo loop distinto centro según configuración; divorce;
  intuición-vs-corpus.
- Pedagogía OMT VERIFIED (tonicalización, mezcla, Aug6, tono común
  CTo7/CT+6 con disociación enarmónica; cadential 6/4).
- SRC-THEORETICAL-002 (Caplin, VERIFIED): sentence clásica
  (fragmentación + liquidación + aceleración armónica hacia cadencia);
  cadencia como proceso.
- SRC-EMPIRICAL-016 (Sears, PARTIAL): ratings de completitud;
  predictores bajo (músicos) / soprano (no-músicos); betas NO utilizables
  como pesos.
- Capital Melody: Dowling, Bartlett & Dowling, Krumhansl & Kessler,
  Prince, Halpern, Jones & Ralston, Müllensiefen, Palmer & Krumhansl
  1987/1990, Schellenberg, von Hippel & Huron, Margulis, Huron 1996,
  Tan et al., Witek, Madison, White 2022, Eitan, Ilie & Thompson
  (alcances según síntesis Melody; ninguno reabierto aquí).
- EXP-001 (n=1, indicio propio): transposición pequeña B=3; tolerancia
  unidimensional D/E=4; degradación multidimensional C/F=2.

Heredado PARTIAL / UNVERIFIED (sin elevar estatus; solo marcos y gaps):

- Doll 2017 texto completo; Nobile (divorce, cadencias rock/pop);
  Temperley 2001 primario métrico; corpus pop/rock con juicios de
  oyentes (GAP estructural); pedagogía clásica de armonización de
  soprano/bajo sin texto inspeccionado; chord-scale / avoid-note /
  guide-tone jazz (GAP, no citable); literatura de priming armónico
  con melodía (GAP; localizar).

Ver tabla "Sources" en
`research/domain/harmony/melody-harmony-interaction.md`.

## Candidate Claims Produced

Serie CAND-HAR-046–052 (7 claims, todos interactionales; ningún
duplicado paralelo CAND-MEL; forma ligera del roadmap §5):

- CAND-HAR-046 (pertenencia al acorde != estabilidad melódica;
  binario chord/non-chord insuficiente; heurística negativa).
- CAND-HAR-047 (melodía fija infradetermina selección armónica;
  misma melodía admite varias armonías; heurística negativa/estructural).
- CAND-HAR-048 (contexto armónico reinterpreta el mismo pitch melódico;
  reinterpretación analítica vs perceptiva separadas; hipótesis).
- CAND-HAR-049 (misma identidad armónica admite varias realizaciones
  bajo melodía fija; melodía restringe sin determinar
  bajo/inversión/voicing; heurística negativa).
- CAND-HAR-050 (llegadas melódica y armónica pueden divergir;
  cierre exige convergencia cross-domain; heurística).
- CAND-HAR-051 (variación armónica puede acompañar material melódico
  repetido sin alterar identidad; rearmonización != desarrollo
  automático; hipótesis con alcance).
- CAND-HAR-052 (categorías de non-chord tone dependen de
  marco/temporalidad/conducción; ninguna etiqueta infiere
  tensión/belleza/error; heurística negativa).

IDs 001–045 no reutilizados. Ningún claim pasa a `manual/` ni `rules/`
sin revisión y aprobación del Project Owner y del Music/Methodology
Director. La auditoría de candidatos queda registrada en `Candidate Audit
Status` más abajo; no implica promoción.

## Candidate Audit Status

`candidate_audit_status: COMPLETED` (CAND-HAR-046–052 audit completed;
no promotion; lifecycle remains unsolved). The audit result is seven
`POSSIBLE_WITH_SCOPE`, zero `STRONG_CANDIDATE`, zero `NOT_READY`, and zero
rejected candidates. The earlier synthesis status is retained as historical
context; this section records the completed audit state.

## Unresolved Issues

- Ponderación perceptiva de pertenencia al acorde frente a colección,
  bajo, métrica y contexto en juicios de estabilidad melódica
  (ninguna medida dedicada inspeccionada).
- Si la reinterpretación armónica de una melodía idéntica es
  analítica, perceptiva o ambas (diseño con melodía fija × armonía
  variada pendiente; GAP).
- Criterios de identidad melódica bajo rearmonización (qué debe
  permanecer invariante; dependencia de RQ-MEL-001 sin curva).
- Elección ponderada de bajo/inversión/voicing bajo melodía dada
  (manipulable y diagnosticable; elección bien fundada todavía NO).
- Fuerza sentida de llegadas divergentes (melodía llega / armonía no
  y viceversa; medida multi-dominio pendiente).
- Frontera tonicalización/modulación con melodía como evidencia
  (cede a RQ-HAR-007).
- Transferencia jazz (avoid notes, chord-scale, guide tones) sin
  fuente inspeccionada (GAP puro).

## Further External Research Needed

Ordenada por leverage para HAR-009:

1. Nobile (divorce melodía-armonía; cadencias rock/pop con soprano).
2. Corpus pop/rock de alineación melodía-acorde con metodología
   declarada (distribuciones melodía vs root; non-chord tones vocales;
   cambios bajo motivo repetido; finales de frase).
3. Literatura de expectativa melódica bajo contexto armónico y de
   priming armónico sobre juicios melódicos (tarea/medida declaradas).
4. Pedagogía clásica de armonización (soprano/bajo dados; reglas de
   non-chord tones con pasajes textuales).
5. Temperley / de Clercq pop (sintaxis con línea superior).
6. Sears completo + Krumhansl tonal hierarchy con contexto
   melodía+armonía combinados.
7. Pedagogía jazz registrada antes de citar (transferencia acotada o GAP).
8. Corpus pop/rock con juicios de oyentes sobre rearmonización
   (GAP; excede esta RQ pero se registra).

## Further Experiment Currently Justified

NO. Ningún experimento propio en esta tarea (prohibido por el encargo;
EXP-002 sigue PAUSED). La síntesis alcanza estado SYNTHESIZED con
confianza provisional/baja-media según claim. Futuras preguntas
falsables candidatas se registran en la sección "Need for Experiment"
de la síntesis sin diseñar ningún experimento.

## Evidence-Sufficiency Gate (for later candidate audit)

- Claims con apoyo directo suficiente para auditar: 046 (CAND-HAR-003
  + 007 + 015/016 + 040 + CAND-MEL-004/005/013 marcos heredados);
  047 (CAND-HAR-007/009/011/036 + 040 + divorce Spicer/Everett/Doll
  vía reseña + CAND-MEL-001/004/006); 048 (disociación enarmónica OMT
  VERIFIED como analogía estructural + 036 + divorce + 033–035
  marcos); 049 (040–045 + 016 + tesitura CAND-MEL-020 + Sears PARTIAL
  acotado); 050 (028 + 027/029/031/032 + 041/042 + CAND-MEL-014/016/
  017/025/028 marcos); 051 (CAND-MEL-007/008/011 + 026 + 040/043 +
  Margulis marcos); 052 (pedagogía clásica PARCIAL acotada + 015 +
  024/025/037 + Caplin marco + CAND-MEL-013/026 marcos).
- Records UNVERIFIED no sostienen ningún claim: solo delimitan marcos
  y gaps (jazz, priming con melodía, corpus con juicios). Gate: PASS
  con alcance declarado (ver sección "Candidate Audit Evidence Gate"
  en la síntesis). Audit de candidatos NOT STARTED en esta tarea:
  046–052 quedan como `candidate` pendientes de auditoría epistémica.
