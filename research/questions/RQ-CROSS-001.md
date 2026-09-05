# RQ-CROSS-001 - Temporal Cues to Local Melodic Arrival

## Status

- `status: SYNTHESIZED`
- `candidate_audit_status: COMPLETED`
- `candidate_audit_evidence_gate: PASS`
- `next_unused_candidate_id: CAND-CROSS-002`
- `scope: llegada melodica local, no equivalente a cierre total`

## Central question

Para una llegada melodica local, que evidencia existe sobre contribuciones
separadas o conjuntas de alargamiento del evento final y silencio posterior,
bajo contexto metrico, armonico y formal declarado?

La pregunta compositiva es cuando, si acaso, la evidencia justifica considerar
alargamiento, silencio, ambos o ninguno para hacer mas legible una llegada local.

## Construct definitions

### Local arrival

En esta RQ, `local arrival` es un objetivo compositivo/analitico de que un
evento melodico alcance un punto local interpretable dentro de una frase o
unidad, sin afirmar cierre completo de frase, seccion o cancion.

La literatura inspeccionada no ofrece una operacionalizacion unica y directa
de este constructo. Por eso no se puede tratar como sinonimo de completion,
boundary detection, cadence, closure, tension release o preference.

### Lengthening

`Final-event lengthening` significa una duracion relativamente mayor del
evento final respecto de su contexto melodico inmediato, no una duracion
absoluta universal ni un umbral numerico.

### Post-event silence

`Post-event silence` significa un intervalo sin el evento melodico despues del
evento final observado o manipulado. No se trata como sinonimo automatico de
rest notado, phrase gap, IOI, articulacion, boundary o closure.

## Factor separation

Las cuatro configuraciones conceptuales son:

| Duration | Post-event silence | Label |
|---|---|---|
| baseline | absent | A |
| lengthened | absent | B |
| baseline | present | C |
| lengthened | present | D |

La literatura no ofrece un factorial musical limpio que permita separar todos
los efectos. No se inventa un resultado para las celdas ausentes.

## Evidence table

| Source | Cue manipulated/observed | Comparison | Measured construct | Harmonic context | Metric context | Result | Scope | Directness |
|---|---|---|---|---|---|---|---|---|
| SRC-EMPIRICAL-020 | pause length, last-tone length, implicit harmonic function | natural melodies sorted by boundary cues; partial confounding | phrase-boundary processing/recognition, EEG/MEG | varied and partly represented by boundary-tone function | meter and phrase position in repertoire | pause and boundary-tone length modulated boundary processing; interaction not isolated cleanly | Western art-music melodies, musicians/nonmusicians | PARTIAL |
| SRC-EMPIRICAL-021 | inserted pause, tone duration and pitch pattern | natural vs shifted phrase segmentation; altered rhythmic/pitch patterns | infant orientation/preference to phrase structure | Mozart tonal context | phrase positions in minuets | pause placement and duration/pitch patterns affected phrase-structure response | infants, Mozart minuets | INDIRECT |
| SRC-EMPIRICAL-010 | silence after musical material | contextual extracts and constructed stimuli | silence detection, tension and characterization | strongly context-dependent, especially tonal context | metric/formal position not a clean factorial | identical silence was experienced differently by context; not a local-arrival measure | mixed musical extracts, nonmusicians | INDIRECT |
| SRC-EMPIRICAL-011 | production dwell time at phrase-limit chords | boundary chords vs other chords in self-paced production | temporal production at phrase boundaries | tonal effect larger; atonal comparison included | phrase boundary context, not isolated metric placement | listeners lengthened boundary chords in production | Bach chorales and constructed sequences | INDIRECT |
| SRC-EMPIRICAL-016 | cadential context including duration/density and melodic/harmonic cues | completion categories in Mozart excerpts | completion rating, not local arrival | harmonic bass/soprano stability central | formal subordinate-theme context | timing-related features modulated completion ratings, but no isolated lengthening/silence comparison | Mozart keyboard sonatas | INDIRECT |

## Context accounting

| Variable | Status in inspected evidence |
|---|---|
| meter / metric position | present in musical phrase materials, not cleanly controlled across all studies |
| harmonic context | present or varied; often confounded with boundary tone/function |
| formal role | phrase boundary, cadential or subordinate-theme contexts; not local arrival as independent construct |
| register | generally unreported or not central |
| preceding rhythmic context | varies with phrase materials; not factorially isolated |
| tempo | not a primary comparative factor |
| contour / final pitch | present and sometimes influential |
| articulation / texture | partly embedded in stimuli, not isolated |

## Structure -> perception -> composition

### Structural facts

Some inspected musical materials contain longer final tones, pauses, or both
near phrase boundaries. Studies also manipulate or sort by these cues.

### Perceptual results

The measured outcomes are phrase-boundary processing, segmentation,
orientation/preference, silence detection, production timing, completion
ratings and neural markers. None is automatically local arrival.

### Implicaciones compositivas

The evidence supports at most a bounded heuristic that these cues may be
considered when a boundary or phrase-organization goal is already declared.
It does not justify “use a long note and a rest to create arrival” or a
preference for both cues.

## Means-end table

| Means | Target effect | Evidence basis | Scope | Comparative support | Main confounds | Composer action justified? |
|---|---|---|---|---|---|---|
| final-event lengthening | boundary-related processing or local temporal emphasis | Neuhaus, Jusczyk/Krumhansl, Kragness/Trainor | phrase/boundary tasks | FILTER ONLY / PARTIAL | silence, harmony, contour, phrase role | consider as a scoped option, not rank |
| post-event silence | phrase segmentation/boundary processing | Neuhaus, Jusczyk/Krumhansl, Margulis | phrase/silence tasks | FILTER ONLY / PARTIAL | placement, preceding tone, harmony, task | consider as a scoped option, not rank |
| lengthening + silence | stronger boundary-cue package | Neuhaus and related boundary literature | phrase-boundary context | PACKAGE-ONLY / INSUFFICIENT FOR ARRIVAL RANK | factors partly confounded | retain as an alternative package, not preference |
| neither / baseline | absence of those cues | comparison conditions in some studies | task-specific | INSUFFICIENT FOR LOCAL ARRIVAL | other structural cues remain | remains a valid option |

## Comparative decision result

| Comparison | Result |
|---|---|
| lengthening vs baseline | FILTER ONLY; INSUFFICIENT for local-arrival ranking |
| silence vs baseline | FILTER ONLY; INSUFFICIENT for local-arrival ranking |
| lengthening + silence vs baseline | PACKAGE-ONLY; INSUFFICIENT for local-arrival ranking |
| lengthening vs silence | INSUFFICIENT; no clean direct musical comparison found |
| combination vs each alone | INSUFFICIENT; no factorial musical evidence isolating interaction |

No comparison reaches `RANK SUPPORTED` for the target construct.

## Metric, harmonic and formal findings

Metric position matters as context for phrase interpretation, but no source
supports strong beat = arrival. Harmonic function of the final tone influences
boundary processing in Neuhaus, so duration and silence cannot be credited
independently of harmony. Formal evidence concerns phrase boundaries or
completion, not a general local-arrival function.

The inherited distinctions remain:

- melodic temporal cue != harmonic arrival;
- local arrival != boundary;
- local arrival != cadence;
- local arrival != full closure.

## Capability result

- `CAN ENUMERATE`: YES — baseline, lengthening, silence and combined package
  can be represented as distinct alternatives.
- `CAN FILTER`: PARTIAL — context can rule out or qualify options, especially
  when the goal is boundary/phrase organization rather than arrival itself.
- `CAN RANK`: NO — no direct evidence prefers lengthening, silence, both or
  neither for local arrival.

## Candidate audit result

`CAND-CROSS-001` queda como `REVISE / POSSIBLE_WITH_SCOPE`. Su tipo es
`COMPARATIVE_DECISION_CONSTRAINT`: documenta que la evidencia de phrase
boundary no puede transferirse automaticamente a un ranking de local arrival.
No se creo `CAND-CROSS-002` y no se promovio conocimiento comparativo positivo.

## Candidate audit evidence gate

**PASS.** El candidato auditado conserva soporte suficiente para la
restriccion negativa acotada. La comparacion directa de local arrival sigue
sin resolverse y no se convierte en conclusion positiva.

## Puerta de experimento

**NOT JUSTIFIED en esta RQ.** La literatura no proporciona una
operacionalizacion estable e independiente de `local arrival` entre las tareas
inspeccionadas, y los estudios existentes no separan limpiamente duration y
silence bajo contextos armonicos y metricos comparables. Es una pregunta
residual precisa para trabajo posterior, no un diseño experimental aqui.
`EXP-002` permanece intacto.

## Phase-2 methodological result

**PARTIALLY.** La RQ produjo un diagnostico comparativo util:

- existe evidencia de un paquete de cues de boundary;
- lengthening y silence pueden representarse por separado;
- no existe evidencia inspeccionada de ranking directo para local arrival;
- la deuda restante esta especificada con precision, no de forma vaga.

## Recommended next step

Actualizar Composer Foundations con esta restriccion comparativa auditada
antes de decidir si la comparacion de local arrival merece trabajo
experimental posterior.
