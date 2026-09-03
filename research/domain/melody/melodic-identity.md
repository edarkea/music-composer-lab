# RQ-MEL-001 — Identidad melódica: síntesis de evidencia existente

## Research Question

¿Qué rasgos estructurales contribuyen a los juicios de identidad o parentesco
melódico, cómo se ponderan según el contexto y qué combinaciones de
conservación/cambio cuentan con apoyo empírico o teórico?

## Scope

Esta síntesis opera dentro del scope inicial del proyecto: conocimiento
general de composición dentro de la música popular tonal/modal occidental y
tradiciones estrechamente relacionadas (common-practice, pop, rock, jazz,
electrónica/dance y tradiciones afines cuando la transferibilidad pueda
demostrarse). `general` NO significa `universal para toda la música humana`.

Toda la evidencia externa reseñada utiliza oyentes enculturados en la
tradición tonal occidental (estudiantes universitarios norteamericanos,
adultos, niños occidentales). Ninguna conclusión se generaliza fuera de ese
ámbito sin advertencia explícita.

## Definitions

Los siguientes términos NO son sinónimos en esta síntesis. Cada fuente se
clasifica según lo que midió realmente:

- **Similarity (similitud):** parecido percibido o computado analíticamente
  entre dos fragmentos. Ejemplo: ratings de similitud por pares (Prince 2014;
  Halpern, Bartlett & Dowling 1998, Exp. 1).
- **Identity / same-idea judgment (juicio de misma idea):** juicio de que dos
  apariciones son la misma idea musical, una de ellas transformada. Es el
  constructo de EXP-001 ("¿hasta qué punto percibes esta versión como la
  misma idea melódica transformada?"). Ninguna fuente externa revisada mide
  exactamente esto; las fuentes miden reconocimiento o similitud, que son
  evidencia indirecta.
- **Recognition (reconocimiento):** detección de que material escuchado antes
  ha vuelto o está relacionado (tareas mismo/diferente, detección de
  transposición). Ejemplo: Dowling & Fujitani 1971; Bartlett & Dowling 1980.
- **Recall / memorability (recuerdo):** capacidad de retener o recuperar
  material después (no medida por ninguna fuente de esta síntesis; no inferir
  memorabilidad desde reconocimiento).
- **Coherence (coherencia):** relación entre materiales dentro de un contexto
  musical más amplio. Ninguna fuente revisada la mide directamente; aparece
  solo como implicación compositiva provisional.

Advertencia metodológica: si una fuente mide ratings de similitud, no se
convierte silenciosamente en evidencia sobre identidad de misma idea. Si mide
reconocimiento en memoria a corto plazo con melodías aisladas, no se
convierte en evidencia sobre memorabilidad ni sobre hooks.

## Existing Project Work

- `experiments/EXP-001.md`: exploración con una melodía base, cinco
  transformaciones (B–F), un único evaluador (Project Owner), melodía
  aislada en MIDI, escala ordinal de parentesco 1–4. Resultados: B=3, C=2,
  D=4, E=4, F=2. Ver sección "Project Experimental Evidence" para el
  detalle. Estado: resultado experimental propio, exploratorio, no
  generalizable.
- `experiments/EXP-002.md`: diseño de replicación pausado (tres bases
  nuevas A1–A3, mismas familias B–F). Estímulos especificados y congelados
  como diseño, pero SIN resultados perceptivos. En esta síntesis aparece
  únicamente como diseño de replicación en pausa.
- `manual/drafts/melody-v1.md` (material candidato, NO aprobado): contiene
  afirmaciones relevantes pero no verificadas, en particular MEL-001
  (la identidad del motivo sobrevive a cambios de notas si ritmo y contorno
  se conservan) y MEL-002 ("el ritmo puede ser más importante que las
  notas"). Ambas se tratan aquí como hipótesis a contrastar, no como
  conocimiento. La evidencia revisada NO las confirma en forma general
  (ver "What We Cannot Conclude").
- No se encontró en el repositorio ningún otro informe previo, literature
  note o auditoría sobre identidad melódica. Las menciones a "Dowling &
  Fujitani", "Krumhansl", "Prince", "Jones & Ralston" y "Pick et al." en el
  encargo no correspondían a documentos internos: se verificaron como
  fuentes externas (ver "Source List"). "Pick et al." no pudo verificarse
  como fuente concreta y queda registrado como UNVERIFIED.

## External Evidence

### E1. Contorno, intervalos y pitch en memoria a corto plazo

Dowling & Fujitani (1971), con melodías breves novedosas y oyentes
occidentales:

- STRUCTURE: melodías estándar y comparaciones transpuestas o no
  transpuestas; comparaciones idénticas, de mismo contorno (mismas
  direcciones, distintos tamaños interválicos) o aleatorias. Ritmo
  constante entre estándar y comparación.
- PERCEPTION: tarea mismo/diferente en memoria a corto plazo.
- Hallazgo: sin transposición, los sujetos reconocían por pitch exacto
  (idéntica vs. contorno: fácil). Con transposición, la comparación
  idéntica se confundía casi totalmente con la de mismo contorno
  (discriminación apenas sobre el azar); el contorno se volvía la base del
  reconocimiento.
- Experimento 2 (folktunes familiares distorsionadas): el reconocimiento
  fue mejor que el azar conservando solo el contorno, y algo mejor
  conservando contorno + tamaños relativos de intervalos.
- Lectura prudente: el contorno es un rasgo relacional robusto cuando el
  pitch absoluto deja de estar disponible (transposición), pero el
  contorno solo no equivale a identidad: en memoria a corto plazo, misma
  vs. mismo-contorno transpuestas eran casi indistinguibles entre sí,
  pero ambas se distinguían de comparaciones aleatorias. Es evidencia
  sobre reconocimiento, no sobre juicio de misma idea.

### E2. Modelo de dos componentes: escala y contorno

Dowling (1978):

- Propone que la memoria de melodías combina (a) esquema de escala
  tonal sobreaprendido y (b) contorno melódico.
- Los intervalos exactos son difíciles de extraer en una sola escucha
  para no músicos; el contorno se retiene con facilidad; la representación
  tonal (qué escala/grados) sostiene el detalle interválico con
  aprendizaje y familiaridad.
- Lectura prudente: apoya una representación por grados de escala/función
  tonal además de contorno e intervalos físicos. Teoría dentro de la
  tradición tonal occidental; no establece ponderaciones universales.

### E3. Transposición y distancia tonal

Bartlett & Dowling (1980), cuatro experimentos con melodías novedosas y
familiares, niños y adultos, músicos y no músicos:

- STRUCTURE: estándares y comparaciones en misma tonalidad, tonalidad
  cercana o lejana; señuelos con intervalos alterados.
- PERCEPTION: detección de transposición exacta (aceptar transposiciones,
  rechazar señuelos).
- Hallazgo: efecto de distancia tonal robusto en falsas alarmas (señuelos
  en misma tonalidad o cercana generan más falsas alarmas que en tonalidad
  lejana), invariante en lo cualitativo a edad, experiencia y
  familiaridad; el nivel de acierto sí mejora con experiencia y
  familiaridad. No hubo efecto de distancia en los aciertos a
  transposiciones.
- Lectura prudente: la transposición exacta preserva las relaciones
  internas y es reconocible como tal, pero el contexto tonal (cercanía
  entre tonalidades) modula la confusión. Apoya que la identidad bajo
  transposición depende también del marco tonal, no solo de intervalos.

### E4. Inversión y retrógrado

Dowling (1971; 1972): el reconocimiento de inversiones, retrógrados y
retrógrados invertidos de melodías novedosas es difícil; la inversión
deteriora el reconocimiento respecto de la transposición exacta.

- Tensión con EXP-001 (ver "Contradictions"): en EXP-001, la inversión
  con ritmo y magnitudes conservados (D) obtuvo el juicio máximo (4).
  Las condiciones de tarea difieren radicalmente (reconocimiento de
  memoria vs. juicio comparativo A→candidato con repetición permitida,
  un solo evaluador, una sola melodía). No se resuelve a favor de
  ninguna; se registra como evidencia mixta dependiente de tarea.

### E5. Información interválica en memoria a largo plazo

Dowling & Bartlett (1981): en memoria a largo plazo de melodías, la
información interválica exacta gana importancia frente a lo observado en
memoria a corto plazo.

- Lectura prudente: la ponderación contorno vs. intervalos cambia con el
  tipo de memoria y la familiaridad. Ninguna jerarquía fija.

### E6. Acentos y reconocimiento

Jones & Ralston (1991): la estructura de acentos influye en el
reconocimiento de melodías (Memory & Cognition, 19, 8–20).

- STRUCTURE: manipulación de la estructura acentual/temporal.
- PERCEPTION: reconocimiento.
- Lectura prudente: el marco métrico-acentual es una dimensión propia de
  la identidad, no reducible a duraciones aisladas. Relevante para
  EXP-001 E (cambio de patrón temporal con pitches conservados): el
  parentesco puede sobrevivir a redistribuciones temporales si la
  estructura de alturas se conserva intacta, pero la colocación métrica
  de eventos es una variable a controlar, no un detalle menor.

### E7. Similitud melódica: el orden de factores cambia con la tarea

Prince (2014), oyentes occidentales, ratings de similitud con melodías
que varían en contorno de pitch, tonalidad, ritmo y metro:

- Experimento 1 (mismo tempo, sin contexto previo): el ritmo fue el
  mayor contribuyente a la similitud percibida, seguido de contorno,
  metro y tonalidad.
- Experimento 2 (tempo variado dentro del par + prefijo de 3 acordes que
  orienta al oyente): el contorno pasó a ser la influencia más fuerte,
  seguido de tonalidad y luego ritmo; el metro dejó de ser significativo.
- Lectura prudente: NO existe una jerarquía estable
  ritmo > pitch ni contorno > ritmo. La ponderación depende de las
  condiciones de escucha (estabilidad temporal, contexto tonal previo).
  Es evidencia sobre similitud, no sobre misma idea; pero refuta
  directamente cualquier regla universal del tipo "el ritmo es más
  importante que las notas" (cf. MEL-002 del borrador).

### E8. Modo, ritmo y contorno con melodías no familiares

Halpern, Bartlett & Dowling (1998), músicos y no músicos, jóvenes y
mayores, con melodías transpuestas que varían en ritmo, modo y/o
contorno:

- Exp. 1 (similitud): las melodías que diferían solo en modo se juzgaron
  las más similares; ritmo y contorno pesaban más, con el orden exacto
  dependiente del grupo (en músicos mayores, el contorno fue lo más
  distintivo).
- Exp. 2 (discriminación): ritmo y contorno se discriminaron bien
  (~0.80–0.88); el modo apenas sobre el azar en no músicos (~0.54–0.56).
- Lectura prudente: el modo/color tonal es sutil para oyentes no
  expertos, mientras ritmo y contorno sostienen la discriminación. La
  ponderación varía con experiencia y edad. Coherente con E7: sin
  jerarquía universal.

### E9. Jerarquías tonales como representación

Krumhansl & Kessler (1982); Krumhansl & Shepard (1979); Krumhansl (1979):

- Con el paradigma de probe-tone, oyentes occidentales califican los 12
  tonos cromáticos según su ajuste a un contexto tonal, produciendo
  perfiles estables de jerarquía tonal (tónica > tríada > resto
  diatónico > no diatónicos).
- Lectura prudente: los oyentes enculturados representan los pitches en
  términos de grados/funciones de escala, no solo como frecuencias o
  intervalos físicos. Esto fundamenta la dimensión "representación
  tonal/por grados" de RQ-MEL-001. Límite importante: los perfiles
  reflejan la tonalidad mayor/menor de práctica común y oyentes
  enculturados; estudios posteriores (p. ej., perfiles menos
  diferenciados en rock) muestran que la jerarquía se modula por estilo.
  No usar Krumhansl como prueba de identidad melódica: es evidencia
  sobre representación tonal, insumo para hipótesis de identidad.

### E10. Desarrollo: contorno temprano, intervalos con aprendizaje

Morrongiello, Trehub y colaboradores (1985): niños pequeños detectan
cambios de contorno y transposiciones, y perciben similitud a través de
transposiciones incluso en melodías no familiares; la sensibilidad a
intervalos exactos y a la tonalidad se desarrolla con edad y exposición
(Trehub et al. 1985, Psychomusicology).

- Lectura prudente: el contorno parece accesible temprano; el detalle
  interválico y tonal requiere enculturación. Evidencia convergente con
  E1–E2, en población infantil occidental.

## Structural Dimensions

Estado del conocimiento por dimensión (qué sabemos / qué NO sabemos):

- **Absolute pitch (altura absoluta):** sabemos que la identidad sobrevive
  a la transposición exacta en tareas de reconocimiento (E1, E3) y en
  EXP-001 (B=3). NO sabemos a qué distancia de transposición se degrada
  el parentesco en juicios de misma idea, ni cómo interactúa con el
  registro vocal/instrumental. Sin datos propios más allá de +2
  semitonos en una melodía.
- **Interval sequence (secuencia interválica exacta):** sabemos que su
  importancia crece con familiaridad y memoria a largo plazo (E5, E1-Exp2).
  NO sabemos qué desviación interválica rompe la misma idea en contexto
  compositivo.
- **Interval magnitude (magnitud):** EXP-001 C muestra que cambiar varias
  magnitudes (con ritmo y contorno intactos) puede bastar para degradar
  el parentesco a 2/4 en una realización concreta. Dowling & Fujitani
  muestran que magnitudes importan más en melodías familiares. NO sabemos
  si el efecto en C se debe a magnitudes per se, al cambio de color
  modal (C introduce Mi bemol: "triste") o a su combinación.
- **Contour/direction (contorno):** sabemos que es un rasgo relacional
  central y temprano (E1, E2, E10), pero insuficiente por sí solo para
  garantizar reconocimiento fuerte o misma idea (E1: misma vs.
  mismo-contorno casi indistinguibles; EXP-001 C=2 con contorno intacto).
  NO sabemos qué granularidad de contorno (signos globales vs. patrón
  exacto de giros) sostiene la misma idea.
- **Scale-degree / tonal representation (grados/función):** sabemos que
  los oyentes representan pitches jerárquicamente (E9) y que la
  distancia tonal modula la confusión (E3). NO sabemos cómo ponderar
  cambios que preservan función tonal frente a cambios que la alteran.
- **Rhythm (ritmo/duraciones):** sabemos que su peso en similitud es
  alto pero condicional (E7: primero en Exp.1, tercero en Exp.2) y que
  el parentesco puede sobrevivir a redistribuciones temporales si el
  pitch se conserva (EXP-001 E=4). NO sabemos qué tipos de cambio
  rítmico (redistribución vs. cambio de metro vs. desplazamiento
  acentual) rompen la misma idea.
- **Meter (metro/acentos):** sabemos que la estructura acentual influye
  en el reconocimiento (E6) y que el metro contribuye a la similitud en
  algunas condiciones pero no en otras (E7). NO sabemos cómo separar
  efecto métrico de efecto rítmico en juicios de misma idea.
- **Register (registro):** la transposición cambia necesariamente el
  registro; en EXP-001 B (+2 semitonos) el parentesco fue 3, no 4, con
  nota cualitativa "terminación más arriba". NO sabemos si esa
  penalización se debe al registro, a la distancia tonal o a ruido de
  medida (n=1). Sin evidencia externa directa en esta síntesis.
- **Transposition (transposición):** ver absolute pitch. E4 añade que
  inversiones y retrógrados son más difíciles que transposiciones en
  reconocimiento de melodías novedosas, en tensión parcial con EXP-001 D.
- **Tonal/harmonic context (contexto tonal/armónico):** E3 y E9 apoyan
  que el marco tonal modula reconocimiento y representación; E7-Exp2
  muestra que un prefijo armónico repondera los factores. EXP-001 usó
  melodía aislada sin armonía: sus resultados NO generalizan a melodía
  acompañada. La interacción melodía-armonía pertenece al dominio
  cross-domain.
- **Familiarity (familiaridad):** modula el nivel de rendimiento (E3) y
  el peso de los intervalos (E5, E1-Exp2). En composición, motivo nuevo
  vs. establecido son condiciones distintas; no tratarlas igual.
- **Interaction among features (interacción):** la evidencia converge en
  que los factores interactúan (E7, E8, E3). Ninguna fuente apoya efectos
  puramente aditivos ni una jerarquía fija.

## Context and Boundary Conditions

- Oyentes enculturados en tonalidad occidental en todas las fuentes
  externas. Nada de lo anterior se afirma de otras tradiciones.
- Melodías breves, aisladas, a menudo isócronas o con ritmo controlado;
  escucha de laboratorio, no escucha musical ecológica.
- Tareas de reconocimiento/similitud, no de juicio compositivo de misma
  idea (salvo EXP-001, n=1).
- Músicos vs. no músicos, edad y familiaridad modulan resultados (E3,
  E8, E10).
- La presencia de contexto tonal previo (acordes) repondera los factores
  (E7-Exp2).
- EXP-001: melodía aislada, MIDI piano, un evaluador, escala ordinal;
  no generaliza a melodía con armonía, letra, timbre vocal o producción.

## Contradictions / Mixed Evidence

1. **Jerarquía ritmo vs. pitch:** Prince 2014 Exp.1 (ritmo primero) vs.
   Exp.2 (contorno primero, ritmo tercero). El borrador MEL-002 ("el
   ritmo puede ser más importante que las notas") queda refutado como
   regla general y reformulado como dependencia de tarea/contexto.
   EXP-001 E=4 (pitch intacto, ritmo cambiado → máximo parentesco) es
   contraevidencia adicional contra la dominancia universal del ritmo.
2. **Contorno preservado + parentesco bajo:** EXP-001 C=2 con contorno y
   ritmo intactos tensiona la lectura ingenua de Dowling ("el contorno
   basta"). La literatura en realidad no dice eso: Dowling muestra que
   el contorno sostiene reconocimiento pero no identidad exacta. C
   sugiere que magnitudes + color modal pueden dominar al contorno en
   una realización concreta, sin establecer regla.
3. **Inversión:** Dowling 1971/1972 (inversión difícil en reconocimiento)
   vs. EXP-001 D=4 (inversión con ritmo+magnitudes → máximo parentesco).
   Diferencias de tarea (memoria vs. comparación directa con repetición),
   de material (una melodía, magnitudes conservadas exactamente) y de
   medida (n=1) impiden concluir; se registra como evidencia mixta.
4. **Transposición no máxima:** EXP-001 B=3 (no 4) pese a conservar todas
   las relaciones internas. Posibles lecturas: penalización por registro
   ("más arriba"), distancia tonal, o ruido de medida. La literatura
   (E3) hace plausibles las dos primeras sin decidir entre ellas.

## STRUCTURE → PERCEPTION → COMPOSITION

Para cada conclusión, se separan las tres capas. La implicación
compositiva nunca es más fuerte que la evidencia.

### SPC-1. Transposición exacta

- STRUCTURE: desplazamiento constante de todas las alturas; ritmo,
  intervalos, contorno intactos; registro y centro tonal desplazados.
- PERCEPTION: reconocida como relacionada en laboratorio (E1, E3);
  EXP-001: juicio 3/4 ("transformación de la misma idea").
- COMPOSITION (provisional): transportar un motivo es una estrategia
  disponible para conservar parentesco cambiando altura/registro; prever
  posible cambio de color por registro y distancia tonal. No garantiza
  máxima identidad.

### SPC-2. Contorno

- STRUCTURE: patrón de direcciones (signos interválicos).
- PERCEPTION: rasgo relacional robusto y temprano (E1, E2, E10), pero
  insuficiente por sí solo para identidad fuerte (E1; EXP-001 C=2).
- COMPOSITION (provisional): conservar el contorno es una forma
  disponible de retener un rasgo relacional durante la variación, pero
  puede no bastar para un juicio fuerte de misma idea si magnitudes,
  ritmo o marco tonal cambian sustancialmente.

### SPC-3. Magnitudes interválicas y color modal

- STRUCTURE: tamaños en semitonos; pertenencia diatónica/modal de los
  pitches resultantes.
- PERCEPTION: ganan peso con familiaridad y largo plazo (E5, E1-Exp2);
  EXP-001 C sugiere que cambiar varias magnitudes puede degradar el
  parentesco aun con contorno+ritmo intactos (una realización, n=1).
- COMPOSITION (provisional): al variar magnitudes, vigilar el cambio de
  color modal resultante (p. ej., alteraciones que cambian el modo
  percibido); el comentario "triste" de EXP-001 C ilustra el riesgo,
  sin medirlo.

### SPC-4. Ritmo y marco métrico-acentual

- STRUCTURE: duraciones, onsets, acentos, posición métrica.
- PERCEPTION: peso alto pero condicional en similitud (E7); la estructura
  acentual influye en el reconocimiento (E6); EXP-001 E muestra que
  redistribuir duraciones con pitch intacto puede conservar máximo
  parentesco (una realización, n=1).
- COMPOSITION (provisional): el ritmo es una palanca poderosa pero no
  universalmente dominante; redistribuir duraciones conservando alturas
  es una estrategia de variación disponible; los cambios que alteran la
  estructura acentual merecen atención separada.

### SPC-5. Representación tonal

- STRUCTURE: grados de escala, funciones, distancia entre tonalidades.
- PERCEPTION: los oyentes representan jerárquicamente (E9); la distancia
  tonal modula confusión (E3); el contexto armónico previo repondera
  factores (E7-Exp2).
- COMPOSITION (provisional): considerar en qué marco tonal se escucha
  cada aparición del motivo; un cambio de marco puede reponderar qué
  rasgo sostiene el parentesco. La interacción completa pertenece al
  dominio cross-domain.

## Project Experimental Evidence

EXP-001 (evidencia experimental propia, exploratoria; un evaluador, una
melodía base de 8 eventos / 6 beats, MIDI piano aislado, escala ordinal
1–4, juicio A→candidato):

| Condición | Transformación | Score |
|---|---|---:|
| B | Transposición exacta +2 st | 3 |
| C | Ritmo + contorno conservados, magnitudes cambiadas (6 de 7 intervalos) | 2 |
| D | Direcciones invertidas, ritmo + magnitudes conservados | 4 |
| E | Pitches conservados, patrón temporal modificado | 4 |
| F | Cambio multidimensional (ritmo + contorno + intervalos) | 2 |

Notas cualitativas originales: B "es la misma pero con terminación mas
arriba"; C "como si fuera la misma melodía pero en triste"; D "la misma
pero en diferente orden"; E "la misma solo que diferente ritmo"; F "al
inicio pero termina diferente". Expresión espontánea posterior sobre
preferencia ("me gustó") y emoción ("triste") registrada separadamente;
no forma parte del juicio de parentesco.

Interpretación aprobada (sin cambios en esta tarea): B compatible
parcialmente con H1; H2 no apoyada (C empató con F en 2); H3 no apoyada
(D y E en 4); H4 parcialmente apoyada (F bajo B/D/E, empatada con C).
El parentesco puede tolerar cambios grandes en una dimensión cuando
otras relaciones se conservan; ritmo y contorno por sí solos no fueron
suficientes en C. Sin atribución causal; sin generalización.

Limitaciones preservadas: un evaluador; una melodía; una realización por
condición; escala ordinal; 4 de 5 trials con repetición; melodía
aislada sin armonía/arreglo/letra; sin estimación estadística; diseño
no factorial; C–F no aíslan variables puras.

EXP-002: diseño de replicación pausado (A1–A3 × B–F, 15 trials), SIN
resultados perceptivos. No se utiliza como evidencia de ningún resultado
perceptivo.

## Candidate Compositional Implications

Implicaciones candidatas, todas provisionales (detalle en
`research/candidates/melody/`):

- CAND-MEL-001: la transposición exacta como estrategia de conservación
  de parentesco (con cautela de registro/marco tonal).
- CAND-MEL-002: conservar contorno sin conservar magnitudes/ritmo/marco
  puede no bastar para misma idea.
- CAND-MEL-003: en material familiar o repetido, el detalle interválico
  gana peso; variar magnitudes cambia más que en material nuevo.
- CAND-MEL-004: no presuponer jerarquía fija ritmo vs. pitch; decidir
  según contexto y función.
- CAND-MEL-005: los cambios que alteran función tonal/grados pesan
  distinto que los que la preservan (hipótesis, apoyo indirecto).
- CAND-MEL-006: la estructura acentual/métrica como dimensión propia a
  controlar en la variación.

Ninguna es regla aprobada. Ninguna entra en `manual/` ni `rules/`.

## What We Cannot Conclude

- No podemos concluir ninguna jerarquía universal (ritmo > pitch,
  contorno > intervalos, o inversas).
- No podemos concluir que el contorno defina la identidad.
- No podemos concluir ningún umbral ("variación se vuelve material nuevo
  tras X % de cambio", "un motivo debe tener N notas").
- No podemos concluir que la transposición preserve siempre la identidad
  (EXP-001 B=3, no 4; E3 muestra modulación tonal).
- No podemos concluir nada sobre memorabilidad, hook, preferencia o
  emoción desde esta evidencia (no medidas).
- No podemos generalizar fuera de oyentes enculturados occidentales ni a
  melodía acompañada, vocal o producida.
- No podemos atribuir causalidad a ninguna dimensión desde EXP-001
  (diseño no factorial, n=1).

En particular, MEL-001 y MEL-002 del borrador heredado quedan
clasificados como hipótesis no confirmadas en su forma general, no como
conocimiento.

## Open Questions

- ¿Qué granularidad de contorno sostiene la misma idea (direcciones
  globales vs. giros exactos)?
- ¿Qué magnitud y cantidad de cambio interválico rompe la misma idea, y
  cómo depende del cambio modal resultante?
- ¿Qué tipos de cambio rítmico (redistribución, cambio métrico,
  desplazamiento acentual) rompen la misma idea con pitch intacto?
- ¿Cómo interactúan registro, distancia tonal y pitch absoluto en
  juicios de misma idea?
- ¿Cómo cambia la ponderación con familiaridad (motivo nuevo vs.
  establecido) en contexto compositivo real?
- ¿Qué papel juega la armonía acompañante (dominio cross-domain)?
- ¿Cómo se relacionan similitud, misma idea, reconocimiento y
  memorabilidad entre sí (constructos separados, relaciones sin estudiar)?

## Need for Further Experimentation

La incertidumbre externa es moderada; la incertidumbre proyectual es
alta (n=1). No se justifica ahora un experimento nuevo distinto de la
replicación ya diseñada: el paso empírico lógico es EXP-002 (pausado),
que replica las familias B–F en tres bases nuevas. NO se reanuda
EXP-002 en esta tarea; queda como trabajo futuro pendiente de decisión
del Project Owner. Antes de cualquier EXP-003, EXP-002 debe ejecutarse.

## Source List

| ID | Fuente | Estado |
|---|---|---|
| SRC-ACADEMIC-001 | Dowling & Fujitani (1971) | VERIFIED |
| SRC-ACADEMIC-002 | Dowling (1978) | VERIFIED |
| SRC-ACADEMIC-003 | Bartlett & Dowling (1980) | VERIFIED |
| SRC-ACADEMIC-004 | Dowling (1971, 1972) inversión/retrógrado | VERIFIED |
| SRC-ACADEMIC-005 | Dowling & Bartlett (1981) | VERIFIED |
| SRC-ACADEMIC-006 | Jones & Ralston (1991) | VERIFIED (referencia completa) |
| SRC-ACADEMIC-007 | Prince (2014) | VERIFIED |
| SRC-ACADEMIC-008 | Halpern, Bartlett & Dowling (1998) | VERIFIED |
| SRC-ACADEMIC-009 | Krumhansl & Kessler (1982) + Krumhansl & Shepard (1979) | VERIFIED |
| SRC-ACADEMIC-010 | Morrongiello / Trehub y col. (1985) desarrollo | VERIFIED (parcial: datos extraídos desde resúmenes y citas cruzadas; sin acceso al texto completo) |
| SRC-ACADEMIC-090 | "Pick et al." (mención sin referencia completa) | UNVERIFIED |

Detalles y DOI en `research/sources/academic/`.
