# EXP-003 — Especificación de verificación MIDI v1

Este documento define únicamente la codificación y las comprobaciones técnicas
del MIDI de verificación. No modifica la duración acústica ni sustituye la
especificación de renderizado auditivo.

## Referencias congeladas

- Item freeze v2: `experiments/EXP-003-item-freeze-manifest-v2.yaml`
  - SHA-256: `940D317684BF17BCB5CAF3EA9E08CCE4FE8C428BC1CD63F4C2004D32739E5B64`
- Render spec v2: `experiments/EXP-003-rendering-spec-v2.md`
  - SHA-256: `25B7238C6854BDE63C47E40C27F82C6FA7A5C89946C255ED771FB6FC3CFD2625`
- Fuente de eventos F01 LOW: `experiments/EXP-003/technical-canary/EXP003-CANARY-001-F01-LOW.events.json`
  - SHA-256: `D25B504CF5CB57749B4ECC51C0145BA83827A7BC452AE4939218338A3C6E9BF2`

## Política de codificación

- Tempo metadata: **120 BPM**.
- PPQ: **1000**.
- El PPQ es una elección de codificación MIDI, no una variable musical o
  perceptual.
- Un beat SongPlan es una posición 1-based en unidades de negra; una duración
  es una fracción de redonda.
- R1 se codifica en `bar: 1`, `beat: "3/2"`.
- R2 se codifica en `bar: 1`, `beat: "5/2"`.
- Ambas duraciones se codifican como `"6/25"`.
- El adaptador debe tomar pitches y velocity del artefacto de eventos. No puede
  inventar ni alterar pitch, voicing, octava, condición, velocity, timing,
  duración o articulación.

## Landmarks exactos

Con 120 BPM y PPQ 1000, un tick equivale a 0,0005 s:

| evento | tiempo absoluto | ticks MIDI |
|---|---:|---:|
| R1 ON | 0,250 s | 500 |
| R1 OFF | 0,730 s | 1460 |
| R2 ON | 0,750 s | 1500 |
| R2 OFF | 1,230 s | 2460 |

La duración `6/25` de redonda equivale exactamente a **960 ticks**.
La conversión debe ser racional y exacta. No se permite redondeo, truncado,
ceiling, epsilon ni cuantización silenciosa. Si un valor no es representable
exactamente, la verificación falla.

## Adaptador

- Identidad lógica: `EXP003-MIDI-ADAPTER-v1`.
- Implementación: `tools/exp003/exp003_midi_verification_adapter.py`.
- SHA-256: `311F0B03946678E700690C47372A6832E45F4BBF5656E1E435A387225C295745`.
- La API pública `materialize_song_plan_v2` materializa el SongPlan y el
  adaptador fija el `Song.ppq` resultante a 1000 antes de una futura llamada
  autorizada a `write_midi`.
- El CLI `songplan render` no expone PPQ; esta especificación requiere la ruta
  adaptadora explícita.

La propagación PPQ está **CONFIRMADA ESTÁTICAMENTE** por la API de dominio y
por la comprobación no multimedia del adaptador. La escritura real de MIDI aún
requiere una ejecución autorizada; no se ha producido ningún archivo.

## Estado de verificación

- SongPlanV2 schema: PASS.
- Representabilidad exacta: PASS.
- Onsets absolutos: PASS.
- PPQ 1000 dentro de las restricciones del writer: PASS.
- CANARY-001: permanece `FAILED_BEFORE_MIDI_WRITE`.
- Gate E: **NOT YET PASS**; E2 queda `READY FOR TECHNICAL RE-VALIDATION`.
- Próximo intento, si se autoriza: `EXP003-CANARY-002`.
