# Melody + Harmony Foundations v0

## Purpose and Scope

Esta integración pregunta si el conocimiento auditado de Melody y Harmony permite coordinar intención melódica, selección armónica y realización concreta para tomar decisiones compositivas. No es una suma de los dos dominios, una guía de acordes, una receta de armonización, una teoría universal, un esquema de `SongPlan` ni una promoción a `manual/` o `rules/`.

El documento usa únicamente el estado heredado de Melody Foundations, Harmony Foundations v1 y RQ-HAR-009. No realiza nueva investigación, auditoría de candidatos ni investigación de modulación.

## Epistemic Status

Estado: **integración de investigación / candidato a revisión metodológica**. Las etiquetas `SUPPORTED`, `PROVISIONAL`, `DIAGNOSTIC ONLY`, etc. describen la capacidad de integración, no cambian el estado de ningún candidato. `CAND-MEL-018` permanece rechazado. La integración no contiene resultados experimentales propios.

## Why Joint Integration Is Needed

Melodía y armonía pueden compartir pitch, tiempo, registro y función sin ser el mismo objeto. La melodía puede permanecer mientras cambia la armonía; una armonía puede permanecer mientras cambia la melodía. Por ello, el problema útil no es buscar una correspondencia nota→acorde, sino razonar sobre restricciones, alternativas e interpretaciones.

## Domain Capital Before Integration

Melody aporta operaciones acotadas de establecimiento, continuación, repetición, variación, llegada, registro, ritmo, silencio y reutilización. Sigue abierta la construcción de la idea melódica inicial. Harmony v1 aporta orientación y organización, selección frente a realización, persistencia/cambio, timing, llegada/apertura, cromatismo y realización como sonoridad. RQ-HAR-009 aporta el interfaz: pertenencia no equivale a estabilidad, una melodía fija subdetermina la selección, existen reinterpretaciones analíticas y realizaciones múltiples, y las llegadas melódica y armónica pueden divergir.

Este capital permite diagnosticar y manipular alternativas acotadas. No proporciona una jerarquía general entre ellas ni predicción perceptiva suficiente.

## Core Interaction Architecture

La arquitectura que mejor encaja con la evidencia es iterativa:

`MATERIAL / INTENCIÓN MELÓDICA ↔ CONTEXTO ARMÓNICO ↔ SELECCIÓN ↔ REALIZACIÓN ↔ TIMING Y LLEGADA`

Cada intercambio se clasifica como **determina**, **constriñe**, **sugiere**, **permite**, **reinterpreta** o **no informa actualmente**. Una nota fija normalmente constriñe el espacio de realizaciones; no determina inversión, bajo ni sonoridad. La realización puede reinterpretar analíticamente la función de una nota; eso no demuestra una reinterpretación perceptiva.

No se colapsan estas distinciones: Melody ≠ top voice universal; pitch melódico ≠ chord member automático; chord member ≠ estabilidad; non-chord tone ≠ tensión ni error; llegada melódica ≠ llegada armónica ≠ cierre; root ≠ bass; símbolo ≠ sonoridad realizada; centro ≠ colección; tonicización ≠ modulación.

## Melodic Invariants

Antes de escoger armonía hay que declarar qué se pretende conservar. Los invariantes posibles son: pitch exacto, pitch class, contorno, relaciones interválicas, ritmo, onset, duración, registro, identidad de motivo, posición de frase y punto de llegada. No pesan igual: conservar el ritmo puede preservar una relación distinta de conservar el pitch, y mantener el pitch exacto puede reducir más la realización que mantener solo contorno.

La pregunta operativa es: «¿qué debe permanecer igual para llamar a esto el mismo material?». Melody Foundations permite trabajar con esa declaración y con repetición/variación, pero no ofrece una jerarquía universal de invariantes ni resuelve la invención inicial.

## Harmonic Context

El contexto mínimo registra evidencia de centro, colección, organización dirigida/cíclica/ambigua, relación o región actual, timing, persistencia superficial frente a regional, estado de llegada/apertura y posible interpretación cromática. Centro no es colección: una colección alterada puede conservar el centro. Root no es bajo. La sonoridad realizada puede diferir de la identidad armónica analítica.

## Harmonic Selection Under Melody

La melodía puede **constreñir** selecciones incompatibles con un pitch exacto, una colección declarada, un objetivo local o un timing; puede **sugerir** lecturas y objetivos; y puede **permitir** más de una relación armónica. La evidencia no autoriza deducir una armonía única desde una melodía, ni tratar un tono de reposo melódico como obligación de tónica.

La secuencia útil es: declarar material e invariantes; declarar centro/colección/región; formular el objetivo (mantener, variar, aproximar, permanecer abierto, volver o reinterpretar); enumerar selecciones; filtrar por restricciones; conservar alternativas cuando no exista criterio para rankearlas. Selección diatónica, modal o cromática puede ser una hipótesis contextual. Si se pretende establecer un centro nuevo, aparece la dependencia de RQ-HAR-007.

## Harmonic Realization Under Melody

Después de seleccionar una identidad o relación armónica, la melodía fija puede reducir el espacio de bajo, inversión, pitches exactos, registro, spacing, doubling/omission y asignación de voces. CAND-HAR-040/041/043/044/045 y 049 permiten inspeccionar estas variables por separado.

La capacidad actual llega a construir realizaciones admisibles y comprobar restricciones físicas o de tesitura. No llega a escoger con criterios generales cuál es mejor. La conducción de voces, el movimiento del bajo, la retención de tonos comunes y el espaciamiento ofrecen alternativas; mínima distancia no es objetivo universal. La escucha y el contexto de arreglo siguen siendo necesarios.

## Same Melody / Different Harmony

Hay que separar tres niveles:

1. **Posibilidad analítica:** el mismo pitch/contorno/ritmo puede recibir otra lectura armónica.
2. **Disponibilidad compositiva:** se puede cambiar bajo, inversión, identidad, función, colección, timing o realización, sujeto a restricciones.
3. **Efecto perceptivo:** continuidad, contraste, desarrollo o reinterpretación que un oyente experimente no se sigue automáticamente.

Una melodía sustancialmente igual puede ser reutilizada, recibir variación de contexto, terminar de otro modo o volver con distinto soporte. `same melody + changed harmony` no es desarrollo por definición.

## Same Harmony / Different Melody

Armonía persistente puede sostener melodía móvil, tonos comunes, notas no pertenecientes al acorde, cambios de registro, silencio y llegadas melódicas. No exige que la melodía siga cada cambio ni que toda nota tenga acorde compatible sin calificar el marco temporal y analítico. Cambiar melodía no implica cambiar armonía; una llegada melódica puede ocurrir mientras la armonía permanece abierta.

## Held Melody / Changing Harmony

Con E4 tenida a través de dos contextos, el corpus puede: conservar literalmente E4; comprobar su pertenencia relativa a cada sonoridad; describir cambio de grado/función analítica; proponer bajo, inversión y voice-leading alternativos; declarar si centro y colección persisten o cambian; y registrar el timing. Puede haber tono común, pedal melódico, extensión, suspensión-tipo o reinterpretación.

Puede generar varias posibilidades estructurales y explicar por qué son posibles. No puede seleccionar de forma general la mejor, ni afirmar que el cambio crea tensión o continuidad percibida. Un cambio de función en el análisis es **analytical reinterpretation**; solo una escucha diseñada podría establecer **perceptual reinterpretation**.

## Repeated Motif / Harmonic-Context Change

La repetición puede conservar identidad melódica mientras cambia el contexto armónico. El cambio puede operar en bajo, inversión, sonoridad, relación, función, colección o timing. CAND-MEL-007/010/011/012 y CAND-HAR-051 ayudan a distinguir identidad, reutilización y variación contextual. No prueban que el resultado sea desarrollo, más expresivo o más memorable. El objetivo debe declararse: reutilizar, contrastar, cambiar el final o sostener un retorno.

## Melody Rhythm ↔ Harmonic Rhythm

Se registran separadamente onset melódico, duración, IOI, posición métrica, onset y duración armónicos, tasa de cambio y revoicing. El conocimiento permite describir acorde bajo melodía móvil, cambio bajo nota tenida, cambio durante silencio, anticipación melódica y armonía previa a llegada. CAND-MEL-025–030 y HAR-004/021–026 aportan vocabulario y límites.

No hay regla de sincronización: onset melódico ≠ onset armónico, y alineación no equivale a cierre. La colocación concreta sigue siendo una decisión contextual, dependiente también de métrica, forma, arreglo y prosodia.

## Melody ↔ Bass

El bajo es una capa distinta de la melodía y del root. Se puede mantener el bajo mientras se mueve la melodía, mantener la melodía mientras se mueve el bajo, o hacer que una llegada preceda a la otra. La melodía puede restringir inversiones por el espacio disponible, pero no determina el bajo. El corpus puede enumerar movimiento contrario, similar, paralelo, pedal y trayectorias, pero no rankearlos universalmente ni predecir su efecto sin escucha.

## Melody ↔ Inversion / Voicing

Una voz superior fija puede limitar pitches y registro, y una inversión deseada puede entrar en conflicto con tesitura o conducción. La identidad armónica no basta para elegir sonoridad. Deben declararse bass, inversión, pitches exactos, registro, spacing, duplicaciones/omisiones y asignación de voces. La realización mínima o más cercana no es automáticamente la mejor; las convenciones de duplicación y voicing son dependientes de tradición y estilo.

## Arrival / Openness / Closure

La representación conjunta mantiene cuatro estados: `melodic_arrival`, `harmonic_arrival`, `formal_rhythmic_boundary` y `full_closure_judgment`. Son posibles llegada alineada, melodía primero, armonía primero, melodía llegada sobre loop, armonía llegada mientras la melodía continúa, o frontera formal sin llegada plena.

El conocimiento apoya la existencia de estas configuraciones y permite diagnosticar qué falta. No exige convergencia universal ni permite asignar pesos a sus indicios. El cierre completo requiere al menos contexto melódico, armónico, métrico/formal y de realización; puede además depender de arreglo y letra.

## Chord Membership / Non-Chord Classification

La pregunta correcta es «¿miembro respecto de qué armonía realizada o analítica, en qué ventana temporal, bajo qué marco, y con qué relación antes/después?». Membership es diagnóstico. No produce por sí solo estabilidad, tensión, calidad ni resolución obligatoria. `non-chord` tampoco significa error. La clasificación debe conservar incertidumbre cuando el marco, la conducción o el estilo no están determinados.

## Chromatic Interaction

Son posibles: melodía cromática sobre armonía persistente; melodía diatónica sobre armonía cromática; participación de la melodía en un cambio de colección; conservación de la colección previa; reinterpretación armónica de un pitch cromático; y cromatismo recurrente de loop. Cromático no implica tensión, emoción ni necesidad de armonía cromática. Un objetivo local puede ser sugerido sin que exista nuevo centro. Establecer, confirmar o fechar ese centro requiere RQ-HAR-007.

## Selection / Realization / Interaction Matrix

| Decisión | La melodía puede | La armonía puede | Resultado actual |
|---|---|---|---|
| selección con nota fija | constreñir pitches/lecturas | ofrecer varias relaciones | alternativas, sin ranking |
| selección con motivo corto | preservar invariantes | cambiar contexto o función | razonamiento con alcance |
| realización | reducir bajo/inversión/voicing | reinterpretar la sonoridad | diagnóstico + manipulación |
| timing | anticipar, sostener, callar | persistir, cambiar, revoicing | opciones separables |
| llegada | señalar objetivo melódico | reforzar o mantener apertura | cierre no deducible |
| cromatismo | conservar o cambiar colección | ofrecer varias lecturas | convergencia/escucha requerida |

## Candidate Coverage Matrix

La siguiente cobertura es trazabilidad, no reauditoría. Todos permanecen en estado candidato salvo el rechazo heredado.

| ID | dominio | readiness heredado | rol integrado / etapa | alcance y blocker |
|---|---|---|---|---|
| CAND-MEL-001 | melody | candidato | identidad/variación; material | alcance de transposición; no jerarquía |
| CAND-MEL-002 | melody | candidato | identidad; material | contorno no basta; mecanismo insuficiente |
| CAND-MEL-003 | melody | candidato | identidad; invariantes | detalle interválico contextual |
| CAND-MEL-004 | melody | candidato | invariantes | no jerarquía fija; ponderación bloqueada |
| CAND-MEL-005 | melody | candidato | contexto/selección | función melódica depende del marco |
| CAND-MEL-006 | melody | candidato | timing/variación | ritmo y acento no determinan efecto |
| CAND-MEL-007 | melody | candidato | repetición; objetivo | repetición exacta no garantiza percepción |
| CAND-MEL-008 | melody | candidato | llegada | final cambiado puede continuar; no cierre |
| CAND-MEL-009 | melody | candidato | variación/desarrollo | aplicación dependiente de material |
| CAND-MEL-010 | melody | candidato | repetición/variación | desarrollo no automático |
| CAND-MEL-011 | melody | candidato | loop/contexto | cambio textural no implica función |
| CAND-MEL-012 | melody | candidato | repetición | efecto no monotónico; sin medida |
| CAND-MEL-013 | melody | candidato | contorno/llegada | proximidad no fija preferencia |
| CAND-MEL-014 | melody | candidato | frase/llegada | indicios aditivos, sin peso |
| CAND-MEL-015 | melody | candidato | contorno | descriptivo, no norma |
| CAND-MEL-016 | melody | candidato | llegada | pico no equivale a clímax |
| CAND-MEL-017 | melody | candidato | llegada/cierre | descenso no equivale a cierre |
| CAND-MEL-018 | melody | **rechazado** | ninguna; debe permanecer excluido | registro seccional no verificado |
| CAND-MEL-019 | melody | candidato | registro/realización | desplazamiento tiene coste; sin ranking |
| CAND-MEL-020 | melody | candidato | tesitura/voicing | restricción habitable, no efecto estético |
| CAND-MEL-021 | melody | candidato | prominencia | rareza no certifica saliencia |
| CAND-MEL-022 | melody | candidato | contraste | contraste registral contextual |
| CAND-MEL-023 | melody | candidato | registro | altura no implica emoción |
| CAND-MEL-024 | melody | candidato | retorno | extremos y retorno no garantizan función |
| CAND-MEL-025 | melody | candidato | timing/llegada | métrica organiza, no determina armonía |
| CAND-MEL-026 | melody | candidato | anticipación/timing | onset puede divergir |
| CAND-MEL-027 | melody | candidato | timing | groove dependiente de contexto |
| CAND-MEL-028 | melody | candidato | llegada/silencio | alargamiento/silencio son opciones |
| CAND-MEL-029 | melody | candidato | silencio | función depende de contexto |
| CAND-MEL-030 | melody | candidato | densidad/continuación | no umbral universal |
| CAND-HAR-001 | harmony | sintetizado/auditado | centro/selección | recurrencia aporta evidencia, no certeza |
| CAND-HAR-002 | harmony | not ready | centro/bajo | sigue bloqueado; pesos con melodía faltan |
| CAND-HAR-003 | harmony | sintetizado/auditado | selección | consonancia no estabilidad |
| CAND-HAR-004 | harmony | sintetizado/auditado | timing | frecuencia no tonicidad |
| CAND-HAR-005 | harmony | not ready | timing/centro | duración/posición requieren confirmación |
| CAND-HAR-006 | harmony | sintetizado/auditado | colección/centro | centro modal sin dominante, alcance acotado |
| CAND-HAR-007 | harmony | candidato, RQ no iniciado | función/selección | candidato no equivale a RQ-HAR-007; modulación pendiente |
| CAND-HAR-008 | harmony | sintetizado/auditado | selección/relación | dominante-tónica acotado |
| CAND-HAR-009 | harmony | sintetizado/auditado | root/bajo | movimiento no basta |
| CAND-HAR-010 | harmony | sintetizado/auditado | centro | frecuencia no expectativa |
| CAND-HAR-011 | harmony | sintetizado/auditado | loop/selección | ciclo no sintaxis dirigida |
| CAND-HAR-012 | harmony | sintetizado/auditado | selección | dominante no tensión automática |
| CAND-HAR-013 | harmony | sintetizado/auditado | realización | tono común puede dar continuidad |
| CAND-HAR-014 | harmony | sintetizado/auditado | realización | distancia mínima no objetivo |
| CAND-HAR-015 | harmony | sintetizado/auditado | realización | tendencia acotada por tradición |
| CAND-HAR-016 | harmony | sintetizado/auditado | selección/realización | etiqueta subdetermina movimiento |
| CAND-HAR-017 | harmony | sintetizado/auditado | realización | planing depende de alcance |
| CAND-HAR-018 | harmony | sintetizado/auditado | persistencia | continuidad y función separadas |
| CAND-HAR-019 | harmony | not ready | registro/realización | equivalencia registral bloqueada |
| CAND-HAR-020 | harmony | sintetizado/auditado | realización | planing organiza sonoridad |
| CAND-HAR-021 | harmony | sintetizado/auditado | timing | ritmo armónico no es tempo |
| CAND-HAR-022 | harmony | sintetizado/auditado | timing | duración no importancia automática |
| CAND-HAR-023 | harmony | sintetizado/auditado | timing | aceleración acotada |
| CAND-HAR-024 | harmony | sintetizado/auditado | persistencia | superficie ≠ región |
| CAND-HAR-025 | harmony | sintetizado/auditado | persistencia | prolongación depende de marco |
| CAND-HAR-026 | harmony | sintetizado/auditado | loop/timing | estasis puede organizar |
| CAND-HAR-027 | harmony | sintetizado/auditado | llegada | cadencia es proceso contextual |
| CAND-HAR-028 | harmony | sintetizado/auditado | llegada/cierre | llegada tónica no cierre |
| CAND-HAR-029 | harmony | sintetizado/auditado | llegada | fuerza no ranking universal |
| CAND-HAR-030 | harmony | sintetizado/auditado | llegada | plagal/modal, alcance acotado |
| CAND-HAR-031 | harmony | sintetizado/auditado | loop | retorno no cadencia |
| CAND-HAR-032 | harmony | sintetizado/auditado | cierre | final no tónico posible |
| CAND-HAR-033 | harmony | sintetizado/auditado | cromatismo | tonicización/modulación separadas |
| CAND-HAR-034 | harmony | sintetizado/auditado | cromatismo | etiqueta secundaria no prueba tonicización |
| CAND-HAR-035 | harmony | sintetizado/auditado | colección | mezcla sin cambio de centro |
| CAND-HAR-036 | harmony | sintetizado/auditado | cromatismo | múltiples análisis |
| CAND-HAR-037 | harmony | sintetizado/auditado | cromatismo/realización | voice-leading no partida |
| CAND-HAR-038 | harmony | sintetizado/auditado | cromatismo | no proxy de tensión |
| CAND-HAR-039 | harmony | sintetizado/auditado | loop/colección | recurrencia puede organizar |
| CAND-HAR-040 | harmony | sintetizado/auditado | realización | símbolo no sonoridad |
| CAND-HAR-041 | harmony | sintetizado/auditado | bajo | root/bass son variables distintas |
| CAND-HAR-042 | harmony | sintetizado/auditado | inversión | jerarquía dependiente de tradición |
| CAND-HAR-043 | harmony | sintetizado/auditado | voicing | pitch-class equivalente no idéntico |
| CAND-HAR-044 | harmony | sintetizado/auditado | realización | duplicación/omisión estilísticas |
| CAND-HAR-045 | harmony | sintetizado/auditado | registro/spacing | sonoridad no función |
| CAND-HAR-046 | harmony | posible con alcance | interacción | pertenencia no estabilidad |
| CAND-HAR-047 | harmony | posible con alcance | selección | melodía fija subdetermina |
| CAND-HAR-048 | harmony | posible con alcance | reinterpretación | analítica no perceptiva |
| CAND-HAR-049 | harmony | posible con alcance | realización | pluralidad bajo melodía |
| CAND-HAR-050 | harmony | posible con alcance | llegada | divergencia posible, cierre incierto |
| CAND-HAR-051 | harmony | posible con alcance | repetición | cambio armónico no desarrollo |
| CAND-HAR-052 | harmony | posible con alcance | clasificación | marco/tiempo/conducción necesarios |

## Interaction-Specific Candidate Map

| Familia | Candidatos combinados | Qué permite afirmar sin crear una regla nueva |
|---|---|---|
| identidad | MEL-001–005, MEL-007, HAR-046–049 | declarar invariantes y alternativas de lectura |
| repetición/variación | MEL-006–012, HAR-051 | conservar identidad mientras cambia contexto; desarrollo queda abierto |
| contorno/arribo | MEL-013–017, MEL-025, MEL-028, HAR-027–032, HAR-050 | separar indicios de llegada y cierre |
| registro | MEL-019–024, HAR-019, HAR-045, HAR-049 | tesitura constriñe realización; no rankea voicing |
| ritmo/silencio | MEL-025–030, HAR-021–026 | timing separado; sin sincronización por defecto |
| centro/función | HAR-001–009, MEL-005 | contexto y relación pueden orientar; nuevo centro requiere HAR-007 |
| continuidad/voice-leading | HAR-013–020, HAR-040–045 | explorar sonoridades y conexiones, no elegir universalmente |
| cromatismo | HAR-033–039, HAR-046, HAR-048, HAR-052 | mantener varias interpretaciones y declarar marco |
| interfaz directa | HAR-046–052 | diagnóstico interactional específico; sin promoción |

Coexistencia no equivale a claim combinado: cada combinación necesita mantener su alcance.

## Composition-Action Ladder

| Problema | acción actual |
|---|---|
| declarar invariantes, separar capas y registrar timing | ACTIONABLE NOW |
| enumerar selecciones bajo una melodía fija | ACTIONABLE WITH SCOPE |
| generar realizaciones físicamente admisibles | ACTIONABLE WITH SCOPE |
| clasificar membership y alternativas analíticas | DIAGNOSTIC ONLY |
| rankear bajo/inversión/voicing | BLOCKED |
| predecir continuidad, tensión, desarrollo o cierre percibido | BLOCKED |
| establecer un nuevo centro | BLOCKED: RQ-HAR-007 |

## Diagnostic vs Generative Power

Las etiquetas son cualitativas de integración, no métricas empíricas.

| Problema | diagnóstico | generativo | límite |
|---|---|---|---|
| armonía bajo nota fija | HIGH | LOW | varias lecturas, sin ranking |
| armonía bajo motivo corto | HIGH | LOW-MEDIUM | invariantes y alternativas |
| elegir bajo | MEDIUM | LOW | root no es bajo; sin pesos |
| elegir inversión | MEDIUM | LOW | restricción, no preferencia general |
| elegir voicing | MEDIUM | LOW | realiza, pero no rankea |
| chord/non-chord | HIGH | LOW | membership no estabilidad |
| reharmonizar repetición | MEDIUM-HIGH | LOW-MEDIUM | cambio no desarrollo |
| timing melódico/armónico | HIGH | LOW | describe divergencias |
| coordinar arrivals | MEDIUM-HIGH | LOW-MEDIUM | convergencia no obligatoria |
| cromatismo melódico | HIGH | LOW-MEDIUM | lecturas múltiples; HAR-007 si nuevo centro |
| identidad bajo cambio armónico | MEDIUM-HIGH | LOW-MEDIUM | identidad declarada, percepción incierta |

La integración sabe manipular más de lo que sabe escoger bien.

## Positive Composition Test

**A — E4 tenida.** Puede conservar E4 y generar varios soportes; puede explicar pertenencia, bajo, inversión, realización y timing como decisiones distintas. Puede verificar restricciones. No puede elegir mejor soporte, predecir continuidad ni medir reinterpretación perceptiva: `CAN REASON WITH SCOPE` hasta realización; `PARTIALLY` para efecto.

**B — Motivo repetido.** Puede mantener invariantes y cambiar bajo, voicing, identidad o función armónica. Puede llamar a la operación variación contextual, no desarrollo. `CAN REASON WITH SCOPE`.

**C — Llegada melódica.** Puede reforzarla o conservar apertura y listar convergencias/divergencias. No puede determinar cierre sin forma, métrica, arreglo y escucha. `CAN REASON WITH SCOPE`.

**D — Loop + hook.** Puede mantener ciclo, variar bajo/voicing o cambiar nivel armónico, y declarar qué permanece. Diferencia seccional perceptiva y mejor operación no están justificadas. `CAN REASON WITH SCOPE`.

**E — Pitch cromático.** Puede mantener armonía, clasificar non-chord, reinterpretar o proponer colección/armonía cromática. No puede decidir umbral de tonicización/modulación; nuevo centro activa HAR-007. `PARTIALLY`.

**F — Realización fija.** Puede producir alternativas compatibles con E4, tesitura, spacing y conducción declarados. No puede rankear bass/inversion/inner voices. `PARTIALLY` para manipulación, `CANNOT YET` para elección ponderada.

## Composer Capability Check

| Decisión | capacidad | blocker |
|---|---|---|
| armonizar una nota | CAN REASON WITH SCOPE | subdeterminación |
| armonizar motivo corto | CAN REASON WITH SCOPE | invariantes y estilo |
| reharmonizar repetición | CAN REASON WITH SCOPE | efecto no medido |
| conservar melodía/cambiar bajo | PARTIALLY | sin ranking bajo–melodía |
| conservar bajo/cambiar armonía | PARTIALLY | sonoridad y centro |
| realizar armonía bajo melodía | PARTIALLY | no criterio ponderado |
| alinear/divergir ritmos | CAN REASON WITH SCOPE | no colocación normativa |
| reforzar una llegada | CAN REASON WITH SCOPE | cierre requiere dominios |
| evitar reforzarla | CAN REASON WITH SCOPE | efecto perceptivo incierto |
| soportar hook en loop | CAN REASON WITH SCOPE | diferencia seccional |
| evento cromático | PARTIALLY | ambigüedad; HAR-007 |
| final cambiado | CAN REASON WITH SCOPE | final ≠ cierre |
| coordinar cierre | CANNOT YET | forma, métrica, arreglo, prosodia |

## Interaction Tradeoff Matrix

| Conflicto | clasificación | lectura segura |
|---|---|---|
| identidad melódica / reinterpretación | SUPPORTED TRADEOFF | conservar invariantes puede limitar lecturas |
| common tone literal / trayectoria de bajo | SUPPORTED TRADEOFF | ambas capas pueden divergir |
| registro fijo / flexibilidad de voicing | SUPPORTED TRADEOFF | tesitura constriñe, no decide |
| inversión / top-line | SUPPORTED TRADEOFF | top-line no determina inversión |
| llegada armónica / continuación melódica | SUPPORTED TRADEOFF | pueden divergir |
| llegada melódica / apertura armónica | SUPPORTED TRADEOFF | llegada no exige cierre |
| repetición / cambio armónico | SUPPORTED TRADEOFF | cambio no desarrollo |
| centro / cromatismo | PROVISIONAL | colección puede cambiar sin centro |
| loop / diferenciación seccional | PLAUSIBLE / UNESTABLISHED | operaciones disponibles, efecto no medido |

## Cross-Domain Dependencies

Form bloquea jerarquía de llegadas y función seccional; mejora el contexto de frase. Rhythm/meter bloquea pesos de onset, duración y acento; el timing local puede proceder. Arrangement/production bloquea fusión, streaming, prominencia y efecto de voicing; la estructura abstracta puede proceder. Lyrics/prosody bloquea decisiones cuando la melodía sirve texto; puede ignorarse solo en escenarios abstractos. Genre bloquea transferencias estilísticas; las formulaciones generales deben permanecer acotadas. Modulation/RQ-HAR-007 bloquea confirmar centro nuevo, frontera tonicización/modulación, pivotes, reinterpreación con cambio de centro y retorno; la selección local con centro asumido puede proceder.

## RQ-HAR-007 Dependency Map

HAR-007 no es necesario para toda cromaticidad. Se vuelve necesario al seleccionar un nuevo centro establecido, decidir cuándo una tonicización se convierte en modulación, confirmar un cambio de centro, evaluar confirmación melódica del nuevo centro, analizar pivotes/reinterpretaciones que fundan ese centro o explicar el retorno al centro original. No debe absorber los casos de mezcla, cromatismo de conducción o loop sin salida demostrada.

## Initial-Idea / Initial-Progression Gaps

La coordinación actual no compensa el gap de Melody sobre construcción de la idea inicial: puede tomar material dado y trabajar con él, pero no explica suficientemente cómo inventar un motivo inicial con intención. Harmony tampoco inventa una progresión inicial en sentido fuerte; puede seleccionar entre alternativas dentro de un contexto u objetivo asumido. Por tanto, el sistema es más competente como diagnosticador y transformador contextual que como compositor desde cero.

## Provisional Joint Composition Workflow

| etapa | estado | razón |
|---|---|---|
| establecer/asumir material o contexto | PROVISIONAL | la invención inicial sigue bloqueada |
| identificar invariantes | SUPPORTED | variables explícitas |
| identificar centro/colección/región | SUPPORTED WITH SCOPE | evidencia contextual, no certeza |
| elegir objetivo local | PROVISIONAL | objetivo artístico externo |
| enumerar selecciones | SUPPORTED WITH SCOPE | subdeterminación explícita |
| filtrar por restricciones | SUPPORTED WITH SCOPE | no convierte restricción en determinación |
| realizar candidatos | SUPPORTED WITH SCOPE | sonoridad separada de identidad |
| inspeccionar bajo/voice-leading/timing | SUPPORTED | diagnóstico estructural |
| inspeccionar llegada/apertura | SUPPORTED WITH SCOPE | cierre no automático |
| evaluar conflictos cross-domain | SUPPORTED | dependencias visibles |
| escuchar y revisar | SUPPORTED / necesario | ranking perceptivo no disponible |

El flujo debe iterar entre selección, realización y timing cuando una realización revele que la selección no satisface el objetivo.

## Positive Knowledge vs Ranking Knowledge

Conocer que existen varias operaciones viables, sus condiciones, variables separables y tradeoffs es conocimiento compositivo positivo. No equivale a saber cuál alternativa es mejor. La integración ofrece procedimientos para generar y diagnosticar candidatos, pero la elección final depende de intención, contexto, tradición y escucha humana cuando la evidencia no rankea.

## Integrated Anti-Rules

| No asumir | Reemplazo seguro |
|---|---|
| nota→acorde | declarar objetivo, marco, ventana temporal y alternativas |
| acorde→notas permitidas | examinar función, conducción, realización y estilo |
| chord tone = estable/bueno | separar membership de estabilidad y efecto |
| non-chord = tensión/error | clasificar relación temporal y contextual |
| tónica melódica exige tónica | tratarla como evidencia posible, no obligación |
| cambio armónico = desarrollo | distinguir contexto cambiado de desarrollo perceptivo |
| misma melodía exige misma armonía | conservar invariantes y permitir recontextualización |
| V–I requerido para cierre | analizar llegada y cierre con contexto |
| melodía siempre top voice | declarar asignación de voces |
| bass = root | mantener variables separadas |
| mínimo movimiento = mejor | comparar objetivos de conducción y sonoridad |
| cromatismo exige armonía cromática | conservar múltiples lecturas |
| arrivals alineadas = closure | registrar cuatro estados y no inferir convergencia |

## Unsupported / Blocked Knowledge

No hay ponderación entre indicios de melodía, bajo, duración, registro y colección; no hay dosis→efecto para repetición, spacing o registro; no hay jerarquía universal de invariantes, voicings o cadencias; no hay predicción perceptiva robusta de reinterpretación, desarrollo o cierre; no hay técnica general para escoger bajo, inversión o voicing; no hay solución de modulación; no hay construcción inicial de motivo ni progresión.

## Joint Manual Readiness

**NO**, en sentido de promoción. Existe un esqueleto coherente para enseñar un flujo de diagnóstico y decisión con alcance, pero faltan ranking, percepción, límites formales y construcción inicial. Puede servir como integración de investigación para revisión, no como conocimiento general aprobado.

## Joint Rule Readiness

**NO**. Algunas comprobaciones estructurales podrían ser machine-checkable (pitch fijo, tesitura declarada, onset, pertenencia bajo un marco explícito), pero no constituyen reglas de calidad ni de selección. No crear YAML ni rule engine a partir de este documento.

## Highest-Leverage Next Research

| opción | leverage | riesgo/prerrequisito |
|---|---|---|
| A. RQ-HAR-007 | alto para centros nuevos | puede acumular teoría sin resolver invención |
| B. idea/motivo inicial | alto para capacidad generativa | requiere definir qué significa construir intención |
| C. FORM | alto a nivel canción | muchas decisiones actuales ya están bloqueadas por forma |
| D. RHYTHM/METER | alto para timing | profundiza una interfaz ya diagnosticada |
| E. gap conjunto Melody+Harmony | alto si se formula como ranking/percepción | debe evitar repetir HAR-009 |

La comparación favorece **B**, porque desbloquea el punto en que el sistema deja de operar solo sobre material ya dado y evita acumular taxonomía antes de probar capacidad generativa. HAR-007 sigue siendo importante, pero no es automáticamente el siguiente paso.

## Recommended Next Step

**Iniciar una investigación específica sobre la construcción de la idea melódica inicial / motivo inicial**, definiendo primero qué decisiones, invariantes y objetivos deben considerarse y qué parte podría evaluarse sin confundir descripción con calidad. No iniciar esa investigación automáticamente en este documento.

## Final Report

### What I changed

Se creó únicamente este archivo. No se modificaron las integraciones históricas, RQ, candidatos, manuales, reglas, géneros, experimentos ni `music-engine`.

### Joint interaction architecture

La arquitectura respaldada es iterativa: material e intención melódica ↔ contexto y selección armónica ↔ realización ↔ timing/llegada. La melodía normalmente constriñe o sugiere; rara vez determina. La armonía puede reinterpretar analíticamente, pero no prueba percepción.

### Melody constraints on Harmony

Pitch, ritmo, registro, contorno, identidad y llegada declarados pueden reducir selecciones o realizaciones. No determinan acorde, root, bajo, inversión ni cierre.

### Harmony constraints on Melody

Centro, colección, sonoridad, bajo, timing y llegada ofrecen marcos de interpretación y restricciones locales. No convierten chord membership en estabilidad ni obligan a que la melodía cambie o siga los acordes.

### Selection vs realization under melody

La selección puede enumerarse y filtrarse con alcance; la realización puede manipularse y comprobarse estructuralmente. Ninguna de las dos puede rankearse de forma general bajo una melodía fija.

### Main interaction principles that survived

Separar selección/realización; separar root/bass; distinguir membership/estabilidad; mantener invariantes explícitos; separar timing y arrivals; conservar interpretaciones alternativas; no inferir percepción desde análisis.

### Main principles that remain only provisional

Qué invariantes dominan identidad, qué soporte mejora una llegada, cuándo el cambio armónico produce contraste o desarrollo, cómo pesa el bajo frente a la melodía y qué cromatismo se percibe como reinterpretación.

### Positive compositional operations available

Conservar material, cambiar contexto, mantener o mover bajo, elegir una sonoridad compatible, variar timing, sostener loop, cambiar final, proponer lecturas cromáticas y alinear o divergir llegadas.

### Operations that can be manipulated but not ranked

Bajo, inversión, voicing, spacing, duplicación, sonoridad equivalente, soporte de nota tenida, grado de cambio armónico y sincronización de llegadas.

### Diagnostic vs generative power

El diagnóstico es medio-alto para separar capas, alternativas y errores de inferencia. La generación es baja a media: produce opciones con alcance, pero no decide bien entre ellas.

### Positive Composition Test

Los escenarios A–F muestran que el sistema puede razonar con alcance sobre restricciones y alternativas, pero queda parcial o bloqueado en ranking perceptivo, cierre, elección de realización y cambio de centro.

### Composer Capability Check

Puede razonar con alcance sobre armonizar, rearmonizar, loops, timing y llegadas. Solo parcialmente sobre elección de bajo, voicing y cromatismo. Todavía no puede coordinar cierre completo ni crear el material inicial con intención explicada.

### Candidate coverage

`CAND-MEL-001–030 = 30/30` representados; `CAND-HAR-001–052 = 52/52` representados. `CAND-MEL-018` permanece rechazado. No se alteró readiness.

### Cross-domain blockers

Form, rhythm/meter, arrangement/production, lyrics/prosody y genre bloquean pesos y efectos situados. Modulation queda en RQ-HAR-007. La brecha de idea inicial permanece en Melody.

### RQ-HAR-007 dependency

Solo se activa cuando la pregunta requiere establecer, confirmar, delimitar o retornar desde un centro nuevo; no para todo cromatismo o rearmonización local.

### Initial melodic-idea / progression gaps

La integración no inventa el motivo inicial ni una progresión inicial: opera sobre material/contexto asumidos. La coordinación Melody+Harmony no compensa ese déficit.

### Joint manual readiness

**NO.**

### Joint rule readiness

**NO.**

### Highest-leverage next research comparison

Se compararon HAR-007, idea melódica inicial, FORM, RHYTHM/METER y un gap conjunto. La idea melódica inicial ofrece mayor leverage generativo y menor riesgo de seguir acumulando teoría sin material compositivo.

### Recommended next research step

Investigar la **construcción de la idea melódica inicial / motivo inicial**. No comenzar esa investigación automáticamente.
