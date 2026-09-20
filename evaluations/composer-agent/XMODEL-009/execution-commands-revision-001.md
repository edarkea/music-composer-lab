# XMODEL-009 — ejecución Stage 1, revision-001

No ejecutar todavía sin aprobar esta revisión. Estos comandos son los únicos comandos actualizados para Stage 1; los comandos originales permanecen preservados en `execution-commands.md`.

```powershell
$root = (Get-Location).Path
$x = Join-Path $root "evaluations/composer-agent/XMODEL-009"
$brief = Join-Path $x "brief.yaml"
$s1instruction = Join-Path $x "frozen-prompt-stage-1-n3-canonical.txt"
$s1schema = Join-Path $x "stage-1-output-schema-v1.1-n3-canonical.json"
$hostcaps = Join-Path $x "model-visible-host-capabilities.md"

# Qwen
$q = Join-Path $x "qwen3-14b/revision-001"
python integrations/composer-agent/staged_runner.py `
  --model qwen3:14b `
  --stage stage-1 `
  --attempt 1 `
  --input (Join-Path $q "stage-1-payload.txt") `
  --brief $brief `
  --stage-number 1 `
  --instruction $s1instruction `
  --format-schema $s1schema `
  --required-record $s1schema `
  --required-record $hostcaps `
  --output-dir (Join-Path $q "outputs/stage-1/attempt-1") `
  --num-predict 4096

# Ministral (misma condición y mismos registros)
$m = Join-Path $x "ministral-3-14b/revision-001"
python integrations/composer-agent/staged_runner.py `
  --model ministral-3:14b `
  --stage stage-1 `
  --attempt 1 `
  --input (Join-Path $m "stage-1-payload.txt") `
  --brief $brief `
  --stage-number 1 `
  --instruction $s1instruction `
  --format-schema $s1schema `
  --required-record $s1schema `
  --required-record $hostcaps `
  --output-dir (Join-Path $m "outputs/stage-1/attempt-1") `
  --num-predict 4096
```

La revisión usa directorios nuevos y el runner escribe exclusivamente con creación exclusiva; no reutiliza ni sobrescribe capturas.
