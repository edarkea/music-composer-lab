# Initial Harmonic Material Construction

## Estado

Sintesis de `RQ-HAR-010`. No es manual, regla, genero ni auditoria de
candidatos. El dominio permanece en estado candidato.

## Conclusion

La construccion armonica desde cero puede producir **varios seeds abstractos**
condicionados por centro, coleccion, organizacion, objetivo formal y restricciones
locales. Puede enumerar y filtrar material con alcance, pero no seleccionar una
progresion unica de forma generalmente justificada.

El seed puede ser una secuencia de relaciones, una region, un loop, un pedal,
un vamp, una trayectoria de bajo, una organizacion funcional bajo marco o un
patron de ritmo armonico. Ninguna representacion es primaria en todos los
contextos.

## Construction, organization, later fitness

### Construction

Construir no significa elegir acordes realizados. Primero puede decidirse una
representacion abstracta, una organizacion y unas relaciones. Las alturas exactas,
registro, inversion, spacing, duplicacion y asignacion pertenecen normalmente a
realization.

### Organization

`DIRECTED`, `CYCLIC`, `PERSISTENT` y `AMBIGUOUS` son organizaciones distintas.
Un loop puede ser forma ciclica; un pedal puede ser persistencia; una progresion
dirigida puede orientar hacia una meta; un vamp puede mantener una configuracion
sin sintaxis cadencial completa. La organizacion no determina calidad ni efecto.

### Fitness for later operations

La utilidad de un seed puede describirse operacionalmente:

- relaciones que pueden repetirse;
- material que admite cambio parcial;
- soporte compatible con melodias futuras;
- endpoint que puede continuar o llegar;
- relaciones que pueden retornar o expandirse.

Esto no demuestra que el seed sea bueno, memorable, interesante o adecuado para
un genero.

## Center and collection

Un centro puede restringir relaciones, recurrencia, pedal, finalis o esquemas.
Una coleccion puede restringir membresia de alturas y acordes. Centro y coleccion
son variables distintas; una coleccion diatonica no garantiza estabilidad y un
evento cromatico no garantiza tension.

Everett documenta varios sistemas tonales en rock, incluidos sistemas modales y
no funcionales. Temperley documenta colecciones amplias y shifts escalares, pero
no una receta de construccion ni pesos de cues. Spicer muestra centros fragiles,
emergentes y ausentes. Estos son marcos analiticos y observaciones de repertorio,
no una gramatica generativa universal.

## Directed, cyclic, persistent and ambiguous

### Directed

Puede construirse una relacion hacia una meta bajo un marco funcional o modal
declarado. V-I tiene valor dentro de ciertos marcos, no universalmente.

### Cyclic

Un loop o shuttle puede organizar recurrencia sin cadencia dirigida. La funcion
interna y la direccion percibida permanecen abiertas.

### Persistent

Pedal, vamp o region persistente pueden sostener material mientras el cambio se
traslada a otros niveles. Pedal no equivale a centro fijado en todos los casos.

### Ambiguous

La ambiguedad puede surgir de centros competidores, orden, metro, textura,
paralelismo, bajo o coleccion. No se dispone de una tecnica verificada para
construir ambiguedad a voluntad.

## Harmonic rhythm and extent

El numero de eventos, la duracion de una region y el ritmo armonico son
decisiones distintas. Tempo, densidad melodica y actividad del arreglo no son
ritmo armonico. No existe apoyo para una longitud optima de seed o progresion.

Caplin apoya aceleracion dentro de continuation de la sentence clasica, junto a
fragmentacion y liquidacion. Esta relacion es `TRADITION_SPECIFIC`; no se
transfiere a pop, loops o energia perceptiva sin evidencia adicional.

## Loops, vamps and pedals

La evidencia popular permite tratar loops, vamps y pedales como organizaciones
armonicas posibles. Butler describe diseno electronico basado en patrones
repetidos y transformaciones en otros dominios. Spicer documenta vamps y
tonicidad emergente/ausente. La reseña de Doll describe casos donde metro,
textura y paralelismo modifican la atribucion de centro.

Estas fuentes no sostienen:

- longitud optima;
- loop mas memorable;
- loop menos desarrollado;
- cierre automatico en la costura;
- percepcion seccional desde textura sola.

## Formal-goal conditioning

Form permite declarar el objetivo y la escala, pero solo ofrece informacion de
meta. Las relaciones formales con medios armonicos son:

- `establish`: puede orientar a recurrencia/soporte, sin escoger un acorde;
- `continue`: no implica mas cambios, fragmentacion o aceleracion;
- `prepare`: puede orientar relaciones hacia una meta, sin exigir dominante;
- `arrive`: puede orientar a una llegada, no necesariamente cadencial;
- `remain open`: puede orientar persistencia o terminalidad diferida;
- `contrast`: puede orientar otra organizacion o coleccion, sin exigir cambio de
  centro;
- `return`: puede orientar reaparicion exacta o transformada, sin preferencia
  universal.

El resultado mas firme es `GOAL INFORMATION -> FILTER WITH SCOPE`. El ranking
continua bloqueado.

## Harmony-first versus melody-constrained

Harmony-first puede generar un espacio de apoyo para melodias futuras; no
garantiza una melodia mejor. Melody-constrained puede reducir armonias
admisibles; no determina una seleccion unica. Esta conclusion pertenece a la
frontera de seleccion y no reabre `RQ-HAR-009`.

## Enumerate / Filter / Rank

| Decision | Enumerate | Filter | Rank | Estado |
|---|---|---|---|---|
| representation | yes | yes with scope | no | no universal primary representation |
| organization | yes | partial | no | goals and traditions differ |
| center/collection | yes | yes with framework | no | center != collection |
| relations | yes | yes with framework | no | label/function/root motion diverge |
| event extent | yes | partial | no | no length rule |
| harmonic rhythm | yes | yes with declared unit | no | tempo and meter dependencies |
| recurrence/loop/pedal | yes | genre-scoped | no | perception and seam open |
| arrival/open behavior | yes | partial | no | arrival != cadence != closure |

## Structure, perception, composition

The strongest current claims are structural and negative. A construction can be
described and filtered by explicit constraints. Perceptual claims about direction,
stability, openness, tension, coherence or memorability remain bounded, partial
or unverified. Compositionally, the system can preserve alternatives and expose
tradeoffs; it cannot justify one progression globally.

## Candidate audit evidence gate

**PASS.** La auditoria se completo sin promocion. `CAND-HAR-053`, `055`,
`056`, `058` y `059` quedan como `POSSIBLE_WITH_SCOPE` despues de revision.
`CAND-HAR-054` y `057` quedan como `NOT_READY` porque su puente especifico
hacia construccion inicial aun no supera la duplicacion o la insuficiencia de
evidencia.

La principal correccion es que la construccion armonica puede usar objetivos,
organizacion, centro, coleccion y aptitud para operaciones futuras como filtros
acotados, pero ninguno produce un ranking general. Las representaciones son
grados de abstraccion y no una arquitectura compositiva validada. Ambiguous se
mantiene como estado diagnostico, no como categoria exhaustiva. Loop, vamp y
pedal quedan como ejemplos no sinonimos de recurrencia o persistencia.

## Audit status

`RQ-HAR-010` queda en `SYNTHESIZED` con `candidate_audit_status:
COMPLETED`. No se creo `CAND-HAR-060` y no se actualizo Composer Foundations.
