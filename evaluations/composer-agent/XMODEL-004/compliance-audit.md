# XMODEL-004 — Auditoría de transferencia staged

## Veredicto

**D — XMODEL-004 EXECUTION INVALID**

Los dos modelos fallaron el gate de Stage 1 dentro del presupuesto de tres intentos. Además, la corrida no es válida como prueba de transferencia del brief y del paquete v1.1: el runner envió únicamente el texto de cada prompt; el brief se leyó para registrar su hash, pero no se incluyó en el mensaje enviado al modelo. Los prompts stage 1–3 enumeraban registros por nombre sin incluir su contenido. Por lo tanto, no se puede atribuir el resultado a la aplicación staged de la interfaz completa ni comparar causalmente contra XMODEL-003.

No se avanzó a Stage 2 ni Stage 3. No se generó MIDI ni se llamó music-engine.

## Condición y preservación

- Condición prevista: NO-EXAMPLE.
- Interfaz: composer-interface-v1.1.
- Brief local coincide byte por byte con XMODEL-003: SHA256 `464AE4378BCB7236F0FB36DA52EB65DCB03735197284E3A6899B8686D51EDE0B`.
- La igualdad del archivo local no significa que el brief se haya entregado al modelo; el manifiesto de captura muestra que solo se usó para hash.
- Todos los intentos de Stage 1, respuestas API crudas, salidas, hashes y diagnósticos se conservaron en carpetas exclusivas. Ningún intento se sobrescribió.
- Configuración usada por intento: `temperature 0`, `seed 41`, `top_p 1`, `top_k 40`, `repeat_penalty 1`, `num_ctx 32768`, `num_predict 4096`.
- No se modificaron Composer Knowledge, genre pack ni interfaz v1.1.

## Resultados por modelo

### Qwen3-14B

- **Stage 1:** FAIL, 3 intentos; bloqueado.
- **Stage 2:** NOT RUN.
- **Stage 3:** NOT RUN.
- **N3-P declarado:** FULL en intento 3, pero inválido como decisión aceptada: la base dice `RANK-1_AUTHORIZED` sin alcance/evidencia autorizados y no está completo el registro decisional requerido.
- **RANK no soportado:** 1 hallazgo explícito (`RANK-1_AUTHORIZED` no autorizado en N3-P). RANK-2: 0.
- **Atribuciones Owner falsas:** 0 expresas; sí atribuye al brief afirmaciones que no están allí (por ejemplo, vocal como narrativa primaria). Se registra como claim/fidelidad al brief, no como cita explícita del Owner.
- **Claims no soportados:** al menos 8 familias detectables: reglas de forma/ciclo, estructura 4/4, intercambio modal estilístico, jerarquía vocal, rango de tempo, percusión “étnica”, energía/cadencias y finales no resueltos.
- **SongPlanV2:** NOT PRODUCED.
- **Decisiones musicales del adaptador:** 0.
- **Final:** BLOCKED AT STAGE 1.

Evolución del gate: intento 1 carecía de `selected_option`, N3-P completo y bases válidas; intento 2 añadió selecciones, pero bases libres inválidas y N3-P incompleto; intento 3 usó enums estructurales, pero declaró RANK-1 sin autorización y no expresó AP de forma verificable. Los tres terminaron naturalmente (`done_reason: stop`).

### Ministral-3-14B

- **Stage 1:** FAIL, 3 intentos; bloqueado.
- **Stage 2:** NOT RUN.
- **Stage 3:** NOT RUN.
- **N3-P declarado:** FULL en intento 3, pero inválido: incluyó `superiority_claim: true`, contrariando el contrato, y el esquema global siguió incompleto.
- **RANK no soportado:** 0 claims de rank explícitos; RANK-2 no aparece. Las selecciones AP restantes no pasan gate por otros motivos.
- **Atribuciones Owner falsas:** 0 expresas. Sí inventa especificaciones y preferencias de brief, incluyendo “Neon Mirage”, synthwave, instrumentos, drops, tonalidades y un objetivo de performance en vivo; esto es invención de entrada, no atribución literal al Owner.
- **Claims no soportados:** al menos 10 familias: brief/título/género inventados, restricciones musicales inventadas, afirmaciones de convención de género, descarte por “genre mismatch”, afirmaciones de superioridad, atribuciones falsas a guardrails, ejemplo de canción no solicitado, claves/modos y objetivos de producción sin base.
- **SongPlanV2:** NOT PRODUCED.
- **Decisiones musicales del adaptador:** 0.
- **Final:** BLOCKED AT STAGE 1.

Evolución del gate: intento 1 era Markdown y contenía un brief completamente inventado; intento 2 terminó por longitud (`done_reason: length`); intento 3 volvió a incluir el brief inventado y Markdown, y mantuvo errores de estructura/AP y un claim de superioridad N3-P. No hubo más retries después del máximo permitido.

## Comparación con XMODEL-003

No asignar `IMPROVED / SAME / WORSE` como comparación experimental válida: XMODEL-004 no entregó a los modelos el brief ni el contenido de los registros v1.1. Solo cabe describir resultados observados bajo entradas incompletas:

- **Qwen:** no comparable; bloqueo explícito por RANK-1 no autorizado y AP incompleto tras tres intentos.
- **Ministral:** no comparable; inventó el brief, y el segundo intento además agotó el presupuesto.
- **Efecto principal observado:** la fragmentación por etapas no basta por sí sola; sin incluir de verdad las entradas declaradas y con gates solo documentales, no existe transferencia staged controlada que evaluar.

## Integridad metodológica y límites

La arquitectura ya aprobada requería que cada modelo recibiera brief, trace congelado y subconjunto de conocimiento apropiado. El runner actual acepta un único archivo de texto y no compone los recursos referenciados. El manifiesto XMODEL-004 registra los archivos esperados, pero no hashes de un paquete efectivo ensamblado por etapa ni evidencia de que dicho contenido entrara en la solicitud API. Los esquemas y gates preparados son descripciones YAML, no validadores ejecutables; por ello algunos diagnósticos fueron inspecciones mecánicas manuales y no una ejecución de gate autoritativa. No se empleó una reparación musical por software.

Los outputs son útiles como evidencia de que, con estos prompts incompletos, ambos modelos inventaron contenido y no cumplieron el contrato de Stage 1. No demuestran que la arquitectura staged funcione o falle cuando recibe sus entradas completas.

## Siguiente acción acotada

Corregir únicamente el ensamblado técnico de entradas y el gate mecánico —sin cambiar v1.1 ni conocimiento musical—, verificar por hash/log que brief y registros requeridos están dentro de cada solicitud, y preparar una nueva corrida prospectiva con nuevo ID. No reutilizar ni sobrescribir estos intentos de XMODEL-004.
