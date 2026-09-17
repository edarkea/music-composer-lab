# XMODEL-006 — Stage 1 hardened prospective test

Estado: `PREPARED_NOT_EXECUTED`.

XMODEL-006 es una prueba prospectiva nueva. No es continuación de evidencia válida de XMODEL-004 (inválido) y no es byte-identical a XMODEL-005. Conserva la semántica de `composer-interface-v1.1`, pero cambia deliberadamente la condición técnica de Stage 1: esquema JSON específico transmitido mediante Ollama `format`, prompt de serialización literal y gates deterministas.

Modelos simétricos: `qwen3:14b` y `ministral-3:14b`. Condición: NO-EXAMPLE. No se ejecuta Stage 2 hasta que Stage 1 pase; no se materializa MIDI.
