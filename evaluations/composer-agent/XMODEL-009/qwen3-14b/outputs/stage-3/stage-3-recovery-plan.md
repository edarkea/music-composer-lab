# XMODEL-009 — recuperación técnica propuesta para Stage 3 Qwen

Estado: PROPUESTA_NO_EJECUTADA

El intento 2 original queda cerrado como fallo de transporte. No se repite el intento 2 y no se inicia el intento 3 en esta revisión.

## Evidencia

Ollama registró el `POST /api/chat` en `C:/Users/Steeven/AppData/Local/Ollama/server.log` con HTTP 500 y duración exacta de `1h0m0s`, aproximadamente de 15:29:02 a 16:29:02 hora local. La tarea `4729` fue cancelada y el slot terminó con `n_tokens=16953`, `truncated=0`. No existe respuesta final recuperable.

El modelo cargado después del timeout solo demuestra que el proceso permaneció cargado; no demuestra finalización de la generación.

## Por qué ocurrió

`staged_runner.py` usa `urlopen(..., timeout=3600)` con `stream:false` y después ejecuta `response.read()`. El timeout de urllib es un límite de conexión/operación de socket, no una garantía de captura progresiva ni una medición semántica de generación completa. Como Ollama no entrega un cuerpo utilizable hasta completar la respuesta no streaming, el cliente esperó una hora sin poder guardar fragmentos. El log muestra generación prolongada y cancelación al terminar ese intervalo.

El contexto de 32768, el prompt grande, el procesamiento de contexto, el offload CPU/GPU y la tasa de generación observada pueden explicar la duración. El log no permite atribuir el retraso a una sola de esas causas.

Aumentar solamente 3600 segundos no resuelve la pérdida de observabilidad y no debe hacerse sin una decisión de protocolo.

## Recuperación mínima segura

Si el Owner autoriza una solicitud técnica posterior, debe:

- usar un directorio nuevo, por ejemplo `outputs/stage-3/recovery-001/`, nunca `attempt-2` ni `attempt-3`;
- reutilizar byte por byte `attempt-2/retry-input.txt` y verificar el hash `f06cda45cc4945a6170baf179b6f421402256019a915878b8817942399e0664a`;
- conservar `qwen3:14b`, seed, temperatura, top-p, top-k, repeat penalty, `num_ctx`, `num_predict`, esquema y brief;
- registrar que es una nueva solicitud después de una desconexión, no una continuación exacta de la generación interrumpida;
- escribir capturas con creación exclusiva y guardar request, respuesta, tiempos, estado HTTP y motivo de terminación;
- mantener este registro de fallo sin modificarlo.

La recuperación debe ser una nueva captura técnica y no debe alterar el prompt ni aportar soluciones musicales.

## Mejoras del runner aplicadas antes de usar esa recuperación

1. `staged_runner.py` acepta `--http-timeout`, registra el valor efectivo y mide el tiempo monotónico.
2. El runner registra explícitamente `TIMEOUT`, `CONNECTION_FAILURE`, `HTTP_ERROR`, `INTERRUPTED_OR_INCOMPLETE`, `INCOMPLETE_RESPONSE` e `INVALID_API_RESPONSE`; ninguno recibe `CAPTURED`.
3. Las respuestas parciales disponibles se conservan como `raw-api-response.partial.json`; las capturas completas siguen usando escritura exclusiva.
4. `--request-id` permite identificar la recuperación sin reutilizar silenciosamente la identidad experimental.
5. El modo streaming no está implementado todavía. Ollama puede ofrecer streaming, pero habilitarlo requiere una prueba específica de reconstrucción de eventos; esta recuperación usa deliberadamente el transporte no streaming con timeout ampliado.

Estas mejoras son técnicas: no cambian el prompt, la semántica musical, los parámetros de generación ni la comparación del modelo. Aun así, una solicitud posterior no es una continuación exacta del intento 2 y debe analizarse como recuperación separada.
