# EXP-003 CANARY-002 — Provenance

## Result

- Canary: `EXP003-CANARY-002`
- Item: `EXP003-F01`
- Condition: `LOW_SELECTED`
- Result: **SUCCESS**
- Lineage: `CANARY-001 FAILED_BEFORE_MIDI_WRITE` → MIDI timing
  representability audit → `EXP003-MIDI-ADAPTER-v1` → MIDI-verification
  spec v1 → `CANARY-002`
- `CANARY-001` remains unchanged and failed before MIDI write.
- All CANARY-002 media are **TECHNICAL VALIDATION ONLY** and **NOT PARTICIPANT
  ASSETS**.

## Authoritative hashes

| artifact | SHA-256 | result |
|---|---|---|
| item freeze v2 | `940D317684BF17BCB5CAF3EA9E08CCE4FE8C428BC1CD63F4C2004D32739E5B64` | PASS |
| render spec v2 | `25B7238C6854BDE63C47E40C27F82C6FA7A5C89946C255ED771FB6FC3CFD2625` | PASS |
| deterministic renderer | `89E61135B51728F9D469B6658AF494DFA9AD638CB921173ABAEEA05DFE4B7404` | PASS |
| MIDI adapter v1 | `311F0B03946678E700690C47372A6832E45F4BBF5656E1E435A387225C295745` | PASS |
| MIDI verification spec v1 | `346D4A24023A85128050BF69EECDCA394F3869F8A34BB48CD98882518C76E134` | PASS |
| canonical F01 LOW events | `D25B504CF5CB57749B4ECC51C0145BA83827A7BC452AE4939218338A3C6E9BF2` | PASS |

Freeze validator: **12/12 PASS**.

## Runtime

- Python: `3.14.3`
- `music-engine`: `4.0.0`
- Engine commit: `71bbc73337da0d755618bdc796e19ce2e82cc3df`
- Wheel SHA-256: `110E987A1E102C1CF3D29FEC1CCC68583459030F40748E10D66CE1F8E4819FE1`
- MIDI metadata tempo: `120 BPM`
- Actual MIDI header PPQ: `1000`

## MIDI verification

- Path: `EXP003-CANARY-002-F01-LOW.verification.mid`
- Size: `162` bytes
- SHA-256: `C2262E47A83EAAA918D75E9E556B2BC6A8B291BC99EE91614C6578F060E509EC`
- R1 pitches: `[48, 52, 60, 67]`
- R2 LOW pitches: `[43, 55, 62, 71]`
- Velocity: `96` for all notes
- R1 ON: `500` ticks
- R1 OFF: `1460` ticks
- R2 ON: `1500` ticks
- R2 OFF: `2460` ticks
- Unintended pitched notes: **NO**
- Unintended sound-affecting controllers/program changes: **NO**
- MIDI event fidelity: **PASS**
- MIDI absolute timing fidelity: **PASS**
  - `500 × 0.0005 = 0.250 s`
  - `1460 × 0.0005 = 0.730 s`
  - `1500 × 0.0005 = 0.750 s`
  - `2460 × 0.0005 = 1.230 s`
- Approximation: **NO**

## WAV verification

Audio was rendered twice directly from the canonical event representation, not
from MIDI.

| run | path | size | SHA-256 |
|---|---|---:|---|
| 1 | `EXP003-CANARY-002-F01-LOW.audio.run1.wav` | `288044` bytes | `E722C0F6DD973826746DF7F8796361C8647B20DFF0C682628495ABD8A68574BF` |
| 2 | `EXP003-CANARY-002-F01-LOW.audio.run2.wav` | `288044` bytes | `E722C0F6DD973826746DF7F8796361C8647B20DFF0C682628495ABD8A68574BF` |

- File-bit identical: **YES**
- PCM-bit identical: **YES**
- Channels: `1` (mono)
- Sample rate: `48000 Hz`
- Bit depth: `24-bit signed integer PCM`
- Frames: `96000`
- Duration: `2.000 s`
- Actual peak: `2098232`
- Clipping: **NO**
- Nonempty sounding region: frames `12001–59999` (zero-based inspection)
- R1 onset frame: `12000`
- R1 note-off frame: `35040`
- R1 release completion / zero: `36000`
- R2 onset frame: `36000`
- R2 note-off frame: `59040`
- R2 release completion / zero: `60000`
- Final silence: frames `60000–95999` are zero
- R1/R2 unintended overlap: **NO**

## Gate status

- E1: **PASS WITH SCOPE**
- E2: **PASS WITH SCOPE**
- E3: **PASS WITH SCOPE**
- E4: **PASS WITH SCOPE**
- E5: **PASS WITH SCOPE**
- E6: **PASS IN CANONICAL ENVIRONMENT**
- Overall Gate E: **PASS WITH SCOPE**

Bulk MIDI: **NOT AUTHORIZED**  
Bulk WAV: **NOT AUTHORIZED**  
Pilot: **NOT AUTHORIZED**  
Participants: **NOT AUTHORIZED**
