# XMODEL-003 — Preparación de control de presupuesto

Estado: preparado, no ejecutado. La única variable de generación que cambia
frente a XMODEL-002 es `num_predict`: 8192 → 12288 para ambos modelos. No se
autoriza ni se ha hecho ninguna llamada a los modelos durante esta preparación.

El brief, prompt congelado, schema estructurado y hash de los componentes v1.1
están registrados en `run-manifest.yaml`. Los directorios por modelo están
reservados para capturas inmutables; `ollama_runner.py` crea los archivos de
captura en modo exclusivo.

Ejecutar ambas corridas con el mismo comando y parámetros, cambiando solo el
identificador y directorio de salida:

```powershell
python integrations/composer-agent/ollama_runner.py `
  --model qwen3:14b `
  --input evaluations/composer-agent/XMODEL-003/frozen-prompt.txt `
  --brief evaluations/composer-agent/XMODEL-003/brief.yaml `
  --schema evaluations/composer-agent/XMODEL-003/structured-output-schema.json `
  --num-predict 12288 `
  --output-dir evaluations/composer-agent/XMODEL-003/qwen3-14b
```
