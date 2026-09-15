# Interfaz externa de composición v1.1

`datasets/composer-interface-v1.1/` es una exportación derivada enfocada en los
fallos de transferencia de XMODEL-001. El delta está documentado en
`delta-v1-to-v1.1.md`. No altera la fuente canónica ni los archivos v1.

Para preparar/ejecutar una corrida, XMODEL-002 conserva su propio prompt,
brief y manifiesto. La condición está congelada como NO-EXAMPLE; los ejemplos
SONG-001..004 no se incorporan. No ejecutar XMODEL-002 como parte de la
preparación.

## Captura local con Ollama

El runner usa `POST /api/chat`, `stream: false` y el campo `format` con el JSON
Schema de salida. Ollama documenta esta forma de respuesta estructurada en
[Chat API](https://docs.ollama.com/api/chat) y
[Structured Outputs](https://docs.ollama.com/capabilities/structured-outputs).
La estructura restringe formato; no autoriza al adaptador a completar o reparar
contenido musical. Se conservan la respuesta HTTP cruda y `message.content` en
UTF-8. Los archivos se crean en modo exclusivo.

Ejemplo de invocación (ejecutar solo cuando se decida iniciar la prueba):

```powershell
python integrations/composer-agent/ollama_runner.py `
  --model qwen3:14b `
  --input evaluations/composer-agent/XMODEL-002/frozen-prompt.txt `
  --brief evaluations/composer-agent/XMODEL-002/brief.yaml `
  --output-dir evaluations/composer-agent/XMODEL-002/qwen3-14b
```

El mismo comando y parámetros se usan para el otro modelo, cambiando únicamente
identificador y directorio de salida. Semilla y parámetros iguales controlan la
configuración enviada; no prometen identidad bit a bit entre hardware o
backends. El adaptador captura, no normaliza ni reescribe la respuesta.
Antes de aceptar una salida, se puede pasar por el gate de solo lectura
`integrations/composer-agent/validate_v1_1_output.py`; un incumplimiento se
rechaza, nunca se repara.
