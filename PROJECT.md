# Music Composer Research Lab

## Project Status

**Estado:** Initial Research Phase
**Dominio actual:** Melody
**Versión del conocimiento:** Pre-v1 / no validated knowledge
**Género inicial previsto:** Indie Dance
**Implementación técnica:** No iniciada

---

# 1. Project Overview

Music Composer Research Lab es un proyecto de investigación cuyo objetivo es comprender y formalizar cómo se toman decisiones durante la composición musical.

El proyecto busca construir un sistema de conocimiento de composición que pueda ser utilizado posteriormente por diferentes sistemas de inteligencia artificial sin depender de un modelo, proveedor o arquitectura concreta.

El objetivo no es enseñar teoría musical de manera enciclopédica.

El objetivo es transformar conocimiento musical en principios útiles para responder preguntas compositivas como:

* ¿qué debería repetirse?
* ¿qué debería variar?
* ¿cuándo introducir silencio?
* ¿cómo establecer identidad?
* ¿cómo generar tensión?
* ¿cómo resolverla?
* ¿cómo crear dirección?
* ¿cómo construir contraste?
* ¿cómo desarrollar una idea?
* ¿cómo crear un hook?
* ¿cómo hacer que diferentes secciones cumplan funciones distintas?
* ¿cómo adaptar estas decisiones a un género?

---

# 2. Long-Term Goal

Construir un sistema de conocimiento musical:

* independiente del modelo;
* modular;
* auditable;
* revisable;
* experimental;
* transferible;
* comprensible tanto para humanos como para sistemas de IA.

El conocimiento desarrollado debería poder utilizarse en el futuro con:

* GPT;
* Gemini;
* Claude;
* Codex;
* modelos open-source;
* modelos musicales especializados;
* modelos fine-tuned;
* modelos simbólicos;
* sistemas híbridos;
* modelos propios todavía no desarrollados.

La arquitectura conceptual del proyecto no debe depender de ninguno de ellos.

---

# 3. Core Research Question

La pregunta central del proyecto es:

> ¿Cómo podemos representar de forma explícita el conocimiento y los procesos de decisión que permiten componer música con intención?

Esto requiere estudiar no solamente:

> qué ocurre musicalmente,

sino también:

> por qué podría elegirse una determinada solución compositiva en lugar de otra.

---

# 4. Project Philosophy

El proyecto parte de una distinción fundamental:

**Saber teoría musical no es lo mismo que saber componer.**

La teoría es necesaria para describir muchos fenómenos musicales, pero no siempre indica qué decisión debe tomar un compositor en un contexto concreto.

El proyecto intenta conectar:

`musical phenomenon`

→ `compositional problem`

→ `decision`

→ `possible effect`

→ `context`

→ `evaluation`

El objetivo no es crear leyes rígidas.

El objetivo es construir conocimiento que ayude a razonar sobre alternativas compositivas.

---

# 5. Knowledge Philosophy

No todas las afirmaciones musicales poseen el mismo nivel de certeza.

El proyecto distingue entre:

* THEORY;
* GENRE OBSERVATION;
* COMPOSITION HEURISTIC;
* HYPOTHESIS;
* EXPERIMENTAL RESULT;
* ARTISTIC PREFERENCE.

Las heurísticas no deben presentarse como leyes.

Las observaciones de género no deben convertirse automáticamente en principios generales.

Las preferencias del Project Owner son válidas artísticamente, pero no constituyen evidencia general.

Los resultados experimentales deben interpretarse solamente dentro de las condiciones estudiadas.

---

# 6. Current Knowledge Status

Actualmente el proyecto debe considerarse prácticamente vacío desde el punto de vista epistemológico.

La estructura de archivos existe, pero esto NO significa que el conocimiento contenido en esas áreas haya sido desarrollado.

Actualmente:

* no hay principios de melodía aprobados;
* no hay principios de armonía aprobados;
* no hay principios de ritmo aprobados;
* no hay principios de forma aprobados;
* no hay reglas machine-readable aprobadas;
* no hay rúbrica de evaluación validada;
* no hay experimentos completados;
* no hay resultados experimentales propios;
* no hay conocimiento validado de Indie Dance;
* no hay datasets seleccionados;
* no hay sistema de generación musical implementado.

Existe un documento heredado:

`manual/drafts/melody-v1.md`

Este documento contiene una primera propuesta sobre melodía.

Su contenido debe considerarse:

**material candidato para revisión.**

No constituye todavía conocimiento oficial del proyecto.

Los conceptos MEL-001–MEL-024 incluidos en ese documento pueden ser:

* aceptados;
* modificados;
* divididos;
* combinados;
* renombrados;
* reordenados;
* rechazados.

---

# 7. Current Research Phase

La fase actual es:

## Phase 1 — Melody Foundations

Objetivo:

Construir desde cero una representación rigurosa de las principales decisiones involucradas en composición melódica.

La primera tarea no es ampliar automáticamente el manual heredado.

La primera tarea es auditarlo.

Debemos determinar:

1. qué conceptos son realmente necesarios;
2. cuáles describen teoría;
3. cuáles constituyen decisiones compositivas;
4. cuáles son heurísticas;
5. cuáles son hipótesis;
6. cuáles dependen del género;
7. cuáles se solapan;
8. cuáles faltan;
9. qué mecanismos podrían explicar sus efectos;
10. qué afirmaciones necesitan experimentos.

No asumir que la taxonomía MEL existente es correcta.

---

# 8. Current Research Question

La pregunta metodológica inmediata es:

> ¿Cuáles son las variables y decisiones fundamentales que intervienen en la construcción de una melodía?

Antes de formalizar reglas debemos construir un mapa suficientemente bueno del espacio de decisiones melódicas.

---

# 9. Planned Knowledge Domains

El orden inicial previsto es:

## Phase 1 — Melody

Investigar:

* motivo;
* identidad;
* frase;
* ritmo melódico;
* repetición;
* variación;
* contorno;
* intervalos;
* registro;
* rango;
* notas estructurales;
* silencio;
* densidad;
* tensión;
* resolución;
* expectativa;
* sorpresa;
* desarrollo;
* cierre.

Esta lista es provisional.

---

## Phase 2 — Harmony

Investigar decisiones como:

* estabilidad;
* cambio de acorde;
* permanencia;
* tensión;
* resolución;
* ritmo armónico;
* dirección;
* función;
* color;
* voice leading;
* movimiento del bajo;
* relación con melodía;
* contraste entre secciones.

---

## Phase 3 — Rhythm

Investigar:

* pulse;
* meter;
* subdivision;
* syncopation;
* accents;
* rhythmic motifs;
* density;
* groove;
* timing;
* rhythmic tension;
* repetition;
* variation.

---

## Phase 4 — Form

Investigar:

* frase;
* sección;
* repetición estructural;
* contraste;
* transición;
* expectativa;
* desarrollo;
* acumulación;
* clímax;
* cierre.

---

## Phase 5 — Interaction

Estudiar interacciones entre dominios:

* melody-harmony;
* melody-rhythm;
* harmony-rhythm;
* form-development;
* tension across domains.

---

## Phase 6 — Hooks

Estudiar qué características hacen que determinadas ideas funcionen como elementos especialmente identificables y memorables.

---

## Phase 7 — Section Contrast

Estudiar cómo diferentes variables permiten diferenciar:

* verse;
* pre-chorus;
* chorus;
* bridge;
* intro;
* outro;
* otras estructuras.

---

## Phase 8 — Full-Song Development

Estudiar cómo cambia el material a lo largo de una canción completa.

---

## Phase 9 — Genre Specialization

Aplicar el conocimiento desarrollado a géneros concretos.

Primer género previsto:

`indie-dance`

---

## Phase 10 — Arrangement

Investigar:

* instrumentation;
* texture;
* density;
* register distribution;
* layering;
* entrances;
* removals;
* timbral contrast;
* arrangement development.

---

# 10. Repository Structure

```text
music-composer-lab/
│
├── AGENTS.md
├── PROJECT.md
│
├── manual/
│   ├── 00-philosophy.md
│   ├── 01-melody.md
│   ├── 02-harmony.md
│   ├── 03-rhythm.md
│   ├── 04-form.md
│   ├── 05-arrangement.md
│   └── 06-evaluation.md
│
├── genres/
│   └── indie-dance/
│       ├── genre-definition.md
│       ├── melody.md
│       ├── harmony.md
│       ├── rhythm.md
│       ├── structure.md
│       └── instrumentation.md
│
├── rules/
│   ├── melody.yaml
│   ├── harmony.yaml
│   └── evaluation.yaml
│
├── examples/
│   ├── approved/
│   ├── rejected/
│   └── corrected/
│
├── experiments/
│
├── evaluations/
│   └── rubric.md
│
├── datasets/
│   └── README.md
│
└── decisions/
    └── DECISIONS.md
```

---

# 11. Purpose of Each Area

## `manual/`

Contiene conocimiento conceptual sobre composición.

Debe explicar fenómenos, decisiones, contexto, mecanismos candidatos, heurísticas, excepciones y formas de evaluación.

Es la principal representación humana del conocimiento.

---

## `genres/`

Contiene conocimiento específico de género.

Debe documentar cómo se manifiestan los principios generales dentro de estilos concretos.

No debe utilizarse para almacenar principios generales.

---

## `rules/`

Contiene representaciones estructuradas y machine-readable derivadas de conocimiento suficientemente maduro.

No constituye la fuente primaria de investigación.

Primero se entiende el concepto.

Después se formaliza.

---

## `examples/`

Contiene ejemplos que ayuden a estudiar diferencias entre decisiones compositivas.

### `approved/`

Ejemplos considerados musicalmente efectivos dentro de un contexto determinado.

### `rejected/`

Ejemplos que muestran problemas relevantes.

### `corrected/`

Versiones modificadas de ejemplos problemáticos que permiten estudiar qué cambio produjo una mejora.

---

## `experiments/`

Contiene experimentos controlados.

Cada experimento debe intentar responder una pregunta específica y registrar condiciones, resultados y limitaciones.

---

## `evaluations/`

Contiene los sistemas utilizados para evaluar composiciones, fragmentos y experimentos.

Las métricas deben justificarse antes de convertirse en puntuaciones.

---

## `datasets/`

Contendrá información sobre datasets utilizados en fases futuras.

Actualmente no existe ningún dataset aprobado.

---

## `decisions/`

Contiene decisiones metodológicas o arquitectónicas importantes.

Debe permitir reconstruir por qué cambió el proyecto.

---

# 12. Development Workflow

El flujo general del proyecto es:

`question`

→ investigación

→ análisis

→ concepto candidato

→ búsqueda de límites y contraejemplos

→ hipótesis

→ experimento cuando proceda

→ evaluación humana/modelo/estructural

→ interpretación

→ conocimiento provisional

→ revisión

→ formalización

→ reglas estructuradas cuando estén justificadas.

---

# 13. Collaboration Workflow

El proyecto utiliza tres roles.

## Project Owner

Define objetivos, escucha resultados y toma decisiones artísticas finales.

## Music/Methodology Director

Dirige la metodología y revisa críticamente los resultados.

## Codex Research Agent

Investiga, organiza, documenta, cuestiona y mantiene el repositorio.

Flujo habitual:

`Music/Methodology Director / Project Owner`

→ pregunta o tarea

→ `Codex Research Agent`

→ investigación y reporte

→ `Project Owner`

→ revisión con `Music/Methodology Director`

→ decisión

→ actualización del proyecto.

---

# 14. Experiment Philosophy

Los experimentos no existen para demostrar que nuestras reglas son correctas.

Deben intentar descubrir:

* cuándo funcionan;
* cuándo no funcionan;
* qué variables realmente importan;
* qué mecanismos podrían explicar el efecto;
* qué contextos modifican el resultado.

Idealmente un experimento cambia pocas variables a la vez.

La escucha humana del Project Owner tiene la última palabra respecto de preferencia artística.

---

# 15. Evaluation Philosophy

El proyecto distingue tres niveles principales.

## Structural Validation

Comprueba restricciones observables o mensurables.

## Model Evaluation

Un sistema de IA puede evaluar características musicales.

Sus juicios son información auxiliar.

## Human Listening Evaluation

El Project Owner escucha la música.

La evaluación humana decide finalmente si una solución funciona artísticamente.

Ninguna puntuación sustituye automáticamente esta evaluación.

---

# 16. Model Independence

El conocimiento central debe permanecer separado de cualquier implementación específica.

El proyecto distingue:

## Composition Knowledge

Principios y decisiones musicales.

## Model Adapters

Instrucciones específicas para que un determinado modelo utilice ese conocimiento.

Los adapters se desarrollarán solamente cuando exista una necesidad concreta.

Actualmente no forman parte del alcance principal.

---

# 17. Initial Genre

El primer género previsto para especialización es:

`indie-dance`

Sin embargo, actualmente los archivos de:

`genres/indie-dance/`

deben considerarse vacíos conceptualmente.

No asumir características del género sin investigación.

La especialización comenzará después de desarrollar suficiente conocimiento general como para distinguir:

* principio general;
* convención estilística;
* característica frecuente;
* excepción;
* preferencia artística.

---

# 18. Out of Scope — Current Phase

Actualmente NO es prioridad:

* generar canciones completas;
* desarrollar una aplicación;
* construir una API;
* crear una interfaz;
* automatizar composición;
* implementar un motor MIDI;
* entrenar modelos;
* realizar fine-tuning;
* seleccionar arquitectura ML;
* construir datasets masivos;
* diseñar prompts específicos de proveedores;
* optimizar para GPT, Gemini, Claude u otro modelo.

Estas áreas podrán desarrollarse posteriormente.

---

# 19. Major Project Decisions

## DEC-001 — Model-independent core

El conocimiento central de composición debe ser independiente de modelos concretos.

No diseñar principios musicales específicamente alrededor de GPT, Gemini, Claude, Codex u otros sistemas.

---

## DEC-002 — Composition before implementation

Primero debemos comprender y formalizar composición.

La implementación técnica viene después.

---

## DEC-003 — Decision-oriented knowledge

El conocimiento debe priorizar decisiones compositivas y sus consecuencias, no solamente definiciones teóricas.

---

## DEC-004 — Human artistic authority

La evaluación humana del Project Owner tiene autoridad final respecto de calidad y preferencia artística.

---

## DEC-005 — Knowledge begins unvalidated

El manual/drafts/melody-v1.md heredado no constituye conocimiento aprobado.

Debe auditarse antes de incorporarse al sistema.

---

# 20. Immediate Next Step

La siguiente acción del proyecto es:

**Auditar conceptualmente el dominio de melodía antes de escribir o aprobar principios MEL individuales.**

Objetivo inmediato:

crear un mapa provisional de las principales variables, fenómenos y decisiones de composición melódica y comparar dicho mapa con el `manual/drafts/melody-v1.md`.

El resultado debe indicar:

* qué conceptos del borrador parecen fundamentales;
* cuáles se solapan;
* cuáles están mal definidos;
* cuáles son heurísticas;
* cuáles son dependientes de contexto o género;
* cuáles faltan;
* cuáles requieren investigación adicional.

No formalizar todavía `rules/melody.yaml`.

---

# 21. Definition of Progress

Una tarea constituye progreso cuando hace que el conocimiento del proyecto sea:

* más claro;
* más preciso;
* mejor delimitado;
* más comprobable;
* más falsable;
* más útil para tomar decisiones;
* más transferible;
* más útil musicalmente.

Crear más documentación por sí mismo no constituye progreso.

La pregunta que debe guiar el proyecto es:

> ¿Entendemos mejor que antes cómo tomar una decisión compositiva y bajo qué condiciones funciona?
