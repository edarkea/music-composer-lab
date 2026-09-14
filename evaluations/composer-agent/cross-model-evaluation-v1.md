# Protocolo de evaluación cross-model — Composer Interface v1

## Objetivo y límite

Comparar si distintos agentes externos pueden utilizar la misma interfaz derivada para producir decisiones completas, trazables y materializables bajo un mismo brief. Este protocolo evalúa cobertura, disciplina y cumplimiento de interfaz; no declara superioridad musical universal ni reemplaza el juicio del Project Owner.

SONG-005 queda reservado como primer test prospectivo de `composer-interface-v1`. **No se define aquí su brief ni se compone la canción.** El Owner debe aprobar un único brief y las preferencias abiertas antes de preparar corridas. Cada modelo recibe una copia idéntica del brief, manifest, conocimiento, genre pack, guardrails, decision-schema y contrato SongPlanV2. Se congela el hash/versión de cada paquete compartido.

## Preparación controlada

1. Seleccionar dos o más modelos/agentes independientes. Registrar identificador y versión reportados, fecha, parámetros disponibles y herramienta de ejecución; no incluir instrucciones específicas de proveedor.
2. Usar el mismo brief aprobado, el mismo `composer-interface-v1`, el mismo pack de género, guardrails, decision schema y especificación SongPlanV2 para todas las corridas.
3. Mantener iguales herramientas permitidas, presupuesto de salida y contexto disponible; registrar cualquier diferencia inevitable. No dar a un modelo feedback artístico o resultados de otro antes de congelar todas las salidas iniciales.
4. Iniciar cada agente en contexto limpio. Una salida bloqueada o handoff pendiente se conserva como resultado, no se completa retroactivamente con otra salida.
5. Guardar entradas, salidas crudas, hashes del paquete y validación en `evaluations/composer-agent/model-runs/`; crear el comparativo en `evaluations/composer-agent/comparative-audits/` después de las corridas.

## Dimensiones que se reportan por separado

No sumar en una puntuación global. Para cada dimensión usar `PASS`, `PARTIAL`, `FAIL` o `NOT_APPLICABLE`, con evidencia y referencias a salida:

| Dimensión | Criterio observable |
|---|---|
| Cobertura de decisiones | Decisiones principales del brief resueltas o explícitamente bloqueadas; traza previa a SongPlan. |
| Cumplimiento de alcance | No compone fuera del brief, no modifica conocimiento ni introduce investigación no autorizada. |
| Claims sin soporte | Contar y localizar claims musicales no soportados, generalizaciones y campos completados desde memoria. Cero es objetivo de cumplimiento. |
| Artistic Priority | Identifica supervivientes y transfiere elección al Owner cuando no hay ranking válido; no fabrica una preferencia. |
| Disciplina de ranking | Distingue enumerate/filter/rank; RANK-1 solo bajo CK-CROSS-01 y su tarea; RANK-2 no se inventa. |
| Guardrails | N3-P explícita; integridad etiqueta/voicing; separación estructura/percepción/composición; scope y proxies. WARNING debe detener ruta afectada. |
| Validez de SongPlan | Validador SongPlanV2 declara validez; registrar issues exactos. |
| Materializabilidad | El runtime de music-engine materializa el plan; registrar errores, recursos y correspondencia. |
| Coherencia cross-domain | Dependencias, tradeoffs y revisión mínima están documentados; revisión humana de traza, no score estético. |
| Escucha del Owner | El Owner escucha archivos con identificación de modelo oculta cuando sea viable y da aceptación/revisión por candidato; evaluación artística separada. |

La revisión de claims y trazas debe ser lo más ciega posible a identidad de modelo. Un validador estructural no evalúa calidad musical. La escucha del Owner no se convierte en ground truth general.

## Criterios de parada y registro

- Una discrepancia armónica sin explicación es `WARNING` y bloquea la decisión/handoff afectado hasta resolución explícita.
- Un SongPlan inválido no pasa a materialización/escucha como si fuera composición lista; se conserva la salida original y se registra el fallo.
- N3-P ausente o sin decisión explícita es fallo de cobertura de interfaz, no se rellena manualmente para rescatar la corrida.
- Decisión ambigua puede quedar en handoff al Owner; no se penaliza por no fingir ranking cuando la interfaz no lo sustenta.
- Ningún resultado único, incluso con aceptación del Owner, autoriza una afirmación de superioridad general o modificación de Composer Knowledge.

## Informe por corrida y comparación

Para cada modelo guardar: input/package hashes, output raw, DecisionTrace normalizada para inspección sin alterar contenido, estado de cada dimensión, eventos de bloqueos, validator/runtime y log de materialización. El informe cruzado presenta diferencias y coincidencias por dimensión y cita evidencia concreta. No producir leaderboard, promedio ponderado ni “ganador” global salvo que una evaluación futura autorice por separado un criterio operacional defendible.

## Estado

**Protocolo listo; evaluación no ejecutada.** No hay resultados de modelos externos, SongPlan de SONG-005 ni feedback de Owner derivados de este documento.
