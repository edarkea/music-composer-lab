# EXP-003 — especificación del backend mínimo

## Alcance

Backend específico de despliegue para crear sesiones, persistir estado, validar una finalización, registrar abortos, aplicar idempotencia y exportar registros técnicos. No es una plataforma general de experimentos.

## Runtime y almacenamiento

- Node.js 24.13.1 usado para la validación local; Node.js 18+ es el mínimo previsto por las APIs utilizadas.
- Sin dependencias npm externas.
- Persistencia en un archivo JSON local mediante escritura temporal y rename atómico. El hosting debe proporcionar filesystem persistente; no se asume persistencia en serverless/ephemeral.
- HTTPS obligatorio cuando el backend se publique remotamente.
- `EXP003_PORT` y `EXP003_DATA_DIR` son las únicas configuraciones de runtime.

## API

- `GET /api/health`
- `POST /api/session/start`
- `POST /api/session/:session_id/complete`
- `POST /api/session/:session_id/abort`

El mismo proceso sirve únicamente los recursos participantes permitidos: `index.html`, `pilot.css`, `experiment.js`, `public-deployment-manifest.json` y `media/*.wav`. Deniega el directorio `server/`, incluido el mapa privado.

## Contratos y políticas

Estados: `STARTED`, `COMPLETE`, `ABORTED`, `INVALID`, `DUPLICATE`.

La finalización exige una celda válida, 12 registros experimentales con posiciones `1..12`, IDs opacos exactos del manifest público, ratings enteros `1..7`, `playback_completed: true`, 2 prácticas y 1 diagnóstico. La respuesta repetida con payload idéntico es idempotente; otro payload para una sesión completa produce conflicto.

Refresh, abandono o fallo invalidan la sesión activa y no se fusionan con otra. Un restart crea otra `session_id` y conserva `restart_of`. Una segunda sesión completa del mismo ID sin restart autorizado se marca `DUPLICATE`, sin elegir según ratings o condición.

## Frontera de datos

El cliente recibe sólo `cell_id`, `serial_position`, `opaque_stimulus_id` y `opaque_audio_path` mediante `public-deployment-manifest.json`. El mapa científico offline está en `server/private-scientific-map.json` y no es servido por el backend.
