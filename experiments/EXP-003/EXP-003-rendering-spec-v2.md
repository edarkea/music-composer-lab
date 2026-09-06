# EXP-003 — Especificación congelada de rendering v2

## Estado y entradas autoritativas

- `experiment_id: EXP-003`
- `render_spec_version: EXP003-RENDER-SPEC-v2-FROZEN`
- `render_spec_status: FROZEN`
- `item_freeze_manifest: experiments/EXP-003-item-freeze-manifest-v2.yaml`
- `item_freeze_sha256: 940D317684BF17BCB5CAF3EA9E08CCE4FE8C428BC1CD63F4C2004D32739E5B64`
- `historical_render_spec_v1: experiments/EXP-003-rendering-spec-v1.md`
- `historical_render_spec_v1_status: SUPERSEDED_BY_V2`

El manifiesto v2 no se modifica. El manifiesto v1 y el render spec v1 son
artefactos históricos; no son inputs actuales de ejecución.

## Clasificación del renderer

`tools/exp003/deterministic_additive_renderer.py` es un **EXPERIMENTAL
TECHNICAL RENDERER**. No es un music engine, composition engine, modelo
musical ni fuente de conocimiento compositivo. Recibe eventos ya decididos y
produce PCM.

Identidad:

- versión lógica: `EXP003-ADDITIVE-RENDERER-v1`;
- source: `tools/exp003/deterministic_additive_renderer.py`;
- source SHA-256: `89E61135B51728F9D469B6658AF494DFA9AD638CB921173ABAEEA05DFE4B7404`;
- dependencias: Python standard library únicamente;
- Python canónico: `3.14.3`.

El validador estructural general es
`tools/exp003/validate-exp003-freeze-v2.py`.

## Entorno canónico

La reproducibilidad reclamada es únicamente dentro del entorno canónico del
proyecto: Windows, Python `3.14.3`, el source SHA anterior, este spec y los
eventos exactos. No se reclama identidad entre sistemas operativos o máquinas
Windows distintas.

## Representación de eventos

El input canónico es una representación JSON de eventos, no MIDI. Cada evento
contiene `event_id`, `pitch_midi`, `onset_seconds`, `duration_seconds` y
`velocity`; el documento contiene además `sample_rate_hz` y
`duration_seconds` total.

Para un estímulo EXP-003, un validador específico deberá exigir exactamente
ocho eventos pitched: cuatro R1 y cuatro R2, con identidad estructural única,
pitches exactos del freeze-v2, onsets y note-offs exactos, y velocity 96.

El orden canónico de acumulación es la ordenación total por:

`(onset_sample, event_id)`

No depende de la inserción JSON, el sistema de archivos ni una elección del
investigador. `event_id` es obligatorio, no vacío y único dentro del estímulo;
el renderer rechaza ausencias o duplicados y nunca crea UUIDs.

## Papel de music-engine y MIDI

`music-engine` sigue siendo el backend de materialización y verificación
simbólica. MIDI es un artefacto separado de verificación/exportación. MIDI no
es el input primario del renderer, porque la conversión de tempo/ticks no debe
alterar el input científico.

La cadena canónica es:

`freeze-v2 → exact event representation → deterministic additive renderer → WAV`

Una cadena paralela futura puede ser:

`freeze-v2 → SongPlanV2 → music-engine → MIDI`

para comprobar que la representación simbólica es materializable. El adaptador
SongPlan, si se necesita, debe mapear mecánicamente R1/R2 a eventos explícitos
con cuatro pitches simultáneos, onsets, duraciones y velocity 96. No puede
decidir voicings, timbre o timing.

## Síntesis exacta

- afinación: 12-TET, A4 = 440 Hz;
- frecuencia: `f(m) = 440 * 2^((m - 69) / 12)`;
- oscillator: seno;
- fase inicial: `0` en cada onset, sin estado free-running;
- espectro: armónicos 1–4 con amplitudes `[1, 1/2, 1/4, 1/8]`;
- anti-aliasing: se incluye un parcial solo si
  `harmonic * frequency < sample_rate / 2`;
- suma: acumulación estable en el orden canónico de eventos;
- polyphony: suma de las cuatro voces, sin voice priority;
- compresor, limiter y normalizer: OFF.

El timbre es sintético y no se presenta como neutral ni como evidencia sobre
calidad musical.

## Envolvente y timing

Una única envolvente se aplica a todas las notas:

- ataque lineal: `0.010 s`;
- sustain: amplitud constante;
- release lineal: `0.020 s`.

Timing absoluto común a LOW y HIGH:

| evento | tiempo |
|---|---:|
| leading silence / R1 onset | `0.250 s` |
| R1 note-off | `0.730 s` |
| R1 release zero / R2 onset | `0.750 s` |
| R2 note-off | `1.230 s` |
| R2 release zero | `1.250 s` |
| canonical file end | `2.000 s` |

No existe solapamiento acústico R1/R2 ni sonoridad compuesta de ocho notas.
La señal es cero desde `1.250 s` y el intervalo restante hasta el final de
archivo es silencio.

`120 BPM`, si aparece en SongPlan, es metadata de implementación y no una
variable musical del experimento.

## Amplitud y headroom

- velocity: `96` para todas las voces, condiciones e ítems;
- mapping: `96 / 127`, lineal;
- gain: `1/16`, único para todo el experimento;
- no hay normalización específica por estímulo.

Con cuatro voces y el espectro congelado, la cota previa a cuantización es:

`4 * (96/127) * (1 + 1/2 + 1/4 + 1/8) * (1/16) = 45/127 < 1`.

La validación futura comprobará peak efectivo y clipping. Si la implementación
contradice esta cota, se detiene el proceso y se audita el renderer; no se
atenúa individualmente ningún estímulo.

## Sample indexing

Sample rate: `48000 Hz`. Cada tiempo aprobado se convierte directamente con
`round(seconds * 48000)`; no se acumulan duraciones flotantes.

| tiempo | frame |
|---:|---:|
| `0.250 s` | `12000` |
| `0.730 s` | `35040` |
| `0.750 s` | `36000` |
| `1.230 s` | `59040` |
| `1.250 s` | `60000` |
| `2.000 s` | `96000` |

El ataque ocupa `480` frames y el release `960` frames. La salida tiene
exactamente `96000` frames.

## PCM y WAV

Formato canónico: WAV PCM lineal mono, 48 kHz, signed integer de 24 bits.

Cada muestra float se multiplica por `8388607` (`2^23 - 1`), se redondea con
`round` de Python (round-half-to-even) y se satura al intervalo simétrico
`[-8388607, 8388607]`. `+1` se representa como `8388607` y `-1` como
`-8388607`.

Cada entero se empaqueta en tres bytes signed little-endian. La serialización
usa el módulo estándar `wave`, sin timestamps, chunks de metadata variable,
identificadores aleatorios ni stereo intermedio. La salida es mono directa y
no se aplica pan ni spatialization.

## Determinismo y efectos

No existe randomness. Están desactivados o fuera del modelo: random phase,
round-robin, random detune, drift, random LFO, random velocity, humanization,
sustain pedal, reverb, chorus, delay, compresión, limiting y voice stealing.

La ejecución requiere argumentos explícitos `render-events INPUT_JSON OUTPUT_WAV`;
sin input no hay render y nunca se hace bulk rendering automático.

## Provenance

La línea de procedencia futura es:

`item_freeze_v2_sha256 + render_spec_v2_sha256 + renderer_source_sha256 + canonical_environment + event_input → WAV_asset_sha256`

El SHA de MIDI, si se produce, se registra aparte porque MIDI no es el input
canónico del renderer.

## Canary y Gate E

Canary técnico futuro: `EXP003-F01 / LOW_SELECTED`. Primero debe pasar la
validación simbólica y de eventos, después se compara una doble ejecución del
renderer mediante FILE-BIT y PCM-BIT. No es un piloto perceptual.

- E1: `PASS WITH SCOPE`;
- E2: `DESIGN READY`;
- E3: `PASS WITH SCOPE`;
- E4: `PASS WITH SCOPE`;
- E5: `DESIGN READY`;
- E6: `READY FOR TECHNICAL VALIDATION`;
- Overall Gate E: `NOT YET PASS`.

La receta está congelada, pero el canary no está autorizado por este
documento.
