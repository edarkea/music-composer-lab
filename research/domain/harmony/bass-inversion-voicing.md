# RQ-HAR-008 — Bajo, inversión, sonoridad y voicing: síntesis

## Research Question

"How do bass position, inversion, spacing, register, doubling, omission,
voice allocation, and realized sonority interact with harmonic identity,
function, continuity, center attribution, and arrival, and which of these
relationships are structural, perceptual, stylistic, or merely pedagogical?"

Formulación compositiva: dada una armonía o relación armónica, ¿cómo decide
un compositor qué poner en el bajo y cómo distribuir sus notas entre
registros/voces para obtener la organización estructural deseada sin asumir
que el cifrado determina una única realización?

## Scope

Síntesis dentro del scope del proyecto: música popular tonal/modal
occidental y tradiciones estrechamente relacionadas. `general` NO significa
universal. Toda evidencia perceptiva citada utiliza oyentes enculturados
occidentales salvo indicación explícita.

Estado: SYNTHESIZED (confianza global: provisional; por claim: ver matriz
y candidatos CAND-HAR-040–045). No poblar `manual/` ni `rules/`.

Nota de verificación: sin inspección externa nueva en esta sesión (búsqueda
web 403, igual que en RQ-HAR-002–004). La síntesis descansa en fuentes ya
inspeccionadas del repositorio: Spicer 2017, Everett 2004, Temperley 2011,
de Clercq 2018 (reseña de Doll), capítulos OMT VERIFIED (Tonicization,
Modal Mixture, Augmented Sixth, Common-Tone Chords, Mediants, Modal
Schemas), Sears 2014/2015 (PARTIAL, extractos), corpus de Clercq &
Temperley 2011 (PARCIAL), más candidatos CAND-HAR-001–039 heredados y
Melody Foundations v0 en lo materialmente relevante. Ningún metadato se
inventa. Ver § Sources y `research/questions/RQ-HAR-008.md`.

Principio nuclear preservado en toda la síntesis:

```
CHORD SYMBOL != REALIZED SONORITY
ROOT != BASS
```

## Terminology

Distinciones obligatorias del encargo (no colapsar; cada par se trata por
separado en toda la síntesis):

- ROOT != BASS. La fundamental analítica y la nota grave realizada son
  variables independientes (heredado RQ-HAR-001).
- LOWEST NOTE != ROOT. La nota más grave no determina la fundamental.
- BASS NOTE != BASS LINE FUNCTION. Una altura grave y su rol (miembro del
  acorde, pedal, línea, ancla) son niveles distintos.
- INVERSION != VOICING. La inversión nombra qué grado ocupa el bajo; el
  voicing es la realización completa.
- INVERSION != SPACING. Inversión y distribución interválica son
  independientes.
- VOICING != REGISTER. La misma disposición relativa en otra zona es otra
  realización.
- REGISTER != SPACING. Zona absoluta y distancias entre voces vecinas.
- SPACING != VOICE IDENTITY. Distancias y asignación a voces estables.
- DOUBLING != FUNCTION. Duplicar no asigna rol.
- DOUBLING != PERCEPTUAL WEIGHT automáticamente.
- OMISSION != FUNCTION LOSS automáticamente.
- ROOT POSITION != GREATER STABILITY universalmente.
- FIRST INVERSION != SMOOTHER VOICE LEADING automáticamente.
- SECOND INVERSION != INSTABILITY universalmente.
- CLOSE POSITION != BETTER CONNECTION.
- OPEN POSITION != MORE POWER / SPACE / EMOTION.
- LOW BASS != STRONGER TONIC.
- BASS 5→1 != CADENCE por sí solo.
- PEDAL != ROOT; PEDAL != PROLONGATION automáticamente.
- SLASH CHORD != NEW CHORD FUNCTION automáticamente.
- VOICE COUNT != HARMONIC COMPLEXITY.
- SONORITY != HARMONIC FUNCTION; SONORITY != CHORD LABEL.

Vocabulario heredado: ESTABLISH / CONFIRM / MAINTAIN / WEAKEN / AMBIGUATE
(estados relativos al centro, RQ-HAR-001). El vocabulario de metas
(STAY/DEPART/…) sigue no adoptado; esta síntesis usa prosa provisional.

Definición de trabajo de `voicing` (alcance de esta síntesis, no oficial
del proyecto): realización concreta de una armonía especificada por, de
forma separable: (a) pitch classes incluidas; (b) alturas exactas;
(c) registro; (d) spacing entre voces adyacentes; (e) duplicación;
(f) omisión; (g) asignación a voces; (h) bajo; (i) nota superior;
(j) número de voces sonantes. Ningún marco revisado usa `voicing` con
exactamente estos diez componentes; se registra la divergencia
terminológica como hecho, no como problema a resolver aquí.

Definición de trabajo de `sonority`: evento vertical realizado con su
estructura interválica, registro y disposición — distinto de CHORD IDENTITY
(adscripción analítica a una clase de acorde bajo un marco) y distinto de
VOICING solo en énfasis (sonoridad = lo que suena; voicing = cómo se
distribuye). Timbre/producción es dependencia cross-domain, no parte de
Harmony salvo evidencia en contrario.

## Root vs Bass

Hallazgo organizador: root y bajo son dos variables con lógicas propias
que co-determinan centro, función y dirección sin sustituirse.

- ROOT (fundamental): constructo analítico asignado por un marco (p. ej.,
  fundamental de tríada/séptima en nomenclatura de práctica común; objeto
  en disputa fuera de ella). No es observable bruto: fuera de repertorio
  triádico, su asignación depende del marco declarado.
- BASS (bajo): altura grave realizada, observable. Conlleva saliencia
  auditiva propia (registro grave, posible duplicación por instrumentación)
  pero sin peso causal medido frente al root (CAND-HAR-002, NOT_READY).
- LOWEST NOTE (nota más grave): hecho acústico instantáneo; puede no
  coincidir con el bajo funcional (cruces, doblajes, transitorios) ni con
  el root.
- Lo que el bajo aporta y el root no: posición registral real, trayectoria
  lineal audible (la línea de bajo es melodía grave), anclaje rítmico
  (sincronía con batería/percusión en groove), y rol de pedal/drone por
  insistencia. Ninguno de estos es deducible del root.
- Lo que el root aporta y el bajo no: identidad de clase (qué colección de
  pitch classes se nombra), root motion como descriptor de sucesión,
  anclaje a esquemas de repertorio expresados en roots.
- Estatus: THEORY acotada (distinción analítica) + HYPOTHESIS (peso
  relativo). Sin medida dedicada que aísle bajo de root en atribución de
  centro o función (GAP heredado). La IA NO debe: inferir centro desde
  bajo, prescribir pedal como fijador, ni tratar root y bajo como
  intercambiables.

## Bass Roles

Roles analíticos posibles del bajo (posibilidades, no categorías
oficiales exhaustivas):

1. Miembro del acorde en estado fundamental (bajo = root).
2. Tono definitorio de inversión (tercera o quinta en bajo).
3. Pedal/drone (altura sostenida o repetida bajo armonía móvil o estática).
4. Línea melódica grave (bajo andante, walking, contramelodía).
5. Voz contrapuntística con lógica propia (movimiento contrario/oblicuo).
6. Ancla registral (fondo grave sin rol lineal).
7. Patrón recurrente (riff/ostinato).
8. Non-chord tone (retardo, anticipación, pedal no-armónico).
9. Bajo de slash chord (función lineal independiente de la estructura
   superior).
10. Parte de trayectoria de conducción a gran escala (línea de bajo
    estructural, p. ej., descenso por grados).

Cada rol se evalúa con su propia evidencia; ningún rol es el "verdadero"
bajo. Pregunta diagnóstica permanente: ante un bajo dado, ¿qué rol
desempeña en este contexto y qué evidencia lo establece?

## Bass and Tonal Center

Revisión de CAND-HAR-002 (sin editarlo): el bajo contribuye a la
atribución de centro como indicio derrotable entre varios, sin
ponderación establecida.

- A favor (analítico, VERIFIED): pedal F que fija centro ("Sara", Spicer
  §15); tónicas frágiles precisamente por inversión (Spicer §§3/7: la
  inversión debilita jerárquicamente la tónica presente); factores de
  vamp de dos acordes incluyendo pedal de bajo y acento duracional
  (Spicer §12); pedal modal con colección y repetición (Everett §10).
- En contra (analítico, VERIFIED): pedal D♭ que NO fija centro y genera
  expectativa fallida ("Human", Spicer §15); metro/textura/paralelismo
  que desambiguan loops idénticos con independencia del bajo (Doll cap.6
  vía reseña); convergencia melodía-sobre-bajo que decanta la atribución
  ("Reach Out", Spicer §5).
- Prohibido: root-en-bajo = tónica como regla; tónica-en-bajo = función
  de tónica; pedal = centro. La ponderación bajo-vs-root sigue sin medir.
- Resultado para CAND-HAR-002: MORE SUPPORT a nivel de distinción y de
  casos (la inversión/bajo afectan materialmente la atribución analítica),
  STILL BLOCKED como guía accionable (sin pesos, sin medida dedicada, sin
  `possible_action`). Ver § Existing-Candidate Blocker Audit.

## Bass and Harmonic Function

Continuación de HAR-002 con el bajo como variable separada.

- Mismo root + distinto bajo: puede preservar la función con distinto rol
  local (p. ej., I6 como prolongación/paso frente a I como llegada en
  marco clásico), o reinterpretarse (pedal que engaña; cadential 6/4 como
  ornamento de dominante, no como tónica). La inversión no cambia la
  etiqueta de función por sí sola; cambia la configuración que el marco
  lee.
- Mismo bajo + distinto root/estructura superior: pedal bajo cambios
  superiores (Spicer: fija o engaña según contexto); la trayectoria grave
  aporta información direccional propia (descensos/ascensos de bajo con
  armonía superior móvil), pero inferir función solo desde el intervalo
  de bajo es el mismo error que con root motion (CAND-HAR-009 extendido
  al bajo: insuficiencia, no irrelevancia).
- ¿Puede la inversión cambiar la función? Respuesta delimitada: dentro de
  un marco declarado, ciertas inversiones reciben lecturas funcionales
  distintas (cadential 6/4 = dominante, no tónica; I6 con rol de paso).
  Fuera del marco, `uncertain`. Ningún marco revisado se adopta como
  universal.
- ¿Puede el pedal contradecir la armonía superior? Sí, documentado
  ("Human"): el pedal es indicio derrotable, no operador de centro ni de
  función.

## Bass Trajectory

El movimiento del bajo como variable compositiva propia (operaciones
disponibles como descripciones, sin efecto garantizado):

repetición del bajo; pedal; bajo por grados; moción por quintas; moción
por terceras; bajo cromático; línea descendente/ascendente; bajo contrario
a voces superiores; salto de bajo con voces superiores quietas; ostinato
de loop.

- Cada operación se registra con root motion, conducción superior, metro
  y esquema por separado (herencia CAND-HAR-009: ninguna moción sola
  determina función).
- HAR-003: bass motion != voice leading completo. La conducción del bajo
  es una voz; la conexión total incluye voces superiores e interiores.
- El ostinato/riff de bajo en loop-based music organiza por insistencia
  y sincronía rítmica (Spicer §§10/15; dependencia Arrangement), no por
  sintaxis dirigida.

## Root Position

Auditoría de claims pedagógicos/teóricos sobre el estado fundamental
(estabilidad, identidad, llegada, función, finalidad):

- Contenido estructural real: en pedagogía clásica, el estado fundamental
  es posición de referencia taxonómica (figured bass como sistema de
  notación/análisis de tradición; marco-existencia UNVERIFIED, sin texto
  inspeccionado) y, en repertorio clásico, configuración habitual de
  llegada estructural. Alcance: tradición acotada.
- Contenido perceptivo: NINGUNA medida dedicada inspeccionada compara
  root-position con inversiones aislando solo el bajo (GAP). Sears
  (PARTIAL, tarea 1–7 Mozart/teclado) muestra que la estabilidad del bajo
  predice completitud en músicos, pero no compara posiciones de la misma
  armonía ni establece jerarquía perceptiva general.
- Contenido analítico pop (VERIFIED): la tónica en estado fundamental es
  la configuración no-marcada; su ausencia (inversión) fragiliza la
  tónica presente (Spicer). Esto establece que la inversión MODULA la
  lectura analítica, no que el estado fundamental sea perceptivamente más
  estable en general.
- Veredicto por claim (THEORY? PEDAGOGY? CORPUS? PERCEPTION?): mayor
  estabilidad = PEDAGOGÍA/TRADICIÓN acotada, sin puente perceptivo;
  mejor identidad = ANALÍTICO acotado (fragilidad por inversión);
  llegada más fuerte = depende de soprano/metro/posición (Sears PARTIAL;
  CAND-HAR-028); finalidad preferente = convención de repertorio, no ley.
- La jerarquía textbook NO se traduce a verdad perceptiva (cruce con
  CAND-HAR-003: consonancia != estabilidad se extiende a inversión).

## First Inversion

Qué cambia realmente la primera inversión (marcos acotados, sin
universales):

- Roles teóricos documentados (práctica común, pedagogía PARCIAL sin
  texto + OMT VERIFIED donde aplica): suavidad de línea de bajo
  (conexión por grados); uso prolongacional/lineal (paso, bordadura);
  menor énfasis del root (tónica frágil, Spicer VERIFIED en pop).
- Ninguno asumido universalmente. "Más suave" presupone textura a voces
  estables y norma de tradición; en voicings de guitarra/teclado pop la
  conducción opera bajo otras restricciones (HARMONY-ROADMAP, sin
  investigación dedicada: GAP).
- Evidencia empírica que distinga root de primera inversión en
  percepción: NO localizada (GAP; priming armónico bajo inversión por
  localizar). Sin ella, toda preferencia por primera inversión para
  "suavizar" es heurística de tradición con escucha obligatoria, no regla.

## Second Inversion / Six-Four

Descomposición obligatoria: NO existe "la segunda inversión" como un
fenómeno. Categorías dependientes de marco (práctica común; ninguna
oficial del proyecto):

- Cadential 6/4 (I6/4–V–I): suspensión ornamental de la dominante, no
  acorde de tónica (OMT Augmented Sixth VERIFIED: Ger+6 resuelve a V a
  menudo vía cadential 6/4; síntesis HAR-005 auditada; predictor
  de llegada cadencial en Sears PARTIAL, descriptivo). Su "inestabilidad"
  es rol de dominante ornamentada, no propiedad de la inversión.
- Passing 6/4: sonoridad de paso entre dos armonías (rol de marco
  clásico; textos pedagógicos pendientes de inspección — no sostiene
  sub-claims).
- Pedal 6/4: bajo pedal con voces superiores móviles (rol de marco
  clásico; textos pendientes — no sostiene sub-claims).
- Arpeggiating 6/4: despliegue del bajo (rol de marco clásico; textos
  pendientes — no sostiene sub-claims).
- Sonoridad independiente de segunda inversión en otros estilos
  (tónica frágil por inversión en pop, Spicer VERIFIED; sin taxonomía
  propia: GAP).

Pregunta "¿inestabilidad de la inversión o interpretación de tradición?"
Respuesta: con la evidencia revisada, la segunda es la formulación
sostenible — la inestabilidad atribuida a 6/4 vive en roles declarados
por marcos acotados, y el único efecto analítico general es la
fragilización por inversión (Spicer). Ninguna medida perceptiva general
de 6/4 fue inspeccionada.

## Inversion and Arrival

Continuación de HAR-005 con realización:

- La llegada cadencial clásica puede mediar cadential 6/4 (I6/4–V–I)
  como señalización de llegada (Sears: predictor; OMT: ornamento de
  dominante). Sin 6/4 la llegada es analíticamente más débil en ese
  marco; fuera de él, `uncertain`.
- Bass 5→1 NO constituye cadencia por sí solo: sin proceso cadencial
  declarado (stages, posición formal, sintaxis de tradición) es llegada
  de bajo, no cierre (CAND-HAR-027/028 heredados).
- Soprano/bajo combinados: el split Sears (bajo→músicos,
  soprano→no-músicos; disonancia melódica como modulador) es el único
  dato empírico directo sobre registración de llegada, acotado a tarea
  1–7 / Mozart / teclado. Ningún score de fuerza cadencial se crea;
  ningún coeficiente se convierte en peso compositivo.
- Tareas preservadas exactamente: ratings de completitud 1–7, músicos vs.
  no-músicos, repertorio Mozart/teclado (SRC-EMPIRICAL-016, PARTIAL).

## Pedal / Drone

Continuación de HAR-001/003/004, consolidada:

- Aportes documentados (analíticos, VERIFIED): continuidad por insistencia
  grave; centro modal con colección+repetición; reinterpretación de la
  armonía superior (fija o engaña); organización cíclica (vamp de un
  acorde; pedal electrónico/drone análogo funcional).
- Límites (VERIFIED en ambas direcciones): PEDAL != CENTER ("Human");
  PEDAL != ROOT (pedal no-armónico); PEDAL != PROLONGATION automática
  (convención HAR-004 de cinco ranuras obligatoria para toda lectura
  prolongacional).
- En loop/groove, el pedal/drone sostiene interés formal cuando otras
  dimensiones cambian (CAND-HAR-026; dependencia Arrangement/Production).

## Slash Chords

Terminología y diferencias estructurales reales:

- Slash = inversión (p. ej., C/E como primera inversión): lectura
  suficiente cuando el bajo es miembro del acorde y la estructura
  superior conserva identidad.
- Slash con función lineal independiente: el bajo opera como
  contrapunto/línea (bajo andante, cromatismo) y la notación
  upper-structure/bajo describe mejor la organización que la inversión.
- Misma estructura superior + distinto bajo: puede reinterpretar centro
  y función (Doll cap.6 vía reseña: configuración desambigua; Spicer
  pedal bidireccional). Sin medida de oyentes: diagnóstico analítico,
  no efecto perceptivo establecido.
- Ninguna ontología universal de slash chords se crea; la notación slash
  es práctica de cifrado y de lectura, no teoría de función.

## What Voicing Means

Ver § Terminology (diez componentes separables). Consecuencias:

- Dos realizaciones pueden compartir nueve componentes y diferir en uno
  (p. ej., solo el bajo) con consecuencias estructurales distintas:
  la independencia de variables es el hallazgo, no su ponderación.
- `voicing` no viaja entre marcos sin declaración: SATB, jazz
  (drop/shell; pedagogía UNVERIFIED), pop (guitarra/teclado; GAP),
  electrónica (capas; GAP) usan organizaciones distintas. Ninguna
  definición se adopta como oficial.
- Número de voces sonantes, pitch classes distintas y partes registradas
  son tres conteos separados (ver § Number of Voices).

## Chord Identity Under Voicing

Qué puede cambiar manteniendo la adscripción analítica (depende de marco):

- Inversión, duplicación, omisión (típicamente quinta), registro, spacing,
  duplicación de octava: la pedagogía clásica y la práctica pop mantienen
  la etiqueta en estos casos (marco de tradición; pedagogía PARCIAL).
- Alteración de notas definitorias (tercera, séptima, tensiones): cambia
  la clase en casi todos los marcos.
- Caso paradigmático VERIFIED (OMT Common-Tone): CTo7 vs. viio7/aplicado
  y CT+6 vs. Ger+6 comparten alturas con distinta función según vecinos
  y resolución — la identidad depende de contexto, no de contenido
  aislado (herencia CAND-HAR-036; aporte voicing-específico nuevo aquí:
  la realización registral/posicional participa en la lectura).
- Pregunta "¿cuándo un revoicing se vuelve otra armonía?": sin criterio
  general; depende de marco (clásico: bajo/función; pop: esquema/loop;
  jazz: guide tones — GAP). Toda adscripción declara FRAMEWORK.

## Register

Continuación de CAND-HAR-019 y Melody (tres niveles PHYSICAL /
PERCEPTUAL / COMPOSITIONAL):

- same pitch != same pitch class != same register != same voice identity
  (preservado; analítico).
- Efectos con apoyo directo y acotado: penalización parcial de parentesco
  por transposición melódica (EXP-001 B=3, indicio propio aislado n=1, sin
  transferencia a voicing general); registro seccional
  como marcador con haz (Melody GENRE_SPECIFIC); convergencia
  melodía-sobre-bajo (Spicer VERIFIED); split bajo/soprano en llegada
  (Sears PARTIAL).
- Efectos sin apoyo: reconocimiento de acorde bajo inversión/registro
  (GAP); fusión/segregación con estímulos armónicos (Bregman
  solo-marco); equivalencia de octava (GAP); fundamental implicada
  (GAP).
- Lo que bloquea a CAND-HAR-019: ausencia de medida dedicada de
  equivalencia registral en conducción y de ponderación perceptiva del
  registro (ver § Existing-Candidate Blocker Audit). Futuro desbloqueo
  requeriría: literatura streaming/proximidad con estímulos armónicos +
  medida de continuidad con manipulación registral.

## Spacing

- Close/open/wide/compact y gap bajo-superior: descripciones
  estructurales disponibles como vocabulario, sin efecto general
  establecido.
- Pedagogía clásica de spacing (PARCIAL sin texto): marco de tradición,
  no evidencia perceptiva.
- Lenguaje emocional (wide = poderoso/espacioso; close = íntimo/denso):
  NO soportado; prohibido salvo constructo definido con medida directa
  (ninguna inspeccionada).
- "Close = mejor conexión": NO establecido (CAND-HAR-013/014: retención
  literal y movimiento pequeño son heurísticas débiles separadas, sin
  dosis-respuesta; la equivalencia de octava no es retención).

## Low-Register Spacing

- Reglas de orquestación/mezcla sobre intervalos graves: marcos acústicos
  candidatos (fusión armónica, rugosidad, critical bandwidth,
  solapamiento espectral) — UNVERIFIED, sin texto inspeccionado; no
  sostienen ningún claim.
- Separación obligatoria: ROUGHNESS ACÚSTICA != FUNCIÓN ARMÓNICA !=
  CALIDAD COMPOSITIVA. Un voicing grave rugoso puede ser intencional
  (planing, power chords, pedal modal).
- Ninguna regla de spacing grave se convierte en universal armónico.
  GAP: medida de rugosidad con estímulos armónicos musicales y su
  relación con juicios de función/cierre.

## Doubling

Reglas de duplicación de práctica común (root doubling; tendency tones;
duplicación según inversión; leading tone; tercera):

- Estatus: normas pedagógicas de tradición con objetivo declarado
  (independencia de voces + cierre de tendencias en SATB), pedagogía
  PARCIAL sin texto inspeccionado. Para cada regla: tradición = práctica
  común pedagógica; objetivo = teórico/pedagógico; evidencia perceptiva
  = ninguna inspeccionada; contraejemplos = planing, power chords,
  doblajes pop/electrónicos (vía Spicer/Doll); relevancia fuera de SATB
  = no establecida.
- Ninguna regla SATB se codifica como armonía universal (ver
  CAND-HAR-044).

## Omission

- Quinta omitible preservando adscripción (práctica común y pop; marco
  de tradición); shell voicing y power chord (root+quinta) como prácticas
  documentadas en repertorio/análisis (voice-leading synthesis; alcance
  acotado, sin medida).
- Root omitido (rootless jazz; bajo implicado): práctica pedagógica de
  tradición (UNVERIFIED como texto); missing root != no root
  interpretation automáticamente a nivel analítico — pero NINGUNA
  fundamental implicada se afirma perceptivamente sin medida (prohibición
  expresa).
- Tercera omitida: cambia la calidad/clase en casi todos los marcos
  (alcance de tradición).
- Extensiones y tensiones: omisión idiomática por tradición (GAP fuera
  de pedagogía jazz no inspeccionada).

## Number of Voices / Pitch Classes

Tres conteos separados, ninguno equivalente a complejidad, plenitud,
calidad o importancia:

1. Voces sonantes (sounding voices).
2. Pitch classes distintas.
3. Partes registradas (registered parts / streams).

Un power chord (2 pitch classes, N voces) no es "menos complejo" por
conteo; una séptima con 6 voces no es "más rica" por conteo. La
complejidad armónica != calidad compositiva (distinción obligatoria
HARMONY-ROADMAP).

## Outer Voices

Continuación de HAR-003: bajo y voz superior tienen roles documentados
pero no dominancia asumida.

- Bajo: ancla registral, trayectoria lineal, voto en llegada para
  músicos (Sears PARTIAL), co-determinación de centro (Spicer).
- Voz superior: voto en llegada para no-músicos (Sears PARTIAL);
  portadora melódica (cede a RQ-HAR-009: la nota superior es a la vez
  miembro del acorde, evento melódico y destino de conducción — NO se
  resuelve aquí).
- Ninguna jerarquía general bajo-vs-superior se establece; los pesos
  Sears son descriptores de tarea, no pesos compositivos.

## Inner Voices

- No son relleno: portan tonos comunes por semitono, cromatismo de
  conducción, duplicaciones y cambios de color (marco analítico de
  tradición).
- Ninguna afirmación de menor importancia perceptiva sin medida
  (prohibición expresa; GAP).
- En texturas por capas sin voces estables, la asignación
  interior/exterior pierde contenido (herencia HAR-003 voice identity).

## Sonority

Ver definiciones en § Terminology. Separación operativa en análisis:

CHORD IDENTITY (adscripción bajo marco) / REALIZED SONORITY (evento que
suena) / VOICING (distribución) / VERTICAL INTERVAL STRUCTURE (contenido
intervalar) / REGISTER (zona) / TIMBRE-TEXTURE (dependencia Arrangement).

Frontera de sonoridad (auditoría RQ-HAR-008): REALIZED HARMONIC SONORITY
para Harmony significa organización realizada de alturas (alturas exactas,
pitch classes, bajo, registro, spacing, duplicación, omisión, asignación
a voces). Instrumento, timbre, articulación, producción, mezcla y diseño
espectral pertenecen primariamente a Arrangement/Production y se marcan
CROSS_DOMAIN_REQUIRED cuando afecten materialmente la cuestión. `sonority`
nunca es sinónimo de `chord label`.

El color armónico co-deciden clase, voicing y timbre (dependencia
HAR-006 registrada); ningún componente decide solo.

## Sensory Consonance / Roughness

Continuación de CAND-HAR-003 extendida a realización:

- Voicing/registro pueden alterar rugosidad sensorial manteniendo la
  función contextual (casos: tríada consonante en segunda inversión
  escuchada frágil, Spicer §7 VERIFIED; soul-dominant con 7ª/9ª/11ª sin
  leading tone clásico, Spicer §3 VERIFIED). La disociación es
  conceptual/analítica, no independencia psicológica medida.
- Prohibido: voicing más consonante = más estable tonalmente; roughness
  = tensión. La rugosidad puede modular prominencia sin decidir centro
  ni función.
- Tensión como constructo: fuera de alcance (cede a dominio Tension;
  revisión PARTIAL HAR-006 como límite).

## Voice-Leading Interaction

Continuación de HAR-003 a nivel de realización: el mismo par de
etiquetas admite conducciones distintas según voicing.

- Decisiones: qué tonos quedan literales; cuáles se mueven por
  grado/salto; cuáles cambian de octava (no es retención: CAND-HAR-019);
  qué voz recibe cada tono; si las interiores quedan o se mueven.
- Prohibido optimizar por distancia agregada mínima (CAND-HAR-014).
- Revoicing con misma armonía como continuidad deliberada (tono común
  literal, proximidad registral) o como diferenciación (desplazamiento
  deliberado): heurística débil CAND-HAR-013 con escucha obligatoria.
- Intercambio de voces (voice exchange): operación descriptiva de
  tradición; sin efecto general establecido.

## Harmonic-Rhythm Interaction

Dependencia HAR-004: un revoicing de la misma armonía puede o no contar
como onset armónico nuevo.

- Criterio: depende de qué cuenta como cambio armónico bajo el marco
  declarado (etiqueta, bajo, pitch classes, disposición, timbre) y de la
  escucha (onset percibido: dependencia Arrangement sin resolver).
- Prohibido: nuevo voicing = nueva armonía; mismo cifrado = ningún
  evento armónico significativo. La repetición con voicing cambiante es
  estrategia documentada de persistencia sin estatismo (CAND-HAR-024/026;
  `uncertain` en aceleración local de loops).
- Terminología de onset: declarar unidad, ventana y tempo (HAR-004).

## Chromatic Reinterpretation

Continuación de HAR-006: bajo/voicing pueden cambiar la lectura de una
sonoridad cromática (aplicada, tono común, predominante alterada,
inversión, pedal con estructura superior, otra relación).

- Casos VERIFIED: disociación enarmónica CTo7/aplicado y CT+6/Ger+6
  (OMT Common-Tone); cadential 6/4 como sonoridad afiliada a dominante
  (OMT Augmented Sixth + síntesis HAR-005); soul-dominant sin leading
  tone (Spicer §3).
- Interpretación por oyentes: sin medida (GAP CAND-HAR-036). Matriz
  diagnóstica con centro y conducción implicados por lectura; función
  `uncertain` fuera de convergencia.
- Realizar armonía cromática sin cambiar su identidad analítica:
  conservar resolución verificada y rol bajo marco declarado
  (CAND-HAR-037, heurística débil).

## Common-Practice Evidence

Alcance declarado: pedagogía y análisis de práctica común (textos
PARCIAL sin inspección; OMT VERIFIED donde aplica).

- Inversión/figured bass, duplicación, spacing, resolución de tendency
  tones, cadential 6/4, restricciones de paralelas: normas de tradición
  con objetivo declarado, no leyes perceptivas (CAND-HAR-015/017/042).
- Transferencia al pop/loop: NO automática (aceleración capliniana,
  cadencia, prolongación: TRADITION_SPECIFIC con negativas generales).
- Textos completos pendientes (ver RQ § Further External Research).

## Popular / Rock Evidence

Requisito pop obligatorio; solo material con apoyo directo:

- Inversiones que fragilizan tónica; pedal que fija/engaña; vamp de dos
  acordes con factores §12; soul-dominant; V perpetuo (Spicer VERIFIED).
- Mismo loop, distinto centro según configuración (Doll cap.6 vía
  reseña); pre-tónicas y esquemas (Doll vía reseña + corpus PARCIAL).
- Power chords y planing como organización sin retención ni economía de
  movimiento (voice-leading synthesis; alcance acotado).
- Tónica emergente al coro; finales no-tónicos; retorno de loop
  (síntesis HAR-005).
- Ningún ejemplo se convierte en ley de género. Corpus pop/rock de
  bajo/inversión con metodología declarada: GAP.

## Jazz / Transferable Evidence

Solo material transferible con apoyo directo: NINGUNO inspeccionado en
esta tarea más allá de menciones de marco.

- Rootless/shell/guide-tones/drop voicings/bajo independiente:
  pedagogía de tradición (UNVERIFIED como texto). GAP declarado; no se
  cita folklore; no se generaliza pedagogía jazz (ver CAND-HAR-044).
- Principio de transferencia: una práctica jazz solo entra como
  GENRE OBSERVATION acotada con fuente registrada, nunca como ley
  general.

## Electronic / Groove-Based Evidence

Donde hay apoyo (Spicer §§10/15; Butler/Middleton vía Melody):

- Línea de sub/bajo independiente de la armonía superior; pedal/drone;
  patrón de bajo fijo bajo material superior cambiante; redistribución
  de octavas/registro; block chords/planing.
- Producción/timbre como cross-domain (no recomendaciones de mezcla;
  nada acústico prescriptivo sin fuente).
- El cambio formal en estasis armónica viene de capas/densidad/timbre
  (CAND-HAR-026); el voicing electrónico es arreglo tanto como armonía.

## Perceptual Evidence

Estudios directos accesibles con efecto en esta RQ:

- Sears 2014/2015 (PARTIAL, extractos): ratings 1–7 de completitud en
  extractos Mozart/teclado; estabilidad del bajo predice en músicos,
  soprano en no-músicos; cadential 6/4 como predictor; disonancia
  melódica y duración como moduladores. Tarea/población/repertorio
  preservados; sin generalización; sin pesos.
- Probe-tone (Krumhansl, VERIFIED): goodness-of-fit jerárquico, no
  atribución de centro en canciones; contrapeso Butler 1989 (abstract).
- EXP-001 B=3 (indicio propio n=1): penalización parcial por
  transposición; causas no separadas.
- GAPs: inversión/root-position en percepción; reconocimiento de acorde
  bajo inversión; saliencia del bajo aislada; fundamental
  virtual/implicada; fusión/spacing; equivalencia de octava; priming
  bajo inversión; cierre con manipulación de bajo fuera de Mozart.

Para cada estudio futuro registrar: estímulo exacto, tarea, población,
variable manipulada, medida. Prohibido traducir tiempo de reacción en
preferencia o estabilidad.

## Root Perception / Virtual Root

Separación crítica (no intercambiables):

ACOUSTIC/VIRTUAL PITCH (fundamental faltante, Terhardt/Parncutt como
marcos UNVERIFIED) != MUSIC-THEORETICAL ROOT (adscripción de marco) !=
BASS (altura realizada) != TONAL CENTER (organización percibida) !=
HARMONIC FUNCTION (rol contextual).

Ninguna teoría psicoacústica de root inspeccionada; no se afirma nada
sobre percepción de fundamentales. La confusión entre estos cinco
constructos es el error de método central que esta RQ prohíbe.

## Corpus / Repertoire Evidence

- Repertorio cercano VERIFIED: Spicer (fragilidad, pedal, vamp,
  soul-dominant, V perpetuo, divorce); Everett (sistemas, pedal modal);
  Temperley (scalar shift); Doll vía reseña (esquemas, ambigüedad
  configurable); Biamonte por puntos (patrones eolios).
- Corpus PARCIAL: de Clercq & Temperley 2011 (distribuciones/transiciones
  como conteo); corpus cromático rock Tabla 2 (conteo).
- GAPs estructurales: corpus pop/rock de bajo/inversión/voicing con
  metodología; corpus con juicios de oyentes; corpus registral por
  sección (GAP-11 Melody).

## Theoretical Frameworks

Marcos en su alcance, ninguno oficial: Rameau/funcional/riemanniana;
Schenker (solo-marco analítico); Schoenberg/Piston/Aldwell-Schachter
(pedagogía PARCIAL); Lerdahl/TPS/GTTM (solo-marco); Temperley
(cognición); Tymoczko (deuda UNVERIFIED); neo-riemanniana (sin uso
perceptivo); Nobile/de Clercq/Doll/Stephenson/Everett/Summach/Tagg
(pop/rock, alcance declarado); jazz (GAP). Caplin (sentence/cadencia,
VERIFIED vía texto/reseña, acotado a clásica).

## Operation Matrix

Solo operaciones con apoyo o GAP declarado; sin intuición (`uncertain`
donde no hay apoyo). Columnas: Operation | Root changes? | Bass changes?
| Pitch classes change? | Register/spacing change? | Possible structural
role | Perceptual evidence | Theory/corpus evidence | Scope |
Alternatives | Confidence.

| Operation | Root? | Bass? | PC? | Reg/spacing? | Possible structural role | Perceptual evidence | Theory/corpus evidence | Scope | Alternatives | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| Root-position → first inversion | no | yes | no | maybe | Fragilizar tónica; suavizar línea de bajo; paso/prolongación | none dedicated (GAP) | Spicer fragile VERIFIED; pedagogía PARCIAL | Tradición acotada + pop (fragilidad) | Revoicing sin cambio de bajo | media-baja |
| Root-position → second inversion (cadential) | no (lectura: V) | yes (5̂) | no | maybe | Señalizar llegada cadencial como ornamento de dominante | Sears PARTIAL (predictor, tarea acotada) | OMT VERIFIED; Caplin | Clásica | V sin 6/4 | media-baja |
| Same upper triad, changed bass | no | yes | maybe | yes | Reinterpretar centro/función; línea de bajo | none (GAP) | Doll cap.6 vía reseña; Spicer pedal | General (negativo) + pop | Cambio de root | baja-media |
| Pedal bass under upper changes | maybe | no | yes | no (bajo) | MAINTAIN modal/cíclico; reinterpretación | none dedicated | Spicer ambos sentidos VERIFIED; Everett VERIFIED | Modal/pop/loop | Bajo móvil | media-baja (bidireccional) |
| Retained bass while root changes | yes | no | yes | maybe | Continuidad grave; pedal invertido | none (GAP) | Spicer vamp §12 (factores) | Pop/loop | Pedal literal | baja |
| Octave-displace one chord member | no | maybe | no | yes | Re-encuadre registral; diferenciación | EXP-001 B=3 indicio | CAND-HAR-019 analítico | General (analítico) | Retención literal | baja |
| Double root | no | maybe | no | yes | Refuerzo grave/agudo según registro | none (GAP) | Pedagogía PARCIAL | SATB | Duplicar otro tono | baja |
| Double third | no | maybe | no | yes | Color/equilibrio (marco) | none (GAP) | Pedagogía PARCIAL (restringida) | SATB | Duplicar root | baja |
| Omit fifth | no | no | yes (-1) | maybe | Adscripción preservada; shell/power | none (GAP) | Práctica documentada (acotada) | Clásica/pop | Conservar quinta | media-baja |
| Omit root | `uncertain` (marco) | maybe | yes (-1) | maybe | Sonoridad sin bajo fundamental (jazz) | none (GAP) | Pedagogía UNVERIFIED | Jazz (GAP) | Conservar root | `uncertain` |
| Close → open spacing | no | no | no | yes | Cambio de sonoridad sin cambio de clase | none (GAP) | Pedagogía PARCIAL | Tradición | Mantener spacing | baja |
| Spread bass from upper voices | no | yes/no | no | yes | Encuadre grave-agudo; claridad | Sears split PARTIAL (llegada) | Sin marco general | Acotado a llegada | Gap estrecho | baja |
| Retain top voice, change lower | no | yes | maybe | yes | Continuidad superior; re-armonización parcial | none (GAP) | Divorce (alcance) | General (negativo) | Cambio total | baja |
| Retain inner common tone | no | no | maybe | no | Conexión interior | none dedicated | CAND-HAR-013 débil | Contextual | Desplazamiento | baja-media |
| Voice exchange | no | yes | no | yes | Conexión por intercambio registral | none (GAP) | Tradición descriptiva | Clásica | Movimiento similar | baja |
| Slash-chord realization | no | yes | maybe | yes | Línea de bajo independiente; reinterpretación | none (GAP) | Doll/Spicer (casos) | Pop/rock | Inversión simple | baja-media |
| Power-chord realization | no | maybe | yes (2 PC) | yes | Organización sin tercera ni función triádica | none (GAP) | Repertorio acotado | Rock | Tríada completa | baja-media |
| Rootless realization | `uncertain` | yes | yes | yes | Función sin fundamental realizada | none (GAP) | Pedagogía UNVERIFIED | Jazz (GAP) | Shell con root en bajo | `uncertain` |
| Repeated chord, changed voicing | no | maybe | no | yes | Persistencia sin estatismo literal | none (GAP) | CAND-HAR-024/026 | Cíclico | Repetición literal | baja-media |
| Same PCs, different bass | no | yes | no | yes | Distinta lectura con mismo contenido | none (GAP) | Doll; Spicer | General (negativo) | Misma inversión | baja-media |
| Same bass, different upper PCs | yes | no | yes | maybe | Centro grave con función móvil | none (GAP) | Spicer pedal | Modal/loop | Bajo móvil | baja-media |

## Diagnostic Questions

Mapa NO-DETERMINISTA. Ante una armonía planificada, preguntar
(DIAGNOSTIC QUESTIONS, no algoritmo):

1. ¿Cuál es el root teórico/analítico, si el marco lo provee?
2. ¿Qué altura debe ser realmente la más grave?
3. ¿Es el bajo miembro del acorde, pedal, tono contrapuntístico o capa
   independiente?
4. ¿Qué trayectoria de bajo exige la frase/loop mayor?
5. ¿Qué alturas exactas deben permanecer de la sonoridad anterior?
6. ¿Qué pitch classes pueden cambiar de octava?
7. ¿Qué relaciones de registro importan (gap grave, nota superior)?
8. ¿Qué tonos son estructuralmente necesarios bajo el marco elegido?
9. ¿Qué duplicaciones/omisiones son idiomáticas del estilo?
10. ¿Altera esta realización la interpretación armónica pretendida?
11. ¿Restringe la melodía la voz superior (cede a RQ-HAR-009)?
12. ¿Se está infiriendo un claim perceptivo desde una regla teórica de
    voicing? (Si sí: detener y declarar el salto.)

## Contradictions / Mixed Evidence

- Pedal que fija vs. pedal que engaña (ambos Spicer VERIFIED): resuelta —
  el pedal es indicio derrotable, no operador (herencia Foundations).
- Inversión que suaviza (pedagogía) vs. inversión que fragiliza (Spicer):
  delimitadas por marco y rol (línea local vs. jerarquía de centro).
- Bajo que decide (Sears músicos) vs. soprano que decide (Sears
  no-músicos): resuelta por formación/tarea; sin jerarquía general.
- Close/open con efectos opuestos según tradición: sin contradicción
  factual — no hay efecto general que contradecir.
- Rootless que preserva función (pedagogía jazz) vs. root necesario
  (marcos clásicos): disputa entre tradiciones; sin medida; ambos
  acotados.

## STRUCTURE → PERCEPTION → COMPOSITION

Separación obligatoria aplicada a los hallazgos mayores:

- STRUCTURE (inversión fragiliza tónica presente, Spicer) → PERCEPTION
  (sin medida de atribución; NO inferir) → COMPOSITION (coordinar bajo
  con otros indicios; verificar por escucha).
- STRUCTURE (cadential 6/4 = ornamento de dominante, OMT) → PERCEPTION
  (predictor en tarea Sears acotada; NO generalizar) → COMPOSITION (usar
  como señalización solo en marco clásico declarado).
- STRUCTURE (mismo loop, distinta configuración, Doll) → PERCEPTION
  (sin medida de oyentes; NO inferir) → COMPOSITION (diagnosticar por
  configuración completa, no por etiqueta).
- STRUCTURE (CTo7 = viio7 en alturas, OMT) → PERCEPTION (sin
  discriminación medida; NO inferir audición) → COMPOSITION (asignar
  función por contexto convergente; registrar alternativas).
- ACOUSTICS (rugosidad grave candidata, UNVERIFIED) → HARMONY (nada) →
  COMPOSITION (nada): cadena bloqueada en el primer eslabón.

Casos prohibidos del encargo (ninguno cometido): root-position→estable→
usar en llegadas; close-grave→rugoso→voicings abiertos; no-duplicar-
leading-tone→oyentes lo rechazan; mismas PCs→equivalencia compositiva.

## Candidate Strategies

Se crean 6 candidatos (CAND-HAR-040–045), uno por familia de conocimiento
nuevo, sin duplicar 002/003/005/009/013/014/016/018/019/028/029/036/037
(aporte diferencial declarado en cada YAML vía `cross_references`):

- 040: cifrado != sonoridad (etiqueta infradetermina realización e
  identidad) — extiende 016 (movimiento) y 036 (cromatismo) al plano
  realización/identidad.
- 041: root != bass con trayectoria propia — extiende 002 (centro) y 009
  (roots) al bajo como capa/roles/trayectoria, sin ponderar.
- 042: anti-regla de jerarquías de inversión + taxonomía 6/4 parcial
  (cadencial apoyado; subtipos como marco sin texto) — heurística
  negativa (cruza 003/008/015/029).
- 043: realización→configuración concreta de conducción (núcleo
  voice-leading que supera el overlap test frente a 019/040);
  llegada/identidad cedidas a 028/040/036; sin Sears/EXP-001/Bregman.
- 044: una sola anti-generalización con mitades doubling/omission
  separadas (sin split a 046); jazz como GAP puro no-citable.
- 045: registro/spacing alteran sonoridad sin determinar función —
  extiende 003 (consonancia) a realización.

## Anti-Rule Results

Investigadas (no pre-etiquetadas como falsas); veredicto con alcance:

1. Root position inherentemente más estable: TRADICIÓN/PEDAGOGÍA acotada;
   sin puente perceptivo (GAP). Fragilización por inversión: ANALÍTICO
   pop acotado (Spicer).
2. Root en bajo aclara tónica: RECHAZADA como regla (CAND-HAR-002; pedal
   que engaña).
3. Primera inversión inherentemente más suave: TRADICIÓN acotada
   (texturas a voces estables); sin medida.
4. Segunda inversión inherentemente inestable: DESCOMPUESTA por rol de
   marco; formulación sostenible = interpretación de tradición.
5. Root-position mejor en tiempos fuertes: SIN APOYO (primario métrico
   no inspeccionado).
6. Acordes finales en root position: CONVENCIÓN de repertorio, no ley
   (finales no-tónicos documentados).
7. Bajo 5→1 garantiza cierre: RECHAZADA como suficiencia (proceso
   cadencial requerido).
8. Nota más grave determina root: RECHAZADA (LOWEST NOTE != ROOT).
9. Bajo y root coinciden lo bastante para fusionarlos: RECHAZADA como
   método (variables separadas obligatorias).
10. Close = más coherente: SIN APOYO general (heurísticas débiles).
11. Open = más espacioso/poderoso: SIN APOYO (lenguaje emocional
    prohibido).
12. Spacing amplio mejor en grave: MARCO acústico UNVERIFIED; no
    universal armónico.
13. Tonos distribuidos uniformemente: SIN APOYO (ninguna norma general).
14. Root debe duplicarse: PEDAGOGÍA SATB acotada.
15. Tercera no debe duplicarse: PEDAGOGÍA SATB acotada.
16. Leading tone nunca duplicado: PEDAGOGÍA SATB acotada.
17. Quinta siempre omitible: ACOTADA (quinta sí; tercera/root según
    marco; jazz GAP).
18. Rootless preserva función automáticamente: `uncertain` (GAP jazz;
    nada perceptivo).
19. Más voces = más rico/complejo: RECHAZADA como inferencia (conteos
    separados).
20. Voz superior lo más importante: DEPENDIENTE de tarea/formación
    (Sears); sin jerarquía general.
21. Voces interiores despreciables: RECHAZADA como método (GAP; sin
    medida de importancia).
22. Desplazamiento de octava preserva identidad de voz: RECHAZADA
    (CAND-HAR-019; no es retención).
23. Mismo pitch-class set = mismo evento armónico: MATIZADA (HAR-004:
    revoicing/bajo/inversión cambian sonoridad; identidad según marco).
24. Distinta inversión = distinta función: ACOTADA a marcos declarados
    (cadential 6/4); fuera `uncertain`.
25. Mismo cifrado = misma sonoridad percibida: RECHAZADA (040; Doll,
    Spicer, OMT).
26. Voicing más suave = mejor: RECHAZADA (CAND-HAR-014).

## Existing-Candidate Blocker Audit

Sin editar ningún candidato (solo evaluación):

- CAND-HAR-002 (bajo/root/pedal/centro): MORE SUPPORT (casos de
  inversión/bajo que modulan atribución analítica: tónicas frágiles,
  pedal bidireccional, vamp-§12, Doll-configuración) + STILL BLOCKED
  (sin medida dedicada, sin pesos, sin `possible_action`). La RQ no lo
  desbloquea como guía accionable; lo precisa como indicio derrotable.
- CAND-HAR-005 (duración/métrica/formal): MORE SUPPORT parcial (split
  bajo/soprano en llegada, Sears PARTIAL, añade dimensión de
  registración a la colocación) + STILL BLOCKED (primario métrico
  Temperley 2001 sin inspeccionar; sin fusión de indicios; sin medida
  que aísle cada sub-indicio). No forzado.
- CAND-HAR-019 (pitch/clase/registro/identidad/octava): MORE SUPPORT
  (organización por variables independientes, OMT enarmónica, Sears
  split, EXP-001 B=3) + STILL BLOCKED (sin medida dedicada de
  equivalencia registral en conducción; `possible_action` sigue sin
  apoyo perceptivo suficiente). Determina qué falta exactamente:
  literatura streaming con estímulos armónicos + medida de continuidad
  con manipulación registral.

## Failure Modes

- Leer función desde cifrado sin realización (falla 040/016).
- Fusionar root y bajo en una variable (falla 041/002/009).
- Aplicar jerarquía de inversión fuera de su tradición (falla 042).
- Tratar equivalencia de octava como retención (falla 019/043/013).
- Duplicar/omitir por regla universal (falla 044).
- Esperar función desde sonoridad (falla 045/003).
- Dar por cerrado lo llegado solo por bajo 5→1 o tónica final (falla
  028/032).
- Funcionalizar cada cromatismo del loop por su bajo (falla 039/036).
- Llamar voicing a la etiqueta y etiqueta al voicing (falla
  terminológica basal).

## What We Cannot Conclude

1. Qué ponderación tienen bajo vs. root en percepción (GAP).
2. Si root-position se oye más estable que inversiones (GAP).
3. Qué spacing/duplicación/registro "funciona mejor" en general (nada).
4. Cuándo un revoicing se vuelve otra armonía en general (marco).
5. Si fundamentales implicadas se oyen (GAP; prohibición expresa).
6. Cómo elegir inversión bajo melodía dada (cede a RQ-HAR-009).
7. Si el bajo modula (frontera RQ-HAR-007).
8. Curvas dosis→efecto para cualquier variable de realización (nada).

## Cross-Domain Dependencies

- Melody (RQ-HAR-009, última): voz superior como evento melódico;
  chord tones vs. non-chord tones; voicing alrededor de objetivo
  melódico; bajo-contrapunto contra melodía. Registradas, no resueltas.
- Rhythm/Meter: colocación métrica del bajo; onset percibido de
  revoicing; metro operativo que fija el conjunto.
- Form: posición formal de llegadas; función seccional de loops/pedales;
  tónica emergente al coro.
- Arrangement/Texture/Production: registro/timbre/densidad como
  co-determinantes de sonoridad, fusión y frontera cíclica; sub/bajo
  electrónico; capas sin voces estables.
- Lyrics/Prosody: cierre textual co-determina cierre (herencia HAR-005).
- Tension (dominio futuro): rugosidad != tensión; cromatismo != tensión.

## Evidence Gaps

1. Medida dedicada bajo-vs-root en atribución de centro/función.
2. Percepción root-position vs. inversiones (priming/inversión).
3. Reconocimiento de acorde bajo inversión/registro.
4. Streaming/proximidad con estímulos armónicos; equivalencia de octava.
5. Rugosidad grave con estímulos musicales y su relación con función.
6. Corpus pop/rock de bajo/inversión/voicing con metodología.
7. Corpus con juicios de oyentes sobre inversión/voicing.
8. Pedagogía jazz registrada (shell/rootless/guide-tones/drop).
9. Textos primarios: Doll 2017, Nobile 2016, Sears, Temperley 2001,
   pedagogía clásica, Terhardt/Parncutt, priming armónico.
10. Manipulación de bajo en cierre fuera de Mozart/teclado.
11. Importancia perceptiva de voces interiores.
12. Criterios de identidad armónica bajo voicing por marco.

## Need for Experiment

Default: NO EXPERIMENT (prohibido en esta tarea; EXP-002 PAUSED).
Preguntas falsables futuras (solo registro, sin diseño):

1. ¿Modifica solo el bajo (tónica vs. 3̂/5̂, colección fija) la
   atribución de centro? (Falsaría/delimitaría 002/041.)
2. ¿Tratan oyentes pitch-class retenida en otra octava como equivalente
   a nota retenida en continuidad? (Delimitaría 019/043.)
3. ¿Difiere completitud percibida entre root-position e inversiones con
   soprano/metro fijos? (Delimitaría 042.)
4. ¿Predice la configuración (bajo+soprano+posición) el cierre mejor que
   la etiqueta? (Extendería Sears fuera de Mozart.)

## Sources

| ID | Trabajo | Estatus | Qué sostiene aquí |
|---|---|---|---|
| SRC-ACADEMIC-028 | Spicer 2017, MTO 23(2) | VERIFIED | Fragilidad por inversión; pedal fija/engaña; vamp-§12; soul-dominant; V perpetuo |
| SRC-ACADEMIC-029 | Everett 2004, MTO 10.4 | VERIFIED | Pedal modal; seis sistemas sin comportamiento común |
| SRC-ACADEMIC-030 | Temperley 2011, MTO 17.4 | VERIFIED | CENTER != COLLECTION; tendencia métrica citada |
| SRC-ACADEMIC-031 | de Clercq 2018 (reseña Doll) | VERIFIED como reseña | Misma configuración→distinto centro; intuición-vs-corpus |
| SRC-PEDAGOGICAL-010 | OMT Tonicization | VERIFIED | Aplicadas (mecánica V(7)/x, resolución; el record no documenta mediación 6/4) |
| SRC-PEDAGOGICAL-011 | OMT Modal Mixture | VERIFIED | Mezcla sin cambio de centro necesario |
| SRC-PEDAGOGICAL-012 | OMT Augmented Sixth | VERIFIED | Predominantes alteradas; tipos; Ger+6 resuelve a V a menudo vía cadential 6/4 (soporte 6/4) |
| SRC-PEDAGOGICAL-013 | OMT Common-Tone Chords | VERIFIED | CTo7/CT+6; disociación enarmónica |
| SRC-THEORETICAL-017 | OMT Mediants | VERIFIED | Taxonomía mediantes (sin función) |
| SRC-PEDAGOGICAL-009 | OMT Modal Schemas | VERIFIED | Schemas pop modales |
| SRC-EMPIRICAL-014 | Puntero pasajes bajo/pedal | PARCIAL | Fija/engaña; melodía-sobre-bajo |
| SRC-EMPIRICAL-016 | Sears 2014/2015 | PARCIAL | Split bajo/soprano; 6/4 predictor; tarea acotada |
| SRC-CORPUS-009 | de Clercq & Temperley 2011 | PARCIAL | Distribuciones como conteo |
| SRC-CORPUS-007 | Doll 2017 (vía reseña) | PARCIAL | Esquemas; ambigüedad configurable |
| SRC-ACADEMIC-009 | Krumhansl probe-tone | VERIFIED (heredado) | Goodness-of-fit, no atribución en canciones |
| SRC-ACADEMIC-035 | Butler 1989 (abstract) | PARCIAL-marco | Contrapeso jerarquía tonal |
| SRC-THEORETICAL-002 | Caplin forma clásica | VERIFIED (heredado) | Sentence/aceleración/cadencia clásica |
| Marcos UNVERIFIED | Figured bass; SATB doubling/spacing; jazz voicings; Terhardt/Parncutt; roughness grave; priming bajo inversión | UNVERIFIED (existencia) | NADA: solo delimitan gaps |

## Candidate Audit Evidence Gate

PASS con alcance declarado: cada candidato 040–045 dispone de apoyo
material directo (repertorio/análisis VERIFIED + pedagogía OMT VERIFIED +
empírica PARTIAL acotada + candidatos heredados) suficiente para una
futura auditoría epistemológica. Ningún claim depende de records
UNVERIFIED (solo delimitan marcos/gaps). Ninguna fuente se cita a texto
completo fuera de lo inspeccionado. Audit de candidatos COMPLETED en esta
tarea: 040/041/042/043/044/045 → REVISE + POSSIBLE_WITH_SCOPE; sin split
(046 no creado); sin rechazos. Correcciones mayores: 6/4 re-soportado en
PED-012 (no 010); subtipos passing/pedal/arpeggiating como marco sin texto;
EXP-001 aislado sin transferencia a voicing; jazz GAP puro; frontera de
sonoridad aplicada; `independent`→DISTINCT/DIVERGE en 041; 042→heurística;
043 podado a núcleo voice-leading; 044 con mitades separadas y base inválida
eliminada; 045 sin prominencia.

## Questions for the Music/Methodology Director

1. ¿Suficiencia del gate PASS con base mayoritariamente analítica +
   Sears PARTIAL, sin medida dedicada bajo-vs-root?
2. ¿Aceptar CAND-HAR-043 como extensión decisionaria de CAND-HAR-019 sin
   reabrir su NOT_READY?
3. ¿Mantener jazz (044) como GAP declarado o priorizar registro de
   pedagogía jazz antes de auditar?
4. ¿Tratar "sonoridad" (045) como constructo Harmony o cederlo a
   Arrangement/Textura en la próxima arquitectura?

## Recommended Next Step

Auditar los nuevos claims CAND-HAR-040–045 contra esta síntesis
(auditoría epistemológica, sin nueva investigación). No realizar
automáticamente.
