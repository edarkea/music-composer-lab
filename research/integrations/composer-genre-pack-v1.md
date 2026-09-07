# Composer Genre Pack v1

## A. Selected genre/style

**Indie-dance MVP — realización loop/groove-based de electrónica-pop,
acotada a los rasgos ya representados en el repositorio.**

Esta etiqueta no afirma que todo indie-dance tenga estas características. El
pack usa únicamente observaciones existentes sobre repertorios loop/groove-
based, EDM, dance-pop y pop/rock relacionado. La carpeta `genres/indie-dance/`
permanece vacía y no se modifica; este documento es una especialización de
integración provisional para Composer MVP.

## B. Why this genre is the MVP choice

Es la opción con mayor soporte actual para una realización mínima porque el
repositorio contiene material revisado sobre:

- melodía cíclica sostenida con cambio formal en capas, textura, densidad o
  timbre (`CAND-MEL-011`);
- persistencia armónica cíclica y cambio cross-domain (`CAND-HAR-026`);
- retorno de loop, parada y frontera sin imponer una cadencia clásica
  (`CAND-HAR-031`);
- forma loop-based con diferenciación analítica mediante cambios en otros
  dominios (`CAND-FORM-008`).

La elección se basa en soporte de repositorio, no en popularidad ni en gusto
personal. `pop/rock` y `loop-based` son alternativas de alcance relacionadas,
pero no se construye un segundo pack en esta unidad.

## C. Evidence and scope boundary

Las fuentes son observaciones de género y análisis de repertorio, con soporte
teórico/corpus según cada candidato. No prueban que un rasgo produzca interés,
energía, memorabilidad, coherencia percibida o calidad.

La arquitectura de tres capas es obligatoria:

```text
GENERAL COMPOSER KNOWLEDGE
+ GENRE SPECIALIZATION
+ ARTISTIC INTENT
→ CONCRETE DECISION
```

La frecuencia o presencia en repertorio permite enumerar una realización y,
con alcance, orientar un filtro de compatibilidad. No convierte una práctica
en requisito ni produce `RANK-1`.

## D. Genre-pack entries

### GP-01 — Melodic persistence with cross-domain change

- **Fuente:** `CAND-MEL-011`.
- **Alcance:** repertorios loop/groove-based, EDM y música popular relacionada;
  melodía cíclica sostenida.
- **Estado:** `GENRE ADMIT WITH SCOPE`.
- **Pregunta:** si la melodía debe permanecer, ¿dónde se puede planificar el
  cambio formal?
- **Operación / rol:** `ENUMERATE`, `FILTER`; `SOFT FILTER`, `SECTION PRIORITY`,
  `CROSS-DOMAIN CONSTRAINT`.
- **General:** repetición y variación pueden gestionar identidad y cambio.
- **Especialización:** el cambio puede trasladarse a capas, textura, densidad
  o timbre mientras el material melódico se sostiene.
- **Uso:** conservar la melodía cuando la intención prioriza groove/continuidad
  y generar el cambio en parámetros de realización declarados.
- **No-claim:** no demuestra interés, participación, ausencia de aburrimiento ni
  que la melodía deba repetirse en toda canción.
- **Handoff artístico:** elegir qué parámetro cambia y cuánto; la preferencia
  decide entre melodía estable, variación mínima o contraste nuevo.
- **Cross-domain:** melodía → textura/densidad/timbre (`CO-DEVELOPMENT`).
- **SongPlan:** material melódico recurrente, parámetros de cambio por sección y
  prioridad de realización.

### GP-02 — Cyclic/static harmonic frame

- **Fuente:** `CAND-HAR-026`.
- **Alcance:** pop/rock y música groove-based con loop, vamp o pedal; no se
  transfiere automáticamente a práctica común.
- **Estado:** `GENRE ADMIT WITH SCOPE`.
- **Pregunta:** ¿puede una sección sostener un marco armónico cíclico mientras
  la diferenciación ocurre en otros dominios?
- **Operación / rol:** `ENUMERATE`, `FILTER`; `DEFAULT`, `REALIZATION
  PREFERENCE`, `CROSS-DOMAIN CONSTRAINT`.
- **General:** un marco armónico y una realización se deciden separadamente.
- **Especialización:** la persistencia cíclica puede funcionar como marco de
  sección; el arreglo, registro, densidad o timbre puede portar el cambio.
- **Uso:** considerar loop/vamp/pedal como opción de continuidad y filtrar
  cambios de superficie que contradigan la intención de persistencia.
- **No-claim:** el loop no genera coherencia, energía, calma, aburrimiento o
  dirección por sí solo; la estasis no equivale a ausencia de forma.
- **Handoff artístico:** escoger entre persistencia, superficie móvil o
  progresión dirigida según intención.
- **Cross-domain:** armonía → arreglo/densidad/registro/timbre (`CONSTRAINT`).
- **SongPlan:** marco armónico, ciclo, secciones donde persiste y capas que
  pueden cambiar.

### GP-03 — Loop return, stop and boundary vocabulary

- **Fuente:** `CAND-HAR-031`.
- **Alcance:** organización cíclica pop/rock/groove-based.
- **Estado:** `GENRE ADMIT WITH SCOPE`.
- **Pregunta:** ¿cómo se articula una frontera sobre un ciclo sin llamar
  cadencia a todo retorno?
- **Operación / rol:** `ENUMERATE`, `FILTER`; `AVOIDANCE`, `DIAGNOSTIC
  GUARDRAIL`, `SECTION PRIORITY`.
- **General:** arrival, closure, boundary y return son estados distintos.
- **Especialización:** una parada, cambio de capas/densidad o iteración final
  marcada puede ser una opción de frontera sobre un loop.
- **Uso:** nombrar `RETURN`, `STOP`, `BOUNDARY` y `FINAL EVENT` de forma neutral;
  usar cadencia solo si existe un proceso declarado.
- **No-claim:** una parada no prueba cierre armónico; un retorno no es cadencia;
  la costura recurrente o terminal sigue incierta.
- **Handoff artístico:** decidir si la frontera debe continuar, cortar,
  retornar o sonar terminal mediante la combinación de rasgos elegida.
- **Cross-domain:** forma → arreglo y articulación (`CONSTRAINT`); frontera →
  revisión de estados de cierre (`REVISION TRIGGER`).
- **SongPlan:** tipo de retorno/parada, iteración marcada, entradas/salidas y
  estado de frontera.

### GP-04 — Loop-based formal differentiation

- **Fuente:** `CAND-FORM-008`.
- **Alcance:** repertorios populares/loop-based delimitados.
- **Estado:** `GENRE ADMIT WITH SCOPE`.
- **Pregunta:** ¿cómo diferenciar unidades formales cuando el marco cíclico
  persiste?
- **Operación / rol:** `ENUMERATE`, `FILTER`; `OPTION WEIGHTING`, `SECTION
  PRIORITY`, `CROSS-DOMAIN CONSTRAINT`.
- **General:** una función formal orienta objetivos, pero no determina un medio.
- **Especialización:** la diferenciación puede situarse en capas, densidad,
  timbre, registro, parada, entrada/salida o ubicación del retorno.
- **Uso:** generar opciones de forma cíclica y filtrar las que no expresen la
  diferencia o continuidad buscada.
- **No-claim:** los oyentes no necesariamente perciben las unidades como
  secciones; ningún cambio aislado crea forma automáticamente.
- **Handoff artístico:** seleccionar qué dimensiones cambian y cuáles preservan
  identidad.
- **Cross-domain:** forma ↔ melodía/armonía ↔ arreglo (`CO-DEVELOPMENT`).
- **SongPlan:** funciones por sección, marco persistente, cambios de capas y
  ubicación de retornos.

### GP-05 — Genre-scoped anticipatory rhythmic option

- **Fuente:** `CAND-RHY-005`, con relación a `CAND-MEL-026`.
- **Alcance:** pop/rock reciente; solo es un input opcional para una realización
  indie-dance si la prosodia, el metro y el material realmente coinciden.
- **Estado:** `GENRE ADMIT WITH SCOPE`.
- **Pregunta:** ¿cuándo considerar anticipación sin perder la referencia
  métrica?
- **Operación / rol:** `ENUMERATE`, `FILTER`; `OPTION WEIGHTING`, `SOFT FILTER`,
  `DIAGNOSTIC GUARDRAIL`.
- **General:** el desplazamiento debe analizarse respecto de una métrica y un
  contexto declarados.
- **Especialización:** anticipación con sustain y stress compatible es una
  alternativa documentada en pop/rock reciente.
- **Uso:** considerarla solo cuando exista metro recuperable, sustain, stress y
  armonía compatibles.
- **No-claim:** no es requisito de indie-dance, ni prueba de groove, energía,
  tensión, prominencia o mejor phrasing.
- **Handoff artístico:** elegir onset alineado, anticipado o retardado según
  intención y legibilidad.
- **Cross-domain:** ritmo ↔ melodía, prosodia y armonía (`CONSTRAINT`).
- **SongPlan:** posición del onset, sustain, stress y condición métrica.

### GP-06 — Sectional contrast as a bundle

- **Fuente:** `CAND-MEL-022`.
- **Alcance:** pop/rock verso-coro o forma análoga; no es una afirmación de que
  el coro deba ser más alto.
- **Estado:** `GENRE ADMIT WITH SCOPE`.
- **Pregunta:** ¿qué haz de cambios puede diferenciar una sección sin perder
  continuidad?
- **Operación / rol:** `ENUMERATE`, `FILTER`; `OPTION WEIGHTING`, `SOFT FILTER`,
  `ARTISTIC PRIORITY`.
- **General:** el contraste seccional puede usar varios parámetros coordinados.
- **Especialización:** cambio registral puede ser uno de los marcadores junto a
  dinámica, textura, densidad, ritmo armónico o letra.
- **Uso:** reservar espacio registral y probar el haz de marcadores, no subir el
  registro como solución automática.
- **No-claim:** el registro aislado no crea energía, contraste ni función de
  coro; la eficacia requiere escucha.
- **Handoff artístico:** elegir qué dimensiones contrastan y cuáles permanecen.
- **Cross-domain:** forma ↔ registro/densidad/textura (`CO-DEVELOPMENT`).
- **SongPlan:** diferencias por sección, registro relativo y capas coordinadas.

## E. Decision-domain coverage

| Necesidad | Cobertura del pack | Tratamiento |
|---|---|---|
| Forma global | Sí, dentro de una organización cíclica | opción + preferencia |
| Roles de sección | Sí, con `establish/maintain/contrast/return/boundary` | filtro acotado |
| Melodía | Sí, persistencia y cambio trasladado | prioridad de sección |
| Armonía | Sí, loop/vamp/pedal como marco posible | realización preferida |
| Ritmo/métrica | Parcial, anticipación condicionada | opción, no requisito |
| Repetición/desarrollo | Sí, repetición en un dominio y cambio en otros | preferencia |
| Hook/foco | Parcial; se mantiene separado de memorability | general + preferencia |
| Textura/arreglo | Sí, como vehículo de cambio mínimo | dependencia explícita |
| Contraste | Sí, como haz de marcadores | filtro + escucha |
| Tensión/release | No hay scalar; solo dimensiones declaradas | diagnóstico + intención |
| Densidad/registro | Sí, como variables coordinadas, sin umbral | preferencia |
| Continuidad/cambio | Sí, marco persistente + cambio seleccionado | tradeoff artístico |

La cobertura suficiente es mínima y acotada: el pack no pretende resolver
producción, mezcla, instrumentación exhaustiva ni optimización de estilo.

## F. Style priorities

Dentro del alcance del pack, las prioridades disponibles son:

- permitir persistencia cíclica de material melódico o armónico;
- trasladar parte del cambio formal a capas, textura, densidad, timbre o
  registro;
- tratar retorno, parada y cadencia como conceptos separados;
- conservar una jerarquía focal explícita cuando se añadan capas;
- coordinar cambios entre dominios en vez de exigir variación melódica;
- mantener la anticipación rítmica como opción condicionada, no como firma
  obligatoria.

Estas son prioridades de búsqueda/realización del pack, no leyes ni rankings.

## G. Style-compatible options

Opciones compatibles que permanecen abiertas:

- loop/vamp/pedal o progresión dirigida;
- melodía estable, variación mínima o material nuevo por sección;
- cambio mediante capas, densidad, timbre, registro, dinámica o ritmo;
- frontera por parada, iteración marcada, cambio de arreglo o continuidad;
- onset alineado o anticipado bajo condiciones métricas;
- contraste concentrado en un dominio o distribuido como haz.

El pack no asigna pesos numéricos. La intención artística decide entre opciones
que sobreviven.

## H. Avoidances and diagnostic guardrails

Se rechazan como prescripciones automáticas:

1. “el loop debe tener cadencia”;
2. “el retorno del loop es una cadencia”;
3. “la melodía debe variar para que exista forma”;
4. “la densidad crea energía”;
5. “el registro alto crea contraste o coro”;
6. “la anticipación crea groove/tensión”;
7. “la repetición crea memorabilidad”;
8. “un cambio de capa garantiza una nueva sección”.

Son guardrails diagnósticos o límites de transferencia. No generan elecciones
por sí solos.

## I. Artistic-choice handoffs

El compositor debe decidir explícitamente:

- qué material permanece y qué parámetro cambia;
- si el marco cíclico o una progresión dirigida sirve mejor al objetivo;
- qué capa es focal y qué capas deben retirarse o reducirse;
- qué diferencia de sección se busca y qué identidad se conserva;
- si una frontera debe sonar abierta, como corte o terminal;
- si la anticipación es apropiada para el metro, prosodia y armonía concretos;
- cuánto se acepta la incertidumbre perceptiva.

## J. General-vs-genre boundary

El conocimiento general poblado en `composer-knowledge-v1.md` sigue activo. El
pack solo añade un contexto de prioridad y realización. No puede:

- convertir una observación de repertorio en requisito;
- sustituir el alcance de una evidencia general;
- fabricar una explicación de memorabilidad o tensión;
- imponer una forma fija;
- eliminar alternativas que la intención artística mantiene válidas.

## K. Cross-domain inputs for Unit 4

Se entregan **6** inputs:

1. melodía cíclica → cambio en textura/capas/densidad/timbre;
2. marco armónico cíclico → realización y cambio de arreglo;
3. retorno/parada → estado de frontera y cierre separado;
4. función formal → organización cross-domain de la sección;
5. anticipación → coordinación ritmo-melodía-prosodia-armonía;
6. contraste registral → haz de registro, densidad, textura y dinámica.

Son dependencias y prioridades de integración, no una orquestación completa.

## L. SongPlan relevance

Se identifican **6** decisiones de género relevantes para SongPlan:

1. tipo de marco: cíclico, vamp, pedal o progresión alternativa;
2. material melódico que permanece y dominios donde cambia la realización;
3. capas, densidad, timbre y registro por sección;
4. tipo de retorno, parada o frontera;
5. onset anticipado y sus condiciones, si se selecciona;
6. jerarquía focal y restricciones del acompañamiento.

El SongPlan recibe decisiones y restricciones concretas. La clase de evidencia,
alcance, preferencia e incertidumbre permanecen como metadatos de traza.

## M. Proposed form options

El pack permite proponer, para Unit 4, dos familias de forma sin congelar una:

1. **Ciclo persistente con diferenciación de capas:** marco armónico/melódico
   recurrente; cambio por entradas, salidas, densidad, timbre, registro o
   parada.
2. **Secciones contrastantes con marco loop-based:** secciones delimitadas por
   cambios coordinados y retornos marcados, sin llamar cadencia al retorno.

La forma concreta queda deferida a intención artística y Unit 4. No se afirma
que ninguna familia sea superior.

## N. Remaining genre limitations

- No existe contenido canónico previo en `genres/indie-dance/`.
- La etiqueta indie-dance es una acotación de integración, no una taxonomía
  histórica completa.
- El soporte directo proviene de loop/groove-based, EDM y pop/rock relacionado;
  la transferencia exacta a todo indie-dance es desconocida.
- No hay ranking de realizaciones, de densidad, de registro ni de textura.
- Hook, prominence y memorability siguen separados.
- Tensión sigue siendo multidimensional y no tiene scalar oficial.
- Prosodia, producción, mezcla e instrumentación detallada quedan fuera.

## O. MVP sufficiency verdict

El pack cierra el P0 de realización estilística mínima **con alcance**. Permite
que Unit 4 combine conocimiento general, prioridades loop-based e intención
artística para construir una primera decisión de canción sin inventar reglas de
género.

### Success test

1. Selección por soporte del repositorio: **PASS**.
2. Sin conocimiento externo inventado: **PASS**.
3. Prevalencia no convertida en prescripción: **PASS**.
4. General y género separados: **PASS**.
5. Preferencia artística explícita: **PASS**.
6. Realización mínima de canción: **PASS, con alcance**.
7. Textura/arreglo tratado honestamente: **PASS**.
8. Sin claims de memorabilidad no soportados: **PASS**.
9. Sin modelo universal de tensión: **PASS**.
10. Inputs útiles para Unit 4: **PASS**.

**Resultado: 10 / 10 PASS.**

## Estado de Unit 3

**A — MINIMAL GENRE PACK READY FOR CROSS-DOMAIN SONG INTEGRATION**

Genre entries admitted: **6**. `GENRE ADMIT`: **0**.
`GENRE ADMIT WITH SCOPE`: **6**. `GENRE REFERENCE ONLY`: **0**.
`GENRE EXCLUDE`: **0**. `ENUMERATE`: **6**. `FILTER`: **6**.
`RANK-1`: **0**. `RANK-2`: **0**.

Artistic-priority handoffs: **7**. Genre-specific diagnostic guardrails: **8**.

No se modificaron candidatos, `manual/`, `rules/`, `genres/`, SongPlan, código,
experimentos ni metodología. Nueva investigación: **NONE**. Experimentos:
**NONE**.
