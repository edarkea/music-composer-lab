---

name: audit-music-knowledge
description: Audita críticamente conocimiento musical existente en el proyecto. Detecta generalizaciones, solapamientos, causalidad injustificada, números arbitrarios, dependencias de género y afirmaciones no sustentadas. Usar al revisar manuales, principios, taxonomías, reglas o borradores musicales antes de aprobarlos.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Audit Music Knowledge

## Objetivo

Revisar críticamente conocimiento musical existente antes de aceptarlo como parte del sistema.

La finalidad NO es corregir estilísticamente un documento.

La finalidad es determinar:

* qué afirma;
* qué tipo de conocimiento representa;
* qué está suficientemente justificado;
* qué necesita reformulación;
* qué necesita investigación;
* qué debería rechazarse;
* qué conceptos faltan.

Seguir `AGENTS.md` y `PROJECT.md`.

## Principio fundamental

El documento auditado NO debe considerarse correcto por el hecho de existir en el repositorio.

Especialmente:

`manual/drafts/`

contiene material candidato, no conocimiento aprobado.

## Proceso

### 1. Identificar unidades conceptuales

Separar el documento en afirmaciones o conceptos analizables.

No auditar únicamente párrafos completos si contienen varias afirmaciones independientes.

### 2. Determinar qué está afirmando

Para cada afirmación importante identificar si es:

* definición;
* descripción;
* relación;
* explicación causal;
* recomendación;
* prohibición;
* criterio de evaluación;
* número o umbral;
* clasificación.

### 3. Clasificación epistemológica

Clasificar provisionalmente como:

* THEORY
* GENRE OBSERVATION
* COMPOSITION HEURISTIC
* HYPOTHESIS
* EXPERIMENTAL RESULT
* ARTISTIC PREFERENCE
* UNCLASSIFIED / INSUFFICIENT INFORMATION

### 4. Analizar alcance

Preguntar:

* ¿pretende ser general?
* ¿solo pertenece a música tonal?
* ¿depende de un género?
* ¿depende de voz o instrumento?
* ¿depende de una función estructural?
* ¿depende de contexto temporal?
* ¿depende de otras variables?

Marcar cualquier generalización excesiva.

### 5. Analizar utilidad compositiva

Preguntar:

* ¿qué problema ayuda a resolver?
* ¿qué variable controla el compositor?
* ¿qué alternativas existen?
* ¿qué resultado intenta favorecer?

Si no puede relacionarse con ninguna decisión, determinar si es conocimiento teórico necesario o simplemente información fuera de alcance.

### 6. Revisar causalidad

Detectar formulaciones del tipo:

`X produce Y`

y comprobar si realmente sabemos que existe esa relación.

Cuando sea necesario, reformular provisionalmente como:

`X puede contribuir a Y bajo determinadas condiciones`.

No debilitar automáticamente toda afirmación: indicar qué evidencia sería necesaria para sostener una relación más fuerte.

### 7. Buscar absolutismos

Marcar términos como:

* siempre;
* nunca;
* debe;
* necesita;
* obligatorio;
* buena melodía;
* correcto;
* incorrecto;

cuando la afirmación no justifique ese nivel de generalidad.

### 8. Revisar números

Todo número debe responder:

> ¿Por qué este número?

Marcar como provisional o injustificado cualquier:

* rango;
* porcentaje;
* puntuación;
* threshold;
* cantidad recomendada;

que carezca de fundamento explícito.

### 9. Buscar solapamientos

Comprobar si dos conceptos:

* describen el mismo fenómeno con nombres diferentes;
* mantienen una relación jerárquica;
* representan causa y efecto;
* deberían fusionarse;
* necesitan separarse.

No preservar una taxonomía únicamente por respeto al borrador original.

### 10. Buscar conceptos ausentes

Preguntar qué decisiones necesarias no están representadas.

No asumir que una lista existente es exhaustiva.

### 11. Buscar contraejemplos

Intentar imaginar o investigar contextos donde la recomendación:

* no sea necesaria;
* produzca el efecto contrario;
* sea estilísticamente irrelevante;
* pueda sustituirse por otro mecanismo.

## Estados recomendados

Al finalizar la auditoría, cada elemento puede recibir provisionalmente uno de estos estados:

### KEEP FOR RESEARCH

Concepto relevante que merece investigación.

### REFORMULATE

La idea parece útil, pero su formulación actual es problemática.

### SPLIT

Contiene fenómenos distintos que deberían estudiarse por separado.

### MERGE

Se solapa significativamente con otro concepto.

### GENRE-SPECIFIC CANDIDATE

Parece depender principalmente de contexto estilístico.

### NEEDS EVIDENCE

No puede evaluarse adecuadamente sin investigación adicional.

### EXPERIMENT CANDIDATE

La cuestión parece especialmente adecuada para prueba controlada.

### REJECT CANDIDATE

La afirmación parece conceptualmente incorrecta, irrelevante o demasiado problemática para conservarla en su forma actual.

Estos estados son resultados de auditoría, no decisiones finales del proyecto.

## Formato del reporte

# Audit Scope

Qué material fue revisado.

# Overall Assessment

Diagnóstico general breve.

# Concept Map

Conceptos principales detectados y relaciones entre ellos.

# Findings by Concept

Para cada concepto importante:

* afirmación;
* clasificación epistemológica;
* problema detectado;
* alcance probable;
* decisión compositiva asociada;
* estado recomendado;
* investigación necesaria.

# Dangerous Generalizations

Afirmaciones especialmente susceptibles de convertirse en falsas reglas.

# Unsupported Numbers

Umbrales o cantidades sin fundamento suficiente.

# Overlaps

Conceptos potencialmente redundantes.

# Missing Concepts

Áreas importantes aparentemente ausentes.

# Counterexamples / Boundary Conditions

Principales límites encontrados.

# Research Priorities

Preguntas que deberían investigarse antes que otras.

# Questions for the Music/Methodology Director

Decisiones metodológicas que necesitan revisión externa.

# Recommended Next Step

Una única siguiente acción.

## Regla de modificación

Por defecto, una auditoría produce un informe.

NO reescribir silenciosamente el documento auditado.

NO mover el conocimiento auditado a `manual/`.

NO generar reglas YAML.

Las modificaciones deben hacerse después de que el Project Owner y, cuando corresponda, el Music/Methodology Director revisen las conclusiones.
