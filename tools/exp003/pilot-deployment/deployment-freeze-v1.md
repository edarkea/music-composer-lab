# EXP-003 — congelación técnica del dry-run de despliegue

## Estado

Resultado: **B — implementación local validada; requiere revisión antes del piloto**.

El dry-run local quedó validado para los seis cells operativos: `A-O1`, `A-O2`, `A-O3`, `B-O1`, `B-O2` y `B-O3`. No se reclutaron participantes, no se inició un piloto y no se produjo ningún registro humano.

## Alcance implementado

- Infraestructura participante en `tools/exp003/pilot-deployment/`.
- jsPsych fijado a `8.2.1`; plugins fijados a `2.1.0`.
- Preload obligatorio de 27 WAV; un fallo de preload impide continuar.
- Control de auriculares antes de la tarea.
- Control de volumen, dos prácticas y 12 trials experimentales por cell.
- Un solo playback por trial; los botones permanecen deshabilitados durante el audio.
- Pre-delay de 1000 ms e inter-trial delay de 1000 ms.
- Exportación estructurada con escala `1–7`, identificación opaca en la interfaz y referencias internas para auditoría técnica.

## Assets

- 24 copias opacas de los WAV canónicos, con hash idéntico al WAV de origen.
- 1 control de volumen: `media/volume-check.wav`.
- 2 prácticas: `media/practice-01.wav` y `media/practice-02.wav`.
- Mapa privado: `mapping.private.json`, 27 entradas.
- Manifest canónico verificado: 24/24 hashes coincidentes.

## Resultado del dry-run

Cada cell produjo 51 registros: 12 `EXPERIMENTAL`, 2 `PRACTICE` y los registros de control, interfaz y diagnóstico. Las seis ejecuciones terminaron correctamente y las 12 respuestas experimentales de cada ejecución fueron aceptadas solamente después de la reproducción.

## Fallos y recuperación

La interfaz rechaza un mapping inválido o incompleto y configura el preload para detenerse ante errores de audio. La ruta local no implementa persistencia de sesión ni deduplicación server-side: refresh, abandono y reenvío deben validarse en el proyecto Pavlovia configurado antes de autorizar datos reales.

## Pavlovia

La integración se dejó preparada conceptualmente, pero no se publicó ni se ejecutó contra Pavlovia porque este repositorio no contiene un proyecto, credenciales ni endpoint privado del Project Owner. Por ello no se declara `READY FOR STAGE-1 PILOT`.

## Integrity

- `EXP-003-asset-manifest-v1.yaml`: `9B23143B7EEE384E5454056F0617E22DD2242C85848CD62920C109ABB6DDA1F0`.
- Los WAV canónicos permanecen sin modificación; todos sus hashes siguen coincidiendo con el manifest.
- Los archivos de despliegue deben considerarse una build técnica congelada para revisión, no un paquete de publicación.

## Siguiente acción recomendada

Configurar un proyecto Pavlovia privado de prueba y repetir únicamente las validaciones de preload, exportación, refresh y deduplicación antes de solicitar la autorización del Director.
