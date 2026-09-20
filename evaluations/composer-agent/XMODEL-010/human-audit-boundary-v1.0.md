# XMODEL-010 - Limites de auditoria semantica humana

El gate determinista prueba JSON completo, claves unicas, contrato SongPlanV2, parseo y reglas implementadas por music-engine 4.0.0, y resolucion de host maps. No demuestra calidad compositiva ni todos los significados del material.

Despues de un PASS tecnico, una auditoria humana debe comprobar al menos:

- que el SongPlan conserva el material y las decisiones aceptadas de Stage 1/2;
- que las etiquetas armonicas declaradas describen de forma no enganosa las notas/voicings concretos;
- que cualquier `chromatic: true` esta respaldado por la decision congelada del compositor, no por reparacion del adaptador;
- que las afirmaciones de evidencia, RANK y atribucion al Owner respetan sus registros y alcances;
- que una asignacion `percussion` dispone de una PercussionMap aprobada por separado; si no, el gate host falla.

La auditoria humana solo acepta o rechaza/documenta discrepancias. No corrige pitches, armonia, instrumentacion ni decisiones musicales. No se materializa MIDI en XMODEL-010. La aceptacion humana y la escucha se mantienen como puertas posteriores, fuera del criterio automatico del experimento.
