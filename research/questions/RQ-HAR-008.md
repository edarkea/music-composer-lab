# RQ-HAR-008 — Bajo, inversión, sonoridad y voicing como decisiones de composición

## Status

INVESTIGATED + SYNTHESIZED (direct source verification: PARTIAL — see below;
candidate_audit_evidence_gate: PASS (see gate section);
candidate_audit_status: COMPLETED (epistemic audit, no new thematic research;
CAND-HAR-040–045: all REVISE, no split, no CAND-HAR-046, no rejections);
lifecycle unchanged: no promotion to manual/ or rules/; NOT solved).

## Central Question

"How do bass position, inversion, spacing, register, doubling, omission,
voice allocation, and realized sonority interact with harmonic identity,
function, continuity, center attribution, and arrival, and which of these
relationships are structural, perceptual, stylistic, or merely pedagogical?"

Formulación orientada a composición:

"Dada una armonía o relación armónica, ¿cómo decide un compositor qué poner
en el bajo y cómo distribuir sus notas entre registros/voces para obtener la
organización estructural deseada sin asumir que el cifrado determina una
única realización?"

## Scope

Conocimiento general dentro de la música popular tonal/modal occidental y
tradiciones estrechamente relacionadas (common practice, pop, rock,
electrónica/dance, prácticas modales, songwriting, cognición musical).
`general` NO significa universal para toda la música humana.

Toda la evidencia perceptiva reseñada utiliza oyentes enculturados en la
tradición tonal occidental salvo indicación explícita. Ver síntesis en
`research/domain/harmony/bass-inversion-voicing.md`.

Restricciones del encargo aplicadas:

- NO iniciar RQ-HAR-007 (modulación solo como dependencia/frontera).
- NO iniciar RQ-HAR-009 (interfaz melodía-armonía: solo dependencias registradas, no resueltas).
- NO modificar Harmony Foundations v0 (`research/integrations/harmony-foundations-v0.md`): es snapshot previo.
- NO promociones a `manual/` ni `rules/`.
- NO `genres/`, NO `experiments` (EXP-002 sigue PAUSED; ningún EXP-HAR).
- NO music-engine; NO MIDI/audio.
- NO modificar CAND-HAR-001–039, RQ-HAR-001–006, archivos Melody, ni ningún otro documento fuera de los tres entregables.
- Melody Foundations (`research/integrations/melody-foundations-v0.md`)
  consultada solo donde registro / identidad de pitch / línea de bajo
  interactúan materialmente. Ningún candidato MEL modificado.
- Skills `.agents/skills/research-music-concept/SKILL.md` y
  `.agents/skills/audit-music-knowledge/SKILL.md` aplicadas manualmente.

## Absolute Core Principle (preserved throughout)

```
CHORD SYMBOL != REALIZED SONORITY
ROOT != BASS
```

Una armonía no queda especificada para composición nombrando un acorde.
Toda afirmación de esta RQ conserva estas dos distinciones explícitas.

## Existing Research Incorporated

- `research/ROADMAP.md` (workflow por pregunta, clases de evidencia,
  regla epistémica STRUCTURE → PERCEPTION → COMPOSITION; soporte ortogonal
  `support_basis`).
- `research/domain/harmony/README.md` (fronteras del dominio; bajo como
  variable armónica).
- `research/domain/harmony/HARMONY-ROADMAP.md` (RQ-HAR-008 como sonoridad
  diferida dependiente de 001–006; riesgos: chord symbol = voicing,
  root = bass, complejidad = calidad, equivalencia de inversiones).
- `research/domain/harmony/stability-center.md` y
  `research/questions/RQ-HAR-001.md` (ROOT != BASS; bajo/pedal como indicio
  sin ponderación; CAND-HAR-001–006; pedal que fija vs. pedal que engaña).
- `research/domain/harmony/direction-function.md` y
  `research/questions/RQ-HAR-002.md` (función != etiqueta; root motion
  insuficiente; bajo co-determina dirección; CAND-HAR-007–012).
- `research/domain/harmony/voice-leading.md` y
  `research/questions/RQ-HAR-003.md` (cinco niveles etiqueta/root/bajo/
  inversión/realización; distinción quíntuple pitch/clase/identidad/registro/
  octava; planing; power chords; pedal modal; CAND-HAR-013–020).
- `research/domain/harmony/harmonic-rhythm-prolongation.md` y
  `research/questions/RQ-HAR-004.md` (SAME CHORD SYMBOL != NO HARMONIC
  CHANGE; revoicing/inversión/bajo como cambio de sonoridad; pedal !=
  prolongación; CAND-HAR-021–026).
- `research/domain/harmony/cadence-closure-arrival.md` y
  `research/questions/RQ-HAR-005.md` (cadential 6/4 como ornamento de
  dominante; llegada tónica != cierre; split bajo→músicos /
  soprano→no-músicos en Sears; CAND-HAR-027–032).
- `research/domain/harmony/chromatic-expansion.md` y
  `research/questions/RQ-HAR-006.md` (disociación enarmónica CTo7/aplicado
  y CT+6/Ger+6: mismas alturas, distinta función; cadential 6/4 como
  mediación aplicada; CAND-HAR-033–039).
- `research/integrations/harmony-foundations-v0.md` (snapshot previo;
  orden práctico HAR-001…HAR-006 → HAR-008 → HAR-007 → HAR-009; bloqueos
  CAND-HAR-002/005/019 preservados).
- `research/integrations/melody-foundations-v0.md` (tres niveles de registro
  PHYSICAL/PERCEPTUAL/COMPOSITIONAL; transposición pequeña con penalización
  parcial EXP-001 B=3; registro seccional como marcador con haz;
  tesitura habitable; solo lo materialmente relevante).
- Fuentes ya registradas y reutilizadas aquí (sin reabrir):
  SRC-ACADEMIC-028 (Spicer 2017, VERIFIED), SRC-ACADEMIC-029 (Everett 2004,
  VERIFIED), SRC-ACADEMIC-030 (Temperley 2011, VERIFIED),
  SRC-ACADEMIC-031 (de Clercq 2018, VERIFIED como reseña),
  SRC-PEDAGOGICAL-001/002 (Schoenberg/OMT forma), SRC-PEDAGOGICAL-009/010/
  011/012/013 (OMT Schemas, Tonicization, Mixture, Aug6, Common-Tone,
  VERIFIED), SRC-THEORETICAL-002 (Caplin), SRC-THEORETICAL-017 (OMT
  Mediants, VERIFIED), SRC-EMPIRICAL-014 (puntero de pasajes bajo/pedal),
  SRC-EMPIRICAL-016 (Sears, PARTIAL), SRC-CORPUS-007/009 (Doll vía reseña;
  de Clercq & Temperley 2011, PARCIAL).

## Source Set (this RQ)

Sin inspección externa nueva en esta sesión: la búsqueda web devolvió 403
(igual que en las sesiones de RQ-HAR-002–004), de modo que ningún texto
completo nuevo fue inspeccionado. La síntesis descansa en fuentes ya
inspeccionadas del repositorio (arriba) más las delimitaciones de marco
registradas abajo. Ningún metadato se inventa.

Texto completo ya inspeccionado y reutilizado directamente (VERIFIED,
sin reabrir):

- SRC-ACADEMIC-028 (Spicer 2017): tónicas frágiles por inversión;
  pedal que fija centro ("Sara") vs. pedal que engaña ("Human");
  factores de vamp de dos acordes (§12: acento duracional, pedal de bajo,
  alturas melódicas enfatizadas, orden de acordes); soul-dominant;
  V perpetuo sin resolución.
- SRC-ACADEMIC-029 (Everett 2004): pedal/drone modal ("Tomorrow Never
  Knows"); seis sistemas tonales sin comportamiento común.
- SRC-ACADEMIC-030 (Temperley 2011): scalar shift (CENTER != COLLECTION);
  tendencia métrica citada (primario Temperley 2001 no inspeccionado).
- SRC-ACADEMIC-031 (de Clercq 2018, reseña de Doll 2017): mismo loop con
  distinto centro según metro/textura/paralelismo (Doll cap.6);
  intuición-vs-corpus (fn6).
- SRC-PEDAGOGICAL-010/011/012/013 + SRC-THEORETICAL-017 (OMT, VERIFIED):
  tonicalización aplicada (incluida mediación por cadential 6/4);
  mezcla modal; sexta aumentada; acordes de tono común CTo7/CT+6 con
  disociación enarmónica (mismas alturas, distinta función);
  taxonomía de mediantes (sin función).
- SRC-EMPIRICAL-014 (puntero de pasajes inspeccionados, PARCIAL):
  pedal que fija / pedal que engaña / convergencia melodía-sobre-bajo.

Heredado PARTIAL (extractos, textos completos pendientes; sin elevar
su estatus en esta tarea):

- SRC-EMPIRICAL-016 (Sears 2014/2015): ratings de completitud 1–7 en
  extractos Mozart/teclado; estabilidad del bajo predice en músicos,
  soprano en no-músicos; cadential 6/4 como predictor; betas/R² NO
  utilizables como pesos compositivos.
- SRC-CORPUS-009 (de Clercq & Temperley 2011): distribuciones como
  conteo, no como fuerza/conducción.
- SRC-CORPUS-007 (Doll 2017, vía reseña): esquemas, pre-tónicas,
  ambigüedad configurable.

UNVERIFIED / deuda de marco (existencia solamente, sin claim citable,
sin sostener ningún candidato):

- Taxonomía de inversiones y bajo cifrado (figured bass) como sistema
  pedagógico de práctica común.
- Duplicación/spacing SATB como normas pedagógicas de tradición.
- Voicings jazz (shell, rootless, guide tones, drop) como pedagogía
  de tradición.
- Teorías psicoacústicas de fundamental/root (Terhardt virtual pitch,
  Parncutt) como marcos en disputa.
- Rugosidad / critical bandwidth en registro grave como marco acústico.
- Práctica pop/rock de power chords, slash chords y bass ostinato más
  allá de los pasajes Spicer inspeccionados.
- Literatura de priming armónico bajo inversión; key-finding con
  manipulación de bajo (GAP; localizar).

Ver tabla "Sources" en
`research/domain/harmony/bass-inversion-voicing.md`.

## Candidate Claims Produced

- CAND-HAR-040 (cifrado no especifica realización; selección y realización
  como decisiones separadas; COMPOSITION HEURISTIC negativa;
  POSSIBLE_WITH_SCOPE).
- CAND-HAR-041 (root/bajo como DISTINCT VARIABLES que pueden divergir;
  trayectoria del bajo como capa a coordinar, sin ponderación ni técnica;
  HYPOTHESIS; POSSIBLE_WITH_SCOPE diagnóstico).
- CAND-HAR-042 (anti-regla de jerarquías de inversión + taxonomía 6/4
  parcial; COMPOSITION HEURISTIC negativa; POSSIBLE_WITH_SCOPE).
- CAND-HAR-043 (realización→configuración concreta de conducción, núcleo
  voice-leading; llegada/identidad cedidas a 028/040/036;
  COMPOSITION HEURISTIC débil analítica; POSSIBLE_WITH_SCOPE).
- CAND-HAR-044 (anti-generalización de duplicación/omisión con mitades
  separadas; jazz como GAP puro; sin split a 046; HYPOTHESIS;
  POSSIBLE_WITH_SCOPE).
- CAND-HAR-045 (registro/spacing como dimensiones de sonoridad sin
  determinar función; prominencia retirada; COMPOSITION HEURISTIC
  negativa; POSSIBLE_WITH_SCOPE).

IDs 001–039 no reutilizados. Ningún claim pasa a `manual/` ni `rules/`
sin revisión y aprobación del Project Owner y del Music/Methodology
Director. Audit de candidatos NO realizado en esta tarea.

## Unresolved Issues

- Ponderación perceptiva bajo-vs-root en atribución de centro y en
  función (ninguna medida dedicada inspeccionada; CAND-HAR-002 sigue
  bloqueado para ponderación).
- Si existe medida que distinga root-position de primera inversión en
  percepción (GAP; literatura de priming/inversión por localizar).
- Criterios de identidad armónica bajo voicing (cuándo un revoicing se
  vuelve armonía distinta; dependencia de marco).
- Curva dosis→efecto para spacing/registro/duplicación (inexistente;
  solo cautelas negativas).
- Transferencia de reglas SATB fuera de texturas a voces estables (sin
  apoyo inspeccionado).
- Audición de fundamentales implicadas con root omitido (sin medida;
  no inferir percepción desde etiqueta de análisis).
- Interacción top-voice/melodía en la elección de inversión (cede a
  RQ-HAR-009).
- Papel del bajo en modulación (frontera RQ-HAR-007, solo dependencias).

## Further External Research Needed

Inspección directa pendiente (ordenada por leverage para RQ-HAR-008):

1. Doll 2017, texto completo (sintaxis pop, inversión/slash, cap.6).
2. Nobile 2016, texto completo (función vs. numeral; divorce).
3. Literatura de priming armónico bajo inversión y de key-finding con
   manipulación de bajo (localizar; medida dedicada).
4. Pedagogía clásica textual (Piston, Schoenberg SFH, Aldwell-Schachter,
   Kostka-Payne): pasajes de inversión, duplicación y spacing.
5. Corpus pop/rock de bajo/inversión con metodología declarada
   (slash chords, pedal, ostinatos, power chords).
6. Pedagogía jazz registrada antes de citar (shell/rootless/guide tones;
   transferencia acotada).
7. Terhardt/Parncutt y literatura de roughness en registro grave
   (textos primarios; solo-marco hasta inspeccionar).
8. Temperley 2001 (primario métrico) y Sears 2014/2015 (textos
  completos; betas como descriptores de tarea, nunca como pesos).
9. Corpus pop/rock con juicios de oyentes sobre inversión/voicing
   (GAP; excede esta RQ pero se registra).

## Further Experiment Currently Justified

NO. Ningún experimento propio en esta tarea (prohibido por el encargo;
EXP-002 sigue PAUSED). La síntesis alcanza estado SYNTHESIZED con
confianza provisional/baja-media según claim. Futuras preguntas
falsables candidatas se registran en la sección "Need for Experiment"
de la síntesis sin diseñar ningún experimento.

## Evidence-Sufficiency Gate (for later candidate audit)

- Claims con apoyo directo suficiente para auditar: CAND-HAR-040 (OMT
  Common-Tone VERIFIED + Spicer fragile-tonic/inversión VERIFIED + Doll
  vía reseña + CAND-HAR-016/036 heredados + HAR-004 same-symbol),
  CAND-HAR-041 (Spicer pedal-fija/engaña + vamp-§12 VERIFIED + Everett
  pedal modal VERIFIED + CAND-HAR-002/009 heredados, sin ponderación),
  CAND-HAR-042 (Spicer §§3/7 VERIFIED + OMT cadential-6/4 VERIFIED +
  Sears PARTIAL acotado a tarea + CAND-HAR-003/008/015 heredados),
  CAND-HAR-043 (CAND-HAR-019 heredado + OMT enarmónica VERIFIED + Sears
  split PARTIAL + Melody EXP-001 B=3 como indicio propio + Bregman
  solo-marco), CAND-HAR-044 (pedagogía PARCIAL sin texto + power-chord/
  planing vía Spicer/Doll + CAND-HAR-015/017/020 heredados; mitad jazz
  como GAP declarado), CAND-HAR-045 (CAND-HAR-003 heredado + Sears
  PARTIAL acotado + Melody registro PHYSICAL/PERCEPTUAL + marcos
  acústicos UNVERIFIED sin sostener nada).
- Records UNVERIFIED no sostienen ningún claim: solo delimitan marcos
  y gaps. Gate: PASS con alcance declarado (ver sección
  "Candidate Audit Evidence Gate" en la síntesis). Audit de candidatos
  COMPLETED (esta tarea): 040/041/042/043/044/045 → REVISE +
  POSSIBLE_WITH_SCOPE; sin split (046 no creado); sin rechazos; 043
  supera el overlap test por núcleo voice-leading; 044 conserva una sola
  anti-regla con mitades separadas; jazz permanece GAP puro no-citable;
  frontera de sonoridad aplicada (timbre fuera, CROSS_DOMAIN_REQUIRED);
  ver `verification_note` en cada YAML.
