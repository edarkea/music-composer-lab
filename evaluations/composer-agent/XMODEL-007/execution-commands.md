# Comandos de ejecuci?n (no ejecutar durante la preparaci?n)

PowerShell desde la ra?z del repositorio:

```powershell
$root = (Get-Location).Path
$base = Join-Path $root "evaluations/composer-agent/XMODEL-007"
$brief = Join-Path $base "brief.yaml"
$schema = Join-Path $base "stage-1-output-schema-v1.1-n3-canonical.json"
$instruction = Join-Path $base "frozen-prompt-stage-1-n3-canonical.txt"

# Qwen Stage 1 attempt 1
python integrations/composer-agent/staged_runner.py --model qwen3:14b --stage stage-1 --attempt 1 --input "$base/qwen3-14b/stage-1-payload.txt" --brief $brief --stage-number 1 --instruction $instruction --format-schema $schema --required-record $schema --output-dir "$base/qwen3-14b/outputs/stage-1/attempt-1" --num-predict 4096
python integrations/composer-agent/staged_harness.py gate --stage 1 --output "$base/qwen3-14b/outputs/stage-1/attempt-1/raw-output.txt"

# Qwen retry attempt 2 (usar cada error literal devuelto por gate):
python integrations/composer-agent/staged_harness.py retry-payload --original "$base/qwen3-14b/stage-1-payload.txt" --out "$base/qwen3-14b/outputs/stage-1/attempt-2/retry-input.txt" --diagnostic "<diagn?stico exacto del gate>"
python integrations/composer-agent/staged_runner.py --model qwen3:14b --stage stage-1 --attempt 2 --input "$base/qwen3-14b/outputs/stage-1/attempt-2/retry-input.txt" --brief $brief --stage-number 1 --instruction $instruction --format-schema $schema --required-record $schema --output-dir "$base/qwen3-14b/outputs/stage-1/attempt-2" --num-predict 4096
python integrations/composer-agent/staged_harness.py gate --stage 1 --output "$base/qwen3-14b/outputs/stage-1/attempt-2/raw-output.txt"
# Repetir el mismo bloque para attempt-3, sin a?adir soluciones musicales.

# Stage 2 solo despu?s de un gate Stage 1 PASS; primero ensamblar su payload con la salida aceptada:
python integrations/composer-agent/staged_harness.py assemble --stage 2 --brief $brief --instruction "$base/frozen-prompt-stage-2.txt" --prior "$base/qwen3-14b/outputs/stage-1/accepted-output.json" --out "$base/qwen3-14b/stage-2-payload.txt"
python integrations/composer-agent/staged_runner.py --model qwen3:14b --stage stage-2 --attempt 1 --input "$base/qwen3-14b/stage-2-payload.txt" --brief $brief --stage-number 2 --instruction "$base/frozen-prompt-stage-2.txt" --prior "$base/qwen3-14b/outputs/stage-1/accepted-output.json" --output-dir "$base/qwen3-14b/outputs/stage-2/attempt-1" --num-predict 8192

# Ministral: repetir exactamente el flujo anterior sustituyendo qwen3:14b y qwen3-14b por ministral-3:14b y ministral-3-14b.
```

Estos comandos son informativos y no constituyen autorizaci?n de ejecuci?n.
