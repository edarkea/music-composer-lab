# XMODEL-009 — auditoría final y cierre

**Disposición:** `CLOSED — VALID NEGATIVE FOR FULL PIPELINE COMPLETION UNDER XMODEL-009 CONDITIONS`  
**Interfaz:** Composer Interface v1.1  
**Condición:** NO-EXAMPLE  
**Brief congelado SHA256:** `464ae4378bcb7236f0fb36da52eb65dcb03735197284e3a6899b8686d51ede0b`

## Alcance y método

Esta auditoría concilia las capturas, manifiestos, payloads, informes de gate y el log local de Ollama. Se calcularon SHA256 sobre los archivos existentes, se reconstruyeron los cuerpos de solicitud a partir del payload capturado, los parámetros y esquemas registrados, y se repitieron en modo de solo lectura los gates locales; para Stage 3 se invocó el validador real de music-engine 4.0.0 mediante el gate, sin materializar MIDI. El ledger JSON contiene una fila por solicitud enviada o captura completa, con las rutas, hashes y resultados.

La preparación inicial de Stage 1 usó payloads con hash `a2f6fa4451d6597a806fb7bf49ee073d1b6ad4b0295e062df610d916a21c472a`. El runner falló en preflight porque el esquema requerido no estaba incluido; no llegó a Ollama, no cuenta como solicitud ni como intento. La corrección `revision-001` añadió el esquema y la información de capacidad host al payload visible. Ambos modelos ejecutaron Stage 1 con el mismo payload corregido, hash `0ed8244b617281f39e553f40a9212bf74b555d21c6876abc7a5a9c26dcd88be5`.

Los manifiestos de ejecución describen Composer Interface v1.1, NO-EXAMPLE, máximo tres intentos evaluables por etapa, retries con diagnósticos deterministas solamente, sin replay de la respuesta previa, sin reparación semántica y sin avanzar tras un gate fallido. Generation settings congelados: temperatura 0, seed 41, top-p 1, top-k 40, repeat penalty 1, contexto 32768; presupuestos: Stage 1 4096, Stage 2 8192, Stage 3 8192. Stage 1 usó `stage-1-output-schema-v1.1-n3-canonical.json`; Stage 2 no usó `format` de Ollama; Stage 3 usó `stage-3-songplan-format-schema-v1.1.json` y el gate de music-engine más host config.

Registros de Stage 3 observables en los payloads: prompt reconciliado, contrato SongPlanV2, serialización, schema de salida, brief, salida Stage 2 aceptada y recursos host. Configuración: `host-config.yaml` SHA256 `030ce1ccc36a7a900052a675a6dc9524b09e56a6765271a070c8d214a797d147`; mapa Steven Slate `song001_r1_steven_slate_map.yaml` SHA256 `3c8f366f7ea0ee870dfd8ccaac563ebd8545d1f17ab87d49658aa058faf8a1ab`. Se aprobó la capacidad `drums`; no hay IDs PercussionMap aprobados. Estas son capacidades de validación/materialización, no decisiones musicales del adaptador.

## Cronología y resultados

### Qwen 3:14b

- **Stage 1, intento 1:** respuesta CAPTURED; `done_reason=stop`; gate PASS (`contract_validation`). Modelo solicitado y reportado: `qwen3:14b`.
- **Stage 2, intento 1:** CAPTURED; `done_reason=stop`; gate PASS (`contract_validation`). Modelo solicitado y reportado: `qwen3:14b`.
- **Stage 3, intento 1:** CAPTURED; JSON de salida completo; gate FAIL en validación musical-semántica del motor. El motor informó dos notas fuera de la escala declarada sin `chromatic` autorizado: `tracks[0].motifs[0].events[1].pitches[0]` y `tracks[1].motifs[0].events[0].pitches[0]`.
- **Stage 3, intento 2 original:** la solicitud alcanzó Ollama. El log `C:/Users/Steeven/AppData/Local/Ollama/server-1.log` registra `POST /api/chat`, HTTP 500 tras exactamente `1h0m0s`, tarea 4729 cancelada y `n_tokens=16953, truncated=0`. No hay respuesta completa, captura ni gate. El `request_id`, request hash y traceback íntegro no quedaron guardados por el runner; el inicio y fin horarios son aproximados/derivados del log y del informe de transporte.
- **Stage 3, recovery-001 asociada al intento 2:** fue una solicitud adicional, no continuación de la generación interrumpida. Usó el mismo retry payload (`f06cda45...399e0664a`) y los mismos parámetros de generación; el timeout de transporte cambió de 3600 a 7200 segundos. CAPTURED, `done_reason=stop`; gate FAIL `invalid_songplan_structure`: `duration must be a valid fraction`. La salida no pasó la validación estructural, así que este resultado no demuestra que se corrigieran las notas fuera de escala.
- **Stage 3, intento 3:** CAPTURED; `done_reason=stop`; gate FAIL en validación musical-semántica. El motor informó tres pitches fuera de escala sin autorización cromática: `tracks[0].motifs[0].events[1].pitches[0]`, `tracks[1].motifs[0].events[0].pitches[0]` y `tracks[1].motifs[0].events[2].pitches[0]`.

Resultado: Qwen pasó Stage 1 y Stage 2. Stage 3 produjo tres respuestas completas evaluables y fallidas (intento 1, recovery-001 asociada al intento 2 e intento 3), más una solicitud de intento 2 que terminó en fallo de transporte. No existe SongPlanV2 aprobado para materialización.

### Ministral 3:14b

- **Stage 1, intentos 1–3:** los tres CAPTURED; en cada uno `done_reason=length`, `eval_count=4096`; los tres gates fallaron como `serialization_failure` por JSON incompleto (`Unterminated string`) y el requisito de un único objeto JSON raw.
- Modelo solicitado/reportado en las tres capturas: `ministral-3:14b`.
- **Stages 2 y 3:** NOT EXECUTED porque Stage 1 no pasó; no se clasifican como fallos.

Resultado: Ministral quedó bloqueado en Stage 1 bajo el brief, payload, esquema y presupuesto registrados. No se infiere qué produciría con otras condiciones.

## Conciliación de solicitudes

El ledger contiene **9 solicitudes a Ollama: 6 Qwen y 3 Ministral; 8 respuestas HTTP completas capturadas y 1 fallo de transporte sin respuesta recuperable**. La solicitud fallida está corroborada por el log local de Ollama. La preparación fallida de Stage 1 queda fuera del recuento porque se detuvo en preflight antes de Ollama.

Los hashes del cuerpo de solicitud se reconstruyeron desde el payload, settings y esquema para las ocho capturas; coinciden con los hashes de request de sus manifiestos. Para la solicitud original con timeout no hay request hash capturado y el ledger lo deja vacío, sin reconstrucción presentada como hash observado. Los ocho hashes de respuesta API y ocho hashes de salida coinciden con sus manifiestos. Los hashes y resultados individuales están en `request-capture-gate-ledger.json`.

## Niveles de evidencia

1. **Solicitud/transporte:** ocho respuestas completas; una solicitud Qwen llegó a Ollama y terminó con HTTP 500/cancelación tras una hora.
2. **Captura HTTP:** ocho archivos `raw-api-response.json` completos; el intento interrumpido no tiene cuerpo completo recuperable.
3. **Serialización JSON:** Qwen Stage 1/2 y tres salidas de Stage 3 pasaron el parseo local suficiente para alcanzar sus validaciones siguientes; Ministral falló el parseo en las tres respuestas. La salida recovery de Qwen fue JSON parseable, pero no cumplió estructura SongPlanV2.
4. **Gates por etapa:** Qwen Stage 1/2 PASS; sus tres salidas completas Stage 3 FAIL. Ministral Stage 1 FAIL en los tres intentos; etapas posteriores no ejecutadas.
5. **Engine real:** invocado para las tres salidas completas de Qwen Stage 3: dos fallos musicales-semánticos por escala y un fallo estructural de duración. No se ejecutó para Ministral por no alcanzar Stage 3.
6. **Evaluación compositiva independiente:** no consta y no se realizó en esta auditoría.
7. **MIDI/materialización/audición:** no se generó MIDI ni hay evidencia de evaluación audible en XMODEL-009.

Todos los manifiestos de captura declaran `semantic_repair_performed: false`. Las entradas retry añaden diagnósticos estructurales de gate, sin sugerencias musicales. Reparaciones semánticas o decisiones musicales añadidas por el adaptador: **0**.

## Integridad, comparabilidad y discrepancias

Los dos modelos recibieron el mismo brief y el mismo payload Stage 1 `revision-001`, así como el mismo esquema y generación settings. Los retries difieren únicamente en los diagnósticos producidos por sus fallos previos, según el protocolo. Ambos modelos no recorrieron las mismas etapas: Qwen alcanzó Stage 3 y Ministral no superó Stage 1. No procede un ranking ni una comparación general de capacidad o calidad sonora.

La recuperación de Qwen es una solicitud adicional. Cambió solo el timeout de transporte (3600→7200 s), manteniendo prompt, schema, modelo y generación settings. El tiempo de transporte queda como desviación técnica documentada: la respuesta de recovery tardó aproximadamente 3908 s según su manifiesto. No se presenta como continuación exacta ni se mezcla con el timeout original.

Hay metadatos de preparación que quedaron obsoletos y se preservan byte por byte: `run-manifest.yaml` y `preflight-results.yaml` aún dicen PREPARED_NOT_EXECUTED; el manifiesto de recovery conserva `outcome: PENDING` y su README dice que el directorio está vacío, aunque existen capturas. El `qwen3-14b/payload-manifest.json` raíz apunta actualmente a Stage 3, mientras que el Stage 1 usado está documentado por el manifiesto de `revision-001` y por los hashes de entrada de ambas capturas. Los manifiestos iniciales tampoco registran request_id en capturas Qwen antiguas; el ledger marca esos IDs como derivados de modelo/etapa/intento, no como valores originales.

El historial de transporte del intento 2 no conserva traceback Python íntegro, request_id ni hash de request; los hechos disponibles son el `TimeoutError` comunicado, el registro YAML de transporte y el log Ollama corroborante. No se infiere terminación exitosa a partir del modelo cargado.

Estas limitaciones reducen la trazabilidad fina de esa solicitud, pero no borran los resultados de las ocho respuestas completas ni invalidan la conclusión de que el pipeline completo no se completó bajo las condiciones XMODEL-009. No se encontró un índice o registro global de experimentos que requiera actualización; por ello no se creó uno.

## Verificación offline de cierre

Comandos/procedimientos ejecutados en solo lectura:

- `Get-FileHash <archivo> -Algorithm SHA256` para brief, payloads originales/corregidos, schemas, host config, mapa y capturas.
- Un script Python de solo lectura sobre `capture-manifest.json`: localizó payload por hash, reconstruyó el request compacto con schema/settings, comparó request/response/output hashes y llamó `staged_harness.gate()` para cada captura. Resultado: 8/8 request hashes, 8/8 response hashes y 8/8 output hashes coincidentes con manifiestos; gates consistentes con la tabla del ledger.
- Lectura del log `server-1.log`: una línea `POST /api/chat` HTTP 500 tras 1h0m0s para el fallo Qwen, con cancelación de tarea 4729.
- No se ejecutaron pruebas de modelo ni de MIDI. La verificación del gate de Stage 3 es una validación offline real-engine, no materialización.

## Conclusión y cierre

XMODEL-009 es un **resultado negativo válido para completar el pipeline bajo sus condiciones específicas**: Ministral no superó Stage 1; Qwen superó Stage 1 y Stage 2, pero ninguna salida Stage 3 superó la aceptación del SongPlanV2 con el engine real. Ninguno produjo un SongPlanV2 aceptado por el protocolo completo. Esto no demuestra incapacidad general de ninguno de los modelos para componer música.

**Estado final:** `CLOSED — VALID NEGATIVE FOR FULL PIPELINE COMPLETION UNDER XMODEL-009 CONDITIONS`.

**Durante el cierre:** modelos ejecutados NO; MIDI generado NO; capturas históricas modificadas NO; decisiones musicales/reparaciones semánticas del adaptador añadidas 0.
