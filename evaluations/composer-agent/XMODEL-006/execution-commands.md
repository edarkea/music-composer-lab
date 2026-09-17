# XMODEL-006 — Comandos preparados (NO EJECUTAR DURANTE LA PREPARACIÓN)

Todos los comandos se ejecutan desde `D:\projects\music-composer-lab`. El gate debe devolver `pass: true` antes de preparar la etapa siguiente. Cada retry usa `staged_harness.py retry-payload`, que conserva el payload completo y añade únicamente diagnósticos deterministas; no vuelve a insertar automáticamente la salida cruda previa.

## Qwen Stage 1

```powershell
$root='D:\projects\music-composer-lab'; $base="$root\evaluations\composer-agent\XMODEL-006\qwen3-14b"
python integrations/composer-agent/staged_runner.py `
  --model qwen3:14b --stage stage-1 --attempt 1 `
  --input "$base\stage-1-payload.txt" `
  --brief "$root\evaluations\composer-agent\XMODEL-006\brief.yaml" `
  --stage-number 1 `
  --instruction "$root\evaluations\composer-agent\XMODEL-006\frozen-prompt-stage-1-clarified.txt" `
  --format-schema "$root\evaluations\composer-agent\XMODEL-006\stage-1-output-schema-v1.1-hardened.json" `
  --required-record "$root\evaluations\composer-agent\XMODEL-006\stage-1-output-schema-v1.1-hardened.json" `
  --output-dir "$base\outputs\stage-1\attempt-1" --num-predict 4096
python integrations/composer-agent/staged_harness.py gate --stage 1 --output "$base\outputs\stage-1\attempt-1\raw-output.txt"
```

## Qwen retry workflow

```powershell
python integrations/composer-agent/staged_harness.py retry-payload `
  --original "$base\stage-1-payload.txt" `
  --out "$base\outputs\stage-1\attempt-2\retry-input.txt" `
  --diagnostic 'schema validation failed at /decision_trace' `
  --diagnostic 'return exactly one JSON object; no Markdown or prose'
python integrations/composer-agent/staged_runner.py `
  --model qwen3:14b --stage stage-1 --attempt 2 `
  --input "$base\outputs\stage-1\attempt-2\retry-input.txt" `
  --brief "$root\evaluations\composer-agent\XMODEL-006\brief.yaml" --stage-number 1 `
  --instruction "$root\evaluations\composer-agent\XMODEL-006\frozen-prompt-stage-1-clarified.txt" `
  --format-schema "$root\evaluations\composer-agent\XMODEL-006\stage-1-output-schema-v1.1-hardened.json" `
  --required-record "$root\evaluations\composer-agent\XMODEL-006\stage-1-output-schema-v1.1-hardened.json" `
  --output-dir "$base\outputs\stage-1\attempt-2" --num-predict 4096
python integrations/composer-agent/staged_harness.py gate --stage 1 --output "$base\outputs\stage-1\attempt-2\raw-output.txt"
```

Repetir hasta `attempt-3` cambiando solamente el intento, el diagnóstico exacto y las rutas. No subir `num_predict`.

## Ministral Stage 1

Usar los mismos comandos sustituyendo:

```powershell
$base="$root\evaluations\composer-agent\XMODEL-006\ministral-3-14b"
--model ministral-3:14b
```

El payload, brief, schema, prompt, parámetros y gate son idénticos salvo el identificador del modelo.

## Stage 2 condicional (solo después de Stage 1 PASS)

```powershell
python integrations/composer-agent/staged_harness.py assemble --stage 2 `
  --brief "$root\evaluations\composer-agent\XMODEL-006\brief.yaml" `
  --instruction "$root\evaluations\composer-agent\XMODEL-006\frozen-prompt-stage-2.txt" `
  --prior "$base\outputs\stage-1\attempt-<accepted>\raw-output.txt" `
  --out "$base\stage-2-payload.txt"
python integrations/composer-agent/staged_runner.py `
  --model <model> --stage stage-2 --attempt 1 `
  --input "$base\stage-2-payload.txt" `
  --brief "$root\evaluations\composer-agent\XMODEL-006\brief.yaml" --stage-number 2 `
  --instruction "$root\evaluations\composer-agent\XMODEL-006\frozen-prompt-stage-2.txt" `
  --prior "$base\outputs\stage-1\attempt-<accepted>\raw-output.txt" `
  --output-dir "$base\outputs\stage-2\attempt-1" --num-predict 8192
python integrations/composer-agent/staged_harness.py gate --stage 2 --output "$base\outputs\stage-2\attempt-1\raw-output.txt"
```

Stage 3 y `music-engine` no están autorizados en esta preparación.
