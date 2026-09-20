# XMODEL-010: Preflight prospectivo offline

Estado: **PREPARED_NOT_EXECUTED**. `EXECUTED: NO`. Experimento nuevo, después de XMODEL-009. Qwen 3 14B (`qwen3:14b`) es el único modelo planeado; Ministral está aparcado y no debe ejecutarse en esta preparación. Todo trabajo reportado aquí fue local/offline. No se generó MIDI.

El éxito principal será que una salida originada por Qwen, sin reparación semántica ni decisiones musicales del adaptador, supere: gate estructural Stage 3, contrato SongPlanV2 del music-engine 4.0.0, validación semántica del engine y resolución host necesaria. Eso mide transferencia/proceso técnico, no calidad musical. No es continuación numérica de XMODEL-009.

La solicitud usa el mismo brief congelado que XMODEL-009 para aislar cambio de lmite tcnico. Interface semntica sigue v1.1, Composer Knowledge y genre pack no cambian. El esquema Stage 3 v1.2 y prompt v1.2 son endurecimiento de representacin tcnica: tipos/estructuras del engine y notacin Fraction; no anaden decisiones musicales. N3-P conserva significado y posibles estados.

## Presupuesto y entrada

Qwen Stage 1 de XMODEL-009 termin con `eval_count=2864` de `num_predict=4096` y `done_reason=stop`; se conservan 4096 como lmite. Stage 2 y 3 conservan 8192. La medicin est documentada en `stage1-output-budget-audit-v1.0.md`. Payload idntico para las condiciones Qwen y Ministral: 65 010 bytes, hash `5fdae8712a5e74e91ad78b078b97b06c5dfcfaab230d77c1fd6458301e54a8ce`.

Stage 1 incluye el brief exacto, interfaz v1.1 y conocimiento aprobado, contrato del sistema, prompt, esquema Stage 1 embebido y pasado adems como formato estructurado, y las capacidades host aprobadas. El manifiesto y payload reflejan cada registro. `--format-schema` por s mismo no sustituye su inclusin en el texto model-visible.

## Comandos de preparacin/ejecucin (Qwen solamente)

Este bloque contiene comandos preparados, no ejecutados. En PowerShell desde raiz del repositorio:

```powershell
$root = (Get-Location).Path
$x = Join-Path $root 'evaluations/composer-agent/XMODEL-010'
$q = Join-Path $x 'outputs/qwen3-14b'
$brief = Join-Path $x 'brief.yaml'
$s1 = Join-Path $x 'stage-1-prompt-v1.2.txt'
$s1schema = Join-Path $x 'stage-1-output-schema-v1.1-n3-canonical.json'
$hostcaps = Join-Path $x 'model-visible-host-capabilities.md'
```

Comando exacto del primer request, al autorizarse el experimento:

```powershell
python integrations/composer-agent/staged_runner.py `
  --experiment-id XMODEL-010 `
  --request-kind evaluable_attempt --request-id XMODEL-010-QWEN-STAGE1-A1 `
  --request-registry (Join-Path $q 'request-registry') `
  --model qwen3:14b --stage stage-1 --attempt 1 `
  --input (Join-Path $q 'stage-1-payload.txt') `
  --brief $brief --stage-number 1 --instruction $s1 `
  --format-schema $s1schema `
  --required-record $s1schema --required-record $hostcaps `
  --output-dir (Join-Path $q 'captures/stage-1/attempt-1') `
  --num-predict 4096 --http-timeout 7200
```

La misma política de transporte de 7200 segundos se aplica a las etapas 2 y 3. Se amplía únicamente el timeout HTTP: en XMODEL-009 la respuesta completa de recuperación de Qwen tardó 3908.344 segundos (`evaluations/composer-agent/XMODEL-009/qwen3-14b/outputs/stage-3/recovery-001/capture/capture-manifest.json`), por encima de 3600. No cambian los parámetros de generación. El timeout de urllib es de socket, no un plazo total de experimento.

La politica congelada esta en `transport-policy-v1.0.yaml`. El runner vuelve a ejecutar el mismo preflight de los argumentos requeridos. Antes de HTTP reserva ID y directorio con creacin exclusiva y registra `PREPARED`; luego escribe `SENT` antes de llamar al transporte. Estados terminales: `CAPTURED`, `TIMEOUT`, `CONNECTION_FAILURE`, `HTTP_ERROR`, `INTERRUPTED_OR_INCOMPLETE`, `INVALID_API_RESPONSE`. Cada estado `SENT` incrementa `model_request_count` en uno y especifica `request_kind`. El request ID, identidad etapa/intento ya enviada o directorio existente hace fallar antes de enviar. Un fallo de transporte no es fallo de cumplimiento del modelo ni produce una salida evaluable. Sin embargo, despus de `SENT` el par etapa/intento queda reservado para impedir reutilizarlo; una recuperacin usa request ID y nmero de intento siguiente, `--request-kind transport_recovery`, queda marcada y contada como peticin separada y no es continuacin de la generacin interrumpida.

Tras cada salida capturada se ejecuta el gate. Solo si Stage 1 PASS se promueve la salida a `accepted-output.json` mediante copia nueva/exclusiva y se prepara Stage 2. Stage 2 usa prompt/mapa Stage 2 y formato JSON object-neutral `stage-2-json-object-format-v1.0.json` en `--format-schema` y `--required-record`; esto refuerza una sola raiz objeto sin imponer propiedades/soluciones musicales. Stage 3 usa `stage-3-prompt-v1.2.txt`, pasa `stage-3-songplan-format-schema-v1.2.json` por `--format-schema` y `--required-record`, e incluye el schema de referencia `engine-songplan-v2.schema-music-engine-4.0.0.json` como registro requerido. Cada etapa posterior incluye la salida aceptada anterior. No se ejecuta etapa posterior tras gate fallido.

## Reintentos

Poltica congelada en `stage-2-retry-policy-v1.0.yaml`: mximo tres intentos evaluables por etapa. Crear cada retry desde el payload de etapa original congelado con el ultimo diagnstico exacto del gate. No encadenar `retry-input` previo, no retransmitir respuesta raw, no sugerir valores musicales. Intentos adicionales de transporte requieren ID unico y se informan como recuperacin aparte; la regla de mximo tres intentos evaluables no convierte recuperacin en continuacin exacta.

## Percusin / host

La unica configuracin aprobada disponible para este experimento es `drums` con `drum_voice` y DrumExternalMap `song001_r1_steven_slate_map`. La asignacin MIDI Steven Slate permanece intacta. No se aprobaron IDs/mapa `PercussionMap`; una pista `percussion` con eventos que no pueda resolverse produce `HOST_CONFIGURATION_INVALID` y bloquea la etapa, sin cambiar IDs ni convertirla a drums. El Owner decidir esos mapas fuera de este paquete si fueran necesarios.

## Revision semantica humana

La puerta humana posterior al PASS del engine se define en `human-audit-boundary-v1.0.md`. El engine no demuestra por si solo que toda etiqueta armonica describa correctamente el voicing concreto. Esta auditoria acepta o registra discrepancias; no repara material.

## Ejecucin prohibida durante preflight

No se envio ninguna solicitud a Ollama; Qwen y Ministral no se ejecutaron; no se emitieron etapas 2/3 ni se genero MIDI. Las carpetas `captures` estn vacas. `outputs/ministral-3-14b-parked` solo guarda copia byte-idntica del payload simtrico, sin configuracin de invocacin ni resultado.


El payload raiz es el input seleccionado y coincide byte a byte con `outputs/qwen3-14b/revision-002/stage-1-payload-v1.2.txt`. `revision-000` y `revision-001` conservan borradores de preflight no transmitidos; el manifiesto los marca supersedidos. El attempt 1 sigue intacto y sin captura porque no hubo inferencia.
