# Recovery command prepared only; do not execute automatically.
$root = (Get-Location).Path
$x = Join-Path $root 'evaluations/composer-agent/XMODEL-009'
$q = Join-Path $x 'qwen3-14b'
$brief = Join-Path $x 'brief.yaml'
$s3instruction = Join-Path $x 'stage-3-prompt-reconciled-v1.1.txt'
$s3schema = Join-Path $x 'stage-3-songplan-format-schema-v1.1.json'
python integrations/composer-agent/staged_runner.py `
  --model qwen3:14b `
  --stage stage-3 `
  --attempt 2 `
  --request-id XMODEL-009-QWEN-STAGE3-RECOVERY-001 `
  --input (Join-Path $q 'outputs/stage-3/attempt-2/retry-input.txt') `
  --brief $brief `
  --stage-number 3 `
  --instruction $s3instruction `
  --prior (Join-Path $q 'outputs/stage-2/accepted-output.json') `
  --format-schema $s3schema `
  --required-record $s3schema `
  --output-dir (Join-Path $q 'outputs/stage-3/recovery-001/capture') `
  --num-predict 8192 `
  --http-timeout 7200
