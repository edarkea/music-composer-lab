# XMODEL-011 — Preparación de Codex CLI como compositor

Estado: `PREPARADO_CON_AISLAMIENTO_PARCIAL`; Stage 1 no está listo para ejecución. XMODEL-011 es una evaluación nueva y no es una continuación de los resultados de XMODEL-009 o XMODEL-010.

El paquete conserva el brief, Composer Interface v1.1, conocimiento aprobado, indie-dance, N3-P, el contrato SongPlanV2 y el mapa de drums aprobado. No contiene salidas, planes fallidos, auditorías ni fixtures de otros experimentos en `model-visible/`. La invocación futura usará una petición nueva y efímera de `codex exec` para cada etapa; el evaluador externo y `music-engine 4.0.0` conservan la autoridad de validación. No se materializa MIDI.

Cada entrada se arma y congela por etapa en `outputs/codex/stage-N/payload/`; las capturas, resultados de gate y copias aceptadas se mantienen separados bajo `attempts/` y `accepted/`. Cada payload tiene su propio `payload-manifest.json`. Stage 2 requiere una copia aceptada de Stage 1; Stage 3 requiere las copias aceptadas de Stage 1 y 2. `accept_output.py` solo crea una copia byte-identical después de un gate PASS sin reparación semántica; la copia incluye un manifiesto de aceptación que los siguientes ensamblados comprueban.

Los reintentos conservan el payload original y agregan solamente una línea con el diagnóstico literal del gate inmediatamente anterior. No se permite una cuarta tentativa. Una sesión CLI debe terminar con código cero, archivo final no vacío y un evento terminal `turn.completed` o `response.completed`; en caso contrario el resultado se marca `CLI_FAILED_OR_INCOMPLETE`, nunca como captura aceptable. Eventos JSONL, stderr, respuesta final y hashes se separan.

La preparación técnica está incompleta por aislamiento: el CLI permite elegir un directorio de trabajo y `read-only`, pero la ayuda local limita expresamente ese modo a comandos de shell generados, y no demuestra que el compositor no pueda leer archivos externos. `codex sandbox` requiere un perfil que no está configurado; la función de sandbox para Windows figura como “under development”. El directorio temporal por petición, `--ignore-user-config`, `--ignore-rules` y `--sandbox read-only` reducen superficie accidental, pero no establecen una frontera de lectura exigible contra XMODEL-009/XMODEL-010 ni contra internals del evaluador. Mantener `execution_authorized: false` hasta disponer de un aislamiento comprobable.

El identificador de modelo no se fija: la CLI instalada no publica su modelo predeterminado mediante `--help` y el Owner no ha seleccionado uno. La herramienta registra el modelo solicitado y solo registra identidad servida si la CLI emite un campo explícito `server_model`; no usa campos genéricos ni infiere identidad. No se afirma equivalencia de inferencia con Ollama.

El paquete está preparado para revisión. La política de ejecución manual y el límite restante de aislamiento se detallan en la sección siguiente.

Consulte `codex-cli-findings.md`, `run-manifest.yaml`, `model-visible-inventory.json` y `prepared-commands.ps1.txt` para el detalle y los comandos preparados.

## Actualización de infraestructura: frontera parcial de herramientas

Corrección de precisión respecto a la nota inicial: `--permission-profile` es opcional en `codex sandbox`; el bloqueo no era la ausencia de ese perfil sino los permisos ACL amplios heredados por su identidad restringida.

La frontera para las herramientas locales del compositor se aplica mediante la identidad restringida Windows `STEVE\CodexSandboxUsers` y ACE NTFS de denegación de lectura/ejecución en la raíz del repositorio y en `C:\Users\Steeven\.codex`. La prueba ejecutada como `steve\codexsandboxoffline` confirmó que el repositorio, el sentinel de XMODEL-010 y CODEX_HOME devuelven acceso denegado, mientras que el workspace externo y el schema copiado siguen legibles. El runner repite este control antes de reservar el intento y falla cerrado si cambian permisos, identidad o hash del schema.

Esto solo prueba el token de los procesos de herramientas. El proceso padre `codex exec` seguiría ejecutándose como la cuenta Owner y conserva acceso al repositorio; no se ha demostrado que todas las rutas de lectura de Codex pasen por el sandbox restringido. Por eso el control es defensa adicional, no una frontera completa: Stage 1 sigue bloqueado y `execution_authorized` permanece `false`.

Este mecanismo usa el token restringido de Windows y permisos efectivos; no es una VM. La protección comprobada cubre accesos de filesystem ejecutados con esa identidad. No se afirma aislamiento frente a un posible canal interno que omitiera el sandbox de herramientas. Si la CLI pudiera leer archivos por fuera de ese token, el preflight no podría demostrarlo sin inferencia; la alternativa sería ejecutar dentro de una VM sin unidades compartidas.

## Flujo manual del Owner — preparación de Stage 1

La instrucción anterior de usar `codex_composer_runner.py` queda reemplazada para este experimento: Codex de mantenimiento no ejecuta ni lanza Codex CLI. El Owner debe ejecutar manualmente los comandos de `prepared-commands.ps1.txt` desde PowerShell, con el repositorio como directorio actual. Ese archivo solo prepara la reserva y muestra la invocación manual; no se ha ejecutado.

El intento se reserva con ID exclusivo antes de enviar la petición. Después de marcarlo `SENT_MANUAL`, el ID no se reutiliza aunque la consola se interrumpa o no haya respuesta. Cada intento tiene directorio y registry propios, y se rechaza cualquier destino existente. Los reintentos (máximo tres) usan una entrada nueva derivada del payload Stage 1 original más únicamente el diagnóstico literal del gate anterior; un error de transporte requiere registrarse como transporte y no se disfraza de diagnóstico de gate.

La CLI guarda el mensaje final, los eventos JSONL y stderr en archivos separados. `manual_capture.py record` registra hashes, código de salida, versión y cualquier identidad literal `server_model`; `verify` y `gate_capture.py` impiden pasar al gate sin respuesta no vacía, código cero, evento terminal y hashes coherentes. No se ha confirmado en esta preparación que Codex 0.154.0 emita `turn.completed` en una ejecución real; por diseño se bloqueará si el formato difiere.

La frontera de archivos no es estricta: ejecutar la CLI con la cuenta Owner, `--cd` fuera del repositorio, `--sandbox read-only` o una instrucción de prompt no demuestra que XMODEL-009/010 sean inaccesibles durante toda la ejecución. Las alternativas son: (1) continuar como prueba exploratoria con posible exposición histórica y documentar esa limitación metodológica; (2) configurar una cuenta Windows dedicada con ACL y comprobar bajo el token real de Codex que el repositorio histórico y CODEX_HOME son inaccesibles, manteniendo disponible solo el paquete curado; o (3) usar una VM aislada sin unidades ni carpetas compartidas y verificar allí el paquete. No se impone Windows Sandbox. Antes de considerar el test aislado, el Owner debe escoger la condición metodológica; los comandos no inician Stage 1 automáticamente.

Stage 2 solo se prepara después del PASS externo de Stage 1. Stage 3 mantiene gate externo con music-engine 4.0.0 y no materializa MIDI.
