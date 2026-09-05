# Composer Foundations v4

## Estado y alcance

Esta es una integracion conceptual de `Composer Foundations v3` con los dos
primeros resultados auditados de Fase 2. No es manual, regla, genero,
experimento, motor musical ni conocimiento aprobado.

Esta version no modifica v0, v1, v2 ni v3. Tampoco modifica RQs, candidatos,
fuentes ni integraciones de dominio. Los estados se heredan y se resumen para
razonamiento del compositor.

## Estado de fases

**GENERAL STRUCTURAL FOUNDATIONS - PHASE 1: PROVISIONALLY COMPLETE = YES**

Fase 2 esta **ACTIVE**. El cuello de botella dominante es:

**MOSTLY COMPARATIVE DECISION KNOWLEDGE**

Fase 1 ya permite generar material, representar variables, declarar metas
formales/locales, filtrar estructura y contexto, coordinar dominios, conservar
alternativas e identificar fronteras de ranking. Fase 2 pregunta cuando la
evidencia permite preferir una alternativa viable sobre otra para una meta y un
criterio declarados.

## Resultados auditados de Fase 2

### RQ-CROSS-001

`CAND-CROSS-001`:

- outcome: `REVISE`;
- readiness: `POSSIBLE_WITH_SCOPE`;
- type: `COMPARATIVE_DECISION_CONSTRAINT`.

La evidencia de phrase-boundary no justifica rankear final-event lengthening,
post-event silence, su combinacion o ninguno para `LOCAL MELODIC ARRIVAL`.
Su principal efecto es mejorar el filtrado de evidencia/inferencia, no la
enumeracion, el filtrado de opciones musicales ni el ranking general.

### RQ-CROSS-002

`CAND-CROSS-002`:

- outcome: `REVISE`;
- readiness: `POSSIBLE_WITH_SCOPE`;
- type: `CONSTRUCT_TRANSFER_CONSTRAINT`.

Boundary, completion y closure tienen tareas y resultados acotados, pero no
pueden usarse como proxies automaticos de `LOCAL ARRIVAL` sin justificar la
transferencia fuente-destino. `LOCAL ARRIVAL` sigue:

**NOT READY - ONLY ADJACENT MEASURES AVAILABLE**

No se identifico una operacionalizacion perceptiva directa estable. Esto no
demuestra que local arrival no pueda percibirse u operacionalizarse.

### Estado experimental

La comparacion lengthening/silence permanece `NOT JUSTIFIED` y `EXP-002`
permanece `PAUSED`. No se reabre la comparacion local-arrival por defecto.

## Arquitectura de conocimiento de Fase 2

La arquitectura distingue, sin crear un nuevo lifecycle de candidatos:

1. **STRUCTURAL KNOWLEDGE**: variables, organizaciones y operaciones que
   existen.
2. **DECISION-SPACE FILTERING KNOWLEDGE**: alternativas musicales que violan
   restricciones explicitas.
3. **GOAL INFORMATION**: funcion o efecto compositivo buscado.
4. **MEANS-END KNOWLEDGE**: operaciones que pueden servir a una meta.
5. **COMPARATIVE DECISION KNOWLEDGE**: bajo `GOAL G`, `CONTEXT S` y
   `CRITERION C`, evidencia que apoya A sobre B.
6. **COMPARATIVE DECISION CONSTRAINT**: evidencia X no justifica A > B para C.
7. **CONSTRUCT-TRANSFER CONSTRAINT**: el constructo medido X no puede ocupar
   automaticamente el lugar del objetivo compositivo Y.

## Tres filtros distintos

### 1. Musical-option filtering

Elimina alternativas que incumplen restricciones estructurales, formales,
metricas, temporales, cross-domain o de realizacion.

### 2. Evidence filtering

Elimina estudios o resultados que no sostienen la afirmacion que se quiere
hacer: por ejemplo, un estudio de completion no es automaticamente evidencia
de closure.

### 3. Inference / transfer filtering

Bloquea puentes no justificados:

```text
SOURCE CONSTRUCT X -> TARGET CONSTRUCT Y
OBSERVATION -> CAUSAL CLAIM -> COMPOSITION RULE
```

`CAND-CROSS-001` mejora principalmente el segundo filtro. `CAND-CROSS-002`
mejora principalmente el tercero. Ninguno reduce por si solo el espacio
musical de opciones.

## Funnel de razonamiento del compositor

```text
COMPOSITIONAL GOAL
        |
DECLARE TARGET EFFECT / CRITERION
        |
TARGET-CONSTRUCT CHECK
        |
OPERATIONALIZATION CHECK
        |
GENERATE CANDIDATE MEANS
        |
STRUCTURAL / FORMAL / RHYTHMIC / CROSS-DOMAIN FILTERING
        |
SURVIVING OPTIONS
        |
SOURCE-EVIDENCE CHECK
        |
SOURCE -> TARGET TRANSFER CHECK
        |
COMPARATIVE EVIDENCE CHECK
        |
RANK IF JUSTIFIED
        |
OTHERWISE: retain alternatives / artistic commitment /
refine criterion / further research
```

No es un pipeline determinista. Es un marco para detectar en que punto una
decision deja de estar respaldada.

## Construct-first frente a comparison-first

La heuristica de workflow queda:

- si el efecto objetivo es operacionalmente ambiguo: **CONSTRUCT-FIRST**;
- si el criterio ya tiene una operacionalizacion suficientemente estable:
  **COMPARISON-FIRST**.

Esto es **SUPPORTED AS PROJECT WORKFLOW HEURISTIC**, no una ley cientifica
universal. `RQ-CROSS-001` muestra el coste de comparar antes de validar el
constructo; `RQ-CROSS-002` proporciona la razon metodologica para comprobar
constructo y operacion antes de comparar.

### Antes y despues de RQ-CROSS-002

Antes:

```text
A vs B -> buscar evidencia perceptiva -> descubrir despues que el resultado
no coincide con la meta compositiva
```

Despues:

```text
GOAL -> TARGET CONSTRUCT -> OPERATIONALIZATION
     -> SOURCE -> TARGET TRANSFER -> COMPARISON
```

## Salvaguardas de ausencia de evidencia

```text
NO EVIDENCE THAT A > B
!= EVIDENCE THAT A = B

NO VALIDATED X -> Y TRANSFER
!= EVIDENCE X AND Y ARE UNRELATED

NO DIRECT OPERATIONALIZATION FOUND
!= CONSTRUCT CANNOT BE OPERATIONALIZED

ADJACENT CONSTRUCT
!= VALID PROXY

ANALYTICAL CONSTRUCT
!= PERCEPTUAL CONSTRUCT
!= EXPERIMENTAL OPERATIONALIZATION
!= COMPOSITIONAL GOAL
```

## Fronteras actuales de ranking

Se preservan cuatro fronteras:

1. **WITHIN-DOMAIN MATERIAL RANKING**: seed melodico A vs B, seed armonico
   A vs B.
2. **CROSS-DOMAIN PAIR RANKING**: M1+H1 frente a M1+H2 o M2+H1.
3. **TEMPORAL-PLACEMENT RANKING**: onset, duration, anticipation,
   synchronization y chord-change placement.
4. **REALIZATION RANKING**: bass, inversion, voicing, register y spacing.

Para cada frontera deben auditarse filtro actual, criterio potencial,
operacionalizacion, evidencia comparativa y bloqueo principal. Compatibilidad
no equivale a preferencia.

## Ranking-readiness matrix

| Decision | Goal | Candidate alternatives | Current FILTER power | Potential criterion | Criterion readiness | Known comparative evidence | Main blocker | Phase-2 readiness |
|---|---|---|---|---|---|---|---|---|
| initial melodic seed | establecer una idea | seeds con pitch/contour/rhythm distintos | `YES WITH SCOPE` | identidad, saliencia, estilo | baja/mixta | no ranking general | objetivo y estilo | `NEEDS CONSTRUCT-FIRST` |
| initial harmonic seed | organizar centro/proceso | dirigido, ciclico, persistente | `YES WITH SCOPE` | expectancy/tonal fit | parcial | no preferencia general | marco armonico | `NEEDS CONSTRUCT-FIRST` |
| Melody-Harmony pair | compatibilidad | M1+H1, M1+H2, M2+H1 | `CROSS-DOMAIN` | tonal fit/expectancy | parcial | no ranking integrado | definir fit sin colapsar realizacion | `NEEDS CONSTRUCT-FIRST` |
| repetition vs variation | establecer/continuar | repeticion exacta vs variacion | `YES WITH SCOPE` | reconocimiento/identidad | mejor desarrollada | evidencia parcial, no comparacion completa | tarea y alcance de identidad | `READY FOR COMPARISON-FIRST` |
| exact vs varied return | preservar recurrencia con cambio | retorno exacto vs cambiado | `YES WITH SCOPE` | reconocimiento de recurrencia | plausible y operable | evidencia de similitud/repeticion, no RQ especifica | separar identidad de novedad | `READY FOR COMPARISON-FIRST` |
| harmonic persistence vs change | continuidad o renovacion | mantener acorde vs cambiar | `YES WITH SCOPE` | expectancy, tension, continuidad | no estable general | asociaciones acotadas | goal y estilo | `NEEDS CONSTRUCT-FIRST` |
| onset placement | alineacion o desplazamiento | onset alineado vs anticipado | `GENRE-SCOPED` | grouping/expectancy | disponible con alcance | observacion popular, no ranking general | genre y metro | `TOO GENRE-DEPENDENT` |
| synchronization vs anticipation | coordinar Melody/Harmony | sync vs anticipation | `GENRE-SCOPED` | grouping/expectancy | parcial | no preferencia universal | estilo y funcion | `NEEDS CONSTRUCT-FIRST` |
| bass/inversion | realizacion tonal | root bass, inversion, otras | `YES WITH SCOPE` | tonal clarity/closure | dependiente de marco | no ranking general | armonia, estilo, textura | `NEEDS CONSTRUCT-FIRST` |
| voicing continuity | continuidad de realizacion | voice-leading alternatives | `YES WITH SCOPE` | connectedness/roughness | posible pero no consolidada | no comparacion integrada | criterio perceptivo y registro | `READY FOR COMPARISON-FIRST` |
| continuation operation | continuar material | fragmentacion, secuencia, repeticion | `PARTIAL` | continuation formal | baja fuera de marco clasico | asociacion clasica acotada | `FORM-003 NOT_READY` | `NEEDS CONSTRUCT-FIRST` |
| contrast operation | diferenciar | register, rhythm, harmony, texture | `UNCERTAIN` | perceived sectional contrast | baja | `FORM-006 NOT_READY` | multidimensionalidad | `NEEDS MORE STRUCTURAL KNOWLEDGE` |
| local arrival | punto local sin cierre | temporal, melodic, harmonic cues | diagnostico, no proxy | arrival judgment | no estable | no ranking | constructo no operacionalizado | `NEEDS CONSTRUCT-FIRST` |
| boundary | marcar agrupamiento | pausa, cambio, timing, texture | `YES WITH SCOPE` | boundary detection | disponible con escala | evidencia de segmentation | correspondencia compositiva | `READY FOR COMPARISON-FIRST` |
| closure | cerrar frase/seccion | cadence, melody, harmony, context | `YES WITH SCOPE` | closure/completeness rating | disponible por tipo | evidencia acotada | no escala unica | `NEEDS CONSTRUCT-FIRST` |

## Estado de la linea local-arrival

No debe continuar inmediatamente por inercia. Ya se emplearon dos RQs:

- `RQ-CROSS-001`: restriccion comparativa especifica;
- `RQ-CROSS-002`: restriccion de transferencia de constructos.

Una nueva RQ local-arrival solo tendria sentido si apareciera una nueva medida
directa y un nuevo leverage. El estado actual no satisface esas condiciones.

**Should local-arrival research continue immediately: NO.**

## Comparacion de posibles siguientes targets

| Target | Decision concreta | Criterion | Transfer risk | Leverage | Diagnosis |
|---|---|---|---|---|---|
| exact vs varied return | decidir como retornar una idea | recognition/recurrence identity | medio y auditable | alto: within-domain ranking | mejor candidato actual |
| Melody-Harmony pair | elegir pares compatibles | tonal fit/expectancy | medio-alto | alto | necesita construct-first |
| temporal alignment vs anticipation | colocar eventos coordinados | grouping/expectancy | medio, genre-dependent | medio-alto | demasiado dependiente de estilo |
| voicing/voice-leading | elegir realizacion | continuity/connectedness | medio | alto | criterio posible, pero deuda experimental/comparativa mayor |
| continuation operation | continuar bajo funcion formal | formal continuation | alto | medio | `FORM-003 NOT_READY` |
| contrast operation | crear contraste | perceived contrast | alto | alto | `FORM-006 NOT_READY`, multidimensional |
| boundary | elegir medios para segmentacion | boundary detection | bajo-medio | medio | mejor literatura, leverage compositivo menos claro |
| completion/closure | hacer terminar/completar | completion/closure rating | medio | medio | evitar estudiar una medida sin decision |
| genre-specific RQ | ranking dentro de estilo | criterion de estilo | variable | variable | especializacion prematura |

## Siguiente target elegido

**Exact return vs varied return**.

La elección no afirma que el retorno exacto sea superior. Se elige porque
conecta con una frontera real de material melódico, aprovecha evidencia
existente sobre repeticion/similitud, permite un conjunto pequeño de opciones
y tiene menor riesgo de constructo que local arrival.

### Research target specification

**GOAL:** preservar la identidad perceptible de una idea al retornar, permitiendo
  decidir si la variacion sirve mejor a una meta adicional de continuidad.

**CONTEXT:** retorno de una idea melodica dentro de una unidad de frase o
  seccion declarada, con estilo y tarea de reconocimiento especificados; no
  generalizar automaticamente a retorno seccional o a todas las tradiciones.

**OPTIONS:**

- A: retorno exacto;
- B: retorno variado con cambios declarados y parentesco conservado.

**CRITERION:** reconocimiento de que el material posterior es la misma idea o
  una recurrencia relacionada, medido con una tarea de identidad/similitud
  declarada y separado de agrado, novedad o calidad.

**WHY THIS CRITERION:** la literatura previa del dominio Melody ya distingue
  reconocimiento/similitud de preferencia y ofrece variables de identidad; por
  eso es un criterio más concreto que “lo que suena mejor”.

**SOURCE -> TARGET RISK:** reconocimiento en fragmentos o tareas de similitud
  no equivale automaticamente a identidad formal de retorno en una cancion. La
  tarea, familiaridad, intervalo, ritmo, registro, armonia y escala formal
  deben auditarse antes de rankear.

**EXPECTED CAPABILITY GAIN:** potencialmente `FILTER -> RANK` en la frontera
  `WITHIN-DOMAIN MATERIAL RANKING`; inicialmente puede producir solo filtro si
  las alternativas o el criterio no quedan separables.

No se inicia esta RQ en v4.

## Preferencia frente a función

Fase 2 debe distinguir:

- **FUNCTIONAL CRITERION:** A sirve mejor a la meta G.
- **PERCEPTUAL CRITERION:** A produce más/menos efecto medido X.
- **STYLE CRITERION:** A caracteriza mejor el género S.
- **ARTISTIC PREFERENCE:** el compositor prefiere A.

Solo los tres primeros pueden producir ranking basado en evidencia bajo
alcance; la preferencia artística sigue siendo legítima y no es un defecto de
investigación.

## Composer manual readiness

**YES, provisionalmente.** v4 fortalece una arquitectura posible:

1. `STRUCTURAL DECISION SPACE`;
2. `FILTERING`;
3. `COMPARATIVE DECISION REASONING`;
4. `WHEN EVIDENCE DOES NOT JUSTIFY RANKING`.

No se modifica `manual/` y readiness no equivale a promoción.

## Rule readiness

**NO.** Un structural validator, composition heuristic, comparative heuristic
o evidence constraint no se convierte automaticamente en regla machine-
readable.

## Estado de Fase 2

- `RQ-CROSS-001` -> `PARTIALLY` -> specific comparative constraint.
- `RQ-CROSS-002` -> `YES` -> construct-transfer constraint y heuristica
  construct-first de proyecto.
- Positive `A > B` knowledge: ninguno todavía.

Esto no significa que Fase 2 falle. Significa que ha mejorado el diagnóstico
de cuándo un ranking sería válido.

## Experiment policy

No se diseña experimento. La línea local-arrival permanece `NOT JUSTIFIED`.
El siguiente objetivo recomendado debe comenzar con investigación, seguida de
auditoría de candidato; la elegibilidad experimental se evaluará después.

## Candidate coverage

Se preservan:

- `CAND-CROSS-001`: `REVISE`, `POSSIBLE_WITH_SCOPE`,
  `COMPARATIVE_DECISION_CONSTRAINT`;
- `CAND-CROSS-002`: `REVISE`, `POSSIBLE_WITH_SCOPE`,
  `CONSTRUCT_TRANSFER_CONSTRAINT`;
- next Cross-domain candidate: `CAND-CROSS-003`.

No se modifican candidatos existentes.

## Recommended next action

Investigar `exact return vs varied return` con el objetivo, contexto,
alternativas y criterio especificados arriba; no comenzar automáticamente esa
RQ desde este documento.
