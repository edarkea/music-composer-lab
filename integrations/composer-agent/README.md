# Interfaz para agentes compositores externos

Esta integración entrega el paquete derivado `datasets/composer-interface-v1/` y define un contrato neutral de entrada/salida. El corpus de investigación completo no se necesita para una ejecución normal. Las fuentes canónicas permanecen en `research/`, `genres/`, `decisions/` y `rules/`; una exportación no las reemplaza.

Archivos de contrato:

- `system-contract-v1.md`: instrucciones normativas para el agente externo.
- `input-schema.yaml`: paquete de entrada por ejecución.
- `output-schema.yaml`: traza, handoffs, guardrails y candidato SongPlanV2 requeridos.
- `../../datasets/composer-interface-v1/decision-schema.yaml`: registros de conocimiento/decisión.
- `../../datasets/composer-interface-v1/manifest.yaml`: versión, procedencia y límites.

SongPlanV2 y su validación se rigen por `integrations/music-engine/integration-contract.md`; el validador/runtime exacto debe estar disponible en la evaluación para declarar validez o materializabilidad.

SONG-005 está reservado como primer test prospectivo. Este paquete no define su brief, no compone esa canción y no afirma preparación para fine-tuning.
