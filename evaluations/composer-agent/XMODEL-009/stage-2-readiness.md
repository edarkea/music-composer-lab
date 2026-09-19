# Stage 2 readiness

Estado local: **READY**.

- El gate exige un único JSON raw, sin Markdown, prose ni múltiples objetos.
- Las claves duplicadas se rechazan antes del parseo.
- Los reintentos reenvían el contexto completo y solo añaden diagnósticos.
- No se usa Ollama `format` en Stage 2 porque el contrato congelado es YAML
  descriptivo; derivar un JSON Schema nuevo podría introducir restricciones
  musicales no aprobadas.

Riesgo conocido: Ministral puede repetir el fallo de Markdown/truncamiento
observado previamente. Esa repetición sería evidencia prospectiva sobre el
cumplimiento de serialización bajo condiciones idénticas, no una reparación del
adaptador. Qwen y Ministral mantienen exactamente la misma condición Stage 2.
