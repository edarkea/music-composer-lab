# Stage 1 hardening candidate v1.1

This candidate is for a future prospective test. It is not `composer-interface-v1.2` and does not modify v1.1.

## Changes

- `stage-1-output-schema-v1.1-hardened.json`: structural JSON Schema for one DecisionTrace object, exact decision fields and N3-P enum/fields.
- `stage-1-prompt-clarified-v1.1.txt`: literal serialization wording only.
- `staged_runner.py --format-schema`: sends the supplied stage schema to Ollama using `format`, while preserving raw content.
- `staged_harness.py retry-payload`: repeats the complete original context and diagnostics without blindly embedding previous raw output.

## Semantic diff

| Cambio | Clasificación |
|---|---|
| One JSON object / no Markdown / no extra prose | SERIALIZATION CLARIFICATION |
| Exact `decision_id`, required fields and N3-P enum | STRUCTURAL ENFORCEMENT already present in v1.1 |
| Ollama `format` and parse/reject boundary | STRUCTURAL ENFORCEMENT |
| Retry diagnostics without automatic output replay | RETRY/HARNESS ERGONOMICS |
| Musical semantics, choices, preferences, ranking or knowledge | 0 semantic changes |

No new musical values, options, rules, evidence or preferences were introduced.
