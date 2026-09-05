# Constructo de continuidad entre realizaciones armónicas

## Estado

Síntesis de `RQ-CROSS-004`. Es investigación construct-first: no compara
voicings y no establece una regla de voice leading.

## Conclusión

La literatura inspeccionada no ofrece una operacionalización directa y estable
de “continuidad entre sucesivas realizaciones armónicas”. Sí ofrece un
constructo más estrecho y utilizable: **perceived musical distance between
successive sonorities**.

Rogers y Callender (2006) presentaron pares de trichords sucesivos y pidieron
ratings de distance. El total de movimiento se relacionó con mayor distance;
los tonos comunes tendieron a reducirla. La métrica taxicab no fue suficiente:
dirección, número de voces, afinación y tamaño de los desplazamientos también
interactuaron.

Esto es evidencia perceptiva directa para una tarea de distance, no para
continuidad compositiva. `Voice-leading distance -> perceived continuity`
queda en `PARTIAL`.

Wall et al. (2020) muestran que voice leading y armonía influyen en la
expectativa de secuencias polifónicas mediante tiempos de reacción. El
resultado indica procesamiento y expectativa, no un rating de smoothness o
continuidad.

Milne y Holland (2016) comparan modelos de distance triádica percibida,
incluidos voice-leading distance, Tonnetz, distancia espectral y tonos
comunes. Su valor es metodológico: distintos modelos pueden compararse contra
juicios perceptivos; no hay un modelo universal de continuity.

Eerola y Lahdelma (2022) muestran que registro afecta ratings de consonance
mediante roughness y sharpness. Esto es una propiedad estática de sonoridad,
no una medida secuencial de continuity.

## Matriz resumida

| Constructo | Nivel | Medida | Relación con continuity |
|---|---|---|---|
| Voice-leading distance | Analítico/perceptivo | Rating de distance | Parcial |
| Common-tone retention | Analítico con efecto perceptivo acotado | Conteo + distance | Parcial |
| Smoothness | Teórico/pedagógico heterogéneo | Sin tarea homogénea | No establecida |
| Connectedness | Perceptivo/compositivo | Sin tarea directa estable | No establecida |
| Roughness | Acústico/perceptivo | Modelo + consonance rating | No establecida |
| Similarity | Perceptivo | Rating de parecido/distance | Parcial, no proxy |
| Voice streaming | Perceptivo | Integración/segregación | Parcial local |
| Preference | Perceptivo | Agrado/elección | Inadecuada por defecto |

## Restricciones de transferencia

```text
static roughness != sequential continuity
common tones != global connectedness automatically
minimum motion != optimal realization
individual voice tracking != global harmonic continuity
distance != continuity
```

La fuente más cercana al objetivo es la tarea secuencial de distance
percibida, pero su estímulo sintético y trichordal no representa una textura
popular completa. La transferencia es `PARTIAL`.

## Frontera Phase 2

`REALIZATION RANKING` permanece **CONSTRUCT-FIRST BLOCKED** para continuity
amplia. Queda **READY WITH SCOPED OPERATIONALIZATION** solo para una futura
comparación cuyo criterio sea distance percibida y cuyo alcance controle las
variables relevantes.

## Fuentes

- `SRC-EMPIRICAL-029`: Rogers y Callender, juicios de distance entre trichords.
- `SRC-EMPIRICAL-030`: Wall, Lieck, Neuwirth y Rohrmeier, voice leading y expectancy.
- `SRC-EMPIRICAL-031`: Milne y Holland, modelos de distance triádica percibida.
- `SRC-EMPIRICAL-032`: Eerola y Lahdelma, register, roughness y consonance.

## Recommended next step

Auditar `CAND-CROSS-004`; no iniciar todavía una comparación A/B.
