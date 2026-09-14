# SONG-002 ? Traza de decisi?n Composer MVP v1.1

## Estado, origen y m?todo

SONG-002 es una composici?n nueva y el segundo caso de canci?n completa del
proyecto. Se elabor? prospectivamente con Composer MVP v1.1: la misma base de
conocimiento y el contrato de v1, con la subdecisi?n dependiente **N3-P ?
Percussion architecture**. v1 permanece hist?rico. No se us? SONG-001 como molde;
no se modifican SONG-001 ni SONG-001-R1.

La traza precede al SongPlan. Registra elecciones de composici?n, su alcance,
alternativas, base general y de g?nero, handoffs art?sticos, efectos esperados y
consecuencias cross-domain. Ninguna expectativa perceptiva se presenta como
resultado.

## N0 ? Intenci?n y alcance

- **Brief:** instrumental Indie-dance/electronic-pop dentro del alcance MVP;
  car?cter nocturno, dance-oriented pero contenido, mayor sensaci?n de avance
  que SONG-001, identidad focal reconocible, contraste moderado, build gradual a
  un ?nico foco de energ?a, release deliberado y repetici?n con desarrollo
  audible.
- **Pregunta:** ?qu? arquitectura breve de canci?n mantiene una identidad
  reconocible mientras acumula movimiento y luego lo transforma en un release
  intencional?
- **Alternativas:** loop casi constante con pocos cambios; forma contrastante;
  arco por capas con secci?n de pulso, preparaci?n, foco prolongado y
  `afterglow`.
- **Restricciones duras:** material nuevo; una sola secci?n principal de mayor
  energ?a; sin prescribir acorde, melod?a, drum pattern, instrumentaci?n ni
  secuencia formal antes de decidirlos; sin ranking global.
- **Filtros:** coherencia con intenci?n, foco legible, espacio para crecer y un
  final que no dependa solamente de bajar actividad.
- **General / genre:** CK-SONG-01 exige intenci?n y dependencias expl?citas;
  GP-01/GP-04 permiten considerar persistencia loop-based con diferenciaci?n
  cross-domain, no una forma obligatoria.
- **Selecci?n:** `ARTISTIC PRIORITY` elige continuidad nocturna con cambios
  coordinados, acento focal ?nico y retorno terminal, no una forma convencional
  preasignada.

## N1 ? Forma y trayectoria

- **Pregunta:** ?d?nde se establece el material, se hace visible el pulso, se
  prepara el foco, ocurre el ?nico pico y se articula el release?
- **Opciones:** cuatro bloques regulares; secciones muy contrastantes; cinco
  unidades con funciones y longitudes distintas.
- **Filtros:** habilitar un ?nico foco prolongado, graduar la entrada de capas y
  mantener un retorno terminal deliberado.
- **Genre input:** GP-04 permite diferenciar una organizaci?n loop-based por
  capas, densidad, timbre y entradas/salidas; no garantiza percepci?n de forma.
- **Selecci?n art?stica:** `threshold` (4 compases) ? `pulse` (8) ? `lift` (4)
  ? `focal` (8) ? `afterglow` (4), total 28 compases. Las longitudes dan dos
  vueltas de cuatro compases a las funciones `pulse` y `focal`, con una
  preparaci?n breve y un final diferenciado. Es una preferencia de esta canci?n,
  no una plantilla del g?nero.
- **SongPlan:** rangos 1?4, 5?12, 13?16, 17?24 y 25?28; `energy` codifica solo
  una trayectoria relativa como metadato, no una curva autom?tica de audio.

## N2 ? Identidad, lead y foco

- **Pregunta:** ?qu? material focal puede volver, variar parcialmente y seguir
  subordinando el acompa?amiento?
- **Opciones:** motivo exclusivamente pitch-based; c?lula de pitch/ritmo con
  colocaci?n desplazada; material nuevo por secci?n.
- **General:** CK-MEL-01/02 permiten explicitar semilla, relaci?n y recurrencia;
  CK-DEV-01 permite declarar qu? relaci?n se altera. Ninguno garantiza
  memorabilidad o ?xito perceptivo.
- **Genre:** GP-01 permite sostener material mel?dico mientras cambia la
  realizaci?n de otras capas; no obliga a repetirlo.
- **Selecci?n:** `ARTISTIC PRIORITY` establece como semilla una frase de cuatro
  compases cuyo gesto abre en A4, salta a E5, contesta con D5/F#5/C5 y retorna a
  A4. Se conserva ese conjunto r?tmico/intervalar en `pulse` y `focal`; var?an
  la cola de la segunda recurrencia, la densidad local y un punto alto en el
  segundo ciclo focal. `afterglow` recupera A4 con menos eventos y una nota final
  larga. El plan escribe pitches y onsets exactos.
- **Jerarqu?a:** el lead es `focal_lead`; armon?a sostenida, bajo y percusi?n
  quedan como soporte. No se a?ade una l?nea pitched `texture` independiente:
  la sonoridad arm?nica sostenida basta para el apoyo escogido y otra l?nea
  podr?a disputar el foco.
- **Hook guardrail:** el motivo tiene prominencia asignada, pero `HOOK !=
  PROMINENCE != MEMORABILITY`. No se reclama memorabilidad ni se usa CK-CROSS-01
  `RANK-1`: no es una comparaci?n de reconocimiento de material previamente
  establecido.

## N3 ? Groove, armon?a y movimiento

### N3a ? Marco arm?nico y realizaci?n

- **Pregunta:** ?qu? marco nocturno puede repetirse con una salida deliberada al
  final?
- **Opciones:** progresi?n dirigida con sensible; pedal ?nico; loop modal de
  cuatro acordes.
- **General:** CK-HAR-01 separa etiqueta y pitches realizados; CK-HAR-02/03
  dejan abiertas realizaciones compatibles. No hay una progresi?n ??ptima?.
- **Genre:** GP-02 admite loop/vamp como posibilidad contextual y recuerda que
  persistencia no crea por s? sola coherencia ni energ?a.
- **Selecci?n art?stica:** A Dorian y ciclo `Am9 ? D6 ? Am9 ? G6`, un acorde por
  comp?s. El ciclo persiste por `threshold`, `pulse`, `lift` y `focal`. En
  `afterglow` se usa `G6 ? D6 ? Am9 ? Am9`, ralentizando el cambio arm?nico en la
  llegada final a Am9. Es una llegada/retorno modal elegida; no se etiqueta como
  cadencia cl?sica ni se afirma cierre percibido.
- **Voicings:** se especifican como pitches en el track harmony, sin depender de
  labels `harmony` para generar notas.

### N3b ? Metro, pulso y bajo

- **Pregunta:** ?qu? relaci?n de ataques permite m?s avance que la base previa,
  sin convertir velocidad o densidad en proxy de energ?a?
- **Opciones:** pulso amplio con bajo sostenido; bajo sincopado sobre metro
  estable; actividad constante de todas las capas.
- **General:** CK-RHY-01 filtra onset/duraci?n respecto del metro declarado; no
  equipara beat fuerte con prominencia. CK-RHY-02 mantiene alternativas
  temporales dependientes del contexto y no prescribe aceleraci?n/densidad.
- **Genre:** la anticipaci?n de GP-05 solo ser?a opci?n condicional cuando el
  material/metro fueran compatibles; no se trata como firma de Indie-dance ni
  resultado garantizado.
- **Selecci?n:** `ARTISTIC PRIORITY` elige 4/4 a 118 BPM. El bajo alterna ra?ces
  y tonos del acorde con patrones por secci?n: `threshold` espaciado; `pulse`
  con segundo ataque en 2& y respuesta en beat 4; `lift` con anticipaciones;
  `focal` con una c?lula de cuatro ataques; `afterglow` vuelve a duraci?n larga
  y termina en A2. El tempo no cambia.
- **SongPlan:** todos los pitches, beats y durations ser?n eventos expl?citos.

## N3-P ? Percussion architecture

**Decisi?n registrada antes de serializar el SongPlan.** No se deriva de la
omisi?n anterior de SONG-001 ni de un recordatorio para poner drums.

- **Pregunta:** ?qu? arquitectura de percusi?n, si alguna, apoya el avance
  nocturno y dance-oriented manteniendo el car?cter contenido y el lead focal?
- **Objetivo:** a?adir referencia de pulso y subdivisi?n independiente, con una
  acentuaci?n estructural limitada y actividad graduada por secci?n.
- **Alternativas consideradas:**
  1. `FULL PERCUSSION`: varios estratos de kick, backbeat, subdivisi?n, fills y
     acentos durante toda la trayectoria;
  2. `MINIMAL PERCUSSION`: pocas voces funcionales, con cambios locales de
     entrada/densidad;
  3. `PULSE / PERCUSSIVE FUNCTION DELEGATED TO OTHER LAYERS`: bajo y material
     arm?nico-r?tmico llevan todas las funciones, sin track drums;
  4. `INTENTIONALLY NO PERCUSSION`: ninguna percusi?n y ausencia elegida como
     parte del car?cter.
- **Filtros/restricciones:** brief dance-oriented y mayor avance que SONG-001;
  car?cter nocturno y contenido; acompa?amiento bajo la jerarqu?a del lead;
  relacionar kick con bajo sin imponer un?sono; coordinaci?n con subdivisiones y
  textura; desarrollo por secciones sin llenar todos los espacios; representar
  solo voces que tengan funci?n.
- **General:** CK-RHY-01/02 permiten razonar sobre posici?n y actividad en
  contexto, pero no indican una receta de bater?a. No existe principio general
  del repositorio que exija percusi?n.
- **Genre:** GP-01/04 permite que capas y densidad porten contraste en una
  realizaci?n loop-based. El pack no dice que Indie-dance requiera drums, ni
  aporta un patr?n o instrumentaci?n espec?fica.
- **Filtrado:** la ausencia/delegaci?n permanece leg?tima; para esta intenci?n
  reduce la separaci?n expl?cita entre pulso del acompa?amiento y patr?n de
  bajo. `FULL` sigue siendo posible, pero a?ade estratos/acento que la prioridad
  de contenci?n no requiere. No se descarta como mala estrategia general.
- **Selecci?n:** **MINIMAL PERCUSSION**, por `ARTISTIC PRIORITY`: kick, closed hat
  y rimshot muy limitado. Esta es una preferencia local para el brief, no un
  requisito de g?nero ni un ranking. El patr?n usa el mapa Steven Slate
  previamente proporcionado y aprobado; esa correspondencia es solo
  **TECHNICAL MATERIALIZATION INPUT** (`kick` 36, `closed_hat` 44, `rimshot` 40),
  no informa la selecci?n r?tmica.
- **Secciones:** `threshold`, dos golpes de closed hat en 2& en compases 2 y 4,
  sin kick; `pulse`, kick en beat 1 y hats en 2&/4& cada comp?s; `lift`, kick en
  1/3, hats en 1&/3& y un rimshot en beat 4 del ?ltimo comp?s; `focal`, kick en
  1/3, hats en 1&/3& y rimshot en beat 4 de cada segundo comp?s; `afterglow`,
  kick en beat 1 y hat en 4& de sus dos primeros compases, un rimshot en beat 4
  del segundo, despu?s silencio percusivo durante la llegada final.
- **Desarrollo:** pulso inicial delegado parcialmente al bajo/harmony, entrada
  de kick en `pulse`, mayor kick/hats en `lift` y `focal`, menor frecuencia de
  rimshot para no crear un backbeat denso, y retirada de capas en `afterglow`.
  El patr?n de hats no duplica todas las posiciones de bajo.
- **Tradeoff:** se sacrifica una realizaci?n m?s llena y una subdivisi?n
  continua para priorizar contenci?n y espacio del foco. Se acepta que si la
  escucha juzga el pulso insuficiente, esa ser?a una evaluaci?n posterior, no
  raz?n para falsear la decisi?n actual.
- **Cross-domain:** kick coincide con el primer ataque de ra?z donde se decide;
  el bass conserva anticipaciones que no se cuantizan a los kicks; rimshot
  aparece como acento escaso; el foco mel?dico mantiene espacio; el pulso de hats
  aporta actividad sin a?adir otra l?nea pitched; las entradas/salidas ayudan a
  diferenciar secciones. Estos son objetivos de coordinaci?n, no f?rmulas
  universales.
- **SongPlan:** track `type: drums` con `drum_voice` sem?nticas y assignments
  expl?citos a las cinco secciones; mapa existente
  `song001_r1_steven_slate_map` como recurso t?cnico externo. La decisi?n queda
  trazada aqu? porque SongPlan conserva eventos, no rationale.

**N3-P v1.1 audit:** instanciada por el flujo normal desde la intenci?n r?tmica;
se evaluaron las cuatro salidas sin que el Owner ordenara a?adir drums. La
selecci?n es expl?cita, anterior al SongPlan y trazable al brief.

## N4 ? Capas y jerarqu?a focal

- **Pregunta:** ?qu? capas son necesarias y qu? queda fuera para evitar
  competencia?
- **Selecci?n:** lead monof?nico como foco; harmony en voicings medios sostenidos;
  bass grave con ataques definidos; drums minimal. No se a?ade otro track
  `texture` pitched. La identidad t?mbrica de plugins queda fuera: SongPlan no
  selecciona presets.
- **General/genre:** la jerarqu?a es una restricci?n de arreglo decidida; GP-01/
  GP-04 permiten mover parte del contraste a las entradas/densidad de drums,
  pero ning?n cambio aislado garantiza contraste percibido.
- **Consecuencia:** la acumulaci?n principal ocurre en pulso/subdivisi?n y
  desarrollo de lead, no en sumar capas instrumentales sin funci?n.

## N5 ? Recurrencia y desarrollo

- **Qu? permanece:** ciclo arm?nico/modal; c?lula mel?dica de cuatro compases;
  metro/tempo; centro focal del lead; relaci?n b?sica de kick al pulso donde
  entra.
- **Qu? cambia:** bajo y percusi?n aumentan actividad entre `threshold` y
  `focal`; el motivo recibe finales modificados en lift/focal; la ?ltima
  recurrencia de lead se fragmenta y sostiene A4; el ciclo arm?nico da paso a
  `G6?D6?Am9?Am9` en afterglow.
- **Por qu?/d?nde:** hacer identificable el material mientras las funciones de
  transici?n, foco y afterglow se distinguen por un conjunto limitado de cambios.
  La repetici?n no se trata como garant?a de memoria ni la densidad como energ?a
  autom?tica.
- **SongPlan:** cada motivo/asignaci?n y cada versi?n alterada se escribe
  expl?citamente; no se pide transformaci?n creativa al motor.

## N6 ? Contraste, tensi?n, release y final

No se calcula scalar de tensi?n. La trayectoria se compone con dimensiones
separadas: continuidad del loop, densidad de eventos por capa, registro/densidad
del lead, entradas/salidas y ritmo arm?nico. El pico ?nico es `focal`; su
realizaci?n se prepara en `lift`. El release no es solo retirada: retorna el
color de Am9, prolonga el material arm?nico final, adelgaza bajo/drums y deja A4
sostenido. **Final elegido:** llegada a A y continuidad terminal abierta, sin
claim de cadencia o cierre perceptivo. El Owner debe juzgarlo al escuchar.

## N7 ? Conflictos, guardrails y SongPlan handoff

No apareci? conflicto duro que obligue a reabrir una decisi?n. El presupuesto
de capas, voces/densidad del lead y posiciones de kick/hats se coordinan; los
metadatos `energy` y `harmony_assignments` no generan m?sica. No se modifica una
decisi?n por facilidad de codificaci?n.

### Guardrails antes de serializar

| Guardrail | Estado | Revisi?n |
|---|---|---|
| Hook/prominence/memorability son constructos distintos | PASS | No se reclama memorabilidad ni se usa RANK-1. |
| Posici?n m?trica no equivale a prominencia o funci?n | PASS | Beat/acento descritos como decisiones de este plan. |
| Harmony label no equivale a sonoridad | PASS | Pitches y voicings se escribir?n expl?citamente. |
| Energ?a de secci?n no genera din?mica | PASS | `energy` ser? solo metadato ordinal aproximado. |
| Loop/retorno no equivale a cadencia/cierre | PASS | Se declara llegada modal elegida, percepci?n abierta. |
| Cambio de densidad no garantiza energ?a/contraste | PASS | Efectos son objetivos para escuchar, no hechos. |
| Patr?n de percusi?n no es obligaci?n de g?nero | PASS | N3-P considera cuatro resultados; selecciona minimal localmente. |
| Staff/texture no compite con lead | PASS | No hay track pitched extra; velocidades/registro son soporte. |
| Mapeo MIDI y funci?n compositiva se mantienen separados | PASS | Recurso Steven Slate fijo; no determina la m?trica del patr?n. |
| Conflicto cross-domain no encontrado | NOT APPLICABLE | No se activa revisi?n de N7. |

Resultado previo: **9 PASS / 0 WARNING / 1 NOT APPLICABLE**.

### Handoff

SongPlanV2 2.0 recibe valores musicales expl?citos: secciones, pitches,
voicings, onsets, duraciones, velocities, drums sem?nticos, motifs y
assignments. `harmony_assignments` son etiquetas. La traza conserva objetivo,
alternativas, preferencias, l?mites y cross-domain rationale. La validaci?n
prueba el contrato; la materializaci?n determinista prueba ejecuci?n t?cnica,
no calidad ni ?xito de g?nero.

## Contabilidad de decisiones

- Nodos principales N0?N7: **8**.
- Subdecisi?n dependiente expl?cita N3-P: **1**.
- Decisiones/song-level registradas: **9**.
- Artistic-priority handoffs: **8** (N0 forma/global; N1 forma; N2 semilla/identidad; N3a marco arm?nico; N3b tempo/groove; N3-P arquitectura; N4 ausencia de textura pitched; N6 final abierto).
- `RANK-1` usado: **0**.
- `RANK-2`: **0**.
- Revisiones por conflicto cross-domain: **0**.
- Decisiones musicales no sustentadas o encubiertas como defaults t?cnicos: **0**.

## L?mites

El resultado es una primera composici?n MIDI simb?lica dentro del ?mbito del
MVP. No se ha escuchado a?n. No genera evidencia cient?fica, no valida claims
de conocimiento ni demuestra que el patr?n de bajo/percusi?n produzca groove,
que A Dorian produzca car?cter nocturno o que el final se perciba como se
pretende. Plugin, preset y reproducci?n pertenecen a la posterior audici?n en
REAPER.
