# SONG-003 - Traza de decisiones Composer MVP v1.1

## Estado y brief

SONG-003 es una composicion nueva para probar diversidad de decisiones dentro
Composer MVP v1.1. El brief pide una pieza instrumental indie-dance/electronic-pop
mas brillante y kinetica que SONG-001/002, juguetona, bailable, con mayor
contraste seccional, identidad focal clara, una llegada de energia principal y
un final breve e intencional. La repeticion debe aportar desarrollo audible.

Esta traza se registra antes de serializar `SONG-003.songplan.yaml`. No usa los
materiales musicales previos ni pretende validar conocimiento cientificamente.
La realizacion FM8 que pueda usarse despues es contexto de audition, no decision
de timbre ni evidencia compositiva.

## N0 - Intencion song-level

- **Pregunta:** como crear impulso y contraste jugueton sin hacer que todas las
  capas esten al maximo ni derivar la identidad de una sola capa dominante?
- **Opciones:** arco persistente con variaciones leves; contraste por secciones
  regulares; forma breve con retirada clara, reentrada y coda.
- **Restricciones:** una sola llegada principal; identidad conservable durante
  los cambios; no copiar soluciones de SONG-001/002; no introducir una regla
  general ni ranking global.
- **Filtros:** satisfacer el brief brillante/kinetico, permitir un valle audible
  antes de la llegada y acabar con una accion breve distinguible.
- **Base:** CK-SONG-01 permite declarar intencion y dependencias, no seleccionar
  una forma universal. GP-04 permite explorar diferenciacion por capas,
  actividad y entradas/salidas en el alcance loop-based/pop del MVP.
- **Seleccion - ARTISTIC PRIORITY:** impulso jugueton con una caida marcada,
  reentrada expansiva y coda de dos compases.

## N1 - Forma y funciones

- **Alternativas:** cuatro secciones iguales; cinco bloques de build regular;
  seis secciones desiguales con un pocket retirado y una coda corta.
- **Seleccion - ARTISTIC PRIORITY:** `spark` (4 compases) -> `stride` (6) ->
  `pocket` (4) -> `lift` (2) -> `arrival` (6) -> `button` (2), total 24.
- **Roles:** establecer la llamada; convertirla en movimiento; retirar kick/snare
  y bajar actividad; reintroducir actividad en dos compases; una llegada focal de
  seis compases; cerrar con un tag de dos compases y ataque final corto.
- **Metadatos de energia:** 0.30 / 0.58 / 0.22 / 0.63 / 0.90 / 0.35 describen
  solo una trayectoria relativa y no generan audio.
- **Comparacion:** SONG-001 emplea cuatro bloques regulares de cuatro compases;
  SONG-002 usa 4/8/4/8/4 y 28 compases. La forma 4/6/4/2/6/2 y su retirada breve
  se seleccionan para este brief; no son plantilla de genero.

## N2 - Identidad, melodia y jerarquia focal

- **Pregunta:** que identidad puede conectar frase y ritmo sin asumir que lead
  o bajo debe dominar?
- **Alternativas:** lead continuo sobre soporte; bajo como protagonista;
  relacion compartida entre llamada melódica corta y respuesta percusiva.
- **Filtro:** la identidad debe sobrevivir la retirada de `pocket` y la expansion
  de `arrival`; no depender de densidad continua.
- **Base:** CK-MEL-01/02 y CK-DEV-01 permiten declarar semilla, recurrencia y
  cambio parcial. No garantizan memorabilidad. `HOOK != PROMINENCE !=
  MEMORABILITY`; no aplica CK-CROSS-01/RANK-1, pues no se hace tarea de
  reconocimiento comparativo.
- **Seleccion - ARTISTIC PRIORITY:** foco compartido: llamada corta de lead y
  respuesta de cowbell/percusion. El bajo sostiene el cambio armonico y el pulso,
  sin ocupar el primer plano decidido para esta pieza.
- **Celula melodica:** dos compases. Compas local 1: B4 en 1&, D5 en 2&, F#5
  en 3 y E5 en 4&. Compas local 2: G#5 en 1, B5 en 2, A5 en 3& y D5 en 4&.
  Material enteramente nuevo; pitches y onsets quedaran escritos en el plan.
- **Registro/variacion:** las primeras apariciones mantienen la llamada en
  registro medio-alto; `pocket` conserva solo fragmentos; `lift` conduce hacia
  B5; `arrival` reitera la celula y varia su ultima respuesta; `button` reduce a
  un gesto final. No se afirma memorabilidad garantizada.
- **Comparacion:** SONG-001 puso el foco en lead continuo; SONG-002 dio al bajo
  protagonismo del groove. SONG-003 elige una relacion lead-percusion compartida
  y un bajo de apoyo; no se copia ninguna frase.

## N3a - Marco y realizacion armonica

- **Pregunta:** que marco armonico permite color mayor brillante y cambios
  audibles, manteniendo legibilidad en secciones contrastantes?
- **Alternativas:** ciclo de cuatro acordes; pedal persistente; ciclo modal con
  cambios por seccion.
- **Seleccion - ARTISTIC PRIORITY:** centro E, modo mixolidio; seis sonoridades
  de triada explicita: E mayor, A mayor, F# menor, B menor, D mayor y C# menor.
  Este marco no reutiliza C-Am-F-G (SONG-001) ni Am9-D6-Am9-G6 (SONG-002).
- **Ritmo armonico:** un acorde por compas. Los acordes se sostienen en `spark`
  y `pocket`; las mismas alturas reciben ataques mas cortos en `stride`, `lift`
  y `arrival`. `button` termina con E mayor y un acorde final breve. El cambio
  de articulacion no se presenta como cambio de armonia.
- **Recorrido por compases:**
  - 1-4 `spark`: E, A, F#m, Bm.
  - 5-10 `stride`: D, A, E, Bm, C#m, A.
  - 11-14 `pocket`: C#m, D, Bm, A.
  - 15-16 `lift`: C#m, D.
  - 17-22 `arrival`: E, D, A, Bm, E, D.
  - 23-24 `button`: E, E.
- **Voicings explicitos:** E = [E3,G#3,B3]; A = [A3,C#4,E4]; F#m =
  [F#3,A3,C#4]; Bm = [B2,D3,F#3]; D = [D3,F#3,A3]; C#m = [C#3,E3,G#3]. No se
  planifican inversiones, omisiones ni adiciones: cada etiqueta nombra la
  triada que aparece en harmony.
- **Diagnostic label/voicing:** cada asignacion de un compas se comparara con
  el pitch set explicito en la pista harmony. Estado prospectivo: `CONSISTENT`
  para las 24 etiquetas; el proceso audit conservara compas, etiqueta, pista,
  pitches y resultado. No se inferira funcion desde pitches aisladas ni se
  exigira una lista teorica mayor que la realizacion declarada.
- **Base:** CK-HAR-01/02/03 separan cifrado de sonoridad y dejan abierta la
  realizacion; no hay progresion optima.

## N3b - Metro, groove y bajo

- **Seleccion artistica:** 4/4 a 132 BPM. La sensacion kinetica se construye
  mediante llamada sincopada, respuestas, articulacion armonica y cambios de
  capas; no mediante velocidad de playback o velocity por si solas.
- **Bajo:** raices armonicas en registro grave con pocas notas por compas.
  `spark` y `stride` usan raiz en beat 1 y quinta en beat 4 o beat 3; `pocket`
  sostiene raices; `lift` anticipa una salida; `arrival` mantiene raiz/quinta
  sencillas; `button` deja E grave corto. El patron no copia las raices/quintas
  de SONG-001 ni las celulas mas activas de SONG-002.
- **Foco ritmico:** hats/cowbell responden a los huecos de la llamada de lead;
  kick/snare anclan secciones de movimiento, se sustraen en `pocket`, crecen en
  `lift` y `arrival`, y cesan tras el tag final.
- **Base:** CK-RHY-01 filtra posiciones respecto del compas declarado; CK-RHY-02
  no impone densidad o aceleracion. Ninguno prescribe este patron.

## N3-P - Arquitectura de percusion

**Decidida antes de SongPlan mediante el flujo normal v1.1; no proviene de un
recordatorio para incluir drums.**

- **Pregunta/objetivo:** que arquitectura respalda un indie-dance jugueton,
  kinetico y contrastante, preservando una identidad compartida con el lead?
- **Candidatos:** `FULL`; `MINIMAL`; funcion delegada a bajo/armonias; ninguna
  percusion intencional.
- **Filtro:** el brief pide movimiento bailable y contraste claro; la ausencia o
  delegacion siguen siendo validas, pero no aportan la respuesta percusiva
  elegida para la llamada ni el contraste de reentrada. `MINIMAL` tambien podria
  bastar, pero reduce estratos de respuesta; FULL no exige actividad maxima en
  cada seccion.
- **General:** CK-RHY-01/02 permiten razonar sobre onsets y actividad contextual,
  no ofrecen receta de bateria ni obligacion de percusion.
- **Genero:** GP-01/04 permite considerar capas, entradas y densidad en una
  realizacion loop-based/pop; no impone kit o patron.
- **Seleccion - ARTISTIC PRIORITY:** **FULL PERCUSSION** con kick, snare,
  closed_hat, open_hat y cowbell. Se busca una llamada/respuesta ritmica y una
  llegada llena, no una ley de genero.
- **Desarrollo seccional:** `spark`, kick ligero y color de hat/cowbell; `stride`,
  kick sincopado, snare desplazado y subdivisiones; `pocket`, se retiran kick y
  snare, quedan respuestas finas; `lift`, regresan capas y subdivision; `arrival`,
  realizacion mas completa con cowbell y open_hat selectivos; `button`, un tag
  corto coordinado y luego silencio.
- **Diferencia frente a SONG-001-R1:** se admite la misma clase amplia FULL solo
  por decision nueva; el plan evita copiar su backbeat/patrón de hats/toms. El
  kick de SONG-003 incluye anticipaciones y el cowbell responde a la celula como
  parte de la identidad. Frente a SONG-002, la eleccion es FULL, no MINIMAL.
- **Mapa:** usar `song001_r1_steven_slate_map` solo como entrada tecnica fija:
  kick 36, snare 38, closed_hat 44, open_hat 46, cowbell 50. No determina voces
  musicales, acentos ni onsets.

## N4 - Capas, contraste y textura

- **Jerarquia:** relacion compartida lead/cowbell; armonia como soporte ritmico y
  tonal; bajo grave de apoyo; percusion como respuesta y anclaje. No se anade
  otra linea pitched para no competir con la llamada.
- **Contraste:** alternar armonia sostenida vs. articulada, llamada completa vs.
  fragmento, presencia vs. retirada de kick/snare y percusion ligera vs. completa.
  El pocket reduce capas; la llegada es la unica seccion de maximo energy (0.90
  como metadato) y mayor reunion de estratos.
- **Comparacion:** se diferencia de la textura mas persistente de SONG-001 y de
  SONG-002, donde el bajo era protagonista; no se afirma que esta jerarquia sea
  mejor en general.

## N5 - Recurrencia y desarrollo

- **Que permanece:** contorno rítmico de dos compases, relacion llamada/respuesta,
  centro E y secuencia de acordes reconocible dentro de cada bloque.
- **Que cambia:** fragmentacion en `pocket`, anticipacion en `lift`, mayor
  realizacion de capas en `arrival`, cambio de finales de lead y articulacion
  armonica por seccion.
- **Por que:** el material retorna en condiciones distintas para que el retorno
  final a la llamada tenga otro contexto; evitar copia literal de todas las capas
  y evitar novedad sin relacion.
- **Limite:** el plan hace audibles las operaciones estructurales; si la
  recurrencia se percibe como desarrollo o mantiene identidad lo decide la
  escucha del Owner.

## N6 - Tension, release y final

No se usa scalar de tension. Se coordinan por separado continuidad/retirada de
capas, densidad de eventos por pista, actividad de percusion, armonia por compas,
registro del lead y expectativa de reentrada. `pocket` es un valle planificado;
`lift` reintroduce actividad; `arrival` es el unico maximo planeado. `button`
recupera E mayor y concluye con un acorde final corto en beat 1 del compas 24,
seguido de silencio. Esto es una intencion estructural, no una garantia de cierre
percibido.

## N7 - Conflictos, guardrails y diversidad

No aparece conflicto que requiera revision de una decision minima antes del
handoff. Se explicitan las dependencias: acordes/raices se coordinan; percusion
responde al lead; el bajo apoya y no compite; el pocket retira kick/snare; la
llegada suma capas sin cambiar la semilla.

### Guardrails previos

| Guardrail | Estado | Evidencia |
|---|---|---|
| Hook/prominence/memorability separados | PASS | No claim de memorabilidad ni RANK-1. |
| Metrica no equivale a prominencia/funcion | PASS | Posiciones elegidas localmente. |
| Harmony labels vs pitches explicitas | PASS | 24 labels comparadas contra voicings exactos; sin omisiones/adiciones. |
| Tension multidimensional, sin scalar | PASS | Se registran capas, armonia, registro y reentrada por separado. |
| Focal hierarchy explicitada y comparada | PASS | Llamada de lead y respuesta de percusion, bajo de soporte. |
| Contraste no se infiere de un parametro unico | PASS | Se coordinan articulacion, entradas, actividad y fragmentacion. |
| N3-P evaluada entre cuatro resultados | PASS | FULL, MINIMAL, DELEGATED y NONE permanecen opciones validas. |
| Mapeo tecnico separado de patron musical | PASS | Mapa solo resuelve notas MIDI. |
| Cross-domain conflict | NOT APPLICABLE | No se detecto conflicto que fuerce revision. |

Resultado: 8 PASS / 0 WARNING / 1 NOT APPLICABLE.

### Comparacion de diversidad

| Dimensiones | SONG-001 | SONG-002 | SONG-003, decision independiente |
|---|---|---|---|
| Forma | 4x4 | 4/8/4/8/4, 28 compases | 4/6/4/2/6/2, 24 compases; valle y coda |
| Armonia | C-Am-F-G | Am9-D6-Am9-G6 | E Mixolydian; E/A/F#m/Bm/D/C#m y nueva secuencia |
| Foco | Lead persistente | Bajo protagonista | Relacion lead/cowbell compartida; bajo de apoyo |
| Groove | Bajo raiz/quinta persistente | Bajo sincopado al frente | Respuesta lead-percusion y kick anticipado |
| Percusion | Original sin drums; R1 FULL | MINIMAL | FULL, con otra organizacion; coincide solo la clase amplia con R1 |
| Desarrollo | Capas + variacion del lead | Build por actividad de capas y bajo | Retirada pocket, llamada fragmentada y reentrada FULL |
| Textura | Lead/texture/support | Lead, harmony, bass, percusion minima | Lead/respuesta, triadas articuladas, bajo sobrio, cinco voces de percusion |
| Final | Release abierto | Afterglow modal prolongado | Tag corto en E y silencio tras el ultimo acorde |

Diversity audit: **PASS vs SONG-001 y PASS vs SONG-002**. No se copia material
nota a nota. La clase FULL coincide con SONG-001-R1, pero los patrones y la
funcion focal no se reutilizan; la diversidad no exige que cada categoria cambie.

## Handoff y contabilidad

SongPlanV2 recibira seis secciones, armonia por compas, pitches/voicings
explicitos, motivos con eventos locales que cubren exactamente cada seccion,
bajo, percusion semantica y asignaciones. Cada pitch, onset, duracion y velocity
es una decision musical explicita; style/energy no generan audio.

- Nodos principales N0-N7: 8.
- Subdecision dependiente N3-P: 1.
- Decisiones registradas: 9.
- Artistic-priority handoffs: 8 (N0, N1, N2, N3a, N3b, N3-P, N4, N6).
- RANK-1: 0; RANK-2: 0.
- Revisiones cross-domain: 0.
- Decisiones sin base / defaults musicales encubiertos: 0.
- Conocimiento, genero, manual, rules, candidatos, experimentos y music-engine: sin cambios.

La escucha del Owner queda pendiente. No hay resultado artistico, evidencia
cientifica ni afirmacion de que la forma, el modo, el hook o el groove funcionen
como se espera.
