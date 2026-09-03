# Harmony Foundations v1 — Integración de selección y realización armónica

## Estado de este documento

- Tipo: capa de integración y auditoría. NO es conocimiento aprobado de `manual/`, ni reglas de `rules/`, ni conocimiento de género de `genres/`, ni experimento de `experiments/`, ni motor musical.
- Cubre: RQ-HAR-001, 002, 003, 004, 005, 006 y 008. Todas en estado SYNTHESIZED con audit COMPLETED.
- No cubre: RQ-HAR-007 (modulación, NOT STARTED) ni RQ-HAR-009 (interfaz melodía-armonía, NOT STARTED).
- Candidatos cubiertos: CAND-HAR-001–045, 45/45. Ningún candidato creado, modificado, re-auditado ni rechazado en esta tarea. Próximo ID libre: CAND-HAR-046.
- Relación con v0: `research/integrations/harmony-foundations-v0.md` es un snapshot histórico. NO se modifica. Este documento lo re-evalúa y lo extiende; no lo sobrescribe conceptualmente.
- Relación con Melody: `research/integrations/melody-foundations-v0.md` se consulta solo como interfaz futura. NO se modifica ningún archivo Melody.
- Idioma: contenido humano en español; identificadores, claves y nombres técnicos en inglés.
- Alcance: conocimiento general dentro de la música popular tonal/modal occidental y tradiciones estrechamente relacionadas (common practice, pop, rock, electrónica/dance, prácticas modales, songwriting, cognición musical). `general` NO significa universal para toda la música humana. Toda evidencia perceptiva reseñada utiliza oyentes enculturados en la tradición tonal occidental salvo indicación explícita.
- Método: aplicación manual de `.agents/skills/research-music-concept/SKILL.md` y `.agents/skills/audit-music-knowledge/SKILL.md`. Separación obligatoria `STRUCTURE → PERCEPTION → COMPOSITION` en cada afirmación no trivial. Ningún nivel implica automáticamente el siguiente.
- Verificación de fuentes: heredada de las RQs (PARTIAL global; textos completos ya inspeccionados: Spicer 2017, Everett 2004, Temperley 2011, de Clercq 2018 como reseña de Doll 2017, pedagogía Open Music Theory de HAR-006; parciales/pendientes: Doll 2017 completo, Nobile 2016, Sears 2014/2015 completos, corpus pop/rock con juicios de oyentes como GAP estructural). Esta integración NO reabre fuentes, NO verifica fuentes nuevas, NO usa web, NO diseña experimentos.
- Lectura y aprobación: requiere revisión del Project Owner y del Music/Methodology Director antes de cualquier promoción a `manual/` o `rules/`.

---

# 1. Purpose and Scope

## Pregunta que responde v1

> ¿Sobre qué puede ya razonar el sistema acerca de la SELECCIÓN armónica y la REALIZACIÓN armónica, y qué sigue bloqueado antes de poder coordinar una melodía con esa realización?

v0 respondía: ¿sobre qué decisiones armónicas puede razonar el sistema a partir de RQ-HAR-001–006?

v1 añade RQ-HAR-008 y por tanto debe responder algo más exigente: habiendo seleccionado una identidad o relación armónica, ¿cuánto del evento musical sigue sin decidirse, y qué parte de lo que sigue puede decidirse con criterios?

## Lo que v1 NO es

- NO es un capítulo de manual sobre acordes, inversiones o voicings.
- NO es una lista de reglas de conducción, duplicación u omisión.
- NO es una taxonomía de inversiones, spacings o texturas.
- NO es un schema de SongPlan ni de music-engine.
- NO es una auditoría nueva de CAND-HAR-002/005/019 (se preservan).
- NO es investigación de modulación ni de interacción melodía-armonía (solo mapas de dependencia).

## Alcance de decisiones

v1 integra dos grupos que v0 no separaba arquitectónicamente:

**Selección armónica (qué armonía / qué relación / cuándo / con qué interpretación):** centro, colección, organización dirigida/cíclica/ambigua, objetivo armónico siguiente, timing, persistencia frente a partida, llegada frente a apertura, interpretación cromática.

**Realización armónica (cómo suena lo seleccionado):** bajo, inversión, alturas exactas, registro, spacing, duplicación, omisión, asignación de voces, retención literal de tono común, conducción concreta realizada.

La distinción es la hipótesis arquitectónica central de esta integración y se evalúa en §3. No se adopta por defecto: se adopta porque la evidencia auditada la sostiene como principio de razonamiento (no como schema de software).

---

# 2. Epistemic Status

- Clases de evidencia utilizadas: THEORY, GENRE OBSERVATION, COMPOSITION HEURISTIC, HYPOTHESIS. Ningún EXPERIMENTAL RESULT propio en Harmony (EXP-002 sigue PAUSED; ningún EXP-HAR existe).
- Vocabulario de integración (ortogonal al readiness de candidatos): SUPPORTED, PROVISIONAL, TRADITION_SPECIFIC, GENRE_SPECIFIC, UNSUPPORTED, CROSS_DOMAIN_REQUIRED. Combinables.
- Readiness heredado (NO modificado en esta tarea): STRONG_CANDIDATE 2 (CAND-HAR-003, CAND-HAR-006); POSSIBLE_WITH_SCOPE 40 (resto salvo bloqueados); NOT_READY 3 (CAND-HAR-002, CAND-HAR-005, CAND-HAR-019); REJECTED 0.
- Confianza global de la integración: provisional. Lo más sólido sigue siendo conocimiento negativo (anti-reglas). Lo positivo exige alcance explícito y, en realización, escucha confirmatoria.
- Prohibiciones metodológicas vigentes: ningún peso numérico de ponderación; ninguna curva dosis→efecto; ninguna jerarquía universal de inversiones, progresiones, cadencias o voicings; ninguna inferencia perceptiva desde etiqueta analítica; ningún mapeo afectivo fijo (préstamo→emoción, cromático→tensión, grave→poder, close→suavidad); ningún `possible_action` donde el YAML lo deja vacío.

---

# 3. What Changed Since Harmony Foundations v0

v0 organizaba el conocimiento en ocho familias: ORIENTAR, ORGANIZAR, CONECTAR, TEMPORIZAR, PERSISTIR, LLEGAR / MANTENER ABIERTO, EXPANDIR / REINTERPRETAR, DIAGNOSTICAR (transversal). Esa arquitectura sobrevive en lo esencial, pero RQ-HAR-008 obliga a cuatro cambios estructurales y varios desplazamientos de contenido.

## 3.1. Selección vs realización se convierte en eje arquitectónico (NUEVO, central)

v0 trataba bajo, inversión y voicing como variables pendientes (bloqueo interno denso: CAND-HAR-002/005/019). RQ-HAR-008 demuestra que la carencia no era solo de ponderación: era de arquitectura. La evidencia sostiene que la decisión armónica tiene dos momentos lógicamente distintos que v0 colapsaba parcialmente dentro de CONECTAR y de LLEGAR:

- decidir QUÉ armonía o relación (selección);
- decidir CÓMO suena realizada (realización).

CAND-HAR-040 (cifrado infradetermina sonoridad) se promueve en v1 a principio arquitectónico central (ver §4). No es una observación más sobre voicing: es la razón por la que CONECTAR debe dividirse y por la que la representación de razonamiento debe tener dos bloques separados.

## 3.2. Root vs bass como separación operativa (REVISE → SPLIT operativo)

v0 ya imponía `root != bass` como distinción obligatoria. RQ-HAR-008 la convierte en separación operativa de variables con consecuencias en centro, función, conducción, cadencia e interpretación cromática (CAND-HAR-041). El bajo deja de ser un "indicio más" dentro de ORIENTAR para convertirse en una capa con trayectoria propia que debe coordinarse con roots, colección y voces superiores. Sin ponderación perceptiva (CAND-HAR-002 sigue bloqueado), pero con estatus de variable manipulable y diagnosticable.

## 3.3. Inversión contextualizada (REVISE)

v0 registraba "no asumir equivalencia de inversiones" como cautela. RQ-HAR-008 la convierte en anti-jerarquía explícita más taxonomía parcial del 6/4 (CAND-HAR-042): las jerarquías de manual (fundamental más estable, primera más suave, segunda inestable) son lecturas de tradición, no propiedades perceptivas generales. La única categoría con apoyo suficiente es el 6/4 cadencial como ornamento de dominante en práctica común; el resto de subtipos 6/4 queda como marco sin texto inspeccionado o como GAP pop. Consecuencia: la IA NO puede inferir estabilidad, suavidad, fuerza de cierre o calidad desde la inversión sin marco declarado.

## 3.4. Voicing exacto como decisión compositiva (NUEVO)

v0 trataba registro/duplicación/identidad de voz como bloqueos (CAND-HAR-019) y variables de conducción sin ponderación. RQ-HAR-008 establece que alturas exactas, registro, spacing, duplicación, omisión y asignación son decisiones que cambian la sonoridad realizada y la configuración concreta de conducción aunque el pitch-class set se conserve (CAND-HAR-043/044/045). Manipulables estructuralmente, débilmente guiadas perceptivamente. Esto desplaza parte de CONECTAR al nuevo bloque de realización y redefine la frontera con Arrangement (§9).

## 3.5. Desplazamientos menores por familia

- ORIENTAR: KEEP con REVISE. El bajo pasa de indicio a capa (041); la registración añade un indicio parcial (Sears split) sin desbloquear ponderación (002/005 siguen bloqueados).
- ORGANIZAR: KEEP. El bajo co-determina dirección pero sin peso; los loops admiten trayectoria de bajo propia.
- CONECTAR: SPLIT (ver §5.4). Conexión abstracta vs conexión realizada.
- TEMPORIZAR: KEEP con REVISE. Revoicing/inversión/bajo NO constituyen automáticamente nuevo onset armónico (HAR-008 vs HAR-004): el criterio de onset debe declararse por marco y confirmarse por escucha.
- PERSISTIR: KEEP. Pedal != prolongación (confirmado); pedal que fija vs pedal que engaña impide cualquier regla causal.
- LLEGAR / MANTENER ABIERTO: REVISE. La inversión en la llegada (6/4, posición del bajo, 5→1 sin proceso) NO es medida de fuerza de cierre fuera de tradición declarada (042 vs 028/029).
- EXPANDIR / REINTERPRETAR: KEEP con REVISE. Bajo/voicing pueden alterar la lectura analítica de un evento cromático (enarmónica CTo7/aplicado, Ger+6) sin probar reinterpretación perceptiva (HAR-008 vs HAR-006).
- DIAGNOSTICAR: KEEP y se amplía. Ahora incluye diagnóstico de realización (qué realización suena, qué rol cumple el bajo, qué marco de inversión/duplicación aplica) además de diagnóstico de función/cromatismo/prolongación.

---

# 4. Selection vs Realization

## 4.1. Hipótesis sometida a prueba

> Las decisiones de SELECCIÓN armónica y de REALIZACIÓN armónica son momentos de razonamiento distintos, con variables, criterios, alcances y bloqueos diferentes, y deben representarse por separado.

## 4.2. Veredicto: la distinción SE SOSTIENE y se adopta como eje de v1

La evidencia auditada apoya la separación en los tres planos exigidos por la skill de investigación (fenómeno → decisión → contexto → efecto → límites):

1. **Fenómeno:** la misma identidad armónica admite múltiples realizaciones con distinta lectura analítica y distinta configuración de conducción (CAND-HAR-040/043; disociación enarmónica CTo7/aplicado y CT+6/Ger+6 con mismas alturas y distinta función según marco; tónicas frágiles por inversión; mismo loop con distinto centro según configuración).
2. **Decisión:** el compositor controla variables de selección (objetivo, timing, persistencia, interpretación) y variables de realización (bajo, inversión, alturas, registro, spacing, duplicación, omisión, asignación) de forma independiente en el acto compositivo: puede fijar la selección y variar la realización, o fijar la realización y reinterpretar la selección.
3. **Contexto y límites:** las dos capas dependen de marcos distintos (selección: tradición funcional/modal/loop; realización: práctica de voces — SATB clásica, voicings de guitarra/teclado pop, pedal/drone modal — más arreglo) y fallan por separado (una buena selección puede arruinarse por una realización inadecuada y viceversa).

Por tanto v1 adopta la separación. NO es schema de software: es orden de razonamiento (primero qué relación armónica se busca, después cómo se realiza, con iteración permitida cuando la realización revela una lectura distinta).

## 4.3. Principio representacional: ADOPTADO como central

> CHORD / HARMONIC IDENTITY no especifica por completo REALIZED HARMONIC SONORITY.
> REALIZED HARMONIC SONORITY no especifica por completo CROSS-DOMAIN MUSICAL REALIZATION.

CAND-HAR-040 se convierte en principio arquitectónico central de v1 porque:

- explica por qué ningún candidato de selección (001–039) autoriza por sí solo una realización concreta;
- explica por qué los nuevos candidatos 040–045 son todos POSSIBLE_WITH_SCOPE y ninguno promete función, cierre o tensión por sí solo;
- delimita la frontera con Arrangement sin colapsarla (ver §9);
- hace falsable la arquitectura: bastaría un contraejemplo donde el cifrado determinara unívocamente bajo, inversión, registro, spacing, duplicación y asignación para refutarla en ese marco. No se ha encontrado; los marcos más restrictivos (SATB pedagógica) siguen dejando grados de libertad (qué voz duplica, qué octava, qué disposición exacta).

## 4.4. Arquitectura de tres niveles: ADOPTADA como razonamiento compositivo

1. **HARMONIC INTENT / SELECTION** — qué centro/colección/organización/objetivo/timing/persistencia/llegada/interpretación se busca.
2. **HARMONIC REALIZATION** — cómo se distribuyen alturas realizadas (bajo, inversión, registro, spacing, duplicación, omisión, asignación, conducción concreta).
3. **CROSS-DOMAIN REALIZATION** — cómo esa sonoridad vive con melodía, ritmo/metro, forma, arreglo/producción, letra/prosodia.

Cada nivel puede confirmar, matizar o contradecir al anterior (una realización puede sugerir otra lectura funcional; un arreglo puede convertir estasis armónica en interés formal). La iteración es legítima; el colapso (deducir realización desde etiqueta, o función desde sonoridad aislada) es error de método.

---

# 5. Integrated Decision Architecture

Se re-evalúan las ocho familias de v0. Resultado por familia: KEEP, REVISE, SPLIT, MERGE, RELOCATE.

## 5.1. Harmonic Orientation (ORIENTAR) — REVISE (antes D1)

**Pregunta:** ¿qué evidencia puede contribuir a un centro tonal/modal, qué NO lo determina solo, cómo mantener/debilitar/ambiguizar?

**Variables:** colección compartida como marco; recurrencia (de acorde, de pitch de tónica, de loop); bajo como capa (root en bajo, pedal/drone, repetición grave, trayectoria); duración; colocación métrica; colocación formal (inicio, retorno); confirmación cadencial posterior; competidores; registración (indicio parcial Sears, sin peso).

**Relaciones que sobreviven:** consonancia != estabilidad (003, SUPPORTED); frecuencia/primero/final no bastan (004); duración/colocación confirman como máximo centro ya plausible (005, HYPOTHESIS); centro modal sin V–I con marcadores por tradición (006, STRONG con alcance); bajo como indicio derrotable, nunca prueba (002 bloqueado + 041 diagnóstico).

**Cambio v1:** el bajo deja de listarse como un indicio entre otros y se representa como capa coordinable (ver §11). ORIENTAR decide el centro buscado; la capa de bajo se decide en realización y puede confirmar o sabotear la orientación.

**Candidatos:** 001–006, 041 (capa bajo), 042 (fragilidad por inversión como modulador analítico), 045 (registro como dimensión sonora sin fijar centro).

## 5.2. Harmonic Organization (ORGANIZAR) — KEEP (antes D2)

**Pregunta:** una vez insinuado centro/región, ¿permanecer, partir, continuar, preparar, aproximar, volver, ciclar, mantener ambiguo?

**Variables:** rol contextual asignado (no etiqueta); root motion; bajo y su trayectoria; conducción abstracta; tendency tones; esquema/convención; organización global (dirigida vs cíclica vs ambigua); posición formal.

**Relaciones:** función por rol en contexto (007); V–I acotado a tradición (008); root motion insuficiente sin bajo+contexto (009); frecuencia != expectativa (010); loops coherentes sin sintaxis clásica (011); dominante como indicios distribuidos sin traducción a tensión (012).

**Cambio v1:** menor. Se registra que la trayectoria del bajo es organizable como capa propia dentro de organización dirigida o cíclica, pero sin técnica positiva (041). Root motion y bass trajectory permanecen variables distintas que deben coordinarse, no deducirse una de otra (041 vs 009).

**Candidatos:** 007–012, 041.

## 5.3. Harmonic Selection (SELECCIÓN) — REVISE, ahora explícita como familia

En v0 la selección estaba distribuida entre ORGANIZAR, TEMPORIZAR, PERSISTIR y EXPANDIR. v1 la hace explícita como momento de razonamiento porque la separación selección/realización lo exige. NO es una fase temporal obligatoria (en loops la selección puede ser "continuar ciclo" y en modales "mantener colección"); es el lugar donde se fija QUÉ relación armónica se busca antes de realizarla.

**Subdecisiones:** objetivo siguiente (target/relación); timing del cambio; persistencia (mantener región variando superficie); llegada/apertura buscada; interpretación cromática (qué lectura se adopta entre las admisibles).

**Candidatos principales:** 007–012 (objetivo/organización), 021–023 (timing), 024–026 (persistencia), 027–032 (llegada), 033–039 (interpretación cromática).

## 5.4. Harmonic Connection (CONECTAR) — SPLIT en dos subfamilias

Veredicto: una sola familia YA NO basta. La evidencia de HAR-008 (CAND-HAR-043, 040, 016) demuestra que "conectar" nombra dos decisiones con variables y criterios distintos.

### 5.4.1. Abstract Connection (conexión abstracta)

**Pregunta:** entre dos identidades armónicas sucesivas, ¿qué relación de parentesco se busca (continuidad, articulación, desplazamiento deliberado, planing)?

**Variables:** clases de pitch compartidas; proximidad abstracta; intención (CONNECT vs ARTICULATE); rol funcional de cada identidad; marco de tradición.

**Candidatos:** 013 (tono común/movimiento pequeño como heurística débil de continuidad), 014 (no minimizar como objetivo), 018 (continuidad != función), 020 (planing como organización alternativa).

**Estatus:** PROVISIONAL como heurística débil con escucha; TRADITION/GENRE_SPECIFIC donde aplique (015/017/020).

### 5.4.2. Realized Voice Connection (conexión realizada)

**Pregunta:** dadas dos sonoridades realizadas concretas, ¿qué voces permanecen literalmente, cuáles se mueven, cuánto, en qué dirección relativa, en qué registro, con qué asignación?

**Variables:** retención literal de altura (no de pitch-class); tamaño y dirección del movimiento por voz; movimiento relativo (contrario/oblicuo/paralelo); registro y duplicación; identidad/asignación de voz; tendency tones realizados; bajo realizado.

**Candidatos:** 013 (mitad literal), 016 (partir de realización, no de etiqueta), 019 (distinción registral, analítica), 040–045 (realización).

**Estatus:** estructuralmente manipulable, perceptivamente débil sin medida. La conducción concreta es consecuencia decidible de la realización (043, SUPPORTED como hecho analítico/decisionario), pero ninguna configuración concreta promete continuidad percibida, suavidad preferida o calidad sin escucha y marco.

**Regla de método:** toda afirmación de conducción declara si habla de conexión abstracta o realizada. Deducir conducción realizada desde etiqueta/root/bajo es error de método (016 + 040 + 043).

## 5.5. Harmonic Timing (TEMPORIZAR) — KEEP con REVISE (antes D4)

**Pregunta:** ¿cuándo cambia la armonía, cuánto se sostiene cada sonoridad, cuándo acelerar/desacelerar, dónde colocar cambios?

**Variables (permanentemente separadas):** TEMPO; HARMONIC-CHANGE RATE; CHORD/EVENT DURATION; PATTERN OF CHANGES; METRIC PLACEMENT; STRUCTURAL HARMONIC CHANGE.

**Revisión v1 (HAR-008 vs HAR-004):** revoicing, cambio de inversión o cambio de bajo NO constituyen automáticamente nuevo onset armónico. Si el criterio de onset es "cambio de root", un revoicing no es onset; si es "cambio de bajo", un pedal con acordes cambiantes sí redistribuye onsets; si es "cambio de colección", un revoicing no es onset. El criterio debe declararse por marco y confirmarse por escucha/arreglo. Prohibido: mismo cifrado = sin evento; nuevo voicing = nueva armonía (ambas como reglas automáticas).

**Candidatos:** 021–023, 040 (criterio de identidad), 041 (bajo como onset potencial).

## 5.6. Structural Persistence (PERSISTIR) — KEEP (antes D5)

**Pregunta:** ¿cómo sostener región/función mientras la superficie cambia (paso, bordadura, pedal, sustitución, inversión, repetición cíclica)?

**Convención obligatoria heredada:** todo "X prolonga Y" declara FRAMEWORK, OBJECT, CRITERION, SCOPE, EVIDENCE TYPE. Sin marco, vocabulario neutral (cyclic persistence, recurrence, stasis).

**Revisión v1:** pedal != prolongación (confirmado por HAR-008: pedal que fija vs pedal que engaña). Inversión/duplicación/omisión/revoicing como variación de superficie dentro de región persistente es admisible como heurística débil con marco, sin promesa de unidad audible (024 + 040/043).

**Candidatos:** 024–026, 037 (CTo7/CT+6 dentro de región), 040/043.

## 5.7. Arrival / Openness (LLEGAR / MANTENER ABIERTO) — REVISE (antes D6)

**Pregunta:** ¿cómo contribuir a llegada/cierre/suspensión/apertura/retorno, y qué alternativas existen sin cadencia clásica?

**Constructos permanentemente distintos:** CADENCE, ARRIVAL, CLOSURE, RESOLUTION, COMPLETION, RETURN, STOP, BOUNDARY, FINAL EVENT.

**Revisión v1 (042 vs 028/029):** la inversión en la llegada NO es medida de fuerza de cierre. El 6/4 cadencial señaliza proceso solo en marco clásico declarado; fuera de él, llegar en inversión, con 5→1 en el bajo sin proceso, o con tónica frágil, puede ser llegada de bajo, color deliberado o fragilidad buscada, no cierre débil. La jerarquía analítica PAC>IAC>HC no es ranking perceptivo general (029). Llegada tónica != cierre; el cierre exige convergencia cross-domain (028).

**Candidatos:** 027–032, 042 (inversión en llegada), 041 (bajo de llegada), 045 (registro de llegada como sonoridad, no como fuerza).

## 5.8. Chromatic Expansion (EXPANDIR / REINTERPRETAR) — KEEP con REVISE (antes D7)

**Pregunta:** ante evento fuera de colección, ¿enfatiza otro grado, mezcla, conecta, cambia colección, crea color, pertenece a loop, admite varias lecturas, prepara cambio de centro?

**Distinciones:** CENTER != COLLECTION; TONICIZATION != MODULATION; CHROMATICISM != TENSION.

**Revisión v1 (HAR-008 vs HAR-006):** cambiar bajo/voicing puede alterar la LECTURA ANALÍTICA de un evento cromático (misma altura, distinta función: CTo7 vs aplicado; CT+6 vs Ger+6; 6/4 cadencial como mediación aplicada) sin probar reinterpretación perceptiva. La ambigüedad analítica != confusión del oyente (036). Toda lectura cromática con bajo/voicing no estándar declara marco y convergencia (centro, contexto, conducción, posición, repetición, convención).

**Candidatos:** 033–039, 040/041/043 (realización como modulador de lectura).

## 5.9. Harmonic Realization (REALIZACIÓN) — NUEVA familia (extraída de CONECTAR + LLEGAR + ORIENTAR)

**Pregunta:** seleccionada una identidad/relación armónica, ¿qué bajo, qué inversión, qué alturas exactas, en qué registro, con qué spacing, qué duplicaciones/omisiones y qué asignación de voces la realizan?

Subbloques (cada uno con su auditoría en §13):

- **Bass** (041; 002 bloqueado): nota grave realizada + rol + trayectoria. DISTINCT de root, coordinable, sin ponderación.
- **Inversion** (042): rol por marco, no jerarquía perceptiva. 6/4 descompuesto obligatoriamente.
- **Exact pitches / Register** (043/045; 019 bloqueado): alturas exactas como decisión; registro como dimensión sonora sin fijar función.
- **Spacing** (045): disposición vertical como sonoridad, sin receta close/open.
- **Doubling / Omission** (044): restricción de idioma/estilo, no ley general. Jazz rootless = GAP puro.
- **Voice allocation** (043/041): qué voz lleva qué altura, con superior doblemente restringida (cantabilidad + conexión) y bajo con lógica propia; interiores portan tercera/color/retención.

**Estatus global:** estructuralmente manipulable pero perceptivamente débilmente guiada (ver §13). Ninguna elección de realización promete por sí sola estabilidad, función, cierre, tensión o calidad.

## 5.10. Diagnosis (DIAGNOSTICAR) — KEEP y ampliada, transversal

**Pregunta:** bajo incertidumbre, ¿qué lectura (de función, de prolongación, de cromatismo, de realización) es admisible y con qué marco?

**Ampliación v1:** además de matriz de lecturas funcionales/cromáticas/prolongacionales, el diagnóstico incluye: qué realización suena (inventario de bajo/inversión/registro/spacing/duplicación/omisión/asignación); qué rol cumple el bajo; qué marco de inversión/duplicación aplica; si un revoicing cruza el umbral de "otra armonía" según marco declarado (sin criterio general: se declara FRAMEWORK).

**Candidatos:** 007/009/010/012 (función), 024/025 (región), 033–036 (cromatismo), 040–045 (realización).

---

# 6. Sonority Boundary

Frontera adoptada de RQ-HAR-008 (auditoría de sonoridad):

**REALIZED HARMONIC SONORITY incluye:** pitch classes realizadas; alturas exactas; bajo; registro; spacing; duplicación; omisión; asignación de voces; número de voces/clases/partes como conteos descriptivos (no como complejidad).

**NO incluye automáticamente:** instrumento; timbre; articulación; dinámica; efectos; mezcla; producción espectral; microtiming; capas de arreglo; densidad de arreglo.

Lo segundo pertenece principalmente a Arrangement / Production. Donde el timbre (u otra variable de arreglo) afecte materialmente a la interpretación armónica (fusión de voces, enmascaramiento del bajo, prominencia de interiores, rugosidad grave, normalización de loop por capas), se marca CROSS_DOMAIN_REQUIRED y se registra la dependencia en vez de resolverla.

**Prohibiciones terminológicas:**

- `sonority` NO es sinónimo de chord label / cifrado.
- `sonority` NO es sinónimo de timbre.
- `voicing` (cómo se distribuyen alturas entre voces/registros) != `register` (dónde suena) != `inversion` (qué grado está en el bajo) != `spacing` (distancias verticales).
- `doubling` (qué pitch se repite) != `función` ni `peso`.
- `omission` (qué pitch falta) != `pérdida de identidad` automáticamente.
- `root-position` != `estabilidad`; `first inversion` != `suavidad`; `second inversion` != `inestabilidad`.
- `close` != `conexión`; `open` != `potencia`.
- `número de voces` != `complejidad` ni `calidad`.

---

# 7. Integrated Anti-Rules

v1 conserva las 19 anti-reglas de v0 y añade las aportadas por HAR-008. Lo negativo sigue siendo el conocimiento más sólido. Todas en formulación negativa SUPPORTED o PROVISIONAL con alcance.

**De v0 (conservadas):** consonancia != estabilidad; frecuencia/primero/final no bastan; duración/colocación confirman como máximo; ningún V–I necesario para todo centro; etiqueta/root-motion/V/x no fijan función; V–I no universal, dominante != tensión; distancia mínima no objetivo; tendency tones como normas acotadas; paralelas como normas de juego; continuidad != función; octavas no intercambiables (analítico); tempo != ritmo armónico, duración != importancia, aceleración acotada; prolongación sin marco no subordina; cadencia != dos últimos acordes, llegada != cierre, jerarquía != ranking; retorno loop != cadencia, parada sola no cierra, tónica final no garantiza cierre; tonicalización != modulación, mezcla != modulación, centro != colección, cromatismo != tensión; fuente de préstamo y lectura cromática por marco; más cambios != más desarrollo; frecuencia en corpus != expectativa ni calidad.

**Añadidas o reforzadas por HAR-008:**

20. Cifrado != sonoridad: del cifrado no se deduce bajo, inversión, registro, spacing, duplicación, omisión ni asignación (040).
21. Root != bass: el bajo no se deduce del root ni el root del bajo; pedal, slash y trayectoria grave tienen lógica propia (041).
22. Ninguna jerarquía de inversiones es ranking perceptivo general; la segunda inversión no es un fenómeno único (6/4 cadencial vs passing/pedal/arpeggiating vs tónica frágil pop) (042).
23. Igual pitch-class set con distinta realización no es el mismo evento de conducción; la conducción se lee desde alturas exactas realizadas (043 + 016).
24. Ninguna política de duplicación/omisión SATB es regla general; rootless jazz sin marco registrado no autoriza ninguna inferencia (044).
25. Registro/spacing no fijan función, centro ni calidad; grave rugoso no prohibido por principio general (045).
26. Revoicing/inversión/bajo nuevo no equivalen automáticamente a nueva armonía ni a nuevo onset; mismo cifrado no equivale a sin cambio sonoro (HAR-008 vs HAR-004).
27. Bajo cambiado no equivale a reinterpretación perceptiva probada; 5→1 en el bajo sin proceso no equivale a cadencia ni a cierre (041/042 vs 028/029).
28. Fundamental implicada con root omitido no se presume percibida (044).
29. Conteo de voces/clases/partes no mide complejidad ni calidad (045/044).

---

# 8. Candidate Coverage Matrix

Todos los CAND-HAR-001–045 representados (45/45). Readiness heredado NO modificado. Dimensiones: SEL = SELECTION, REA = REALIZATION, DIA = DIAGNOSIS, X-D = CROSS-DOMAIN INTERFACE.

| ID | Significado integrado conciso | Readiness | Problema compositivo | Scope | Limitación / bloqueador | SEL / REA / DIA / X-D |
|---|---|---|---|---|---|---|
| CAND-HAR-001 | Centro por colección + recurrencia como indicios separados | POSSIBLE_WITH_SCOPE | Establecer centro sin declararlo por etiqueta | Tradiciones tonales/modales occidentales | Sin ponderación/dosis; possible_action vacío | SEL + DIA |
| CAND-HAR-002 | Bajo/root/pedal/bajo-repetido/centro como 5 elementos sin ponderación | NOT_READY | Reforzar centro vía bajo sin cambiar roots | Sin alcance afirmable | MORE SUPPORT + STILL BLOCKED: sin medida bajo-vs-root ni técnica | REA + DIA |
| CAND-HAR-003 | Consonancia != estabilidad tonal-contextual | STRONG_CANDIDATE | No decidir estabilidad desde sonoridad aislada | General en scope | Heurística negativa, no técnica positiva | DIA |
| CAND-HAR-004 | Frecuencia/posición no bastan para tónica en pop/rock | POSSIBLE_WITH_SCOPE | Centro único vs ambigüedad en loops | Pop/rock cíclico | Sin medida en oyentes; ambigüedad deliberada abierta | DIA (+SEL) |
| CAND-HAR-005 | Duración/metro/posición formal como 3 indicios separados | NOT_READY | Reforzar centro plausible sin confundir prominencia con función | Sin alcance afirmable | MORE SUPPORT + STILL BLOCKED: primario métrico sin inspeccionar; sin fusión | SEL + DIA |
| CAND-HAR-006 | Centro modal sin V–I con marcadores por tradición | STRONG_CANDIDATE | Centrar en modo sin sintaxis dominante | Por tradición modal | Sin medidas modales pop; sin kit universal | SEL |
| CAND-HAR-007 | Etiqueta sola no fija función | POSSIBLE_WITH_SCOPE | Asignar rol sin confundir etiqueta con función | Intra-tradición informativo | Sin medida de asignación; cautela negativa | DIA (+SEL) |
| CAND-HAR-008 | V–I privilegiado solo en práctica común acotada | POSSIBLE_WITH_SCOPE | Llegada dirigida fuerte sin universalizar | Clásica / pre-tónica pop | Mitad positiva con pedagogía parcial; sin acción | SEL |
| CAND-HAR-009 | Root motion solo no fija función/dirección | POSSIBLE_WITH_SCOPE | No inferir dirección solo desde roots | General + contexto | Peso propio del root sin medir; corpus = conteo | DIA |
| CAND-HAR-010 | Frecuencia != expectativa != función != receta | POSSIBLE_WITH_SCOPE | No convertir conteos en expectativa | General metodológico | Frecuencias rock = intuición; aprendizaje GAP | DIA |
| CAND-HAR-011 | Loops pop/rock organizables sin sintaxis clásica | POSSIBLE_WITH_SCOPE | Sostener sección en ciclo | Pop/rock/loop-based | Interpretable != coherencia medida; acción vacía | SEL + DIA |
| CAND-HAR-012 | Dominante como indicios distribuidos; dominante != tensión | POSSIBLE_WITH_SCOPE | Leer/construir dominante sin reducirla | Por tradición | Sin pesos/sustituibilidad; tensión no medida | DIA + SEL |
| CAND-HAR-013 | Continuidad por tono común literal o movimiento pequeño | POSSIBLE_WITH_SCOPE | Conectar sin imponer sintaxis ni minimización | Contextual con escucha | Heurística débil; sin mecanismo común ni dosis | REA (abstracta + realizada) |
| CAND-HAR-014 | Distancia mínima no objetivo universal | POSSIBLE_WITH_SCOPE | No optimizar economía ciega | General negativo | Sin medida de preferencia | REA + DIA |
| CAND-HAR-015 | Tendencias como normas clásicas acotadas | POSSIBLE_WITH_SCOPE | Resolver o no tonos activos | Práctica común | Expectativa no medida; sin lenguaje perceptivo | SEL + REA |
| CAND-HAR-016 | Etiqueta/root/bajo no determinan voces; 5 niveles | POSSIBLE_WITH_SCOPE | Planear conducción sin deducirla del cifrado | General metodológico | Peso etiqueta/root sin medir | REA + DIA |
| CAND-HAR-017 | Paralelas como norma de juego clásico | POSSIBLE_WITH_SCOPE | Aplicar restricción solo con juego declarado | Clásica polifónica | "Suenan mal" no justificado | REA + DIA |
| CAND-HAR-018 | Continuidad != función (no-equivalencia, no independencia) | POSSIBLE_WITH_SCOPE | Diseñar continuidad y función separables | General | Sin covariación medida | DIA (+REA/SEL) |
| CAND-HAR-019 | Octava/registro cambia organización (analítico) | NOT_READY | Colocar registro sin tratar octavas como intercambiables | Sin alcance decisional | MORE SUPPORT + STILL BLOCKED: equivalencia/continuidad sin medir; acción vacía | REA |
| CAND-HAR-020 | Planing como organización legítima acotada | POSSIBLE_WITH_SCOPE | Usar bloque sin tratarlo como error | Repertorios acotados | Sin efecto medido; invariantes por caso | REA + SEL |
| CAND-HAR-021 | Tasa armónica != tempo != actividad arreglo | POSSIBLE_WITH_SCOPE | Especificar ritmo armónico sin confundirlo | General metodológico | Sin unidad privilegiada | DIA + X-D |
| CAND-HAR-022 | Duración != importancia/estabilidad/tónica | POSSIBLE_WITH_SCOPE | Durar sin prometer importancia | General negativo | Sin curva dosis→centro | SEL + DIA |
| CAND-HAR-023 | Aceleración como dispositivo clásico acotado | POSSIBLE_WITH_SCOPE | Acelerar sin prometer tensión/llegada | Clásica sentence + resto uncertain | Desaceleración uncertain; loops uncertain | SEL + X-D |
| CAND-HAR-024 | Superficie-en-región solo bajo marco declarado | POSSIBLE_WITH_SCOPE | Mover superficie sin abandonar región | Con marco | Jerarquía audible sin medida | DIA + SEL |
| CAND-HAR-025 | Prolongación = 6 sentidos por marco; sin marco infalsable | POSSIBLE_WITH_SCOPE | Usar el término sin vaciarlo | Metodológico | Ningún marco = verdad general | DIA |
| CAND-HAR-026 | Loop/vamp/pedal organiza cíclicamente; cambio formal en arreglo | POSSIBLE_WITH_SCOPE | Sostener estasis con interés formal | Pop/rock/groove/loop | Jerarquía interna abierta | SEL + X-D |
| CAND-HAR-027 | Cadencia clásica como proceso contextual | POSSIBLE_WITH_SCOPE | Distinguir cadencia de llegada | Clásica + resto uncertain | Sin acción positiva | DIA + SEL |
| CAND-HAR-028 | Llegada tónica != cierre; armonía aportador parcial | POSSIBLE_WITH_SCOPE | Diseñar llegada y cierre por separado | General + cross-domain | Cierre exige melodía/metro/forma; acción débil | SEL + X-D |
| CAND-HAR-029 | PAC>IAC>HC analítico != ranking perceptivo | POSSIBLE_WITH_SCOPE | Ponderar llegadas sin universalizar | Clásica/teclado/músicos | Betas prohibidos como pesos; hipótesis | DIA |
| CAND-HAR-030 | IV–I y llegadas modales como fórmulas por tradición | POSSIBLE_WITH_SCOPE | Llegada idiomática sin tratarla como deficiente | Por tradición | Sin medida de cierre | SEL |
| CAND-HAR-031 | Retorno loop != cadencia; frontera por parada/arreglo | POSSIBLE_WITH_SCOPE | Frontera cíclica sin sintaxis clásica | Loop-based | Terminal-vs-corte uncertain | SEL + X-D |
| CAND-HAR-032 | Final tónico-sin-cadencia y final no-tónico legítimos; nada garantiza cierre | POSSIBLE_WITH_SCOPE | Terminar sin prometer cierre | Por escala formal | Existencia, no licencia | SEL |
| CAND-HAR-033 | Tonicalización vs modulación como diagnóstico clásico sin umbral | POSSIBLE_WITH_SCOPE | Enfatizar grado sin declarar cambio de centro | Práctica común | Fuera uncertain → HAR-007 | DIA + SEL |
| CAND-HAR-034 | Etiqueta V/x != prueba de centro local percibido | POSSIBLE_WITH_SCOPE | No sobreatribuir tonicalización | General negativo | Sin acción positiva | DIA |
| CAND-HAR-035 | CENTER != COLLECTION; préstamo/schemas con centro persistente | POSSIBLE_WITH_SCOPE | Ampliar colección sin cambiar centro | Por marco + tradición | Audición de fuente sin medida; genre-sensitive | SEL + DIA |
| CAND-HAR-036 | Evento cromático admite múltiples análisis; etiqueta única = error | POSSIBLE_WITH_SCOPE | Diagnosticar sin etiqueta oficial | General metodológico | Sin medida | DIA |
| CAND-HAR-037 | Conducción/CTo7/CT+6 en región persistente declarada | POSSIBLE_WITH_SCOPE | Conectar con color sin declarar partida | Con marco clásico | Unidad audible sin medida | REA + SEL |
| CAND-HAR-038 | Cromatismo no proxy de tensión/inestabilidad/complejidad/emoción | POSSIBLE_WITH_SCOPE | No usar cromático como medidor | General negativo | Tensión multivariada pendiente | DIA |
| CAND-HAR-039 | Cromáticos recurrentes como miembros estables de loop | POSSIBLE_WITH_SCOPE | Sostener loop cromático sin sintaxis funcional | Pop/rock cíclico | Normalización/sorpresa no medidas | SEL |
| CAND-HAR-040 | Cifrado infradetermina realización; selección vs realización separadas | POSSIBLE_WITH_SCOPE | Realizar sin asumir sonoridad única | General representacional | No toda realización preserva función | REA + DIA (eje SEL/REA) |
| CAND-HAR-041 | Root/bajo DISTINCT que pueden divergir; bajo como capa coordinable | POSSIBLE_WITH_SCOPE | Mover bajo como capa propia | Diagnóstico + manipulación sin ponderación | Sin peso bajo-vs-root; sin técnica; no desbloquea 002 | REA + DIA |
| CAND-HAR-042 | Jerarquía de inversión = lectura de tradición; 6/4 descompuesto | POSSIBLE_WITH_SCOPE | Elegir fundamental/inversión sin jerarquía universal | 6/4 cadencial clásico + resto marco/GAP | Sin técnica positiva; Sears nunca peso | REA + DIA |
| CAND-HAR-043 | Igual pitch-class set con distinta realización = distinta conducción concreta | POSSIBLE_WITH_SCOPE | Leer conducción desde alturas exactas | Analítico/decisionario | Ningún efecto perceptivo prometido | REA |
| CAND-HAR-044 | Duplicación/omisión SATB acotadas; jazz rootless GAP | POSSIBLE_WITH_SCOPE | Duplicar/omitir por idioma | Por sistema declarado | Mitades con soportes separados; sin medida ni acción | REA |
| CAND-HAR-045 | Registro/spacing cambian sonoridad sin fijar función/centro/calidad | POSSIBLE_WITH_SCOPE | Conformar sonoridad sin leer función en ella | Sonoro con escucha; timbre fuera | Sin dosis; marcos acústicos sin apoyo | REA (+X-D arreglo) |

Confirmación: CAND-HAR-001–045 = 45/45 representados. Ningún omitido.

---

# 9. Selection vs Realization Matrix

`BOTH / INTERFACE` donde la decisión cruza niveles. Sin pesos numéricos.

| Decisión | ¿Selección o realización? | Qué se sabe | Qué está bloqueado | Soporte (candidatos) | Scope | Dependencia cross-domain |
|---|---|---|---|---|---|---|
| Elegir objetivo armónico siguiente | SELECTION | Rol por contexto; loops sin sintaxis; dominante por indicios | Ponderación de indicios; función interna loops | 007–012 | Por tradición | Melodía/bajo/forma |
| Elegir root relation | SELECTION (abstracta) | Root motion insuficiente solo; quintas frecuentes sin puente perceptivo | Fuerza/dirección por root solo | 009, 008, 010 | General negativo + clásica acotada | Bajo (co-determina) |
| Elegir bajo | REALIZATION (capa coordinable) | DISTINCT de root; pedal fija/engaña; trayectoria coordinable | Ponderación bajo-vs-root; técnica de trayectoria; pedal como fijador | 041 + 002 bloqueado | Diagnóstico general; técnica pendiente | Arreglo (grave), melodía (convergencia) |
| Elegir inversión | REALIZATION | Anti-jerarquía; 6/4 cadencial clásico; tónica frágil pop analítica | Técnica positiva; 6/4 no-cadencial; medida root-vs-inversiones | 042 + 002/005 parcial | Por marco | Melodía (superior), forma (llegada) |
| Elegir alturas exactas | REALIZATION | Misma etiqueta admite varias; enarmónica cambia lectura | Criterio revoicing→otra armonía; fundamentales implicadas | 040, 043, 036 | Por marco declarado | Arreglo (capas), melodía |
| Elegir registro | REALIZATION (+X-D) | Cambia sonoridad; no fija función; octavas no intercambiables analíticamente | Equivalencia/continuidad percibida; dosis; prominencia | 045 + 019 bloqueado | Sonoro general; perceptivo bloqueado | Arreglo/timbre (CROSS_DOMAIN_REQUIRED si afecta) |
| Elegir spacing | REALIZATION | Dimensión sonora; close != conexión, open != potencia | Receta close/open; curva dosis→efecto | 045 | Sonoro, sin receta | Arreglo (fusión/enmascaramiento) |
| Elegir duplicación | REALIZATION | Sistemas acotados (SATB, power-chord); 5ª omitible en marcos | Política general; jazz rootless; medida | 044 | Por idioma declarado | Arreglo (capas/densidad) |
| Elegir omisión | REALIZATION | 5ª omitible; 3ª/7ª cambian identidad en marcos; root omitido != no-interpretación analítica | Audición de fundamental implicada; criterio general | 044 | Por marco | Arreglo |
| Elegir retención de tono común | INTERFACE (abstracta + realizada) | Heurística débil (retención literal o paso pequeño); pedal bidireccional | Mecanismo común; dosis; continuidad percibida | 013 + 043 | Contextual con escucha | Ninguna directa |
| Elegir asignación de voces | REALIZATION (+X-D melodía) | Bajo con lógica propia; superior doblemente restringida; interiores portan color | Importancia medida de interiores; streaming armónico | 043, 041, 016 | Por textura (SATB vs capas) | Melodía (superior = melodía) |
| Elegir nota superior | INTERFACE (REALIZATION + MELODY) | Superior condiciona conducción y prominencia parcial | Elección bajo melodía dada → HAR-009 | 043, 028/029 parcial | Bloqueado sin melodía | MELODY (directo) |
| Elegir onset armónico | INTERFACE (SELECTION + REALIZATION + RHYTHM) | 6 variables separadas; revoicing no es onset automático | Unidad privilegiada; colocación prescriptiva | 021, 040, 026 | Metodológico + género | Rhythm/Meter, Arrangement |
| Elegir sonoridad de llegada | INTERFACE (SELECTION + REALIZATION + FORM) | Proceso > par; llegada != cierre; inversión no mide fuerza | Fuerza sentida fuera clásica; terminal-vs-corte | 027–032, 042, 041 | Por tradición | Melodía/metro/forma/arreglo |
| Elegir interpretación cromática | SELECTION (con modulador de realización) | Matriz de lecturas; fuente por marco; bajo/voicing modulan lectura analítica | Reinterpretación perceptiva; umbral tonicalización/modulación | 033–039, 040/041/043 | Por marco | Melodía (línea cromática) |

---

# 10. Decision Conflict / Tradeoff Matrix

| Conflicto | Polos | Qué se sabe | Qué falta para elegir bien | Candidatos |
|---|---|---|---|---|
| Tonos comunes vs diferenciación/planing | CONNECT vs ARTICULATE | Ambos legítimos por contexto; planing acotado | Criterio de cuándo articular deliberadamente | 013/014/020 |
| Economía de movimiento vs trayectoria de bajo/melodía | Mínimo vs línea | Mínimo no objetivo; bajo/melodía tienen lógica propia | Curva coste→efecto; pesos | 014/041 |
| Centro vs ambigüedad | ESTABLISH vs AMBIGUATE | Ambigüedad legítima documentada; sin receta | Técnica de ambigüedad deliberada | 004/006/011 |
| Dirigida vs cíclica | Progresión vs loop | Elección por marco; gestos locales en loops | Función interna loops | 008/011/026/039 |
| Superficie vs región | Cambiar vs persistir | Heurística superficie-en-región con marco | Criterios de subordinación fuera tradición | 024/025/037 |
| Llegada fuerte vs apertura | ARRIVE vs REMAIN OPEN | Repertorio de opciones por tradición | Efecto fuera clásica; medida terminal-vs-corte | 027–032 |
| Colección vs expansión | Diatónico vs cromático | Familia de mecanismos; fuente por marco | Umbral tonicalización/modulación | 033–039 |
| Claridad vs lecturas múltiples | Una lectura vs matriz | Higiene: no forzar etiqueta única | Discriminación entre lecturas admisibles | 036/034 |
| Selección fijada vs realización variada | Misma armonía, otro voicing | Realización varía sonoridad y conducción concreta | Cuándo la variación cruza a otra armonía | 040/043 |
| Bajo = root vs bajo divergente | Refuerzo vs capa propia | Divergencia legítima; sin ponderación | Cuándo converger/divergir y con qué trayectoria | 041/002 |
| Close vs open | Densidad vertical | Sin receta; ambos cambian sonoridad | Dosis→efecto; fusión/timbre | 045 |
| Duplicar fundamental vs color (3ª/7ª) | Estabilidad analítica vs color | Sistemas acotados; sin ley general | Medida de efecto por idioma | 044 |
| Registro grave rico vs claridad | Sonoridad vs inteligibilidad | Registro cambia sonoridad; rugosidad != función | Psicoacústica aplicable + arreglo | 045 |

---

# 11. Actionability Audit

Categorías: ACTIONABLE NOW (heurística negativa/estructural usable ya con alcance); ACTIONABLE WITH SCOPE (solo en tradición/contexto explícito); DIAGNOSTIC ONLY (interpreta, no justifica generar); BLOCKED (la IA no debe actuar).

## Selección (de v0, conservada con ajustes menores)

- ACTIONABLE NOW: no decidir estabilidad desde sonoridad aislada; no inferir tónica desde frecuencia/primero/final; no inferir función desde etiqueta/root solo; no usar cromatismo/dominante como proxy de tensión; no tratar llegada como cierre ni categoría como fuerza; especificar ritmo separado de tempo; declarar marco ante "prolonga"; vocabulario neutral loop/frontera.
- ACTIONABLE WITH SCOPE: colección+recurrencia; centro modal; V–I clásico; loops; tono común/paso pequeño con escucha; tendency/paralelas/planing en tradición; aceleración sentence clásica; fórmulas plagales/modales; préstamos/conducción/CTo7 con fuente+resolución+escucha.
- DIAGNOSTIC ONLY: fuerza cadencial por categoría; función cromática por matriz; atribución local tras V/x.
- BLOCKED: ponderación de centro/duración/posición/registro; cierre ponderado multi-dominio; función interna loops; curva corpus→expectativa; frontera fuera clásica.

## Realización (nueva, núcleo de v1)

| Variable | Clasificación | Justificación |
|---|---|---|
| BASS | Estructuralmente manipulable + diagnosticable; NO ponderable → entre WITH SCOPE (diagnóstico) y BLOCKED (elección ponderada) | 041 POSSIBLE (DISTINCT, trayectoria coordinable) pero 002 NOT_READY (sin medida, sin técnica). Formulación exacta: "estructuralmente manipulable pero perceptivamente débilmente guiada; prohibida la inferencia de centro/función desde el bajo solo" |
| INVERSION | WITH SCOPE (negativa) + DIAGNOSTIC ONLY (positiva acotada) | 042: anti-jerarquía usable ya; elección positiva solo con marco (6/4 cadencial clásico; subtipos resto marco/GAP). Sin técnica general |
| REGISTER | Manipulable + DIAGNOSTIC ONLY; elección ponderada BLOCKED | 045 manipulable como sonoridad; 019 bloquea equivalencia/continuidad percibida y dosis. "Estructuralmente manipulable pero perceptivamente débilmente guiada" |
| SPACING | Manipulable + DIAGNOSTIC ONLY | 045: cambia sonoridad sin receta; sin curva; fusión/timbre cross-domain |
| DOUBLING | WITH SCOPE (intra-sistema) ; general BLOCKED | 044: dentro de sistema declarado las normas aplican; fuera, ninguna política general |
| OMISSION | WITH SCOPE (5ª en marcos; 3ª/7ª cambian identidad) ; root omitido BLOCKED perceptivamente | 044: quinta omitible documentada; fundamental implicada no presumible |
| VOICE ALLOCATION | PARTIALLY (manipulable con restricciones) ; bajo melodía dada BLOCKED → HAR-009 | 043/041/016: restricción superior/bajo conocidas; optimización pendiente; elección bajo melodía fija cede a HAR-009 |

**Regla de no-promoción:** la existencia de un candidato POSSIBLE_WITH_SCOPE nuevo NO eleva automáticamente la actionability. La pregunta de control es: ¿puede el sistema ELEGIR entre alternativas con criterios? Para realización la respuesta general es NO todavía en positivo ponderado; SÍ en manipulación diagnosticada con marco y escucha. Por eso el resultado probable anticipado se confirma exactamente: "estructuralmente manipulable pero perceptivamente débilmente guiada".

---

# 12. Diagnostic Power vs Generative Power

Nueva sección de integración (exigida por el encargo). DIAGNOSTIC POWER = ¿puede la IA describir/clasificar lo que ocurre sin malclasificarlo? GENERATIVE POWER = ¿puede elegir una operación para un objetivo musical con criterios justificados?

| Área | Diagnostic power | Generative power |
|---|---|---|
| Estabilidad / centro | MEDIA-ALTA negativa (qué NO determina centro) + MEDIA positiva con alcance | BAJA-MEDIA: indicios sin ponderación; sin dosis; 002/005 bloqueados |
| Dirección / función | MEDIA-ALTA (rol por contexto; loops clasificados; dominante desagregada) | BAJA-MEDIA: sin pesos; sin función interna loops; sin predicción transición→expectativa |
| Conexión abstracta | MEDIA (parentesco, planing, articulación) | BAJA-MEDIA: heurística débil 013 con escucha |
| Conexión realizada | MEDIA (inventario bajo/inversión/registro/conducción concreta) | BAJA: manipulable sin criterio ponderado; 043 analítica |
| Timing | MEDIA-ALTA (6 variables; criterio onset declarable) | BAJA-MEDIA: higiene usable; sin dosis ni curva tasa→energía |
| Persistencia | MEDIA (marco obligatorio; superficie-en-región) | BAJA: operaciones condicionales; sin técnica general |
| Llegada / cierre | MEDIA (proceso vs par; llegada vs cierre; fórmulas por tradición) | BAJA-MEDIA con alcance; cierre coordinado CANNOT YET sin melodía/forma |
| Cromatismo | MEDIA-ALTA (matriz de lecturas; fuente por marco) | BAJA-MEDIA: con convergencia+escucha; frontera → HAR-007 |
| Bajo / inversión / voicing | MEDIA (qué suena, qué rol, qué marco) | BAJA: manipulación sin guía ponderada |
| Registro / spacing / duplicación / omisión | MEDIA-BAJA (qué dimensión cambió) | BAJA: sin dosis; por escucha e idioma |

**Conclusión:** Harmony acumula potencia diagnóstica considerable (especialmente anti-reglas: sabe lo que NO debe inferir) y potencia generativa débil y acotada. La competencia diagnóstica NO equivale a capacidad compositiva. El compositor artificial actual evita malclasificar mejor de lo que elige bien entre opciones. RQ-HAR-008 aumenta la potencia diagnóstica de realización sin elevar proporcionalmente la generativa: ahora se sabe QUÉ queda sin decidir (bajo, inversión, voicing exacto) y SE PUEDE manipular, pero no se sabe elegir bien entre opciones con criterios generales.

---

# 13. AI Harmony Reasoning Representation v1

Representación no ejecutable de razonamiento. Sin código, sin schema SongPlan, sin pesos numéricos, sin motor determinista. Actualiza v0 con los bloques SELECTION / REALIZATION separados.

```
HARMONIC CONTEXT
- center_evidence: indicios separados (collection, recurrence, bass_layer,
  duration, metric_position, formal_position, cadential_confirmation,
  registral_configuration) + competidores. Sin fusión ni pesos.
- collection: colección vigente declarada (+ centro de referencia si difieren).
- organization: directed / cyclic / ambiguous (+ marco de tradición).
- current_region: región/función solo si el marco lo permite, con ranuras
  FRAMEWORK, OBJECT, CRITERION, SCOPE, EVIDENCE TYPE.

GOAL (uno o varios; conflicto explícito)
- ESTABLISH / CONFIRM / MAINTAIN / WEAKEN / AMBIGUATE (centro).
- STAY / DEPART / CONTINUE / PREPARE / APPROACH / RETURN / CYCLE (organización;
  metas, no funciones oficiales).
- CONNECT vs ARTICULATE (conexión abstracta).
- ARRIVE vs REMAIN OPEN (llegada/apertura).
- EXPAND con fuente declarada (mezcla, aplicado, conducción, tono común,
  loop-membership, ambigüedad).

HARMONIC SELECTION
- target_identity_or_relation: objetivo o continuación cíclica declarada.
- timing: 6 variables (rate, duration, pattern, placement, structural_change;
  tempo aparte) + criterio de onset declarado.
- persistence: evento de superficie + región con marco declarado.
- chromatic_interpretation: matriz de lecturas admisibles; nunca etiqueta
  única forzada; TONICIZATION vs MODULATION vs MIXTURE vs LEADING vs
  LOOP-MEMBER.

HARMONIC REALIZATION
- bass: nota grave + rol (fundamental/inversión/pedal/línea/contrapunto/ancla/
  riff/non-chord/slash/trayectoria) + relación con root declarada (igual/diverge).
- exact_pitches: pitch classes + alturas + criterio de identidad (qué marco
  decide si un revoicing es otra armonía).
- inversion: fundamental/1ª/2ª con rol por marco (6/4 descompuesto
  obligatoriamente); sin inferencia de estabilidad/fuerza/calidad.
- register: colocación por voz; octavas no intercambiables analíticamente.
- spacing: disposición vertical declarada; sin receta close/open.
- doubling_omission: qué se duplica/omite + sistema declarado; jazz rootless
  solo como GAP.
- voice_assignment: qué voz lleva qué altura (superior/bajo/interiores);
  superior pendiente de melodía si existe.

CROSS-DOMAIN CONSTRAINTS (estado por dominio: blocks / improves / independent)
- melody: superior fija, chord-vs-non-chord, voicing bajo melodía dada.
- rhythm_meter: colocación, onset, síncopa, densidad.
- form: escala frase/sección/canción; frontera cíclica vs cadencial.
- arrangement_production: capas, densidad, timbre, fusión, mezcla, registro grave.
- lyrics_prosody: stress vs tiempo fuerte (cuando aplique).

UNCERTAINTIES / BLOCKERS
- unresolved: 002/005/019 u otros con possible_action vacío.
- cross_domain_dependency: qué dominio falta para cerrar cada decisión.
- perception_gap: afirmado analíticamente sin medida (atribución de centro
  por bajo, equivalencia registral, fuerza sentida, normalización de loop,
  fundamentales implicadas).
```

Fuera explícito: pesos, curvas, gramática T–PD–D universal, máquina de estados, valores por defecto de voicing.

---

# 14. Composer Capability Check

Escala: CAN REASON / CAN REASON WITH SCOPE / PARTIALLY / CANNOT YET. Se distingue CAN MANIPULATE (mover la variable) de CAN CHOOSE WELL (elegir entre opciones con criterios). El proyecto necesita lo segundo.

| Capacidad | v0 | v1 | Comentario v1 |
|---|---|---|---|
| Seleccionar identidad armónica | PARTIALLY | PARTIALLY (sin cambio) | Rol por contexto sin pesos; HAR-008 no añade criterio de selección |
| Seleccionar bajo separado del root | BLOCKED (dentro de ponderación) | CAN MANIPULATE sí / CAN CHOOSE WELL todavía NO → PARTIALLY como capacidad, WITH SCOPE como diagnóstico | 041 permite mover y diagnosticar el bajo; 002 bloquea elegir bien con ponderación |
| Elegir inversión | BLOCKED/implícito | CAN MANIPULATE sí / CAN CHOOSE WELL solo con marco → CAN REASON WITH SCOPE (negativa) + PARTIALLY (positiva) | Anti-jerarquía usable; positiva solo 6/4 cadencial clásico y marcos declarados |
| Elegir voicing exacto | BLOCKED | CAN MANIPULATE sí / CAN CHOOSE WELL NO → PARTIALLY | 040/043/045: se puede variar realización con inventario; sin criterio ponderado |
| Realizar dos acordes seleccionados con movimiento intencional de voces | WITH SCOPE | WITH SCOPE (reforzado en mitad realizada) | 013 + 043: intención CONNECT/ARTICULATE con escucha; configuración concreta decidible analíticamente |
| Preservar un tono común literal | WITH SCOPE | CAN REASON WITH SCOPE | Operación estructural disponible; efecto (continuidad percibida) solo con escucha; pedal bidireccional como límite |
| Cambiar registro deliberadamente | BLOCKED | CAN MANIPULATE sí / CAN CHOOSE WELL NO → PARTIALLY | 045: cambio sonoro decidible; función/efecto no prometidos; 019 bloquea equivalencia |
| Crear distintas realizaciones de armonía repetida | — (no evaluada en v0) | CAN REASON WITH SCOPE (estructural) | 040 + HAR-004: revoicing/inversión/bajo como variación de superficie; si cuenta como evento depende de marco + escucha |
| Elegir duplicación/omisión | BLOCKED | CAN REASON WITH SCOPE intra-sistema; CANNOT YET general | 044: dentro de idioma declarado sí; política general no existe |
| Planificar trayectoria de bajo | — | PARTIALLY (capa coordinable sin técnica) | 041: capa propia reconocida; sin técnica de trayectoria; ver §15 |
| Coordinar bajo y voces superiores en la llegada | WITH SCOPE parcial | PARTIALLY (mejor diagnosticado, igual de débil en elección) | 041/042/028: inventario de llegada completo; fuerza sentida sin medida |

**Delta v0→v1:** ningún CAN REASON pleno nuevo en positivo; una familia (realización) pasa de BLOCKED a manipulable-con-diagnóstico; la brecha entre manipular y elegir bien queda explícita y medida. El avance es arquitectónico (se sabe qué decidir y en qué orden) más que generativo (todavía no se sabe elegir bien entre voicings con criterios generales).

---

# 15. Bass Trajectory

¿Puede Harmony razonar positivamente sobre una línea de bajo? Respuesta: parcialmente, como capa coordinable sin técnica.

- **¿Decidir cuándo el bajo debe igualar al root?** NO con criterios generales. Convergencia root=bajo como refuerzo de centro es plausible solo con convergencia de indicios y marco; prescribirla como regla es error (002 bloqueado). En marcos declarados (bajo fundamental clásico de llegada, pedal modal, riff/ostinato pop) sí, con alcance.
- **¿Decidir cuándo debe divergir?** SÍ como posibilidad diagnosticada (inversiones de paso, pedal bajo cambios, slash como línea independiente, bajo cromático de conducción), pero sin criterio de cuándo divergir mejor. La divergencia es legítima; su bondad es contextual con escucha.
- **¿Planificar pedal?** Solo como opción con doble filo documentado (fija en "Sara", engaña en "Human"). Pedal != fijador ni prolongación probada. Planificable como superficie, no como garantía.
- **¿Trayectoria para organización dirigida/cíclica?** Reconocida como capa (041) sin técnica: 5→1 como indicio scope-dependiente, líneas diatónicas/cromáticas como conducción, ostinatos como organización cíclica. Ninguna trayectoria promete dirección, centro o cierre por sí sola.
- **¿Coordinar bajo con voz superior?** Inventario disponible (movimiento relativo, cruce, ancla grave vs soprano móvil, convergencia melodía-sobre-bajo como indicio parcial) pero elección bajo melodía dada cede a HAR-009; bajo en modulación cede a HAR-007.

**Consecuencia para HAR-007 vs HAR-009:** la trayectoria de bajo es coordinable dentro de un centro pero no resuelve cambio de centro (requiere HAR-007) ni sirve bajo melodía dada (requiere HAR-009). No decide por sí sola entre ambas; ambas la necesitan. El desempate debe venir de otro criterio (ver §21).

---

# 16. Existing Blocked Candidates

Preservados sin re-auditoría. Solo se responde qué decisiones deben seguir prohibidas.

## CAND-HAR-002 — MORE SUPPORT + STILL BLOCKED

Soporte añadido por HAR-008: inversión/bajo modulan analíticamente atribución de centro (tónicas frágiles, pedal fija/engaña, vamp §12, modal Everett, configuración Doll, convergencia melodía-sobre-bajo, split Sears parcial).

Sigue bloqueado: ninguna medida dedicada de ponderación bajo-vs-root; sin pesos; sin `possible_action`.

**Prohibido:** inferir centro desde bajo/root-en-bajo/pedal/bajo-repetido solos; prescribir pedal como fijador; tratar root y bajo como intercambiables; ponderar indicios de centro numéricamente.

## CAND-HAR-005 — MORE SUPPORT + STILL BLOCKED

Soporte añadido: split Sears (registración como indicio parcial en tarea Mozart/teclado) como indicio adicional separado; Spicer §12 como convergencia duracional débil.

Sigue bloqueado: primario métrico (Temperley 2001) sin inspeccionar; Caplin clásico sin transferencia pop; sin fusión de duración/metro/forma; sin dosis; sin `possible_action`.

**Prohibido:** probar centro desde duración/posición sola; convertir prominencia (larga, fuerte, inicial, final) en función; fusionar indicios en un score.

## CAND-HAR-019 — MORE SUPPORT + STILL BLOCKED

Soporte añadido: independencia de pitch/pitch-class/registro/voz/octava reforzada; disociación enarmónica OMT (mismas alturas, distinta función); split Sears bajo/soprano; indicio propio EXP-001 B=3 (transposición pequeña penaliza, n=1).

Sigue bloqueado: equivalencia/continuidad perceptiva bajo manipulación registral sin medir; streaming/proximidad con estímulos armónicos pendiente; `possible_action` vacío.

**Prohibido:** tratar octavas como intercambiables en decisiones; derivar continuidad percibida, prominencia o preferencia desde distinción registral; usar registro como guía ponderada de conducción o cierre.

---

# 17. Cross-Candidate Consistency Pass

Además de los pares de v0 (sin contradicciones fácticas sin delimitar), se inspeccionan los pares exigidos:

- **040 vs 016:** consistentes y mutuamente reforzantes. 016 (etiqueta/root/bajo no determinan voces) es el caso particular de conducción del principio general 040 (identidad infradetermina sonoridad). Sin contradicción. 040 amplía el alcance de 016 a todas las dimensiones de realización.
- **040 vs 043:** consistentes con división del trabajo. 040 afirma multiplicidad de realizaciones; 043 afirma consecuencias concretas de conducción de cada realización. 040 abre el espacio, 043 lo hace decidible analíticamente. Ninguno promete efecto perceptivo.
- **041 vs 002:** consistencia delicada pero sin contradicción. 041 (DISTINCT/DIVERGE, capa coordinable, HYPOTHESIS diagnóstica) NO desbloquea 002 (ponderación, NOT_READY). La distinción sin peso es compatible con el bloqueo de peso. Riesgo vigilado: leer 041 como si resolviera 002. Se prohíbe explícitamente.
- **041 vs 009:** consistentes. 009 (root motion insuficiente) + 041 (trayectoria de bajo como capa) implican que dirección requiere ambas capas más contexto. Root motion y bass trajectory permanecen distintas y ninguna basta sola.
- **042 vs 003:** consistencia con cautela. 042 (anti-jerarquía de inversión) NO debe leerse como 003 (consonancia != estabilidad) aplicada al bajo: inversión no es sonoridad aislada sino rol contextual. La jerarquía de inversión no se convierte en jerarquía de estabilidad desnuda. Delimitado.
- **042 vs 028/029:** consistentes con prohibición explícita. Inversión en la llegada (042) no mide fuerza de cierre (028/029). Llegar en inversión puede ser llegada válida sin ser cierre fuerte; la fuerza sentida exige convergencia cross-domain.
- **043 vs 013/014:** consistentes. 043 (realización cambia configuración de conducción) no convierte mínimo movimiento en objetivo (014 lo prohíbe) ni promete continuidad (013 la deja en heurística débil). Consecuencia decidible != preferencia.
- **043 vs 019:** consistencia con cesión explícita. 043 usa la distinción de 019 como herramienta decisionaria (qué altura exacta retener/mover) sin reclamar lo que 019 bloquea (equivalencia/continuidad percibida). Consecuencia concreta vs efecto bloqueado: delimitado.
- **044 vs 015/017:** consistentes. Las tres son restricciones de idioma/tradición acotadas (tendency, paralelas, duplicación/omisión). Ninguna es ley perceptiva; todas exigen sistema declarado. Pedagogía acotada tratada uniformemente.
- **045 vs 003:** consistentes. 045 (sonoridad realizada/acústica) != 003 (estabilidad tonal contextual/función). Registro/spacing cambian lo primero sin determinar lo segundo. Delimitado.
- **045 vs 019:** consistentes. 045 preserva distinciones registrales (qué cambió sonoramente) sin reclamar efectos de continuidad que 019 bloquea. Descripción sonora vs efecto: delimitado.
- **HAR-008 vs HAR-004:** consistencia con regla de criterio. Revoicing/inversión/bajo pueden ser evento sonoro sin ser onset armónico estructural; el criterio de onset se declara por marco. Ni "revoicing = nueva armonía" ni "mismo cifrado = sin evento" como automáticos.
- **HAR-008 vs HAR-006:** consistencia con distinción análisis/percepción. Bajo/voicing cambiado puede alterar la lectura analítica (reinterpretación musicológica) sin probar reinterpretación perceptiva (re-escucha del oyente como otro centro/función). La primera documentada; la segunda no medida.

**Contradicciones no resueltas:** ninguna factual sin delimitar. Tensiones vivas (no contradicciones): desarrollo dirigido vs estasis/loop como virtud (resuelta por scope); 6/4 como inestabilidad de rol vs fragilidad pop como color (delimitadas por marco, no fusionadas); pedal como fijador vs engañador (ambos documentados, sin regla causal: es el límite, no un error).

---

# 18. Cross-Domain Dependency Map

| Decisión armónica | Dominios de los que depende | Qué falta |
|---|---|---|
| Establecer/mantener centro | Rhythm/Meter (posición, duración), Form (posición, retorno), Arrangement (bajo, densidad, capas) | Ponderación 002/005; medida con canciones |
| Dirección percibida | Melody (confirma/contradice), Bass realizado (co-determina), Form (frase vs sección) | Pesos; función interna loops |
| Conexión realizada | Melody (superior), Arrangement (capas, registro, timbre, fusión) | Medida continuidad/independencia; streaming armónico |
| Ritmo armónico funcional | Rhythm/Meter (colocación), Form (función seccional), Arrangement (onset distribuido, loops) | Unidad privilegiada; dosis |
| Cierre | Melody + Rhythm/Meter + Form + Arrangement + Lyrics/Prosody | Unidad melodía-armonía (HAR-009); medida terminal-vs-corte; fade GAP |
| Expansión cromática | Melody (línea cromática), Arrangement (voicing/timbre normalizan) | Umbral tonicalización/modulación (HAR-007); afecto GAP |
| Loops con interés formal | Arrangement/Production (capas, densidad, timbre) | Jerarquía interna; normalización perceptiva |
| Tónica ambigua/doble | Form seccional | Receta de ambigüedad; atribución por oyentes |
| Realización bajo melodía dada | Melody (HAR-009) | Voicing alrededor de nota fija; non-chord tones; duplicación de melodía |
| Cambio de centro | HAR-007 (modulación) | Tipos, pivotes, confirmación, retorno |

---

# 19. Melody–Harmony Interface Readiness

Actualización del preview de v0. Sin modificar Melody.

## Qué proporciona Melody que la realización armónica necesita

- Tres niveles de registro PHYSICAL/PERCEPTUAL/COMPOSITIONAL (tesitura habitable como restricción; prominencia como hipótesis débil; transposición pequeña provisional, amplia unsupported).
- Vocabulario rítmico obligatorio (duration, onset, IOI, pattern, meter, accent, syncopation con definición declarada, density con tempo controlado, silence tipificado) para colocar onsets armónicos y llegadas.
- Transformación motívica como operaciones (repetición exacta, transposición pequeña, final cambiado, redistribución rítmica, fragmentación+liquidación clásica) que la armonía debe sostener sin imponer sintaxis.
- Contribuciones parciales a llegada/cierre (pico, sustain, posición fuerte, alargamiento+silencio) que exigen soporte armónico para cerrar.
- Restricción de cantabilidad para la voz superior (tesitura, esfuerzo) que limita la asignación de voces.

## Qué proporciona Harmony que Melody necesitaba

- ORIENTAR/ORGANIZAR con cautelas + indicios débiles para enmarcar finales cambiados (pregunta vs cierre según marco armónico).
- Aceleración armónica clásica (023) como condición de fragmentación+liquidación que conduce (pendiente fuera de clásica).
- Llegada vs cierre separados (028) + fórmulas por tradición (030–032) como marco donde el cierre melódico parcial puede completarse (GAP-08).
- Matriz cromática (036) + mezcla/colección (035) para coordinar cromatismo melódico-armónico.
- Realización (040–045) como capa que Melody no tenía: bajo coordinable, inversión por rol, voicing exacto manipulable, registro/spacing como sonoridad.

## Interfaces candidatas (prompts, no conclusiones)

- MELODIC PITCH ↔ chord membership / non-chord status: BLOQUEADO hasta HAR-009 (RQ-MEL-007 pendiente).
- MELODIC REGISTER ↔ top-voice allocation / voicing: PARCIALMENTE preparada (045 + 043 + tesitura Melody) pero elección bajo nota fija BLOQUEADA hasta HAR-009.
- MELODIC RHYTHM ↔ harmonic onset / rhythm: VOCABULARIO listo en ambos lados (021 + RQ-MEL-006); colocación prescriptiva BLOQUEADA.
- MELODIC ARRIVAL ↔ bass/harmonic arrival: MARCO listo (028 + 041/042); fuerza coordinada BLOQUEADA (multi-dominio sin medida).
- MELODIC MOTIF TRANSFORMATION ↔ harmonic support across repetition/variation: PARCIAL (026 + 040: mismo ciclo con revoicing/arreglo cambiado como variación de superficie); normalización perceptiva BLOQUEADA.

## Bloqueadores de interfaz (solo identificados, no investigados)

1. Nota superior como melodía y miembro del acorde simultáneamente (doble restricción).
2. Inversión condicionada por objetivo melódico (bajo debe sostener sin duplicar ni enmascarar).
3. Voicing alrededor de nota melódica fija (qué asignación preserva cantabilidad y conducción).
4. Melodía duplicada en interiores/bajo (fusión vs prominencia).
5. Non-chord tone melódico sobre armonía realizada (qué disonancia es apoyatura/suspensión/color según marco).
6. Contrapunto bajo vs melodía (trayectoria grave bajo arco melódico).
7. Cambio armónico vs frase melódica (qué onset corta/sostiene la frase).

---

# 20. Modulation Dependency Map

Qué decisiones actuales no pueden completarse sin HAR-007 (solo dependencias, sin investigar modulación):

1. Cuándo la tonicalización local se convierte en nuevo centro (umbral confirmación+permanencia fuera de clásica; 033 cede a HAR-007).
2. Soporte del bajo al nuevo centro (pedal/posición que fija vs engaña a escala de cambio de centro; 041 cede).
3. Voicing de la armonía pivote/reinterpretada (qué realización facilita doble lectura; 040/043 ceden).
4. Confirmación de la nueva región (cadencia posterior, recurrencia, colección: criterios fuera de clásica pendientes).
5. Retorno/continuación tras cambio de centro (trayectoria a gran escala; forma seccional).
6. Distinción mezcla/colección vs cambio de centro en pop modal (035 cede: scalar shift y doble tónica como casos límite).

Ninguna de estas bloquea la coordinación melodía-armonía dentro de un centro. Solo bloquean piezas con cambio estructural de centro.

---

# 21. v0 → v1 Capability Delta

| Capacidad | v0 | v1 | Delta |
|---|---|---|---|
| Diagnosticar realización (qué bajo/inversión/voicing suena, qué rol cumple) | NO (bloqueo denso) | SÍ con marco (040–045) | +NUEVO |
| Manipular bajo/inversión/voicing/registro/spacing/duplicación/omisión estructuralmente | NO | SÍ (inventario 22 operaciones HAR-008) | +NUEVO |
| Elegir bien entre realizaciones con criterios generales ponderados | NO | TODAVÍA NO | Sin cambio (débilmente guiada) |
| Leer conducción desde realización exacta | Parcial (016 negativo) | SÍ analíticamente (043) | +REFORZADO |
| Criterio de onset con revoicing | NO | SÍ metodológico (criterio declarable) | +NUEVO |
| Inversión en llegada como medida | NO evaluada | NO como medida (prohibición explícita 042 vs 028/029) | +ACLARADO (negativo) |
| Selección (objetivo, timing, persistencia, cromatismo) | PARTIALLY/WITH SCOPE | Igual | Sin cambio |
| Cierre coordinado con melodía | CANNOT YET | CANNOT YET | Sin cambio (mejor diagnosticado) |
| Cambio de centro | PARTIALLY clásico / uncertain resto | Igual (→ HAR-007) | Sin cambio |

---

# 22. Unsupported / Blocked Knowledge

Lista consolidada de lo que la IA NO debe afirmar, inferir, prescribir ni ponderar:

1. Ponderación bajo-vs-root en centro/función (002).
2. Fusión duración/metro/forma en score de centro; dosis de duración/repetición (005).
3. Equivalencia/continuidad perceptiva registral; dosis de registro/spacing/duplicación (019/045).
4. Jerarquía universal de inversiones; 6/4 como propiedad única (042).
5. Política general de duplicación/omisión; fundamental implicada percibida; rootless como prueba (044).
6. Fuerza de cierre desde inversión/bajo/registro solos (042/041/045 vs 028/029).
7. Revoicing = nueva armonía / mismo cifrado = sin evento como automáticos (040 vs HAR-004).
8. Reinterpretación perceptiva desde cambio de bajo/voicing (HAR-008 vs HAR-006).
9. Tensión por dominante/cromatismo/tasa/disonancia como proxies (012/038/023).
10. Función desde etiqueta/root-motion/V/x solos (007/009/034).
11. Tónica desde frecuencia/primero/final/duración/posición solos (004/005/022).
12. Cierre desde llegada tónica, categoría cadencial, parada o tónica final solas (028/029/031/032).
13. Tonicalización percibida desde etiqueta aplicada; umbral tonicalización/modulación fuera clásica (034/033 → HAR-007).
14. Afecto fijo de préstamos/cromatismo/registro (035/038/045).
15. Corpus→expectativa→receta (010).
16. Elección de armonía/voicing bajo melodía dada; non-chord tones coordinados (→ HAR-009).
17. Fade-out como cierre; terminal-vs-corte ponderado (031/032 GAP).

---

# 23. Manual Readiness

**NO.**

La barra exigida (¿podemos enseñar un flujo compositivo general coherente y suficientemente apoyado?) no se alcanza:

- Lo positivo sigue mayoritariamente PROVISIONAL/WITH SCOPE con `possible_action` vacío en 13 candidatos heredados más realización sin guía ponderada.
- Ponderaciones de centro, bajo, registro y cierre siguen BLOCKED (002/005/019).
- Cierre coordinado y melodía bajo armonía exigen dominios ausentes (HAR-009).
- Fuentes PARTIAL con deudas (Doll/Nobile completos, Sears completo, corpus con juicios).
- Lo nuevo (040–045) es manipulable pero no enseñable como flujo prescriptivo general: enseña qué NO inferir y qué declarar, no qué elegir entre voicings.

Un manual prematuro convertiría heurísticas débiles y anti-reglas en recetas. Se mantiene la prohibición de poblar `manual/02-harmony.md`.

---

# 24. Rule Readiness

**NO.**

La barra exigida (¿puede el conocimiento volverse determinista/machine-checkable con seguridad?) tampoco se alcanza:

- Ninguna regla de selección o realización admite condiciones suficientes verificables sin escucha humana o marco estrecho declarado.
- Toda formalización actual colapsaría STRUCTURE→PERCEPTION→COMPOSITION (p. ej., "si bajo = root entonces centro = X", "si inversión = 6/4 entonces inestable", "si spacing = close entonces conexión").
- Lo único machine-checkable hoy son higienes negativas y convenciones de declaración (6 variables de timing separadas; 5 ranuras de prolongación; vocabulario neutral de loops; 5 niveles etiqueta/root/bajo/inversión/realización; 6/4 descompuesto; criterio de onset declarado). Son valiosas como validadores futuros, pero no constituyen reglas compositivas deterministas.
- Se mantiene la prohibición de crear `rules/harmony.yaml`.

---

# 25. HAR-007 vs HAR-009 Decision

Comparación por los ocho criterios del encargo, con evidencia de v1.

## 1. Número de bloqueadores actuales desbloqueados

- **HAR-007** desbloquearía: frontera 033 fuera de clásica (diagnóstico tonicalización/modulación), confirmación de nueva región, retorno tras cambio, voicing/bajo del pivote, parte de 035 en casos modales límite. Alcance estrecho: un mecanismo (cambio de centro) con pocos candidatos pendientes directos.
- **HAR-009** desbloquearía: GAP-08 melódico (cierre), RQ-MEL-007 (non-chord tones, apoyaturas, suspensiones), finales cambiados (CAND-MEL-008), elección de acorde bajo melodía y voicing bajo nota fija, duplicación de melodía, contrapunto bajo-melodía, coordinación de llegada (028 + 041/042 con soprano), y daría uso compositivo a toda la capa de realización HAR-008 (¿para qué sirve poder variar el voicing si no es bajo una melodía?). Alcance ancho: activa transversalmente selección + realización + cierre + cromatismo melódico.

Ventaja clara: **HAR-009**.

## 2. Composer leverage (capacidad positiva de elegir bien)

- HAR-007 añadiría una palanca estructural ocasional (cambiar de centro a gran escala), relevante en repertorios con modulación pero infrecuente en la canción pop/loop contemporánea dentro de un centro.
- HAR-009 ataca la decisión generativa más frecuente en canciones reales: qué armonía y qué realización bajo/sobre una melodía dada, compás a compás y frase a frase. Es donde la diferencia entre manipular y elegir bien más duele hoy (realización manipulable pero sin guía: §11–12).

Ventaja clara: **HAR-009**.

## 3. Prerrequisitos (¿uno requiere al otro? ¿está HAR-009 lista para empezar?)

- v0 aplazó HAR-009 por falta de bajo/voicing y forma/ritmo operativos. v1 constata que el prerrequisito de realización YA existe en forma diagnosticable y manipulable (040–045, matriz §9, representación §13). Lo que falta de forma/ritmo para HAR-009 es parcial pero suficiente para empezar (vocabularios listos, §19); la medida fina puede coevolucionar con la interfaz.
- HAR-007 no es prerrequisito de HAR-009 salvo en piezas modulantes; la coordinación melodía-armonía dentro de un centro es lógicamente previa y empíricamente dominante.
- HAR-009 no es prerrequisito de HAR-007 salvo para el voicing del pivote bajo melodía (caso particular).

Veredicto: **HAR-009 tiene ya fundamento suficiente para comenzar; HAR-007 no la bloquea**.

## 4. Cross-domain value (conexión Melody–Harmony existente)

- HAR-007 conecta Harmony consigo misma a gran escala (región→región) con poco uso del capital Melody v0.
- HAR-009 conecta directamente los dos capitales acumulados: Melody v0 (motivo, registro 3 niveles, ritmo, llegada parcial, transformación) con Harmony v1 (selección + realización). Es la única que convierte dos inventarios paralelos en decisiones conjuntas y pone a prueba si ambos sirven juntos.

Ventaja clara: **HAR-009**.

## 5. Theory-accumulation risk (¿otra taxonomía sin capacidad?)

- HAR-007 presenta riesgo ALTO de acumulación taxonómica: tipos de modulación (pivote/cromática/directa/tono común), pivotes por.SUCCESSION, confirmaciones y retornos, sin resolver la selección previa (¿para qué modular si aún no se elige bien dentro de un centro?). Repetiría el patrón diagnosticado en v0 para 007: alcance estrecho, un mecanismo, recetas universales como riesgo principal.
- HAR-009 presenta riesgo opuesto y más fértil: expone si la Harmony actual puede componer con melodía. Si falla, el fracaso es informativo (revela qué parte de selección/realización era hueca); si funciona parcialmente, produce capacidad positiva inmediata. El riesgo de taxonomía existe (tipos de non-chord tones) pero mitigable con la disciplina de esta integración (operación vs función, marco declarado, sin must-resolve universal).

Ventaja: **HAR-009** (riesgo fértil frente a riesgo estéril).

## 6. Song-level value (qué importa en canciones reales del scope)

- La mayoría de decisiones armónicas en canción pop/rock/loop operan dentro de un centro/colección (ciclos, préstamos, aplicados locales, revoicings, trayectorias de bajo, llegadas seccionales). El cambio estructural de centro es comparativamente raro y seccionalmente localizado.
- La decisión "qué armonía/realización bajo esta melodía en este compás" ocurre decenas de veces por canción. Es el cuello de botella transversal del proyecto (Melody v0: harmony como bottleneck; Harmony v0: cierre coordinado CANNOT YET).

Ventaja clara: **HAR-009**.

## 7. Blocked-candidate value (¿cuál atiende NOT_READY / CROSS_DOMAIN_REQUIRED?)

- HAR-007 no desbloquea 002/005/019 (ninguno es de cambio de centro) y atiende pocos CROSS_DOMAIN_REQUIRED salvo forma seccional.
- HAR-009 atiende directamente el mayor cúmulo CROSS_DOMAIN_REQUIRED (028 cierre, 026 loops con arreglo, 021 ritmo, 045 registro/timbre, superior melódica 043/041) y somete a 002/005/019 a su prueba más exigente (¿pesan bajo/duración/registro cuando hay melodía que confirma o contradice?). No los desbloquea por decreto, pero es el contexto donde su desbloqueo futuro se volverá medible.

Ventaja: **HAR-009**.

## 8. Future genre specialization (prerrequisito antes de género)

- Los géneros del scope (incluido indie-dance previsto) se diferencian más por cómo realizan y coordinan armonía con melodía/ritmo/arreglo (voicings de teclado/guitarra, bajo ostinato/syncopado, préstamos, loops con melodía cambiante, llegadas seccionales) que por cómo modulan entre centros.
- Sin HAR-009, la especialización de género carecería de la interfaz donde el género más se manifiesta (elección armónica bajo melodía y realización idiomática).

Ventaja: **HAR-009**.

## Criterio crítico (no confundir ausencia con prioridad)

"No hemos investigado modulación" es cierto pero no convierte a la modulación en la incapacidad que más impide componer bien hoy. La incapacidad actual, medida en §12 y §14, es: **sabemos diagnosticar y manipular armonía, pero no sabemos elegir ni realizar armonía bajo una melodía con criterios**. Esa es exactamente HAR-009. Elegir HAR-009 no es elegirla "por ser cross-domain": es elegirla porque es donde la brecha entre potencia diagnóstica y potencia generativa más bloquea decisiones reales compás a compás.

## Decisión v1

**Comenzar RQ-HAR-009 — Melody–Harmony Interaction.**

Derivada de la evidencia, no del orden numérico.

---

# 26. Recommended Next Research Step

**Begin RQ-HAR-009 — Melody–Harmony Interaction.**

Por qué (en una línea por criterio): desbloquea más bloqueadores y CROSS_DOMAIN_REQUIRED que HAR-007; aporta la palanca generativa más frecuente (acorde/realización bajo melodía); sus prerrequisitos de realización ya existen tras HAR-008; conecta los dos capitales Melody+Harmony; su riesgo es fértil (prueba si Harmony sirve componiendo); domina el valor song-level dentro de un centro; prepara la especialización de género.

No comenzar automáticamente. Esperar confirmación del Project Owner y del Music/Methodology Director.

---

# Apéndice A. Cuestiones para el Music/Methodology Director

1. ¿Se adopta la separación SELECTION vs REALIZATION (y los tres niveles con CROSS-DOMAIN REALIZATION) como arquitectura de razonamiento del proyecto?
2. ¿Se aprueba el SPLIT de CONECTAR en conexión abstracta vs conexión realizada con la regla de método (toda afirmación de conducción declara su nivel)?
3. ¿Se promueve CAND-HAR-040 a principio arquitectónico central con la formulación adoptada aquí?
4. ¿Se confirma la lectura de 041 (DISTINCT/DIVERGE sin ponderación, capa coordinable) con la prohibición explícita de leerla como desbloqueo de 002?
5. ¿Se confirma que 042 (anti-jerarquía + 6/4 parcial) prohíbe inferir estabilidad/fuerza/calidad desde inversión sin marco?
6. ¿Se acepta el veredicto "estructuralmente manipulable pero perceptivamente débilmente guiada" para realización como estado oficial hasta nueva medida?
7. ¿Se confirma HAR-009 como siguiente RQ frente a HAR-007 con la argumentación de §25?
