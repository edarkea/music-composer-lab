# EXP-003 — Protocolo de producción canónica v1

## Alcance y estado

Este documento prepara la producción futura de los estímulos canónicos de
EXP-003. No genera medios, no constituye evidencia perceptual y no autoriza un
piloto.

CANARY-001 permanece como `FAILED_BEFORE_MIDI_WRITE`. CANARY-002 fue
`SUCCESS`, con Gate E `PASS WITH SCOPE`; sus medios son únicamente validación
técnica y no forman parte del pool de participantes.

## Entradas autoritativas

| entrada | SHA-256 |
|---|---|
| item freeze v2 | `940D317684BF17BCB5CAF3EA9E08CCE4FE8C428BC1CD63F4C2004D32739E5B64` |
| render spec v2 | `25B7238C6854BDE63C47E40C27F82C6FA7A5C89946C255ED771FB6FC3CFD2625` |
| renderer | `89E61135B51728F9D469B6658AF494DFA9AD638CB921173ABAEEA05DFE4B7404` |
| MIDI adapter v2 | `CB478EF0C3464F4F5389D84695C440060D62C6DABEC0FBA36F9C758D167D6074` |
| MIDI verification spec v2 | `DA114080D5F3D4910D7BB334DB1C3278CFFE1C17C2281F0222DC7D9A6BD183A4` |

Si cualquiera de estos hashes no coincide al iniciar producción, detener todo
el proceso y no generar medios.

## Pool objetivo

El pool futuro contiene exactamente `12 familias × 2 condiciones = 24
estímulos`: `LOW_SELECTED` y `HIGH_SELECTED`. Cada estímulo tiene ocho
eventos: cuatro R1 y cuatro R2, con pitches, timing y velocity tomados del
freeze. La expansión es mecánica; no se permite ninguna decisión musical nueva.

## Identidad y nombres

El identificador técnico interno será `EXP003-F{family:02d}-{condition}`.
Ejemplos: `EXP003-F01-LOW`, `EXP003-F01-HIGH`, `EXP003-F12-HIGH`.

Los eventos usarán `EXP003-F{family:02d}-{condition}-R{1|2}-V{1|2|3|4}`. El
orden canónico será `(onset_sample, event_id)`. Cada artifact de eventos
recibirá su propio SHA-256; ese SHA será la identidad de entrada del renderer.
El MIDI no sustituye la identidad del evento.

Los nombres internos pueden incluir la condición. Los identificadores futuros
de presentación serán separados y opacos; no se asignan todavía.

## Directorios

```text
experiments/EXP-003/
├── technical-canary/              # CANARY-001 y CANARY-002
├── canonical-assets/              # pool futuro autorizado
│   ├── events/
│   ├── verification-midi/
│   └── wav/
├── participant-assets/            # reservado; vacío hasta autorización
└── EXP-003-asset-manifest-v1.yaml # manifiesto futuro
```

Los medios de canary no se copiarán a `canonical-assets/` ni a
`participant-assets/`.

## Producción MIDI

Se recomienda producir y validar **24/24 verification MIDI**, uno por cada
combinación familia-condición. El coste técnico es bajo y la verificación
completa evita que una familia quede sin comprobación de la ruta simbólica.

Cada archivo usará `music-engine 4.0.0`, `EXP003-MIDI-ADAPTER-v2`, tempo 120,
PPQ 1000 y representación exacta. Se inspeccionará el archivo real, no solo la
configuración del adaptador: PPQ, ticks 500/1460/1500/2460, pitches congelados,
velocity 96, ausencia de eventos extra y conversión absoluta exacta a
0,250/0,730/0,750/1,230 s.

Un fallo no se redondea ni se repara silenciosamente.

## Producción WAV y repetibilidad

Cada estímulo se renderizará directamente desde su artifact de eventos, nunca
desde MIDI. Se recomienda la política de **doble render**:

1. ejecutar dos veces el renderer congelado;
2. exigir igualdad de bytes de archivo y de PCM;
3. conservar un único WAV canónico tras la comprobación;
4. registrar ambos hashes en el manifiesto o registro de validación.

La segunda copia puede eliminarse después de registrar la igualdad, si la
política de repositorio lo permite. No se permite normalización, atenuación,
limitación, compresión ni cambios de gain por ítem.

Cada WAV debe cumplir objetivamente: mono, 48.000 Hz, PCM entero de 24 bits,
96.000 frames, 2,000 s, peak sin clipping, regiones sonoras no vacías y
silencio final desde frame 60.000. No se rechazará un ítem por sonar extraño,
débil, áspero, distante o agradable.

## Criterios técnicos de exclusión

Se declaran antes de producir:

- hash de entrada o de herramienta incorrecto;
- fallo del contrato de eventos o del SongPlan;
- fallo de materialización MIDI;
- PPQ, pitch, velocity o ticks incorrectos;
- tiempo absoluto MIDI no exacto;
- excepción del renderer;
- formato, sample rate, canales, frames o duración WAV incorrectos;
- clipping;
- región sonora esperada vacía o silencio final incorrecto;
- falta de evento o evento extra;
- falta de igualdad de archivo/PCM en el doble render.

No se añaden criterios después de escuchar los estímulos.

## Atomicidad y fallos

La producción es atómica a nivel de pool: si falla el estímulo N, detener la
ejecución, registrar el fallo y marcar el pool como `INCOMPLETE`. Los artefactos
exitosos parciales pueden conservarse para diagnóstico, pero ningún pool
parcial es autoritativo ni se continúa silenciosamente.

## Manifiesto de assets

Ruta propuesta: `experiments/EXP-003/EXP-003-asset-manifest-v1.yaml`.

Cada entrada futura incluirá como mínimo:

```yaml
experiment_id: EXP-003
family_id: EXP003-F01
condition: LOW_SELECTED
internal_asset_id: EXP003-F01-LOW
item_freeze_sha256: "..."
render_spec_sha256: "..."
renderer_sha256: "..."
midi_adapter_sha256: "..."
midi_verification_spec_sha256: "..."
event_artifact_path: "canonical-assets/events/...json"
event_sha256: "..."
verification_midi_path: "verification-midi/...mid"
midi_sha256: "..."
canonical_wav_path: "wav/...wav"
wav_sha256: "..."
sample_rate_hz: 48000
bit_depth: 24
channels: 1
frames: 96000
duration_seconds: 2.0
peak: 0
clipping: false
timing_validation: PASS
midi_validation: PASS
repeatability: {file_bit_identical: true, pcm_bit_identical: true}
```

Tras 24/24 entradas completas se calculará y registrará el SHA-256 del
manifiesto.

## Freeze final y límites

El pool solo podrá declararse congelado cuando haya 24/24 PASS en eventos, MIDI
(política completa), WAV, repetibilidad y manifiesto completo con hashes. Esto
no convierte la producción en evidencia perceptual ni apoya CAND-CROSS-005.

El piloto seguirá necesitando autorización separada y revisión de wording,
escala, contrabalanceo, playback y criterios de exclusión.

## Estado de autorización

- Decisión musical nueva pendiente: **NO**.
- Código nuevo requerido: **NO**; se reutiliza el tooling congelado.
- MIDI bulk generado: **NO**.
- WAV bulk generado: **NO**.
- Pilot autorizado: **NO**.
- Listo para autorizar producción de 24 assets: **NO**; falta autorización
  explícita del Project Owner.
