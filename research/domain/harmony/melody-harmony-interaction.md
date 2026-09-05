# Melody–Harmony Interaction (RQ-HAR-009) — Síntesis

## Estado y alcance de este documento

- Tipo: síntesis de investigación por pregunta. NO es conocimiento aprobado
  de `manual/`, ni reglas de `rules/`, ni conocimiento de género de
  `genres/`, ni experimento de `experiments/`, ni motor musical.
- Cubre: RQ-HAR-009 (Melody–Harmony Interaction). Estado: SYNTHESIZED.
  Confianza global: provisional (baja-media según claim; ver cada sección).
- Candidatos producidos: CAND-HAR-046–052 (7 claims interactionales).
  Audit de candidatos: NOT STARTED en esta tarea.
- No cubre: RQ-HAR-007 (modulación, NOT STARTED; solo dependencias).
- No modifica: `research/integrations/melody-foundations-v0.md`,
  `research/integrations/harmony-foundations-v0.md`,
  `research/integrations/harmony-foundations-v1.md`, CAND-HAR-001–045,
  CAND-MEL-001–030, RQ-HAR anteriores, `manual/`, `rules/`, `genres/`,
  `experiments/`, music-engine.
- Idioma: contenido humano en español; identificadores y claves en inglés.
- Alcance: conocimiento general dentro de la música popular tonal/modal
  occidental y tradiciones estrechamente relacionadas (common practice,
  pop, rock, electrónica/dance, prácticas modales, songwriting, cognición
  musical). `general` NO significa universal. Toda evidencia perceptiva
  reseñada utiliza oyentes enculturados occidentales salvo indicación
  explícita.
- Método: aplicación manual de
  `.agents/skills/research-music-concept/SKILL.md` y
  `.agents/skills/audit-music-knowledge/SKILL.md`. Separación obligatoria
  `STRUCTURE → PERCEPTION → COMPOSITION` en cada afirmación no trivial.
- Verificación de fuentes: PARTIAL global. Sin inspección externa nueva en
  esta sesión; la síntesis reutiliza el capital ya inspeccionado de las
  RQs previas en su alcance declarado, sin elevar estatus. Ningún
  metadato se inventa. Detalle en "Sources".

---

# Research Question

"How do melodic pitch, scale-degree interpretation, register, rhythm,
phrase position, repetition, and local melodic motion interact with
harmonic identity, bass, inversion, voicing, harmonic rhythm, tonal/modal
center, and arrival, and which relationships are structurally
constrained, perceptually supported, stylistically conventional, or
compositionally actionable?"

Formulación orientada a composición:

"Dada una melodía concreta, ¿cómo puede un compositor elegir y realizar
una armonía que la apoye, reinterprete, contraste o deje abierta; y dada
una armonía concreta, qué decisiones melódicas siguen disponibles sin
reducir la relación melodía–armonía a una tabla chord-tone/non-chord-tone?"

# Scope

Dentro: coordinación melodía-armonía dentro de un centro establecido,
centro modal, contextos ambiguos no modulantes y tonicalización local
solo donde ya existe apoyo (HAR-001/002/006). Todo caso que establezca
genuinamente un nuevo centro se marca `CROSS-RQ DEPENDENCY: RQ-HAR-007`
y no se resuelve aquí.

Fuera: modulación (HAR-007); gramática rítmica de superficie (Rhythm);
forma seccional completa (Form); arreglo/producción salvo dependencias
declaradas; prosodia salvo anticipación rock ya registrada; jazz salvo
material transferible con fuente inspeccionada (en otro caso GAP);
cualquier tabla universal chord-tone/non-chord-tone.

# Terminology

Términos con marco declarado obligatorio (sin marco, uso neutral o
prohibido):

- `chord tone`: pitch melódico que pertenece a la sonoridad realizada
  bajo un marco declarado (no a la etiqueta abstracta). Preguntar siempre:
  ¿sonoridad exacta o acorde abstracto? ¿pitch class o pitch exacto?
  ¿extensiones incluidas? ¿suspensiones? ¿pedal? ¿armonía implicada?
  ¿voicing incompleto/rootless? ¿contexto no-tercial? Sin marco: término
  diagnóstico débil, nunca veredicto.
- `non-chord tone`: pitch melódico fuera de la sonoridad realizada bajo
  marco declarado. No implica disonancia, tensión, error ni necesidad de
  resolución (ver CAND-HAR-046/052).
- `melodic stability`: persistencia/aceptabilidad de un pitch melódico en
  contexto (colección, métrica, duración, repetición, frase). Distinta de
  pertenencia al acorde y de consonancia sensorial.
- `harmonic selection`: qué armonía/relación/región (decisión de v1).
- `harmonic realization`: cómo suena realizada (bajo, inversión, alturas
  exactas, registro, spacing, duplicación, omisión, asignación).
- `scale-degree reference frame`: tónica/centro modal, objetivo
  tonicalizado local, root del acorde vigente, bajo, colección, contexto
  cromático temporal. Nunca cambiar de marco sin declararlo.
- `arrival` (llegada): evento que alcanza un punto estructural.
  `closure` (cierre): convergencia que completa una unidad.
  `cadence` (cadencia): proceso contextual con stages (Caplin), no par
  final. Nunca sinónimos (CAND-HAR-027/028).
- `reinterpretation (analytical)`: otra lectura musicológica admisible
  del mismo evento. `reinterpretation (perceptual)`: el oyente escucha
  otra función/centro. Nunca equivalentes sin medida.
- `compatible`: prohibido sin calificar (¿pertenece al acorde? ¿a la
  colección? ¿evita rugosidad? ¿satisface estilo? ¿preserva identidad?
  ¿confirma expectativa?). Cada sentido es distinto.

# Melody–Harmony as Bidirectional Interaction

Principio arquitectónico adoptado (hereda v1 SELECTION vs REALIZATION):

```
MELODIC EVENT / MOTIF + HARMONIC GOAL
  → HARMONIC SELECTION (qué relación)
  → HARMONIC REALIZATION (cómo suena: bajo, inversión, voicing, timing)
  → CROSS-DOMAIN CHECK (melodía confirma / contradice / deja abierta)
  → iteración permitida; colapso prohibido.
```

Ninguna dirección causal se asume por defecto. La melodía puede
constreñir selección, realización, ambas o ninguna con fuerza; lo mismo
la armonía sobre la melodía. La evidencia disponible sostiene la
bidireccionalidad como hecho analítico (divorce documentado: melodía y
armonía apuntan a centros distintos; véase Melody → Harmony) pero no
proporciona ponderación perceptiva general (todo peso numérico
prohibido; CAND-HAR-002/005/019 siguen bloqueados).

# Melody → Harmony

Dada una melodía, qué constriñe o sugiere (con límites):

- **Center.** La melodía aporta evidencia de centro: colección implicada,
  pitches enfatizados por duración/posición/repetición, dirección propia
  en modos (CAND-HAR-006), tónica presente en melodía con armonía sin
  tónica (Smith 2016, alcance heredado), decisión C-vs-A en "Dreams" por
  melodía, "Reach Out" como confirmación. Pero melodía no domina
  siempre: con armonía cíclica/estática/ambigua la melodía puede
  confirmar, contradecir o dejar abierto. Sin ponderación melodía-vs-bajo
  (GAP). Estado: PROVISIONAL con alcance; diagnóstico, no técnica de
  atribución.
- **Collection.** Una línea diatónica/modal sugiere colección pero no la
  fija: el mismo pitch admite varias colecciones (scalar shift,
  Temperley). Melodía cromática no implica armonía cromática (ver
  sección cromática). Estado: diagnóstico débil.
- **Harmonic target.** Finales cambiados (CAND-MEL-008) dirigen o
  cierran según marco armónico; la melodía propone candidatos de
  objetivo, la armonía califica. Estado: CROSS_DOMAIN_REQUIRED.
- **Chord membership.** Un pitch melódico es compatible con varios
  acordes (root, tercera, quinta, séptima, extensión, suspensión,
  anticipación, pedal, tono común entre dos armonías). La melodía sola
  no fija miembro-de-qué (ver matriz de una nota). Estado: infradetermina
  (CAND-HAR-047).
- **Bass.** La melodía no determina el bajo; convergencia
  melodía-sobre-bajo es indicio parcial (Spicer §12, VERIFIED en su
  alcance) sin peso. El bajo tiene trayectoria propia (CAND-HAR-041).
- **Inversion.** Melodía fija + acorde seleccionado dejan varias
  inversiones posibles salvo restricción física (duplicación no deseada,
  cruce registral, cantabilidad). Ninguna tabla de inversión preferida
  está justificada. Estado: restringen sin determinar (CAND-HAR-049).
- **Voicing.** La melodía como voz superior fija el techo y condiciona
  spacing/duplicación, pero no determina el voicing (CAND-HAR-040/043).
- **Timing.** Onsets/duraciones melódicas no prescriben cambios
  armónicos (ver ritmo vs ritmo). Estado: vocabularios listos,
  colocación prescriptiva bloqueada.
- **Arrival.** Contribuciones parciales (pico, sustain, posición fuerte,
  alargamiento+silencio) exigen soporte armónico; cierre melódico sin
  armonía = como máximo parcial (Melody v0 §9). Estado:
  CROSS_DOMAIN_REQUIRED.
- **Chromatic interpretation.** Línea cromática melódica puede conectar
  (conducción), colorear o pertenecer a loop; no decide lectura
  armónica sola (cede a matriz cromática HAR-006).

# Harmony → Melody

Dado un contexto armónico, qué constriñe o sugiere sobre la melodía:

- **Pitch interpretation.** El mismo pitch se lee como distinto grado
  (de tónica, de acorde, de bajo, de colección) según soporte. La
  armonía reasigna marco de referencia sin cambiar la melodía
  (CAND-HAR-048). Analíticamente soportado; perceptivamente pendiente.
- **Local stability.** Pertenecer al acorde realizado contribuye a
  estabilidad local solo con convergencia (duración, métrica, repetición,
  colección). Miembro del acorde puede ser contextualmente activo
  (séptima que pide continuación en marco clásico; tónica frágil por
  inversión en pop). No-miembro puede ser estable (pedal melódico,
  tono común entre armonías, miembro de loop cromático estable
  CAND-HAR-039). Estado: heurística negativa (CAND-HAR-046).
- **Chord membership / non-chord functions.** La armonía define contra
  qué se clasifica un pitch (marco), y la conducción realizada define
  qué comportamientos están disponibles (paso, bordadura, suspensión,
  anticipación). Pero la etiqueta no prescribe percepción ni obligación
  de resolver (CAND-HAR-052).
- **Register.** La armonía realizada ocupa registro grave/medio y deja
  techo; tesitura habitable (CAND-MEL-020) limita la superior.
  Prominencia por altura sola no garantizada (CAND-MEL-021/023).
- **Tendency.** ^7→^1 y séptima descendente son normas clásicas
  acotadas (CAND-HAR-015), no leyes perceptivas. Fuera de marco
  declarado, ninguna tendencia melódica se exige.
- **Arrival / continuation.** La armonía puede reforzar una llegada
  melódica (llegada tónica + soprano 2^–1^/7^–1^ + bajo 5^–1^ +
  posición), contradecirla (loop que continúa, bajo que sigue en
  movimiento, cambio tras la llegada) o precederla (llegada armónica
  antes del cierre melódico). Ver sección llegadas.
- **Chromatic tone interpretation.** Un pitch cromático melódico puede
  leerse como miembro del acorde cromático, conducción, mezcla o
  color según marco; la armonía no fija la lectura sola (convergencia
  exigida; CAND-HAR-036 + 048).

# Harmonic Selection vs Realization Under Melody

Se hereda v1 (§4, §9, §13). Para un evento melódico fijo:

| Nivel | Pregunta | Variables | Estado bajo melodía dada |
|---|---|---|---|
| SELECTION | ¿qué armonía/relación/región? | objetivo, timing, persistencia, llegada, interpretación cromática | Infradeterminada por la melodía (047); diagnosticable con marcos 007–012/021–039 |
| REALIZATION | ¿cómo suena? | bajo, inversión, alturas exactas, registro, spacing, duplicación, omisión, asignación | Restringida sin determinar por la melodía (049); manipulable + diagnosticable (040–045) |
| CROSS-DOMAIN | ¿confirma/contradice/deja abierta? | convergencia colección+bajo+métrica+forma+arreglo | Bloqueada en ponderación; escucha confirmatoria exigida |

Regla de método: un acorde elegido no es una armonización terminada.
Toda afirmación declara si habla de selección, realización o
convergencia cross-domain. Deducir realización desde etiqueta, o
función desde sonoridad aislada, es error de método (016+040+043).

# Chord Membership

Qué significa `chord tone` según marco (sin ontología universal):

- En SATB clásica: miembro de la tríada/séptima realizada con duplicación
  normada; séptimas con resolución esperada (015); suspensiones como
  retardos con preparación/resolución. Alcance: tradición declarada.
- En pop/rock loop-based: miembro del pitch-class set del símbolo en la
  realización concreta; quintas omitibles; power chords de 2 clases;
  miembros cromáticos estables de loop (039) sin función clásica.
- En modal: miembro de la colección del centro con grados
  característicos; V–I ausente sin defecto (006).
- Casos límite que impiden binario universal: extensiones (¿7ª/9ª/11ª/13ª
  son miembros o adornos? solo por marco), added-note, pedal (miembro de
  qué: del acorde o de la región), suspensiones estilizadas como miembros,
  voicings incompletos/rootless (jazz GAP), sonoridades no-terciales y
  planing (020), melodía que implica miembro omitido del acorde.
- Consecuencia: la clasificación chord/non-chord exige declarar
  sonoridad realizada + marco + ventana temporal. Sin eso es etiqueta
  vacía (CAND-HAR-046).

# Chord Tone vs Melodic Stability

Tesis: NO equivalentes (CAND-HAR-046). Evidencia convergente:

- Estructural: consonancia != estabilidad (003 STRONG); miembro del
  acorde fuera de colección/centro puede ser inestable tonalmente;
  no-miembro dentro de colección con duración/posición puede ser
  localmente estable.
- Melódica: proximidad/reversión (CAND-MEL-013) y representación
  jerárquica (CAND-MEL-005) describen estabilidad melódica sin mencionar
  acordes; EXP-001 muestra parentesco máximo con pitches intactos aunque
  el ritmo cambie (E=4), sin intervención armónica medida.
- Armónica: séptimas de color, tónicas frágiles por inversión, dominantes
  perpetuas sin resolver (Spicer) muestran miembros inestables o activos.
- Conclusión: pertenencia clasifica contra una sonoridad; estabilidad
  juzga en contexto multidimensional. Ninguna deduce la otra.

# Non-Chord Tones

No es catálogo terminológico. Para cada categoría la pregunta obligatoria
es: ¿qué relación estructural la define? ¿qué colocación temporal exige?
¿qué conducción? ¿qué marco presupone? ¿qué repertorio? ¿qué efecto está
medido? ¿qué acción compositiva sigue? (CAND-HAR-052).

| Categoría | Relación definitoria | Temporalidad | Conducción | Marco supuesto | Efecto medido | Acción |
|---|---|---|---|---|---|---|
| passing | conecta dos miembros por grado | débil o fuerte | paso | clásico/modal/pop | ninguno aislado | conectar sin prometer suavidad percibida |
| neighbor | rodea un miembro | variable | bordadura | general | ninguno aislado | ornamentar con escucha |
| suspension / retardation | misma altura retenida contra cambio | acentuada típica | preparación–suspensión–resolución | práctica común | Sears: disonancia degrada ratings (tarea Mozart/teclado, PARTIAL) | solo con marco + resolución verificada |
| appoggiatura | salto + resolución por grado | acentuada | salto→grado | clásico | ninguno aislado | enfatizar con marco, sin promesa expresiva |
| anticipation | adelanta miembro de la armonía siguiente | pre-onset + sustain | anticipación | pop/rock vocal (Tan et al.) | corpus, no percepción | GENRE_SPECIFIC con stress + sustain |
| escape tone | grado + salto contrario | débil | fuga | clásico | ninguno | marco declarado |
| pedal point (melódico) | pitch sostenido contra cambios | extendida | tono común | general/modal | ninguno aislado | sostener como tono común; efecto uncertain |
| accented passing/neighbor | paso/bordadura en tiempo fuerte | fuerte | como su tipo | clásico/pop | ninguno que distinga fuerza | no inferir expresividad del acento |
| unresolved | no resuelve por grado | variable | ninguna | contemporáneo/loop | ninguno | legítimo; prohibido exigir resolución |

Prohibiciones: ninguna etiqueta infiere tensión, belleza, error ni
obligación de resolver. "Acentuado = más expresivo" sin medida.
"Debe resolver" fuera de marco declarado.

# Extensions / Added Notes

Solo con apoyo directo. Cuándo un 7º/9º/11º/13º melódico es extensión,
non-chord, color/add, suspensión o adorno depende de: sonoridad
realizada (¿la armonía incluye esa altura?), marco (¿séptimas de color
o funcionales?), temporalidad (¿preparada? ¿resuelve?), estilo (jazz
GAP sin fuente). Sin fuente inspeccionada: folklore jazz
("avoid notes", "chord-scale", "toda nota es extensión", "guide tones
lo deciden todo") queda como GAP puro no-citable. Estado: uncertain
general; con marco clásico/pop declarado, clasificable; efecto nunca
automático.

# Scale-Degree Reference Frames

Un pitch melódico admite simultáneamente: grado de tónica/centro modal,
grado de objetivo tonicalizado local, grado de root vigente, intervalo
contra el bajo, miembro de colección, grado cromático temporal. No son
idénticos. La evidencia exige declarar el marco (Temperley scalar
shift: CENTER != COLLECTION; CAND-HAR-035). Fallo típico: llamar
"tónica melódica" a la coincidencia con el root y concluir centro;
o llamar "sensible" a ^7 melódico y exigir V. Ambos prohibidos sin
convergencia (duración, métrica, repetición, bajo, resolución).

# Melody as Center Evidence

La melodía aporta evidencia de centro que la armonía no da (Spicer/
Everett/herencia Melody): colección cantada, pitches enfatizados,
dirección modal propia, tónica cantada sobre armonía sin tónica,
divorce que decide ambigüedades de loop. Pero: melodía no domina
siempre; con armonía retenida/ambigua/cíclica/estática/no-funcional la
melodía puede establecer centro provisional, compartirlo o contradecirlo
sin resolverlo. Sin pesos numéricos de indicios (002/005 bloqueados).
Estado: PROVISIONAL diagnóstico; generativo solo con convergencia +
escucha.

# Harmonic Reinterpretation of Melody

Caso inverso de alto valor compositivo: mismo pitch/fragmento melódico
+ distinto soporte = distinta lectura de grado/miembro/función.
Dimensiones de cambio (no equivalentes): preservar centro; alterar
función local; alterar bajo; cambiar inversión; cambiar colección;
tonicalizar otro objetivo (cede a 007 si funda centro); pedal; retrasar
cambio; reinterpretación cromática. Separar siempre reinterpretación
analítica (otra etiqueta admisible) de perceptiva (el oyente escucha
otra función). La primera está soportada estructuralmente (matriz
cromática 036 + disociación enarmónica OMT); la segunda no tiene medida
dedicada inspeccionada (GAP). No inferir efecto emocional
(CAND-HAR-048).

# Reharmonization

NO es "cambiar acordes bajo la misma melodía" como bloque. Es
arquitectura de decisiones (ver sección operaciones): 1) ¿qué
información melódica permanece invariante (pitches, ritmo, acentos,
registro, final)?; 2) ¿qué nivel armónico cambia (bajo, inversión,
identidad, función, colección, centro)?; 3) ¿cambia el timing?; 4)
¿cambia el voicing?; 5) ¿qué efecto está soportado? Modulación completa
queda en HAR-007 (no absorber). Pregunta guía: ¿qué aspectos de la
identidad melódica pueden permanecer mientras la armonía cambia?
(Conexión CAND-MEL-001/004/006.) Ninguna rearmonización promete
automáticamente variación/desarrollo (CAND-HAR-051).

# Repetition / Harmonic Variation

Sección mayor. Hereda Melody (operación vs función; repetición exacta
como establecimiento PROVISIONAL; final cambiado TRADITION_SPECIFIC;
loop con cambio en arreglo GENRE_SPECIFIC).

| Configuración | Función candidata | Estado |
|---|---|---|
| Motivo repetido + misma armonía | refuerzo, establecimiento, expectativa | PROVISIONAL (detección/agrado Margulis; identidad no medida) |
| Motivo repetido + armonía cambiada | repetición con contexto cambiado; contraste seccional; final cambiado; desarrollo sin alterar motivo; retorno con reinterpretación | Hipótesis de alto valor; sin medida que distinga funciones |
| Loop + melodía cambiante | variación melódica sobre estasis | GENRE_SPECIFIC descriptivo; efecto no medido |
| Loop + revoicing/inversión/bajo cambiado | variación de superficie (040/043) | Estructuralmente disponible; si cuenta como evento depende de marco + escucha |

Prohibido: armonía cambiada = variación/desarrollo automático; armonía
igual = monotonía automática (CAND-MEL-012 no-monótona).

# Sustained Melody over Harmonic Change

Caso concreto de alto valor. Un pitch sostenido con armonía cambiante
admite lecturas: tono común (misma clase, distinta función); miembro que
cambia de función (p. ej. 3ª→7ª); comportamiento tipo-suspensión
(retención contra cambio; solo con marco); extensión de la nueva
armonía; tono tipo-pedal melódico; tono activo/disonante; reinterpretación
entre acordes. Ninguna lectura es automática; cada una exige declarar
sonoridades, conducción y marco. Sin efecto universal (tensión incluida).

# Moving Melody over Static Harmony

Caso inverso. Sobre armonía sostenida la melodía puede: arpegiar
(miembros); bordar/pasar (no-miembros de paso); moverse escalar/modal;
embellecer cromáticamente; tocar extensiones superiores; moverse con
independencia lineal. Melodía en movimiento no implica cambio armónico
(HAR-004: duración != importancia; superficie-en-región 024 con marco).
Estado: operaciones disponibles; funciones solo con marco + escucha.

# Melody Rhythm vs Harmonic Rhythm

Vocabularios permanentemente separados (Melody RQ-MEL-006 + HAR-004/021):

MELODIC ONSET / DURATION / IOI / METRIC POSITION vs HARMONIC ONSET /
DURATION / CHANGE RATE. Interacciones investigadas: cambio bajo nota
tenida; armonía tenida bajo notas móviles; anticipación armónica;
anticipación melódica (pop/rock con sustain + stress, Tan);
síncopa melódica sobre armonía inmóvil; cambio durante silencio
melódico; cambios en fronteras melódicas. Ninguna alineación se
prescribe (llegada exige declarar las 6 variables de timing + criterio
de onset por marco; revoicing no es onset automático). Estado:
higiene especificativa ACTIONABLE NOW; colocación prescriptiva
CANNOT YET.

# Bass–Melody Interaction

Central. Hereda 041 (bajo como capa) + Melody (tesitura, prominencia
débil) + Sears split (bajo predice en músicos, soprano en no-músicos;
descriptor de tarea, no peso).

- Movimiento relativo contrario/similar/paralelo, relación interválica
  entre outer voices, marcos de outer-voice, bajo 5→1 con llegadas
  melódicas, bajo estático bajo melodía móvil, pedal melódico sobre
  bajo móvil, cruces registrales: todos disponibles como configuraciones.
- Prohibido: species counterpoint como ley; "contrario siempre mejor";
  5→1 en bajo = cadencia/cierre sin proceso (042 vs 028/029).
- Pregunta productiva: ¿qué coordinan bajo y melodía que las etiquetas
  de root no capturan? Respuesta parcial: trayectoria grave propia,
  convergencia/divergencia con el root, ancla vs soprano móvil,
  indicio convergente de centro/llegada. Sin ponderación (002
  bloqueado). Estado: manipulable + diagnosticable; elección ponderada
  CANNOT YET.

# Melody and Inversion

Fijado acorde + nota melódica, ¿qué inversiones quedan? Distinguir
posibilidad estructural (¿la nota melódica duplica el bajo? ¿cruce?
¿cantabilidad?) de preferencia estilística (normas SATB acotadas, idiom
pop) y de efecto percibido (sin medida). Pregunta de investigación:
si la melodía ocupa un miembro, ¿poner otro en el bajo cambia
interpretación local o solo realización? Respuesta: puede cambiar la
lectura analítica (tónica frágil por inversión, Spicer; 6/4 cadencial
como dominante) sin prueba de reinterpretación perceptiva. Sin tablas
de inversión preferida (CAND-HAR-049; 042 anti-jerarquía vigente).

# Melody and Voicing

Hereda HAR-008 (040/043/044/045). Con melodía como voz superior o
saliente: ¿qué alturas exactas quedan? ¿duplicar la melodía? ¿qué
spacing? ¿qué movimiento interior? ¿qué bajos? Respuestas: duplicar la
melodía en interiores/bajo es configurativamente posible; fusión vs
prominencia sin medida (Bregman solo-marco); interiores portan
tercera/color/retención; omisión de 5ª documentada en marcos; resto por
idioma declarado. Sin reglas SATB por defecto (044). Estado:
manipulable con inventario; elección ponderada pendiente.

# Melody as / vs Top Voice

No siempre. Texturas: melodía arriba (mainstream pop: caso más
relevante con apoyo), interior, duplicada, cruzada registralmente,
distribuida entre capas. No forzar todo a soprano-melodía; pero en
canción pop mainstream el caso top-line es prioritario si hay apoyo
(Sears split: soprano predice en no-músicos; Spicer: alturas melódicas
enfatizadas en vamp). Estado: con marco de textura declarado; sin
norma general.

# Arrival / Closure Interaction

Hereda HAR-005 (027–032) + Melody cierre (§9). Separar MELODIC ARRIVAL
/ HARMONIC ARRIVAL / CADENCE / FULL CLOSURE.

- La armonía puede reforzar la llegada melódica (convergencia:
  objetivo tónico/modal + soprano 2^–1^/7^–1^ + bajo 5→1 + métrica
  fuerte + posición formal + proceso cadencial).
- Puede contradecirla/retrasarla (loop que continúa; bajo en
  movimiento; cambio tras la llegada; tónica frágil deliberada).
- La melodía puede llegar con armonía cíclica (llegada melódica sin
  cierre armónico = como máximo parcial).
- La llegada armónica puede preceder al cierre melódico (armonía
  llega, melodía continúa).
- Final cambiado (changed ending) desplaza la interacción.
Sin score de cierre (029: jerarquía analítica != ranking perceptivo;
betas prohibidos como pesos). Cierre completo exige convergencia
multi-dominio (028). Estado: marco clasificatorio CAN REASON WITH
SCOPE; fuerza sentida CANNOT YET (CAND-HAR-050).

# Open Endings / Divergent Arrivals

Cómo la armonía puede no reforzar un endpoint melódico: mantener loop;
evitar objetivo tónico local; cambiar tras la llegada melódica;
sostener región ambigua; continuar bajo; retrasar frontera. Son
objetivos investigables, no recetas. Prohibido `no-tónica = abierto`
como regla universal (finales no-tónicos legítimos 032; tónica final
sin proceso 032; parada sola no cierra 031). Estado: repertorio de
opciones con alcance; efecto fuera de marco uncertain.

# Melody and Chromatic Harmony

Hereda HAR-006 (033–039). Preguntas con respuesta:

- ¿Melodía cromática implica armonía cromática? No necesariamente
  (conducción interior genera sonoridades como subproducto 037;
  loop cromático estable 039).
- ¿Melodía diatónica sobre armonía cromática? Sí (préstamo con centro
  persistente 035; tono común melódico sobre cambio).
- ¿Melodía confirma colección alternativa? Puede (convergencia
  colección+bajo+repetición), sin umbral.
- ¿Mezcla vs tonicalización por melodía? La melodía aporta evidencia
  (línea que resuelve a otro grado con confirmación) pero el umbral
  tonicalización/modulación cede a HAR-007.
- ¿Melodía mantiene centro viejo sobre colección cambiada? Sí
  (CENTER != COLLECTION; scalar shift).
- ¿Armonía reinterpreta un tono cromático melódico como miembro? Sí
  analíticamente (036 + 048); perceptivamente uncertain.
Sin inferir tensión/emoción (038). Estado: matriz de lecturas
ACTIONABLE como diagnóstico; generativo solo con convergencia.

# Melody and Local Tonicization

HAR-007 sin investigar. HAR-009 solo registra si la melodía aporta
evidencia a un pitch/acorde localmente enfatizado (duración, repetición,
resolución melódica hacia él, convergencia con bajo). Si el caso exige
establecimiento de nuevo centro: `CROSS-RQ DEPENDENCY: RQ-HAR-007`.
Etiqueta V/x sola no prueba centro local percibido (034).

# Consonance / Dissonance / Membership

Separación estricta vigente: RELACIÓN INTERVÁLICA VERTICAL /
CONSONANCIA SENSORIAL / PERTENENCIA / ESTABILIDAD TONAL / ESTABILIDAD
MELÓDICA / TENSIÓN / FUNCIÓN. Hereda 003 (consonancia != estabilidad).
Un no-miembro puede ser sensorialmente consonante; un miembro puede ser
contextualmente activo. Sin tablas binarias seguro/inseguro (046).

# Popular-Music Evidence

Requisito cumplido con capital heredado (sin corpus nuevo):

- Melodía sobre loops; hook repetido sobre armonía cambiante (repertorio
  de opciones, § Repetition); mismo loop con melodía cambiante;
  misma melodía sobre armonía seccional cambiada; non-chord tones
  vocales incl. anticipaciones (Tan et al., GENRE_SPECIFIC);
  melodía modal sobre cifrados mayor/menor (006 + divorce);
  notas melódicas como extensiones/add (marco-dependiente);
  finales en loops (031/032); melodía sobre pedal/bajo estático
  (Spicer/Everett); divergencia melódico-armónica seccional (divorce).
Sin ley de género derivada de ejemplos (frecuencia != norma).

# Common-Practice Evidence

Alcance legítimo y acotado: non-chord tones con preparación/resolución;
suspensiones; tendency tones (015); cadencia outer-voice con soprano
2^–1^/7^–1^ + bajo; armonización de soprano/bajo dados (marcos
pedagógicos PARCIAL, sin texto completo: no universalizar); interacción
frase/cadencia (Caplin). Pedagogía clásica no inspeccionada a texto
completo no sostiene claims positivos; solo delimita marcos.

# Jazz / Transferable Evidence

Solo material transferible con apoyo directo; sin él, GAP. Folklore no
citable (avoid notes, chord-scale, "toda nota es extensión", "guide
tones lo deciden todo"). Rootless/omisión de root: GAP puro (044).
Estado: GAP declarado; ninguna inferencia jazz sostiene candidatos.

# Perceptual Evidence

Directa accesible (alcances heredados, sin reabrir):

- Expectativa melódica tono-a-tono (Schellenberg; alternativa tesitura
  von Hippel & Huron; coexistentes).
- Jerarquía tonal con contexto (Krumhansl; probe-tone como
  representación, no regla pop).
- Fraseo aditivo pitch+tiempo+armonía (Palmer & Krumhansl 1987).
- Jerarquía métrica y expectativa de acentos (P&K 1990).
- Ratings de completitud con superbajo/soprano (Sears, tarea
  Mozart/teclado, PARTIAL; betas no-pesos).
- Detección/atribución de repetición y silencio post-cierre
  (Margulis 2012/2013 MP/JMT; detección/tensión/atribución por
  contexto).
- Alargamiento en límites (Kragness & Trainor, producción).
Para cada fuente: tarea, estímulos, población y medida según su
síntesis de origen. Prohibido inferir preferencia compositiva desde
tiempos de reacción o ratings de tarea ajena.

# Corpus / Repertoire Evidence

Accesible con alcance heredado (conteo, no norma):

- Distribuciones de progresiones rock/pop (Doll vía reseña; de Clercq
  & Temperley 2011): conteo, no expectativa (010).
- Síncopas anticipatorias rock (Tan et al. 2382/10433, stress crucial).
- Células-4 postmillennial (White 2022, distribucional).
- Cadencias seccionales rock (59% RS200 con sectional cadence;
  Nobile vía HAR-005, sin texto completo: existencia, no fuerza).
- Casos divorce / tónica ausente / doble centro (Spicer, Everett,
  Doll cap.6 vía reseña).
Frecuencia != requisito perceptivo != calidad (010). Ninguna
probabilidad de transición se convierte en regla.

# Theoretical Frameworks

Ningún marco oficial. Utilizados con scope: funcional/T–PD–D acotado
(007/008); Schenker solo analítico de tradición (fondo no prescribe
superficie); Caplin sentence/cadencia clásicas (009/023/027);
Temperley (scalar shift; divorce); Spicer/Everett/Doll-de Clercq
(loops, tónica ausente/frágil, divorce); Schoenberg (repetición,
variación desarrolladora como teoría de tradición); OMT (aplicadas,
mezcla, Aug6, tono común, mediantes); Sears (ratings acotados).
Jazz, Terhardt/Parncutt, roughness grave: solo-marco hasta inspeccionar.

# One-Note Diagnostic Matrix

Una nota melódica sobre una armonía candidata (solo filas con apoyo;
nunca desde memoria de manual):

| Melodic relation | Structural interpretation | Requires temporal context? | Requires voice-leading context? | Requires style/framework? | Perceptual evidence | Composition implication | Confidence |
|---|---|---|---|---|---|---|---|
| root (fundamental en bajo) | miembro + convergencia centro | sí (duración/posición) | bajo = root | sí | convergencia Spicer §12 | refuerzo plausible con convergencia | provisional |
| root (otra voz en bajo) | miembro con bajo divergente | sí | trayectoria bajo | sí | sin medida dedicada | color/inversión, no prueba centro | provisional/baja |
| third | miembro que fija cualidad | sí | interiores | por marco | sin medida aislada | portar color; no garantiza función | provisional/baja |
| fifth (omitible) | miembro estructural débil | sí | omisión por marco | por marco | sin medida | omitible en marcos; no inferir pérdida | provisional |
| seventh | miembro/color/tendencia según marco | sí | resolución en clásica | sí (clásica vs color) | Sears: disonancia degrada ratings (tarea) | solo con marco + resolución verificada | provisional |
| extension (9/11/13) | miembro/add/no-miembro según marco | sí | voicing | sí | ninguna aislada | clasificar antes de usar | uncertain |
| suspension | retención contra cambio | sí (preparación) | retención literal + resolución | práctica común | parcial (Sears) | solo con marco clásico declarado | provisional acotada |
| anticipation | adelanto del acorde siguiente | sí (pre-onset+sustain) | acorde siguiente | pop/rock vocal | corpus Tan | GENRE_SPECIFIC con stress+sustain | genre provisional |
| passing | conexión por grado | sí (débil/fuerte) | dos miembros | general | ninguna aislada | conectar sin prometer suavidad | baja |
| neighbor | ornamento de un miembro | sí | miembro eje | general | ninguna aislada | ornamentar con escucha | baja |
| pedal-like tone | tono común contra cambios | sí (extendida) | tono común literal | general/modal | ninguna aislada | sostener; efecto uncertain | baja |
| chromatic neighbor | conducción cromática | sí | semitono a miembro | por marco | ninguna aislada | color/conducción con marco | uncertain |
| appoggiatura | salto + grado | sí (acentuada) | salto→resolución | clásica | ninguna aislada | enfatizar con marco | provisional acotada |
| non-tertian member | miembro de sonoridad no-tercial | sí | bloque/planing | repertorios acotados | ninguna | organización alternativa (020) | uncertain |
| ambiguous / multiple readings | varias lecturas admisibles | sí | contexto convergente | sí | ambigüedad analítica != confusión (036) | diagnosticar matriz, no forzar etiqueta | provisional |

# Same-Melody / Different-Harmony Matrix

El objeto es la REINTERPRETACIÓN:

| Fixed melodic event | Harmonic change | What changes analytically? | What may remain? | Perceptual evidence | Repertoire evidence | Composition use | Confidence |
|---|---|---|---|---|---|---|---|
| pitch sostenido | cambio con tono común | función del pitch (3ª→7ª…) | pitch, colección | ninguna dedicada | vamp de 2 acordes (Spicer §12) | sostener con nueva función | provisional/baja |
| pitch sostenido | cambio a armonía que lo excluye | miembro→no-miembro | pitch, registro, métrica | ninguna dedicada | pedal melódico sobre cambios | suspender/anticipar/pedalizar | baja |
| motivo repetido | cambio de bajo solo | lectura bajo/root; inversión | identidad, roots | ninguna dedicada | slash/pedal (041) | variar superficie (040/043) | provisional (estructural) |
| motivo repetido | cambio de inversión | rol de inversión | identidad, pitch classes | ninguna (042 GAP) | tónica frágil (Spicer) | color/fragilidad deliberada | baja |
| motivo repetido | cambio de identidad (mismo centro) | función local | centro, motivo | ninguna dedicada | loops con trayectoria (011/026) | repetición con contexto cambiado | hipótesis |
| motivo repetido | cambio de colección (préstamo) | colección; fuente por marco | centro (035), motivo | ninguna que aísle mezcla | bVII/bVI/bIII rock | color sin partida | provisional acotada |
| motivo repetido | tonicalización local (V/x) | énfasis local | centro global (033) | ninguna (034) | aplicadas clásicas/pop | redirección local; umbral →007 | provisional acotada |
| llegada melódica | armonía no-tónica / loop continúa | llegada != cierre | gesto melódico | Sears: DC/EV altas en no-músicos | finales no-tónicos (032) | apertura deliberada | provisional |
| motivo | pedal/drone bajo cambios | ancla grave vs movimiento | motivo, centro modal | Everett modal | "Tomorrow Never Knows" | centrar modalmente | provisional acotada |

# Melody ↔ Realization Matrix

| Melody constraint | Harmonic selection affected? | Bass affected? | Inversion affected? | Exact voicing affected? | Timing affected? | Cross-domain dependency | Evidence |
|---|---|---|---|---|---|---|---|
| fixed top note | infradetermina (047) | restringe sin determinar | restringe sin determinar | fija techo; resto libre | no prescribe | marco + escucha | 040/043/007 |
| fixed register (tesitura) | no | limita cruces | limita | limita spacing | no | intérprete/estilo (020) | CAND-MEL-020 |
| held note | admite varias funciones | admite pedal/trayectoria | admite varias | admite tono común | permite cambio bajo tenida | marco temporal | 013/026/041 |
| phrase-final note | propone objetivo | 5→1 con marco | 6/4 cadencial clásico | soprano 2^–1^/7^–1^ | colocación + proceso | forma/métrica (028/029) | 027–032, MEL-028 |
| repeated motif | admite rearm. (051) | admite trayectoria propia | admite cambio | admite revoicing | admite retraso/anticipación | arreglo/forma | 011/026/040 |
| chromatic pitch | admite lecturas (036) | puede modular lectura | puede modular lectura | puede modular lectura | no prescribe | marco cromático (033–039) | 035–038 |
| silence (gap) | no prescribe | cambio posible durante silencio | — | — | onset posible | contexto tonal/métrico (029) | MEL-029 |
| dense local activity | no prescribe | incierta | incierta | conducción concreta (043) | aceleración solo clásica (023) | tempo/metro | MEL-030, 023 |
| melodic leap | aceptabilidad local (013) | incierta | incierta | registro/voz (019/045) | no prescribe | tesitura | MEL-013/024 |

`uncertain` usado liberalmente donde no hay medida.

# Tradeoff Matrix

| Conflicto | Polos | Estado |
|---|---|---|
| preservar nota como miembro vs trayectoria de bajo deseada | miembro vs línea grave | ambos legítimos; sin criterio ponderado (041/049) |
| identidad armónica vs conducción realizada cómoda | selección vs voicing | iterar; sin receta (040/043) |
| mantener centro vs reinterpretar pitch | centro vs función local | convergencia decide; umbral →007 |
| registro melódico vs spacing preferido | techo vs disposición | tesitura manda físicamente; resto escucha (020/045) |
| llegada armónica vs continuación melódica | ARRIVE vs CONTINUE | divergencia legítima (050); cierre exige convergencia |
| repetición melódica vs variación armónica | mismo vs cambiado | variación de superficie disponible; desarrollo no automático (051) |
| persistencia de loop vs objetivo local | CYCLE vs TARGET | gestos locales dentro de ciclo (011); función interna uncertain |

Ningún efecto causal inventado; cada fila marcada establecida o plausible.

# STRUCTURE → PERCEPTION → COMPOSITION

Casos prohibidos aplicados en esta RQ (ninguno inferido):

- ESTRUCTURA "nota fuera de tríada" → PERCEPCIÓN "tensión" →
  COMPOSICIÓN "resolver ya". NO PERMITIDO.
- TEORÍA "es suspensión" → "oyentes esperan resolución descendente".
  NO sin tarea que mida expectativa de resolución.
- CORPUS "la voz canta a menudo la 3ª" → "la 3ª es la mejor nota".
  NO PERMITIDO (010: frecuencia != norma).
- ESTRUCTURA "misma melodía rearmonizada" → "oyentes perciben
  desarrollo". NO PERMITIDO (desarrollo sin correlato medido).
- ETIQUETA "V/x" → "centro local percibido". NO (034).
- BAJO "5→1" → "cadencia/cierre". NO sin proceso (042 vs 028/029).
- REVOICING → "nueva armonía percibida". NO sin marco + escucha
  (040 vs HAR-004).

# Diagnostic Power vs Generative Power

| Área | Diagnostic power | Generative power |
|---|---|---|
| Pertenencia vs estabilidad | MEDIA-ALTA negativa (qué NO inferir) | BAJA (clasificar con marco; sin pesos) |
| Selección bajo melodía fija | MEDIA (matriz de lecturas; infradeterminación) | BAJA-MEDIA (opciones admisibles, sin ranking) |
| Reinterpretación | MEDIA analítica; BAJA perceptiva | BAJA (analítica usable; perceptiva uncertain) |
| Realización bajo melodía fija | MEDIA (inventario 040–045 + techo melódico) | BAJA (manipulable, sin guía ponderada) |
| Bajo–melodía | MEDIA (trayectoria, convergencia) | BAJA (sin ponderación bajo-vs-melodía) |
| Timing melódico/armónico | MEDIA-ALTA (vocabularios + criterio onset) | BAJA (higiene; sin colocación prescriptiva) |
| Llegada/cierre | MEDIA (proceso vs par; divergencia clasificada) | BAJA-MEDIA con alcance; cierre CANNOT YET sin convergencia |
| Cromatismo melódico/armónico | MEDIA-ALTA (matriz de lecturas) | BAJA-MEDIA con convergencia + escucha |
| Repetición + variación armónica | MEDIA (operación vs función) | BAJA-MEDIA (opciones; desarrollo no automático) |

Veredicto: HAR-009 aumenta la potencia diagnóstica interactional
considerablemente y la generativa solo parcialmente: el sistema ahora
sabe qué opciones son admisibles bajo una melodía y qué declarar, pero
sigue sin saber elegir bien entre ellas con criterios generales. El
avance es arquitectónico (qué decidir y en qué orden) más que
prescriptivo.

# Generative Capability Test

Varios escenarios abstractos, sin música generada. Escala: CAN REASON /
CAN REASON WITH SCOPE / PARTIALLY / CANNOT YET.

A. **Nota melódica tenida a través de dos eventos armónicos.**
   PARTIALLY. Puede razonar lecturas admisibles (tono común, cambio de
   función, suspensión-tipo, extensión, pedal melódico) y exigir marco +
   conducción + escucha. No puede predecir qué lectura escuchará un
   oyente ni cuál es mejor.

B. **Motivo repetido con armonía cambiada.** CAN REASON WITH SCOPE
   (estructural). Puede enumerar niveles de cambio (bajo, inversión,
   identidad, función, colección) y preservar identidad melódica según
   RQ-MEL-001 (una dimensión intacta tolera; multidimensional degrada).
   No puede prometer variación/desarrollo percibidos.

C. **Llegada melódica de frase.** CAN REASON WITH SCOPE (marco).
   Puede clasificar refuerzo vs divergencia y listar convergencias
   necesarias para cierre. Fuerza sentida y cierre completo:
   CANNOT YET sin melodía+metro+forma+arreglo.

D. **Melodía sobre loop.** CAN REASON WITH SCOPE. Puede sostener ciclo
   (011/026), variar superficie (040/043) o línea melódica, y registrar
   divorce/ambigüedad sin forzar tónica. Coherencia percibida del loop
   con melodía: PARTIALLY (sin medida).

E. **Pitch cromático melódico en centro por lo demás estable.**
   PARTIALLY. Puede clasificar lecturas (miembro cromático, conducción,
   mezcla, color, loop-member) con fuente por marco y convergencia.
   Elección entre lecturas y umbral tonicalización: CANNOT YET
   (→ HAR-007 si funda centro).

F. **Melodía fija + elegir bajo/inversión.** PARTIALLY (manipulación)
   / CANNOT YET (elección ponderada). Puede generar realizaciones
   admisibles con inventario 040–045 respetando tesitura y sin duplicar
   problemáticamente; no puede rankearlas con criterios generales.

# Candidate Strategies

Solo claims interactionales genuinos (melodía × armonía), 6–9. Ningún
candidato por tipo de non-chord tone. Producidos 046–052 (ver RQ-HAR-009
y YAML individuales). Familias aprobadas por evidencia:

- 046 pertenencia != estabilidad (negativo sólido).
- 047 infradeterminación de selección por melodía fija.
- 048 reinterpretación armónica del mismo pitch (analítica vs
  perceptiva separadas).
- 049 pluralidad de realizaciones bajo melodía fija.
- 050 divergencia de llegadas melódica/armónica.
- 051 variación armónica sobre repetición melódica.
- 052 dependencia marco/temporal/conducción de categorías non-chord.

# Anti-Rule Results

Investigadas sin pre-etiquetar como falsas; veredicto por evidencia
heredada (S = soportada como falsa-generalización en alcance; P =
plausible-bloqueo; U = uncertain):

1. notas melódicas normalmente chord tones — S (falsa como norma;
   046; anticipaciones pop, pedales, loop-members como contraejemplos).
2. non-chord tones crean tensión — S (falsa como automático; 003/038).
3. non-chord acentuados son más expresivos — U/P (sin medida que aísle
   acento; 052).
4. todo non-chord debe resolver — S (falsa fuera de marco clásico;
   irresueltos legítimos).
5. evitar la 4ª sobre acorde mayor — U (sin fuente inspeccionada;
   no adoptada ni refutada; GAP).
6. la melodía debe seguir los cambios — S (falsa; tono común/pedal
   melódico, superficie-en-región).
7. los acordes deben cambiar cuando cambian notas importantes — S
   (falsa; armonía tenida bajo melodía móvil).
8. cada nota necesita acorde compatible — S (falsa sin calificar
   `compatible`; infradeterminación 047).
9. la melodía determina el root — S (falsa; divorce, 009).
10. el root determina notas aceptables — S (falsa; 007/046).
11. tónica melódica exige tónica armónica — S (falsa; tónica ausente
    en armonía, finales no-tónicos 032).
12. sensible exige V — P/S acotada (norma clásica acotada 015; falsa
    como ley general).
13. tónica final melódica exige armonía tónica — S (falsa; 032).
14. misma melodía necesita misma armonía al repetir — S (falsa; 051).
15. rearmonizar crea automáticamente variación/desarrollo — S (falsa
    como automático; 051).
16. cambiar bajo nota tenida crea tensión — S (falsa como automático).
17. armonía estática bajo melodía móvil es menos interesante — S
    (falsa como juicio; loops como contraejemplo de virtud).
18. bajo y melodía en contrario siempre — S (falsa; sin norma
    general).
19. la voz superior determina la inversión — S (falsa; restringe sin
    determinar, 049/042).
20. no duplicar la melodía — U/P (sin medida fusión/prominencia;
    configurativamente posible).
21. extensiones son chord tones en todas partes — S (falsa; por
    marco).
22. compatibilidad escala-acorde predice calidad — S (falsa; 010/038).
23. melodía diatónica implica armonía diatónica — S (falsa; 035).
24. melodía cromática exige armonía cromática — S (falsa; 037/039).
25. llegadas deben coincidir — S (falsa como obligación; 050).
26. ritmos deben alinearse — S (falsa; timing separado 021).
27. cierre melódico predecible desde armonía sola — S (falsa; 028).

# Candidate Audit (CAND-HAR-046–052)

Auditoría epistémica completada: 0 `STRONG_CANDIDATE`, 7
`POSSIBLE_WITH_SCOPE`, 0 `NOT_READY` y 0 rechazados. Todos permanecen
`candidate`; no se promociona ninguno.

046–047, 049–052 reciben `REVISE`; 048 queda `KEEP_AS_IS`. La auditoría
mantiene separadas estructura, percepción y composición. La reinterpretación
analítica no se presenta como cambio perceptivo; la pertenencia se refiere a
un objeto armónico declarado, preferentemente la sonoridad realizada. Las
acciones conservadas son diagnósticas o heurísticas débiles, no reglas
generativas. La convergencia de llegadas puede contribuir al cierre en
contextos inspeccionados, pero no es requisito universal ni tiene pesos.

# Existing-Candidate Impact

Sin editar ni re-auditar (solo contexto nuevo que HAR-009 aporta):

- **CAND-HAR-002** (NOT_READY): más contexto de prueba (¿pesa el bajo
  cuando la melodía confirma o contradice?), pero sin medida dedicada:
  sigue bloqueado. Prohibido leer HAR-009 como desbloqueo.
- **CAND-HAR-005** (NOT_READY): idem para duración/métrica/posición
  frente a melodía (¿larga+fuerte melódica = centro?). Sigue bloqueado.
- **CAND-HAR-019** (NOT_READY): idem para equivalencia registral
  (transposición melódica B=3 como indicio propio puntual, sin medida
  armónica). Sigue bloqueado.
- **CAND-HAR-028** (llegada != cierre): uso positivo mejorado —
  ahora con inventario de contribuciones melódicas y matriz de
  divergencia (050). Sigue exigiendo convergencia cross-domain.
- **CAND-HAR-040** (cifrado != sonoridad): uso positivo mejorado —
  melodía fija como caso que demuestra la infradeterminación (047/049).
- **CAND-HAR-041** (root/bajo): uso positivo mejorado — bajo como capa
  bajo melodía con configuraciones (trayectoria, pedal, ancla).
  Ponderación sigue bloqueada.
- **CAND-HAR-043** (realización→conducción): uso positivo mejorado —
  conducción concreta alrededor de superior fija (049).
- **CAND-HAR-045** (registro/spacing): uso positivo mejorado —
  techo melódico + tesitura como restricción física (CAND-MEL-020).
  Dosis/efecto siguen bloqueados.
- Resto 001–039: sin cambio de estatus; 007/009/011/013/015/016/021/
  024/026/027/029/031/032/033–039 reutilizados como marcos en su
  alcance.

# Melody Foundations Interface Impact

Pregunta: ¿resuelve o avanza HAR-009 el gap interfaz Melody–Harmony
aplazado hasta Harmony Foundations?

MELODY-HARMONY INTERFACE: **materially advanced, still blocked in
ponderación**.

- Avanza: pertenencia vs estabilidad separadas (CAND-MEL-005 sin acción
  ahora tiene marco de uso); finales cambiados (CAND-MEL-008) ahora con
  marco armónico que califica; cierre (GAP-08) ahora con matriz de
  divergencia y condiciones de convergencia; non-chord tones
  (RQ-MEL-007 pendiente) ahora con taxonomía marco-dependiente sin
  inferencias falsas; transformación motívica bajo rearmonización
  (CAND-MEL-001/004/006) ahora con niveles de cambio armónico;
  tesitura/registro (CAND-MEL-019/020/022) ahora con techo y
  restricciones de realización; anticipación (CAND-MEL-026) ahora con
  marco armónico del tiempo fuerte.
- Sigue bloqueado: ponderación (cuánto pesa cada indicio cuando melodía
  y bajo/armonía apuntan a lugares distintos); predicción perceptiva
  (qué escuchará un oyente ante melodía fija × armonía variada);
  ranking entre realizaciones admisibles.
- NO se marca Melody como resuelto retroactivamente. Ningún candidato
  MEL se edita; dependencias cross-domain registradas en 049/050.

# Failure Modes

1. Colapsar pertenencia con estabilidad (usar chord-tone como
   certificado de buena nota).
2. Deducir armonía única desde melodía (lookup mel→acorde).
3. Deducir melodía aceptable desde cifrado (lookup acorde→mel).
4. Inferir tensión/resolución desde etiqueta non-chord.
5. Exigir resolución universal fuera de marco clásico.
6. Leer reinterpretación analítica como prueba perceptiva.
7. Tratar rearmonización como desarrollo automático.
8. Alinear por defecto cambios armónicos con onsets melódicos.
9. Fijar bajo = root para "sostener" la melodía sin marco.
10. Inferir fuerza de cierre desde inversión/bajo/registro solos.
11. Usar `compatible` sin calificar.
12. Cambiar de marco de grado (tónica/root/bajo/colección) sin
    declararlo.
13. Absorber modulación (casos con nuevo centro tratados como
    rearmonización local).

# What We Cannot Conclude

- Ninguna ponderación numérica entre indicios melódicos y armónicos.
- Ninguna curva dosis→efecto (repeticiones, duración, registro,
  spacing, tasa).
- Ninguna jerarquía universal (rasgos de identidad, inversiones,
  progresiones, cadencias, voicings).
- Ninguna predicción perceptiva de reinterpretación, desarrollo por
  rearmonización, o fuerza de cierre divergente.
- Ninguna técnica positiva general para elegir bajo/inversión/voicing
  bajo melodía dada más allá de admisibilidad + escucha.
- Ninguna transferencia jazz sin fuente.
- Ninguna frontera tonicalización/modulación con melodía fuera de
  clásica (→ HAR-007).

# Cross-Domain Dependencies

| Decisión interactional | Dominio del que depende | Qué falta |
|---|---|---|
| Atribución de centro con melodía | Rhythm/Meter (posición, duración), Form, Arrangement | pesos 002/005 con melodía |
| Función local de pitch melódico | Bass realizado, Form | medida bajo-vs-melodía |
| Conducción alrededor de superior fija | Arrangement (capas, timbre, fusión) | continuidad/streaming con melodía |
| Onset bajo melodía | Rhythm/Meter, Arrangement | colocación prescriptiva |
| Cierre completo | Melody + Rhythm/Meter + Form + Arrangement + Lyrics | medida terminal-vs-corte; fade GAP |
| Color cromático conjunto | Arrangement (voicing/timbre normalizan) | afecto GAP |
| Nuevo centro con melodía | HAR-007 | tipos, pivotes, confirmación, retorno |

# Evidence Gaps

1. Corpus pop/rock de alineación melodía-acorde (nota vs root,
   non-chord vocales, cambios bajo motivo repetido, finales).
2. Corpus pop/rock con juicios de oyentes sobre rearmonización.
3. Expectativa melódica bajo contexto armónico manipulado (tarea
   declarada).
4. Priming armónico sobre juicios melódicos / key-finding con bajo
   manipulado.
5. Medida de continuidad/independencia entre sonoridades con melodía
   fija.
6. Medida de fuerza sentida en llegadas divergentes.
7. Pedagogía clásica de armonización a texto completo.
8. Pedagogía jazz registrada (o GAP permanente).
9. Normalización perceptiva de loops cromáticos con melodía.
10. Falsación de "4ª sobre mayor" y duplicación de melodía
    (diseños declarados, no realizados aquí).

# Need for Experiment

Default NO EXPERIMENT (EXP-002 PAUSED; ninguno diseñado aquí). Solo se
registran preguntas falsables futuras de alto leverage (ninguna
diseñada):

- Q1: misma melodía × 3 soportes (tónica / no-tónica mismo centro /
  préstamo): ¿cambia atribución de centro/función? (afectaría 047/048).
- Q2: nota tenida × armonía que la incluye vs excluye: ¿cambia juicio
  de estabilidad/tensión? (afectaría 046).
- Q3: motivo repetido × misma vs cambiada armonía: ¿cambia juicio de
  variación/desarrollo? (afectaría 051).
- Q4: llegada melódica × llegada armónica convergente vs divergente:
  ¿cambia juicio de completitud? (afectaría 050).
Cada una requiere tarea, estímulos, población y medida declaradas antes
de considerarse evidencia.

# Sources

Una fuente = una obra identificable. Clases según roadmap §4b.
Estatus VERIFIED/PARTIAL/UNVERIFIED heredado de RQs de origen; ninguno
elevado aquí.

| ID (heredado) | Obra | Estatus | Qué sostiene en HAR-009 (alcance) |
|---|---|---|---|
| SRC-ACADEMIC-028 | Spicer 2017 | VERIFIED | tónica frágil; pedal fija/engaña; vamp §12; divorce; soul-dominant |
| SRC-ACADEMIC-029 | Everett 2004 | VERIFIED | pedal/drone modal; sistemas tonales |
| SRC-ACADEMIC-030 | Temperley 2011 | VERIFIED | CENTER != COLLECTION; divorce citado |
| SRC-ACADEMIC-031 | de Clercq 2018 (reseña Doll) | VERIFIED como reseña | mismo loop distinto centro; intuición-vs-corpus |
| SRC-PEDAGOGICAL-010–013 | OMT tonicalización/mezcla/Aug6/tono común | VERIFIED | aplicadas; mezcla; disociación enarmónica; cadential 6/4 |
| SRC-THEORETICAL-002 | Caplin forma/cadencia | VERIFIED | sentence; cadencia como proceso; aceleración acotada |
| SRC-EMPIRICAL-016 | Sears (ratings completitud) | PARTIAL | soprano/bajo split; disonancia degrada; betas no-pesos |
| Capital Melody empírico/teórico | Dowling; Bartlett & Dowling; Krumhansl; Prince; Halpern; Jones & Ralston; Müllensiefen; P&K 1987/1990; Schellenberg; von Hippel & Huron; Margulis; Huron 1996; Tan et al.; Witek; Madison; White; Eitan; Ilie & Thompson | Alcances según síntesis Melody (ninguno reabierto) | identidad sin jerarquía; repetición; contorno-función; registro 3 niveles; ritmo; cierre parcial |
| EXP-001 | Experimento propio exploratorio n=1 | EXPERIMENTAL RESULT (indicio) | B=3; C/F=2; D/E=4; tolerancia unidimensional |
| Doll 2017 completo; Nobile; Temperley 2001 primario; corpus con juicios; pedagogía clásica armonización; pedagogía jazz; priming con melodía | Varias (localizar/inspeccionar) | UNVERIFIED/GAP | Ningún claim sostenido; solo marcos y gaps |

# Candidate Audit Evidence Gate

**candidate_audit_evidence_gate: PASS** (con alcance declarado).

PASS significa: cada nuevo candidato interactional (046–052) tiene
apoyo material suficiente en el capital inspeccionado (marcos
VERIFIED/PARTIAL heredados + candidatos previos + indicio propio
EXP-001) para una futura auditoría epistémica. NO significa que toda la
literatura melodía-armonía esté verificada. FAIL habría significado que
uno o más candidatos dependen de evidencia no inspeccionada (jazz,
priming con melodía, corpus con juicios). Esos materiales quedan
explícitamente como GAP y no sostienen ningún candidato (ver RQ-HAR-009
§ Evidence-Sufficiency Gate). Auditoría de candidatos NO realizada en
esta tarea.
