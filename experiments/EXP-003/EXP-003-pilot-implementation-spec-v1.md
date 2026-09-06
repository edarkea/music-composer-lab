# EXP-003 — Especificación de implementación del piloto v1

## Estado

**A — IMPLEMENTATION SPEC READY; DEPLOYMENT DEPENDENCIES ONLY**

Esta especificación convierte el diseño de piloto auditado en tablas y reglas
implementables. No crea software, assets de participantes ni audio, y no
autoriza la ejecución.

Asset manifest congelado:
`9B23143B7EEE384E5454056F0617E22DD2242C85848CD62920C109ABB6DDA1F0`.

## Assignment lists

Cada participante recibe una condición por familia. Las listas son
complementarias y contienen exactamente 6 LOW y 6 HIGH.

| family | List A | List B |
|---|---|---|
| F01 | LOW | HIGH |
| F02 | HIGH | LOW |
| F03 | LOW | HIGH |
| F04 | LOW | HIGH |
| F05 | HIGH | LOW |
| F06 | HIGH | LOW |
| F07 | LOW | HIGH |
| F08 | HIGH | LOW |
| F09 | HIGH | LOW |
| F10 | HIGH | LOW |
| F11 | LOW | HIGH |
| F12 | LOW | HIGH |

## Order sequences

Cada secuencia contiene F01–F12 exactamente una vez.

- O1: `F03, F10, F01, F08, F12, F05, F07, F02, F11, F06, F04, F09`
- O2: `F09, F04, F06, F11, F02, F07, F05, F12, F08, F01, F10, F03`
- O3: `F08, F12, F05, F07, F02, F11, F06, F04, F09, F03, F10, F01`

LOW/HIGH alterna en cada lista a lo largo de cada orden.

## Six operational cells

Cada tabla expresa `position → family → condition`. Las seis celdas se cubren
en bloques balanceados de seis participantes.

### A × O1

| pos | family | condition |
|---:|---|---|
| 1 | F03 | LOW |
| 2 | F10 | HIGH |
| 3 | F01 | LOW |
| 4 | F08 | HIGH |
| 5 | F12 | LOW |
| 6 | F05 | HIGH |
| 7 | F07 | LOW |
| 8 | F02 | HIGH |
| 9 | F11 | LOW |
| 10 | F06 | HIGH |
| 11 | F04 | LOW |
| 12 | F09 | HIGH |

### A × O2

| pos | family | condition |
|---:|---|---|
| 1 | F09 | HIGH |
| 2 | F04 | LOW |
| 3 | F06 | HIGH |
| 4 | F11 | LOW |
| 5 | F02 | HIGH |
| 6 | F07 | LOW |
| 7 | F05 | HIGH |
| 8 | F12 | LOW |
| 9 | F08 | HIGH |
| 10 | F01 | LOW |
| 11 | F10 | HIGH |
| 12 | F03 | LOW |

### A × O3

| pos | family | condition |
|---:|---|---|
| 1 | F08 | HIGH |
| 2 | F12 | LOW |
| 3 | F05 | HIGH |
| 4 | F07 | LOW |
| 5 | F02 | HIGH |
| 6 | F11 | LOW |
| 7 | F06 | HIGH |
| 8 | F04 | LOW |
| 9 | F09 | HIGH |
| 10 | F03 | LOW |
| 11 | F10 | HIGH |
| 12 | F01 | LOW |

### B × O1

| pos | family | condition |
|---:|---|---|
| 1 | F03 | HIGH |
| 2 | F10 | LOW |
| 3 | F01 | HIGH |
| 4 | F08 | LOW |
| 5 | F12 | HIGH |
| 6 | F05 | LOW |
| 7 | F07 | HIGH |
| 8 | F02 | LOW |
| 9 | F11 | HIGH |
| 10 | F06 | LOW |
| 11 | F04 | HIGH |
| 12 | F09 | LOW |

### B × O2

| pos | family | condition |
|---:|---|---|
| 1 | F09 | LOW |
| 2 | F04 | HIGH |
| 3 | F06 | LOW |
| 4 | F11 | HIGH |
| 5 | F02 | LOW |
| 6 | F07 | HIGH |
| 7 | F05 | LOW |
| 8 | F12 | HIGH |
| 9 | F08 | LOW |
| 10 | F01 | HIGH |
| 11 | F10 | LOW |
| 12 | F03 | HIGH |

### B × O3

| pos | family | condition |
|---:|---|---|
| 1 | F08 | LOW |
| 2 | F12 | HIGH |
| 3 | F05 | LOW |
| 4 | F07 | HIGH |
| 5 | F02 | LOW |
| 6 | F11 | HIGH |
| 7 | F06 | LOW |
| 8 | F04 | HIGH |
| 9 | F09 | LOW |
| 10 | F03 | HIGH |
| 11 | F10 | LOW |
| 12 | F01 | HIGH |

## Balance audit

- Six cells: **YES**.
- Cada célula: 12 posiciones, 12 familias, 6 LOW y 6 HIGH.
- En cada posición serial, el par A/B del mismo orden contiene una LOW y una
  HIGH; por tanto las seis celdas producen 3 LOW y 3 HIGH por posición,
  incluidas posiciones 1 y 12.
- Las posiciones tempranas 1–6 y tardías 7–12 quedan balanceadas por la misma
  estructura A/B.
- Longitud máxima de racha de condición: 1, porque cada lista alterna LOW/HIGH.
- Acoplamiento familia–posición: reducido por O1 base, O2 inversa y O3 rotada;
  no hay una familia fija en una posición única.

Resultado: **PASS**, con la salvedad operativa de que el balance exacto por
celda requiere completar cada bloque de seis asignaciones.

## Participant allocation

- Stage 1, N=12: **2 participantes por cada una de las seis celdas**.
- Si se extiende a N=24: **4 participantes por cada celda en total**.
- La asignación se realiza por el calendario predeclarado de celdas; nunca por
  respuestas, ratings, dirección del efecto o consistencia individual.

## Opaque-ID contract

La provenance interna conserva `EXP003-F01-LOW` y sus hashes. La superficie
visible solo muestra un número de trial o un token opaco, por ejemplo:
`PILOT-<session_token>-TRIAL-01`.

La tabla privada de mapping relaciona:

`opaque_presentation_id → internal_asset_id → condition → asset SHA`.

El participante no recibe family ID, LOW/HIGH, motion, nombres técnicos ni
filename. No se crean copias ni presentation IDs en esta tarea.

## Exact state machine

```text
READY
  → pre-play delay: 1000 ms
  → automatic one-time WAV playback
  → playback complete
  → response enabled
  → one rating from 1..7
  → inter-trial delay: 1000 ms
  → next READY
```

No hay replay. El delay de 1000 ms es de interfaz y no altera el WAV. Si falta
respuesta, el sistema registra el estado; no debe inventar ni reparar el
rating.

## Exact participant text

> Escucharás pares de sonoridades, una después de la otra. Después de cada par,
> indica qué tan grande te parece la distancia musical entre la primera y la
> segunda sonoridad. No hay respuestas correctas o incorrectas. Usa cualquier
> punto de la escala que describa mejor lo que percibiste.

La pregunta por trial es:

> ¿Qué tan grande te parece la distancia musical entre la primera y la segunda sonoridad?

Escala:

- 1 — distancia musical muy pequeña
- 2 — sin etiqueta
- 3 — sin etiqueta
- 4 — distancia musical intermedia
- 5 — sin etiqueta
- 6 — sin etiqueta
- 7 — distancia musical muy grande

No se mencionan LOW/HIGH, movimiento, voice leading, smoothness, similarity ni
la hipótesis.

## Headphones and volume

- Headphones: **REQUIRED**, confirmado por el participante; no se inventa
  detección automática.
- Registrar tipo de auricular, dispositivo, navegador/app y problemas de
  reproducción.
- Procedimiento común: reproducir un material neutral de comprobación, pedir
  un nivel cómodo y confirmar que ambos canales se oyen claramente; no pedir
  SPL exacto ni modificar gain de ningún asset.
- **OPEN DEPLOYMENT DEPENDENCY:** no existe todavía un asset neutral de volumen
  aprobado. Debe resolverse durante preparación de despliegue, sin generarlo en
  esta tarea.

## Practice

Exactamente 2 trials de práctica, fuera de F01–F12, con la misma interfaz y
escala 1–7, sin feedback de corrección y excluidos del análisis. No deben
enseñar que mayor movimiento implica mayor distancia.

**OPEN DEPLOYMENT DEPENDENCY:** el audio de práctica todavía no existe; no se
crea aquí.

## Post-task diagnostic

Después de los 12 trials y de la última respuesta se registra un único campo de
texto libre:

> Con tus propias palabras, ¿qué entendiste por “distancia musical” al hacer esta tarea?

Es diagnóstico del piloto, no rating secundaria ni criterio de selección por
respuesta deseada.

## Response-log schema

Cada fila experimental requiere:

```text
participant_id
pilot_stage
assignment_list
order_sequence
serial_position
opaque_presentation_id
internal_family_id
condition
canonical_asset_sha256
canonical_asset_reference
rating
playback_started
playback_completed
technical_error
response_recorded
```

Timestamps pueden registrarse para diagnóstico operativo. Las filas de práctica
usan `record_type: PRACTICE` y la respuesta abierta usa
`record_type: CONSTRUCT_DIAGNOSTIC`; no se mezclan con las 12 filas
experimentales.

## Data integrity and exclusions

Una sesión completa requiere 12 filas experimentales, 12 familias únicas, 6
LOW, 6 HIGH, 12 ratings válidos 1–7, un playback completado y una respuesta por
trial, además de una de las seis celdas válidas. No se reparan silenciosamente
filas inválidas.

Solo se operacionalizan estas exclusiones: sesión incompleta, playback fallido
documentado, interrupción técnica, respuesta ausente/corrupta o incumplimiento
explícito y documentado de la tarea. No se excluye por velocidad, varianza,
dirección LOW/HIGH ni consistencia del efecto.

## Platform and dependencies

Plataforma de participantes seleccionada: **NO**.

Resultado de la inspección del repositorio: **PLATFORM NOT SELECTED**. No se
elige ni implementa una plataforma en esta fase.

Deployment dependencies abiertas:

1. seleccionar plataforma;
2. disponer de un asset neutral para volumen;
3. disponer de dos assets de práctica no confirmatorios;
4. implementar la tabla privada de opaque-ID mapping;
5. registrar la semilla o calendario de asignación por bloques.

Participant assets: **NO**. Pilot: **NO**.
