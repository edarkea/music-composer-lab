# Melody Foundations — Primera integración (v0)

## Estado y alcance de este documento

- Tipo: capa de integración y auditoría entre candidatos de investigación y eventual promoción a `manual/`. NO es conocimiento aprobado de `manual/` ni regla de `rules/`.
- Cubre: RQ-MEL-001 (SYNTHESIZED), RQ-MEL-002 (SYNTHESIZED), RQ-MEL-003 (SYNTHESIZED), RQ-MEL-005 (SYNTHESIZED), RQ-MEL-006 (SYNTHESIZED); RQ-MEL-004 (DEFERRED, sin evidencia nueva); EXP-001 (evidencia exploratoria propia, n=1); EXP-002 (PAUSADO, solo diseño, sin resultados); CAND-MEL-001–030 incluyendo CAND-MEL-018 rechazado (ID preservado).
- No se ha realizado investigación externa nueva, ni experimentos, ni composición de ejemplos, ni codificación de reglas. Toda pregunta sin respuesta en la evidencia actual se marca como GAP.
- Scope general del proyecto: música popular tonal/modal occidental y tradiciones estrechamente relacionadas. Nada de lo aquí integrado se afirma fuera de ese ámbito. Oyentes enculturados occidentales en toda la evidencia externa.
- Idioma: contenido humano en español; identificadores y claves técnicas en inglés.
- No se modifica ningún estado `status` de candidatos, ni `manual/`, ni `rules/`, ni `genres/`, ni EXP-001/EXP-002.

## Mapa del flujo decisional adoptado

Se organiza por problema compositivo, no por tema académico. El flujo aprobado como hipótesis de trabajo es:

MATERIAL (dato de partida, no generado por nuestro conocimiento)
→ ESTABLISH (hacer disponible la idea)
→ CONTINUE (seguir sin abandonar identidad)
→ VARY (variar conservando parentesco)
→ DEVELOP (transformar con dirección formal — solo en tradición delimitada)
→ CONTRAST (diferenciar preservando continuidad parcial)
→ APPROACH ARRIVAL (acercarse a una meta — contribución melódica parcial)
→ CLOSE / REMAIN OPEN (cerrar o dejar abierto — nunca solo con melodía)
→ RETURN / REUSE (retornar o reutilizar a escala de frase o sección)

No se fuerza una secuencia obligatoria: ESTABLISH puede lograrse por repetición exacta o por statement–response; CONTINUE y VARY se solapan; DEVELOP solo aplica en su tradición; CONTRAST a escala seccional requiere dominios cruzados; CLOSE casi siempre requiere armonía. El hallazgo estructural de esta integración es que sabemos mucho más de TRANSFORMAR material existente que de INVENTAR la primera idea (ver sección 1 y GAP-01).

## 1. Crear material melódico inicial

Pregunta: ¿qué puede decidir actualmente una IA sobre relaciones de pitch, contorno, registro, rango, organización rítmica, onsets, duraciones, silencio y relación métrica al inventar el primer motivo?

Respuesta: CASI NADA con apoyo directo.

- Ningún candidato describe una estrategia generativa de motivo inicial (qué pitches elegir, qué contorno inicial, qué ritmo inicial, qué rango). CAND-MEL-003 y CAND-MEL-005 hablan de detalle interválico y función tonal pero con `possible_action` vacío y apoyo indirecto: no generan material.
- CAND-MEL-007 presupone un motivo ya enunciado ("enunciar el motivo y repetirlo"): no dice cómo inventarlo.
- CAND-MEL-013 (proximidad/reversión) opera tono-a-tono una vez existe un intervalo implicativo; no construye un motivo completo.
- CAND-MEL-015 usa el arco como forma disponible con precedente distribucional folk, pero explícitamente sin prescripción: no es una estrategia de invención.
- RQ-MEL-006 aporta vocabulario temporal preciso (onset, duration, IOI, accent, metric placement, density, silence) pero ninguna receta de organización inicial.

Conclusión de integración: el sistema actual NO dispone de estrategia generativa apoyada para la primera idea. Esto es un GAP central (GAP-01), no un fracaso: delimita que la capacidad real está en ESTABLECER, CONTINUAR, VARIAR y REUTILIZAR, no en INVENTAR. Cualquier futura IA que deba proponer el primer motivo operará fuera del conocimiento actual o por preferencia artística explícita.

Estado: UNSUPPORTED (estrategia generativa de motivo inicial).

## 2. Establecer una idea (ESTABLISH)

Problema: hacer que una idea esté disponible y reconocible para uso posterior.

Lo que sí sabemos:

- La repetición exacta o inmediata en la presentación es una operación disponible con doble apoyo: pedagogía compositiva (Schoenberg: la repetición construye el tema antes de desarrollar) y percepción (Margulis 2012: detección de repeticiones; Margulis 2013: agrado con repetición insertada en música no familiar). CAND-MEL-007.
- La función exacta está delimitada: lo medido es detección y agrado, NO reconocimiento de identidad en sentido estricto ni expectativa de retorno (esta última es extensión teórica de Huron, marco parcial). Por eso la formulación honesta es débil: "puede usarse para establecer o reforzar", no "establece identidad garantizada".
- Qué debe permanecer estable: todo o casi todo (pitch, ritmo, registro) salvo posición formal. Cambiar de registro ya penaliza parcialmente el parentesco (EXP-001 B=3, no 4; causas no separadas).
- Alternativa documentada desde el inicio: statement–response (variar ya el final, CAND-MEL-008), práctica clásica con segunda aparición ya variada. No hay norma de "repetir N veces antes de variar": contradicción entre tradiciones (clásica varía pronto, loop sostiene muchas repeticiones). Ningún número está justificado.

Lo que NO sabemos: cuántas repeticiones según función y tradición; si el oyente registra cada repetición igual con familiaridad creciente (Margulis 2012 sugiere desplazamiento atencional: lo que cuenta como repetición cambia); umbral donde la variación se vuelve necesaria.

Estado: operación de repetición exacta/inmediata como establecimiento: PROVISIONAL (heurística débil justificada). Dosis de repetición: UNSUPPORTED (ningún número). Expectativa de retorno como efecto medido: UNSUPPORTED.

## 3. Continuar sin abandonar identidad (CONTINUE)

Problema: seguir adelante manteniendo el ancla.

Operaciones disponibles (AVAILABLE OPERATION) y su función con apoyo (SUPPORTED FUNCTION):

- Repetición exacta continuada (refuerzo). Operación: SUPPORTED como hecho estructural; función de establecimiento: PROVISIONAL.
- Transposición exacta pequeña (+2 st medido). Operación disponible; función de conservar parentesco con posible penalización: PROVISIONAL (CAND-MEL-001/019; un dato propio n=1 + reconocimiento en laboratorio). No extender a octavas ni a función seccional.
- Final cambiado (changed ending): conservar arranque, cambiar cierre. Operación descrita sistemáticamente en pedagogía clásica; función de continuación: TRADITION_SPECIFIC (sentence clásica) + CROSS_DOMAIN_REQUIRED (la dirección real la califica la armonía). CAND-MEL-008.
- Variación rítmica con pitches intactos (redistribución de duraciones/onsets). Operación disponible; un dato propio de parentesco máximo (EXP-001 E=4, n=1); controlar estructura acentual como dimensión propia: PROVISIONAL (CAND-MEL-006 matizado). Cambiar pitches puede reponderar acentos aunque el IOI se conserve (inferencia desde Müllensiefen, no medida directa).
- Secuencia (repetición del motivo por pasos tonales o reales). Operación pedagógica disponible; función direccional/acumulativa: TRADITION_SPECIFIC, riesgo de mecanicismo sin punto de llegada.
- Fragmentación + liquidación hacia cadencia. Operación y función ligadas SOLO en marco clásico; fuera de él: TRADITION_SPECIFIC + CROSS_DOMAIN_REQUIRED (requiere aceleración armónica). CAND-MEL-009. Fragmentar sin liquidar ni coordinar armonía es corte sin dirección (failure mode).
- Desplazamiento registral / métrico, ornamentación, extensión, reducción, recombinación, omisión: operaciones descriptivamente disponibles; funciones respectivas: en su mayoría UNSUPPORTED o PROVISIONAL débil (matriz RQ-MEL-002; casi todo `uncertain` en efecto). El desplazamiento métrico altera estructura acentual y arriesga más parentesco que cambios internos de duración (apoyo parcial Jones & Ralston).

Regla de trabajo: separar siempre OPERACIÓN (observable en partitura) de FUNCIÓN (papel en contexto). La misma operación cumple funciones distintas según posición formal.

## 4. Variación (VARY)

Mapa preserve/change con lo que sabemos de preservación de identidad (desde RQ-MEL-001; sin jerarquía universal de rasgos):

Preservar (palancas candidatas):
- pitches exactos (EXP-001 E=4 con ritmo cambiado; n=1) — palanca fuerte pero puntual.
- relaciones internas vía transposición exacta (EXP-001 B=3; reconocimiento en laboratorio) — PROVISIONAL.
- contorno/direcciones (rasgo relacional robusto y temprano, Dowling; Morrongiello/Trehub) pero INSUFICIENTE por sí solo (EXP-001 C=2 con contorno+ritmo intactos; Dowling: misma vs. mismo-contorno confundibles bajo transposición) — SUPPORTED como conocimiento negativo.
- ritmo/patrón temporal (peso alto pero condicional: Prince Exp.1 ritmo primero, Exp.2 contorno primero con contexto armónico previo) — sin jerarquía fija: SUPPORTED como anti-jerarquía (CAND-MEL-004).
- acento/posición métrica (Jones & Ralston; Müllensiefen; Palmer & Krumhansl 1990) — dimensión propia a controlar: PROVISIONAL.
- registro (la transposición lo desplaza necesariamente; penalización parcial no separada) — PROVISIONAL.
- función tonal/grados (representación jerárquica Krumhansl; distancia tonal Bartlett & Dowling) — apoyo indirecto, sin test directo de misma idea: PROVISIONAL como sensibilidad, UNSUPPORTED como acción concreta (CAND-MEL-005, action vacío).

Cambiar (y su riesgo):
- nivel de pitch (transposición pequeña): riesgo bajo-moderado, PROVISIONAL.
- tamaño interválico: en material familiar pesa más (Dowling & Bartlett); cambiar varias magnitudes puede degradar a 2/4 aun con contorno+ritmo intactos (EXP-001 C; confundido con cambio modal) — PROVISIONAL.
- final (ending): riesgo controlable si se conserva arranque; la dirección depende de armonía — TRADITION_SPECIFIC + CROSS_DOMAIN_REQUIRED.
- duraciones/onsets: riesgo bajo si pitches intactos en la realización medida; riesgo alto si se altera estructura acentual — PROVISIONAL.
- colocación métrica: riesgo alto (cambia función y parentesco) — PROVISIONAL (hipótesis por coherencia teórica).
- registro amplio/octava: sin apoyo incorporado — UNSUPPORTED.

NO crear jerarquía universal de rasgos. La ponderación depende de estabilidad temporal, contexto tonal previo, tarea (similitud vs. discriminación vs. misma idea), experiencia/edad y familiaridad. CAND-MEL-004 es la guarda metodológica de toda esta sección.

## 5. Desarrollo (DEVELOP)

Pregunta: ¿qué apoya convertir material existente en material ulterior con dirección?

- Variación: reaparición con parte conservada y parte modificada, parentesco reconocible. Apoyo: el de RQ-MEL-001.
- Desarrollo (sentido schoenbergiano/Frisch): cadena de transformaciones donde cada forma deriva de la anterior, con función formal de continuación o crecimiento. Estatus: THEORY dentro de la tradición analítica schoenbergiana y repertorio centroeuropeo del XIX (Brahms). Transferencia al pop: hipótesis sin verificar. Correlato perceptivo (reconocer que B desarrolla A a lo largo de una pieza): GAP central, sin medida. CAND-MEL-010 con `possible_action` vacío.
- Continuación formal (sentido capliniano): fase con fragmentación + liquidación + aceleración armónica hacia cadencia. Estatus: THEORY en repertorio Haydn/Mozart/Beethoven instrumental. Único marco que liga operaciones con función sistemáticamente. No importar vocabulario ("liquidación", "continuation") al pop sin verificar. CAND-MEL-009.

Mantener explícito el scope Schoenberg/Caplin. No convertir developing variation en regla universal de composición. En loop-based music la no-evolución melódica es virtud (Middleton/Butler), no defecto: contradicción de valores estéticos entre tradiciones, no desacuerdo factual.

Estado: desarrollo como concepto analítico en su tradición: TRADITION_SPECIFIC. Desarrollo como efecto percibido o receta pop: UNSUPPORTED.

## 6. Contraste (CONTRAST)

Problema: diferenciar preservando continuidad parcial.

Dimensiones deliberadamente cambiables (operaciones): pitch, contorno, registro, rango, patrón rítmico, colocación métrica, densidad, silencio. Todas disponibles como operaciones; NINGUNA con efecto de contraste percibido medido aisladamente.

Distinguir diferenciación estructural (cambiar una dimensión en la partitura) de contraste percibido (el oyente registra diferencia funcional). Lo segundo no está medido para ninguna dimensión melódica aislada.

Lo más sólido a escala seccional: el cambio registral como UN marcador entre varios (haz: dinámica, textura/densidad, ritmo armónico, letra, subida vocal), estrategia pop/rock a comprobar por escucha, nunca hecho poblacional. CAND-MEL-022: GENRE_SPECIFIC + CROSS_DOMAIN_REQUIRED. CAND-MEL-018 (coros sistemáticamente más altos) permanece RECHAZADO; si un futuro corpus confirma elevación, se creará ID nuevo, nunca se rehabilita el 018.

Estado general de contraste melódico aislado: UNSUPPORTED como efecto garantizado; PROVISIONAL/GENRE_SPECIFIC como estrategia coordinada con otros dominios.

## 7. Continuación de frase (PHRASE CONTINUATION)

Lo conocido, por estatus:

- SUPPORTED: nada como receta positiva. Lo más cercano a sólido es negativo (qué NO asumir).
- PROVISIONAL: proximidad y reversión post-salto como aceptabilidad local tono-a-tono (Schellenberg; simplificación en dos factores; record primario parcial), con lectura alternativa por tesitura coexistente (von Hippel & Huron). CAND-MEL-013. No es función de frase, solo continuación local aceptable.
- PROVISIONAL: fraseo aditivo pitch+tiempo (Palmer & Krumhansl 1987, repertorio clásico): coordinar contorno con timing y armonía; el contorno NO fue aislado como variable. CAND-MEL-014.
- PROVISIONAL: densidad creciente solo con marco coordinado (Caplin clásico o groove global sin traslación a melodía). Aislada: sin efecto establecido. CAND-MEL-030 (action vacío).
- TRADITION_SPECIFIC: fragmentación/liquidación clásica; finales cambiados clásicos.
- UNSUPPORTED: funciones perceptivas separadas por operación rítmica o de contorno; transferencia Caplin-rítmica al pop; equivalencia de definiciones de síncopa.

No colapsar expectativa local de continuación (tono-a-tono, Schellenberg) con continuación formal (función de frase, Caplin). Son niveles distintos.

## 8. Llegada (ARRIVAL)

Qué puede aportar la melodía a una llegada: pico registral, duración sostenida, colocación métrica fuerte, cambio de densidad, silencio previo/posterior, cambio de contorno/giro, tono sostenido. Estado de cada aporte aislado: hipótesis sin medida de "llegada" o contribución parcial a coordinar.

- Pico registral: contribuye a prominencia solo con soporte rítmico/armónico/dinámico y preparación (Eitan, analítico sin medida perceptiva). CAND-MEL-016.
- Duración/sustain: marca por acento agógico; sin medida de llegada.
- Colocación métrica fuerte: congruente con expectativa (Palmer & Krumhansl 1990), no suficiente.
- Cambio de dirección (giro): saliente analíticamente; rol dependiente de contexto.
- Densidad/silencio: sin medida de llegada aislada.

Requieren otro dominio: armonía (llegada armónica, RQ-MEL-007); ritmo/metro (beat fuerte, duración); dinámica (intensidad); forma (posición: mismo evento significa distinto según dónde cae); arreglo (capas que reubican el espacio).

No producir receta de llegada. Estado global: CROSS_DOMAIN_REQUIRED; cada aporte melódico aislado: PROVISIONAL o UNSUPPORTED.

## 9. Cierre / apertura (CLOSURE / OPENNESS)

Integrado desde CAND-MEL-017 (heurística), CAND-MEL-028 (hipótesis rítmica), CAND-MEL-014 (aditividad), CAND-MEL-024 (retorno tras extremo, opción local):

- El descenso de superficie NO es necesario ni suficiente para el cierre. Distribucionalmente frecuente (folk, últimas frases) y fondo descendente schenkeriano (no audible como prescripción de superficie), pero existen ascensos terminales expresivos. Estado del anti-mapeo: SUPPORTED como conocimiento negativo (convergencia teórica + aditividad medida).
- Duración final alargada + silencio post-evento CONTRIBUYEN como condición coordinada (Kragness & Trainor: demora en límites, producción; Margulis MP: silencio post-cierre tonal menos tenso y más rápido de detectar). Ninguno necesario ni suficiente; la armonía probablemente decide. CAND-MEL-028: PROVISIONAL + CROSS_DOMAIN_REQUIRED.
- Posición métrica fuerte: congruente, no suficiente.
- Retorno registral / settling / contracción: hipótesis analítica sin medida. CAND-MEL-024: movimiento interior tras extremo como opción local, no obligación.
- Cierre melódico sin cierre armónico: como máximo cierre parcial (hipótesis).

Qué NO debe asumir una IA al cerrar (conocimiento negativo valioso):

1. Que descender cierra (puede cerrar con armonía irresuelta pendiente; puede no cerrar aunque descienda).
2. Que alargar o callar cierra por sí solo.
3. Que el pitch máximo o la posición fuerte cierran por sí solos.
4. Que el fondo schenkeriano prescribe el contorno de superficie.
5. Que un final alto es automáticamente abierto ni uno bajo automáticamente cerrado (la función abierta del ascenso terminal concreto no está medida; no prescribirla tampoco).

## 10. Decisiones de registro y rango (REGISTER / RANGE)

Desde RQ-MEL-005, separando tres niveles siempre:

- PHYSICAL (restricción): voces e instrumentos tienen rangos finitos y tesituras cómodas; el esfuerzo crece con la altura; existen registros y transiciones con cambio de color. Tesitura habitable vs. rango nominal: escribir picos alcanzables con tesitura inhabitable es fallo físico. CAND-MEL-020 (núcleo físico): SUPPORTED como heurística física genérica (límites concretos siempre provisionales y por intérprete/estilo). No derivar estética de lo físico.
- PERCEPTUAL (saliencia): altura absoluta sola NO determina prominencia (Ilie & Thompson: efectos interactivos y opuestos por dominio; Eitan: picos con configuración; Bregman: streaming ≠ prominencia). Formulación débil: extremidad relativa + configuración contextual PUEDEN contribuir junto a ritmo, dinámica, armonía y posición formal. CAND-MEL-021: PROVISIONAL débil. Sin medida directa de prominencia por altura en canciones.
- COMPOSITIONAL (uso): transposición exacta pequeña conserva relaciones con parentesco provisional (EXP-001 B=3; cautelas de tesitura/timbre genéricas). CAND-MEL-019: PROVISIONAL (pequeña), UNSUPPORTED (octavas, cambios amplios, esfuerzo, timbre, función seccional como extensión). Elevación seccional como estrategia con haz de marcadores: GENRE_SPECIFIC pop/rock (CAND-MEL-022). Reservar el extremo absoluto para momento formal: HYPOTHESIS provisional separada, eficacia sin medir. Repetir el extremo (refuerzo o neutralización): GAP.

No resucitar "chorus = higher". CAND-MEL-018 rechazado permanentemente.

## 11. Organización rítmica (RHYTHMIC ORGANIZATION)

Vocabulario obligatorio (RQ-MEL-006): nunca decir solo `rhythm`; especificar duration, onset, IOI, rhythmic pattern, meter, metric position, accent (metric/agogic/dynamic/pitch/phenomenal), syncopation (con definición declarada: L&H-Lee, Oxford/Temperley-1999, Tan et al., Sadie/Tyrrell — no equivalentes), density (onset density/note rate, local/global; controlar tempo), rhythmic repetition (con pitches iguales o distintos, en igual o distinta posición), silence (notated rest, gap, phrase-final, internal, omitted expected onset).

Lo conocido por variable:

- Duration: la duración larga es correlato robusto de acento agógico; alargamiento en límites (producción) contribuye al cierre con armonía; no equivale a importancia/clímax/llegada por sí sola. PROVISIONAL.
- Onset/IOI: downbeat = congruencia máxima, no estabilidad garantizada; offbeat + sustain sobre fuerte = síncopa (según definición); anacrusa/anticipación con soporte de corpus rock; no hay regla offbeat=tensión. PROVISIONAL/GENRE_SPECIFIC según caso.
- Meter/posición: jerarquía internalizada guía expectativa de acentos (Palmer & Krumhansl 1990); el metro operativo lo fija normalmente el conjunto (cross-domain). CAND-MEL-025: PROVISIONAL.
- Accent: multidimensional y modelable en pop (Müllensiefen: 29 oyentes, 15 melodías, modelo ponderado); predice votos de acento, no función de frase. Especificar siempre el tipo.
- Syncopation: anticipación pop/rock documentada en corpus (Tan et al.: 2382 síncopas, mayoría anticipatoria; ~cero en inglés s.XIX; stress silábico crucial). CAND-MEL-026: GENRE_SPECIFIC (heurística de género). U invertida síncopa↔groove (Witek, breaks funk) y densidad↔groove (Madison, audio global): PROHIBIDO trasladar a frase/energía/dosis melódica. CAND-MEL-027: SUPPORTED como bloqueo de transferencia (conocimiento negativo).
- Density: sin efecto aislado establecido sobre continuación/energía melódica; controlar tempo; no confundir con tempo. CAND-MEL-030: heurística negativa.
- Rhythmic repetition: células-4 más repetidas postmillennial (White 2022, distribucional por época/género, sin efecto medido); lo estable bajo pitch cambiante es el patrón de onsets/acentos, no duraciones absolutas (hipótesis integradora sin test).
- Metric displacement: anticipación con soporte rock; retardo residual; misma forma en otra posición = otro evento funcional potencial (hipótesis por coherencia, sin test).
- Silence: mismo hueco se percibe distinto según contexto (sobre todo tonal): límite, interrupción, revelador, meta-escucha, comunicación (Margulis JMT, ensayo); detección/tensión/atribución moduladas por contexto (Margulis MP). CAND-MEL-029: PROVISIONAL como cautela, UNSUPPORTED como generador (action vacío). Sin regla silence=tensión ni silence=respiro.

## 12. Reutilizar material entre frases y secciones (RETURN / REUSE)

- Retorno exacto tras contraste: funciona si la identidad sobrevivió (depende de RQ-MEL-001); apoyo analítico rock (Everett: retorno de coro) y pedagógico; correlato perceptivo sin estudiar.
- Retorno transformado (transpuesto, con final cambiado, fragmentado): lo dicho en secciones 3–5 más posición formal; transposición pequeña PROVISIONAL; final cambiado TRADITION_SPECIFIC + CROSS_DOMAIN_REQUIRED.
- Retorno registral (volver a la zona inicial como gesto de cierre): hipótesis analítica sin medida.
- Retorno rítmico (misma organización temporal con pitches nuevos o viceversa): sin corpus por función formal; GAP.
- Repetición loop-based sostenida: patrón descriptivo documentado donde el cambio formal viene de textura/capas/densidad/timbre mientras la melodía repite (Butler/Middleton). CAND-MEL-011: GENRE_SPECIFIC + CROSS_DOMAIN_REQUIRED (arrangement). Efectos de interés/estancamiento no medidos.
- Variación en otros dominios con melodía estable: misma dependencia de arreglo/producción; fuera de loop-based: hipótesis.

Dependencias de arreglo y forma en casi todo lo seccional. Ninguna estrategia seccional melódica aislada tiene efecto medido.

## Matriz de decisiones (solo desde la investigación existente)

| Problema compositivo | Acción disponible | Preserve | Change | Función pretendida | Estado | Base de evidencia | Dependencias | Riesgo principal |
|---|---|---|---|---|---|---|---|---|
| Establecer idea nueva | Repetición exacta/inmediata | pitch/ritmo/registro | posición formal | refuerzo/establecimiento | PROVISIONAL | CAND-007: pedagogía Schoenberg + Margulis 2012/13 (detección/agrado, no identidad) | familiaridad, complejidad | monotonía si se abusa; registro atencional cambia con exposiciones |
| Establecer con variación temprana | Statement–response (final cambiado desde 2ª aparición) | arranque | final | continuación temprana | TRADITION_SPECIFIC | CAND-008: Schoenberg/Caplin (sin medida perceptiva) | armonía (cross-domain) | el final nuevo cierra prematuramente o no dirige |
| Conservar parentesco cambiando altura | Transposición exacta pequeña | relaciones internas (intervalos, contorno, ritmo) | altura/registro, marco tonal | continuación con color nuevo | PROVISIONAL | CAND-001/019: E1/E3 + EXP-001 B=3 (n=1) | tesitura, distancia tonal | penalización por registro/marco; no máxima identidad |
| Variar sin romper (general) | Conservar contorno + parte de magnitudes/modalidad | contorno, ritmo | magnitudes parciales | variación emparentada | PROVISIONAL (negativo: SUPPORTED) | CAND-002: E1 + EXP-001 C=2/D=4 | familiaridad, color modal | contorno solo no basta (C=2); contorno tampoco necesario (D=4) |
| Elegir palanca ritmo vs. pitch | Decidir por contexto, sin jerarquía fija | según caso | según caso | parentesco situado | SUPPORTED (anti-jerarquía) | CAND-004: Prince Exp.1/2 + Halpern + EXP-001 E | estabilidad temporal, contexto armónico, tarea, experiencia | aplicar "ritmo domina" o inverso como regla |
| Variar ritmo con alturas intactas | Redistribuir duraciones/onsets, controlar acentos | pitches | duraciones/onsets/IOI | continuación con misma identidad | PROVISIONAL | CAND-006: EXP-001 E=4 (n=1) + Jones&Ralston/Müllensiefen/P&K1990 (marco) | estructura acentual, metro | desplazar todos los acentos sin intención rompe parentesco |
| Continuar hacia cierre (clásico) | Fragmentación + liquidación + aceleración armónica | célula reconocible | longitud, rasgos, ritmo armónico | continuación a cadencia | TRADITION_SPECIFIC + CROSS_DOMAIN_REQUIRED | CAND-009: Caplin/Schoenberg (sin medida perceptiva) | armonía, cadencia | corte sin dirección si no se liquida ni se acelera armonía |
| Generar material nuevo coherente (largo plazo) | Variación desarrolladora encadenada | parentesco paso a paso | rasgos progresivos | coherencia orgánica | TRADITION_SPECIFIC (analítico); UNSUPPORTED (perceptivo) | CAND-010: Frisch/Schoenberg (sin correlato medido) | escucha atenta, familiaridad | saltos bruscos rompen cadena; irrelevante en loop/groove |
| Sostener groove con melodía estable | Repetir melodía, variar textura/capas/densidad/timbre | melodía cíclica | otros parámetros | cambio formal sin variar melodía | GENRE_SPECIFIC + CROSS_DOMAIN_REQUIRED | CAND-011: Butler/Middleton (descriptivo, sin medida perceptiva) | arreglo/producción | estancamiento si nada cambia (hipótesis sin medir) |
| Dosificar repetición | Evaluar por contexto y escucha, sin topes | — | — | evitar monotonía sin variar por variar | PROVISIONAL (negativo) | CAND-012: Margulis + Middleton/Butler | familiaridad, complejidad, otros parámetros | usarlo para justificar repetición indefinida sin escucha |
| Continuar localmente tono-a-tono | Proximidad; reversión con gap-fill tras salto | cercanía | dirección | aceptabilidad local | PROVISIONAL | CAND-013/024: Schellenberg + von Hippel&Huron (lecturas coexistentes) | tesitura, sorpresa deliberada | receta de frase completa o cierre formal |
| Dar forma de frase | Coordinar pitch + timing + armonía | — | — | fraseo multidimensional | PROVISIONAL | CAND-014: P&K 1987 (aditividad, clásico) | armonía, timing interpretativo, familiaridad | cargar función al contorno solo |
| Usar forma global (arco) | Arco como opción, nunca norma | — | — | forma disponible | SUPPORTED (negativo: no normar) | CAND-015: Huron 1996 (distribución) + Cornelissen preprint (cautela clustering) | repertorio | prohibir arcos (también normativo sin base) |
| Culminar en punto alto | Pico + soporte rítmico/armónico/dinámico + posición formal | — | configuración | culminación | PROVISIONAL (hipótesis débil) | CAND-016: Eitan (analítico, parcial, sin medida perceptiva) | ritmo, armonía, dinámica, forma | peak sin soporte; máximo al inicio; multiplicar highs |
| Cerrar frase | Coordinar trayectoria final + armonía + métrica + posición; no prescribir descenso | — | trayectoria | cierre (o apertura deliberada) | PROVISIONAL (negativo: SUPPORTED) | CAND-017: teoría + P&K (sin medida directa de cierre) | armonía (decisiva), métrica, forma | descender sobre armonía irresuelta; cerrar siempre igual |
| Desplazar material de registro | Transposición exacta pequeña; comprobar tesitura | relaciones internas | zona absoluta | contraste suave con parentesco | PROVISIONAL (pequeña); UNSUPPORTED (amplia/octava) | CAND-019: EXP-001 B + física genérica | voz/instrumento, marco tonal, forma | tesitura inhabitable; extender B a octavas/timbre/sección |
| Escribir cantable | Concentración en tesitura cómoda; extremos puntuales | centro | — | ejecutabilidad | SUPPORTED (físico genérico); PROVISIONAL (formal) | CAND-020: Sundberg/Adler (parcial, genérico) | intérprete, estilo | límites clásicos a belt/falsete; estética desde física |
| Destacar momento | Rareza relativa + duración + acento + soporte | marco | configuración | prominencia | PROVISIONAL débil | CAND-021: Eitan/Bregman/Ilie-Thompson (marcos, sin medida directa) | registro, tempo, timbre, textura | subir por subir en zona ocupada; fission no deseada |
| Contrastar secciones | Cambio registral + haz (dinámica, textura, ritmo armónico) | continuidad parcial | registro y marcadores | contraste/incremento seccional | GENRE_SPECIFIC + CROSS_DOMAIN_REQUIRED | CAND-022: Summach/OMT (analítico, sin corpus ni medida) | forma verso-coro, tesitura, crecimiento reservado | subir sin haz (contraste débil); agotar registro en verso |
| Decidir afecto por altura | No mapear altura→afecto simple; componer combinaciones | — | — | evitar falsa regla | SUPPORTED (negativo) | CAND-023: Ilie&Thompson (interactivo) | intensidad, tempo, dominio | negar todo papel de la altura (también absoluto) |
| Continuar tras extremo | Movimiento interior como opción local | — | trayectoria | continuación compatible | PROVISIONAL | CAND-024/013: tesitura + expectativa local | forma (cierre vs. escalada) | ley cognitiva; asumir desvío marcado |
| Colocar eventos importantes | Posición fuerte o desplazamiento deliberado (síncopa); especificar acento | — | posición | congruencia/conflicto controlado | PROVISIONAL | CAND-025: P&K 1990 + Müllensiefen | acompañamiento que fije metro | desplazar sin intención; esperar que la posición trabaje sola |
| Sincopar idiomáticamente (rock/pop) | Anticipación: ataque acentuado pre-fuerte + sustain + stress | metro inferido | onset | síncopa de género | GENRE_SPECIFIC | CAND-026: Tan et al. (corpus) + Temperley/L&H-Lee | letra/stress, armonía del fuerte | anticipar sin sustain; aplicar fuera de tradición |
| Dosificar síncopa por groove | NO trasladar U invertida a frase/melodía | — | — | evitar falsa dosis | SUPPORTED (negativo) | CAND-027: Witek/Madison (groove, no frase) | tarea groove vs. frase | negar todo papel de síncopa en melodía |
| Cerrar rítmicamente | Alargar final + silencio post-evento con armonía que resuelva | — | duración, silencio | contribución al cierre | PROVISIONAL + CROSS_DOMAIN_REQUIRED | CAND-028: Kragness&Trainor + Margulis MP | armonía, métrica, contexto tonal | alargar+callar sobre irresolución |
| Usar silencio | Diseñar por contexto, no por duración; sin efecto fijo | — | contexto | límite/interrupción/comunicación situada | PROVISIONAL (cautela); UNSUPPORTED (generativo) | CAND-029: Margulis MP/JMT | contexto tonal/métrico, tipo de silencio | efecto fijo (tensión/respiro/prominencia) |
| Densificar para continuar | Solo con marco coordinado; si no, no densificar por defecto | — | onsets/ventana | continuación/intensificación situada | PROVISIONAL (cautela); UNSUPPORTED (aislada) | CAND-030: Caplin/Madison (scopes sin puente) | tempo, metro, armonía, fragmentación | more-notes=more-energy |

## Lo que una IA compositora puede actualmente hacer

Solo clases con justificación en candidatos actuales:

- Repetir exacta o inmediatamente un motivo como forma disponible de establecerlo antes de variar (CAND-007, PROVISIONAL débil).
- Transportar exactamente un motivo a poca distancia conservando relaciones internas, previendo posible penalización por registro/marco tonal y comprobando tesitura (CAND-001/019, PROVISIONAL).
- Variar el final conservando el arranque para continuar en marco clásico/pregunta-respuesta, coordinando con armonía (CAND-008, TRADITION_SPECIFIC + CROSS_DOMAIN_REQUIRED).
- Fragmentar y liquidar hacia cadencia dentro de la sentence clásica con aceleración armónica coordinada (CAND-009, TRADITION_SPECIFIC).
- Redistribuir duraciones/onsets con pitches intactos controlando la estructura acentual resultante (CAND-006, PROVISIONAL).
- Decidir la palanca ritmo vs. pitch por contexto sin jerarquía fija (CAND-004, SUPPORTED como heurística negativa).
- Continuar localmente por proximidad y reversión con gap-fill tras salto como opción, sin valor formal (CAND-013/024, PROVISIONAL local).
- Coordinar pitch + timing + armonía para el fraseo en lugar de cargar todo al contorno (CAND-014, PROVISIONAL).
- Usar el arco como forma disponible con precedente, nunca como norma (CAND-015, SUPPORTED negativo).
- Tratar el pico como dimensión contribuyente a culminación solo con soporte y posición formal (CAND-016, PROVISIONAL débil).
- Coordinar el final con armonía/métrica/posición sin prescribir descenso (CAND-017, PROVISIONAL; negativo sólido).
- Escribir tesituras habitables distinguiendo rango nominal de concentración y extremos (CAND-020, SUPPORTED físico genérico).
- Usar cambio registral seccional pop/rock como un marcador entre varios del haz, comprobado por escucha (CAND-022, GENRE_SPECIFIC).
- Anticipar sincopadamente en pop/rock con sustain, stress silábico y armonía compatible (CAND-026, GENRE_SPECIFIC).
- Alargar el final y dejar silencio post-evento como contribución al cierre con armonía que resuelva (CAND-028, PROVISIONAL + CROSS_DOMAIN_REQUIRED).
- Colocar eventos importantes en posiciones fuertes o desplazarlos deliberadamente especificando el tipo de acento (CAND-025, PROVISIONAL).
- Evitar dosis/reglas falsas (no topar repetición por principio; no trasladar groove a frase; no mapear altura→afecto; no normar arco/descenso/peak) — el conocimiento negativo más sólido del sistema (CAND-004/012/015/017/023/027).
- En contextos loop/groove, sostener la melodía cíclica y planificar el cambio en textura/capas/densidad/timbre (CAND-011, GENRE_SPECIFIC + CROSS_DOMAIN_REQUIRED).

## Lo que una IA compositora todavía NO puede decidir fiablemente

Solo gaps apoyados por la investigación (cada uno con su causa):

- Cómo inventar un primer motivo fuerte (altura, contorno, ritmo, rango iniciales): ningún candidato generativo. GAP-01.
- Dosis exacta de repetición (cuántas veces antes de variar): ningún número justificado; depende de familiaridad, complejidad, tradición y otros parámetros. GAP-02.
- Umbral exacto donde la variación se vuelve material nuevo: sin curva; EXP-001 muestra tolerancia grande en una dimensión (D/E=4) y degradación con cambio multidimensional o modal (C/F=2), n=1. GAP-03.
- Qué contorno produce qué función (apertura/continuación/llegada/cierre): ningún mapping; tipos posiblemente no discretos psicológicamente. GAP-04.
- Cuánto rango usar ni qué tesitura exacta por voz/estilo: sin números; límites concretos sin inspeccionar. GAP-05.
- Cuándo un punto alto se vuelve clímax: sin medida perceptiva; configuraciones por estilo sin receta transferible. GAP-06.
- Dosis óptima de síncopa o densidad para frase/energía: transferencias bloqueadas (groove ≠ frase). GAP-07.
- Cómo cerrar solo con melodía (sin armonía): cierre multidimensional con armonía probablemente decisiva. GAP-08.
- Cómo diseñar memorabilidad, hook o prominencia fiable: constructos separados, deliberadamente no investigados aquí; reconocimiento ≠ recall ≠ hook. GAP-09.
- Cómo evoluciona la ponderación de rasgos con familiaridad en contexto compositivo real (motivo nuevo vs. establecido): modulación documentada en laboratorio, sin curva compositiva. GAP-10.
- Registro por sección en pop/rock (pregunta de corpus): ningún corpus mide altura/rango/tesitura por sección. GAP-11 (heredado de CAND-018 rechazado).
- Desplazamiento amplio/octava, expansión/contracción aislada, repetición del extremo, retorno registral con efecto medido: sin apoyo. GAP-12.
- Taxonomía funcional de silencios (interno vs. final vs. omisión) y de síncopa (definiciones no equivalentes): constructos sin delimitar. GAP-13.

## Mapa cross-domain

| Decisión melódica | Dominio requerido faltante | Por qué la melodía sola es insuficiente |
|---|---|---|
| Final cambiado que dirige (continuar vs. cerrar) | harmony (RQ-MEL-007) | El mismo final dirige o cierra según marco armónico (pregunta/respuesta, cadencia) |
| Fragmentación que conduce a cierre | harmony (ritmo armónico, cadencia) | Sin aceleración armónica es corte sin dirección (Caplin) |
| Cierre o apertura de frase | harmony + rhythm/meter + form | Descenso/duración/silencio/posición son contribuciones; la resolución armónica probablemente decide |
| Llegada/culminación | harmony + rhythm/meter + dynamics + form | El pico necesita configuración y posición; misma altura culmina o no según contexto |
| Contraste seccional registral | arrangement/texture + dynamics + harmony + lyrics | El registro es un marcador entre varios; el haz decide |
| Sostener loop con interés formal | arrangement/production | El cambio viene de capas/densidad/timbre mientras la melodía repite (Butler) |
| Establecer metro inequívoco | rhythm (acompañamiento) | La melodía sola induce con ambigüedad; el conjunto fija el metro operativo |
| Anticipación inteligible | lyrics/prosody + harmony | Stress silábico y armonía del tiempo fuerte co-determinan la síncopa (Tan et al.) |
| Prominencia en mezcla | arrangement/timbre + dynamics | Registro melódico vs. foreground en mezcla sin medidas; timbre y densidad simultánea deciden |
| Cantabilidad real | performance/voice (tesitura del intérprete) | Límites genéricos insuficientes; belt/falsete/estilo cambian los números |
| Desarrollo a gran escala | form/song-level | Variación local ≠ desarrollo formal; retorno seccional y trayectoria pertenecen a forma |

Orden futuro sugerido por estos cuellos de botella: armonía (primero melodía-armonía), luego ritmo/metro formal, luego forma (frase/sección), y solo después hooks y contraste seccional fino.

## Anti-reglas — lo que futuras IAs NO deben asumir

Solo conclusiones apoyadas por nuestra investigación (con fuente entre paréntesis):

1. El ritmo NO es siempre más importante que el pitch (ni al revés): la ponderación cambia con tarea y contexto (Prince Exp.1/2; EXP-001 E=4). (CAND-004, SUPPORTED)
2. El contorno solo NO define la identidad: conservar contorno+ritmo cambiando magnitudes puede dar parentesco bajo (EXP-001 C=2); invertir el contorno puede dar máximo (EXP-001 D=4). (CAND-002, SUPPORTED negativo)
3. Subir NO crea automáticamente tensión ni continuación formal: la aceptabilidad local (proximidad/reversión) no es función de frase; la trayectoria necesita marco. (CAND-013/024 + RQ-MEL-003)
4. Bajar NO cierra automáticamente: el descenso no es necesario ni suficiente; ascensos terminales existen; el fondo schenkeriano no prescribe superficie. (CAND-017)
5. La nota más alta NO es automáticamente el clímax: el pico necesita configuración y posición; sin soporte no hay garantía. (CAND-016)
6. El coro NO debe ser más alto que el verso: sin corpus; CAND-MEL-018 rechazado permanentemente; la elevación es estrategia con haz, no hecho. (RQ-MEL-003/005)
7. Más notas NO significa más energía ni continuación: densidad aislada sin efecto establecido; controlar tempo; groove ≠ frase. (CAND-030 + CAND-027)
8. La síncopa NO significa automáticamente groove, energía o tensión melódica: U invertida solo en breaks funk (groove ratings); anticipación es recurso de género con condiciones. (CAND-027/026)
9. El silencio NO significa automáticamente tensión (ni respiro, ni cierre): el mismo hueco se evalúa por contexto tonal/métrico; taxonomía funcional sin test una a una. (CAND-029/028)
10. NO repetir exactamente N veces antes de variar: ningún número justificado; clásica varía pronto, loop sostiene muchas repeticiones; decidir por contexto y escucha. (CAND-007/012 + RQ-MEL-002)
11. Más repetición NO significa monótonamente más aburrimiento (ni más agrado): relación no monótona, dependiente de familiaridad, complejidad, otros parámetros y tradición. (CAND-012)
12. Alto NO equivale a emotivo/energético/brillante por sí solo: efectos interactivos con intensidad y tempo, opuestos por dominio; energía ≠ tensión. (CAND-023)
13. La U invertida de síncopa-groove NO es dosis compositiva melódica. (CAND-027, SUPPORTED negativo)
14. El arco NO es norma de frase completa; los tipos de contorno NO son clases perceptivas establecidas. (CAND-015)
15. La transposición NO preserva máxima identidad automáticamente (B=3, no 4) ni se extiende a octavas o función seccional. (CAND-001/019)
16. Desplazar métricamente NO preserva función automáticamente: misma forma en otra posición es otro evento funcional potencial. (RQ-MEL-006, hipótesis por coherencia)

## Auditoría de solapamientos y conflictos entre candidatos

- CAND-MEL-013 vs CAND-MEL-024 (requerido): solapamiento parcial explícito, registrado en ambas síntesis y en CAND-024. 013 aporta el núcleo tono-a-tono (expectativa medida + explicación por tesitura coexistentes, con acción local). 024 aporta el encuadre de continuación restringida cerca de extremos (opción local tras extremo, con cautelas formales). NO fusionar IDs. Tratamiento futuro recomendado: mantener ambos como lentes complementarias (mecanismo local vs. decisión situada tras extremo) con referencia cruzada obligatoria; si un futuro corpus o medida separa expectativa cognitiva de restricción estadística, reescribir el alcance sin reutilizar ni eliminar IDs.
- CAND-MEL-001 vs CAND-MEL-019: mismo mecanismo (transposición exacta) en dos niveles: 001 identidad/parentesco, 019 desplazamiento con coste físico/tímbrico. Solapamiento por diseño (dependencia RQ-MEL-001 → RQ-MEL-005). Mantener ambos; 019 como cautela situada de 001, no como duplicado a eliminar.
- CAND-MEL-002 (contorno insuficiente) vs CAND-MEL-015 (arco no normativo) vs CAND-MEL-016 (peak ≠ clímax) vs CAND-MEL-017 (descenso ≠ cierre): familia de anti-reglas de contorno/registro. No son redundantes: operan a niveles distintos (identidad, forma global, culminación, cierre). Mantener separadas; futura integración podría agruparlas como "familia contorno-función" sin fusionar IDs.
- Candidatos negativos/heuristicas negativas (004, 012, 015, 023, 027, 029-parcial, 030): describen el mismo patrón metodológico (bloqueo de falsa regla) en dominios distintos. No fusionar: cada bloqueo tiene base empírica propia.
- CAND-MEL-003 vs CAND-MEL-005: ambas sin acción concreta, apoyo indirecto, sensibilidad (familiaridad / función tonal). Riesgo de doble contabilidad si se promocionan: ninguna lista para promoción; retener como sensibilidades, no como técnicas.
- CAND-MEL-021 (prominencia por rareza) vs CAND-MEL-016 (peak ≠ clímax): 021 es el marco general débil, 016 el caso analítico. Solapamiento parcial benigno; 021 más débil (sin medida directa). Si se promociona algo de esta familia, priorizar 016 con scope.
- Tensión potencial resuelta: inversión difícil en memoria (Dowling) vs. aceptada en comparación directa (EXP-001 D=4): registrada como evidencia mixta dependiente de tarea en RQ-MEL-001/002; afecta a la inversión como operación sin invalidar ningún candidato.
- Tensión de valores resuelta por scope: desarrollo como ideal (tradición alemana) vs. loop como virtud (Middleton/Butler): contradicción estética entre tradiciones, no factual. No resolver; marcar scope siempre.

## Promotion readiness (recomendación de integración; NO cambia estados)

Decisión del director (revisión): criterio más conservador. STRONG_CANDIDATE únicamente 004, 012, 017.

- STRONG_CANDIDATE: 004, 012, 017 (3). Solo estos podrían convertirse en conocimiento manual provisional tras revisión del director, con scope explícito.
- POSSIBLE_WITH_SCOPE: 001, 002, 006, 007, 008, 009, 010, 011, 013, 014, 015, 016, 019, 020, 022, 023, 024, 025, 026, 027, 028 (21). Solo con limitaciones fuertes de tradición/género/nivel (clásico, pop/rock, loop, local tono-a-tono, físico genérico) y sin generalizar. CAND-MEL-014 se clasifica aquí porque su redacción actual depende claramente del scope clásico/perceptivo (Palmer & Krumhansl 1987, repertorio clásico, juicios de frase) y no se eleva solo por ser útil. 010 solo como teoría analítica de tradición; 020 con inspección primaria de los pasajes relevantes pendiente antes de cualquier futura promoción a manual (ver decisión del director §4); 026 con representación subyacente inferida; 027/023 como bloqueos negativos con acción vacía.
- NOT_READY: 003, 005, 021, 029, 030 (5). Evidencia indirecta, sin acción concreta o sin medida directa; retener como sensibilidades o cautelas, no como conocimiento manual.
- REJECTED: 018 (1). ID preservado permanentemente, nunca reutilizar.

Conteos: STRONG_CANDIDATE: 3 | POSSIBLE_WITH_SCOPE: 21 | NOT_READY: 5 | REJECTED: 1.

Criterio aplicado (conservador, por decisión del director): STRONG reservado a 004, 012 y 017; todo lo demás previamente considerado fuerte pasa a POSSIBLE_WITH_SCOPE sin contradicción objetiva encontrada.

## Manual readiness

Respuesta: NO.

Razón (decisión del director): la investigación actual aporta estrategias útiles de transformación, anti-reglas y restricciones decisionales, pero todavía carece de una estrategia suficientemente apoyada para crear material melódico inicial y presenta dependencias mayores de cierre/llegada respecto de la armonía.

`research/integrations/melody-foundations-v0.md` permanece como capa provisional de integración operativa. NO poblar `manual/01-melody.md`.

## Rule readiness

Respuesta: NO.

Ningún conocimiento actual está listo para codificación determinista o estructurada en `rules/`. Lo más cercano (tesitura habitable como chequeo físico, anticipación como patrón con condiciones) carece de límites verificados, de medidas de efecto y de resolución cross-domain (armonía, metro operativo, intérprete real). Una heurística composicional no es una regla de máquina. No crear reglas.

## Priorización de gaps por leverage compositivo

Declaraciones preservadas por decisión del director:

- Highest Melody-specific gap: initial melodic idea / motif construction (GAP-01).
- Highest project-wide cross-domain bottleneck: harmony.

Ordenado por "si se resolviera, cuánto mejoraría la capacidad de decidir con intención":

1. Interacción melodía-armonía (RQ-MEL-007): desbloquea cierre, llegada, finales cambiados y función tonal. Cuello de botella de casi toda la matriz.
2. Construcción de frase (cómo ensamblar material en frase bien formada con función): el eslabón entre operaciones locales y forma; sin esto las operaciones flotan.
3. Idea melódica inicial / construcción de motivo: sin esto la IA no puede empezar; hoy solo transforma.
4. Cierre/llegada multidimensional con medida (qué combinaciones cierran, con qué armonía/métrica/posición): receta negativa disponible, positiva ausente.
5. Prominencia/memorabilidad/hook como constructos separados con medidas propias: hoy deliberadamente fuera; sin esto no hay dirección estética.
6. Desarrollo a gran escala y su correlato perceptivo (variación superficial vs. desarrollo genuino en escucha).
7. Corpus pop/rock de registro, rango, tesitura, ritmo y contorno por sección y función (responde GAP-11 y calibra 022/026).
8. Prosodia/letra y flow como dominio rítmico separado (condiciona síncopa y acento).
9. Contraste seccional fino y trayectorias a escala de canción (arco seccional, retornos, coro final).
10. Delimitación de constructos (síncopa, densidad, silencio, tipos de contorno) antes de cualquier experimento nuevo. EXP-002 sigue en pausa; ningún EXP-003 antes de EXP-002.

## Trazabilidad

- Fuentes: síntesis RQ-MEL-001/002/003/005/006 y CAND-MEL-001–030 (ver tablas Sources en cada síntesis y YAML individuales). EXP-001 como indicio exploratorio n=1 citado donde corresponde; EXP-002 solo como diseño pausado.
- Decisiones de integración propias de este documento (no del proyecto): flujo decisional por problema compositivo; estatus SUPPORTED/PROVISIONAL/etc. como lectura de integración (distinta del `status`/`evidence_class` de cada candidato); conteos de promotion readiness como recomendación.
- Prohibido citar este archivo como conocimiento aprobado: es capa de auditoría previa a revisión del director.
- Revisión del director aplicada: promotion readiness conservador (STRONG solo 004/012/017), CAND-013/024 separados con referencia cruzada, CAND-020 pendiente de inspección primaria, manual readiness NO, siguiente dominio HARMONY FOUNDATIONS (sin iniciar RQ-MEL-007: la interacción melodía-armonía se investigará después de un modelo fundacional de armonía).
