# SONG-001 — Decision Trace

## Status and brief

SONG-001 es la primera composición real de Composer MVP v1, autorizada por el
Music/Methodology Director. Es instrumental, indie-dance MVP, con realización
loop/groove-based de electrónica-pop.

Brief: carácter orientado al baile, persistente, intensificación gradual,
identidad focal clara, contraste controlado, recurrencia reconocible con
desarrollo significativo y release final algo abierto.

Este documento registra decisiones antes de la materialización. No presenta la
composición como evidencia científica ni como validación de calidad musical.

## Decision ledger

### N0 — Intent and scope

- **Question:** ¿qué debe hacer la canción?
- **Options:** persistencia con cambio de realización; forma muy contrastante.
- **Filter:** ambas eran posibles; el brief prioriza persistencia gradual.
- **Selection:** `ARTISTIC PRIORITY`: carácter persistente, foco claro, contraste
  controlado y release abierto.
- **Basis:** brief artístico; no evidencia de superioridad global.
- **Consequence:** ciclo armónico persistente, cuatro funciones seccionales y
  cambio principalmente en capas, densidad, registro y variación melódica.

### N1 — Form and trajectory

- **Question:** ¿qué forma completa sirve a la intención?
- **Options:** (A) ciclo persistente con diferenciación de capas; (B) secciones
  contrastantes sobre marco loop-based.
- **General knowledge:** la función formal orienta objetivos pero no rankea una
  forma universal.
- **Genre specialization:** GP-04 permite diferenciar un marco cíclico mediante
  capas, densidad, timbre, registro y retorno.
- **Selection:** `ARTISTIC PRIORITY` selecciona A.
- **Architecture:** `opening` (1–4) → `build` (5–8) → `focal` (9–12) →
  `release` (13–16).
- **SongPlan:** cuatro sections de cuatro compases, energies 0.25/0.5/0.8/0.35.
- **Non-claim:** esta forma no es óptima universalmente ni garantiza secciones
  percibidas.

### N2 — Identity / focal bundle

- **Question:** ¿qué material será focal y qué relación debe permanecer?
- **Options:** figura descendente/ascendente estable; final cambiado; material
  nuevo en focal.
- **General knowledge:** CK-MEL-01/02 permite explicitar representación,
  recurrencia y variación; no garantiza memorabilidad.
- **Genre specialization:** GP-01 permite sostener melodía cíclica y desplazar
  el cambio a otros dominios.
- **Selection:** `ARTISTIC PRIORITY` elige una figura E4–G4–A4 con relación
  reconocible; el último gesto puede cambiar.
- **Material:** `lead_opening`, `lead_build`, `lead_focal`, `lead_release`.
- **Consequence:** `lead` es la capa focal; texture permanece por debajo.

### N3 — Groove / harmony bundle

- **Question:** ¿qué marco rítmico-armónico sostiene la recurrencia?
- **Options:** ciclo C–Am–F–G; progresión dirigida nueva; cambio armónico en
  focal.
- **General knowledge:** CK-HAR-01/02/03 exige separar selección y realización;
  CK-RHY-01 permite usar metro para filtrar colocaciones.
- **Genre specialization:** GP-02 hace disponible la persistencia cíclica; GP-05
  permite onsets anticipados solo con condiciones explícitas.
- **Selection:** `ARTISTIC PRIORITY` conserva el ciclo C–Am–F–G en todas las
  secciones para priorizar continuidad.
- **Realization:** armonía usa pitches explícitos; el bajo alterna raíz y quinta
  en posiciones a tiempo y anticipadas.
- **SongPlan:** harmony assignments son etiquetas; `harmony` y `bass` contienen
  la sonoridad real.
- **Non-claim:** el ciclo no garantiza groove, coherencia o ausencia de tensión.

### N4 — Section-role / texture bundle

- **Question:** ¿cómo crece la realización sin competir con el foco?
- **Options:** solo lead; añadir textura desde build; densificar el soporte;
  subir todo el registro.
- **General knowledge:** textura, foco y registro son decisiones relacionadas;
  un parámetro aislado no prueba contraste.
- **Genre specialization:** GP-01/04/06 favorecen cambios de capas/densidad como
  haz de realización.
- **Selection:** `ARTISTIC PRIORITY` añade `texture` desde build, lo mantiene en
  focal y lo retira en release; el soporte armónico permanece más bajo.
- **SongPlan:** track `texture` con role `focal_texture`, asignado solo a build y
  focal.

### N5 — Recurrence / development bundle

- **Question:** ¿qué permanece y qué cambia en cada recurrencia?
- **What remains:** relación inicial E4–G4–A4, ciclo armónico, patrón de bajo y
  foco del lead.
- **What changes:** build añade B4 al final; focal aumenta densidad y cambia el
  cierre a E4; release reduce actividad y deja G4 sostenido al final.
- **Why:** identidad persistente con desarrollo gradual y release abierto.
- **Knowledge:** CK-DEV-01 y GP-01; operaciones explícitas, sin umbral numérico
  de identidad.
- **Selection:** preferencia artística por cambio parcial en vez de material
  completamente nuevo.
- **SongPlan:** motifs separados; no se usa generación aleatoria ni se pide al
  motor inventar pitches.

### N6 — Contrast / tension / closure bundle

- **Question:** ¿cómo se realiza intensificación y release?
- **Dimensions:** densidad, continuidad/cambio, capas, registro y estados de
  apertura/cierre.
- **Selection:** focal recibe mayor densidad y textura; release retira textura,
  reduce velocidad y termina en G4 sostenido sobre el marco cíclico.
- **Basis:** brief + GP-03/04/06; `ARTISTIC PRIORITY` resuelve entre parada,
  final sostenido y retorno continuo.
- **Non-claim:** no se asigna scalar de tensión; G4 sostenido no se declara
  cierre percibido ni cadencia.

### N7 — Conflict resolution and handoff

- **Conflict:** en la primera realización, elevar `texture` al mismo registro que
  el lead focal reducía la jerarquía de foco.
- **Protocol:** detectado el conflicto; afectados N2 y N4; la prioridad dura de
  jerarquía focal prevalece; se reabrió solo la realización de `texture`; se
  re-filtró bajando sus voicings una octava; la alternativa alta fue descartada.
- **Revision:** `REV-001`, local, sin reiniciar la forma ni el material focal.
- **Handoff:** SongPlanV2 contiene secciones, tracks, motifs, assignments,
  pitches, onsets, durations y velocities explícitos.

## Owner versus composer

### Given by brief

Carácter, trayectoria, persistencia, foco, contraste controlado, desarrollo y
release abierto.

### Artistic priorities used

1. Forma A frente a B.
2. Ciclo C–Am–F–G persistente.
3. Figura focal estable con variación parcial.
4. Añadir texture en build/focal, no en opening/release.
5. Priorizar claridad focal ante registro alto de apoyo.
6. Mantener release abierto en lugar de cadencia enfática.
7. Usar material pitched-only para una primera materialización reproducible sin
   mapas externos.

En cada caso existían alternativas legítimas; el conocimiento no determinaba un
ganador global.

## Diagnostic guardrails before materialization

| Guardrail | Resultado | Revisión |
|---|---|---|
| Cifrado ≠ sonoridad realizada | PASS | voicings escritos explícitamente |
| Posición métrica ≠ prominencia | PASS | anticipaciones tratadas como colocaciones |
| Parada ≠ cierre automático | NOT APPLICABLE | no se usa parada final |
| Tónica/llegada ≠ cierre | PASS | final abierto es intención, no hecho perceptivo |
| Recognition ≠ memorabilidad/calidad | PASS | no se aplica RANK-1 |
| Movimiento mínimo ≠ mejor realización | PASS | no se rankean voicings por distancia |
| Cambio aislado ≠ contraste percibido | PASS | contraste es haz de capas/densidad/registro |
| Retorno ≠ cadencia | PASS | ciclo etiquetado como retorno, no cadencia |

**Resultado:** 7 PASS / 0 WARNING / 1 NOT APPLICABLE.

## SongPlan provenance

| Valor | Base upstream |
|---|---|
| `tempo: 122`, `4/4` | decisión musical + realización técnica explícita |
| `tonic: C`, `mode: ionian` | marco armónico elegido |
| `style: indie_dance_mvp` | etiqueta de género del brief/pack |
| sections y energies | forma y trayectoria decididas; energy es metadato |
| harmony assignments | referencia del ciclo; no genera notas |
| lead motifs | identidad, desarrollo y prioridad focal |
| harmony pitches | realización armónica explícita |
| bass pitches/onsets | groove y coordinación rítmica |
| texture assignments | decisión de capas y conflicto resuelto |
| `schema_version: "2.0"` | TECHNICAL DEFAULT del runtime |

## Materialization boundary

El plan fue validado con el ejecutable local del wheel de `music-engine` 4.0.0 y
posteriormente materializado a MIDI. El motor solo validó y materializó la
especificación explícita; no eligió notas, estilo, energía, armonía ni calidad.
No se generó WAV/audio.
