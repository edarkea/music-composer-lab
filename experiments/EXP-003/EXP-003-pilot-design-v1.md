# EXP-003 — Diseño de piloto perceptual v1

## Estado y alcance

Este documento prepara un piloto diagnóstico de diseño. No ejecuta el piloto,
no genera assets de participantes y no modifica el pool canónico congelado.

- Asset manifest: `experiments/EXP-003/EXP-003-asset-manifest-v1.yaml`
- Asset manifest SHA-256: `9B23143B7EEE384E5454056F0617E22DD2242C85848CD62920C109ABB6DDA1F0`
- Estado de assets: `CANONICAL_ASSET_POOL_FROZEN`
- Estado del piloto: `PREPARED_FOR_DESIGN_AUDIT`
- Pilot authorized: `NO`

El piloto no es una prueba de la hipótesis. Sus datos, si se obtienen, deben
etiquetarse `PILOT / DESIGN DIAGNOSTIC` y mantenerse separados de cualquier
muestra confirmatoria.

## Qué permanece congelado

- Las 24 combinaciones técnicas, sus pitches, condiciones y WAV.
- Timing, duración, gain, renderer, MIDI y manifiesto de assets.
- El estimando primario: política de selección `LOWER-MOTION-SELECTION`.
- El constructo objetivo: perceived musical distance entre R1 y R2.
- La arquitectura confirmatoria ordinal con condición como efecto fijo y
  estructura participante/item según resulte estimable.

## Qué se propone probar en el piloto

- Comprensión de la pregunta y de la escala.
- Uso efectivo del rango de respuestas y posibles efectos suelo/techo.
- Problemas de reproducción, auriculares, volumen e interfaz.
- Duración y carga de la sesión.
- Respuestas faltantes o imposibles de registrar.
- Variabilidad descriptiva suficiente para planificar la simulación posterior.

No se usará la dirección del efecto LOW/HIGH para aceptar, rechazar o modificar
los estímulos.

## Task wording

### Candidatos considerados

1. `¿Qué tan musicalmente distantes te suenan estas dos sonoridades?`
2. `¿Qué tan grande te parece la distancia musical entre la primera y la segunda sonoridad?`
3. `¿Qué tan diferentes te parecen la primera y la segunda sonoridad?`

El candidato 1 conserva bien el constructo, pero `distantes te suenan` puede
resultar menos natural para algunos oyentes. El candidato 3 es natural, pero
puede deslizarse hacia una valoración general de diferencia o similitud. Se
recomienda el candidato 2 porque nombra la relación entre R1 y R2, evita
preferencia y calidad, y no menciona movimiento, conducción de voces ni una
predicción.

### Wording primario propuesto

**¿Qué tan grande te parece la distancia musical entre la primera y la segunda sonoridad?**

La interfaz puede añadir una aclaración breve y neutral:

`Indica cuánta separación musical percibes entre ellas.`

No se explicará la respuesta mediante smoothness, continuidad, tensión,
similitud, gusto o calidad.

## Response scale

Se compararon conceptualmente escalas de 5 y 7 puntos. Cinco puntos reducen
carga y pueden ser suficientes para una tarea breve, pero ofrecen menos
resolución para separar juicios intermedios. Siete puntos ofrecen más espacio
ordinal sin convertir la respuesta en una medición continua; aumentan algo la
carga y exigen etiquetas claras.

Se propone una escala ordinal de **7 puntos**, con pocas etiquetas para no
introducir interpretaciones adicionales en las categorías intermedias:

| valor | etiqueta |
|---:|---|
| 1 | distancia musical muy pequeña |
| 2 | *(sin etiqueta)* |
| 3 | *(sin etiqueta)* |
| 4 | distancia musical intermedia |
| 5 | *(sin etiqueta)* |
| 6 | *(sin etiqueta)* |
| 7 | distancia musical muy grande |

Los extremos miden baja y alta distancia percibida. No dicen si una transición
es buena, agradable, suave, consonante o similar. La escala se tratará como
ordinal; no se definirá un umbral de aprobación ni se analizará como intervalo
por conveniencia.

## Diagnóstico post-tarea de comprensión

Se recomienda añadir una sola pregunta abierta, presentada después de todos los
trials y de la valoración final:

**Con tus propias palabras, ¿qué entendiste por “distancia musical” al hacer esta tarea?**

La respuesta se usará únicamente para diagnosticar comprensión, detectar
interpretaciones como similarity, smoothness o liking y decidir si el wording
necesita revisión. No será una variable dependiente por trial, no se usará para
seleccionar participantes según la respuesta deseada y no se empleará para
excluir retroactivamente respuestas favorables o desfavorables.

## Trial flow y exposición

Cada trial seguirá el mismo flujo:

1. pantalla de preparación/fijación;
2. pre-play delay breve y constante;
3. reproducción automática del WAV de 2,000 s;
4. habilitación de la respuesta al terminar la reproducción;
5. una única valoración de distancia;
6. intervalo constante antes del siguiente trial.

Se recomienda **una sola presentación, sin replay**. Esto fija la exposición y
evita que la decisión de repetir dependa de dificultad, incertidumbre o
características del estímulo. La menor oportunidad de inspección se considera
aceptable porque el estímulo dura 2 s y el objetivo del piloto incluye detectar
si la tarea es comprensible bajo una exposición estandarizada.

Los delays de interfaz no forman parte del timing del estímulo y serán iguales
para LOW y HIGH. El piloto puede informar si la repetición debe eliminarse o
mantenerse en una futura versión, sin cambiar los WAV.

## Exposición y counterbalancing

Cada participante recibirá **12 trials**, uno por familia, con 6 LOW y 6 HIGH.
No recibirá las dos condiciones de una misma familia.

Se proponen dos listas complementarias con el mismo orden de familias y
condiciones alternadas:

| posición | familia | Lista A | Lista B |
|---:|---|---|---|
| 1 | F03 | LOW | HIGH |
| 2 | F10 | HIGH | LOW |
| 3 | F01 | LOW | HIGH |
| 4 | F08 | HIGH | LOW |
| 5 | F12 | LOW | HIGH |
| 6 | F05 | HIGH | LOW |
| 7 | F07 | LOW | HIGH |
| 8 | F02 | HIGH | LOW |
| 9 | F11 | LOW | HIGH |
| 10 | F06 | HIGH | LOW |
| 11 | F04 | LOW | HIGH |
| 12 | F09 | HIGH | LOW |

Así cada posición tiene condiciones complementarias entre listas, cada lista
tiene 6 LOW/6 HIGH y no se crean rachas largas de una condición. La asignación
de participantes a listas deberá usar bloques permutados de tamaño par con una
semilla registrada cuando se implemente; no se asignará por respuestas.

### Trial-order sequences

La asignación de condición y el orden de trial son decisiones distintas. Las
tres secuencias predeclaradas de familias son:

- O1: `F03, F10, F01, F08, F12, F05, F07, F02, F11, F06, F04, F09`
- O2: `F09, F04, F06, F11, F02, F07, F05, F12, F08, F01, F10, F03`
- O3: `F08, F12, F05, F07, F02, F11, F06, F04, F09, F03, F10, F01`

O2 es la inversión de O1 y O3 es una rotación de O1. Así se evita que una
familia tenga siempre la misma posición y se distribuyen primeras y últimas
posiciones. Las condiciones LOW/HIGH siguen alternándose dentro de cada lista.

La unidad de asignación será una celda `assignment list × order sequence`.
Habrá seis celdas: `A-O1`, `B-O1`, `A-O2`, `B-O2`, `A-O3`, `B-O3`. Cada bloque
de seis participantes cubrirá una vez cada celda; el bloque se repetirá. La
selección de la siguiente celda será predeclarada y no dependerá de respuestas.
Si se usa permutación de las seis celdas, la semilla y la permutación deberán
registrarse antes de iniciar. No se usará randomización libre ni orden adaptativo.

Por tanto, el diseño tiene **2 assignment lists** y **3 order sequences**, con
**6 combinaciones operativas**. En cada bloque completo cada familia aparece en
ambas condiciones y cada secuencia tiene su par complementario.

## Blinding

La interfaz participante no mostrará `LOW_SELECTED`, `HIGH_SELECTED`, motion,
family IDs ni nombres técnicos. En esta fase no se crean copias ni IDs de
presentación. Una futura capa de despliegue deberá separar:

- identidad científica interna y provenance;
- `OPAQUE_PRESENTATION_ID` para la interfaz.

## Participant instructions

Texto propuesto:

> Escucharás pares de sonoridades, una después de la otra. Después de cada
> par, indica qué tan grande te parece la distancia musical entre la primera y
> la segunda. No hay respuestas correctas o incorrectas. Usa cualquier punto
> de la escala que describa mejor lo que percibiste.

No se mencionarán LOW/HIGH, movimiento, voice leading, spacing, continuidad,
smoothness, hipótesis ni resultado esperado.

## Practice

Se recomienda incluir **dos trials de práctica** antes de los 12 trials
experimentales. Deben usar pares técnicos no pertenecientes a las 12 familias
confirmatorias, con la misma pregunta y escala, y quedar excluidos del análisis.
No se generan assets de práctica en esta tarea. Si se reutilizara una familia
confirmatoria, habría que documentar explícitamente la consecuencia de
exposición antes de autorizar el piloto.

## Background and playback

La formación musical se recogerá solo como información descriptiva:
autoidentificación de experiencia, años aproximados de práctica cuando el
participante quiera responder, instrumento/voz principal y exposición habitual
a música. No será criterio principal de inclusión ni convertirá el estudio en
un estudio de expertos.

Se requieren auriculares para el piloto, preferentemente conectados y
sin ecualización o efectos especiales. Esto reduce variación de altavoces, pero
no hace idéntica la reproducción doméstica. Se registrarán dispositivo,
navegador o aplicación, tipo de auricular y cualquier incidencia de playback.

Antes de los trials habrá un procedimiento común de comprobación de volumen
con material no experimental. El participante elegirá un nivel cómodo y no se
alterará el gain individual de ningún WAV. No se normalizarán assets por
participante ni por condición.

## Pilot sample

El piloto comenzará con **Stage 1: 12 participantes**. Podrá extenderse hasta
un máximo de **24** únicamente si siguen sin resolverse preguntas de
comprensión, uso de escala, playback, interfaz, carga o variabilidad. La
extensión deberá registrarse antes de continuar.

No se permitirá extenderlo por la dirección del efecto, un p-value, una
diferencia media LOW/HIGH ni el deseo de obtener un efecto más fuerte. El piloto
puede detenerse para revisión si aparecen fallos técnicos repetidos, confusión
sistemática o una carga claramente impracticable.

## Objective exclusions

Se declararán antes de recoger datos:

- sesión incompleta;
- fallo documentado de reproducción;
- interrupción técnica explícita;
- respuesta ausente o imposible de asociar al trial;
- registro duplicado o corrupto;
- incumplimiento explícito de la instrucción básica tras documentarlo.

No se propone un cutoff arbitrario de velocidad, varianza, número de
repeticiones o uniformidad de respuestas. Los patrones de respuestas pueden
ser material de diagnóstico y no deben llamarse desatención sin criterio
predefinido y justificación independiente.

## What may change after the pilot

### Propuesto como mutable tras revisión

- wording;
- longitud o etiquetas de la escala si no se comprende o no se usa;
- delays e interfaz;
- política de repetición;
- instrucciones;
- procedimiento de playback.

### No puede cambiarse por un efecto débil o contrario

- pitches, condiciones y selección de familias;
- WAV, MIDI, timing, duración, gain y renderer;
- item freeze, render spec y asset manifest;
- el constructo primario o su sustitución por smoothness, continuidad,
  preferencia o calidad.

Solo un fallo técnico objetivo del asset congelado abriría una revisión técnica
separada; no se reparará un estímulo por su resultado perceptual.

## Confirmatory analysis and sample size

El piloto permanecerá separado. Su información podrá describir comprensión,
distribución de categorías, missingness y varianza, pero no se usará para
declarar apoyo a la hipótesis.

La planificación confirmatoria seguirá:

`pilot diagnóstico → distribución y varianza plausibles → simulaciones con efectos pequeños, nulos y heterogéneos → muestra confirmatoria → freeze de análisis`

El análisis primario seguirá siendo ordinal, con `MOTION CONDITION` como efecto
fijo y efectos de participante/item según la estructura y estimabilidad del
diseño. No se redefinirá éxito como una media o como la resta cruda de ratings.
El efecto direccional previsto permanece: LOW_SELECTED podría recibir menor
distancia percibida que HIGH_SELECTED, sin revelarlo al participante.

## Secondary ratings

**NO.** Se recogerá una sola valoración primaria de distancia. No se añadirán
liking, smoothness, continuidad, tensión, consonancia, confianza ni calidad,
porque aumentarían carga y podrían primar constructos distintos.

## Gate and authorization

- Diseño de piloto preparado: **YES**.
- Listo para auditoría de diseño: **YES**.
- Participant assets generados: **NO**.
- Pilot ejecutado: **NO**.
- Pilot autorizado: **NO**.

Este documento no produce nuevo conocimiento compositivo ni evidencia de
EXP-003.
