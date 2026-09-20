# XMODEL-009 — Revisión de preflight Stage 1 (revision-001)

Estado: PREPARADO_NO_EJECUTADO

Esta revisión conserva sin cambios el payload original, su hash y el registro del fallo de preflight. No hubo llamada a Ollama ni inferencia de modelo.

## Causa raíz

La preparación anterior ejecutó `preflight` sin pasar los argumentos `--required-record` que usa el runner. El manifiesto anterior marcó PASS para el payload base, pero la ejecución real añadió como registro requerido `stage-1-output-schema-v1.1-n3-canonical.json`; ese registro no estaba embebido en el payload. Además, el payload base tampoco incluía `model-visible-host-capabilities.md`. `--format-schema` entrega un esquema a Ollama, pero no lo convierte en un registro visible dentro del texto transmitido.

## Evidencia preservada

- Payload original Qwen y Ministral: `stage-1-payload.txt`
- Hash original de ambos: `a2f6fa4451d6597a806fb7bf49ee073d1b6ad4b0295e062df610d916a21c472a`
- Registro original: `preflight-results.yaml` y `*/payload-manifest.json`
- Capturas de modelo encontradas: 0

El error del runner (`required record missing from payload: .../stage-1-output-schema-v1.1-n3-canonical.json`) ocurrió antes de `urlopen` en `staged_runner.py`.

## Corrección

Se creó un payload separado en `qwen3-14b/revision-001/` y `ministral-3-14b/revision-001/`. La revisión añade, mediante `--extra-record`, exactamente:

1. `stage-1-output-schema-v1.1-n3-canonical.json`
2. `model-visible-host-capabilities.md`

El esquema sigue siendo también el argumento técnico `--format-schema`; la copia embebida garantiza su visibilidad en el prompt. No se añadió contenido musical ni se modificó ningún contrato semántico.

Hash corregido, idéntico bajo condiciones simétricas para ambos modelos: `0ed8244b617281f39e553f40a9212bf74b555d21c6876abc7a5a9c26dcd88be5`.

## Preflight equivalente al runner

Se ejecutó offline la misma función `preflight` con el payload corregido, brief, instrucción y los dos `--required-record` exactos. Resultado para Qwen y Ministral: PASS, sin errores, `resolved_record_count: 10`. No se ejecutó `staged_runner.py` y no se consumió ningún intento.

## Estado de intento

El intento 1 permanece disponible: no existen `raw-output.txt`, `raw-api-response.json` ni `capture-manifest.json` bajo XMODEL-009. La revisión debe aprobarse explícitamente antes de cualquier ejecución.
