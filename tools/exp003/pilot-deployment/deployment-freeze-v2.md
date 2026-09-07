# Deployment freeze v2 — EXP-003

## Estado

**CONGELADO PARA REVISIÓN TÉCNICA**

La validación remota T8 terminó en PASS. Este freeze no autoriza participantes reales ni publicación científica.

## Superficie validada

- Persistencia remota recuperada desde el volumen persistente de Railway.
- Snapshot remoto conservado sin modificaciones.
- Exportación realizada con el `server/export.js` existente.
- CSV técnico generado con 180 filas.
- Join científico ejecutado offline, fuera del backend.
- Reconstrucción completa de las 72 filas experimentales de las seis sesiones técnicas objetivo.
- Hash T1 conocido verificado.

## Límites del freeze

- No se añadió API.
- No se añadió código de backend.
- No se ejecutó análisis de efectos científicos.
- No participaron personas reales.
- El mapa privado no se expone al participante ni al backend de exportación.
- El CSV técnico no debe mezclarse con datos de participantes reales ni con análisis científico.

## Artefactos congelados

- `server/export.js`
- `remote-technical-sessions.json`
- `remote-technical-export.csv`
- `server/private-scientific-map.json`
- `backend-remote-validation-v2.md`

## Decisión

La build puede considerarse técnicamente validada para revisión humana del flujo remoto y del join offline. Cualquier autorización de piloto requiere una decisión posterior del Project Owner y del Music/Methodology Director.

