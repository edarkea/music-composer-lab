# Composer Foundations v3

## Estado y alcance

Integracion conceptual de `Composer Foundations v2` con el resultado auditado
de `RQ-CROSS-001`. No es manual, regla, genero, experimento, motor musical
ni conocimiento aprobado. No modifica v0, v1 ni v2; los estados de RQ y
candidatos se heredan.

Se integra `CAND-CROSS-001` como `REVISE / POSSIBLE_WITH_SCOPE /
COMPARATIVE_DECISION_CONSTRAINT`. La RQ conserva `SYNTHESIZED`,
`candidate_audit_status: COMPLETED`, `candidate_audit_evidence_gate: PASS` y
experiment gate `NOT JUSTIFIED`.

## Delta v2 -> v3

v2 identificaba un cuello de botella principalmente comparativo. v3 añade una
comprobacion previa: antes de usar una fuente para rankear opciones, hay que
verificar que su constructo medido coincide con el efecto compositivo buscado.

`RQ-CROSS-001` no reduce materialmente el espacio de opciones ni produce una
preferencia temporal. Mejora la identificacion de inferencias no justificadas.

## Estado de Fase 1

**GENERAL STRUCTURAL FOUNDATIONS - PHASE 1: PROVISIONALLY COMPLETE = YES**

Es un cierre de gestion de fase, no una promocion epistemica. El diagnostico
de Fase 2 sigue siendo **MOSTLY COMPARATIVE**.

## Arquitectura de conocimiento de Fase 2

Composer Foundations distingue conceptualmente:

1. **STRUCTURAL KNOWLEDGE**: variables, organizaciones y operaciones existentes.
2. **FILTERING KNOWLEDGE**: opciones que violan restricciones declaradas.
3. **GOAL INFORMATION**: funcion compositiva buscada.
4. **MEANS-END KNOWLEDGE**: operaciones que pueden servir a un objetivo.
5. **COMPARATIVE DECISION KNOWLEDGE**: bajo objetivo, alcance y criterio,
   evidencia que apoya A sobre B.
6. **COMPARATIVE DECISION CONSTRAINT**: evidencia que no justifica rankear A
   sobre B para un criterio concreto.

Esto es una arquitectura de razonamiento, no un nuevo lifecycle de candidatos.

### Decision-space filtering != evidence / inference filtering

**Decision-space filtering** elimina opciones musicales porque violan
restricciones estructurales, formales, cross-domain o contextuales.

**Evidence / inference filtering** elimina razones no justificadas para
preferir o rechazar opciones que siguen siendo musicalmente posibles.

`CAND-CROSS-001` mejora principalmente `EVIDENCE / INFERENCE FILTERING`. No
debe presentarse como una reduccion material de opciones musicales.

## Integracion de CAND-CROSS-001

La evidencia inspeccionada relaciona pausa o silencio, duracion del tono final
y contexto armonico con procesamiento relacionado con `phrase boundaries` en
estudios acotados. Los factores estan parcialmente confundidos; las tareas no
miden directamente `LOCAL MELODIC ARRIVAL`; `boundary != local arrival`; y
`local arrival != full closure`.

No se establece ventaja independiente de `lengthening`, ventaja independiente
de `silence` ni ventaja comparativa de su combinacion. Por tanto, la evidencia
de phrase-boundary por si sola no permite rankear `lengthening`, `silence`,
ambos o ninguno para `LOCAL MELODIC ARRIVAL`.

Esto no demuestra `lengthening = silence` ni que ninguno afecte local arrival.
Demuestra que la evidencia inspeccionada no licencia esa comparacion.

| Capacidad | Resultado | Lectura |
|---|---|---|
| espacio musical / `ENUMERATE` | NO MATERIAL CHANGE | las alternativas ya eran representables |
| filtrar opciones musicales | NO / LITTLE MATERIAL CHANGE | no se elimina un medio por si mismo |
| filtrar justificaciones | IMPROVES | bloquea transferencia no establecida |
| `RANK` | DOES NOT IMPROVE | no hay preferencia comparativa válida |

## Auditoria de transferencia

Antes de usar evidencia para una eleccion:

```text
SOURCE CONSTRUCT -> TARGET COMPOSITION CONSTRUCT
```

Deben comprobarse constructo, poblacion, repertorio/estilo, tarea, contexto
estructural, nivel formal y resultado perceptivo frente a analitico.

En esta RQ:

```text
phrase-boundary processing / segmentation -> local melodic arrival
                                      = NOT ESTABLISHED
```

No se construye una puntuacion numerica de transferencia.

## Positivo frente a constraint en Fase 2

El conocimiento comparativo positivo tiene la forma:

```text
GOAL G + CONTEXT S + A vs B + CRITERION C
        -> evidence supports preferring A or B
```

El conocimiento negativo o de constraint muestra que una comparacion o
transferencia concreta no esta licenciada. Solo es valioso como resultado de
Fase 2 si bloquea una inferencia compositiva plausible pero invalida. Eso es lo
que hace `CAND-CROSS-001`; “no sabemos” por si solo no basta.

## Por que RQ-CROSS-001 no rankeo

- **Target-construct instability:** `local arrival` no tiene una
  operacionalizacion unica y directamente emparejada.
- **Source -> target transfer failure:** boundary processing no equivale a
  arrival.
- **Factor confounding:** duracion, silencio y armonia no siempre fueron
  aislados independientemente.
- **Comparative design absent:** no hubo ranking directo entre lengthening,
  silence y combinacion.
- **Scope limitation:** common-practice, Mozart, bebes y tareas
  experimentales no se convierten silenciosamente en reglas populares.

## Structure -> perception -> composition en Fase 2

Fase 1 protege:

```text
STRUCTURE -> PERCEPTION -> COMPOSITION
```

Fase 2 añade:

```text
MEASURED PERCEPTUAL CONSTRUCT X -> INTENDED COMPOSITIONAL EFFECT Y
```

La segunda flecha requiere comprobacion propia. Por ejemplo,
`boundary detection != arrival judgment` y `completion != closure`.

## Funnel decisional actualizado

```text
ARTISTIC / FORMAL GOAL
 -> GENERATE
 -> STRUCTURAL FILTER
 -> FORMAL FILTER
 -> METRIC / TEMPORAL FILTER
 -> CROSS-DOMAIN FILTER
 -> REALIZATION FILTER
 -> SURVIVING MUSICAL OPTIONS
 -> EVIDENCE TRANSFER CHECK
 -> COMPARATIVE EVIDENCE CHECK
 -> RANK IF JUSTIFIED
 -> OTHERWISE ARTISTIC COMMITMENT / FURTHER RESEARCH
```

No es un pipeline determinista; el compositor puede volver a una etapa
anterior. Los dos checks nuevos filtran razones, no obligan a una unica
secuencia compositiva.

## Ranking frontiers

Se conservan las cuatro fronteras de v2:

1. ranking de seeds dentro de un dominio;
2. ranking de pares Melody-Harmony;
3. ranking de colocacion temporal;
4. ranking de realizacion.

Se añade una pregunta ortogonal: **¿tenemos evidencia valida para el criterio
que se esta usando?** Una frontera puede fallar porque la evidencia mide un
constructo adyacente, no solo porque no existan estudios.

## Capacidad heredada y nueva

Se preserva la capacidad de generar Melody/Harmony seeds, filtrar estructura,
forma, metro, timing y cross-domain, separar seleccion de realizacion,
conservar alternativas y distinguir fronteras de ranking.

Fase 2 añade auditar si la evidencia mide el efecto deseado, rechazar
transferencias invalidas y distinguir `NO EVIDENCE THAT A > B` de `EVIDENCE
THAT A = B`.

## Puerta de experimento

Un hueco de ranking no basta. Antes de un experimento se requieren: decision
precisa, alternativas independientemente manipulables, efecto operacionalizado,
constructos fuente/destino emparejados, confounds controlables, literatura no
concluyente y una posible alteracion de una eleccion compositiva real.

`RQ-CROSS-001` permanece `NOT JUSTIFIED` principalmente porque `LOCAL
ARRIVAL` no esta suficientemente resuelto como constructo operacional. No se
diseña experimento y `EXP-002` permanece intacto.

## Progreso de Fase 2

No debe medirse por cantidad de candidatos ni por resultados A>B. Debe
examinar si una RQ produce preferencia acotada, constraint, refinamiento del
constructo, hueco preciso, elegibilidad experimental o diagnostico de una
comparacion mal formulada.

`RQ-CROSS-001` logro principalmente **B + D**, y parcialmente **C**.

## Readiness

### Composer manual readiness

**YES, provisionalmente.** La metodologia fortalece la preparacion conceptual
del manual al exigir coincidencia entre constructo medido y efecto compositivo.
No se modifica `manual/`; readiness no equivale a promocion.

### Rule readiness

**NO.** “No inferir ranking de arrival desde evidencia de boundary” es una
guarda epistemica contextual, no una regla machine-readable de composicion.
No se modifica `rules/`.

## Cobertura

Se conserva la cobertura de v2: Melody `CAND-MEL-001`--`036`, Harmony
`CAND-HAR-001`--`059`, Form `CAND-FORM-001`--`008` y Rhythm
`CAND-RHY-001`--`009`, con sus estados heredados. Se agrega solamente la
referencia integrada `CAND-CROSS-001: POSSIBLE_WITH_SCOPE`, comparative
decision constraint. No se reauditan candidatos ni se crea `CAND-CROSS-002`.

## Siguiente objetivo

### Comparacion breve

- **Target-construct clarification:** prerequisito de alta utilidad; riesgo de
  prolongar una linea sin criterio estable.
- **Otra RQ means -> effect:** potencial FILTER -> RANK alto si ya tiene
  criterio operativo; riesgo de repetir el error de constructo.
- **Volver a lengthening/silence:** bajo valor mientras arrival siga inestable.
- **Arrangement/texture:** utilidad media, con alto riesgo genre-specific.
- **Genre-specific means-end:** potencial alto localmente, pero especializacion
  prematura.

### Recomendacion única

**TARGET-CONSTRUCT CLARIFICATION.** Pregunta precisa:

> ¿Como se han operacionalizado empiricamente `local arrival`, `boundary`,
> `completion` y `closure` en tareas musicales distinguibles, y bajo que
> contextos puede un criterio de `local arrival` emparejarse validamente con
> una decision compositiva sin sustituirlo por boundary detection,
> completion o full closure?

No se inicia esta investigacion en v3. Solo despues se decide si regresar a
lengthening/silence o abrir otra RQ means -> effect.
