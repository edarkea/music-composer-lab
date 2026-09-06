# EXP-003 — Especificación de verificación MIDI v2

Esta especificación define la adaptación genérica de las 24 combinaciones
congeladas de EXP-003. La v1 permanece como registro histórico de CANARY-002.

## Entradas autoritativas

- Item freeze v2: `experiments/EXP-003/EXP-003-item-freeze-manifest-v2.yaml`
  - SHA-256: `940D317684BF17BCB5CAF3EA9E08CCE4FE8C428BC1CD63F4C2004D32739E5B64`
- Render spec v2: `experiments/EXP-003/EXP-003-rendering-spec-v2.md`
  - SHA-256: `25B7238C6854BDE63C47E40C27F82C6FA7A5C89946C255ED771FB6FC3CFD2625`

## Adaptador

- Identidad: `EXP003-MIDI-ADAPTER-v2`.
- Implementación: `tools/exp003/exp003_midi_verification_adapter_v2.py`.
- SHA-256: `CB478EF0C3464F4F5389D84695C440060D62C6DABEC0FBA36F9C758D167D6074`.
- Entrada: manifiesto de item freeze, `family_id` y condición.
- Combinaciones válidas: `EXP003-F01`–`EXP003-F12` con `LOW_SELECTED` o
  `HIGH_SELECTED`; exactamente 24.
- El adaptador no contiene tablas de pitches: selecciona `R1_pitches_midi` y
  `R2_LOW/HIGH_pitches_midi` del manifiesto.
- Los IDs de evento son locales al artifact (`R1-V1`…`R2-V4`); el namespace
  global es `(internal_asset_id, event_id)`. Los 24 `internal_asset_id` son
  únicos.
- No escribe MIDI/WAV ni invoca el renderer durante sus pruebas.

## Codificación temporal exacta

- Tempo metadata: `120 BPM`.
- PPQ: `1000`.
- R1: `bar: 1`, `beat: "3/2"`.
- R2: `bar: 1`, `beat: "5/2"`.
- Duración: `"6/25"`.
- R1 ON/OFF: `500/1460` ticks.
- R2 ON/OFF: `1500/2460` ticks.
- Duración MIDI: `960` ticks.

No se permite redondeo, truncado, ceiling, epsilon, cuantización ni fallback.
La conversión debe permanecer exactamente representable.

## Resultados de pruebas no multimedia

- Expansión legal: **24/24 PASS**.
- Correspondencia de pitches contra el freeze: **24/24 PASS**.
- Conteo de eventos: **24/24 PASS**, ocho por stimulus.
- Timing y velocity: **24/24 PASS**.
- Representabilidad PPQ/ticks: **24/24 PASS**.
- Validación SongPlanV2: **24/24 PASS**.
- Regresión F01 LOW: **PASS**.
- Hash del artifact canónico F01 LOW: **sin cambios**,
  `D25B504CF5CB57749B4ECC51C0145BA83827A7BC452AE4939218338A3C6E9BF2`.
- Decisiones musicales nuevas: **ninguna**.

Estas pruebas validan el mapping técnico en memoria; no constituyen evidencia
perceptual ni autorizan producción de assets.
