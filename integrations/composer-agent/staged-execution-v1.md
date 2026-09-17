# Staged Third-Party Composer Execution v1

## Propósito

Este documento define una ejecución por etapas para modelos compositores externos. `datasets/composer-interface-v1.1/` permanece congelado. El modelo externo sigue siendo responsable de las decisiones musicales y del material; el software solo valida, diagnostica y bloquea cuando una condición mecánica no se cumple.

La ejecución separa tres responsabilidades:

1. **Stage 1 — Decision Planning:** producir únicamente un `DecisionTrace` completo.
2. **Stage 2 — Musical Material:** producir el material musical que realiza las decisiones aceptadas.
3. **Stage 3 — SongPlan Serialization:** serializar material congelado al contrato SongPlanV2.

Ninguna etapa posterior puede cambiar decisiones congeladas de una etapa anterior.

## Stage 1 — Decision Planning

### Entrada

- brief artístico de la corrida;
- registros de conocimiento general y genre pack que justifican decisiones activas;
- `decision-schema.yaml`;
- `guardrails.yaml` aplicables a decisiones;
- `completion-checklist.yaml` como lista de cobertura.

No se solicita SongPlan ni material completo. Se requieren FORM, SECTION ROLES, HARMONIC FRAMEWORK, FOCAL IDENTITY, LEAD/MOTIF STRATEGY, BASS ROLE, GROOVE, N3-P, TEXTURE, DEVELOPMENT, ENERGY/TENSION/RELEASE, ENDING y CROSS-DOMAIN DEPENDENCIES (registrado como `CROSS_DOMAIN_CONFLICTS` en la interfaz v1.1). Las alternativas deben seguir `ENUMERATE → FILTER → AP → SELECTION → CONTINUE` cuando corresponda.

### Gate 1

El gate calcula presencia, unicidad y estado de cada decisión; valida N3-P, RANK-2, RANK-1, atribución al Owner, AP y contradicciones de estado. No evalúa si una decisión artística es buena y no recomienda contenido musical.

## Stage 2 — Musical Material

### Entrada

- brief artístico;
- `DecisionTrace` aceptado e inmutable;
- solo los registros de conocimiento necesarios para realizar esas decisiones;
- guía de representación de material para la etapa posterior.

### Salida

Material musical estructurado: pitches, motivos, ritmos, voicings, eventos de bajo, percusión, textura, variaciones y material por sección, según las decisiones congeladas. Crear música está permitido; inventar reglas, evidencia o preferencias no lo está.

### Gate 2

Comprueba cobertura de secciones y capas implicadas, representación parseable, correspondencia de N3-P y ausencia de contradicciones con el trace. No juzga calidad melódica, no rankea alternativas y no reescribe material.

## Stage 3 — SongPlan Serialization

### Entrada

- `DecisionTrace` de Stage 1;
- material musical aceptado de Stage 2;
- `songplan-v2-contract.yaml` autoritativo.

### Salida

Un objeto SongPlanV2 que representa el material congelado. En esta etapa el modelo no reconsidera armonía, forma, motivos ni arquitectura N3-P.

### Gate 3

Valida esquema, raíz, secciones, referencias, motivos, eventos, pitches, voces de batería, consistencia de etiqueta armónica/voicing explícito y handoffs. No realiza reparación semántica. Los errores se devuelven al mismo modelo para un retry acotado.

## Gate y retry

Cada etapa permite como máximo dos retries correctivos. Un retry recibe únicamente la entrada original de la etapa, la salida previa y diagnósticos deterministas. No recibe coaching humano ni nuevas recomendaciones musicales. Si el gate sigue fallando, la corrida queda `BLOCKED`; nunca se avanza silenciosamente.

Cada intento conserva modelo, versión de interfaz, etapa, intento, hashes de entrada y brief, parámetros, respuesta API cruda, salida cruda y SHA256. Los intentos no se sobrescriben.

## Responsabilidad de guardrails

### Determinísticamente comprobable

Presencia de decisiones, ausencia de estados sin resolver, enums N3-P, prohibición de RANK-2, alcance de RANK-1, coincidencia de atribución Owner, AP estructural, formato SongPlanV2, referencias, pitches/eventos, operaciones permitidas, integridad de voicing cuando está representada mecánicamente y metadatos de captura.

### Razonado por el modelo

Calidad o adecuación de una elección artística, suficiencia perceptual de un objetivo blando y trade-offs musicales que no tienen una representación mecánica.

### Híbrido

Si sobreviven alternativas, el modelo debe explicar el trade-off y la intención AP; el gate comprueba campos, estados, ausencia de superioridad y coherencia con la entrada, pero no decide cuál opción es mejor. La frontera de claims requiere texto del modelo y comprobaciones mecánicas de atribución y alcance.

## Neutralidad y alcance

La arquitectura es neutral para `qwen3:14b`, `ministral-3:14b` y modelos futuros. Las diferencias de contexto o tokens son configuración técnica, no instrucciones musicales. Se suministra a cada etapa solo el subconjunto de v1.1 que necesita, y el manifiesto registra exactamente qué registros se enviaron.

## XMODEL-004

XMODEL-004 queda preparado, no ejecutado, con el mismo brief NO-EXAMPLE de XMODEL-001..003, la interfaz v1.1 sin cambios, los dos modelos, `num_ctx: 32768` y parámetros de muestreo iguales. La variable principal es únicamente `ONE-PASS → STAGED`.

El éxito exige, por modelo, PASS en los tres gates, SongPlanV2 válido, RANK no soportado igual a cero, atribución Owner falsa igual a cero, N3-P presente y cero reparación semántica del adaptador. Solo entonces se permite `READY FOR MUSIC-ENGINE`.
