# SONG-004 — Plan de composición propuesto

## Estado y alcance

**Estado:** planificación completa; decisiones artísticas propuestas para handoff al Project Owner.  
**Estado tras aprobación:** los handoffs están resueltos; composición autorizada.  
**Alcance de este artefacto:** plan previo a la composición. No contiene SongPlan serializado, motivos con notas, voicings de registro, eventos MIDI ni materialización.

La propuesta sigue el brief autorizado: pieza instrumental indie-dance/electrónica-pop, contenida y cinética, con tensión moderada, identidad recurrente, cambio entre capas sin build continuo y cierre deliberado. Las selecciones abajo son prioridades artísticas para esta pieza, no conclusiones derivadas de ranking o reglas universales.

## Plan central

### Centro tonal y dirección armónica

- Centro propuesto: **Re menor / Re eólico**.
- Paleta armónica propuesta: **Dm – Bb – C – Gm**, usando las triadas diatónicas del marco elegido.
- Contenido de clases de altura que deben describir los labels: Dm = D–F–A; Bb = Bb–D–F; C = C–E–G; Gm = G–Bb–D.
- Dirección de ocho compases para A: Dm → Bb → C → Gm, dos compases por acorde.
- B desplaza el punto de inicio y cierra el ciclo hacia el centro: Bb → C → Gm → Dm, dos compases por acorde.
- A' recupera el orden de A; la coda se apoya en Dm con duración decidida durante la composición.
- No se declara cadencia tonal obligatoria ni se prescribe la inversión, registro o doblaje de ningún acorde. Los pitches explícitos determinarán lo que suena; cualquier realización reducida, extendida o invertida deberá explicitarse junto a su etiqueta.

La elección D eólico ofrece un color menor y un centro diferente de los marcos C jónico, A dórico y E mixolidio de SONG-001–003. Esto es una decisión para lograr identidad en este brief, no una afirmación de que un modo produzca tensión.

### Tempo y metro

- Propuesta: **116 BPM, 4/4**.
- Prioridad: movimiento estable y contenido, con espacio suficiente para que el patrón focal y las retiradas se distingan.
- El tempo no implica por sí solo energía, carácter ni adecuación estilística; su función debe revisarse en la escucha.

### Estructura y curva de energía

**Propuesta formal: 28 compases, cuatro bloques funcionales.**

| Bloque | Extensión | Función y trayectoria prevista |
|---|---:|---|
| A | 8 compases | Establecer pulso, centro D y patrón focal recurrente; textura inicialmente contenida. |
| B | 8 compases | Desplazar el punto de inicio armónico y cambiar la relación entre patrón, bajo y capa sostenida; ampliar el campo sin un crescendo obligatorio. |
| A' | 8 compases | Retornar al ciclo de A; conservar una característica rítmica reconocible y alterar su soporte o distribución entre capas. |
| Coda | 4 compases | Simplificar capas y preparar una terminación deliberada en el centro armónico. La forma exacta del gesto final queda abierta. |

La trayectoria prevista es **establecimiento → expansión moderada → retorno transformado → reducción/cierre**. No se asignan valores numéricos de energía ni se confunden con dinámica MIDI. El bloque B no tiene que ser más intenso que A'; la jerarquía dependerá de las decisiones de arreglo.

### Instrumentación y roles

- **Patrón focal:** sintetizador pluck o instrumento pitched de ataque definido, en registro medio, con un ostinato de acordes o notas armónicas sincopado. Lleva la identidad rítmica principal.
- **Bajo:** sintetizador monofónico de apoyo armónico y corporal; conecta raíces y cambios de acorde, dejando espacio al patrón focal. No será por defecto la capa protagonista.
- **Capa armónica sostenida:** pad u órgano suave que prolonga parte de la sonoridad y ayuda a diferenciar el sostén armónico del ataque sincopado. Su densidad y registro se subordinan al foco.
- **Lead melódico:** intervenciones breves y espaciadas que contestan o alteran el patrón; no mantiene actividad continua ni desplaza automáticamente el foco.
- **Percusión acústica/electrónica independiente:** no se presupone batería. La propuesta N3-P es **PULSE / PERCUSSIVE FUNCTION DELEGATED TO OTHER LAYERS**: el pluck focal define articulación y subdivisión; el bajo apoya el pulso y los puntos armónicos. No se serializa una pista de drums independiente si el Owner aprueba esta arquitectura.

Los nombres anteriores describen funciones previstas, no decisiones de preset, mezcla o biblioteca de sonidos.

### Bajo y groove

El groove se construye por la interacción entre el patrón pitched sincopado y un bajo más espacioso. El bajo ancla los cambios armónicos y refuerza el pulso en puntos seleccionados; puede anticipar algún cambio si la relación con el patrón lo permite, pero la anticipación no es requisito. Se evitará duplicar todos los ataques del patrón focal por defecto.

La claridad del pulso se comprobará también en el bloque de menor densidad: si la delegación deja el pulso ambiguo en el plan o en escucha, se reabre la decisión N3-P afectada y se presenta una alternativa explícita.

### Textura armónica

Triadas explícitas como base, sostenidas por una capa armónica de menor actividad que el patrón focal. El movimiento de acordes no exige que todas las capas ataquen a la vez: el patrón puede articular una parte y la capa sostenida prolongar otra. No se agregan extensiones por densidad o color sin declararlas y ajustar el label correspondiente.

La auditoría etiqueta/voicing se hará antes de cerrar el SongPlan: cada asignación relevante se cotejará con los pitches escritos en la pista armónica designada. El esquema de clases de altura indicado en este plan es internamente consistente; todavía no existe un voicing concreto que validar.

### Motivo, progresión y transiciones

- La identidad recurrente será un patrón rítmico armónico compacto en el pluck; sus pitches exactos se decidirán al componer.
- Invariante propuesto: conservar la forma rítmica reconocible en A, A' y al menos una referencia en la coda.
- Variación propuesta: cambiar su soporte armónico, registro relativo o grado de completitud entre bloques, preservando la relación rítmica central. Las operaciones exactas se decidirán al componer.
- El lead introduce gestos cortos relacionados o contrastantes, no una melodía continua obligatoria.
- Las transiciones se apoyan en cambios de actividad, duración o retirada de capas al final de frase; no se prescriben fills de batería, crashes ni subdivisión continua.
- La coda conserva una relación reconocible con el patrón o su ritmo, reduce elementos y articula el cierre en Dm. La duración y el gesto final se decidirán con el material ya compuesto.

### Contraste previsto con SONG-001–003

- Frente a **SONG-001**, desplaza el foco del lead a un patrón armónico de registro medio y no propone un crecimiento continuo de capas.
- Frente a **SONG-002**, no hace del bajo el protagonista principal y no utiliza su marco A dórico de acordes extendidos ni su afterglow.
- Frente a **SONG-003**, no propone llamada/respuesta lead–cowbell ni batería FULL; usa un patrón armónico focal con funciones percusivas delegadas y una estructura A/B/A'/coda.
- La diferencia es una intención de diseño; su percepción solo podrá evaluarse después de materializar y escuchar. No se fuerza novedad si una decisión posterior perjudica la coherencia.

## Decisiones y capacidad de selección

Las alternativas pueden enumerarse y filtrarse según el brief y las dependencias. No se usa RANK-1 ni RANK-2: no hay una comparación con criterio sustentado que determine un ganador. Centro/modo, estructura, balance de foco, asignación percusiva y cierre son propuestas basadas en prioridad artística, no resultados de ranking.

## Handoffs artísticos al Project Owner

Handoffs aprobados por el Project Owner antes de iniciar la composición:

1. **Marco de tiempo y forma:** 116 BPM, 4/4 y estructura de 28 compases A/B/A'/coda con trayectoria sin build continuo.
2. **Identidad y armonía:** centro Re menor/Re eólico, ciclo Dm–Bb–C–Gm y patrón armónico sincopado como foco, con el bajo en rol de apoyo y lead espaciado.
3. **Arquitectura N3-P:** delegar las funciones de pulso/percusión en patrón focal y bajo, sin drums independiente, condicionado a que el pulso permanezca claro.

Estos son handoffs por preferencia artística; no son preguntas de investigación ni ranking. Si el Owner pide un cambio, se actualiza solo el paquete afectado y se revisan sus dependencias.

## Guardrail findings

- **Armonía:** no se encontró discrepancia en la propuesta de etiquetas y clases de altura del plan. Aún no hay pitches de SongPlan ni voicings de octava que permitan cerrar la comprobación de materialización.
- **Ruta de warning:** cualquier mismatch no explicado durante la composición detiene esa decisión armónica y se presenta como WARNING; no se corrige silenciosamente.
- **Percusión:** N3-P tiene una decisión explícita prospectiva propuesta como DELEGATED. Debe conservarse en la traza antes de serializar; FULL, MINIMAL, DELEGATED y INTENTIONALLY NONE siguen siendo opciones si el Owner solicita revisar esta propuesta.
- **Trazabilidad:** se contabilizarán los handoffs de prioridad artística que aparezcan durante la composición. No se abre ranking salvo que surja una necesidad real.
- **Conocimiento / arquitectura:** no se detectó un vacío bloqueante ni se modificó Composer Knowledge, arquitectura, genre pack, reglas, investigación, SongPlan o MIDI.

## Puerta de avance

**READY FOR SONG-004 COMPOSITION.** El Project Owner aprobó los tres handoffs; la composición fue autorizada y se realizó bajo este plan.

## Resolución de handoffs — 2026-09-13

El Project Owner aprobó los tres paquetes propuestos: 116 BPM / 4/4 / A–B–A'–coda de 28 compases; centro Re menor/Re eólico con patrón armónico sincopado focal, bajo de apoyo y lead espaciado; y N3-P DELEGATED mientras el pulso siga claro. Se cierra el bloqueo anterior y se autoriza la composición. No se abren handoffs adicionales durante la realización.


