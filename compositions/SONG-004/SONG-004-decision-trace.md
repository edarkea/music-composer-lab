# SONG-004 — Traza de decisiones de composición

## Estado y autoridad

SONG-004 fue compuesta después de la aprobación explícita del Project Owner de los tres handoffs del plan: marco de tiempo/forma, identidad/armonía/foco y arquitectura N3-P DELEGATED. Esta traza registra las decisiones realizadas y conserva su base. No se inicia investigación, ranking, cambio de Composer Knowledge ni cambio de arquitectura.

El motor se usó como materializador determinista de la especificación, no como generador musical. El resultado es una composición simbólica en MIDI; no se produjo audio y no se ha registrado aún una escucha o aceptación artística final.

## N0 — Intención y alcance

- **Brief:** pieza instrumental indie-dance/electrónica-pop, contenida, cinética y ligeramente tensa; movimiento sin intensificación continua; idea recurrente con desarrollo entre capas; cierre deliberado.
- **Alcance aprobado:** 116 BPM, 4/4, 28 compases, Re menor/Re eólico, patrón armónico sincopado como foco, bajo de apoyo, lead espaciado y N3-P DELEGATED.
- **Límite:** no se fijaron preset, biblioteca de sonidos ni cualidades de audio.

## N1 — Forma y trayectoria

- **Decisión aprobada:** A (compases 1–8) → B (9–16) → A' (17–24) → coda (25–28).
- **Trayectoria realizada:** establecimiento, expansión moderada, retorno transformado y simplificación/cierre. Las energías del SongPlan son valores relativos de metadato; no generan automatización dinámica.
- **No-claim:** la curva describe el diseño simbólico y no garantiza una curva perceptiva.

## N2 — Identidad, motivo y jerarquía focal

- **Foco aprobado:** patrón armónico sincopado en registro medio, realizado en la pista pitched pattern.
- **Motivo nuevo:** célula de ataques armónicos cortos en posiciones 1&, 2& y 4 para A. Se conservó el marco de ataques pero B lo desplazó a 1, 2& y 4&; A' mantuvo la referencia con el ataque intermedio omitido en barras alternas; la coda redujo aún más la célula.
- **Lead:** respuestas melódicas breves en notas explícitas del marco Re eólico, con densidad baja frente al patrón.
- **Base:** prioridad artística autorizada por el brief y handoff del Owner; pitches y ataques concretos se decidieron durante la composición. No se reclama memorabilidad demostrada ni se aplicó RANK-1.

## N3 — Armonía, groove y bajo

### Armonía

- **Decisión aprobada:** Re menor/Re eólico.
- **Paleta:** D minor, Bb major, C major y G minor.
- **Recorrido:** A = Dm–Dm–Bb–Bb–C–C–Gm–Gm; B = Bb–Bb–C–C–Gm–Gm–Dm–Dm; A' retorna al orden de A; coda mantiene D minor.
- **Realización explícita en harmony:** D minor = D3/F3/A3; Bb major = Bb2/D3/F3; C major = C3/E3/G3; G minor = G2/Bb2/D3. Una sonoridad por compás, con el mismo acorde en los dos compases de cada región armónica.
- **Integridad:** cada pitch set coincide exactamente con el label correspondiente en las 28 barras. No hay omisiones, adiciones, inversiones ni extensiones que requieran semántica de alcance.

### N3-P — Arquitectura de percusión

- **Decisión prospectiva aprobada:** **PULSE / PERCUSSIVE FUNCTION DELEGATED TO OTHER LAYERS (DELEGATED)**.
- Se consideraron FULL, MINIMAL, DELEGATED e INTENTIONALLY NONE como clases disponibles; la preferencia aprobada eligió DELEGATED.
- No hay pista drums/percussion independiente. El patrón focal aporta subdivisiones/ataques sincopados y el bajo articula los tiempos 1 y 3 durante A, B y A'. La coda conserva anclajes de bajo y reduce el patrón.
- **Cobertura:** N3-P queda explícita antes del handoff a SongPlan; no hubo recordatorio manual para añadir drums.
- **Límite de escucha:** la distribución escrita conserva referencias métricas en las secciones, pero la claridad perceptiva del pulso requiere la escucha del Owner; no se afirma aceptación auditiva.

### Bajo

- Bajo sintético de apoyo, en registro grave; alterna raíz en beat 1 y quinta en beat 3 durante A, B y buena parte de A'.
- En B la quinta aparece en beat 3&, y A' reduce ataques en barras alternas. En la coda el bajo sostiene D y reduce movimiento.
- La relación con el patrón evita duplicar todos sus ataques. No se infiere que esta organización sea superior de forma general.

## N4 — Capas y textura

- **pattern:** ataques de acordes triádicos en registro medio; rol rítmico-focal y parte de la función percusiva delegada.
- **harmony:** acordes explícitos sostenidos por compás como soporte armónico.
- **bass:** raíces/quintas y anclaje del pulso.
- **lead:** frases breves de respuesta.
- La coda reduce el número de ataques de pattern y lead y simplifica el bajo, dejando la sonoridad D minor como cierre.

## N5 — Recurrencia y desarrollo

Permanece reconocible la función rítmica sincopada del pattern. Cambian posiciones de ataque y omisiones por sección; el marco armónico rota en B y retorna en A'; el lead ofrece respuestas espaciadas. La coda cita la célula de forma reducida antes del final. Estas son operaciones estructurales elegidas para esta pieza, no una regla sobre desarrollo.

## N6 — Contraste, release y cierre

- B amplía la interacción de capas sin prescribir un crescendo continuo.
- A' recupera el ciclo y reduce algunos ataques intermedios del pattern.
- La coda reduce la actividad y termina con D minor y D en el bajo; las notas finales alcanzan el límite de la sección y del plan.
- No se denomina cadencia funcional ni se afirma que la llegada produzca por sí sola cierre perceptivo.

## N7 — Conflictos, handoffs y guardrails

- **Handoffs artísticos previos:** 3 paquetes aprobados por el Project Owner antes de la composición.
- **Handoffs nuevos durante la composición:** 0. Las alturas, ritmos, voicings y distribución de eventos se eligieron dentro de la autorización explícita para componer según el plan.
- **RANK-1:** 0. **RANK-2:** 0.
- **Conflictos que requirieron reabrir una decisión:** 0.
- **WARNING armónico:** ninguno. La ruta de mismatch no se activó; las 28 comparaciones fueron consistentes.
- **N3-P:** DELEGATED se conserva; no se serializó una pista de percusión independiente.
- **Alcance:** no se modificaron Composer Knowledge, arquitectura, genre pack, reglas, research, experiments ni music-engine.

## Handoff

El SongPlanV2 contiene secciones, asignaciones armónicas, eventos pitched explícitos, motivos, pitches, onsets, duraciones y velocities. El handoff no espera que el motor infiera notas desde labels, modo, energía o roles.
