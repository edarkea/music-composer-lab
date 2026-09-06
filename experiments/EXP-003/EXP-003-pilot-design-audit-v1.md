# EXP-003 — Auditoría metodológica del diseño de piloto v1

## Outcome

**A — PILOT DESIGN READY FOR IMPLEMENTATION PREP**

La versión revisada queda lista para preparación de implementación, no para
ejecución. El asset freeze permanece intacto y el piloto sigue sin estar
autorizado.

## Base inmutable

- Asset manifest SHA-256: `9B23143B7EEE384E5454056F0617E22DD2242C85848CD62920C109ABB6DDA1F0`
- Pool: `CANONICAL_ASSET_POOL_FROZEN`
- Cambios en assets, WAV, MIDI, timing, gain, renderer o manifest: **NO**.

## Decisiones auditadas y revisiones aplicadas

### Constructo y wording

El wording recomendado conserva `perceived musical distance` como relación entre
R1 y R2. No lo define como similarity, smoothness, continuidad, liking,
calidad, consonancia, tensión o expectancy.

Wording final propuesto:

> ¿Qué tan grande te parece la distancia musical entre la primera y la segunda sonoridad?

Se admite una aclaración breve sobre cuánta separación se percibe, sin enseñar
una respuesta ni introducir un criterio musical alternativo.

Se añadió una pregunta abierta post-tarea para comprensión del constructo. Es
diagnóstica, no una rating secundaria ni un criterio de selección de
participantes.

### Escala

Se conserva una escala ordinal de 7 puntos. Solo se etiquetan los puntos 1, 4 y
7 para reducir carga semántica en categorías intermedias:

- 1: distancia musical muy pequeña
- 4: distancia musical intermedia
- 7: distancia musical muy grande

Los puntos 2, 3, 5 y 6 quedan sin etiqueta. No se usan good/bad,
smooth/rough ni similar/different.

### Replay y flujo

Se cambia la propuesta de replay opcional a **una sola presentación sin replay**.
La razón es fijar la exposición y evitar que repetir sea una variable endógena a
dificultad, incertidumbre o stimulus. El flujo es:

`ready/fixation → pre-play delay constante → WAV automático → respuesta → intervalo constante`.

La pregunta abierta aparece una sola vez al final.

### Assignment y orden

Se mantienen dos assignment lists complementarias, 12 trials por participante,
6 LOW y 6 HIGH, una condición por familia. Se separan explícitamente assignment
y trial order.

Se fijan tres secuencias de familias: O1 base, O2 inversa y O3 rotada. Las seis
celdas `A-O1`, `B-O1`, `A-O2`, `B-O2`, `A-O3`, `B-O3` se cubren una vez por
bloque de seis participantes. No hay orden adaptativo; cualquier permutación
de celdas debe predeclarar y registrar su semilla.

### Headphones, práctica y muestra

- Auriculares: **REQUIRED** para el piloto, registrando hardware y problemas.
- Volumen: comprobación común previa, sin modificar gain de assets.
- Práctica: dos trials no confirmatorios, fuera de las familias experimentales.
- Stage 1: **12 participantes**.
- Extensión máxima: **24**, solo si permanecen preguntas de usabilidad,
  comprensión, escala, playback, carga o variabilidad.
- Queda prohibida la extensión por dirección del efecto, p-value o diferencia
  LOW/HIGH.

## Pilot contract

- Primary outcome: rating ordinal 1–7.
- Primary predictor: condition LOW/HIGH.
- Candidate analysis: ordinal mixed-effects model con participante e item; la
  estructura de efectos aleatorios final queda abierta hasta observar
  factibilidad y varianza diagnóstica, y se decidirá mediante simulación sin
  seleccionar el modelo por significación favorable.
- Pilot data separate from confirmatory sample: **YES**.
- Secondary trial ratings: **NO**.
- Participant assets generated: **NO**.
- Pilot executed: **NO**.

## Exclusions and change rules

Se conservan únicamente exclusiones objetivas: sesión incompleta, fallo de
playback documentado, interrupción técnica, respuesta ausente/corrupta o
incumplimiento explícito de instrucciones básicas. No se añaden cutoffs de
reaction time, varianza o consistencia.

Después del piloto podrían revisarse wording, escala, instrucciones, interfaz,
timing de interfaz, replay, práctica y playback. No pueden cambiarse por la
dirección del resultado los assets, selección LOW/HIGH, pitches, timing, gain,
renderer o manifest.

## Consecuencia

- READY FOR IMPLEMENTATION PREP: **YES**.
- PILOT AUTHORIZED: **NO**.
- Gate E: permanece **PASS WITH SCOPE**.
- Esta auditoría no produce evidencia experimental ni conocimiento compositivo.
