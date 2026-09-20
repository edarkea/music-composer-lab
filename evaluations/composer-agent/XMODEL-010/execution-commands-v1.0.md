# XMODEL-010: Comandos preparados (NO EJECUTADOS)

Todos los ejemplos son PowerShell desde la raiz. Ejecutaran solo Qwen. No se ejecutaron durante el preflight.

## Stage 1: primer request

```powershell
$root = (Get-Location).Path
$x = Join-Path $root 'evaluations/composer-agent/XMODEL-010'
$q = Join-Path $x 'outputs/qwen3-14b'
$brief = Join-Path $x 'brief.yaml'
$s1 = Join-Path $x 'stage-1-prompt-v1.2.txt'
$s1schema = Join-Path $x 'stage-1-output-schema-v1.1-n3-canonical.json'
$hostcaps = Join-Path $x 'model-visible-host-capabilities.md'
python integrations/composer-agent/staged_runner.py `
  --experiment-id XMODEL-010 --request-kind evaluable_attempt --request-id XMODEL-010-QWEN-STAGE1-A1 `
  --request-registry (Join-Path $q 'request-registry') `
  --model qwen3:14b --stage stage-1 --attempt 1 `
  --input (Join-Path $q 'stage-1-payload.txt') --brief $brief --stage-number 1 --instruction $s1 `
  --format-schema $s1schema --required-record $s1schema --required-record $hostcaps `
  --output-dir (Join-Path $q 'captures/stage-1/attempt-1') `
  --num-predict 4096 --http-timeout 7200
```

Solo despus de `CAPTURED` se ejecuta `python integrations/composer-agent/staged_harness.py gate --stage 1 --output (Join-Path $q 'captures/stage-1/attempt-1/raw-output.txt')`. Stage 1 PASS permite una copia exclusiva a `outputs/stage-1/accepted-output.json`; cualquier FAIL bloquea Stage 2.

## Stage 2: preparar despus de Stage 1 PASS

```powershell
$s2 = Join-Path $x 'stage-2-prompt-v1.2.txt'
$s2map = Join-Path $x 'stage-2-contract-validation-map-v1.1.md'
$s2format = Join-Path $x 'stage-2-json-object-format-v1.0.json'
$s2prior = Join-Path $q 'outputs/stage-1/accepted-output.json'
python integrations/composer-agent/staged_harness.py assemble --stage 2 --brief $brief --instruction $s2 --prior $s2prior --extra-record $s2map --extra-record $s2format --out (Join-Path $q 'stage-2-payload.txt')
python integrations/composer-agent/staged_runner.py --experiment-id XMODEL-010 --request-kind evaluable_attempt --request-id XMODEL-010-QWEN-STAGE2-A1 --request-registry (Join-Path $q 'request-registry') --model qwen3:14b --stage stage-2 --attempt 1 --input (Join-Path $q 'stage-2-payload.txt') --brief $brief --stage-number 2 --instruction $s2 --prior $s2prior --format-schema $s2format --required-record $s2map --required-record $s2format --output-dir (Join-Path $q 'captures/stage-2/attempt-1') --num-predict 8192 --http-timeout 7200
```

Stage 2 format schema solo dice `type: object`, sin propiedades musicales. Tras gate PASS se guarda accepted output en ruta nueva/exclusiva; luego puede construirse Stage 3.

## Stage 3: preparar despus de Stage 2 PASS

```powershell
$s3 = Join-Path $x 'stage-3-prompt-v1.2.txt'
$s3schema = Join-Path $x 'stage-3-songplan-format-schema-v1.2.json'
$engineSchema = Join-Path $x 'engine-songplan-v2.schema-music-engine-4.0.0.json'
$s3prior = Join-Path $q 'outputs/stage-2/accepted-output.json'
python integrations/composer-agent/staged_harness.py assemble --stage 3 --brief $brief --instruction $s3 --prior $s3prior --extra-record $s3schema --extra-record $engineSchema --out (Join-Path $q 'stage-3-payload.txt')
python integrations/composer-agent/staged_runner.py --experiment-id XMODEL-010 --request-kind evaluable_attempt --request-id XMODEL-010-QWEN-STAGE3-A1 --request-registry (Join-Path $q 'request-registry') --model qwen3:14b --stage stage-3 --attempt 1 --input (Join-Path $q 'stage-3-payload.txt') --brief $brief --stage-number 3 --instruction $s3 --prior $s3prior --format-schema $s3schema --required-record $s3schema --required-record $engineSchema --output-dir (Join-Path $q 'captures/stage-3/attempt-1') --num-predict 8192 --http-timeout 7200
python integrations/composer-agent/staged_harness.py gate --stage 3 --output (Join-Path $q 'captures/stage-3/attempt-1/raw-output.txt') --host-config (Join-Path $x 'host-config.yaml')
```

El gate Stage 3 invoca el parser y validador real music-engine 4.0.0 y host resolution; nunca materializa MIDI. PercussionMap no aprobado significa host FAIL si la composicin tiene eventos percussion no resueltos.

## Retry de validacin

Por intento de validacin 2 o 3: crear `retry-input.txt` con `staged_harness.py retry-payload --original <payload congelado original de etapa> --out <directorio de intento nuevo>/retry-input.txt --diagnostic <cada diagnstico literal>`. Ejecutar runner con el nuevo input, `--attempt` siguiente, request ID unico, output-dir nuevo y los mismos schema/record/prior/parmetros. Siempre ramificar del payload original, nunca del retry anterior. El lmite 3 aplica a intentos evaluables.
