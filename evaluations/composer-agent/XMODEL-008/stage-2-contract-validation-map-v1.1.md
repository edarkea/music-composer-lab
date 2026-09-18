# Stage 2 contract validation map

Cada comprobaci?n es estructural y procede del contrato congelado `stage-2-musical-material-schema.yaml`. No se a?aden decisiones musicales.

| Requisito del contrato | Comprobaci?n ejecutable | Fuente |
|---|---|---|
| `required` root fields | presencia de `$.frozen_decision_trace_hash`, `$.sections`, `$.layers`, `$.material_events`, `$.realization_notes` | `stage-2-musical-material-schema.yaml:required` |
| section required fields | presencia y tipos b?sicos de `$.sections[i].section_id`, `start_bar`, `bar_count`, `decision_references` | `sections.required_fields` |
| layer allowed types | `$.layers[i].type` pertenece a `pitched`, `drums`, `percussion`, `effect`, `texture` | `layers.allowed_types` |
| layer required fields | presencia de `layer_id`, `type`, `role`, `section_assignments` | `layers.required_fields` |
| section assignments | `section_assignments` es array cuando est? presente | `material_events.section_assignments_required` |
| event container | `material_events` es objeto o array; no se infiere contenido musical | `material_events` |
| consistency hash | compara `frozen_decision_trace_hash` con traza aceptada cuando se suministra | `consistency.decision_trace_hash_required` |

No se activa Ollama `format` para Stage 2 porque el contrato disponible es YAML descriptivo y no un JSON Schema autoritativo.
