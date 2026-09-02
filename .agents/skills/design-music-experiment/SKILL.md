---

name: design-music-experiment
description: Convierte una hipótesis de composición musical en un experimento controlado, falsable y evaluable, separando variables, condiciones, candidatos, métricas, sesgos y límites de inferencia. Usar cuando una hipótesis musical necesite ponerse a prueba mediante comparación de ejemplos.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Design Music Experiment

## Objetivo

Diseñar experimentos que ayuden a descubrir si una hipótesis compositiva tiene utilidad y bajo qué condiciones.

Los experimentos NO existen para demostrar que las reglas del proyecto son correctas.

Deben poder producir resultados que contradigan nuestras expectativas.

Seguir `AGENTS.md` y `PROJECT.md`.

## Antes de diseñar

Identificar claramente:

1. qué afirmación queremos comprobar;
2. qué variable compositiva está implicada;
3. qué efecto creemos que puede producir;
4. qué variables alternativas podrían explicar el resultado;
5. qué podremos y qué NO podremos concluir del experimento.

Si la hipótesis es demasiado vaga, reformularla antes de continuar.

## Hipótesis

Preferir formulaciones comparables.

Evitar:

> La repetición mejora las melodías.

Preferir algo similar a:

> Bajo estas condiciones, conservar X entre dos apariciones de un motivo podría aumentar la percepción de parentesco frente a modificar simultáneamente X e Y.

No utilizar esta formulación como plantilla rígida.

## Variables

### Independent Variable

Debe indicar qué elemento cambia deliberadamente.

Intentar modificar una variable principal cada vez.

### Controlled Variables

Mantener constantes todos los factores razonablemente relevantes.

Ejemplos según el experimento:

* tempo;
* armonía;
* instrumentación;
* dinámica;
* duración;
* registro;
* rhythm;
* starting pitch;
* phrase length;
* contexto estructural.

No declarar una variable controlada si realmente cambia entre candidatos.

### Dependent Measures

Definir qué observaremos.

Ejemplos:

* reconocimiento;
* preferencia;
* continuidad;
* tensión percibida;
* sensación de cierre;
* memorabilidad.

No utilizar una palabra subjetiva sin intentar definir qué significa en el experimento.

## Candidates

Crear candidatos suficientemente comparables.

Cuando resulte útil incluir:

* baseline;
* condición experimental;
* alternativa;
* control negativo;
* caso límite.

No hacer deliberadamente peor una condición para favorecer la hipótesis.

## Aislamiento

Antes de aprobar el diseño preguntar:

> Si A gana a B, ¿sabremos realmente qué diferencia causó el resultado?

Si la respuesta es no, reducir variables o reconocer explícitamente la limitación.

## Evaluación humana

El Project Owner debe poder escuchar sin necesidad de conocer qué versión representa la hipótesis preferida cuando sea práctico.

Considerar:

* orden aleatorio;
* identificadores neutrales;
* escucha repetida;
* comparación por pares;
* separación entre preferencia y característica evaluada.

Ejemplo:

No confundir:

> ¿Cuál te gusta más?

con:

> ¿Cuál percibes como más relacionada con la frase anterior?

Son preguntas distintas.

## Sesgos

Considerar:

* order effect;
* loudness bias;
* novelty bias;
* expectation bias;
* familiarity;
* confirmation bias;
* fatigue.

No fingir que podemos eliminar completamente estos sesgos.

Intentar reducirlos.

## Métricas

No crear una escala 0–10 automáticamente.

Elegir la forma de evaluación que mejor responda a la pregunta:

* elección A/B;
* ranking;
* escala ordinal;
* descripción cualitativa;
* recall;
* reconocimiento;
* evaluación multidimensional.

Si se utiliza una escala numérica, definir claramente qué significan sus extremos.

## Repetición

Un único resultado no demuestra una regla general.

Cuando sea relevante, probar:

* distintos materiales;
* distintas tonalidades;
* diferentes registros;
* diferentes tempi;
* otros géneros;
* otros oyentes.

No introducir todas estas variaciones en el primer experimento si destruyen el control.

Utilizarlas posteriormente como pruebas de generalización.

## Formato del experimento

# EXP-XXX — [Título]

## Question

Pregunta específica.

## Background

Por qué merece estudiarse.

## Hypothesis

Predicción y razonamiento.

## Falsification Condition

Qué resultado debilitaría la hipótesis.

## Independent Variable

Variable modificada.

## Controlled Variables

Variables constantes.

## Candidates

Descripción neutral de cada versión.

## Generation Procedure

Cómo producir candidatos comparables.

## Evaluation

Qué debe escuchar o juzgar el evaluador.

## Bias Controls

Medidas utilizadas para reducir sesgo.

## Results

Dejar vacío antes de realizar la prueba.

## Interpretation

Dejar vacío antes de obtener resultados.

## Limitations

Qué no podrá demostrar el experimento.

## Confidence

No asignar antes de obtener resultados.

## Follow-up

Dejar para después de interpretar los resultados.

## Reglas

No rellenar resultados antes de realizar el experimento.

No declarar como confirmada una hipótesis basándose únicamente en que el Project Owner prefiera un candidato.

Preferencia y mecanismo perceptivo pueden ser variables distintas.

No generalizar un resultado más allá de las condiciones probadas.
