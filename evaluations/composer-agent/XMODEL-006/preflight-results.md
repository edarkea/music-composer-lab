# XMODEL-006 — Preflight

Estado: `PREPARED_NOT_EXECUTED`; no se invocaron modelos.

- Brief exacto: PASS; hash `464AE4378BCB7236F0FB36DA52EB65DCB03735197284E3A6899B8686D51EDE0B`, igual a XMODEL-005.
- Registros v1.1 requeridos: PASS; se ensamblan como contenido, no como rutas.
- Genre pack y N3-P: PASS; incluidos en Stage 1.
- NO-EXAMPLE: PASS; el preflight rechaza marcadores SONG-001..004.
- Prompt aclarado: PASS; texto literal sin Markdown, fences, prose ni múltiples objetos.
- Esquema endurecido: PASS; JSON válido y disponible.
- Ollama `format`: PASS en comandos preparados; `staged_runner.py --format-schema` transmite el esquema sin reparación.
- Condiciones simétricas: PASS; mismos parámetros salvo identificador del modelo.
- `num_predict` Stage 1: 4096; Stage 2/3: 8192.
- Decisiones musicales del adaptador: 0.
- XMODEL-005: sin modificaciones.

La asamblea Stage 1 se ejecutará para cada modelo con `staged_harness.py assemble --extra-record ...`; su `payload-manifest.json` será evidencia del texto exacto transmitido. Los gates de Stage 2/3 permanecen sin hardening proactivo.

## Comparabilidad

XMODEL-006 es una prueba nueva. Con XMODEL-005 solo son comparables PASS/FAIL de Stage 1, serialización y satisfacción de requisitos estructurales. La condición técnica cambió deliberadamente; no se atribuirá cualquier mejora a razonamiento musical. XMODEL-004 sigue siendo inválido y no comparable.
