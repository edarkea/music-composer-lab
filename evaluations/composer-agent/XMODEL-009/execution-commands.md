# XMODEL-009 execution commands

These commands are prepared only. Do not run them as part of preparation.
Execute a later stage only after the previous stage has passed its gate. Run
the same command structure for both models; only the model and model directory
change.

```powershell
$root = (Get-Location).Path
$base = Join-Path $root "evaluations/composer-agent/XMODEL-009"
$brief = Join-Path $base "brief.yaml"
$s1instruction = Join-Path $base "frozen-prompt-stage-1-n3-canonical.txt"
$s1schema = Join-Path $base "stage-1-output-schema-v1.1-n3-canonical.json"
$s2instruction = Join-Path $base "stage-2-prompt-hardened-v1.1.txt"
$s2map = Join-Path $base "stage-2-contract-validation-map-v1.1.md"
$s3instruction = Join-Path $base "stage-3-prompt-reconciled-v1.1.txt"
$s3schema = Join-Path $base "stage-3-songplan-format-schema-v1.1.json"
$host = Join-Path $base "host-config.yaml"
```

## Qwen

```powershell
$model = "qwen3:14b"
$q = Join-Path $base "qwen3-14b"
python integrations/composer-agent/staged_harness.py assemble --stage 1 --brief $brief --instruction $s1instruction --out "$q/stage-1-payload.txt"
python integrations/composer-agent/staged_runner.py --model $model --stage stage-1 --attempt 1 --input "$q/stage-1-payload.txt" --brief $brief --stage-number 1 --instruction $s1instruction --format-schema $s1schema --required-record $s1schema --output-dir "$q/outputs/stage-1/attempt-1" --num-predict 4096
python integrations/composer-agent/staged_harness.py gate --stage 1 --output "$q/outputs/stage-1/attempt-1/raw-output.txt"
```

For attempts 2 and 3, use `retry-payload` with every diagnostic returned by
the gate, then resend the complete retry payload with the corresponding
attempt number. Do not add musical suggestions. After Stage 1 PASS, preserve
the accepted output as `accepted-output.json` and continue:

```powershell
python integrations/composer-agent/staged_harness.py assemble --stage 2 --brief $brief --instruction $s2instruction --prior "$q/outputs/stage-1/accepted-output.json" --extra-record $s2map --out "$q/stage-2-payload.txt"
python integrations/composer-agent/staged_runner.py --model $model --stage stage-2 --attempt 1 --input "$q/stage-2-payload.txt" --brief $brief --stage-number 2 --instruction $s2instruction --prior "$q/outputs/stage-1/accepted-output.json" --required-record $s2map --output-dir "$q/outputs/stage-2/attempt-1" --num-predict 8192
python integrations/composer-agent/staged_harness.py gate --stage 2 --output "$q/outputs/stage-2/attempt-1/raw-output.txt"
```

After Stage 2 PASS, preserve `accepted-output.json` and run Stage 3:

```powershell
python integrations/composer-agent/staged_harness.py assemble --stage 3 --brief $brief --instruction $s3instruction --prior "$q/outputs/stage-2/accepted-output.json" --extra-record $s3schema --out "$q/stage-3-payload.txt"
python integrations/composer-agent/staged_runner.py --model $model --stage stage-3 --attempt 1 --input "$q/stage-3-payload.txt" --brief $brief --stage-number 3 --instruction $s3instruction --prior "$q/outputs/stage-2/accepted-output.json" --format-schema $s3schema --required-record $s3schema --output-dir "$q/outputs/stage-3/attempt-1" --num-predict 8192
python integrations/composer-agent/staged_harness.py gate --stage 3 --host-config $host --output "$q/outputs/stage-3/attempt-1/raw-output.txt"
```

## Ministral

Repeat the same commands with:

```powershell
$model = "ministral-3:14b"
$q = Join-Path $base "ministral-3-14b"
```

The Stage 2 command intentionally omits `--format-schema` for both models.
This preserves comparability and measures the known Ministral serialization
risk without adapter repair.

## Retry rule

Every retry must use:

```powershell
python integrations/composer-agent/staged_harness.py retry-payload --original <original-payload> --out <retry-input> --diagnostic "<exact gate diagnostic>"
```

Maximum attempts: 3 per stage. A failed gate blocks later stages. A Stage 3
local PASS is insufficient unless the real engine and host configuration also
return PASS.
