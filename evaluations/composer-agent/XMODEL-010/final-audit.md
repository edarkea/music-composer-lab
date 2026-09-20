# XMODEL-010 — Auditoría final y cierre

**Fecha de cierre:** 2026-09-20  
**Disposición:** **CLOSED — VALID NEGATIVE FOR FULL PIPELINE COMPLETION UNDER XMODEL-010 CONDITIONS**

## Resumen ejecutivo

XMODEL-010 fue una prueba prospectiva de transferencia por etapas para `qwen3:14b`. Stage 1 y Stage 2 pasaron sus gates deterministas. Ninguno de los tres SongPlanV2 producidos en Stage 3 completó toda la validación: el intento 1 y el intento 3 fallaron la validación musical por notas fuera de escala sin autorización cromática; el intento 2 llegó a validación host y falló porque una pista `percussion` usó como `map_id` el identificador aprobado únicamente para `drums`.

La conclusión se limita a que **Qwen no completó el pipeline bajo las condiciones de XMODEL-010**. No es una conclusión sobre su capacidad general para componer, la calidad artística de sus decisiones, ni el sonido audible. No hubo un SongPlanV2 aprobado por engine y host, no se materializó MIDI y no se hizo evaluación auditiva independiente.

## Condiciones congeladas

- Interface: `composer-interface-v1.1`; condición `NO-EXAMPLE`.
- Brief: `brief.yaml`, SHA-256 `464ae4378bcb7236f0fb36da52eb65dcb03735197284e3a6899b8686d51ede0b`.
- Modelo ejecutado: `qwen3:14b`. Ministral permaneció aparcado y no fue ejecutado.
- Parámetros comunes: temperature 0, seed 41, top_p 1, top_k 40, repeat_penalty 1, num_ctx 32768; `num_predict`: 4096 en Stage 1 y 8192 en Stage 2/3.
- Timeout HTTP: 7200 s en todas las solicitudes capturadas. Es timeout de transporte; no cambia los parámetros de generación.
- Máximo de intentos evaluables: tres por etapa. Los retries Stage 3 se ramificaron del payload original más el diagnóstico literal del gate anterior; no incluyeron la respuesta raw anterior.
- Music-engine: 4.0.0, commit `71bbc73337da0d755618bd796e19ce2e82cc3df`, wheel SHA-256 `110E987A1E102C1CF3D29FEC1CCC68583459030F40748E10D66CE1F8E4819FE1`. Las validaciones Stage 3 de cierre se repitieron desde `.venv/Scripts/python.exe`, que importa esta versión.
- Host aprobado: `song001_r1_steven_slate_map` es un `DrumExternalMap` para pistas `drums`. No hay `PercussionMap` aprobado; `host-config.yaml` declara `percussion.map_dir: null` y `approved_map_ids: []`.
- Reparación semántica: cero. Decisiones musicales del adaptador: cero.

## Método y límites de evidencia

Se cotejaron los manifiestos PREPARED/SENT, historiales de estado, manifiestos de captura, respuestas API, payloads, copias aceptadas y hashes. Los cinco gates se volvieron a ejecutar offline sobre las salidas raw inmutables; Stage 3 se ejecutó con el intérprete del `.venv` y la configuración host del paquete. No se ejecutó Ollama durante esta auditoría.

Los gates originales no estaban guardados como archivos `gate-result.json`; las categorías y diagnósticos de este cierre corresponden a las reejecuciones deterministas indicadas en `request-capture-gate-ledger.json`. No falta procedencia de las solicitudes o respuestas. La ausencia de un artefacto raw de gate anterior se conserva como limitación de registro, no se presenta como captura histórica.

Las capas se mantienen separadas: payload preparado; solicitud enviada; respuesta completa; gate de serialización/contrato; parseo y validación SongPlanV2; resolución host; evaluación semántica musical; auditoría compositiva independiente; materialización MIDI; escucha. `CAPTURED` no implica gate PASS; gate PASS no demuestra calidad artística; validación del engine no demuestra calidad audible.

En concreto, las tres salidas Stage 3 pasaron el parseo de un objeto JSON y el gate contractual determinista de Stage 3; el codec del engine también pudo decodificar cada SongPlanV2. A1 y A3 llegaron al validador semántico del engine y fallaron por escala. A2 pasó esa validación y llegó a resolución de recursos host, donde falló. No hubo PASS final de engine+host. El gate local no ejecuta una validación JSON Schema separada; la salida se pidió con el esquema estructurado de Ollama y luego se comprobó con el gate y el codec reales.

## Ejecución y resultados

| Solicitud | Captura | Gate reproducido | Diagnóstico / resultado |
|---|---|---|---|
| Stage 1 A1 — `XMODEL-010-QWEN-STAGE1-A1` | CAPTURED, `stop`; 2496 tokens evaluados; 746.656 s | PASS — `contract_validation` | Salida contractual aceptada. |
| Stage 2 A1 — `XMODEL-010-QWEN-STAGE2-A1` | CAPTURED, `stop`; 1365 tokens; 480.797 s | PASS — `contract_validation` | Salida contractual aceptada. |
| Stage 3 A1 — `XMODEL-010-QWEN-STAGE3-A1` | CAPTURED, `stop`; 2975 tokens; 4390.609 s | FAIL — `musical_semantic_validation_failure`; engine invocado | `tracks[0].motifs[1].events[0].pitches[0]`: `pitch.outside_scale`; “pitch must be in the song scale unless chromatic”. |
| Stage 3 A2 — `XMODEL-010-QWEN-STAGE3-A2` | CAPTURED, `stop`; 1808 tokens; 1186.157 s | FAIL — `host_configuration_failure`; engine invocado | `percussion` usó `map_id` `song001_r1_steven_slate_map`, sin directorio PercussionMap aprobado. El mapa DrumExternalMap aprobado no es inválido; no aplica a pistas `percussion`. |
| Stage 3 A3 — `XMODEL-010-QWEN-STAGE3-A3` | CAPTURED, `stop`; 1228 tokens; 2707.422 s | FAIL — `musical_semantic_validation_failure`; engine invocado | `tracks[0].motifs[0].events[1].pitches[0]`: `pitch.outside_scale`; “pitch must be in the song scale unless chromatic”. |

Se registraron cinco solicitudes reales (`PREPARED → SENT → CAPTURED`) y cinco respuestas completas con `done: true`. El lanzamiento repetido de Stage 3 A2 fue rechazado por el registro de identidad porque ese intento ya se había enviado; no creó otra solicitud ni captura. El intento 3 fue el tercero y último evaluable de Stage 3. No existe intento 4.

## Procedencia y discrepancias técnicas

**Stage 1:** el payload enviado tiene SHA-256 `5fdae8712a5e74e91ad78b078b97b06c5dfcfaab230d77c1fd6458301e54a8ce`. Tanto la copia de conveniencia `outputs/qwen3-14b/accepted/stage-1.json` como la copia protocolaria `outputs/qwen3-14b/outputs/stage-1/accepted-output.json` son byte idénticas a `captures/stage-1/attempt-1/raw-output.txt` y tienen SHA-256 `c7886b2a093a871cd85b34a26768c3459375c0c15440f4c1f66ebd67aa9ae8d4`. La copia adicional es una discrepancia de organización; ambas se preservan.

**Colisión de manifiesto de Stage 2:** el ensamblador escribió `outputs/qwen3-14b/stage-2-payload.txt` (SHA-256 `a25d82686d9388d70405b7fc04c8fe71de748067b651bd1118795c42d4136c72`) y después no pudo escribir el `payload-manifest.json` compartido ya existente. La solicitud Stage 2 usó exactamente ese payload, según su hash de entrada, y el capture manifest conserva los registros resueltos. Fue un problema de disposición de artefactos, no una solicitud ni un fallo del modelo.

**Colisión de manifiesto de Stage 3:** ocurrió el mismo problema al ensamblar `stage-3-payload.txt`. Se conservó el archivo producido y se reensambló en `outputs/qwen3-14b/stage-3-prepared/`, con manifiesto propio y preflight PASS. Ambas copias tienen hash `758927d3ed54e11dfbf22d0f7e7c7e870c9274d2af52bfbddb789e6f92787d39`, 73 999 bytes; la copia aislada registra 11 registros resueltos y es la usada por Stage 3 A1.

**Entorno Python del gate:** la primera invocación Stage 3 con `python` del sistema no pudo importar `music_engine`. Fue un incidente de entorno, no una solicitud, resultado de modelo ni gate evaluable. Repetir con `.venv/Scripts/python.exe` invocó music-engine 4.0.0 y produjo el diagnóstico semántico real.

**Host visible:** las entradas de Stage 3 incluyeron `integration-contract.md`, `host-config.yaml` y el mapa DrumExternalMap. La configuración visible separaba `drums.map_id` del directorio PercussionMap no aprobado. La incompatibilidad del intento 2 es del SongPlan producido respecto a las capacidades host congeladas; no autoriza registrar un mapa ni convertir la pista automáticamente.

**Reintentos:** Stage 3 A2 (SHA-256 `ce407823c5942ab789d46dfaae151c78b1abfee33918ba469b145a81485402e7`) contiene el payload original más el diagnóstico literal del intento 1. Stage 3 A3 (SHA-256 `7de060e36de1e23b9f9966057aca0625647dc826dca7ffc76c4dae6b74250698`) contiene el mismo payload original más el diagnóstico literal del intento 2. Sus manifiestos dicen `previous_raw_output_embedded: false`; ambos pasan preflight. El rechazo del segundo lanzamiento de A2 confirma que el registro evita reutilizar identidades ya enviadas.

## Resultado y límites

Stage 3 alcanzó el máximo de tres intentos y no produjo un SongPlanV2 aceptado por engine y host. En consecuencia no hubo materialización MIDI. No se hizo auditoría compositiva independiente ni escucha. Ministral no participó; esto no es comparación entre modelos. XMODEL-009 solo se menciona descriptivamente: el timeout mayor permitió capturas completas en XMODEL-010; la frontera bloqueante siguió siendo Stage 3. No se deriva ranking cuantitativo ni conclusión general sobre Qwen.

Mejoras de herramienta para trabajo futuro, separadas de este resultado: usar directorios/manifiestos por etapa para los payloads; fijar explícitamente el intérprete que ejecuta el gate del engine; conservar la exclusividad de identidad de solicitud.

## Verificación offline ejecutada

Se reejecutaron los gates sobre las cinco capturas, sin enviar solicitudes: Stage 1 y 2 con `--stage 1/2`; Stage 3 A1 con `--output outputs/qwen3-14b/captures/stage-3/attempt-1/raw-output.txt`; A2 con `--output outputs/qwen3-14b/captures/stage-3/attempt-2/capture/raw-output.txt`; A3 con `--output outputs/qwen3-14b/captures/stage-3/attempt-3/capture/raw-output.txt`. Los tres gates Stage 3 usaron `--host-config evaluations/composer-agent/XMODEL-010/host-config.yaml` y el intérprete `.venv/Scripts/python.exe`. Resultados: 2 PASS y 3 FAIL con las categorías de la tabla.

Pruebas offline adicionales ejecutadas:

- `.venv/Scripts/python.exe -B -m unittest discover -s evaluations/composer-agent/XMODEL-010 -p 'test_*.py'` — 34/34 PASS.
- `.venv/Scripts/python.exe -B -m unittest discover -s integrations/composer-agent -p 'test_staged_harness.py'` — 54/54 PASS.
- Auditoría local por script Python: hashes de payloads/capturas/copias aceptadas, conteo SENT/CAPTURED, retries, ausencia de MIDI y de intento 4 — PASS.

## Cierre documental

No se encontró un índice central de experimentos. El `run-manifest.yaml` y el `resolved-input-manifest-v1.0.json` se preservan como snapshot de preparación y hashes; este informe y el ledger son el registro de cierre. No se reabrió XMODEL-010 ni se preparó otro experimento.
