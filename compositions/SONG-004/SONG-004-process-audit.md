# SONG-004 — Auditoría de materialización y proceso

## Resultado

**SONG-004 está compuesta, SongPlanV2 validado y MIDI materializado.** El Owner aprobó antes de la composición los tres handoffs del plan. N3-P se resolvió como DELEGATED sin pista de percusión independiente. El análisis simbólico confirma apoyo estructural del pulso y coherencia de las etiquetas/pitches; no sustituye la escucha humana. No se generó audio. La aceptación artística queda pendiente.

## Artefactos

- Brief: SONG-004-brief.md
- Plan autorizado: SONG-004-composition-plan.md
- Traza de decisiones: SONG-004-decision-trace.md
- SongPlanV2: SONG-004.songplan.yaml
- Validación y materialización: SONG-004.validation.json
- MIDI: SONG-004.mid

## Validación y materialización

- Runtime local: music-engine 4.0.0; commit 71bbc73337da0d755618bdc796e19ce2e82cc3df.
- Wheel SHA-256: 110E987A1E102C1CF3D29FEC1CCC68583459030F40748E10D66CE1F8E4819FE1; coincide con runtime-lock.yaml.
- Schema SongPlanV2 2.0: **PASS**, valid=true, issues=[].
- Comandos:
  - .venv/Scripts/music-midi.exe songplan validate compositions/SONG-004/SONG-004.songplan.yaml --json
  - .venv/Scripts/music-midi.exe songplan render compositions/SONG-004/SONG-004.songplan.yaml --output compositions/SONG-004/SONG-004.mid
- PPQ MIDI: 960 ticks por negra.
- Longitud: 107520 ticks = 28 compases en 4/4; duración aproximada 57.931 s a 116 BPM.
- SHA-256 SongPlan: 5529307F4C36099744C0BD7CEC0A2985B38CC742F8D4322BC0427ADFCB255A18.
- SHA-256 MIDI: B1B9571A654A7877ED5358FAA7A826F62EAD2EB74859C1C4A339156786D0C62E.
- Note-ons por pista y sección:

| Track | A | B | A' | Coda | Total |
|---|---:|---:|---:|---:|---:|
| pattern | 56 | 56 | 48 | 15 | 175 |
| harmony | 24 | 24 | 24 | 12 | 84 |
| bass | 16 | 16 | 16 | 6 | 54 |
| lead | 3 | 4 | 4 | 2 | 13 |

La pista SONG-004 es la pista de tempo/estructura MIDI y no contiene notas. El archivo contiene cuatro pistas pitched con material; no contiene track drums ni percussion.

## Auditoría armónica

**PASS: 28 asignaciones por compás CONSISTENT / 0 PASS WITH SCOPE / 0 WARNING.** Cada etiqueta fue cotejada con las pitches explícitas de la pista harmony en cada compás cubierto. Las clases de altura coinciden exactamente:

| Etiqueta | Pitches explícitas |
|---|---|
| D minor | D3, F3, A3 |
| Bb major | Bb2, D3, F3 |
| C major | C3, E3, G3 |
| G minor | G2, Bb2, D3 |

La lista aparece en A, B y A' en el orden trazado; la coda asigna D minor durante cuatro compases. Las notas MIDI en pattern, harmony, bass y lead permanecen dentro de la colección D eólica {D, E, F, G, A, Bb, C}. No surgió una discrepancia nueva ni se activó WARNING. La verificación se refiere a la realización explícita del plan; no asigna función armónica por inferencia a notas aisladas.

## N3-P y claridad de pulso

- N3-P apareció antes del handoff SongPlan: **YES**.
- Recordatorio manual para añadir drums: **NO**.
- Decisión aprobada y materializada: **PULSE / PERCUSSIVE FUNCTION DELEGATED TO OTHER LAYERS (DELEGATED)**.
- Capas delegadas: pattern sincopado y bass.
- Drums/percussion independiente: **NO**.
- Comprobación estructural: el bajo marca beats 1 y 3 en A/A', y beat 1 más una quinta en 3& en B; el patrón aporta ataques sincopados y B también conserva un ataque en beat 1. La coda mantiene bajo y patrón con actividad reducida.
- **Límite:** esto confirma organización simbólica con anclajes métricos, no claridad perceptiva. La comprobación auditiva corresponde al Owner y sigue pendiente.

No se añade una parte de drums para llenar huecos ni se convierte DELEGATED en una obligación de percusión.

## Handoffs y límites

- Handoffs aprobados antes de componer: **3** paquetes.
- Nuevos handoffs durante la composición: **0**.
- RANK-1: **0**; RANK-2: **0**.
- Revisiones cross-domain: **0**.
- Validación/render: **PASS**.
- Escucha del Project Owner: **PENDING**.
- Audio/WAV: **NO**.
- Composer Knowledge, arquitectura, genre pack, rules, research, experiments y music-engine modificados: **NO**.

La validación prueba que el SongPlan satisface el contrato local y que el motor materializó las instrucciones simbólicas; no prueba calidad musical, claridad perceptiva del pulso, identidad de género ni aceptación artística. SONG-004 queda preparado para auditoría y escucha del Owner.
