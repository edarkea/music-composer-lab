# N3-P Stage 1 structural correction

Historical XMODEL-005 and XMODEL-006 artifacts remain unchanged. This is a new technical candidate; it is not Interface v1.2 and does not create XMODEL-007.

## Canonical path

```text
decision_trace[i].decision_id = N3-P_PERCUSSION_ARCHITECTURE
decision_trace[i].selected_outcome
decision_trace[i].candidate_strategies
decision_trace[i].bass_groove_interaction
decision_trace[i].focal_hierarchy_interaction
decision_trace[i].section_behavior
decision_trace[i].development_behavior
```

All six fields are direct siblings of `decision_id`. `selected_option` is removed from the N3-P variant. Generic decisions may retain `selected_option`; N3-P may not contain it and may not duplicate the six fields below it.

## Semantic diff against XMODEL-006

| Cambio | Clasificación |
|---|---|
| Explicit N3-P sibling path | STRUCTURAL CLARIFICATION |
| Dedicated N3-P schema variant with direct required fields | SCHEMA ENFORCEMENT |
| Gate emits expected/found path diagnostic | GATE ALIGNMENT + RETRY DIAGNOSTIC |
| Literal prompt wording | STRUCTURAL CLARIFICATION |
| Musical values, N3-P outcomes, roles, knowledge and preferences | SEMANTIC CHANGE: 0 |
