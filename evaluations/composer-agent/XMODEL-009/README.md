# XMODEL-009

**Estado: PREPARED_NOT_EXECUTED**

XMODEL-009 es un nuevo test prospectivo de transferencia end-to-end. No es una
continuación numérica de la evidencia inválida de XMODEL-004 ni modifica los
resultados históricos de XMODEL-008.

Usa el mismo brief artístico congelado que XMODEL-005–008, Interface v1.1,
Composer Knowledge y genre pack sin cambios. Qwen y Ministral reciben las
mismas condiciones, parámetros, contratos y capacidad host.

La aceptación requiere que Stage 1 y Stage 2 pasen sus gates, que Stage 3
produzca un único JSON sin claves duplicadas, y que el parser/validator real de
music-engine 4.0.0 y la configuración host pasen. No se genera MIDI durante el
test de transferencia.

Stage 2 mantiene deliberadamente la ausencia de Ollama `format`: el contrato
descriptivo existente no se convierte en un schema musical nuevo. El gate raw
JSON, los diagnósticos deterministas y los reintentos permiten medir si
Ministral repite su anterior fallo de serialización bajo condiciones idénticas.

**N3-P permanece completamente autónomo.** El host solo declara recursos de
materialización; no selecciona FULL, MINIMAL, DELEGATED ni INTENTIONALLY_ABSENT.
