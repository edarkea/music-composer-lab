# Harmony Foundations v0 — Primera integración

## Estado y alcance de este documento

- Tipo: capa de integración y auditoría entre candidatos de investigación y eventual promoción a `manual/`. NO es conocimiento aprobado de `manual/`, ni regla de `rules/`, ni conocimiento de género de `genres/`.
- Cubre: RQ-HAR-001 (SYNTHESIZED, audit COMPLETED), RQ-HAR-002 (SYNTHESIZED, audit COMPLETED), RQ-HAR-003 (SYNTHESIZED, audit COMPLETED con división 017/020), RQ-HAR-004 (SYNTHESIZED, audit COMPLETED), RQ-HAR-005 (SYNTHESIZED, audit COMPLETED), RQ-HAR-006 (SYNTHESIZED, audit COMPLETED); CAND-HAR-001–039 (ningún ID rechazado, ningún ID reutilizado, ningún candidato nuevo).
- Conteos de integration-readiness heredados (no modificados): STRONG_CANDIDATE: 2 (003, 006) | POSSIBLE_WITH_SCOPE: 34 | NOT_READY: 3 (002, 005, 019) | REJECTED: 0. Próximo ID sin usar: CAND-HAR-040 (no creado en esta tarea).
- No se ha realizado investigación temática nueva, ni verificación externa nueva, ni experimentos, ni composición de ejemplos, ni codificación de reglas. EXP-002 sigue PAUSED. Ningún EXP-HAR existe.
- Scope general del proyecto: música popular tonal/modal occidental y tradiciones estrechamente relacionadas (common practice, pop, rock, electrónica/dance, prácticas modales, songwriting, cognición musical). Nada de lo aquí integrado se afirma fuera de ese ámbito. Toda evidencia perceptiva citada utiliza oyentes enculturados occidentales salvo indicación explícita. NO se afirma universalidad humana.
- Idioma: contenido humano en español; identificadores y claves técnicas en inglés.
- No se modifica ningún estado de candidatos, ni `manual/`, ni `rules/`, ni `genres/`, ni RQ-HAR-001–006, ni archivos Melody, ni experimentos, ni music-engine. NO se inicia RQ-HAR-007, RQ-HAR-008 ni RQ-HAR-009.
- Skills `.agents/skills/research-music-concept/SKILL.md` y `.agents/skills/audit-music-knowledge/SKILL.md` aplicadas manualmente: cada decisión integrada declara problema compositivo, variable manipulable, clase epistemológica, alcance, contraejemplos y falsación; ninguna afirmación plausible se presenta como hecho.
- Prohibido citar este archivo como conocimiento aprobado: es capa de auditoría previa a revisión del Project Owner y del Music/Methodology Director.

## Purpose and Scope

Este documento NO es un capítulo de manual, ni un resumen de seis RQs, ni una lista de reglas de acordes, ni una enciclopedia teórica, ni un generador de armonía, ni una promoción a conocimiento manual.

Responde a una sola pregunta:

> ¿Sobre qué decisiones armónicas puede ya razonar un sistema de composición a partir de RQ-HAR-001–006, con qué confianza, alcance y dependencias?

Pertenece a la capa GENERAL COMPOSITION KNOWLEDGE de la arquitectura:

```
GENERAL COMPOSITION KNOWLEDGE (manual/)
    → GENRE SPECIALIZATION (genres/)
    → CONCRETE COMPOSITION DECISIONS
    → SongPlan
    → music-engine
```

La presente integración vive antes de la especialización de género y antes de cualquier decisión concreta: organiza el conocimiento auditado en problemas compositivos con sus variables, operaciones, límites y dependencias.

## Epistemic Status

- Toda afirmación no trivial conserva la separación STRUCTURE → PERCEPTION → COMPOSITION. Ningún nivel implica automáticamente el siguiente.
- Clases de evidencia utilizadas: THEORY, GENRE OBSERVATION, COMPOSITION HEURISTIC, HYPOTHESIS (más soportes ortogonales registrados en cada YAML). Ningún EXPERIMENTAL RESULT propio existe en Harmony (sin EXP-HAR).
- Verificación de fuentes: PARTIAL en las seis RQs. Cuatro fuentes a texto completo inspeccionado (Spicer 2017, Everett 2004, Temperley 2011, de Clercq 2018 como reseña de Doll 2017); pedagogía Open Music Theory de RQ-HAR-006 a texto completo (tonicalización, mezcla modal, sexta aumentada, tonos comunes, mediantes, schemas modales); resto PARCIAL o pendiente (Doll 2017 texto completo, Nobile 2016, Biamonte 2010, Caplin 2024, Sears 2014/2015 textos completos, corpus pop/rock con juicios de oyentes como GAP estructural). Donde la debilidad de fuente afecta a una conclusión integrada, se marca explícitamente.
- Vocabulario de integración (distinto del readiness de candidatos): SUPPORTED, PROVISIONAL, TRADITION_SPECIFIC, GENRE_SPECIFIC, UNSUPPORTED, CROSS_DOMAIN_REQUIRED. Se permiten combinaciones (precedente: Melody v0), p. ej. `TRADITION_SPECIFIC + CROSS_DOMAIN_REQUIRED`. Readiness (STRONG_CANDIDATE / POSSIBLE_WITH_SCOPE / NOT_READY / REJECTED) e integration status son ejes ortogonales y se registran por separado en la matriz de cobertura.
- La integración no promueve conocimiento. Las evaluaciones de MANUAL READINESS y RULE READINESS están en sus secciones propias.

## From Research Domains to Composition Decisions

Las seis RQs son dominios de investigación, no decisiones. La integración las reorganiza alrededor de problemas compositivos, poniendo a prueba (no adoptando automáticamente) la arquitectura provisional:

ORIENT — ORGANIZE — CONNECT — TIME / PERSIST — ARRIVE / REMAIN OPEN — EXPAND / REINTERPRET — DIAGNOSE

Decisión arquitectónica de esta integración: se adopta la arquitectura con UNA modificación justificada. TIME y PERSIST se separan en dos familias (TEMPORIZAR y PERSISTIR) porque RQ-HAR-004 exige que ritmo armónico y prolongación permanezcan constructos explícitamente distintos (uno es variable temporal observable, el otro interpretación jerárquica dependiente de marco). DIAGNOSE no es una fase secuencial sino una capacidad transversal (asignar función a eventos ambiguos). El resultado:

1. ORIENTAR — establecer / interpretar orientación armónica (HAR-001).
2. ORGANIZAR — decidir organización dirigida vs. cíclica (HAR-002).
3. CONECTAR — conectar sonoridades sucesivas (HAR-003).
4. TEMPORIZAR — decidir cuándo cambia la armonía (HAR-004, mitad ritmo).
5. PERSISTIR — decidir qué persiste mientras la superficie cambia (HAR-004, mitad región).
6. LLEGAR / MANTENER ABIERTO — crear llegada, frontera o no-cierre (HAR-005).
7. EXPANDIR / REINTERPRETAR — decidir qué hace un evento cromático (HAR-006).
8. DIAGNOSTICAR (transversal) — asignar función bajo incertidumbre sin forzar etiqueta única (HAR-002/006, CAND-HAR-007/009/034/036).

No se crea una máquina de estados universal: no hay orden obligatorio entre familias. ORIENTAR suele preceder lógicamente (sin centro no hay dirección ni cierre que signifiquen nada), pero la música cíclica puede ORGANIZAR sin ORIENTAR del todo (centro múltiple/débil tolerado), y EXPANDIR puede preceder a ORIENTAR en repertorio modal.

## Integrated Decision Architecture

Formato por familia: COMPOSITIONAL QUESTION, STRUCTURAL VARIABLES, SUPPORTED / PROVISIONAL RELATIONSHIPS, DO-NOT-INFER, AVAILABLE OPERATIONS, COUNTERPRODUCTIVE CONDITIONS / TRADEOFFS, SCOPE, EVIDENCE BASIS, CROSS-DOMAIN DEPENDENCIES, CANDIDATE REFERENCES, INTEGRATION STATUS.

### D1. ORIENTAR — Establecer / interpretar orientación armónica

Carry forward de HAR-001. Vocabulario de centro preservado como términos analíticos/compositivos (ESTABLISH, CONFIRM, MAINTAIN, WEAKEN, AMBIGUATE), sin pesos numéricos, sin modelo ponderado de indicios (prohibición expresa: no resucitar ponderación).

1. COMPOSITIONAL QUESTION: dado un material, ¿qué evidencia puede contribuir a un centro tonal/modal? ¿Qué NO determina el centro por sí solo? ¿Cómo mantenerlo, debilitarlo o dejarlo ambiguo?
2. STRUCTURAL VARIABLES: colección diatónica compartida como marco; recurrencia de armonía candidata; bajo (root en bajo, pedal, repetición grave); duración de sonoridad; colocación métrica; colocación formal (inicio, retorno); confirmación cadencial posterior; competidores (centros alternativos igualmente apoyados).
3. SUPPORTED / PROVISIONAL RELATIONSHIPS:
   - Soportado (negativo): consonancia sensorial != estabilidad tonal/contextual (CAND-HAR-003); frecuencia / primer acorde / acorde final no determinan tónica por sí solos (CAND-HAR-004); duración/colocación confirman como máximo un centro ya plausible, no lo prueban (CAND-HAR-005, hipótesis).
   - Provisional (positivo débil): colección + recurrencia pueden contribuir a ESTABLISH dentro de marco declarado, con mecanismos y pesos evidenciales separados (CAND-HAR-001); centro modal sin V–I mediante pedal/drone, colección modal, repetición y fórmulas propias en tradiciones acotadas (CAND-HAR-006).
4. DO-NOT-INFER: centro desde sonoridad consonante aislada; tónica desde acorde más frecuente, inicial o final; prueba de centro desde duración o posición fuerte; equivalencia entre prominencia y función; universalidad de jerarquías probe-tone fuera de práctica común (contrapeso Butler 1989).
5. AVAILABLE OPERATIONS: enmarcar un pasaje en una colección diatónica compartida; hacer recurrir una armonía candidata dentro de ese marco; en contexto modal/pop, sostener centro con pedal/drone + repetición + fórmulas idiomáticas (con escucha obligatoria). Sin dosis, sin conteos, sin receta de distribución de indicios.
6. COUNTERPRODUCTIVE CONDITIONS / TRADEOFFS: loop con dos centros igualmente apoyados convierte ESTABLISH en AMBIGUATE; colección cromática o con préstamo activo cede a D7; pedal que engaña (pedal que no fija centro, caso documentado) bloquea cualquier versión fuerte de "bajo = centro"; imponer V–I a contexto modal retonaliza.
7. SCOPE: general-dentro-del-proyecto para las cautelas negativas; positivo modal acotado a tradiciones modales/pop-rock (TRADITION_SPECIFIC / GENRE_SPECIFIC).
8. EVIDENCE BASIS: teoría (jerarquía tonal, pedagogía), empírica externa (probe-tone como goodness-of-fit, no como atribución de centro en canciones), corpus (distribuciones, supermodo rock), repertorio (Spicer, Everett, Temperley). Sin medida dedicada de atribución de centro por oyentes en canciones (GAP).
9. CROSS-DOMAIN DEPENDENCIES: Rhythm/Meter (posición métrica y duración como refuerzo); Form (posición formal); Arrangement/Bass (bajo y densidad como marcadores; ponderación pendiente → RQ-HAR-008).
10. CANDIDATE REFERENCES: CAND-HAR-001, 002, 003, 004, 005, 006.
11. INTEGRATION STATUS: PROVISIONAL para la familia positiva; SUPPORTED para el núcleo negativo (003 y mitad negativa de 004); UNSUPPORTED para ponderación de indicios, dosis y atribución medida. CAND-HAR-002 y 005 permanecen NOT_READY (ver sección dedicada).

### D2. ORGANIZAR — Decidir organización dirigida vs. cíclica

Carry forward de HAR-002. STAY/DEPART/… no adoptado como gramática; T–PD–D–T no es gramática del proyecto; "permanecer, partir, continuar, preparar, aproximar, volver, ciclar, mantener ambiguo" son metas compositivas, no funciones oficiales.

1. COMPOSITIONAL QUESTION: una vez que existe o se insinúa un centro/región, ¿la armonía debe permanecer, partir, continuar, preparar, aproximarse, volver, ciclar o mantener ambigüedad?
2. STRUCTURAL VARIABLES: rol contextual asignado (no etiqueta); root motion; movimiento del bajo; conducción de voces; tendency tones; esquema/convención de repertorio; organización global (progresión orientada vs. loop recurrente); posición formal.
3. SUPPORTED / PROVISIONAL RELATIONSHIPS:
   - La función depende del contexto, no de la etiqueta (CAND-HAR-007, insuficiencia, no determinación total).
   - V→I es relación dirigida fuerte en tradiciones acotadas (práctica común clásica), no requisito universal (CAND-HAR-008, mitad positiva dependiente de pedagogía PARCIAL, mitad negativa en contraevidencia VERIFIED).
   - Root motion solo no determina función (CAND-HAR-009, insuficiencia, no irrelevancia).
   - Frecuencia estadística != expectativa/función/calidad (CAND-HAR-010).
   - Loops pop/rock coherentes sin sintaxis dirigida clásica; dirección local posible dentro del ciclo (CAND-HAR-011).
   - Indicios de dominante distribuidos (leading tone, fundamental/bajo, posición, esquema); dominante != tensión (CAND-HAR-012, sin pesos ni sustituibilidad).
4. DO-NOT-INFER: función desde numeral romano; dirección desde root motion aislado; expectativa de oyente desde corpus o intuición; tensión desde etiqueta de dominante; necesidad universal de sintaxis funcional; irrelevancia del root motion o de V–I en su tradición.
5. AVAILABLE OPERATIONS: asignar rol por contexto con convergencia de indicios (bajo, conducción, esquema, posición); usar V–I como llegada fuerte solo en tradición que lo sostiene; sostener sección sobre loop de 2–4 sonoridades sin imponer sintaxis dirigida; leer dominante por matriz de indicios, nunca por etiqueta sola. Todas con escucha y alcance declarado; `possible_action` vacío en 008/011 (sin técnica positiva establecida más allá de disponibilidad idiomática).
6. COUNTERPRODUCTIVE CONDITIONS / TRADEOFFS: exigir función dirigida en cada frase pop (juzga loops como defectuosos); importar sintaxis clásica (secuencias, aplicadas) al pop sin verificar; leer cada acorde cromático del loop como dominante secundaria (modulaciones ficticias en cadena, ver D7).
7. SCOPE: marcos funcionales acotados (TRADITION_SPECIFIC) para T–PD–D, V–I y predominante; loops como GENRE OBSERVATION pop/rock; cautelas negativas generales-dentro-del-proyecto.
8. EVIDENCE BASIS: teoría y pedagogía (alcance declarado, parte PARCIAL sin texto), repertorio (Spicer VERIFIED: soul-dominant sin leading tone clásico, V perpetuo sin resolución), corpus vía reseña (Doll: pre-tónica, esquemas, ambigüedad), empírica pendiente (priming armónico, aprendizaje estadístico, curva corpus→expectativa: GAP).
9. CROSS-DOMAIN DEPENDENCIES: Melody y Bass (pueden confirmar o contradecir la dirección de los roots); Form (la dirección opera distinto a nivel de frase y de sección); futura RQ-HAR-009 para divorce melodía-armonía.
10. CANDIDATE REFERENCES: CAND-HAR-007, 008, 009, 010, 011, 012.
11. INTEGRATION STATUS: PROVISIONAL (008 y 011 con alcance de tradición/género explícito: TRADITION_SPECIFIC y GENRE_SPECIFIC respectivamente).

Cuándo ayuda el marco funcional acotado y dónde falla: ayuda a decidir permanencia/partida/llegada/retorno dentro de práctica común clásica y repertorio pop con sintaxis pre-tónica documentada; falla como gramática universal ante loops, tónicas frágiles/ausentes, centros modales sin V–I, soul-dominant sin leading tone y organización por shuttle/planing. Los loops son contraevidencia estructural, no armonía defectuosa.

### D3. CONECTAR — Conectar sonoridades sucesivas

Carry forward de HAR-003. "Buena conducción" NO es movimiento mínimo; restricciones clásicas de paralelas NO son leyes universales; same pitch != same pitch class != same register != same voice identity (CAND-HAR-019 preservado como NOT_READY, distinción analítica sin inferencia perceptiva).

1. COMPOSITIONAL QUESTION: entre una sonoridad y la siguiente, ¿qué alturas/voces deben permanecer, cuáles moverse, cuánto, en qué registro, con qué identidades de voz, y cuándo conviene movimiento pequeño frente a desplazamiento deliberado o paralelo?
2. STRUCTURAL VARIABLES: retención de tono común (altura literal); tamaño de movimiento (grado/semitono/salto); dirección relativa (contrario/oblicuo/paralelo); registro y duplicación; identidad de voz (estable vs. reasignada); tendency tones; etiqueta/root/bajo/inversión/realización (cinco niveles separados, CAND-HAR-016).
3. SUPPORTED / PROVISIONAL RELATIONSHIPS:
   - Retención de tono común y movimiento pequeño como herramientas de continuidad dependientes de contexto, sin mecanismo común demostrado ni dosis-respuesta (CAND-HAR-013, heurística débil con escucha obligatoria).
   - Distancia mínima NO es objetivo universal (CAND-HAR-014, anti-regla débil: eficiencia != preferencia != calidad).
   - Resolución de tendency tones acotada a tradición (^7, séptima, suspensión, alterados por fila separada; ningún "must resolve" fuera de norma acotada) (CAND-HAR-015).
   - Etiqueta/root/bajo no determinan el movimiento de las voces (CAND-HAR-016, insuficiencia en cinco niveles).
   - Restricciones al movimiento paralelo como normas acotadas de tradición/pedagogía, no perceptivas (CAND-HAR-017, claim A).
   - Continuidad de conducción y función armónica no-equivalentes con insuficiencia mutua, no independientes (CAND-HAR-018).
   - Planing como procedimiento organizador en repertorios acotados (CAND-HAR-020, invariantes solo por caso).
   - Distinción quíntuple pitch/pitch class/identidad/registro/octava como herramienta analítica sin puente perceptivo (CAND-HAR-019, NOT_READY).
4. DO-NOT-INFER: calidad desde economía de movimiento; obligatoriedad perceptiva de resoluciones clásicas fuera de práctica común; movimiento de voces desde etiqueta/root/bajo; independencia entre conducción y función (exceso de fuerza retirado); equivalencia de octavas; universalidad de prohibiciones de paralelas.
5. AVAILABLE OPERATIONS: conservar alguna altura literal o proximidad registral y mover el resto por grado (verificación por escucha); desplazamiento deliberado (saltos, cambio registral) como articulación del cambio; planing en repertorio que lo sostiene; en tradición clásica acotada, resolver tendency tones según norma declarada. Sin dosis, sin optimización global de distancia.
6. COUNTERPRODUCTIVE CONDITIONS / TRADEOFFS: retener por defecto donde la intención es diferenciar (llegada marcada, contraste seccional); suavizar donde se necesita articulación; planing donde la tradición exige independencia de voces; movimiento contrario/oblicuo como norma sin evidencia de independencia percibida.
7. SCOPE: cautelas negativas generales-dentro-del-proyecto; positivas acotadas (015 y 017: TRADITION_SPECIFIC clásica; 020: GENRE_SPECIFIC por repertorio).
8. EVIDENCE BASIS: repertorio (Spicer VERIFIED: pedal que fija vs. pedal que engaña, giros modales), pedagogía clásica (PARCIAL), marcos genéricos (Bregman proximidad sin medida en sucesiones armónicas; Tymoczko/Huron 2001 como deuda UNVERIFIED). Medida dedicada de continuidad por tonos comunes/tamaño de movimiento: GAP.
9. CROSS-DOMAIN DEPENDENCIES: Melody (voz superior; futura RQ-HAR-009); Timbre/Arrangement (registro/timbre condicionan independencia); Bass (lógica propia del bajo → RQ-HAR-008); identidad de voz en texturas sin voces estables (GAP formal).
10. CANDIDATE REFERENCES: CAND-HAR-013, 014, 015, 016, 017, 018, 019, 020.
11. INTEGRATION STATUS: PROVISIONAL para la familia (heurísticas débiles con escucha); TRADITION_SPECIFIC para 015/017; GENRE_SPECIFIC para 020; UNSUPPORTED para 019 como guía de decisión (solo diagnóstico analítico).

### D4. TEMPORIZAR — Decidir cuándo cambia la armonía

Carry forward de HAR-004 (mitad ritmo). Seis variables permanentemente separadas: TEMPO, HARMONIC-CHANGE RATE, CHORD/EVENT DURATION, PATTERN OF CHANGES, METRIC PLACEMENT, STRUCTURAL HARMONIC CHANGE. Prohibido inferir: más cambios = más desarrollo; ritmo armónico más rápido = más energía/tensión; acorde más largo = mayor importancia. Sin valores numéricos por defecto.

1. COMPOSITIONAL QUESTION: ¿cómo decide el compositor cuándo cambiar de armonía, cuánto mantener cada sonoridad, cuándo acelerar/desacelerar la actividad armónica y dónde colocar los cambios?
2. STRUCTURAL VARIABLES: las seis variables separadas arriba; relación con frase y forma; textura/arreglo concurrente.
3. SUPPORTED / PROVISIONAL RELATIONSHIPS:
   - Ritmo armónico especificado con independencia del tempo (CAND-HAR-021, heurística metodológica).
   - Duración del acorde != importancia estructural/estabilidad/tónica (CAND-HAR-022, negativa).
   - Aceleración armónica como dispositivo de tradición acotada (sentence clásica: fragmentación + liquidación + aceleración hacia cadencia, Caplin VERIFIED); fuera de ella, sin realidad analítica o perceptiva establecida; aceleración local dentro de loops `uncertain` (CAND-HAR-023, THEORY acotada + heurística negativa).
4. DO-NOT-INFER: energía/tensión/desarrollo desde tasa de cambio; importancia desde duración; transferencia de la aceleración capliniana al pop/loop; confusión entre ritmo armónico y actividad rítmica de superficie o densidad del arreglo.
5. AVAILABLE OPERATIONS: especificar cambios por compás/posición métrica con tempo declarado aparte; variar duración sin reclamar importancia; en marco clásico declarado, acelerar hacia cadencia con fragmentación coordinada. Ninguna dosis ni curva tasa→energía.
6. COUNTERPRODUCTIVE CONDITIONS / TRADEOFFS: acelerar donde la forma pide estasis (vamps, grooves); alargar esperando importancia estructural; densificar el arreglo esperando que cuente como cambio armónico para el oyente (onset percibido: dependencia Arrangement sin resolver).
7. SCOPE: cautelas negativas generales-dentro-del-proyecto; aceleración positiva TRADITION_SPECIFIC (sentence clásica).
8. EVIDENCE BASIS: teoría (Caplin VERIFIED para sentence), bloqueos Melody (density != tempo, groove != frase), repertorio (Spicer: vamps, pedales). Corpus pop/rock de ritmo armónico con metodología declarada: GAP (SRC-ACADEMIC-040 como puntero). Medida de ritmo relativo vs. absoluto que prediga juicios: GAP.
9. CROSS-DOMAIN DEPENDENCIES: Rhythm/Meter (colocación métrica); Form (función seccional); Arrangement (en loop-based el cambio formal viene de capas, no del ritmo armónico).
10. CANDIDATE REFERENCES: CAND-HAR-021, 022, 023.
11. INTEGRATION STATUS: PROVISIONAL (021/022 como higiene metodológica operativa; 023 TRADITION_SPECIFIC en su mitad positiva, PROVISIONAL-negativa fuera).

### D5. PERSISTIR — Decidir qué persiste mientras la superficie cambia

Carry forward de HAR-004 (mitad región). Convención metodológica obligatoria: toda afirmación material "X prolonga Y" debe declarar FRAMEWORK, OBJECT, CRITERION, SCOPE, EVIDENCE TYPE. `prolongation` no es comando primitivo de composición.

1. COMPOSITIONAL QUESTION: ¿cómo sostiene el compositor una región/función mientras la superficie cambia (paso, bordadura, pedal, sustitución, inversión, repetición cíclica)?
2. STRUCTURAL VARIABLES: evento de superficie (clase: paso/bordadura/pedal/embellecimiento/sustitución); región de referencia declarada; función bajo marco declarado; criterio de subordinación; alcance; tipo de evidencia.
3. SUPPORTED / PROVISIONAL RELATIONSHIPS:
   - Cambios de superficie dentro de región persistente como heurística débil con cautela de marco (CAND-HAR-024).
   - Prolongación como interpretación dependiente de marco, no hecho bruto; marcos en disputa comparados (CAND-HAR-025, cautela metodológica).
   - Organización por loop/vamp/pedal con estasis armónica y cambio en otros dominios (CAND-HAR-026, observación de género + heurística cross-domain, vocabulario neutral cyclic persistence).
4. DO-NOT-INFER: subordinación estructural desde vocabulario (paso/bordadura como palabra mágica); jerarquía interna de loops sin criterio declarado; equivalencia entre persistencia cíclica y prolongación schenkeriana (pregunta abierta al Director, no conclusión); importancia desde estatismo.
5. AVAILABLE OPERATIONS (solo diagnósticas/condicionales, ninguna aprobada como técnica positiva general): retener bajo con armonía superior móvil; repetir unidad armónica recurrente; insertar conexión de superficie con resolución verificada a la misma región; retener función bajo marco declarado; mantener colección/centro mientras otra variable cambia. Usar solo con las cinco ranuras declaradas.
6. COUNTERPRODUCTIVE CONDITIONS / TRADEOFFS: subordinar lo más saliente por etiqueta ("embellecimiento" != evento poco importante); analizar superficie pop con criterios de práctica común (quién decide qué es "paso" en un loop: abierto); ignorar acordes reales bajo la palabra "prolongación".
7. SCOPE: marcos acotados por tradición (TRADITION_SPECIFIC para criterios schenkerianos/clásicos); persistencia cíclica GENRE_SPECIFIC (loop-based) + CROSS_DOMAIN_REQUIRED.
8. EVIDENCE BASIS: teoría en disputa (Schenker, GTTM, TPS como solo-marco sin texto completo), pedagogía de embellecimiento (UNVERIFIED), repertorio (Spicer bidireccional VERIFIED), descriptivo loop (Butler/Middleton vía Melody). Criterios de subordinación fuera de práctica común, decaimiento temporal de persistencia, y rol del bajo/batería en qué cuenta como cambio: GAPs.
9. CROSS-DOMAIN DEPENDENCIES: Arrangement/Production (decide qué cuenta como cambio y sostiene interés en estasis); Form (escala de la región); Bass (pedal y movimiento grave → RQ-HAR-008).
10. CANDIDATE REFERENCES: CAND-HAR-024, 025, 026.
11. INTEGRATION STATUS: PROVISIONAL como cautela metodológica y heurística débil (024/025); GENRE_SPECIFIC + CROSS_DOMAIN_REQUIRED (026).

### D6. LLEGAR / MANTENER ABIERTO — Crear llegada, frontera o no-cierre

Carry forward de HAR-005. Constructos permanentemente distintos: CADENCE, ARRIVAL, CLOSURE, RESOLUTION, COMPLETION, RETURN, STOP, BOUNDARY, FINAL EVENT. La armonía puede contribuir al cierre sin ser detector necesario ni suficiente universal. Sin modelo fijo de indicios de cierre. Vocabulario neutral de loop/frontera preservado (RETURN, RECURRENCE, STOP, BOUNDARY, LOOP SEAM, FINAL EVENT) cuando no hay proceso cadencial declarado.

1. COMPOSITIONAL QUESTION: ¿cómo contribuye armónicamente el compositor a una llegada, cierre, suspensión, apertura o retorno, y qué alternativas existen cuando la música no se organiza con cadencias funcionales clásicas?
2. STRUCTURAL VARIABLES: proceso cadencial (stages, posición formal, sintaxis declarada); llegada tónica (configuración: soprano, metro, duración, silencio, posición); categoría cadencial + rasgos retóricos + formación del oyente; fórmula de llegada por tradición (auténtica, plagales/modales, retorno de loop, tónica final, final no-tónico); escala formal (frase vs. sección vs. canción).
3. SUPPORTED / PROVISIONAL RELATIONSHIPS:
   - Cadencia como proceso contextual con posición formal, no lookup de dos acordes (CAND-HAR-027, THEORY acotada + heurística negativa).
   - Llegada tónica != cierre; la armonía contribuye sin suficiencia contextual ni necesidad universal demostradas (CAND-HAR-028, heurística negativa con wording corregido).
   - Jerarquía analítica de fuerza (PAC>IAC>HC) != ranking perceptivo general; dependencia de formación y rasgos retóricos (CAND-HAR-029, HYPOTHESIS clásica, `possible_action` vacío).
   - Llegadas plagales/modales como fórmulas de repertorio acotado, no cadencia plagal universal (CAND-HAR-030).
   - Retorno de loop != cadencia; frontera por parada/arreglo; costura recurrente-vs-terminal como OPEN QUESTION (CAND-HAR-031).
   - Tónica final sin cadencia y finales no-tónicos como estados documentados acotados; tónica final no garantiza cierre (CAND-HAR-032, existencia, no licencia general).
4. DO-NOT-INFER: cadencia desde dos últimos acordes; cierre desde llegada tónica; fuerza percibida desde categoría analítica; cierre terminal desde parada no marcada; prueba de centro desde acorde final (CAND-HAR-004); universalidad de tipologías clásicas (auténtica/rota/evadida) en pop; defecto armónico en loops sin cadencia.
5. AVAILABLE OPERATIONS: diseñar llegada y cierre por separado y verificar por escucha; en rock/pop-modal, considerar IV–I seccional, bVII–I o bVI–bVII–i como fórmulas idiomáticas sin promesa de cierre percibido; en marcos cíclicos, marcar la iteración final (parada, cambio de arreglo/densidad, repetición enfática) en vez de insertar V–I; terminar en tónica sosteniéndola (duración/repetición/pedal) con apoyo de otras dimensiones o aceptando cierre parcial; declarar finales no-tónicos como continuación seccional, marco modal/loop o decisión de producción.
6. COUNTERPRODUCTIVE CONDITIONS / TRADEOFFS: insertar V–I para "cerrar" un loop modal (retonaliza); presentar IV–I clásico aislado como cierre temático (es postcadencial); dejar la última repetición idéntica esperando cierre terminal; llamar cadencia a la parada (contamina decisiones futuras); prometer cierre pleno desde final no-tónico en repertorio cadencial.
7. SCOPE: fórmulas por tradición (TRADITION_SPECIFIC clásica; GENRE_SPECIFIC rock/pop-modal/loop); multidimensionalidad del cierre general-dentro-del-proyecto como cautela.
8. EVIDENCE BASIS: empírica parcial (Sears: regresión por voces, split músicos/no-músicos, textos completos pendientes; Smit 2020 solo como límite emoción != cierre), corpus parcial (Temperley RS200: 59%/32%/18.5%, 41% sin sectional cadence), teoría de segundo nivel (Caplin 2024 vía reseña), pedagogía modal (OMT). Efecto perceptivo de fade-out, parada-vs-corte, y prolongational closure: GAPs.
9. CROSS-DOMAIN DEPENDENCIES: Melody (cierre melódico + armónico como unidad futura; finales cambiados dependen del marco armónico); Rhythm/Meter (posición métrica, alargamiento, silencio); Form (frase vs. sección); Lyrics/Prosody (co-determina cierre en canción); Arrangement/Production (marca fronteras cíclicas).
10. CANDIDATE REFERENCES: CAND-HAR-027, 028, 029, 030, 031, 032.
11. INTEGRATION STATUS: PROVISIONAL para la familia (heurísticas débiles con escucha obligatoria); TRADITION_SPECIFIC (027/029 mitad clásica) y GENRE_SPECIFIC (030/031) por fórmula; CROSS_DOMAIN_REQUIRED para cualquier pretensión de cierre (028/032).

### D7. EXPANDIR / REINTERPRETAR — Decidir qué hace un evento cromático

Carry forward de HAR-006. Sin variable `chromaticism_amount` con efectos automáticos; sin mapeo emocional. Distinciones preservadas: CENTER != COLLECTION; TONICIZATION != MODULATION; CHROMATICISM != TENSION. Las siete lecturas (local targeting, mezcla, conducción cromática, tono común, predominante alterada, loop membership, ambigüedad/preparación de cambio) son preguntas de trabajo, no taxonomía oficial exhaustiva.

1. COMPOSITIONAL QUESTION: cuando aparece una nota o sonoridad fuera de la colección vigente, ¿enfatiza temporalmente otro grado, mezcla material modal, conecta voces, cambia de colección, crea color, pertenece a un loop, admite varias lecturas o prepara un cambio de centro?
2. STRUCTURAL VARIABLES: aplicado V(7)/x o viio(7)/x con resolución verificada; confirmación cadencial posterior y permanencia; colección de referencia y centro declarados; marco de tradición; conducción (paso/bordadura/línea, tono común); recurrencia métrica/textural; ortografía vs. función (disociación enarmónica).
3. SUPPORTED / PROVISIONAL RELATIONSHIPS:
   - Tonicalización vs. modulación como diagnósticos contextuales de marco acotado (práctica común), sin umbral numérico; fuera del marco, corte `uncertain`, frontera RQ-HAR-007 (CAND-HAR-033).
   - Etiqueta de dominante secundaria != tonicalización percibida (CAND-HAR-034, puramente negativa).
   - Mezcla modal altera colección sin cambiar centro necesariamente; fuente decidida por marco + colección + centro, nunca por sonoridad aislada (CAND-HAR-035, núcleo CENTER/COLLECTION unificado, evidencia por tradición).
   - Evento cromático admite múltiples análisis; función desde contexto convergente; ambigüedad analítica != confusión del oyente (CAND-HAR-036, puramente negativa).
   - Cromatismo de conducción/tono común (CTo7/CT+6) interpretable dentro de región persistente bajo marco declarado, sin partida estructural implicada (CAND-HAR-037, heurística débil).
   - Cromatismo NO es proxy de tensión/inestabilidad/complejidad/emoción (CAND-HAR-038, cautela metodológica acotada).
   - Acordes cromáticos recurrentes como organización estable de loop en dimensión cíclica explícita, sin sintaxis funcional clásica (CAND-HAR-039, `possible_action` vacío).
4. DO-NOT-INFER: modulación desde alteraciones sin cadencia ni permanencia; centro local desde etiqueta V/x; fuente modal desde sonoridad aislada (todo bVII = mixolidio, todo bVI = menor); tensión desde cromatismo; audición diatónica desde repetición (normalización no medida); etiqueta única cuando la evidencia admite varias; umbrales N-acordes/N-compases.
5. AVAILABLE OPERATIONS: en marco clásico declarado, préstamos documentados (predominantes con le, bVI/bIII/bVII, I→i) y paso/bordadura cromática o CTo7/CT+6 con resolución verificada a la misma región; en pop/rock-modal, schemas idiomáticos (mixolidio/eolio/dórico/lidio) con su alcance; en loops cromáticos, sostener el ciclo sin funcionalizar cada miembro. Todo con fuente declarada, sin promesa de afecto/tensión y con escucha obligatoria. Etiquetado V/x solo como hipótesis de énfasis local.
6. COUNTERPRODUCTIVE CONDITIONS / TRADEOFFS: exigir V–I en contexto modal (retonaliza); funcionalizar cada cromatismo del loop (modulaciones ficticias); leer ortografía enarmónica como modulación percibida; usar "prolongación" para ignorar acordes; importar corte cadencial clásico al pop/loop; sobrediagnosticar modos raros.
7. SCOPE: TRADITION_SPECIFIC (033 clásico; 035 mitad clásica) y GENRE_SPECIFIC (035 mitad pop-modal; 039 pop/rock); cautelas negativas (034/036/038) generales-dentro-del-proyecto.
8. EVIDENCE BASIS: pedagogía a texto completo (OMT VERIFIED), repertorio (Spicer VERIFIED), corpus PARTIAL (distribuciones cromáticas rock), revisión de tensión PARTIAL + TPS solo-marco (038 acotada). Sin medida de atribución de centro local tras V/x, de discriminación entre lecturas por oyentes, de normalización perceptiva en loops, ni de manipulación cromática→tensión aislada (GAPs).
9. CROSS-DOMAIN DEPENDENCIES: Melody (cromatismo melódico ↔ armónico → RQ-HAR-009); Bass/inversión/voicing (interpretación cromática → RQ-HAR-008); Timbre/Arrangement (color desde voicing/timbre tanto como desde clase de acorde).
10. CANDIDATE REFERENCES: CAND-HAR-033, 034, 035, 036, 037, 038, 039.
11. INTEGRATION STATUS: TRADITION_SPECIFIC / GENRE_SPECIFIC para mitades positivas con alcance (033/035/039); PROVISIONAL para heurísticas débiles y cautelas (034/036/037/038).

### D8. DIAGNOSTICAR (transversal)

Capacidad, no fase: ante un evento (aplicado, préstamo, tono común, predominante alterada, llegada, loop), asignar función desde matriz de interpretaciones con centro implicado y conducción implicada por lectura, preguntas diagnósticas no-normativas y convención de cinco ranuras para lecturas prolongacionales. Forzar etiqueta única con evidencia compatible múltiple es error de método. Sin clasificador determinista, sin pesos, sin `possible_action` positivo (CAND-HAR-036). Status: PROVISIONAL como higiene + DIAGNOSTIC ONLY en acción (ver Actionability Audit). Candidatos: 007, 009, 034, 036 (+ 025 para lecturas prolongacionales).

## Integrated Anti-Rules

Solo conclusiones apoyadas por la investigación (con candidato entre paréntesis). Formulación negativa deliberada: es el conocimiento más sólido del sistema.

1. La consonancia no equivale a estabilidad tonal; la disonancia sensorial no equivale a inestabilidad funcional. (003, SUPPORTED)
2. La frecuencia, el primer acorde y el acorde final no determinan la tónica por sí solos. (004)
3. La duración y la colocación métrica/formal confirman como máximo un centro ya plausible; no lo prueban. (005, hipótesis)
4. Ningún V–I es necesario para todo centro; el centro modal sin dominante es documentado. (006)
5. La etiqueta del acorde no determina su función; el root motion solo no determina función; la etiqueta V/x no certifica tonicalización percibida. (007, 009, 034)
6. V→I no es requisito universal; la dominante no es tensión. (008, 012)
7. La distancia mínima de conducción no es objetivo universal; eficiencia != preferencia != calidad. (014)
8. Las resoluciones de tendency tones son normas de tradición acotada, no leyes perceptivas. (015)
9. Las prohibiciones de movimiento paralelo son normas pedagógicas acotadas; el planing es procedimiento organizador en su repertorio. (017, 020)
10. Continuidad de conducción != función armónica (insuficiencia mutua, no independencia). (018)
11. Misma pitch class en otra octava no es el mismo evento registral/identitario. (019, analítico)
12. El tempo no es ritmo armónico; la duración no es importancia; la aceleración hacia cadencia es dispositivo clásico acotado, no ley de energía. (021, 022, 023)
13. "Prolongación" sin marco declarado no subordina nada; la persistencia cíclica no es prolongación schenkeriana demostrada. (025)
14. La cadencia no son los dos últimos acordes; la llegada tónica no es cierre; la jerarquía analítica no es ranking perceptivo. (027, 028, 029)
15. El retorno de loop no es cadencia; la parada no crea cierre armónico por sí sola; la tónica final no garantiza cierre. (031, 032)
16. Tonicalización != modulación; mezcla != modulación; centro != colección; cromatismo != tensión. (033, 035, 038)
17. Ningún préstamo declara su fuente por sí solo; ningún evento cromático admite una sola lectura oficial. (035, 036)
18. Más cambios no es más desarrollo; ritmo armónico más rápido no es más energía; acorde más largo no es más importante. (D4, desde 021/022/023)
19. Lo frecuente en corpus no es lo esperado por oyentes ni lo bueno compositivamente. (010)

## Candidate Coverage Matrix

Lectura de columnas: ID | significado integrado en una línea | readiness heredado (no modificado) | integration status (esta integración) | problema principal | scope | limitación/bloqueador principal.

| ID | Significado integrado | Readiness | Integ. status | Problema | Scope | Limitación / bloqueador |
|---|---|---|---|---|---|---|
| CAND-HAR-001 | Colección + recurrencia pueden contribuir a ESTABLISH, por separado y sin suficiencia | POSSIBLE_WITH_SCOPE | PROVISIONAL | D1 ORIENTAR | General-proyecto (débil); más débil en rock | Sin `possible_action`; sin ponderación/dosis/medida en canciones |
| CAND-HAR-002 | Bajo tónico/pedal/root-en-bajo como contribución al centro | NOT_READY | UNSUPPORTED | D1 ORIENTAR | Sin alcance afirmable | Root/bajo/pedal separados sin peso; pedal insuficiente solo; sin medida dedicada; requiere RQ-HAR-008 |
| CAND-HAR-003 | Consonancia != estabilidad (tres constructos separados; heurística negativa) | STRONG_CANDIDATE | SUPPORTED (negativo) | D1 (transversal) | General-proyecto | Solo cautela metodológica; ningún puente positivo; marcos GTTM/Parncutt/TPS solo-marco |
| CAND-HAR-004 | Frecuencia/primero/final no determinan tónica; ambigüedad documentada en loops | POSSIBLE_WITH_SCOPE | PROVISIONAL | D1 ORIENTAR | Pop/rock preservado | Sin `possible_action`; Doll vía reseña; Capuzzo solo-marco; sin medida en oyentes |
| CAND-HAR-005 | Duración + colocación métrica/formal como confirmación, no prueba | NOT_READY | UNSUPPORTED | D1 ORIENTAR | Sin alcance afirmable | Tres indicios sin fusionar; primario métrico no inspeccionado; Caplin sin transferencia pop; requiere RQ-HAR-008/forma |
| CAND-HAR-006 | Centro modal sin V–I (indicios separados, heurística estructural con repertorio) | STRONG_CANDIDATE | TRADITION_SPECIFIC | D1 ORIENTAR | Modal/pop/rock acotado | Sin efectos perceptivos medidos; cuantificación pendiente |
| CAND-HAR-007 | Función desde contexto, no desde etiqueta (insuficiencia, no determinación total) | POSSIBLE_WITH_SCOPE | PROVISIONAL | D2 ORGANIZAR + D8 | General-proyecto (negativo) | Sin ponderación perceptiva entre indicios; `predominant` en disputa |
| CAND-HAR-008 | V→I dirigido fuerte en tradiciones acotadas, no universal | POSSIBLE_WITH_SCOPE | TRADITION_SPECIFIC | D2 ORGANIZAR | Práctica común clásica (+ pre-tónica pop documentada) | Mitad positiva depende de pedagogía PARCIAL; `possible_action` vacío; criterios V-no-dominante sin formalizar |
| CAND-HAR-009 | Root motion insuficiente para función (no irrelevante) | POSSIBLE_WITH_SCOPE | PROVISIONAL | D2 ORGANIZAR + D8 | General-proyecto (negativo) | Distribuciones PARCIAL; ponderación con bajo/conducción sin medir |
| CAND-HAR-010 | Frecuencia estadística != expectativa/función/calidad | POSSIBLE_WITH_SCOPE | PROVISIONAL | D2 ORGANIZAR | General-proyecto (negativo) | Aprendizaje estadístico como GAP; curva corpus→expectativa sin medir |
| CAND-HAR-011 | Loops coherentes sin sintaxis dirigida clásica (dirección local posible) | POSSIBLE_WITH_SCOPE | GENRE_SPECIFIC | D2 ORGANIZAR | Pop/rock cíclico | Lenguaje estructural sin test de oyentes; función interna abierta; `possible_action` vacío |
| CAND-HAR-012 | Dominante distribuida por indicios; dominante != tensión | POSSIBLE_WITH_SCOPE | PROVISIONAL | D2 ORGANIZAR | General-proyecto (negativo + matriz sin pesos) | Sin pesos ni sustituibilidad; sin modelo oficial; procedencia por indicio |
| CAND-HAR-013 | Tono común + movimiento pequeño como continuidad contextual (mecanismos separados) | POSSIBLE_WITH_SCOPE | PROVISIONAL | D3 CONECTAR | Transversal (qué cuenta como conexión depende de tradición) | Heurística débil; sin dosis-respuesta; sin medida dedicada; escucha obligatoria |
| CAND-HAR-014 | Distancia mínima no es objetivo universal | POSSIBLE_WITH_SCOPE | PROVISIONAL (negativo) | D3 CONECTAR | General-proyecto (negativo) | Tymoczko solo deuda; eficiencia/preferencia/calidad sin relación medida |
| CAND-HAR-015 | Resolución de tendency tones acotada a tradición (filas separadas) | POSSIBLE_WITH_SCOPE | TRADITION_SPECIFIC | D3 CONECTAR | Práctica común clásica | Sin lenguaje perceptivo; `possible_action` vacío; expectativa medida pendiente |
| CAND-HAR-016 | Etiqueta/root/bajo no determinan movimiento de voces (cinco niveles) | POSSIBLE_WITH_SCOPE | PROVISIONAL | D3 CONECTAR | General-proyecto (negativo) | Irrelevancia no inferida; compatibilidad con HAR-002 asumida, no medida |
| CAND-HAR-017 | Restricciones de paralelas como normas acotadas (claim A) | POSSIBLE_WITH_SCOPE | TRADITION_SPECIFIC | D3 CONECTAR | Pedagogía clásica | Mitad planing separada a 020; sin base perceptiva |
| CAND-HAR-018 | Continuidad != función (no-equivalencia e insuficiencia mutua) | POSSIBLE_WITH_SCOPE | PROVISIONAL | D3 CONECTAR | General-proyecto | "Parcialmente independientes" retirado por exceso de fuerza; límite con 012 |
| CAND-HAR-019 | Distinción quíntuple pitch/clase/identidad/registro/octava (analítica) | NOT_READY | UNSUPPORTED | D3 CONECTAR | Sin alcance decisional | Sin `possible_action`; inferencias perceptivas prohibidas; requiere RQ-HAR-008 + evidencia perceptiva |
| CAND-HAR-020 | Planing como organización en repertorios acotados | POSSIBLE_WITH_SCOPE | GENRE_SPECIFIC | D3 CONECTAR | Repertorios con planing documentado | Invariantes solo por caso; sin efecto afirmado; `possible_action` vacío |
| CAND-HAR-021 | Ritmo armónico independiente del tempo (seis variables separadas) | POSSIBLE_WITH_SCOPE | PROVISIONAL | D4 TEMPORIZAR | General-proyecto (metodológico) | Medida relativa-vs-absoluta que prediga juicios: GAP |
| CAND-HAR-022 | Duración != importancia estructural | POSSIBLE_WITH_SCOPE | PROVISIONAL (negativo) | D4 TEMPORIZAR | General-proyecto (negativo) | Hereda debilidad de 005; rol bajo/arreglo pendiente |
| CAND-HAR-023 | Aceleración acotada a sentence clásica; fuera, sin ley | POSSIBLE_WITH_SCOPE | TRADITION_SPECIFIC | D4 TEMPORIZAR | Sentence clásica (positivo); resto negativo | Aceleración local en loops `uncertain`; desaceleración sin teoría |
| CAND-HAR-024 | Superficie cambiante dentro de región persistente (heurística débil + cautela) | POSSIBLE_WITH_SCOPE | PROVISIONAL | D5 PERSISTIR | Marcos declarados | Aldwell & Schachter UNVERIFIED; criterios fuera de práctica común abiertos |
| CAND-HAR-025 | Prolongación dependiente de marco, no hecho bruto | POSSIBLE_WITH_SCOPE | PROVISIONAL | D5 PERSISTIR | Transversal metodológico | Soporte de segundo orden (comparación de alcances); ningún claim positivo |
| CAND-HAR-026 | Loop/vamp/pedal con estasis y cambio en otros dominios | POSSIBLE_WITH_SCOPE | GENRE_SPECIFIC + CROSS_DOMAIN_REQUIRED | D5 PERSISTIR | Loop-based | Jerarquía interna abierta; persistencia cíclica vs. prolongación sin resolver |
| CAND-HAR-027 | Cadencia como proceso contextual, no lookup de dos acordes | POSSIBLE_WITH_SCOPE | TRADITION_SPECIFIC | D6 LLEGAR/ABRIR | Clásica (positivo); negativo general | Stages Caplin 2024 en segundo nivel; transferencia fuera sin verificar |
| CAND-HAR-028 | Llegada tónica != cierre; armonía contribuidor parcial | POSSIBLE_WITH_SCOPE | PROVISIONAL + CROSS_DOMAIN_REQUIRED | D6 LLEGAR/ABRIR | General-proyecto (negativo + heurística débil) | Sin diseño que aísle dominios; sin medida fuera de Mozart/teclado |
| CAND-HAR-029 | Jerarquía analítica != ranking perceptivo (depende de formación/retórica) | POSSIBLE_WITH_SCOPE | TRADITION_SPECIFIC | D6 LLEGAR/ABRIR | Clásica + tarea 1–7 Mozart/teclado | `possible_action` vacío; texto Sears pendiente; betas/p/R² prohibidos como pesos |
| CAND-HAR-030 | Llegadas plagales/modales como fórmulas de repertorio acotado | POSSIBLE_WITH_SCOPE | GENRE_SPECIFIC (por fórmula y tradición) | D6 LLEGAR/ABRIR | Clásica postcadencial / rock seccional / pop modal | Sin medida de cierre para estas fórmulas; textos parciales pendientes |
| CAND-HAR-031 | Retorno de loop != cadencia; frontera por parada/arreglo | POSSIBLE_WITH_SCOPE | GENRE_SPECIFIC | D6 LLEGAR/ABRIR | Pop/rock/loop-based | Terminal-vs-corte sin medida; costura como OPEN QUESTION |
| CAND-HAR-032 | Tónica final sin cadencia y finales no-tónicos como estados acotados | POSSIBLE_WITH_SCOPE | PROVISIONAL + CROSS_DOMAIN_REQUIRED | D6 LLEGAR/ABRIR | Rock/pop/modal/loop | Sin medida de cierre para estos estados; heurística negativa sólida, positiva débil |
| CAND-HAR-033 | Tonicalización vs. modulación como diagnósticos de marco, sin umbral | POSSIBLE_WITH_SCOPE | TRADITION_SPECIFIC | D7 EXPANDIR | Práctica común clásica | Sin medida de centro local; puente positivo pendiente; frontera a RQ-HAR-007 |
| CAND-HAR-034 | Etiqueta V/x != tonicalización percibida | POSSIBLE_WITH_SCOPE | PROVISIONAL (negativo) | D7 EXPANDIR + D8 | Clásica (lectura); negativo general | Sin medida de atribución local tras V/x; `possible_action` vacío |
| CAND-HAR-035 | Mezcla altera colección sin cambiar centro; fuente por marco | POSSIBLE_WITH_SCOPE | TRADITION_SPECIFIC / GENRE_SPECIFIC | D7 EXPANDIR | Clásica + pop-modal (evidencia por tradición) | Función-preservada como reclamación de marco; audición de fuente sin medida |
| CAND-HAR-036 | Evento cromático admite múltiples análisis; función desde contexto | POSSIBLE_WITH_SCOPE | PROVISIONAL (negativo) | D7 EXPANDIR + D8 | General-proyecto (negativo) | Sin medida de discriminación por oyentes; `possible_action` vacío |
| CAND-HAR-037 | Conducción/tono común cromático sin partida estructural (bajo marco) | POSSIBLE_WITH_SCOPE | PROVISIONAL | D7 EXPANDIR | Clásica (positivo débil) | Unidad audible sin medida; transferencia fuera `uncertain`; escucha obligatoria |
| CAND-HAR-038 | Cromatismo no es proxy de tensión/complejidad/emoción | POSSIBLE_WITH_SCOPE | PROVISIONAL (negativo) | D7 (transversal) | General-proyecto (cautela) | Evidencia PARTIAL + GAP; techo POSSIBLE_WITH_SCOPE por decisión del Director |
| CAND-HAR-039 | Cromáticos recurrentes como organización estable de loop (dimensión cíclica) | POSSIBLE_WITH_SCOPE | GENRE_SPECIFIC | D7 EXPANDIR | Pop/rock cíclico | Corpus PARTIAL; normalización/expectativa medidas pendientes; `possible_action` vacío |

Cobertura: 39/39 representados (001–039, sin omisiones). Ningún YAML modificado; ningún candidato ascendido silenciosamente (003 y 006 conservan readiness STRONG pero su integration status se evalúa por alcance: SUPPORTED-negativo y TRADITION_SPECIFIC respectivamente).

## NOT_READY Preservation

- CAND-HAR-002 (bajo tónico / pedal / root en bajo). Bloqueo: cinco elementos separados (root, bajo, pedal, bajo-repetido, centro) sin ponderación; regla root-en-bajo = tónica rechazada; evidencia repertorística/teórica sin medida dedicada; HYPOTHESIS sin `possible_action`. Resolvería: RQ-HAR-008 (peso causal bajo vs. root, pedal, inversión, voicing) + medida de atribución de centro con manipulación de bajo. La IA NO debe: inferir centro desde bajo, prescribir pedal como fijador, ni tratar root y bajo como intercambiables.
- CAND-HAR-005 (duración + colocación métrica/formal). Bloqueo: tres indicios auditados por separado sin fusionar; primario métrico (Temperley 2001) no inspeccionado; Caplin como marco clásico sin transferencia pop; HYPOTHESIS sin `possible_action`. Resolvería: inspección primaria pendiente + RQ-HAR-008/forma (posición y duración en interacción con bajo y función seccional) + medida que aísle cada indicio. La IA NO debe: probar centro desde duración/posición ni convertir prominencia en función.
- CAND-HAR-019 (distinción registral quíntuple). Bloqueo: claim puramente estructural/analítico; inferencias perceptivas prohibidas; `possible_action` vacío por insuficiencia perceptiva (indicio propio n=1 + convergencia melodía-sobre-bajo). Resolvería: RQ-HAR-008 (registro, octava, duplicación, spacing) + literatura de streaming/proximidad con estímulos armónicos + medida de continuidad con manipulación registral. La IA NO debe: tratar octavas como intercambiables ni derivar decisiones registrales de esta distinción.

## Cross-Candidate Contradictions — Consistency Pass

Resultado por par de tensión (documentado, no resuelto por elección silenciosa):

- 001 vs. 004: COMPATIBLES. Recurrencia como indicio débil (001) vs. frecuencia/finalidad insuficientes solas (004): "no suficiente != no informativo". Sin contradicción.
- 003 vs. todos los usos de estabilidad: GUARDA APLICADA. Ningún claim usa "estable" desnudo; 003 opera como cautela transversal. Sin contradicción residual.
- 006 vs. 008: DELIMITADOS POR ALCANCE. Centro sin V–I (006, modal/pop) vs. V–I privilegiado en tradiciones acotadas (008): coexisten por scope. Tensión aparente resuelta por tradición, registrada explícitamente.
- 007 vs. 009/012: COMPATIBLES. El contexto importa (007) sin volver irrelevantes root motion (009: insuficiente, no irrelevante) ni indicios de dominante (012: matriz sin pesos). Registrado como insuficiencia, no determinación total.
- 013 vs. 014: COMPATIBLES. Movimiento pequeño como herramienta contextual (013) vs. distancia mínima no-objetivo (014): la heurística débil vive dentro de la anti-regla. Sin dosis-respuesta en ningún caso.
- 015 vs. 006/008: DELIMITADOS POR ALCANCE. Normas clásicas de tendencia (015) vs. alternativas modales/pop (006: soul-dominant sin leading tone; 008 mitad negativa). Coexisten por tradición.
- 017 vs. 020: RESUELTO POR DIVISIÓN APROBADA. Prohibición acotada (017 claim A) vs. planing como organización (020 claim B): IDs separados, sin solape normativo.
- 018 vs. HAR-002 (007/012): COMPATIBLE CON LÍMITE. No-equivalencia e insuficiencia mutua (018) con "parcialmente independientes" retirado; límite con 012 preservado. Sin afirmación de independencia.
- 021/022/023: SEPARACIÓN OBLIGATORIA. Tempo, tasa, duración y aceleración permanecen variables distintas; ninguna fusión. Sin contradicción.
- 024 vs. 025: TENSIÓN EPISTÉMICA PRESERVADA. Persistencia posible (024, heurística débil) vs. cautela de marco (025): 024 solo opera con las cinco ranuras de 025. Uso sin marco = violación metodológica, no contradicción factual.
- 026 vs. 011: SOLAPE BENIGNO REGISTRADO. Persistencia cíclica cross-domain (026) vs. organización cíclica sin sintaxis dirigida (011): 026 es la mitad temporal/estasis, 011 la mitad sintáctica. Referencia cruzada obligatoria; sin fusión de IDs.
- 027/028/029: DISTINCIONES PRESERVADAS. Cadencia-proceso (027) / llegada != cierre (028) / jerarquía != ranking (029) operan a niveles distintos (proceso, contribución, ponderación). Sin colapso.
- 031 vs. 011/026: DELIMITADO POR FUNCIÓN. Retorno/frontera no-cadencial (031) vs. organización (011) y persistencia (026): 031 es la mitad terminal/frontera. Sin duplicación (ver notas de auditoría).
- 033/034/035: DISTINCIONES PRESERVADAS. Centro vs. colección (035), tonicalización vs. modulación (033), etiqueta vs. percepción (034): tres ejes distintos. Sin colapso.
- 036/037: COMPLEMENTARIOS. Múltiples lecturas (036, diagnóstico) vs. lectura de conducción/tono común (037, una lectura disponible bajo marco): 037 es un valor posible de la matriz de 036. Sin contradicción.
- 038 vs. 012: COMPATIBLES. Ni cromatismo (038) ni clasificación de dominante (012) son proxy de tensión: dos prohibiciones convergentes, dominios distintos. Sin contradicción.
- 039 vs. 011/026: APORTE DISTINTO REGISTRADO. Membership cromática recurrente (039) vs. sintaxis cíclica (011) y persistencia (026): 039 es la extensión cromática de la organización cíclica. Referencia cruzada obligatoria; sin fusión.

Contradicción genuina restante: NINGUNA factual sin delimitar. La única tensión viva es de valores entre tradiciones (desarrollo dirigido clásico como ideal vs. loop/estasis como virtud), ya resuelta por scope en Melody v0 y preservada aquí: no es desacuerdo factual sino estético, y se marca con alcance siempre.

## Cross-RQ Integrated Principles — Evaluation

Cuestiones propuestas, evaluadas una por una (ninguna forzada a sobrevivir):

- A. La interpretación armónica es contextual, no lookup de etiquetas. → SUPPORTED como conocimiento negativo (007, 009, 016, 034, 036 convergen en insuficiencia de etiqueta); PROVISIONAL como asignación positiva (matriz de indicios sin pesos). Sobrevive dividida en dos mitades.
- B. Centro, colección, función, bajo, conducción y cierre son variables distintas. → SUPPORTED (026-distinciones de HAR-001, 018, 025-convención, 028, 035 CENTER != COLLECTION). Es el principio transversal más sólido; opera como higiene en las siete familias.
- C. La armonía puede ser dirigida o cíclica. → SUPPORTED (008 acotado + 011/026/031/039 documentan lo cíclico; contraejemplos clásicos documentan lo dirigido). Sobrevive.
- D. El cambio armónico de superficie no equivale a cambio estructural/regional. → PROVISIONAL (024 heurística débil + 025 cautela + casos Spicer bidireccionales; sin medida de unidad audible). Sobrevive como cautela + heurística, no como hecho medido.
- E. La conducción es multi-objetivo, no optimización de distancia mínima. → PROVISIONAL (014 anti-regla + 013 herramientas + 015/017/020 acotaciones; ponderación entre objetivos sin medir). Sobrevive como marco de decisión, no como modelo.
- F. Cadencia/llegada/cierre requieren razonamiento separado. → SUPPORTED como distinción (027 proceso + 028 no-equivalencia + 032 existencia de estados; Sears como apoyo parcial); PROVISIONAL como ponderación (029 sin `possible_action`). Sobrevive dividida.
- G. El cromatismo es familia de mecanismos, no variable de efecto. → PROVISIONAL (033–039 con evidencia por mecanismo y tradición; funciones positivas débiles, cautelas sólidas). Sobrevive como familia, explícitamente no-exhaustiva.
- H. Muchas decisiones armónicas requieren confirmación cross-domain. → SUPPORTED (028 cierre + 026 estasis + 031 frontera + dependencias bajo/forma registradas en todas las RQs). Sobrevive; es el principal delimitador de capacidad autónoma de Harmony.

Ningún principio se rechaza; A y F se dividen en mitad negativa (SUPPORTED) y mitad positiva (PROVISIONAL). Ninguno se formula como ley universal: todos llevan alcance del proyecto.

## Decision Conflict / Tradeoff Matrix

Cada fila: variables en conflicto | soporte | scope | establecida o plausible (`uncertain` donde corresponde).

| Tensión | Variables en conflicto | Soporte | Scope | Estado |
|---|---|---|---|---|
| Tonos comunes vs. diferenciación registral | Retención literal (013) vs. desplazamiento deliberado / planing (013-alt, 020) | Spicer pedal fija-vs-engaña; Doll conexiones | Transversal; planing por repertorio | Establecida como tradeoff contextual (no hay dosis que la resuelva) |
| Movimiento mínimo vs. trayectoria melódica/bajo independiente | Economía (014-neg) vs. voces superior/grave con lógica propia (016, Melody) | Anti-regla + cinco niveles + divorce pendiente | General (negativo); divorce a RQ-HAR-009 | Plausible con borde establecido (lo establecido es la prohibición, no la curva) |
| Mantener centro vs. crear ambigüedad | ESTABLISH/CONFIRM (001) vs. AMBIGUATE con competidores (004) | Loops con doble centro documentado | Pop/rock/loop | Establecida como alternativa deliberada; receta de ambigüedad excluida (`uncertain` como técnica) |
| Función dirigida vs. recurrencia cíclica | V–I / pre-tónica (008) vs. loop/shuttle (011, 039) | Corpus + repertorio por tradición | Por tradición (incompatibles como gramática única) | Establecida como elección de marco; `uncertain` función interna de loops |
| Actividad de superficie vs. persistencia regional | Tasa/cambios (021–023) vs. región (024–026) | Caplin acotado + Spicer bidireccional | Marcos declarados | Plausible (criterios fuera de práctica común abiertos) |
| Llegada fuerte vs. apertura continuada | Cadencia/llegada (027/030) vs. deceptiva/evadida/apertura (028/032) | Tipologías clásicas + finales documentados | Por tradición y escala formal | Establecida como repertorio de opciones; efecto medido `uncertain` fuera de clásica |
| Consistencia de colección vs. expansión cromática | Centro+colección (035) vs. préstamo/aplicado/conducción (033/034/037) | OMT + Spicer + corpus parcial | Por marco declarado | Plausible con vocabulario disponible; afecto/tensión `uncertain` |
| Claridad funcional vs. lecturas múltiples | Etiqueta única vs. matriz contextual (036) | Disociación enarmónica VERIFIED | General (negativo) | Establecida como higiene; discriminación por oyentes `uncertain` |

Ninguna fila inventa efectos causales: donde no hay medida, se marca `uncertain`.

## Actionability Audit

Definiciones (ayuda de integración, no nuevo ciclo epistémico):

- ACTIONABLE NOW: heurística negativa o estructural suficientemente apoyada para usar ya, con alcance declarado y escucha obligatoria donde se indique.
- ACTIONABLE WITH SCOPE: usable solo dentro de tradición/repertorio/contexto explícito.
- DIAGNOSTIC ONLY: ayuda a interpretar decisiones pero no justifica generar una opción.
- BLOCKED: requiere evidencia o otro dominio/RQ; la IA no debe actuar sobre ello.

| Operación / conocimiento | Clasificación | Base |
|---|---|---|
| No decidir estabilidad desde sonoridad aislada (003) | ACTIONABLE NOW | STRONG, VERIFIED, negativo |
| No inferir tónica desde frecuencia/primero/final (004-neg) | ACTIONABLE NOW | Contraevidencia VERIFIED |
| No inferir función desde etiqueta/root solo (007/009/016/034-neg) | ACTIONABLE NOW | Convergencia multi-RQ |
| No optimizar distancia mínima (014) | ACTIONABLE NOW | Contraejemplos VERIFIED |
| No usar cromatismo/dominante como proxy de tensión (012/038) | ACTIONABLE NOW | Cautela acotada |
| No tratar llegada como cierre ni categoría como fuerza (028/029-neg) | ACTIONABLE NOW | Sears parcial + convergencia |
| Especificar ritmo armónico separado del tempo (021) | ACTIONABLE NOW | Higiene metodológica |
| Declarar marco de cinco ranuras ante "prolonga" (025) | ACTIONABLE NOW | Cautela de segundo orden |
| Usar vocabulario neutral de loop/frontera (031) | ACTIONABLE NOW | Observación convergente |
| Enmarcar con colección + recurrencia (001) | ACTIONABLE WITH SCOPE | Sin `possible_action`; marco + escucha |
| Centro modal sin V–I (006) | ACTIONABLE WITH SCOPE | Tradiciones modales/pop; escucha |
| V–I como llegada fuerte (008) | ACTIONABLE WITH SCOPE | Práctica común / pre-tónica pop |
| Sostener loop sin sintaxis dirigida (011/026/039) | ACTIONABLE WITH SCOPE | Pop/rock/loop-based + arreglo |
| Tono común / movimiento pequeño (013) | ACTIONABLE WITH SCOPE | Intención de continuidad + convergencia + escucha |
| Resolver tendency tones (015) / evitar paralelas (017) / planing (020) | ACTIONABLE WITH SCOPE | Tradición o repertorio declarado |
| Aceleración hacia cadencia (023) | ACTIONABLE WITH SCOPE | Sentence clásica + fragmentación coordinada |
| Fórmulas plagales/modales (030) | ACTIONABLE WITH SCOPE | Fórmula + tradición + escala; sin promesa de cierre |
| Préstamos / conducción cromática / CTo7 (035/037) | ACTIONABLE WITH SCOPE | Marco + fuente + resolución + escucha |
| Ponderar fuerza cadencial por categoría (029) | DIAGNOSTIC ONLY | Hipótesis sin `possible_action` |
| Asignar función cromática por matriz (036) / diagnosticar prolongación (024) | DIAGNOSTIC ONLY | Sin técnica positiva; marco obligatorio |
| Atribuir centro local tras V/x (034) | DIAGNOSTIC ONLY | Puramente negativo |
| Ponderar bajo/pedal/duración/posición/registro (002/005/019) | BLOCKED | NOT_READY; requiere RQ-HAR-008 + medidas |
| Cierre/arrival ponderado multi-dominio | BLOCKED | CROSS_DOMAIN_REQUIRED (melodía, metro, forma, arreglo) |
| Función interna de loops; normalización perceptiva; curva corpus→expectativa | BLOCKED | GAPs empíricos |

La correspondencia readiness→accionabilidad NO es mecánica: 003/006 (STRONG) dan una cautela NOW y una técnica WITH SCOPE; varios POSSIBLE_WITH_SCOPE dan solo DIAGNOSTIC (029/034/036); los tres NOT_READY son BLOCKED.

## AI Harmonic Reasoning Representation (non-executable)

Representación mínima de razonamiento para planificación futura. No es código, no cambia SongPlan, sin pesos numéricos, sin motor determinista de reglas.

```
HARMONIC CONTEXT
- center_evidence: indicios separados (collection, recurrence, bass, duration,
  metric_position, formal_position, cadential_confirmation) + competidores
- collection: colección vigente declarada (y centro de referencia si difieren)
- organization: directed / cyclic / ambiguous (+ marco de tradición declarado)
- region_function: región/función solo si el marco lo permite, con las cinco
  ranuras (FRAMEWORK, OBJECT, CRITERION, SCOPE, EVIDENCE TYPE)

GOAL (uno o varios, con conflicto explícito si coexisten)
- ESTABLISH / CONFIRM / MAINTAIN / WEAKEN / AMBIGUATE (centro)
- STAY / DEPART / CONTINUE / PREPARE / APPROACH / RETURN / CYCLE (metas no-oficiales)
- CONNECT (continuidad) vs. ARTICULATE (diferenciación deliberada)
- ARRIVE (llegada) vs. REMAIN OPEN (apertura continuada)
- EXPAND (colección) con fuente declarada

DECISIONS
- next_harmonic_target: objetivo declarado (o continuación cíclica declarada)
- bass_root_relationship: root y bajo registrados por separado (peso BLOCKED)
- voice_leading_continuity: retención / movimiento pequeño / desplazamiento /
  planing (con registro e identidad; ponderación registral BLOCKED)
- harmonic_timing: las seis variables D4 por separado (tasa, duración, patrón,
  colocación, cambio estructural; tempo aparte)
- surface_vs_region: evento de superficie + región declarada con cinco ranuras
- boundary_arrival_behavior: proceso cadencial o marca cíclica con vocabulario
  neutral (cadencia solo ante proceso declarado)
- chromatic_interpretation: matriz de lecturas con alternativas (nunca etiqueta única
  forzada); TONICIZATION vs. MODULATION vs. MIXTURE vs. LEADING vs. LOOP-MEMBER

CONSTRAINTS
- tradition_genre_scope: marco declarado (clásica / pop-rock / modal / loop-based)
- melody, form, meter, register, arrangement, lyrics_prosody (dominio y estado:
  bloquea / mejora / independiente — ver mapa cross-domain)

UNCERTAINTIES
- unresolved_candidates: 002/005/019 u otros con `possible_action` vacío
- cross_domain_dependency: qué dominio falta para cada pretensión (cierre,
  dirección confirmada, metro operativo, marca de frontera)
- perception_gap: qué se afirma analíticamente sin medida (normalización,
  unidad regional audible, fuerza sentida, atribución local)
```

Lo inventado más allá de la integración (p. ej. pesos, curvas, gramática T–PD–D, máquina de estados) queda explícitamente fuera.

## Composer Capability Check

Evaluación de decisiones hipotéticas concretas. Escala: CAN REASON / CAN REASON WITH SCOPE / PARTIALLY / CANNOT YET.

- Establecer un centro. → CAN REASON WITH SCOPE. Colección + recurrencia (001) y centro modal (006) con alcance y escucha; ponderación bajo/duración/posición BLOCKED (002/005). Bloqueador: sin pesos ni dosis.
- Mantener un centro variando acordes. → PARTIALLY. Persistencia cíclica (026/039) y superficie-en-región (024) con marco declarado; criterios fuera de práctica común abiertos. Bloqueador: convención de cinco ranuras obligatoria pero sin medida de unidad audible.
- Elegir organización dirigida vs. cíclica. → CAN REASON WITH SCOPE. V–I acotado (008) vs. loop (011) por tradición declarada; función interna de loops abierta. Bloqueador: asignación interna `uncertain`.
- Seleccionar la siguiente armonía. → PARTIALLY. Rol por contexto (007) con matriz de indicios (012) sin pesos; root motion insuficiente solo (009). Bloqueador: sin ponderación perceptiva; corpus != expectativa (010).
- Conectar dos sonoridades elegidas. → CAN REASON WITH SCOPE. Tono común / movimiento pequeño (013) o desplazamiento/planing (020) con escucha; resoluciones y paralelas solo en tradición (015/017). Bloqueador: registro/octava/identidad (019) y peso bajo (008 pendiente).
- Elegir timing de cambio armónico. → CAN REASON WITH SCOPE (negativo) / PARTIALLY (positivo). Higiene de seis variables (021/022) usable ya; aceleración solo clásica (023); curva tasa→energía inexistente. Bloqueador: sin dosis ni medida temporal.
- Mantener región cambiando superficie. → PARTIALLY. Operaciones condicionales (D5.5) con cinco ranuras; CTo7 cromático (037) en marco clásico. Bloqueador: criterios de subordinación fuera de práctica común + GAP perceptivo.
- Crear llegada sin suponer V–I. → CAN REASON WITH SCOPE. Fórmulas plagales/modales (030), parada de loop (031), tónica sostenida (032) por tradición; proceso cadencial clásico (027) en su marco. Bloqueador: fuerza sentida sin medida fuera de clásica (029).
- Mantener una frase abierta. → CAN REASON WITH SCOPE. Semicadencia/deceptiva/evadida, final no-tónico declarado (032), loop sin marca terminal (031). Bloqueador: apertura percibida vs. corte sin medida.
- Interpretar/introducir un acorde cromático. → CAN REASON WITH SCOPE. Vocabulario de préstamo/conducción (035/037) con fuente y resolución; matriz de lecturas (036). Bloqueador: fuente y función exigen convergencia + escucha; bajo/voicing pendientes (008).
- Decidir si cromatismo local implica nuevo centro. → PARTIALLY. Corte tonicalización/modulación solo clásico (033); etiqueta V/x insuficiente (034). Bloqueador: frontera fuera de clásica `uncertain` (RQ-HAR-007); atribución local sin medida.
- Terminar una sección basada en loop. → CAN REASON WITH SCOPE. Marcar iteración final con arreglo (031); tónica sostenida o final declarado (032). Bloqueador: terminal-vs-corte sin medida; fade-out GAP total.
- Coordinar cierre con melodía/forma. → CANNOT YET. Armonía como contribuidor parcial (028) con CROSS_DOMAIN_REQUIRED explícito; unidad melodía-armonía pendiente de RQ-HAR-009. Bloqueador: dominios ausentes (melodía, metro operativo, forma, arreglo, prosodia).

Resumen: CAN REASON (pleno, sin scope): ninguno en positivo — solo las cautelas negativas (anti-reglas) son CAN REASON sin scope. CAN REASON WITH SCOPE: 8 (establecer, organizar, conectar, temporizar-negativo, llegada sin V–I, apertura, cromatismo, final de loop). PARTIALLY: 4 (mantener centro, siguiente armonía, región-superficie, cromatismo→centro). CANNOT YET: 1 (cierre coordinado multi-dominio).

## What Harmony Still Cannot Do — Negative-Capability Map

Derivado del material auditado (no de la lista sugerida en el encargo, aunque converge):

- Ponderación bajo/inversión/voicing: peso causal del bajo vs. root, pedal, inversión, spacing, duplicación, registro (002/005/019 BLOCKED; 012/016/028/036-037 lo invocan sin resolver). → RQ-HAR-008.
- Frontera y procedimientos de modulación: corte tonicalización/modulación fuera de práctica común; modulación local vs. seccional; retorno (033 frontera legada). → RQ-HAR-007.
- Interacción melodía-armonía completa: chord/non-chord tones, suspensiones, apoyaturas, disonancia acentuada, elección de acorde bajo melodía, divorce, función del grado melódico (toda pretensión de cierre/llegada/dirección la invoca). → RQ-HAR-009.
- Gramática armónica por género: sintaxis pop/rock interna de loops, función interna, esquemas modales con juicios, predominantes alteradas pop/jazz. → corpus + `genres/` futuro.
- Ponderación cuantitativa/perceptiva de indicios: ninguna curva centro, función, continuidad, cierre o tensión con pesos; betas/p/R² prohibidos como pesos. → GAP empírico estructural.
- Función dentro de loops: asignación interna, jerarquía medible, normalización perceptiva, expectativa sentida. → GAP empírico + teoría.
- Integración del cierre entre dominios: pesos armonía/melodía/metro/forma/arreglo/prosodia; parada-vs-corte; fade-out; prolongational closure. → cross-domain + medida.
- Identidad de voz y percepción registral: voces inestables, cruce, reasignación, streaming con estímulos armónicos, equivalencia de octava. → RQ-HAR-008 + medida.
- Evidencia perceptiva directa para claims teóricos: atribución de centro en canciones, continuidad por tonos comunes, resoluciones concretas, discriminación entre lecturas cromáticas, persistencia regional audible. → agenda experimental futura (ningún diseño en esta tarea).

## Cross-Domain Dependency Map

Por dominio: qué decisiones Harmony bloquea (BLOCKED), cuáles mejora (IMPROVED) y cuáles operan ya independientes (INDEPENDENT).

- MELODY: BLOCKED: cierre/apertura coordinado (028/032), llegadas con soprano (028), divorce y non-chord tones (009 futura), función del grado melódico, cromatismo melódico↔armónico (035/037). IMPROVED: dirección confirmada/contradicha (D2), atribución de centro local (034). INDEPENDENT: higiene negativa (anti-reglas), vocabulario neutral, diagnóstico contextual puro.
- RHYTHM / METER: BLOCKED: metro operativo y colocación eficaz (005/021/028: la melodía/armonía solas no fijan metro). IMPROVED: refuerzo de centro por posición (D1), sincronía de llegada (D6), onset percibido de cambio (D4/D5). INDEPENDENT: distinciones conceptuales (seis variables D4).
- FORM: BLOCKED: escala de región/cierre (frase vs. sección vs. canción: 027/030/032), retorno seccional, trayectoria. IMPROVED: posición formal como indicio (D1/D6), aceleración clásica ligada a continuation (023). INDEPENDENT: organización cíclica como estado (011).
- ARRANGEMENT / PRODUCTION: BLOCKED: interés formal en estasis (026), marca de frontera cíclica (031), qué cuenta como cambio para el oyente (D5). IMPROVED: color cromático (voicing/timbre, 035/037), desambiguación por textura/paralelismo (Doll cap.6). INDEPENDENT: loop como marco analítico.
- BASS / VOICING (futura RQ-HAR-008): BLOCKED: ponderación de centro (002), confirmación por duración/posición (005), decisiones registrales (019), interpretación cromática con bajo (036/037), llegadas por bajo (028). IMPROVED: casi toda D1–D3 y D6–D7. INDEPENDENT: casi ninguna positiva (las negativas sí).
- GENRE (especialización futura): BLOCKED: transferencia de cualquier fórmula positiva fuera de su tradición (008/015/017/023/027/029 clásicas; 011/026/031/039 loop-based; 006/030/035 modal). IMPROVED: calibración de pesos por estilo (cuando existan). INDEPENDENT: cautelas negativas generales-dentro-del-proyecto.
- LYRICS / PROSODY: BLOCKED: cierre en canción (co-determina, 028/032), stress para síncopa armónica asociada. IMPROVED: posición de llegada cantada. INDEPENDENT: armonía instrumental (alcance declarado).

Lectura para priorizar dominios: BASS/VOICING es el bloqueador interno más denso (002/005/019 + mejora a casi todo); MELODY es el bloqueador externo mayor (cierre y RQ-MEL-007); FORM/RHYTHM son co-requisitos del cierre; ARRANGEMENT es co-requisito de lo cíclico.

## Melody v0 ↔ Harmony v0 Interface Preview

Sin fusionar integraciones; sin candidatos nuevos; sin RQ-HAR-009.

- Melody v0 sabe decidir (con apoyo): ESTABLECER por repetición exacta, CONTINUAR/VARIAR conservando parentesco (transposición pequeña, final cambiado clásico, redistribución rítmica con pitches intactos), anti-jerarquía ritmo-vs-pitch, continuación local tono-a-tono, fraseo aditivo, arco como opción no-norma, tesitura habitable, anticipación pop/rock, alargamiento+silencio como contribución al cierre, contraste seccional con haz, sostener loop variando arreglo. Casi todo con scope o escucha; invención del primer motivo UNSUPPORTED (GAP-01).
- Harmony v0 sabe decidir (con apoyo): ORIENTAR con cautelas + indicios débiles, ORGANIZAR dirigido-vs-cíclico por tradición, CONECTAR con heurísticas débiles, TEMPORIZAR con higiene + aceleración clásica, PERSISTIR con marco obligatorio, LLEGAR/MANTENER ABIERTO con fórmulas por tradición, EXPANDIR con familia de mecanismos, DIAGNOSTICAR sin forzar etiqueta. Casi todo PROVISIONAL/WITH SCOPE; ponderaciones y cierre coordinado BLOCKED.
- Dónde ya se necesitan: finales cambiados melódicos (CAND-MEL-008) dependen del marco armónico (D2/D6); fragmentación+liquidación (CAND-MEL-009) exige aceleración armónica (023); cierre melódico aislado es como máximo parcial (GAP-08 Melody ↔ 028 Harmony: la armonía probablemente decide pero tampoco basta sola); llegada/culminación melódica (pico, duración, posición) exige configuración armónica; non-chord tones y apoyaturas (RQ-MEL-007) esperan a RQ-HAR-009; transposición pequeña con penalización (EXP-001 B=3) converge con 019 (octavas no intercambiables) sin resolver registro.
- Futuras preguntas de interfaz (no investigadas aquí): ¿qué marco armónico vuelve a un final cambiado en pregunta vs. cierre? ¿Qué aceleración armónica convierte fragmentación en conducción? ¿Qué combinación armonía–melodía–metro–posición produce cierre medido? ¿Qué guía la elección de acorde bajo melodía dada (y viceversa)? ¿Cómo se coordinan cromatismo melódico y armónico? ¿Qué soprano/bajo de llegada maximizan cierre por tradición?

## Unsupported / Blocked Knowledge

Consolidado BLOCKED (requiere evidencia u otro dominio; la IA no debe actuar):

- Ponderación de indicios de centro; dosis de recurrencia/duración; posición como prueba (002/005 + GAP de medida).
- Decisiones registrales de conexión: octava, duplicación, spacing, identidad de voz (019 + RQ-HAR-008).
- Función interna de loops y normalización perceptiva (011/026/039 + GAP).
- Fuerza cadencial como ranking usable (029: DIAGNOSTIC ONLY).
- Curva corpus→expectativa/percepción (010 + GAP).
- Cierre coordinado multi-dominio (028/032 + RQ-HAR-009/forma/ritmo/arreglo).
- Frontera de modulación fuera de práctica común (033 + RQ-HAR-007).
- Tensión como variable (012/023/038: prohibido el proxy; componentes sin modelo oficial).
- Invención de material armónico inicial (análogo a GAP-01 melódico: ningún candidato genera la primera progresión; todo opera sobre material existente o marcos de repertorio).

## Candidate Promotion Readiness

Evaluación de integración (no cambia estados; no edita YAML):

- Candidatos más fuertes para futura promoción (tras revisión del Director, con scope explícito): 003 (cautela metodológica SUPPORTED), 006 (centro modal con alcance), 004-mitad-negativa, 007/009/014/038 (anti-reglas convergentes), 025 (higiene de marco), 031 (vocabulario + frontera cíclica). Todos requerirían formulación manual (no YAML directo) y rattachement a su tradición.
- Requieren más evidencia directa: 001 (medida de atribución en canciones), 008-mitad-positiva (texto pedagógico), 011/026/039 (test de oyentes en loops), 013 (medida de continuidad), 027–032 (textos completos Sears/Caplin/Doll/Temperley + medida fuera de clásica), 033–037 (medida de centro local/discriminación), 029 (texto Sears + réplica fuera de clásica).
- Bloqueados por otro dominio: 002/005/019 (RQ-HAR-008 + medida), 028/032 (RQ-HAR-009 + forma/ritmo/arreglo), 015/017/023/027 (tradición sin transferencia: `genres/` + corpus), 010-curva (empírico), 036-matriz (medida de discriminación).

## Manual Readiness

Respuesta: NO.

Razones: la capa positiva es mayoritariamente PROVISIONAL/WITH SCOPE con `possible_action` vacío en 13 candidatos (001, 002, 004, 005, 008, 011, 015, 019, 020, 029, 034, 036, 039); las ponderaciones (bajo, duración, posición, registro, función interna, cierre) están BLOCKED; la verificación de fuentes es PARTIAL con textos completos pendientes (Doll, Nobile, Sears, Caplin 2024); el cierre y la dirección confirmada exigen dominios ausentes. Lo sólido (anti-reglas, higiene, vocabulario) es valioso como disciplina pero insuficiente como manual de decisiones. `research/integrations/harmony-foundations-v0.md` permanece como capa provisional operativa. NO poblar `manual/02-harmony.md`.

## Rule Readiness

Respuesta: NO.

Ningún conocimiento está listo para codificación determinista o estructurada en `rules/`. Lo más cercano (higiene de seis variables, convención de cinco ranuras, vocabulario neutral, fórmulas idiomáticas con alcance) carece de límites verificados, de medidas de efecto y de resolución cross-domain (bajo real, metro operativo, intérprete/arreglo, forma). Una heurística composicional no es una regla de máquina; una cautela metodológica menos aún. No crear reglas.

## Remaining Research Priorities

Comparación de siguientes pasos (sin asumir que el orden numérico es prioridad; re-evaluado desde la evidencia integrada):

- RQ-HAR-008 (bajo / inversión / sonoridad / voicing). Desbloquearía: 002, 005 (parcial, con forma), 019, ponderación de 012/016, interpretación cromática con bajo (036/037), llegadas por bajo (028), desambiguación de loops (Doll: bajo como co-determinante). Prerrequisito de: RQ-HAR-009 (melodía sobre bajo/voicing real) y de parte de RQ-HAR-007 (movimiento grave en modulación). Leverage: el más denso internamente; converge con la preferencia del Director (sonoridad/bajo antes que modulación en orden práctico), pero se elige por evidencia, no por precedente.
- RQ-HAR-007 (modulación). Desbloquearía: frontera 033, cambio de centro seccional, retorno. Alcance estrecho: un solo mecanismo (cambio de centro) frente a la transversalidad del bajo. No es prerrequisito de 008 ni de 009. Riesgo: taxonomía de tipos sin decisiones de compositor general (recetas de transición).
- RQ-HAR-009 (interfaz melodía-armonía). Leverage cross-domain máximo (desbloquea GAP-08 melódico, RQ-MEL-007, cierre coordinado). Pero presupone bajo/voicing resuelto (soprano + bajo + realización son los tres términos de la interfaz) y forma/ritmo operativos: empezarla ahora repetiría el patrón de 028 (contribuidor parcial sinfrontrol de los demás dominios). Es la última por dependencia, no por falta de importancia.
- Dependencia documentada adicional: corpus pop/rock con juicios de oyentes (centro, función interna, cierre, normalización cromática). No es RQ sino deuda empírica transversal que condiciona a las tres; se registra como requisito, no como alternativa.

Riesgo de acumulación teórica sin capacidad compositora: medio-alto si se sigue con 007 (más taxonomía) o 009 prematura (más marcos sin bajo); se mitiga con 008 porque convierte cautelas BLOCKED en decisiones ponderables (qué bajo, qué inversión, qué registro, qué voicing) y da a 009 sus variables materiales.

## Recommended Next Domain/RQ

RQ-HAR-008 (bajo / inversión / sonoridad / voicing).

Por qué (desde la evidencia integrada, no por orden numérico): es el bloqueador que más candidatos desbloquea (002, 005, 019 directos; mejora 012/016/028/036/037 y la mitad temporal de 021–026), el prerrequisito material de RQ-HAR-009 (sin bajo ni voicing la interfaz melodía-armonía no tiene sus términos graves), y el que menor riesgo de acumulación estéril presenta (responde preguntas de compositor —qué suena abajo, en qué disposición— en vez de añadir taxonomías). No se inicia automáticamente: espera confirmación del Project Owner y del Music/Methodology Director.

## Trazabilidad

- Fuentes: síntesis RQ-HAR-001–006 (`research/domain/harmony/*.md`), RQs (`research/questions/RQ-HAR-*.md`), CAND-HAR-001–039 (YAML individuales), Melody v0 (comparación e interfaces). Sin fuentes externas nuevas en esta tarea.
- Decisiones de integración propias de este documento (no del proyecto): arquitectura ORIENTAR–DIAGNOSTICAR con TIME/PERSIST separados; integration status por familia y candidato (distinto del readiness heredado); matrices de tradeoffs, accionabilidad y capacidad; representación de razonamiento; comparación de prioridades con recomendación 008.
- Prohibido citar este archivo como conocimiento aprobado: es capa de auditoría previa a revisión.
