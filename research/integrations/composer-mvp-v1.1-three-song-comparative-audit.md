# Auditoría comparativa de capacidades — Composer MVP v1.1

## 1. Alcance

Esta auditoría compara SONG-001, su revisión controlada SONG-001-R1, SONG-002 y SONG-003. Examina las trazas de decisión, SongPlans, validaciones, auditorías de proceso y revisiones de escucha existentes. Su pregunta es qué capacidades del proceso quedan demostradas por esos artefactos y por las decisiones del Project Owner. No compone SONG-004 ni cambia canciones, conocimiento, género, reglas, experimentos o motor.

El alcance musical observado es el de las realizaciones indie-dance/electrónica-pop del MVP. Tres canciones y una revisión controlada no permiten inferir capacidad para cualquier género o brief.

## 2. Límite de la evidencia

Se distinguen cuatro clases de evidencia:

- **Proceso / ingeniería:** trazas, opciones, filtros, handoffs, revisiones y separación entre decisión musical y entrada técnica.
- **Observación estructural del SongPlan:** forma, alturas, asignaciones, eventos, articulación, secciones y relaciones escritas. Describe lo planificado; por sí sola no prueba un efecto audible.
- **Validación de materialización:** validación de SongPlan, MIDI y correspondencia entre lo especificado y lo exportado. No juzga calidad artística ni timbre.
- **Aceptación artística del Owner:** escucha humana en REAPER. Es decisiva para estas obras, pero expresa una evaluación situada, no evidencia científica ni regla general.

La realización FM8 de SONG-002 y las asignaciones de instrumentos de reproducción son contexto de escucha. Los campos energy del SongPlan son metadatos y no crean por sí solos dinámica MIDI.

## 3. Resumen por canción

| Obra | Brief y forma | Armonía y final | Foco, groove y percusión | Desarrollo, textura y escucha |
|---|---|---|---|---|
| **SONG-001** | Instrumental, persistente, intensificación gradual, foco claro y release algo abierto. 16 compases: opening/build/focal/release, 4 compases cada uno. | Ciclo C–Am–F–G sostenido en las secciones; pitches escritos en las pistas. Termina con G4 sostenido sobre el ciclo, con intención abierta, no declarada como cierre perceptivo. | Lead focal; bajo alterna raíces y quintas con colocaciones a tiempo y anticipadas. La percusión quedó omitida sin decisión explícita. Texture sincopada entra en build y focal. | Desarrollo por variación parcial del lead y entrada/retiro de capas; focal más densa y release más despejado. Una revisión transversal bajó el voicing de texture para preservar el lead. El Owner consideró agradable y musical la línea base, pero señaló omisión de percusión y ambigüedad estilística/tímbrica; aceptó R1 como la realización revisada. |
| **SONG-001-R1** | Revisión de percusión controlada: conserva forma, tempo, armonía, lead, bajo y texture de SONG-001. | Hereda ciclo C–Am–F–G y release abierto. | El Owner rechazó una iteración intermedia de solo kick como insuficiente para su intención. La revisión final añade batería completa que crece por secciones: kick, snare, hats, fill de toms y acentos localizados; se coordina con bajo y lead. | La actividad de batería aumenta hacia focal y se retira en release. El Owner aceptó el desarrollo, el fill y la integración con el bajo; el material pitched permanece inalterado. Es una revisión dirigida por el Owner, no una segunda composición independiente. |
| **SONG-002** | 28 compases, 118 BPM, 4/4, A Dorian: threshold 4, pulse 8, lift 4, focal 8 y afterglow 4. | Ciclo principal Am9–D6–Am9–G6, tres tipos de acorde, frente a cuatro en el ciclo de SONG-001; ambos planes contienen siete clases de altura. afterglow: G6–D6–Am9–Am9, con Am9 sostenido al final. En el compás 26, D6 está rotulado sobre pitches explícitos D3–A3–E4: discrepancia histórica LF-022, sin semántica explicativa en el plan. Las pitches son la evidencia de lo que suena. | El bajo es el protagonista perceptivo del groove según el Owner; sus células evolucionan entre secciones y aumentan de tres a cuatro ataques por compás en focal. N3-P se resolvió antes del SongPlan: percusión **MINIMAL**, integrada estrechamente con bajo, sin recordatorio manual del Owner. El lead está más espaciado y subordinado al peso rítmico del bajo. | Cambios de células y de realización rítmica sostienen el desarrollo; la trayectoria llega a un afterglow espacioso. El Owner aceptó la jerarquía de bajo, la percusión mínima, el desarrollo rítmico y la coherencia general; describió un carácter ambiental/espacial ligado también a los timbres de audición. No pidió revisión musical. |
| **SONG-003** | 24 compases, 132 BPM, 4/4, E Mixolydian: spark 4, stride 6, pocket 4, lift 2, arrival 6 y button 2. | 24 asignaciones, un acorde por compás, con seis triadas (E, A, F#m, Bm, D, C#m) y realizaciones explícitas. Final breve en E mediante button. | Llamada/respuesta entre lead y percusión; bajo comparativamente sencillo y de apoyo. N3-P se resolvió prospectivamente como **FULL PERCUSSION** con kick, snare, hats y cowbell. “Full” describe la arquitectura seleccionada, no actividad continua en cada subdivisión. | Contraste por retirada en pocket, breve lift, llegada y reentrada; la armonía cambia su realización rítmica. El Owner cuestionó espacios cerca del compás 18 y escuchó en loop los compases aproximados 17–20: el pulso siguió claro, el groove no colapsó y la entrada siguiente fue natural. Aceptó esos huecos como diseño intencional, la repetición con desarrollo y la diversidad audible. Aceptada sin revisión. |

### Desarrollo, tensión/release y cierres

- **SONG-001:** la traza distribuye el cambio entre capas, densidad, registro y variación melódica; la focal concentra textura/densidad y release las retira, dejando G4 sostenido sobre el ciclo. “Abierto” es intención del plan, no una afirmación automática de cierre percibido.
- **SONG-001-R1:** la batería entra parcialmente, se completa hacia focal y se desmonta en release. Esto describe su arreglo y la aceptación local del Owner, no una curva universal de energía.
- **SONG-002:** threshold/pulse/lift/focal conduce a afterglow con cambio armónico más lento y Am9 sostenido al final. La traza evita llamar cadencia o cierre probado a esa llegada; el Owner acepta la pieza y nota su carácter espacial.
- **SONG-003:** pocket retira actividad antes de lift/arrival; los huecos de arrival conservan pulso según la escucha. El button breve en E es el final planificado y aceptado dentro de la escucha global; no hubo prueba auditiva comparativa aislada de cierres.

### Trazabilidad y guardrails registrados

- **SONG-001:** siete guardrails PASS, cero WARNING y uno NOT APPLICABLE; siete handoffs de prioridad artística, cero usos de RANK-1/RANK-2 y una revisión cross-domain localizada (REV-001). La primera materialización necesitó acortar una duración del bajo que rebasaba el límite de sección.
- **SONG-001-R1:** SongPlan y mapeo de drums validados; 98 note-ons mapeados. La auditoría confirma que los cuatro tracks pitched originales no cambiaron y que el Owner aceptó la versión final. La parte completa sustituye la iteración de kick-only.
- **SONG-002:** nueve guardrails PASS, cero WARNING y uno NOT APPLICABLE en la auditoría previa; ocho handoffs, cero RANK-1/RANK-2 y cero revisiones conceptuales cross-domain. La discrepancia LF-022 se documentó después de esa auditoría previa, por lo que ese resultado no debe leerse como si ya hubiera detectado la ambigüedad. Se corrigieron además límites/duraciones y cobertura de motivos al materializar, sin cambiar las decisiones compositivas trazadas.
- **SONG-003:** ocho guardrails PASS, cero WARNING y uno NOT APPLICABLE; ocho handoffs, cero RANK-1/RANK-2 y cero revisiones cross-domain. El diagnóstico armónico manual cotejó por compás **24 etiquetas: 24 CONSISTENT, cero PASS WITH SCOPE y cero WARNING**. Su auditoría de proceso anterior a la escucha decía que esta estaba pendiente; la posterior revisión de escucha del Owner es la que cierra el estado artístico.

## 4. Capacidades demostradas

La escala evalúa evidencia de ejecución en este alcance, no calidad global del compositor.

| Capacidad | Estado | Evidencia y límite |
|---|---|---|
| **A. Planificación de canción completa** | **DEMONSTRATED** | Tres SongPlans completos con forma, material, secciones y handoff MIDI; SONG-001-R1 prueba además una revisión acotada. |
| **B. Diferenciación formal** | **DEMONSTRATED** | 16, 28 y 24 compases y segmentaciones distintas (4/4/4/4, 4/8/4/8/4, 4/6/4/2/6/2). Solo dentro del alcance actual. |
| **C. Variedad armónica** | **DEMONSTRATED** | Ciclo C–Am–F–G; marco A Dorian de acordes extendidos; marco E Mixolydian de seis triadas y secuencia nueva. SONG-002 conserva una discrepancia localizada de etiqueta/voicing. Variedad estructural no demuestra superioridad ni calidad armónica universal. |
| **D. Variedad rítmica / de groove** | **DEMONSTRATED** | Bajo raíz/quinta y percusión añadida en R1; bajo activo como protagonista con percusión mínima en SONG-002; bajo de apoyo y llamada/respuesta con percusión full en SONG-003. Aceptaciones del Owner son específicas a cada obra. |
| **E. Variedad de jerarquía focal** | **DEMONSTRATED** | Lead focal en SONG-001, bajo protagonista en SONG-002 y relación compartida lead/percusión en SONG-003; el Owner aceptó las jerarquías escuchadas. |
| **F. Repetición + desarrollo** | **DEMONSTRATED** | Las trazas describen qué persiste y qué cambia; el Owner reconoce desarrollo en SONG-002/003 y acepta el ciclo con variaciones de SONG-001. No se infiere una regla sobre cuánta variación funciona en general. |
| **G. Arquitectura de percusión** | **DEMONSTRATED** | Omisión original corregida en una R1 aceptada; N3-P aparece prospectivamente y selecciona MINIMAL en SONG-002 y FULL en SONG-003, ambas aceptadas. DELEGATED e INTENTIONALLY NONE están contempladas como opciones válidas, pero no se prueban como realizaciones en estas canciones. |
| **H. Diferenciación textural** | **DEMONSTRATED** | Entrada/retiro de texture, arreglo mínimo orientado al bajo, y retirada/reentrada con llamada-respuesta; los planes difieren también en persistencia de capas. Alcance acotado a estos arreglos. |
| **I. Trayectoria de energía** | **PARTIALLY DEMONSTRATED** | Las formas y capas proponen build, retirada y llegada; el Owner escucha desarrollo y contraste. energy es metadato, no dinámica, y no hay una medida perceptiva controlada que compruebe de forma aislada la trayectoria. |
| **J. Release / comportamiento del final** | **PARTIALLY DEMONSTRATED** | Los planes contienen tres estrategias distinguibles: release abierto sostenido, afterglow modal prolongado y button breve. La aceptación de SONG-002/003 es global; no hay evaluación específica comparable de la percepción de cada final. |
| **K. Coordinación cross-domain** | **PARTIALLY DEMONSTRATED** | Trazas y una revisión de SONG-001 coordinan foco, textura, armonía, bajo y percusión; SONG-001 omitió percusión y SONG-002 dejó LF-022. Los guardrails posteriores mejoran la integración, pero estos escapes impiden considerar la consistencia plenamente demostrada. |
| **L. Trazabilidad al SongPlan** | **DEMONSTRATED** | Los cuatro paquetes incluyen trazas y artefactos estructurales; las decisiones, pitches, asignaciones, prioridades, límites y handoffs quedan identificables. La discrepancia SONG-002 también quedó registrada en la revisión, no corregida silenciosamente. |
| **M. Materialización segura mediante music-engine** | **DEMONSTRATED** | Validaciones y MIDI producidos para las tres canciones y R1; bounds, cobertura de secciones y mapeos fueron inspeccionados/corregidos cuando hizo falta. Esto demuestra handoff MIDI validado, no render de audio ni percepción de timbre. |
| **N. Coherencia musical aceptable para el Owner** | **DEMONSTRATED** | La línea base SONG-001 fue considerada musical/agradable; el Owner aceptó R1, SONG-002 y SONG-003 sin pedir revisión musical adicional. Es aceptación local del Owner y de estas realizaciones. |

**Recuento:** 11 capacidades demostradas, 3 parcialmente demostradas, 0 no demostradas en los 14 rubros. Esto no implica que se haya demostrado cada tarea musical posible. La capacidad de ranking se trata por separado porque no aparece como uno de esos 14 rubros y no fue utilizada.

## 5. Auditoría de ranking y prioridad artística

La escalera observada es **enumerar → filtrar → rankear por un criterio explícito**. Las trazas enumeran alternativas y usan filtros condicionados por brief, límites técnicos, dependencias y distinciones del conocimiento. No siempre enumeran todas las alternativas posibles: son opciones de trabajo documentadas.

**CAN ENUMERATE: DEMONSTRATED. CAN FILTER: DEMONSTRATED. CAN RANK: NOT YET DEMONSTRATED.** La enumeración y el filtrado se observan en las trazas de las tres canciones; los resultados de composición no sustituyen una prueba de ranking.

| Uso | SONG-001 | SONG-001-R1 | SONG-002 | SONG-003 | Total registrado |
|---|---:|---:|---:|---:|---:|
| Handoffs de prioridad artística | 7 | revisión dirigida por el Owner; no se registra como ledger de canción completa | 8 | 8 | **23 en las tres canciones completas** |
| RANK-1 | 0 | 0 documentado | 0 | 0 | **0** |
| RANK-2 | 0 | 0 documentado | 0 | 0 | **0** |

Las decisiones repetidamente subdeterminadas por el conocimiento incluyeron forma/trayectoria, armonía y su realización, identidad/foco, prioridad entre capas, arquitectura y patrón de percusión, variación, contraste y final. En cada caso el proceso pudo filtrar alternativas, pero la prioridad artística o el brief resolvió entre opciones admisibles. Las trazas no registran decisiones importantes pendientes al cerrar las obras.

Esto es aceptable para el MVP actual: el contrato admite que el Owner resuelva alternativas legítimas cuando no hay criterio musical fundamentado para preferir una. No debe interpretarse una selección aceptada como prueba de ranking. RANK-1 quedó en cero porque no se planteó una tarea aplicable de reconocer/discriminar material melódico previamente establecido; RANK-2 no está disponible en la arquitectura actual. No se identifica aquí una decisión recurrente sin resolver que exija abrir investigación antes de otra composición.

## 6. Auditoría de percusión

La secuencia observable es:

1. **SONG-001:** arquitectura de percusión no declarada; el Owner detectó la omisión en escucha. Fue una omisión de aplicación/integración en esa composición, no una demostración de que la percusión fuera innecesaria.
2. **SONG-001-R1:** tras considerar insuficiente la realización intermedia de solo kick, se añadió una parte completa por secciones. El Owner aceptó esta revisión controlada.
3. **Composer MVP v1.1:** se incorporó N3-P como decisión prospectiva dependiente del groove, separada de la asignación técnica de notas MIDI. FULL, MINIMAL, DELEGATED e INTENTIONALLY NONE se mantienen como posibilidades; no hay un resultado obligatorio por género.
4. **SONG-002:** N3-P se aplicó antes del SongPlan sin recordatorio manual; MINIMAL fue deliberado y aceptado.
5. **SONG-003:** N3-P se aplicó antes del SongPlan; FULL fue deliberado y aceptado. La escucha confirmó que en esta pieza FULL no significaba subdivisión continua ni llenar cada hueco.

**Percussion decision coverage: DEMONSTRATED**, en el sentido de que el proceso consideró y materializó dos arquitecturas prospectivas distintas, aceptadas en sus contextos, además de reparar la omisión original. No demuestra que FULL sea mejor que MINIMAL, que toda canción indie-dance requiera drums, ni que las cuatro salidas de N3-P ya hayan sido materializadas y probadas.

## 7. Integridad de etiqueta armónica / voicing

En SONG-002, LF-022 registra la etiqueta D6 frente al voicing explícito D3–A3–E4 del compás 26. La sonoridad escrita controla lo que suena; no existe en el SongPlan semántica previa que justifique explícitamente esa realización, y no se reescribió la obra aceptada. El hallazgo dio lugar al guardrail documental de comparar la etiqueta con las pitches explícitas, permitir omisiones/adiciones/inversiones/doblamientos cuando se documenten, y emitir WARNING ante una discrepancia sin explicar. No introduce un parser automático ni umbrales de teoría de acordes.

En SONG-003, la revisión de proceso cotejó por compás la pista harmony con las 24 etiquetas: **24 CONSISTENT, 0 WARNING**. Esto demuestra la ejecución manual del chequeo en un SongPlan completo, pero no prueba aún su ruta de WARNING frente a una nueva discrepancia, ni su consistencia a través de una colección amplia.

**Harmonic label / voicing integrity safeguard: PARTIAL.** El procedimiento ya se aplicó prospectivamente una vez y produjo trazabilidad; su detección de incompatibilidad no se probó en esa aplicación. SONG-002 permanece preservada y aceptada sin revisión musical.

## 8. Auditoría de diversidad entre canciones

| Dimensión | SONG-001 / SONG-001-R1 | SONG-002 | SONG-003 |
|---|---|---|---|
| Forma | 16 compases, cuatro bloques iguales; R1 conserva la forma | 28 compases, cinco secciones con pulse y focal largos | 24 compases, seis secciones desiguales, pocket y button breves |
| Armonía | C–Am–F–G persistente | A Dorian, Am9–D6–Am9–G6; afterglow ralentiza/cambia la secuencia | E Mixolydian, seis triadas y secuencia nueva por compás |
| Capa focal | Lead | Bajo/groove según Owner; lead más contenido | Llamada/respuesta lead-percusión; bajo de apoyo |
| Rol del bajo | Raíz/quinta como soporte del ciclo; raíces coinciden con kick en R1 | Protagonista rítmico y focal, con células de mayor actividad | Comparativamente simple, apoya el conjunto |
| Densidad de lead | Identidad recurrente y actividad más continua | Menos continua; deja espacio perceptible al bajo | Identidad que retorna con cortes y variaciones |
| Groove | Ciclo y anticipaciones del bajo; batería se añade en R1 | Desarrollo del bajo con percusión mínima | Batería full con espacios, retirada y respuesta a lead |
| Percusión | Omitida en original; completa y progresiva en R1 | MINIMAL | FULL, con huecos intencionales |
| Contraste y desarrollo | Capas/texture desde build, foco y retirada en release | Cambios por secciones y células de bajo; afterglow | Retirada en pocket, lift breve, arrival y reentrada |
| Final | Release relativamente abierto | Afterglow modal prolongado | Button corto en E |

La auditoría demuestra **diversidad de estrategia dentro del alcance actual**: cambian forma, marco armónico, jerarquía focal, función del bajo, densidad del lead, arquitectura de percusión, contraste y final. SONG-001-R1 comparte la clase amplia de batería completa con SONG-003, pero no reutiliza su patrón/función; SONG-002 aporta la alternativa MINIMAL. La escucha del Owner de SONG-003 acepta la distinción percibida frente a las obras previas. Esto no demuestra diversidad ilimitada de estilos, transferencia a otros géneros ni independencia de las preferencias del Owner.

**Cross-song diversity: DEMONSTRATED**, acotada a diferencias de estrategia observables en estos tres planes y a la aceptación artística disponible.

## 9. Fallos, advertencias y revisiones

| Hallazgo | Clasificación principal | Qué ocurrió y cómo se cerró |
|---|---|---|
| Percusión no declarada en SONG-001 | **DECISION APPLICATION / CROSS-DOMAIN INTEGRATION** | La traza resolvió groove y capas sin dejar una decisión explícita de percusión. El Owner lo detectó; R1 fue la revisión autorizada y aceptada. No prueba un vacío de conocimiento musical. |
| Iteración intermedia de R1 con solo kick | **ARTISTIC CHOICE / DECISION APPLICATION** | El Owner indicó que no cumplía la intención de batería completa. Se reemplazó por una parte desarrollada por secciones y aceptada. La iteración intermedia no es el resultado final de R1. |
| Duración del bajo que excedía límite en primera materialización de SONG-001 | **MATERIALIZATION** | Se acortó para respetar el límite objetivo de la sección; validación/render posterior pasaron. |
| Cobertura de motivos y límites temporales en SONG-002 | **MATERIALIZATION** | Inspección encontró duraciones fuera de sección y que el motor no repetía motivos cortos para cubrir ocho compases. Se completaron eventos explícitos y se corrigieron límites para representar decisiones ya tomadas. No hubo revisión conceptual cross-domain. |
| D6 frente a D3–A3–E4 en SONG-002, compás 26 (LF-022) | **SONGPLAN REPRESENTATION / CROSS-DOMAIN INTEGRATION** | Metadato no explicado respecto de las pitches autoritativas. La realización escuchada se conserva; se documentó el hallazgo y luego se estableció un chequeo manual. No hubo petición de revisión musical. |
| Hueco percibido cerca del compás 18 de SONG-003 | **ARTISTIC CHOICE / PLAYBACK–SOUND REALIZATION** | Tras escuchar en loop compases 17–20, el Owner confirmó pulso claro, continuidad del groove y entrada natural. No era evento MIDI perdido, error de materialización ni defecto compositivo; no se añadió material. |
| Identidad estilística ambigua / timbre dependiente en la primera escucha de SONG-001 | **PLAYBACK / SOUND REALIZATION** | Observación ligada a esa realización y configuración de reproducción; no se atribuye solo al plan ni demuestra una limitación del genre pack. |

No se observó una falla que bloqueara el handoff o requiriera reescribir el motor. La alerta SONG-002 sí justifica conservar el guardrail de integridad descriptiva. Los resúmenes de validación no deben ocultar que algunos problemas solo se vieron después de la primera revisión o al inspeccionar el MIDI.

La **recuperación de fallos de proceso está demostrada de forma acotada**: el límite temporal y la cobertura MIDI se corrigieron sin cambiar las decisiones musicales; la omisión de percusión se resolvió mediante una R1 autorizada y aceptada. Esto prueba que el flujo pudo recuperarse en estos casos, no que detecte automáticamente toda clase de error. No se encontró evidencia de una limitación concreta del genre pack ni de un vacío genuino de conocimiento.

## 10. Evaluación de vacíos de conocimiento

**Vacíos genuinos que bloqueen completar una canción: ninguno demostrado.** En los incidentes documentados, el proceso necesitó una decisión explícita, una revisión de integración, una corrección de materialización, una prioridad del Owner o confirmación por escucha; la evidencia no muestra que una regla compositiva ausente impidiera enumerar, filtrar o terminar las obras.

El ranking general sigue sin demostrarse. Eso es una limitación conocida de alcance: no hubo tarea apropiada de RANK-1, RANK-2 no existe en esta versión, y las preferencias artísticas resolvieron alternativas legítimas. No hay evidencia de que inventar criterios comparativos ahora mejoraría las decisiones ya cerradas. No se asignan prioridades P0/P1/P2 y no se propone nueva investigación para SONG-004.

## 11. Evaluación de arquitectura

La arquitectura actual conserva una separación útil entre intención, opciones, criterios, prioridad artística, decisiones musicales, SongPlan y materialización. Las trazas ofrecen inspección y el flujo ha admitido tanto una revisión controlada como elecciones prospectivas de percusión. Los fallos localizados produjeron correcciones limitadas y trazables.

El chequeo de etiquetas armónicas es una salvaguarda manual de documentación/proceso, no una nueva capacidad del motor. En SONG-003 se aplicó correctamente a 24 asignaciones, pero su ruta de advertencia no ha sido probada en un caso nuevo. El procedimiento debe mantenerse como guardrail explícito al preparar SONG-004. La evidencia no apoya una reparación arquitectónica obligatoria antes de continuar.

## 12. Preparación para SONG-004

**READY WITH SPECIFIC GUARDRAILS.** Composer MVP v1.1 demuestra capacidad suficiente para iniciar SONG-004 dentro de su alcance actual, sin tratar las decisiones aceptadas como conocimiento universal. Para el próximo handoff:

- resolver N3-P prospectivamente desde la intención de groove y dejar registrada una de las opciones, sin asumir percusión obligatoria;
- cotejar cada etiqueta armónica relevante con las pitches explícitas de su track; documentar semántica intencional de omisión, adición, inversión o doblaje, o registrar WARNING si queda inexplicada;
- revisar cobertura de secciones, duraciones/bounds y mapeo MIDI antes de cerrar la materialización;
- conservar opciones, filtros, prioridades del Owner y dependencias cross-domain en la traza;
- dejar la aceptación artística final a la escucha del Owner.

Esta preparación no compone SONG-004 ni altera los artefactos auditados.

## 13. Siguiente acción recomendada

Que el Project Owner autorice el brief de SONG-004 para iniciar una nueva composición bajo Composer MVP v1.1 y los guardrails indicados.
