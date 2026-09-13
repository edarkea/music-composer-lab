# Composer MVP v1.1 ? Decisi?n expl?cita de arquitectura de percusi?n

## Estado y prop?sito

**Composer MVP v1.1 = la misma base de conocimiento de v1 + cobertura expl?cita de la decisi?n de arquitectura de percusi?n en una canci?n completa.** v1 permanece como la versi?n hist?rica que produjo SONG-001. Este documento es un delta arquitect?nico m?nimo; no reemplaza ni reescribe el decision contract v1 ni `composer-cross-domain-songplan-v1.md`.

La correcci?n responde a SONG-001: su flujo pudo marcar ritmo/groove como resuelto sin contestar si la canci?n tendr?a percusi?n, delegar?a el pulso a otras capas o la omitir?a deliberadamente. SONG-001-R1 a?adi? una decisi?n completa; el Project Owner la escuch? en REAPER y la acept?. Es una observaci?n de proceso y una preferencia art?stica para estas composiciones, no evidencia cient?fica.

## A. Observaci?n y localizaci?n

- `SONG-001` es el baseline hist?rico de Composer MVP v1 y permanece intacto.
- `SONG-001-R1` es la revisi?n controlada aceptada, tambi?n preservada.
- Hallazgo primario: **LF-001 ? Percussion architecture omission**. El original no ten?a una capa expl?cita ni una decisi?n trazada de arquitectura de percusi?n.
- La localizaci?n final es **CROSS-DOMAIN / GENRE-REALIZATION OMISSION**: el bundle de ritmo/groove no distingu?a resoluci?n r?tmica de resoluci?n de percusi?n.
- **GENUINE KNOWLEDGE GAP: NOT ESTABLISHED.** No se requiere investigaci?n o experimento nuevo.

El registro completo de escucha, incluidos LF-001?LF-012 y sus l?mites, est? en [`compositions/SONG-001/SONG-001-listening-review.md`](../../compositions/SONG-001/SONG-001-listening-review.md). El resultado de R1 consta en [`compositions/SONG-001-R1/SONG-001-R1-decision-trace.md`](../../compositions/SONG-001-R1/SONG-001-R1-decision-trace.md).

## B. Correcci?n arquitect?nica m?nima

Se conserva el grafo y el contrato fundamental de Composer Decision Contract v1 (objetivo, alcance, opciones, restricciones, base, selecci?n, preferencia, incertidumbre, dependencias, handoff y traza). Se extiende el **N3 ? Groove / harmony bundle** ya definido en `composer-cross-domain-songplan-v1.md` mediante una decisi?n dependiente:

### N3-P ? Percussion architecture

Despu?s de decidir el marco m?trico-r?tmico inicial de N3, el compositor debe responder expl?citamente:

> **?Cu?l es la arquitectura de percusi?n de esta canci?n?**

Esto es un punto obligatorio de cobertura de decisi?n, no una obligaci?n de seleccionar drums. Resolver metro, pulso, groove, soporte del bajo o persistencia/cambio **no** resuelve autom?ticamente N3-P. La composici?n no avanza al handoff song-level como completa mientras falte una respuesta expl?cita, incluso si la respuesta seleccionada es ausencia intencional.

No se introduce un dominio global, schema ni capacidad de ranking nuevos. N3-P usa `ENUMERATE`/`FILTER` cuando ayude a estructurar alternativas y `ARTISTIC PRIORITY` cuando m?s de una siga siendo v?lida; no tiene `RANK-1` ni selector autom?tico.

## C. Cobertura de decisi?n requerida

Cada traza N3-P registra, siguiendo los conceptos existentes del decision contract:

| Elemento | Pregunta / contenido m?nimo |
|---|---|
| Goal | ?Qu? funci?n debe cumplir o dejar de cumplir la percusi?n? |
| Scope/context | ?En qu? canci?n, estilo/realizaci?n, forma y condiciones de reproducci?n se decide? |
| Candidate strategies | ?Qu? arquitecturas plausibles se consideraron, incluida la ausencia cuando sea viable? |
| Constraints | ?Qu? material, jerarqu?a focal, densidad, coordinaci?n y l?mites t?cnicos deben respetarse? |
| General knowledge | ?Qu? conocimiento general existente aplica, y qu? no permite concluir? Puede indicarse que no hay un principio espec?fico que determine la opci?n. |
| Genre specialization | ?Qu? opciones hace disponibles o pondera el pack dentro de su alcance? ?Qu? pr?cticas no convierte en requisito? |
| Artistic priority | Si hay varias opciones v?lidas, ?qu? preferencia elige y qu? tradeoff acepta? |
| Selected architecture | ?Cu?l es la decisi?n para esta canci?n y, cuando proceda, por secci?n? |
| Cross-domain consequences | ?C?mo se coordina con groove, bajo, foco, diferenciaci?n seccional, trayectoria de energ?a, desarrollo y densidad de textura? |
| SongPlan handoff + trace | ?Qu? eventos/tracks/asignaciones expl?citos se serializan y d?nde se conserva el rationale? |

La traza distingue base general, entrada de g?nero, prioridad art?stica e input t?cnico. El mapeo de sonidos/pitches requerido por una biblioteca es dato de materializaci?n, no decide la funci?n r?tmica.

## D. Resultados permitidos

N3-P debe seleccionar y documentar una de estas clases de resultado (los r?tulos describen la decisi?n; no son juicios de calidad):

1. **FULL PERCUSSION** ? varias funciones/estratos expl?citos de percusi?n, con alcance y uso por secci?n decididos.
2. **MINIMAL PERCUSSION** ? una arquitectura deliberadamente limitada, cuya funci?n y suficiencia prevista se declaran.
3. **PULSE / PERCUSSIVE FUNCTION DELEGATED TO OTHER LAYERS** ? se identifican las capas que asumen cada funci?n pertinente y se explicita que no se serializar? una parte de drums independiente.
4. **INTENTIONALLY NO PERCUSSION** ? ausencia escogida de forma deliberada, con su intenci?n/contexto y consecuencias aceptadas.

No existe un default silencioso de ?sin percusi?n?, y ninguna categor?a es obligatoria para todas las canciones. Una selecci?n `none` o `delegated` tambi?n completa N3-P si est? decidida y trazada.

## E. Interfaz con g?nero y libertad art?stica

El pack de Indie-dance MVP puede influir en si ciertas opciones parecen estil?sticamente disponibles o ?tiles, y en su densidad, actividad y desarrollo por secci?n, siempre dentro del alcance del pack. La forma loop-based puede hacer pertinente preguntar por capas y trayectoria. Esto **no** equivale a ?indie-dance requires drums? ni a que la percusi?n garantice groove, energ?a, movimiento o identidad de g?nero.

Para la realizaci?n Indie-dance MVP, decidir ausencia sigue siendo leg?timo; debe aparecer como resultado intencional de N3-P y ser compatible con el brief art?stico. La aceptaci?n de R1 no convierte su patr?n en regla o default de futuras canciones.

## F. Dependencias cross-domain

N3-P es dependiente de la intenci?n song-level y del marco r?tmico de N3; se co-desarrolla o se filtra con decisiones vecinas:

- **Groove/metro ? percusi?n (`CO-DEVELOPMENT`):** la parte puede materializar, reforzar, contrastar o no a?adir una funci?n ya cubierta por otras capas. No se prescribe una f?rmula universal.
- **Bajo ? kick/otros eventos (`CONSTRAINT` o `CO-DEVELOPMENT` local):** revisar alineaci?n, anticipaci?n, solapamiento y duraci?n por contexto; no imponer un un?sono kick/bass ni prohibirlo.
- **Jerarqu?a focal ? actividad/acento (`CONSTRAINT`):** la densidad, el registro t?mbrico y la prominencia percusiva se filtran respecto del lead u otro foco declarado.
- **Forma/secciones ? entradas, salidas y cambios (`CONSTRAINT`):** decidir si la arquitectura permanece, se a?ade, se sustrae o cambia por funci?n.
- **Desarrollo N5 ? recurrencia de percusi?n (`CO-DEVELOPMENT`):** especificar qu? identidad r?tmica permanece, qu? cambia, d?nde y por qu?; no a?adir variaci?n por novedad sola.
- **Trayectoria N6 ? densidad de textura (`CONSTRAINT` / `REVISION TRIGGER`):** revisar si la actividad percusiva apoya el contorno deseado o compite con otras capas. La energ?a de SongPlan es metadato, no una automatizaci?n de din?mica.

Si una consecuencia revela conflicto, se reabre la decisi?n m?nima afectada seg?n el mecanismo de revisi?n v1 y se registra el cambio; no se revisan autom?ticamente melody, harmony o bass.

## G. SongPlanV2 handoff

SongPlanV2 ya representa tracks `drums` y `percussion`, motifs, eventos tipados, voces/instrumentos sem?nticos, asignaciones seccionales y mapas externos. SONG-001-R1 demuestra la representaci?n y materializaci?n usadas en este proyecto. Por tanto:

- **No hay cambio de SongPlan ni de `music-engine` en v1.1.**
- `FULL`/`MINIMAL` se handoffean como capas y eventos expl?citos que el formato existente admita, con cualquier mapa t?cnico requerido suministrado expl?citamente.
- `DELEGATED` se handoffea en los eventos expl?citos de las otras capas ya decididas y en la traza de N3-P; no se inventa una capa drums.
- `INTENTIONALLY NO PERCUSSION` puede producir un plan sin track percusivo, pero su decisi?n y raz?n quedan en la traza externa.
- El Composer decide la organizaci?n r?tmica; un mapa t?cnico suministrado decide solo correspondencias de materializaci?n. No inventar campos, mappings o valores que el usuario/runtime no haya fijado.

## H. No-claims y alcance

Esta revisi?n no introduce conocimiento compositivo, claims, clases de evidencia, estados de candidatos, reglas ni ranking. LF-001?LF-012 son observaciones de escucha del Owner; la aceptaci?n de R1 es **ARTISTIC PREFERENCE** aplicada a SONG-001. No demuestra causalidad, superioridad general, obligaci?n de g?nero ni transferibilidad a SONG-002. No se abre EXP ni se realiza investigaci?n nueva.

## I. Verificaci?n prospectiva con SONG-002

SONG-002 comprobar? la cobertura del flujo de manera prospectiva. Al compositor se le entrega el brief normal y la arquitectura v1.1; no se le recuerda manualmente ?agrega drums?. Antes de SongPlan, la traza debe mostrar N3-P completo: objetivo, alcance, alternativas consideradas, restricciones, bases general/g?nero, prioridad art?stica si aplica, opci?n elegida, impactos cross-domain y handoff. Se verifica que las cuatro salidas son posibles y que `none`/`delegated` no se convierten en fallos. El ?xito es una decisi?n expl?cita y reconstruible, no seleccionar percusi?n.

Esta especificaci?n **no autoriza componer SONG-002 ahora**.

## Estado de versiones

- **Composer MVP v1:** hist?rico; versi?n con la que se compuso SONG-001 y que dej? sin cobertura expl?cita la arquitectura de percusi?n.
- **Composer MVP v1.1:** listo para revisi?n del Music/Methodology Director y uso prospectivo en SONG-002; misma base de conocimiento y contrato, con N3-P a?adido como cobertura dependiente.
- **SONG-002 autorizado:** NO en esta tarea.
