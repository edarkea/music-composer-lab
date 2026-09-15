# Cambios de composer-interface-v1 a v1.1

Esta revisión se limita a fallos observados en XMODEL-001. No cambia Composer
Knowledge, el pack de género, ni el contrato canónico del motor. Los archivos
exportados de conocimiento y género se conservan como copias derivadas del v1.

| Cambio | Fallo que atiende |
|---|---|
| Prioridad artística permite elegir y continuar; handoff al Owner solo con reserva explícita | Ambos modelos interpretaron mal la subdeterminación; Qwen inventó resolución del Owner y Ministral exigió intervención por defecto. |
| Límite entre generación musical e invención de conocimiento, más prohibición de justificar efectos sin soporte | Ambos outputs añadieron claims perceptivos/causales; Ministral añadió hechos de repertorio/género y preferencias no provistos. |
| Disciplina RANK-1/RANK-2 serializada y sin ámbito autodeclarado | Qwen inventó ranking de tempo y RANK-2. |
| Regla de atribución del Owner limitada a decisión exacta en la entrada actual | Ambos outputs atribuyeron decisiones/preferencias no recibidas. |
| Checklist obligatorio de 14 decisiones y puerta READY | Ambos omitieron cobertura; Qwen declaró READY con decisiones faltantes. |
| N3-P requiere registro completo explícito y no puede inferirse de eventos/ausencia | Ambos outputs omitieron arquitectura y sus interacciones. |
| Cada guardrail tiene propósito, activación, PASS, WARNING, BLOCK y no-significado; GR-011 limitado a etiqueta/pitches | Ambos marcaron guardrails PASS sin evidencia; Ministral aplicó GR-011 a una cuestión modal. |
| Contrato SongPlanV2 con raíz exacta y estructura de tracks/eventos | Qwen emitió estructura genérica; Ministral no produjo plan V2 extraíble. |
| Envolvente JSON estricta con puerta de completitud | Las salidas no cumplieron contrato o contradijeron sus propios estados. |
| Se excluyó del paquete de prueba la tabla de casos SONG-002..004 del registro N3-P | Ministral hizo referencia a canciones/datos del Owner no suministrados durante la condición NO-EXAMPLE; se conserva el criterio de arquitectura sin alimentar casos previos. |

Condición de transferencia: NO-EXAMPLE. Ningún ejemplo SONG-001..004 se incluye
en el prompt XMODEL-002. El fixture estructural no se usa.
