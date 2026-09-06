# EXP-003 - Deterministic audio/rendering specification

## Status

- `experiment_id: EXP-003`
- `render_spec_version: EXP003-RENDER-SPEC-v1-FROZEN`
- `item_freeze_manifest: experiments/EXP-003-item-freeze-manifest-v2.yaml`
- `item_freeze_sha256: 940D317684BF17BCB5CAF3EA9E08CCE4FE8C428BC1CD63F4C2004D32739E5B64`
- `historical_item_freeze_manifest: experiments/EXP-003-item-freeze-manifest.yaml`
- `historical_item_freeze_sha256: AE1C5A93C57469CB72C95775A7ED11916A7599729F10EA0B94D4659CA6B8A093`
- `render_spec_status: FROZEN`
- `render_spec_freeze_date: 2026-09-05`
- `renderer_source: experiments/deterministic_additive_renderer.py`
- `renderer_version: EXP003-ADDITIVE-RENDERER-v1`
- `renderer_source_sha256: A19A4D15FB47DE963228BA29224D0D1A8DB533B82DDBCD254BA217C9FC975545`
- `gate_e_status: NOT_YET_PASS`
- `music_engine_runtime: NOT_AUTHORIZED`
- `midi: NOT_AUTHORIZED`
- `audio: NOT_AUTHORIZED`

Esta especificacion separa el item freeze del render freeze. No modifica el
manifiesto congelado, no contiene media generada y no autoriza materializacion.

## Historical preflight blocker

La auditoria historica encontro un fallo simbolico en F11 HIGH. Freeze-v2 lo
resolvio mediante la re-seleccion determinista `[50,53,72,81]`. El manifiesto
v1 y su hash se conservan como evidencia histórica; esta especificación usa
exclusivamente freeze-v2 para trabajo posterior.

## Intended pipeline

```text
frozen item manifest
  -> exact event representation
  -> music-engine SongPlanV2 / deterministic MIDI
  -> pinned CLI renderer + pinned instrument asset
  -> canonical lossless audio
  -> decoded-audio technical validation
  -> asset checksum
```

`music-engine` es solo backend de materializacion determinista. No elige
pitches, voicings, condiciones, timbre, preset ni renderer.

## Mapping and timing proposal

El mapeo de cada item sera mecanico: una nota simultanea explicita por cada
pitch MIDI de `R1` y `R2`, conservando V1-V4 y los pitches congelados. No se
permiten decisiones nuevas durante el mapeo.

Timing comun propuesto para todos los items, clasificado como `PROJECT DESIGN
CHOICE` y pendiente de aprobacion:

- tempo de referencia: 120 BPM;
- `R1`: onset beat 1, duracion de 1 beat;
- `R2`: onset beat 2, duracion de 1 beat;
- sin solapamiento y sin gap intermedio;
- leading silence: 0.25 s;
- release tail: 0.50 s despues del final de R2;
- trailing silence adicional: 0.25 s;
- LOW y HIGH de una familia: timing identico;
- no humanization, arpeggio ni sustain pedal.

Las duraciones deben expresarse posteriormente con fracciones exactas de
SongPlan, no con redondeos de audio. La decision temporal sigue sin estar
congelada.

## Note attack, release and intensity

- note-on simultaneo por evento de sonoridad;
- note-off simultaneo al terminar cada sonoridad;
- envelope identico para todos los pitches y condiciones;
- sustain pedal OFF;
- sin legato adaptativo, release dependiente de armonia ni articulacion
  contextual;
- velocity nominal identica para las cuatro voces: `96`;
- sin acento de bajo, soprano o voz interna.

## Loudness policy

Se evaluaron:

- **A - fixed source gain:** velocity identica y un gain global calibrado una
  sola vez;
- **B - per-stimulus normalization:** normalizar cada archivo individualmente;
- **C - otra politica:** no adoptada.

Se recomienda **A - fixed source gain**. Es determinista, no depende de la
condicion ni de una medicion posterior de cada archivo, y conserva la salida
del renderer. El gain global se elegira antes de renderizar para evitar clipping
en todo el pool. Las diferencias acusticas residuales por registro se
registraran como alcance, no se corregiran manualmente ni se usaran para
reseleccionar items.

## Timbre and renderer proposal

Timbres considerados: tono sintetico aditivo, organ-like neutral y piano-like
sampleado. Se recomienda un **tono sintetico aditivo mono-compatible**, porque
ofrece claridad de pitch y ataques/releases fijables sin depender de una
interpretacion expresiva de piano.

Renderer candidato: **FluidSynth CLI** con una configuracion no interactiva y
un asset de instrumento previamente seleccionado. Actualmente no esta
instalado ni versionado en el entorno (`fluidsynth: NOT_FOUND`), y no existe un
soundfont/preset local identificable. Por eso la recomendacion es de
arquitectura, no una seleccion ejecutable.

Alternativa si el Director la aprueba: un renderer aditivo propio, totalmente
determinista, con parciales, envelope y fase inicial explicitos. Eso requeriria
implementacion adicional y no se introduce aqui.

Requisitos del renderer futuro:

- version fijada;
- preset/instrument ID fijado;
- asset exacto almacenado o referenciado por hash SHA-256;
- polyphony suficiente para cuatro notas simultaneas;
- voice stealing OFF;
- fase reset determinista;
- random detune, drift, unison randomness y random modulation OFF;
- sin decisiones de canal o programa ambiguas.

## Effects, channels and tuning

- reverb: OFF;
- chorus: OFF;
- delay: OFF;
- compression/limiting automatico: OFF;
- spatialization: OFF;
- pan por voz: OFF;
- salida recomendada: mono centrado, para no introducir segregacion espacial;
- tuning: 12-TET, referencia A4=440 Hz;
- canal/programa: explicitamente fijados en la configuracion posterior, no
  inferidos por nombre de acorde.

El tono de cada pitch puede conservar consecuencias registrales del timbre;
Gate E no permite generalizar a otros instrumentos.

## Canonical audio and integrity

Formato canonico propuesto: WAV PCM linear, mono, 48 kHz, 24-bit. Esta es una
decision de proyecto pendiente de aprobacion; no se presenta como requisito
universal de audicion. El master lossless sera la fuente de cualquier
transcodificacion posterior.

Validacion tecnica futura:

- peak absoluto bajo 0 dBFS con margen global predeclarado;
- ausencia de clipping/saturacion digital;
- ausencia de DC offset relevante;
- duracion y limites de silencio esperados;
- canal count, sample rate y bit depth correctos;
- presencia de todos los note-ons/note-offs esperados;
- RMS o descriptor de nivel solo como diagnostico, no como criterio de
  seleccion perceptual.

No se hara trimming manual. Leading silence, tail y trailing silence seguiran
la plantilla comun.

## Asset naming and future render manifest

ID interno determinista:

`EXP003-{family_id}-{condition}-{render_spec_version}`

El participant-facing ID sera neutral y separado del mapping LOW/HIGH. No se
ejecuta randomizacion en esta fase.

Esquema minimo futuro:

```yaml
experiment_id: EXP-003
item_freeze_sha256: "..."
render_spec_version: "..."
item_family_id: EXP003-FXX
condition: LOW_SELECTED
R1_pitches_midi: [0, 0, 0, 0]
R2_pitches_midi: [0, 0, 0, 0]
timing: {tempo_bpm: 120, r1_onset: "1", r1_duration: "1/4", r2_onset: "2", r2_duration: "1/4"}
velocity: 96
renderer: "..."
renderer_version: "..."
instrument_asset: "..."
instrument_asset_sha256: "..."
sample_rate_hz: 48000
bit_depth: 24
channels: 1
effects: {reverb: off, chorus: off, delay: off, compression: off, spatialization: off}
gain_policy: fixed_global_gain
canonical_filename: "..."
output_sha256: null
```

La cadena de provenance sera:

`item_freeze_sha256 + render_spec_sha256 -> audio_asset_sha256`.

El render-spec hash solo se creara cuando esta especificacion sea aprobada y
congelada. Los output hashes se crean solo despues de que existan los archivos.

## Technical canary design

Antes de bulk rendering, un canary futuro debera:

1. seleccionar un item congelado y una condicion;
2. materializarlo con el runtime local fijado;
3. verificar pitches, onsets, note-offs, velocity, canales y ausencia de
   eventos extra relevantes;
4. renderizar dos veces en el mismo entorno canonico;
5. comparar SHA-256 y, si difieren, comparar PCM decodificado y diagnosticar;
6. inspeccionar duracion, peak, clipping, silencio y numero de canales.

El canary no es un piloto perceptual y no autoriza bulk rendering ni
participantes. No se ejecuta ahora.

## Gate-E subgates

- E1 SYMBOLIC MAPPING: `PASS WITH SCOPE` para freeze-v2; mecanicamente el
  formato es suficiente para los 12 items validados.
- E2 MATERIALIZATION: `DESIGN READY`, pendiente de validacion futura con
  `music-engine`.
- E3 RENDERER: `NOT READY`; no hay renderer CLI ni asset timbrico fijado en el
  entorno.
- E4 ACOUSTIC PARAMETERS: `DESIGN READY`; timing, nivel y timbre siguen
  propuestos, no congelados.
- E5 OUTPUT INTEGRITY: `DESIGN READY`; falta producir y verificar archivos.
- E6 REPEATABILITY: `NOT READY`; no hay canary ni renderer pinned ejecutado.

## Overall Gate E

Resultado: **B - DESIGN REVISIONS REQUIRED**.

La arquitectura conceptual es viable, pero Gate E permanece `NOT YET PASS` y
no esta lista para technical materialization validation hasta fijar/versionar
renderer, asset y settings.

La reproducibilidad esperada, una vez fijados esos elementos, es **BIT
IDENTICAL** en el mismo entorno canonico. No se debe depender de que los
participantes rendericen MIDI localmente; se distribuirian assets lossless
pre-renderizados. Eso no elimina la variabilidad de auriculares/altavoces.

## Authorization

- `RENDER SPEC: PROPOSED_NOT_FROZEN`
- `ITEM FREEZE: FREEZE-V2 AUTHORITATIVE; V1 HISTORICAL INVALIDATED`
- `MUSIC-ENGINE RUNTIME: NOT AUTHORIZED`
- `MIDI: NOT AUTHORIZED`
- `AUDIO: NOT AUTHORIZED`
- `PILOT: NOT AUTHORIZED`
- `EXECUTION: NOT AUTHORIZED`

Recommended next action: seleccionar/versionar un renderer y asset concretos
para una futura technical canary authorization. No ejecutar ahora.

## Gate-E renderer/asset pinning re-audit

Esta sección es el estado vigente de la especificación `v2-PROPOSED`.

### Environment and renderer decision

Entorno canónico propuesto: Windows del proyecto, Python `3.14.3`, runtime
local `music-engine` 4.0.0 instalado desde wheel, commit
`71bbc73337da0d755618bdc796e19ce2e82cc3df`, SongPlanV2 `2.0`. El runtime
simbólico está disponible, pero no se invoca en esta tarea.

No están instalados `FluidSynth`, `FFmpeg`, `SoX` ni `TiMidity`. No se
encontraron `.sf2`, `.sfz`, `.wav`, `.flac`, `.dll` o `.vst3` instrumentales
fuera del entorno virtual. No existe, por tanto, ningún renderer o asset
project-owned que pueda fijarse actualmente.

Comparación conceptual:

- tono sintético/aditivo sostenido: mejor control de ataque, release, fase y
  simultaneidad; requiere un renderer implementado y versionado;
- piano-like sampleado: ataque y decay más ecológicos, pero introduce
  dependencia registral, transitorios y posible variación de muestras;
- FluidSynth + SoundFont: ruta CLI viable y no interactiva, pero necesita una
  versión exacta y un SoundFont/preset con licencia y SHA conocidos.

Recomendación metodológica: tono sintético/aditivo mono-compatible para
claridad de pitch, si se adquiere o implementa una ruta determinista. FluidSynth
queda como candidato alternativo, no como elección congelada. No se acepta
`default piano`, `GM piano`, `latest` ni cualquier SoundFont instalado
localmente.

### Acoustic and timing policy

El BPM no es una variable musical de EXP-003. Se conserva `120` únicamente
como metadato necesario para SongPlan/MIDI; la especificación perceptual debe
usar tiempos absolutos derivados de una plantilla única:

- leading silence: `0.25 s`;
- R1 onset: `0.25 s`, duración `0.50 s`;
- R2 onset: `0.75 s`, duración `0.50 s`;
- transición: sin gap y sin solapamiento entre note-off de R1 y note-on de R2;
- release tail determinista: `0.50 s` desde el note-off de R2;
- trailing silence: `0.25 s`;
- duración total canónica: `2.00 s`;
- LOW/HIGH: timing idéntico.

Estas cifras son `PROJECT IMPLEMENTATION CHOICE`, no evidencia compositiva ni
hipótesis rítmica. Las duraciones de SongPlan se expresarán como fracciones
exactas; el renderer deberá producir el mismo límite temporal sin trimming
manual.

Velocity: `96` para las cuatro voces, clasificada como `PROJECT IMPLEMENTATION
CHOICE`; evita jerarquía entre voces y se mantiene idéntica entre condiciones.
La ganancia será una única `fixed_global_gain`, calibrada contra el máximo de
todo el pool. Si un archivo clipea, se ajusta esa ganancia global y se rerenderiza
el pool completo.

Tuning: 12-TET, A4 = 440 Hz. Effects, humanization, sustain, random detune,
random phase, round-robin, drift, random LFO, random velocity y voice stealing:
OFF o, si el renderer lo exige, fijados de forma determinista. No se permite
una configuración que no haga controlable esa aleatoriedad.

Salida: mono centrado. Si un renderer solo produce stereo, se requerirá una
configuración L/R idéntica o un downmix determinista `(L+R)/2`, documentado y
aplicado a todos los archivos; no se permite pan por voz.

### music-engine adapter contract

Clasificación: `ADAPTER REQUIRED`. SongPlanV2 puede expresar el material,
pero requiere nombres de pitch explícitos, beats, duraciones y velocity; no
autoriza canal MIDI ni selecciona instrumento.

El adaptador futuro deberá mapear cada item de freeze-v2 mecánicamente a un
track pitched con dos eventos: R1 y R2, cada uno con cuatro pitches simultáneos,
onsets exactos, duración exacta y velocity `96`. Tempo `120` será metadata de
implementación. El renderer externo será la única autoridad de instrumento,
programa y banco, fijados explícitamente; no se usarán defaults MIDI.

### Canonical asset and integrity contract

Formato propuesto: WAV PCM lineal, mono, 48 kHz, 24-bit. Se conserva como
decisión operativa razonable para no introducir compresión con pérdida; no es
una exigencia universal de audición.

Cada manifest futuro deberá registrar freeze-v2 SHA, render-spec SHA, ID de
familia/condición, evento esperado, renderer/version, asset/version y SHA del
asset, configuración, ganancia, duración, formato y output SHA. La validación
deberá comprobar nonempty audio, duración `2.00 s`, sample rate, bit depth,
canales, ausencia de clipping y checksum.

Provenance requerida para un asset externo: release reproducible o archivo
project-pinned, versión exacta, preset/bank/program, licencia/procedencia y
SHA-256. Actualmente: asset disponible **NO**, asset SHA disponible **NO**,
problema de licencia/procedencia **SÍ, pendiente de resolver**.

### Future technical canary

El primer canary será `EXP003-F01 / LOW_SELECTED`, elegido por ser ordinario y
no extremo; F11 queda excluido del primer canary técnico por su historial de
revisión. El canary deberá validar freeze-v2, inspeccionar eventos MIDI,
renderizar una vez, repetir independientemente, comparar FILE-BIT y PCM
decodificado, y comprobar duración, canales, nivel y clipping. No será dato
perceptual.

Objetivo: `FILE-BIT IDENTICAL` y, como salvaguarda, `PCM-BIT IDENTICAL` en el
mismo entorno, input, renderer, asset y settings. Si headers WAV introducen
metadatos variables, deberán hacerse deterministas o el criterio operativo
será PCM-BIT IDENTICAL con la diferencia documentada.

### Current subgates

- E1: `PASS WITH SCOPE`.
- E2: `DESIGN READY`.
- E3: `NOT READY` — renderer y asset no disponibles/fijados.
- E4: `DESIGN READY` — parámetros propuestos, no congelados.
- E5: `DESIGN READY` — falta producir y validar audio.
- E6: `NOT READY` — no existe repeated render.

Overall Gate E: `NOT YET PASS`.

Ready for technical canary: **NO**. Blockers exactos: renderer CLI versionado,
asset/preset reproducible con SHA y configuración ejecutable. No se instala ni
se selecciona un default automáticamente.

## Current renderer specification: project-owned additive v1

Esta sección sustituye la propuesta FluidSynth como ruta primaria. El renderer
primario es `experiments/deterministic_additive_renderer.py`, implementado con
la biblioteca estándar de Python. FluidSynth queda como fallback futuro y no
forma parte del canary actual.

Veredicto de la decisión: **PREFERRED** para EXP-003. El timbre es sintético y
no se presenta como neutral ni como representación de producción musical. Su
ventaja experimental es que elimina SoundFont, round-robin, capas de velocidad,
preset oculto y variación de fase.

### Exact synthesis contract

- Tuning: `f(m) = 440 * 2^((m - 69) / 12)`.
- Oscillator: sinusoidal, fase inicial `0` para cada nota y cada onset; no hay
  estado free-running entre notas.
- Spectrum: parciales 1--4 con amplitudes exactas `[1, 1/2, 1/4, 1/8]`.
- Anti-aliasing: se incluye cada parcial solo si `harmonic * frequency <
  sample_rate / 2`; no hay ajustes manuales por nota.
- Envelope: ataque lineal de `0.010 s`, sustain a amplitud constante y release
  lineal de `0.020 s`.
- Input duration: `0.480 s` hasta note-off; el release ocupa los `0.020 s`
  restantes de cada intervalo de `0.500 s`.
- Summation: cada nota se acumula en orden estable de la lista de eventos,
  sin compressor, limiter, normalizer ni voice priority.
- Velocity mapping: únicamente `96 / 127`; no se usa curva MIDI externa.
- Global gain: `1/16`, común a todo EXP-003.

### Transition and sample indices

No existe solapamiento R1/R2. R1 tiene note-off en `0.730 s` y su release
termina exactamente en el onset R2 `0.750 s`; R2 termina su release en
`1.250 s`. Por tanto no se crea una sonoridad compuesta de ocho notas.

A 48 kHz, los tiempos se convierten directamente a frames enteros:

| tiempo | frame |
|---:|---:|
| 0.25 s | 12000 |
| 0.73 s | 35040 |
| 0.75 s | 36000 |
| 1.23 s | 59040 |
| 1.25 s | 60000 |
| 2.00 s | 96000 |

El renderer no usa acumulación temporal; cada límite se calcula desde segundos
aprobados mediante `round(seconds * 48000)` y se rechaza cualquier tiempo no
representable dentro de la tolerancia definida en el código. La salida tiene
exactamente `96000` frames.

### PCM and headroom

La salida es WAV PCM little-endian, mono, 24-bit, 48 kHz, sin chunks de metadata
variables. La serialización usa el módulo estándar `wave` y packing signed
little-endian de tres bytes; la cuantización usa el redondeo entero determinista
de Python.

La cota teórica conservadora antes de cuantización es:

`4 * (96/127) * (1 + 1/2 + 1/4 + 1/8) * (1/16) = 45/127 < 1`.

Así, cuatro voces a envolvente máxima permanecen por debajo de full scale sin
normalización por estímulo. La validación del canary debe comprobar además el
peak efectivo y clipping.

### Tail and PCM quantization freeze details

La referencia histórica a `1.750 s` como tail se elimina como límite operativo:
la señal ya es cero desde `1.250 s`; el intervalo restante es silencio final.

Cuantización PCM exacta: cada muestra float se multiplica por `8388607`, se
redondea con `round` de Python (round-half-to-even), y se satura al intervalo
simétrico `[-8388607, 8388607]`. El rango esperado antes de cuantizar es
estrictamente `(-1, 1)` por la cota `45/127`. En los límites explícitos, `+1`
se representa como `8388607` y `-1` como `-8388607`. Cada entero se serializa
en tres bytes signed little-endian, sin timestamps, metadata variable ni
identificadores aleatorios.

### Input structural identity requirement

Cada evento JSON debe incluir `event_id` no vacio junto con `pitch_midi`,
`onset_seconds`, `duration_seconds` y `velocity`. `event_id` solo conserva
trazabilidad estructural; el renderer no toma decisiones musicales a partir de
ese campo.

### Input and provenance boundary

El renderer recibe únicamente JSON de eventos explícitos con
`pitch_midi`, `onset_seconds`, `duration_seconds`, `velocity`, duración total y
sample rate. No realiza voicing, selección de octava, timing, articulación ni
lectura del manifiesto. Solo `render-events INPUT_JSON OUTPUT_WAV` escribe
audio; sin esos argumentos no hay render implícito ni bulk rendering.

La identidad del renderer es: ruta fuente, versión
`EXP003-ADDITIVE-RENDERER-v1`, SHA-256 del fuente
`A19A4D15FB47DE963228BA29224D0D1A8DB533B82DDBCD254BA217C9FC975545`, Python
exacto, render-spec SHA y JSON de eventos.

### Canonical chain decision

La cadena canónica recomendada es:

`freeze-v2 -> exact event manifest -> custom renderer -> canonical WAV`

El MIDI permanece como artefacto de verificación/exportación producido por
`music-engine`, no como input primario del renderer. Así se evita que conversión
de tempo/ticks altere el input científico, sin eliminar el papel de
`music-engine` como backend simbólico validable.

### Updated Gate-E state

- E1: `PASS WITH SCOPE`.
- E2: `DESIGN READY`.
- E3: `PASS WITH SCOPE` — renderer propio implementado; no hay dependencia
  instrumental externa.
- E4: `DESIGN READY` — espectro, fase, envolvente y timing están especificados;
  requieren aprobación/freeze formal.
- E5: `DESIGN READY` — serialización y validaciones están definidas; no se ha
  producido media.
- E6: `READY FOR TECHNICAL VALIDATION` — el repeated render queda pendiente.

Overall Gate E permanece `NOT YET PASS` hasta el canary. La especificación está
`COMPLETE_PENDING_FREEZE`; su SHA estable podrá calcularse al aprobar y congelar
esta versión. Ready for technical canary: **YES**, pendiente de autorización
separada para ejecutar el canary. No se ejecuta en esta tarea.
