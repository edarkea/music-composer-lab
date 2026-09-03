# music-engine integration contract for music-composer-lab

This document is the integration boundary for an external composition or research
system. `music-composer-lab` decides musical hypotheses and authors explicit
SongPlans. `music-engine` parses, validates, deterministically materializes, and
exports MIDI. This document describes the current implementation at commit
`71bbc73337da0d755618bdc796e19ce2e82cc3df`.

## Version and reproducibility

- Package: `music-engine` 4.0.0 (`pyproject.toml`); development version `v4.0.0`.
- Repository state: `master`, release-ready; stable release recorded by
  `project-state.toml` is `v3.1.0`.
- Preferred new format: SongPlanV2, `schema_version: "2.0"`.
- Compatibility: SongPlan 1.0, `schema_version: "1.0"`, remains accepted and can
  be explicitly migrated to V2. V1 and V2 are distinct codecs.
- External maps and percussion performance profiles currently use schema `1.0`.
- Record the exact commit, source plan, resource files, command, and output hash
  for experiments. The generated-document date is 2026-09-02.

## Integration boundary

```text
music-composer-lab
        | explicit musical intent
        v
SongPlan YAML/JSON -> parser/codec -> validator -> deterministic materializer
                                      -> Song/Track/Note -> MIDI writer -> .mid
```

The central rule is: **AI decides music. music-engine validates music.
music-engine materializes music.** The engine does not turn a style adjective,
chord name, or energy value into a composition.

## What music-engine decides vs what the composer decides

The current backend is **Case A: exact specification**. The composer supplies
events, pitches, onsets, durations, velocity, and (where used) semantic drum or
percussion identities. The engine derives timing ticks, arrangement occurrences,
motif/variation results requested by the plan, and MIDI encoding.

| Item | Current classification |
|---|---|
| pitches, pitch classes, registers/ranges | Composer decides; engine validates |
| chord voicings, rhythms, note counts, contour | Composer decides |
| bass, drum, percussion patterns and harmonies | Composer decides |
| sections, arrangement, motifs, variations | Composer declares explicitly |
| instrumentation/timbral family | Composer declares identifiers/`SoundIntent`; no instrument selection |
| random candidates | Not supported |
| tick conversion, motif occurrence placement, supported transformations, MIDI ordering | Engine derives deterministically |
| creative generation from style, energy, emotion, or a seed | Not supported |

Chord symbols in `arrangement.harmony_assignments` are metadata. **Chord symbols
do not generate notes. Explicit pitches are required.**

## Randomness and seeds

Runtime SongPlan parsing, validation, materialization, and MIDI writing use no
randomness. Search results for random/RNG/shuffle/choice do not identify a runtime
SongPlan generation path. There is no SongPlan render seed. The same valid plan,
resource files, and command produces the same symbolic materialization and MIDI;
the exact commit and resources must still be recorded. Deterministic performance
profiles may parameterize velocity behavior, but they do not introduce randomness.

## SongPlanV2 root

The strict V2 codec accepts exactly these root fields:

| Field | Required | Type and rules |
|---|---|---|
| `schema_version` | yes | string exactly `"2.0"` |
| `name` | yes | non-empty string |
| `tempo` | yes | positive BPM number accepted by `Tempo` |
| `time_signature` | yes | numerator/denominator object or accepted codec form; positive conventional values |
| `tonic` | yes | non-empty string; metadata, not automatic note generation |
| `mode` | yes | one of `ionian`, `dorian`, `phrygian`, `lydian`, `mixolydian`, `aeolian`, or `locrian` in the verified runtime |
| `style` | yes | non-empty string; descriptive metadata |
| `arrangement` | yes | object containing `sections` and `harmony_assignments` arrays |
| `tracks` | yes | array of typed track objects; track IDs must be unique |

Sections have `id`, `start_bar` (integer >=1), `bar_count` (integer >=1), and
`energy` (numeric range enforced by the model/schema). Harmony assignments have
`harmony` and either a `section_id` or explicit `start_bar`/`bar_count` range.
Energy and harmony are metadata and do not compose notes.

### Verified mode behavior

En el runtime local verificado de `music-engine` 4.0.0, los valores aceptados
para `mode` son `ionian`, `dorian`, `phrygian`, `lydian`, `mixolydian`,
`aeolian` y `locrian`. En este runtime, `ionian` debe utilizarse para representar
el modo mayor diatónico. Los ejemplos anteriores que utilizan `mode: major` no
reflejan el comportamiento observado y deben leerse como corregidos a
`mode: ionian` cuando se ejecuten con este runtime. La validación del
runtime/codec tiene prioridad sobre los ejemplos documentales. Esta observación
proviene del smoke test local y no debe extenderse a otras versiones de
`music-engine` sin verificación independiente.

## Tracks and events

`TrackType`, `TrackRole`, `SoundIntent`, and `PerformanceBinding` are different
axes. `TrackType` is closed: `pitched`, `drums`, `percussion`, `effect`.
`role` is an identifier validated by syntax, open-ended, and may be reused across
tracks. `SoundIntent` is a sparse timbral direction. `PerformanceBinding` points
to host-supplied runtime resources.

Track event structures are type-specific:

- `pitched` uses pitched motifs/events (`pitches` is a non-empty list of pitch
  strings), with optional `chromatic`, velocity, articulation, IDs, pitch range,
  and phrase connections.
- `drums` uses drum motifs/events with a `drum_voice` identifier and optional
  velocity/articulation.
- `percussion` uses percussion motifs/events with `instrument` and
  `sounding_articulation`, plus required `kit_id` and `map_id`.
- `effect` uses effect motifs/events with position and duration; it is not an
  audio generator.

Track objects require `id`, `type`, `role`, `motifs`, and
`section_assignments`; type-specific required fields are described above.
Assignments reference sections and motifs, optionally with a variation.

### Pitched events and timing

A pitched event is:

```yaml
- bar: 1
  beat: "1"
  duration: "1/4"
  pitches: [C4]
  velocity: 96
```

`pitches` accepts explicit pitch names understood by the domain pitch parser,
including note letter, optional accidental, and octave (for example `C4`, `Bb3`,
`C#5`). A list creates simultaneous notes. `velocity` is optional and, when
present, is 1..127. `chromatic` is an explicit boolean policy field exposed by
the V2 event codec; it does not invent pitches. MIDI channel is not authored on
V2 events; channel assignment is an engine/MIDI concern.

Position and duration deliberately use different units. `beat` is a **1-based
position in quarter-note beat units**. In 4/4:

```text
1 = beat 1     3/2 = 1&     2 = beat 2     5/2 = 2&
3 = beat 3     7/2 = 3&     4 = beat 4     9/2 = 4&
```

The full sixteenth grid is:

```text
1, 5/4, 3/2, 7/4, 2, 9/4, 5/2, 11/4,
3, 13/4, 7/2, 15/4, 4, 17/4, 9/2, 19/4
```

`duration` is a fraction of a **whole note**: whole `1`, half `1/2`, quarter
`1/4`, eighth `1/8`, sixteenth `1/16`, thirty-second `1/32`. Dotted and triplet
values are represented by exact fractions accepted by `Duration`, for example
dotted quarter `3/8`, dotted eighth `3/16`, quarter-note triplet `1/6`, and
eighth-note triplet `1/12`. Beat and duration reference units are different and
must never be interchanged.

Tempo is BPM. Time signature supplies numerator/denominator. Domain timing uses
exact `Fraction` values. PPQ is not a SongPlan root field; MIDI export uses the
engine's configured/default MIDI PPQ and converts exact positions/durations to
ticks. Values not exactly representable at the chosen PPQ are subject to the
writer's deterministic tick conversion.

## Arrangement, motifs, and transformations

Sections define bar ranges. Track assignments connect a section to a motif (or a
variation of one). Materialized occurrences are placed at the assigned section
range. Events are authored relative to their motif; validation/materialization
enforces the current range and timing rules. Notes may not be assumed to cross
section boundaries: author them within the applicable occurrence. Energy is
metadata only.

Motifs are declared inside the type-specific track as an `id` plus explicit
events. Reusing a motif reuses those explicit events at each assigned occurrence;
it does not creatively regenerate them. V2 supports these runtime operations:

| Operation | Parameters | Meaning |
|---|---|---|
| `transpose` | `semitones` integer | shift pitches |
| `octave_shift` | `octaves` integer | shift pitches by octaves |
| `rhythmic_displacement` | exact `offset` | shift positions |
| `truncate` | exact `before` | retain material at/after cutoff per runtime rules |
| `retrograde` | none | reverse supported event order/timing behavior |
| `augment` / `diminish` | exact `factor` | scale timing |
| `invert` | pitch `axis` | invert pitches around axis |

Operations are requested through a variation/development reference targeting a
motif. They are deterministic and restricted by validation (including valid
resulting timing/pitches). Thus transposition, octave shift, displacement,
retrograde, augmentation, diminution, and inversion are expressible; “keep the
rhythm but invent new pitches” is **not** a supported operation. No random
variation candidate facility exists.

## Drums

V2 drums author semantic `drum_voice` IDs, not assumed General MIDI pitches. A
`DrumExternalMap` resolves each voice to a MIDI pitch. Use
`--drum-map-dir DIR`; maps are found as `<map-id>.yaml` or `.json`, with an
optional adjacent deterministic template `<song-stem>_<map-id>.yaml`. A map may
also be selected through the explicit legacy `--drum-map-id` option where the
CLI contract requires it.

```yaml
schema_version: "2.0"
name: drum_test
tempo: 120
time_signature: 4/4
tonic: C
mode: ionian
style: test
arrangement:
  sections: [{id: main, start_bar: 1, bar_count: 1, energy: 0.5}]
  harmony_assignments: []
tracks:
  - id: kit
    type: drums
    role: drums
    motifs:
      - id: beat
        events:
          - {bar: 1, beat: "1", duration: "1/4", drum_voice: kick, velocity: 110}
    section_assignments: [{section_id: main, motif_id: beat}]
```

The corresponding external map is:

```yaml
schema_version: "1.0"
id: drum_test_kit
mappings:
  kick: 36
  clap: 39
```

Missing maps create a null/unfinished template and return controlled materialization
failure; no MIDI is written. Fill the pitches, preserve the map ID, and rerender.

## Percussion

Percussion is distinct from drums. Events author semantic `instrument` and
`sounding_articulation`; the track requires `kit_id` and `map_id`. An external
`PercussionMap` resolves each semantic pair to MIDI pitch. Optional
`PerformanceBinding` has family `percussion`, required `profile_id`, and optional
`style_profile_id`; these IDs refer to host-supplied profile files and are not
invented or auto-resolved.

```yaml
schema_version: "1.0"
id: example-map
assignments:
  - instrument: conga
    sounding_articulation: open
    pitch: 60
  - instrument: conga
    sounding_articulation: slap
    pitch: 61
```

The map codec requires exactly `schema_version`, `id`, and `assignments`; each
assignment has `instrument`, `sounding_articulation`, and `pitch`. Pitch is either
null or an integer 0..127; MIDI pitch **0 is valid**. Null is useful only in a
generated authoring template, not a render-ready mapping.

When a V2 map is missing, render generates `<song-stem>_<map-id>.yaml` containing
the exact semantic pairs used by all tracks sharing that map ID, deterministically
ordered, each with `pitch: null`, then fails with `percussion.missing_map`. Fill
all values and rerender. Existing malformed or incomplete maps are preserved and
fail; there is no GM fallback or semantic inference.

## SoundIntent and performance

`SoundIntent` is an abstract, validated timbral direction. Supported fields are
`family` plus optional `source_character`, `brightness`, `texture`, `weight`,
`transient`, `drive`, `width`, `movement`, and an optional envelope containing
`attack`, `sustain`, and `release`. Family vocabulary is type-specific (for
example pitched families include `piano`, `synth_bass`, `electric_piano`,
`pluck`, and `synth_lead`; percussion families are `acoustic`, `electronic`,
`hybrid`, `processed`, `synthetic`). Values are controlled vocabularies enforced
by the codec. A safe sparse example is:

```yaml
sound_intent: {family: synth_lead, brightness: bright, transient: defined}
```

It does not select a plugin, preset, synth, VST route, or audio sound design.
The supported V2 performance family is percussion. Profile and style-profile IDs
are host-supplied resource identifiers; resources do not exist automatically.

## Validation and failures

`music-midi songplan validate INPUT` parses and validates the selected SongPlan.
It checks strict fields/types and identifiers, schema version, unique track IDs,
track/event type compatibility, positive positions/durations, pitch and velocity
ranges, motif/section references, arrangement ranges, supported variation forms,
and performance/resource reference shape. Render repeats validity and additionally
resolves external resources and materializes the plan. Validation does not judge
whether music is good, catchy, emotional, or stylistically “Indie Dance”.

The CLI is `music-midi` (there is no current `midi-music` command). Relevant exit
codes are parse failure `2`, validation failure `3`, materialization failure `5`,
and I/O failure `4`. `songplan validate --json` emits deterministic JSON for
machine handling. Parse errors mean repair YAML/JSON; validation errors mean
repair only the reported contract issue; materialization errors mean supply or
repair the named external resource; I/O errors mean repair paths/permissions.
Missing or invalid drum/percussion maps are materialization failures. A missing
map's generated template is a first-pass authoring aid; fill it and retry.

## Output contract and MIDI guarantees

`songplan render INPUT --output OUTPUT` writes one Standard MIDI File at the
requested path. Failed renders do not intentionally leave a successful MIDI
output; missing-resource failures occur before writing. The writer uses the
materialized explicit notes, deterministic positions/durations, velocities, and
multiple tracks. Simultaneous events have stable deterministic ordering and note
closures are encoded deterministically. No JSON materialization report or
separate symbolic-note export is exposed by this CLI: **Not currently exposed by
this CLI.**

## Research control matrix

| Variable | Can lab control it? | How | Engine guarantee |
|---|---|---|---|
| tempo/meter | Yes | root fields | exact validated values |
| PPQ | No in SongPlan | engine/writer configuration | deterministic default/configuration |
| pitch/pitch class/exact note/register/range | Yes | explicit pitch and `pitch_range` | no creative pitch invention |
| rhythm/onset/duration | Yes | `bar`, `beat`, `duration` | exact Fraction semantics |
| velocity | Yes | event velocity | 1..127 validation |
| note count/chord pitches | Yes | explicit events/pitch lists | simultaneous explicit notes |
| chord symbol | Metadata only | harmony assignment | never realizes notes |
| bass rhythm, drum voice, percussion articulation | Yes | explicit typed events/maps | deterministic mapping only |
| section/energy | Yes | arrangement | energy does not generate notes |
| motif reuse | Yes | motifs and assignments | deterministic copying/occurrence |
| transposition/octave shift/displacement | Yes | supported variations | deterministic transformation |
| retrograde/augmentation/diminution/inversion | Yes | supported variations | deterministic, validated result |
| random seed | No | none | no random render path |
| SoundIntent | Yes | sparse track field | metadata/direction only |
| plugin/preset | No | outside contract | no automatic routing |
| MIDI channel | Not authored in V2 | writer/materializer behavior | deterministic engine assignment |

## Minimal workflow (PowerShell)

```powershell
@"
schema_version: "2.0"
name: lab_minimal
tempo: 120
time_signature: 4/4
tonic: C
mode: ionian
style: experiment
arrangement:
  sections: [{id: main, start_bar: 1, bar_count: 1, energy: 0.5}]
  harmony_assignments: []
tracks:
  - id: melody
    type: pitched
    role: lead
    motifs:
      - id: phrase
        events:
          - {bar: 1, beat: "1", duration: "1/4", pitches: [C4], velocity: 96}
          - {bar: 1, beat: "2", duration: "1/4", pitches: [E4], velocity: 96}
    section_assignments: [{section_id: main, motif_id: phrase}]
"@ | Set-Content lab_minimal.yaml
music-midi songplan validate lab_minimal.yaml
music-midi songplan render lab_minimal.yaml --output lab_minimal.mid
```

The example is complete, pitched-only, and needs no external resource. A lab
should save the source YAML, validation result, command, and resulting MIDI hash.

## Musical examples

### Melody

```yaml
tracks:
  - id: melody
    type: pitched
    role: lead
    motifs:
      - id: line
        events:
          - {bar: 1, beat: "1", duration: "1/8", pitches: [C4], velocity: 90}
          - {bar: 1, beat: "3/2", duration: "1/8", pitches: [D4], velocity: 82}
          - {bar: 1, beat: "2", duration: "1/4", pitches: [G4], velocity: 100}
    section_assignments: [{section_id: main, motif_id: line}]
```

This fragment must be inserted into a complete V2 root like the minimal example.
Its interpretation is: `(bar 1, beat 1, C4, onset beat 1, duration eighth)`,
`(1, 3/2, D4, 1&, eighth)`, `(1, 2, G4, beat 2, quarter)`.

### Chords

Use explicit pitch lists, for example:

```yaml
- id: voicings
  events:
    - {bar: 1, beat: "1", duration: "1/8", pitches: [C4, E4, G4], velocity: 88}
    - {bar: 1, beat: "2", duration: "1/2", pitches: [A3, C4, E4, G4], velocity: 76}
```

The first is a short stab and the second a sustained chord. These are not
realizations of `C` or `Am7`; every MIDI pitch is explicit.

### Indie Dance control example

The style field may say `indie_dance`, but the following musical decisions remain
explicit: kick events on beats 1, 2, 3, 4; bass events at 1, 2&, 3, 4&; and keys
at 1&, 2, 3&, 4. Use `beat: "5/2"` for 2&, `"7/2"` for 3&, and `"9/2"` for 4&.
This is a control example, not a claim of stylistic quality. Drums additionally
require a `DrumExternalMap`; pitched-only experiments avoid that resource.

### Motif/transformation

Motif reuse and the supported variation operations are available as described
above. A complete minimal transformation should be authored and validated against
the current codec; do not invent a separate “generate from motif” syntax.

## What not to ask music-engine to do

Do not ask it to invent a melody from “sad”, choose voicings from `Am7`, create a
bassline from a style name, generate random candidates from a seed, choose a VST
or preset, generate audio, mix/master, or infer a MIDI mapping from plugin names.
Do not assume `energy`, `tonic`, `mode`, `style`, `SoundIntent`, or harmony text
will create notes. Author the notes and provide every required external mapping.

## Guidance for AI composers

Use `schema_version: "2.0"`; never invent fields or identifiers; distinguish beat
from whole-note duration; use explicit pitches; keep track type and event type
aligned; use host-supplied map/profile IDs; never infer mappings; validate before
render; and repair only reported contract errors while preserving musical intent.
Schema-safe does not necessarily mean codec-safe: strict codecs reject unknown
fields, missing required fields, invalid identifier syntax, and invalid nested
values even when a loose schema interpretation might appear plausible.

## Experiment-design implications

Appropriate experiments compare explicit rhythms, durations, pitches, voicings,
bass onsets, section density, motif reuse, and deterministic transformations
while holding other inputs constant. The lab should implement any higher-level
search itself: the engine cannot generate 100 random melodies, realize a contour
into pitches, or compose from an emotional adjective.

## Reproducibility checklist

Record: experiment ID; music-engine package version; exact git commit; SongPlan
schema version; source SongPlan; every external map/profile file; PPQ/configuration
if changed; exact PowerShell render command; output MIDI hash; validation result;
and the separate listening/evaluation result. Research judgments are not engine
guarantees.

## Source of truth

For an external integration, resolve contradictions in this order: (1) installed
runtime behavior and CLI result, (2) executable models/codecs and materializer,
(3) validator behavior, (4) packaged JSON Schema, (5) current documentation, and
(6) examples. This repository's permanent engineering rules likewise put the
user task first, then repository instructions, release state, active requirements,
focused docs/tests, and historical documents. Historical requirements are frozen
records and are not current capability evidence.

## Final classification

`music-engine` is **CASE A — exact specification** with a deterministic mechanical
layer for arrangement, motif reuse, explicitly requested transformations, external
mapping, and MIDI encoding. It is not a Case B contour-to-note generator or a
Case C high-level generative composer.
