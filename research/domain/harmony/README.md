# Harmony — Dominio de investigación

## Estado de este documento

- Tipo: definición de dominio de investigación. NO es conocimiento aprobado de `manual/`, ni regla de `rules/`, ni conocimiento de género.
- Estado del dominio: ARCHITECTURE ONLY. No existe todavía ninguna investigación temática de armonía (ninguna RQ-HAR iniciada, ningún candidato CAND-HAR, ninguna fuente SRC registrada desde este dominio).
- Idioma: contenido humano en español; identificadores y claves técnicas en inglés.
- Alcance general del proyecto: música popular tonal/modal occidental y tradiciones estrechamente relacionadas. `general` NO significa universal para toda la música humana.

## Qué estudia este dominio

Cómo tomar decisiones de composición armónica con intención.

No estudia simplemente hechos de teoría armónica (qué grados contiene un acorde, cómo se nombra una progresión). Estudia:

**problema compositivo → variable de decisión → posible efecto → contexto → límites**

Ejemplos de decisiones propias del dominio:

- mantener una armonía o cambiarla;
- hacia dónde dirigir una sucesión y con qué medios;
- cómo establecer, mantener o debilitar un centro tonal o modal;
- qué ritmo de cambio armónico usar y dónde colocar los cambios;
- cómo prolongar una región sin repetición estática;
- qué grado de cierre buscar al final de una frase o sección;
- cuándo expandir el material (tonicalización, mezcla modal, cromatismo, modulación) y cuándo no;
- qué sonoridad concreta usar (tríada, séptima, extensiones, inversión, disposición, bajo).

## Fronteras del dominio

### Dentro

- Estabilidad/inestabilidad y centro tonal/modal.
- Dirección armónica y función (incluyendo dónde el modelo T–PD–D no aplica).
- Conducción de voces (voice leading) como decisión compositiva.
- Ritmo armónico y prolongación.
- Cadencia y cierre (incluyendo alternativas al cierre cadencial clásico y loops).
- Tonicalización, mezcla modal, cromatismo, modulación.
- Color armónico (identidad del acorde frente a disposición, registro y timbre).
- Bajo como variable armónica (root frente a bass, pedal, slash chords, inversión).

### Fuera (interfaces con otros dominios)

- Interacción melodía-armonía (non-chord tones, suspensiones, apoyaturas, elección de acorde bajo una melodía dada): pertenece a la futura interfaz `cross_domain` entre Harmony Foundations y Melody Foundations. Durante la fase Harmony, una dependencia melódica puede registrarse como dependencia de contexto sin resolver la interfaz.
- Ritmo de superficie, groove, desplazamiento métrico: dominio Rhythm/Meter.
- Agrupación en frases, funciones seccionales, arco formal: dominio Form.
- Capas, instrumentación, textura, distribución registral: Arrangement/Texture.
- Letra y prosodia: dominio correspondiente cuando exista; hasta entonces, dependencia externa registrada.

### Lo que este dominio NO es

- No es un manual de armonía tonal (no enseñar acordes y progresiones como temario).
- No es la adopción de ningún marco teórico como modelo oficial (ver marcos exploratorios en `HARMONY-ROADMAP.md`).
- No es conocimiento de género: los loops pop, la sintaxis de progresiones pop/rock o la ambigüedad de tónica se investigan primero como decisiones generales y solo después se especializan en `genres/`.

## Principio metodológico obligatorio

Toda afirmación futura del dominio debe conservar la separación:

```
STRUCTURE → PERCEPTION → COMPOSITION
```

- STRUCTURE: hecho estructural (p. ej., V7 contiene determinados grados y tendencias de resolución por semitono en la tradición tonal).
- PERCEPTION: efecto perceptivo, solo si hay evidencia (p. ej., oyentes enculturados juzgan X como más inestable que Y en tales condiciones).
- COMPOSITION: implicación compositiva, solo si está justificada (p. ej., el compositor puede usar X para dirigir hacia Y en tal contexto).

Ningún nivel implica automáticamente el siguiente.

## Política de evidencia

Se reutiliza el sistema existente del proyecto, sin inventar otro:

- `evidence_class`: THEORY, GENRE OBSERVATION, COMPOSITION HEURISTIC, HYPOTHESIS, EXPERIMENTAL RESULT, ARTISTIC PREFERENCE.
- `support_basis` (ortogonal): EXTERNAL_EMPIRICAL, THEORETICAL_SCHOLARSHIP, COMPOSITION_PEDAGOGY, CORPUS_ANALYSIS, REPERTOIRE_ANALYSIS, PROJECT_EXPERIMENT, PRACTITIONER_OBSERVATION.
- Formato de candidatos: el mismo formato ligero `CAND-HAR-NNN` definido en `research/ROADMAP.md` §5 (problema, variable, acción, efecto, contexto, `structure_perception_composition`, falsación). No crear candidatos en esta tarea de arquitectura.

## Archivos del dominio

- `README.md` (este archivo): definición y fronteras.
- `HARMONY-ROADMAP.md`: arquitectura de investigación, secuencia de RQs, mapa de dependencias, interfaces, supuestos peligrosos preliminares, riesgos y siguiente paso recomendado.
- Futuros: síntesis por RQ (`RQ-HAR-NNN.md` en `research/questions/`), notas de trabajo por tema (esta carpeta), candidatos (`research/candidates/harmony/`), fuentes (`research/sources/`).

## Lectura recomendada antes de investigar armonía

- `research/integrations/melody-foundations-v0.md` (especialmente mapa cross-domain, gaps y cuellos de botella: la armonía es el cuello de botella transversal del proyecto).
- `research/ROADMAP.md` (workflow por pregunta, clases de evidencia, regla epistémica crítica).
- `.agents/skills/research-music-concept/SKILL.md` y `.agents/skills/audit-music-knowledge/SKILL.md` (aplicación manual obligatoria en cada RQ-HAR).
