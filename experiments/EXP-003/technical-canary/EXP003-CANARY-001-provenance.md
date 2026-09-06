# EXP-003 Technical Canary 001 — Failure record

## Scope

- `canary_id: EXP003-CANARY-001`
- `family: EXP003-F01`
- `condition: LOW_SELECTED`
- `status: FAILED_BEFORE_MIDI_WRITE`
- `classification: TECHNICAL CANARY; NOT PARTICIPANT ASSET`

## Frozen inputs

- item freeze-v2 SHA-256: `940D317684BF17BCB5CAF3EA9E08CCE4FE8C428BC1CD63F4C2004D32739E5B64`
- render-spec-v2 SHA-256: `25B7238C6854BDE63C47E40C27F82C6FA7A5C89946C255ED771FB6FC3CFD2625`
- renderer source SHA-256: `89E61135B51728F9D469B6658AF494DFA9AD638CB921173ABAEEA05DFE4B7404`
- event artifact: `EXP-003-CANARY-001-F01-LOW.events.json`
- event SHA-256: `D25B504CF5CB57749B4ECC51C0145BA83827A7BC452AE4939218338A3C6E9BF2`
- SongPlan: `EXP003-CANARY-001-F01-LOW.songplan.yaml`

## Environment

- OS: `Windows-11-10.0.26200-SP0`
- Python: `3.14.3`
- `music-engine`: `4.0.0`
- schema: `SongPlanV2 2.0`

## Results before failure

- freeze validator: `12/12 PASS`
- canonical event validator: `PASS`
- SongPlan validation: `SUCCESS`
- exact R1: `[48,52,60,67]`
- exact R2 LOW: `[43,55,62,71]`
- event count: `8` (`4 R1 + 4 R2`)
- MIDI generated: `NO`
- WAV generated: `NO`

## Failure

The single authorized MIDI materialization command failed with:

`MATERIALIZATION_FAILURE: duration cannot be represented exactly at the selected PPQ`

The SongPlan duration `6/25` is an exact representation of the canonical
0.480-second event duration in the event layer, but it is not exactly
representable at the engine's selected MIDI PPQ. The canary stopped at this
point, as required. No timing, renderer, gain, freeze or spec was changed.

## Gate consequence

- E1: `PASS WITH SCOPE`
- E2: `FAIL / BLOCKED BY MIDI TIMING REPRESENTABILITY`
- E3: `NOT TESTED`
- E4: `NOT TESTED`
- E5: `NOT TESTED`
- E6: `NOT TESTED`
- Overall Gate E: `FAIL — CANARY BLOCKED BEFORE MEDIA`

Technical canary remains unsuccessful. Any remediation requires methodological
review of the exact event-to-SongPlan timing contract or an independently
authorized renderer-only canary path. No automatic retry is permitted.
