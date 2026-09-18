# XMODEL-008 execution commands (DO NOT RUN during preparation)

PowerShell desde la ra?z del repositorio. Ejecutar cada etapa ?nicamente despu?s del `gate` PASS de la etapa anterior. Los valores `<diagn?stico exacto del gate>` deben copiarse literalmente; no se deben a?adir soluciones musicales.

```powershell
$root = (Get-Location).Path
$base = Join-Path $root "evaluations/composer-agent/XMODEL-008"
$brief = Join-Path $base "brief.yaml"
$s1schema = Join-Path $base "stage-1-output-schema-v1.1-n3-canonical.json"
$s1instruction = Join-Path $base "frozen-prompt-stage-1-n3-canonical.txt"
$s2instruction = Join-Path $base "stage-2-prompt-hardened-v1.1.txt"
$s3instruction = Join-Path $base "stage-3-prompt-hardened-v1.1.txt"
$s3schema = Join-Path $base "stage-3-songplan-format-schema-v1.1.json"
$s2map = Join-Path $base "stage-2-contract-validation-map-v1.1.md"

# ================= QWEN =================
$q = Join-Path $base "qwen3-14b"
python integrations/composer-agent/staged_runner.py --model qwen3:14b --stage stage-1 --attempt 1 --input "$q/stage-1-payload.txt" --brief $brief --stage-number 1 --instruction $s1instruction --format-schema $s1schema --required-record $s1schema --output-dir "$q/outputs/stage-1/attempt-1" --num-predict 4096
python integrations/composer-agent/staged_harness.py gate --stage 1 --output "$q/outputs/stage-1/attempt-1/raw-output.txt"

# Qwen Stage 1 retry 2 y 3: repetir este bloque con attempt-2 y attempt-3.
python integrations/composer-agent/staged_harness.py retry-payload --original "$q/stage-1-payload.txt" --out "$q/outputs/stage-1/attempt-2/retry-input.txt" --diagnostic "<diagn?stico exacto del gate>"
python integrations/composer-agent/staged_runner.py --model qwen3:14b --stage stage-1 --attempt 2 --input "$q/outputs/stage-1/attempt-2/retry-input.txt" --brief $brief --stage-number 1 --instruction $s1instruction --format-schema $s1schema --required-record $s1schema --output-dir "$q/outputs/stage-1/attempt-2" --num-predict 4096
python integrations/composer-agent/staged_harness.py gate --stage 1 --output "$q/outputs/stage-1/attempt-2/raw-output.txt"

# Qwen Stage 2, solo con Stage 1 PASS.
python integrations/composer-agent/staged_harness.py assemble --stage 2 --brief $brief --instruction $s2instruction --prior "$q/outputs/stage-1/accepted-output.json" --extra-record $s2map --out "$q/stage-2-payload.txt"
python integrations/composer-agent/staged_runner.py --model qwen3:14b --stage stage-2 --attempt 1 --input "$q/stage-2-payload.txt" --brief $brief --stage-number 2 --instruction $s2instruction --prior "$q/outputs/stage-1/accepted-output.json" --required-record $s2map --output-dir "$q/outputs/stage-2/attempt-1" --num-predict 8192
python integrations/composer-agent/staged_harness.py gate --stage 2 --output "$q/outputs/stage-2/attempt-1/raw-output.txt"
# Stage 2 retry 2/3 usa retry-payload con cada diagn?stico exacto y --attempt 2/3.

# Qwen Stage 3, solo con Stage 2 PASS.
python integrations/composer-agent/staged_harness.py assemble --stage 3 --brief $brief --instruction $s3instruction --prior "$q/outputs/stage-2/accepted-output.json" --extra-record $s3schema --out "$q/stage-3-payload.txt"
python integrations/composer-agent/staged_runner.py --model qwen3:14b --stage stage-3 --attempt 1 --input "$q/stage-3-payload.txt" --brief $brief --stage-number 3 --instruction $s3instruction --prior "$q/outputs/stage-2/accepted-output.json" --format-schema $s3schema --required-record $s3schema --output-dir "$q/outputs/stage-3/attempt-1" --num-predict 8192
python integrations/composer-agent/staged_harness.py gate --stage 3 --output "$q/outputs/stage-3/attempt-1/raw-output.txt"
# Stage 3 retry 2/3 usa retry-payload con cada diagn?stico exacto y --attempt 2/3.

# ================= MINISTRAL =================
$m = Join-Path $base "ministral-3-14b"
python integrations/composer-agent/staged_runner.py --model ministral-3:14b --stage stage-1 --attempt 1 --input "$m/stage-1-payload.txt" --brief $brief --stage-number 1 --instruction $s1instruction --format-schema $s1schema --required-record $s1schema --output-dir "$m/outputs/stage-1/attempt-1" --num-predict 4096
python integrations/composer-agent/staged_harness.py gate --stage 1 --output "$m/outputs/stage-1/attempt-1/raw-output.txt"

# Ministral Stage 1 retry 2/3: mismo flujo, sustituyendo la ruta de intento y el n?mero.
python integrations/composer-agent/staged_harness.py retry-payload --original "$m/stage-1-payload.txt" --out "$m/outputs/stage-1/attempt-2/retry-input.txt" --diagnostic "<diagn?stico exacto del gate>"
python integrations/composer-agent/staged_runner.py --model ministral-3:14b --stage stage-1 --attempt 2 --input "$m/outputs/stage-1/attempt-2/retry-input.txt" --brief $brief --stage-number 1 --instruction $s1instruction --format-schema $s1schema --required-record $s1schema --output-dir "$m/outputs/stage-1/attempt-2" --num-predict 4096
python integrations/composer-agent/staged_harness.py gate --stage 1 --output "$m/outputs/stage-1/attempt-2/raw-output.txt"

# Ministral Stage 2, solo con Stage 1 PASS.
python integrations/composer-agent/staged_harness.py assemble --stage 2 --brief $brief --instruction $s2instruction --prior "$m/outputs/stage-1/accepted-output.json" --extra-record $s2map --out "$m/stage-2-payload.txt"
python integrations/composer-agent/staged_runner.py --model ministral-3:14b --stage stage-2 --attempt 1 --input "$m/stage-2-payload.txt" --brief $brief --stage-number 2 --instruction $s2instruction --prior "$m/outputs/stage-1/accepted-output.json" --required-record $s2map --output-dir "$m/outputs/stage-2/attempt-1" --num-predict 8192
python integrations/composer-agent/staged_harness.py gate --stage 2 --output "$m/outputs/stage-2/attempt-1/raw-output.txt"
# Stage 2 retry 2/3 usa retry-payload con cada diagn?stico exacto.

# Ministral Stage 3, solo con Stage 2 PASS.
python integrations/composer-agent/staged_harness.py assemble --stage 3 --brief $brief --instruction $s3instruction --prior "$m/outputs/stage-2/accepted-output.json" --extra-record $s3schema --out "$m/stage-3-payload.txt"
python integrations/composer-agent/staged_runner.py --model ministral-3:14b --stage stage-3 --attempt 1 --input "$m/stage-3-payload.txt" --brief $brief --stage-number 3 --instruction $s3instruction --prior "$m/outputs/stage-2/accepted-output.json" --format-schema $s3schema --required-record $s3schema --output-dir "$m/outputs/stage-3/attempt-1" --num-predict 8192
python integrations/composer-agent/staged_harness.py gate --stage 3 --output "$m/outputs/stage-3/attempt-1/raw-output.txt"
# Stage 3 retry 2/3 usa retry-payload con cada diagn?stico exacto.
```

## Retry command templates

Para cada intento fallido, primero ejecutar `gate`, copiar todos sus diagn?sticos literalmente y construir el payload completo:

```powershell
# Ejemplo Qwen Stage 2 attempt 2; cambiar 2 por 3 para el tercer intento.
python integrations/composer-agent/staged_harness.py retry-payload --original "$q/stage-2-payload.txt" --out "$q/outputs/stage-2/attempt-2/retry-input.txt" --diagnostic "<diagn?stico exacto del gate>"
python integrations/composer-agent/staged_runner.py --model qwen3:14b --stage stage-2 --attempt 2 --input "$q/outputs/stage-2/attempt-2/retry-input.txt" --brief $brief --stage-number 2 --instruction $s2instruction --prior "$q/outputs/stage-1/accepted-output.json" --required-record $s2map --output-dir "$q/outputs/stage-2/attempt-2" --num-predict 8192
python integrations/composer-agent/staged_harness.py gate --stage 2 --output "$q/outputs/stage-2/attempt-2/raw-output.txt"

# Ejemplo Qwen Stage 3 attempt 2; cambiar 2 por 3 para el tercer intento.
python integrations/composer-agent/staged_harness.py retry-payload --original "$q/stage-3-payload.txt" --out "$q/outputs/stage-3/attempt-2/retry-input.txt" --diagnostic "<diagn?stico exacto del gate>"
python integrations/composer-agent/staged_runner.py --model qwen3:14b --stage stage-3 --attempt 2 --input "$q/outputs/stage-3/attempt-2/retry-input.txt" --brief $brief --stage-number 3 --instruction $s3instruction --prior "$q/outputs/stage-2/accepted-output.json" --format-schema $s3schema --required-record $s3schema --output-dir "$q/outputs/stage-3/attempt-2" --num-predict 8192
python integrations/composer-agent/staged_harness.py gate --stage 3 --output "$q/outputs/stage-3/attempt-2/raw-output.txt"

# Ministral Stage 2 attempt 2; cambiar 2 por 3 para el tercer intento.
python integrations/composer-agent/staged_harness.py retry-payload --original "$m/stage-2-payload.txt" --out "$m/outputs/stage-2/attempt-2/retry-input.txt" --diagnostic "<diagn?stico exacto del gate>"
python integrations/composer-agent/staged_runner.py --model ministral-3:14b --stage stage-2 --attempt 2 --input "$m/outputs/stage-2/attempt-2/retry-input.txt" --brief $brief --stage-number 2 --instruction $s2instruction --prior "$m/outputs/stage-1/accepted-output.json" --required-record $s2map --output-dir "$m/outputs/stage-2/attempt-2" --num-predict 8192
python integrations/composer-agent/staged_harness.py gate --stage 2 --output "$m/outputs/stage-2/attempt-2/raw-output.txt"

# Ministral Stage 3 attempt 2; cambiar 2 por 3 para el tercer intento.
python integrations/composer-agent/staged_harness.py retry-payload --original "$m/stage-3-payload.txt" --out "$m/outputs/stage-3/attempt-2/retry-input.txt" --diagnostic "<diagn?stico exacto del gate>"
python integrations/composer-agent/staged_runner.py --model ministral-3:14b --stage stage-3 --attempt 2 --input "$m/outputs/stage-3/attempt-2/retry-input.txt" --brief $brief --stage-number 3 --instruction $s3instruction --prior "$m/outputs/stage-2/accepted-output.json" --format-schema $s3schema --required-record $s3schema --output-dir "$m/outputs/stage-3/attempt-2" --num-predict 8192
python integrations/composer-agent/staged_harness.py gate --stage 3 --output "$m/outputs/stage-3/attempt-2/raw-output.txt"
```

No ejecutar music-engine autom?ticamente despu?s de Stage 3 PASS. La materializaci?n requiere revisi?n y autorizaci?n separadas.
