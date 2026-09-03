# use-music-engine

## Purpose

Use `music-engine` as the deterministic MIDI materialization backend for
`music-composer-lab`.

This skill translates an already approved musical or experimental specification
into a valid SongPlan, validates it with the project-local `music-engine`
runtime, and renders MIDI when requested.

This skill is an integration skill.

It does NOT define composition knowledge.
It does NOT design research hypotheses.
It does NOT evaluate musical quality.
It does NOT modify `music-engine`.

---

## Required context

Before using this skill, read:

- `AGENTS.md`
- `PROJECT.md`
- `integrations/music-engine/integration-contract.md`
- `integrations/music-engine/local-runtime.md`
- `integrations/music-engine/runtime-lock.yaml`, if present

When working on an experiment, also read the complete experiment specification,
for example:

- `experiments/EXP-001.md`

The experiment is the source of musical intent.

The integration contract is the source of truth for what `music-engine` can
materialize.

Do not replace either with assumptions.

---

## Core boundary

The project boundary is:

```text
music-composer-lab
        |
        | musical decisions / experimental conditions
        v
SongPlan YAML
        |
        v
music-engine
        |
        | parse + validate + deterministic materialization
        v
MIDI

`music-composer-lab` decides the music.

`music-engine` validates and materializes the music.

Do not ask `music-engine` to make creative decisions that its public contract
does not support.

---

## Engine model

Treat the current `music-engine` integration as:

**CASE A — exact specification**

The authoring agent must explicitly provide musical material when required,
including:

* pitches;
* beat positions / onsets;
* durations;
* velocities when controlled;
* chord pitches / voicings;
* bass notes;
* drum or percussion events;
* motif material.

Metadata such as:

* `style`;
* `energy`;
* `tonic`;
* `mode`;
* harmony labels;
* `SoundIntent`;

must never be assumed to generate musical notes automatically.

---

## Supported engine transformations

Use only transformations documented by the active integration contract.

The current contract supports deterministic operations including:

* `transpose`;
* `octave_shift`;
* `rhythmic_displacement`;
* `truncate`;
* `retrograde`;
* `augment`;
* `diminish`;
* `invert`.

Do not invent transformation syntax.

Do not assume that the engine can:

* invent pitches while preserving contour;
* generate melodies from style descriptions;
* create random alternatives;
* generate from emotion or energy;
* realize chord symbols automatically;
* choose plugins or presets;
* generate audio.

If an experimental condition cannot be expressed through the current public
contract, report that limitation.

Do not modify `music-engine` to make the experiment possible.

---

## SongPlan policy

Prefer SongPlanV2:

```yaml
schema_version: "2.0"
```

unless the active integration contract explicitly requires another version.

Never invent SongPlan fields.

Use the exact public contract.

For pitched material, pitches must be explicit when required by the experiment.

Example pitched event:

```yaml
- bar: 1
  beat: "1"
  duration: "1/4"
  pitches: [C4]
  velocity: 96
```

Important timing rule:

* `beat` is a 1-based position in quarter-note beat units;
* `duration` is a fraction of a whole note.

These units are different.

Never interchange them.

---

## Musical decision policy

This skill may encode musical decisions that are already approved or explicitly
specified by the experiment.

It must not silently introduce new compositional principles or musical choices.

When translating an experiment to SongPlan, distinguish between:

1. mechanical realization;
2. new musical decision.

### Mechanical realization

Example:

An approved experiment says:

> Transpose motif A upward by 2 semitones.

Using the documented `transpose` transformation is mechanical realization.

It does not require a new compositional decision.

### New musical decision

Example:

An experiment says:

> Preserve rhythm and contour but change interval sizes.

If the resulting pitches are not already specified, choosing those pitches is a
new musical decision because `music-engine` does not invent them.

Do not disguise such a choice as a technical implementation detail.

When a new musical decision is required:

* use the explicit realization already approved in the experiment; or
* propose the missing realization for methodological review before execution.

Never silently invent the missing music.

---

## Experiment integrity

Once an experiment marks its stimuli or conditions as frozen, preserve them.

Do not modify musical material after listening to the generated MIDI merely to
make a hypothesis appear more successful.

After freezing, changes are allowed only for objective implementation errors,
such as:

* invalid SongPlan syntax;
* incorrect timing encoding;
* wrong pitch caused by transcription error;
* unsupported field;
* incorrect motif or variation reference;
* corrupted external resource;
* failed render caused by contract misuse.

If fixing an error changes actual musical content, record the change and
invalidate the previous experimental run when appropriate.

---

## Runtime isolation

Use the project-local runtime.

Preferred executable:

```powershell
.\.venv\Scripts\music-midi.exe
```

Do not rely on a globally installed `music-midi` when the project-local runtime
exists.

Do not use:

* `PYTHONPATH` hacks;
* editable installation from the `music-engine` source repository;
* imports directly from the external source tree;
* direct modifications to the `music-engine` repository.

The lab must operate using the installed wheel and the public integration
contract.

---

## Preflight check

Before the first engine operation in a task, verify that the local runtime is
available.

Run:

```powershell
.\.venv\Scripts\music-midi.exe --help
```

When provenance is uncertain, verify the installed package location:

```powershell
.\.venv\Scripts\python.exe -c "import music_engine; print(music_engine.__file__)"
```

The package should resolve inside the project's `.venv`.

If the runtime is missing or incorrect:

* stop;
* report the environment problem;
* do not build `music-engine`;
* do not modify external repositories.

---

## Validation workflow

Always validate before rendering.

Run:

```powershell
.\.venv\Scripts\music-midi.exe songplan validate <PLAN>
```

When useful for an experiment record, prefer machine-readable validation:

```powershell
.\.venv\Scripts\music-midi.exe songplan validate <PLAN> --json
```

Never skip validation because the YAML appears correct.

Schema-safe does not necessarily mean codec-safe.

---

## Render workflow

Render only after successful validation.

Run:

```powershell
.\.venv\Scripts\music-midi.exe songplan render <PLAN> --output <OUTPUT.mid>
```

`music-engine` generates MIDI.

It does not generate audio.

Do not add an audio-rendering pipeline unless explicitly requested by the
Project Owner.

---

## Error handling

Respect the engine error category.

### Parse failure

Repair only YAML or JSON representation problems.

Do not change musical intent.

### Validation failure

Repair only the reported contract violation.

Do not make unrelated musical changes.

### Materialization failure

Check:

* required external resources;
* motif references;
* supported transformations;
* drum maps;
* percussion maps;
* performance resources when applicable.

Do not rewrite the composition simply to force a successful render.

### I/O failure

Repair paths, filenames, or permissions.

---

## Determinism

The current engine does not provide creative random generation or a SongPlan
seed.

Given the same:

* valid SongPlan;
* installed engine build;
* external resources;
* configuration;
* render command;

the symbolic materialization should be deterministic.

Do not invent a `seed` field.

---

## Reproducibility

For experimental runs, record as much of the following as available:

* experiment ID;
* SongPlan schema version;
* source SongPlan path;
* `music-engine` package version;
* engine git commit represented by the installed wheel;
* wheel SHA256 when tracked;
* runtime lock information;
* external map/profile files;
* exact validation command;
* validation result;
* exact render command;
* output MIDI filename;
* output MIDI SHA256;
* relevant engine configuration if changed.

A deterministic render proves reproducibility of the materialization.

It does NOT prove that a musical hypothesis is valid.

---

## Artifact policy

### SongPlan

The SongPlan defining an experiment is part of the experimental record and should
normally be preserved.

### Validation record

Preserve when it contributes to experimental reproducibility.

### MIDI

MIDI is a generated experimental artifact.

It is not composition knowledge.

Whether generated MIDI is committed or ignored follows project policy.

### Audio

Audio is outside the responsibility of this skill.

---

## Evaluation boundary

Successful validation means:

> The SongPlan satisfies the `music-engine` contract.

Successful rendering means:

> `music-engine` successfully materialized the supplied symbolic instructions
> into MIDI.

Neither result means:

* the melody is good;
* the composition is effective;
* the hypothesis is supported;
* the music is catchy;
* the genre is correct;
* the artistic result is successful.

Those judgments belong to the experiment and to human evaluation.

---

## Never do automatically

Do not automatically:

* modify `manual/`;
* modify `rules/`;
* modify evaluation rubrics;
* approve musical principles;
* write experimental Results;
* write experimental Interpretation;
* change Confidence;
* modify `music-engine`;
* build a new engine wheel;
* install from the `music-engine` source repository;
* generate audio;
* invent undocumented engine capabilities;
* invent SongPlan fields;
* interpret validation success as musical evidence.

---

## Workflow

When asked to materialize an approved experiment:

1. Read the experiment.
2. Read the active `music-engine` integration contract.
3. Read the local runtime documentation.
4. Read the runtime lock if available.
5. Verify the local runtime.
6. Determine whether the experimental condition is expressible with the current
   engine contract.
7. Identify any remaining musical decisions.
8. Stop for methodological review if a required musical decision has not already
   been approved.
9. Create the SongPlan YAML.
10. Validate the SongPlan.
11. Repair only contract or representation errors without changing musical
    intent.
12. Render MIDI when requested.
13. Record reproducibility information.
14. Report generated artifacts and limitations.
15. Stop before interpretation or evaluation unless explicitly requested to
    continue.

---

## Report format

After significant use of this skill, report:

### What I changed

List files created or modified.

### Engine validation

Report:

* runtime used;
* SongPlan schema;
* validation status;
* relevant validation issues.

### Materialization

Report:

* whether MIDI was created;
* output path;
* deterministic transformations used;
* external resources used.

### Musical decisions introduced

List any musical decisions that were not already explicit in the experiment.

If none, write:

`None.`

### Reproducibility

Report available:

* engine version;
* commit;
* wheel hash;
* SongPlan path;
* validation command;
* render command;
* MIDI hash.

### Limitations or contract gaps

Report anything required by the experiment that the current `music-engine`
contract cannot express.

### Questions for the Music/Methodology Director

Include only unresolved methodological or musical questions.

### Recommended next step

Recommend exactly one next action.

Do not automatically continue to the next experimental or research phase.