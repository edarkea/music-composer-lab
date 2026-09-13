# SONG-001-R1 ? Traza de decisi?n

## Prop?sito y alcance

SONG-001-R1 conserva la composici?n SONG-001 y a?ade una arquitectura completa
de bater?a para comparar en REAPER la versi?n sin drums con una realizaci?n
r?tmica apoyada por drums. El Project Owner escuch? la iteraci?n intermedia de
bombo aislado y determin? que no era suficiente; esta actualizaci?n reemplaza
esa arquitectura. El dise?o r?tmico se registra aqu? como decisi?n de esta pieza,
no como regla o evidencia de g?nero.

Se preservan tempo 122, comp?s 4/4, centro C j?nico, forma y orden `opening` ?
`build` ? `focal` ? `release`, longitudes, armon?a, lead, bajo y texture. No se
cambian sus pitches, ritmos, velocidades ni asignaciones. No se corrigen los
solapamientos aceptados del bajo ni se alteran sus velocidades.

## DRUM / PERCUSSION ARCHITECTURE DECISION

### Requisito del Owner y entradas

- **Requisito art?stico:** completar una parte de drums funcional en las cuatro
  secciones; un bombo aislado o una capa trivial repetitiva no satisface la
  escucha prevista.
- **Prioridad art?stica:** reforzar orientaci?n al baile, groove e intensificaci?n
  gradual sin desplazar el lead focal ni reescribir el material original.
- **Input de g?nero disponible:** el Composer Genre Pack v1 GP-01/GP-04 permite
  considerar capas y densidad para diferenciar secciones loop-based. No prescribe
  patrones de bater?a. Las notas de ritmo e instrumentaci?n de `genres/indie-dance/`
  permanecen vac?as.
- **Input general:** SONG-001 ya tiene ataques del bajo en beats 1 y 3 y una
  textura sincopada en `build`/`focal`. Se toman como material concreto para
  coordinar y dejar espacio; no se infiere una regla general de bater?a.

### Mapeo t?cnico fijo proporcionado por el Owner

El mapa Steven Slate recibido del Project Owner es **TECHNICAL MATERIALIZATION
INPUT**, no conocimiento compositivo, evidencia de g?nero ni decisi?n a optimizar.
Se conserva literalmente en `maps/song001_r1_steven_slate_map.yaml`:

| Voz | Pitch MIDI |
|---|---:|
| kick | 36 |
| snare | 38 |
| rimshot | 40 |
| closed_hat | 44 |
| open_hat | 46 |
| pedal_hat | 42 |
| low_tom | 41 |
| mid_tom | 45 |
| high_tom | 48 |
| crash | 55 |
| ride | 51 |
| ride_bell | 53 |
| cowbell | 50 |

No se infiere ni altera ninguna correspondencia. Solo se usan las voces
necesarias para esta composici?n; las restantes siguen disponibles en el mapa.

### Pregunta, estrategias y filtros

**Pregunta:** ?qu? parte r?tmica recurrente con desarrollo por secci?n puede
completar la trayectoria de SONG-001 y mantener el lead en primer plano?

**Estrategias consideradas:** (A) patr?n denso e id?ntico desde el inicio; (B)
bombo m?s una sola subdivisi?n repetida en las cuatro secciones; (C) motivo de
pulso reconocible con backbeat y subdivisi?n que entran o cambian seg?n la
funci?n seccional, un fill localizado antes de `focal` y retirada progresiva en
`release`; (D) variaci?n continua y uso de numerosos colores en cada comp?s.

**Filtros:** cumplir el requisito de parte completa; conservar identidad por
recurrencia; desarrollar solo donde ayude a la funci?n de secci?n; mantener
velocidades de acompa?amiento por debajo de las del lead como orientaci?n de
jerarqu?a, para confirmar al escuchar; evitar golpes que dupliquen sin prop?sito
la textura sincopada; reservar el fill para la transici?n formal que lo justifica;
no usar crash en cada frontera; excluir color que no aporte una funci?n clara.

**Selecci?n:** estrategia C. El pulso de bombo en beats 1 y 3 vuelve como ancla;
el backbeat y las subdivisiones se densifican desde `opening` a `focal`, mientras
un ?nico fill prepara la entrada focal. `release` retira capas y cierra con una
cola despejada. Es una selecci?n art?stica para SONG-001, no una afirmaci?n de
patr?n ?ptimo ni convenci?n universal de indie-dance.

### Comportamiento por secci?n

| Secci?n | Decisi?n prospectiva | Relaci?n funcional buscada |
|---|---|---|
| `opening` | Bombo en 1 y 3; closed hat en algunos contratiempos; snare aparece solo en beats 4 de los compases 2 y 4. Sin crash ni fill. | Establecer el pulso y anticipar una identidad r?tmica sin entregar todav?a el groove completo. |
| `build` | Conserva bombo 1 y 3; snare en 2 y 4 casi toda la secci?n; closed hat en los contratiempos. Se reduce la actividad del ?ltimo comp?s para un fill low?mid?high tom en 3&?4?4&. | A?adir backbeat y subdivisi?n de forma controlada; el fill ?nico articula el paso a `focal`. |
| `focal` | Groove m?s completo: bombo 1 y 3, snare 2 y 4, closed hats en contratiempos y open hat sustituyendo algunos de ellos. Un crash marca solo la entrada de esta secci?n. | Concentrar la mayor continuidad y variedad t?mbrica de la bater?a bajo el lead. |
| `release` | Conserva el pulso al principio, reduce despu?s el bombo, retira primero el snare y termina el ?ltimo comp?s con solo el golpe inicial. Closed/pedal hats escasos; sin fill ni crash final. | Desmontar gradualmente el groove y dejar espacio al final abierto existente. |

### Recurrencia y desarrollo

**Permanece identificable:** bombo sobre beats 1 y 3 como referencia recurrente;
relaci?n de backbeat en beats 2/4 cuando la capa snare est? activa; hats como
subdivisi?n del pulso.

**Cambia:** densidad del hat, regularidad del snare, duraci?n del pulso de bombo
dentro de `release`, articulaci?n closed/open/pedal, acento crash aislado y un
fill de toms.

**D?nde y por qu?:** la parte empieza parcial en `opening`, gana continuidad en
`build`, alcanza su realizaci?n m?s completa en `focal`, y pierde elementos de
forma escalonada en `release`. El fill solo aparece al final de `build`, donde
prepara la secci?n focal. No hay fills peri?dicos; no se a?ade crash a todas las
entradas; ride, ride bell, rimshot y cowbell no se usan porque no se les asign?
una funci?n necesaria para este arreglo.

### Interacci?n transversal y jerarqu?a

- **Bajo:** el bombo coincide con ra?ces en beats 1/3 como refuerzo deliberado.
  No se cambian notas, velocities ni overlaps del bajo. Las quintas anticipadas
  permanecen intactas.
- **Lead:** la mayor actividad percusiva acompa?a la secci?n focal, pero sus
  velocidades son contenidas y no se a?aden l?neas pitched. El criterio de
  prioridad es conservar la melod?a como foco; la claridad real debe confirmarse
  en REAPER con el kit Steven Slate.
- **Texture:** la textura conserva los contratiempos existentes en build/focal.
  Los hats evitan convertir cada onset de textura en unisono permanente; coinciden
  en algunos puntos por dise?o de subdivisi?n.
- **Energ?a de secci?n:** se usa entrada/sustracci?n de voces, densidad y
  articulaci?n como medios de contraste. El campo `energy` original permanece
  sin cambios y no se interpreta como volumen de MIDI.

## Registro de decisi?n anterior

La iteraci?n materializada primero para R1 conten?a solo kick. Tras escucharla, el
Project Owner indic? que esa realizaci?n no cumpl?a la intenci?n. La arquitectura
completa documentada en este bloque la sustituye dentro de SONG-001-R1; el kick
anterior no se conserva como versi?n final ni como decisi?n compositiva aprobada.

## Clasificaci?n epistemol?gica

- **GENERAL COMPOSITION KNOWLEDGE:** no se invoca una regla general nueva. Se
  consideran por separado pulso, acento, subdivisi?n, densidad y capas como
  par?metros editables.
- **GENRE SPECIALIZATION:** GP-01/GP-04 permite diferenciar una forma loop-based
  mediante capas/densidad dentro de su alcance; el pack no respalda estos patrones
  espec?ficos de drums.
- **ARTISTIC PRIORITY:** el patr?n, sus posiciones, la trayectoria por secciones,
  fill, articulaciones elegidas y prioridad del lead son decisiones de esta
  realizaci?n bajo la direcci?n expl?cita del Owner.
- **TECHNICAL MATERIALIZATION INPUT:** mapa Steven Slate exacto y external map
  SongPlanV2 requerido por el motor. Pitch MIDI no determina por s? mismo la
  funci?n musical.

## L?mites y audici?n

No se afirma que esta arquitectura sea objetivamente ?ptima, que asegure una
identidad de g?nero ni que generalice a otras canciones. La escucha A/B del Owner
debe comparar orientaci?n al baile, groove, trayectoria de energ?a,
diferenciaci?n, claridad del lead e impresi?n estil?stica, usando los mismos
sonidos originales y el kit Steven Slate en la pista `drums`. La revisi?n es
simb?lica/MIDI; no se gener? WAV.


## Cierre de escucha

El Project Owner escuch? SONG-001-R1 en REAPER y la **ACEPTA**. En particular,
considera satisfactorios el desarrollo completo de percusi?n, el fill antes de
`focal`/cl?max y la integraci?n de kick/hats contenidos con el bass. No solicita
revisi?n del material pitched. Esta es una preferencia/decisi?n art?stica sobre
esta composici?n; no a?ade evidencia compositiva o de g?nero.
