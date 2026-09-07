# Composer MVP v1 — Full-Song Dry Run

## A. Purpose and limits

Este documento instancia una sola canción hipotética para auditar la
arquitectura de Composer MVP v1. No es la primera canción oficial del proyecto,
no es evidencia científica y no se renderiza. El material de notas del
SongPlan es desechable y existe únicamente para comprobar el handoff exacto a
SongPlanV2.

Entradas consumidas:

- `composer-decision-contract-v1.md`;
- `composer-knowledge-v1.md`;
- `composer-genre-pack-v1.md`;
- `composer-cross-domain-songplan-v1.md`;
- contrato SongPlanV2 y runtime lock de `music-engine`.

No se promovió conocimiento, no se abrió experimento y no se modificó
`music-engine`.

## B. Artistic brief — decided before SongPlan

**Brief hipotético:** canción instrumental de realización indie-dance
loop/groove-based, persistente y orientada al baile, con intensificación gradual,
una identidad focal claramente reconocible y contraste seccional contenido. La
melodía puede permanecer durante parte del ciclo; el cambio debe concentrarse
en una combinación controlada de capas, densidad, registro y textura. El final
debe liberar la densidad sin afirmar cierre armónico completo.

Este brief fija intención, no pitches, acordes, onsets ni instrumentación.

### Given by brief

- carácter persistente y dance-oriented;
- trayectoria de menor a mayor densidad y posterior release;
- prioridad de identidad focal;
- balance favorable a repetición, con cambio gradual;
- contraste moderado;
- escala corta de ocho compases para el dry-run.

### Composer may decide

- marco cíclico y secuencia mínima de secciones;
- representación explícita de identidad;
- metro, colocaciones y material simbólico;
- realizaciones armónicas compatibles;
- capas, roles y densidad relativa;
- operaciones de recurrencia y variación;
- valores técnicos requeridos por SongPlan.

### Hypothetical artistic priorities

1. Preferir un ciclo persistente frente a secciones contrastantes si ambos
   satisfacen la intención de continuidad.
2. Priorizar la identidad focal sobre la máxima novedad local.
3. Reducir competencia textural aunque ello limite una realización melódica más
   alta.
4. Preferir un final abierto/release frente a una clausura fuerte.

Son elecciones hipotéticas, no resultados de evidencia.

## C. Decision trace

### N0 — Intent and scope

- **Question:** ¿qué debe hacer la canción?
- **Goal/context:** persistencia bailable, intensificación gradual, foco claro,
  contraste contenido; instrumental, ocho compases, alcance indie-dance MVP.
- **Options:** persistencia con cambio de capas; contraste seccional más fuerte.
- **Constraints:** no inventar reglas de género; ningún campo SongPlan puede
  quedar como decisión musical sin base.
- **Knowledge:** CK-SONG-01 y contrato de decisión.
- **Capability/actionability:** `ENUMERATE + FILTER`; `ACTIONABLE WITH SCOPE`.
- **Filter:** ambas opciones son compatibles.
- **Selection:** prioridad artística 1 selecciona persistencia.
- **Consequence:** N1 debe mantener un marco recurrente y ubicar el cambio en
  otros dominios.

### N1 — Form and trajectory

- **Question:** ¿qué forma mínima realiza la intención?
- **Options:** (A) ciclo persistente con diferenciación de capas; (B) secciones
  contrastantes sobre loop-based framework.
- **General knowledge:** CK-FORM-01 permite declarar función y filtrar; no
  rankea formas.
- **Genre knowledge:** GP-04 y GP-02 hacen disponible cambio formal mediante
  capas, densidad, timbre, registro y retorno.
- **Capability:** `ENUMERATE + FILTER`; `ACTIONABLE WITH SCOPE`.
- **Filter:** A conserva mejor la prioridad de persistencia; B sobrevive como
  alternativa válida.
- **Artistic handoff:** se elige A porque la intención prioriza continuidad;
  bajo B habría mayor contraste explícito entre secciones.
- **Selected:** `opening → build → focal → release`, todas sobre marco cíclico.
- **SongPlan:** cuatro secciones de dos compases: `opening` 1–2, `build` 3–4,
  `focal` 5–6, `release` 7–8.
- **Uncertainty:** la percepción de secciones y release no se garantiza.

### N2 — Identity / focal bundle

- **Question:** ¿qué material debe permanecer reconocible y focal?
- **Options:** motivo estable; motivo con final cambiado; material nuevo en focal.
- **General knowledge:** CK-MEL-01/02 permite declarar una relación preservada y
  usar repetición/variación sin ranking global.
- **Genre knowledge:** GP-01 prioriza melodía cíclica sostenida cuando el cambio
  se traslada a realización.
- **Capability:** `ENUMERATE + FILTER`; `RANK-1` disponible solo para
  recognition, no aplicable todavía porque el objetivo del brief es identidad
  compositiva/foco, no la tarea experimental de reconocimiento.
- **Filter:** se retiene una figura melódica de cinco eventos y se conserva su
  contorno/relación inicial en `opening`, `build` y `focal`.
- **Artistic handoff:** se elige el motivo estable como prioridad de identidad;
  el final cambiado queda para `focal` y el material nuevo se descarta.
- **Selected:** lead recurrente; `lead_focal` cambia el último evento a `B4`.
- **Consequence:** el acompañamiento debe reducir competencia con la línea.
- **SongPlan:** `focal_lead` con motifs `lead_opening`, `lead_focal` y
  `lead_release`.

### N3 — Groove / harmony bundle

- **Question:** ¿qué marco rítmico-armónico sostiene la identidad?
- **Options:** ciclo armónico persistente; progresión dirigida; cambio de ciclo
  en focal.
- **General knowledge:** CK-HAR-01/02/03 y CK-RHY-01 permiten separar marco,
  realización y colocación; el cifrado no genera pitches.
- **Genre knowledge:** GP-02 permite considerar un marco cíclico; GP-05 deja
  anticipación como opción, no requisito.
- **Capability:** `ENUMERATE + FILTER`; no `RANK-1` ni `RANK-2`.
- **Filter:** se retiene un marco cíclico persistente, compás 4/4 y un patrón de
  bajo explícito con onsets alineados y anticipados.
- **Artistic handoff:** se elige persistencia frente a progresión dirigida para
  no desplazar el foco; la progresión permanece alternativa legítima.
- **Selected:** `cyclic_frame` como metadato de asignación; las sonoridades
  reales se escriben como pitches en `harmonic_support`.
- **SongPlan:** `time_signature: 4/4`, `harmony_assignments` por sección,
  voicings explícitos y `groove_bass` con `5/2` y `9/2`.
- **Uncertainty:** el ciclo no prueba coherencia percibida ni groove.

### N4 — Section-role / texture bundle

- **Question:** ¿cómo aumenta y reduce la textura sin competir con el foco?
- **Options:** añadir capa focal; aumentar densidad del acompañamiento; cambiar
  registro; combinar cambios moderados.
- **General knowledge:** CK-HAR-03 y CK-FORM-01/02 exigen tratar foco, estados y
  realización como decisiones separadas.
- **Genre knowledge:** GP-01/04/06 permiten trasladar diferenciación a capas,
  densidad y registro como haz, sin prescribir un parámetro único.
- **Capability:** `ENUMERATE + FILTER`; `ACTIONABLE WITH SCOPE`.
- **Filter:** una capa `focal_layer` entra en `build` y `focal`; el foco lead
  conserva el registro principal y el acompañamiento queda más bajo.
- **Artistic handoff:** se prioriza claridad focal sobre densidad máxima; no se
  añade otra capa en `release`.
- **Selected:** soporte armónico + bajo en todas las secciones; capa focal en
  build/focal; sin nuevas capas en release.
- **SongPlan:** cuatro tracks pitched con roles y assignments explícitos.
- **Uncertainty:** no se afirma que la densidad cause energía o contraste.

### N5 — Recurrence / development bundle

- **Question:** ¿qué permanece, qué cambia y por qué?
- **Options:** repetición exacta; cambio de final; cambio de capa/densidad;
  material nuevo.
- **General knowledge:** CK-DEV-01 permite declarar una relación preservada y
  filtrar operaciones compatibles; no rankea desarrollo.
- **Genre knowledge:** GP-01/02 priorizan cambio en otros dominios mientras el
  loop puede permanecer.
- **Capability:** `ENUMERATE + FILTER`; `ACTIONABLE WITH SCOPE`.
- **Filter:** se conserva el inicio del lead y el patrón de bajo; cambia el
  último evento en focal y se añade la capa focal desde build.
- **Artistic handoff:** se elige cambio parcial para mantener identidad y evitar
  novedad excesiva.
- **Selected:** `lead_opening` en opening/build; `lead_focal` en focal;
  `lead_release` reduce densidad y vuelve a E4.
- **SongPlan:** motifs separados y assignments; no se pide al motor inventar
  pitches.
- **Uncertainty:** parentesco y desarrollo perceptivo requieren escucha.

### N6 — Contrast / tension / closure bundle

- **Question:** ¿cómo se realiza intensificación, release y apertura?
- **Options:** más capas; mayor registro; cambio armónico; retirada de capas;
  parada marcada.
- **General knowledge:** CK-FORM-02 separa arrival, closure y boundary; tensión
  es multidimensional.
- **Genre knowledge:** GP-03/04 permiten frontera por arreglo/parada y cambio
  cross-domain; GP-06 trata registro como un marcador entre varios.
- **Capability:** `FILTER + DIAGNOSTIC ONLY`; no scalar.
- **Filter:** focal aumenta capas; release retira `focal_layer` y reduce
  velocidad/densidad del lead; no se afirma cierre armónico.
- **Selected:** `focal` como mayor densidad relativa; `release` como reducción y
  final no concluyente.
- **SongPlan:** energía de sección, assignments y eventos explícitos; estados
  perceptivos quedan en esta traza.
- **Uncertainty:** densidad, registro y retirada pueden contribuir, pero no
  garantizan tensión, energía o cierre.

### N7 — Conflict resolution and SongPlan handoff

- **Question:** ¿el plan puede serializarse sin esconder una decisión?
- **Conflict intentionally tested:** el registro alto que inicialmente se
  consideró para el focal competía con la jerarquía de `focal_lead` y con el
  espacio del soporte.
- **Protocol:** se detectó el conflicto; se identificó N4/N2; se priorizó la
  jerarquía focal; se reabrió solo la realización registral de `focal_layer`;
  se re-filtró y se mantuvo el lead como foco principal.
- **Revision:** `REV-001` conserva la alternativa alta, la causa y el resultado;
  no reinicia N0–N3.
- **Handoff:** todos los pitches, bars, beats, durations, velocities, motifs,
  tracks, assignments y secciones están resueltos antes de serializar.
- **Result:** SongPlan V2 preparado para validación; rationale y evidencia
  permanecen fuera del plan.

## D. Owner/composer decision ledger

| Decisión | Origen | Tipo |
|---|---|---|
| carácter persistente y trayectoria | brief | GIVEN BY BRIEF |
| forma A frente a B | intención de continuidad | ARTISTIC PRIORITY |
| marco cíclico | genre + intención | GENRE SPECIALIZATION + ARTISTIC PRIORITY |
| motivo y variación parcial | identidad focal | ARTISTIC PRIORITY con filtro general |
| metro y onsets | compatibilidad del plan | GENERAL KNOWLEDGE + TECHNICAL REALIZATION |
| layer solo desde build | pack + foco | GENRE PRIORITY + ARTISTIC PRIORITY |
| reducción en release | intención de release | ARTISTIC PRIORITY |
| registro de soporte revisado | conflicto N4/N2 | CROSS-DOMAIN CONSTRAINT |
| `schema_version: "2.0"` | runtime contract | TECHNICAL DEFAULT |
| beats y durations exactos | runtime contract | TECHNICAL DEFAULT / MATERIALIZATION |

## E. Diagnostic guardrail pass

| Guardrail | Resultado | Acción |
|---|---|---|
| cifrado ≠ sonoridad realizada | PASS | pitches explícitos en support |
| posición métrica ≠ prominencia | PASS | bajo coordinado, sin claim de prominencia |
| silencio/parada ≠ cierre automático | NOT APPLICABLE | no se usa una parada final |
| tónica/llegada ≠ cierre | PASS | final abierto descrito como intención, no hecho |
| recognition ≠ calidad/memorabilidad | PASS | RANK-1 no aplicado |
| menor movimiento ≠ mejor realización | PASS | no se rankean voicings por distancia |
| cambio aislado ≠ contraste percibido | PASS | contraste se trata como haz y queda incierto |
| retorno ≠ cadencia | PASS | `cyclic_frame`, no cadencia automática |

**Diagnostic guardrails:** 7 PASS / 0 WARNING / 1 NOT APPLICABLE. No hubo
warning que exigiera reabrir otra decisión.

## F. SongPlan handoff audit

### Authoritative artifact

`tools/composer-mvp-v1/full-song-dry-run.songplan.yaml`

El plan usa `schema_version: "2.0"` y solo campos presentes en el contrato
SongPlanV2 inspeccionado. El motor recibiría explicitamente pitches, onsets,
durations, velocities, tracks, motifs, assignments y secciones. Los símbolos
de armonía son metadatos y no sustituyen los eventos pitched.

### Backward audit

| Valor auditado | Pregunta “¿por qué está aquí?” | Resultado |
|---|---|---|
| cuatro secciones | intención persistente + opción formal A | PASS |
| lead focal y su retorno | prioridad de identidad + GP-01 | PASS |
| marco y voicings explícitos | N3 + contrato exact-specification | PASS |
| bajo con onsets anticipados | metro declarado + opción GP-05 acotada | PASS |
| layer desde build/focal | N4 + prioridad de claridad focal | PASS |
| lead focal con final cambiado | N5 + cambio parcial artístico | PASS |
| elección de ciclo sobre contraste fuerte | handoff artístico explícito | PASS |
| `schema_version: "2.0"` | default técnico del runtime | PASS |

**Backward trace audit: 8 / 8 PASS.**

## G. Unit-5 success test

1. Forma A/B y elección artística: **PASS**.
2. Prioridad de género sin ley universal: **PASS**.
3. Varias opciones armónicas y preferencia artística: **PASS**.
4. RANK-1 solo en criterio acotado: **PASS; no aplicado porque no correspondía**.
5. Conflicto de textura/registro y revisión melódica: **PASS**.
6. Foco sin claim de memorabilidad: **PASS**.
7. Tensión multidimensional: **PASS**.
8. Valores SongPlan con base upstream: **PASS**.
9. Defaults técnicos separados: **PASS**.
10. Decisiones completas resueltas, preferencia o default acotado: **PASS**.
11. Auditoría backward desde SongPlan: **PASS**.
12. Sin nueva investigación ni experimento: **PASS**.

**Resultado: 12 / 12 PASS.**

## H. Final readiness

- Artistic brief: **1 hipotético, completo y previo a decisiones**.
- Major decisions instantiated: **8 / 8**.
- Decision bundles instantiated: **4 / 4**.
- Artistic-priority handoffs used: **8**.
- RANK-1 decisions actually used: **0**.
- RANK-2 decisions used: **0**.
- Cross-domain conflict tested: **YES**.
- Revision protocol: **PASS**.
- Complete-song decisions: **RESOLVED / 16**.
- Unsupported decisions detected: **0**.
- Technical defaults clearly marked: **PASS**.
- New research needed: **NO**.
- New experiment needed: **NO**.
- P0 blockers remaining: **0**.

**COMPOSER MVP v1: READY** para revisión del Music/Methodology Director y del
Project Owner.

**FIRST ACTUAL SONG AUTHORIZED: NO.** La autorización requiere revisión
Director/Owner posterior a este dry-run. Este documento no constituye evidencia
de calidad artística ni autorización automática.
