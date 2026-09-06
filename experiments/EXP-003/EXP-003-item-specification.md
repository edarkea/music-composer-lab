# EXP-003 - Item specification candidate pool

## Estado y alcance

Este documento pertenece a la fase `ITEM SPECIFICATION`. Contiene pitches
simbolicos y calculos estructurales offline; no contiene MIDI, audio, SongPlan,
participantes ni respuestas.

El pool usa cuatro voces estructurales ordenadas de grave a agudo:
`V1 -> V1`, `V2 -> V2`, `V3 -> V3`, `V4 -> V4`. La identidad estructural no
implica que el oyente perciba cuatro streams auditivos independientes.

La unidad de independencia es `item_family_id`. Las transposiciones futuras de
una familia no se contaran como familias independientes.

## Bounded scope

Se incluyen transiciones sinteticas de cuatro voces con acordes mayores,
menores, dominantes y mayores/menores con septima dentro de un marco tonal
occidental funcional simplificado. Se excluyen canciones reconocibles, melodia
privilegiada, texturas completas, modulacion, cambios de tempo, cambios de
timbre y generalizaciones a popular song.

`R1` es identico en A/B. `R2_LOW` y `R2_HIGH` conservan identidad armonica,
pitch-class multiplicity, bajo e inversion; la unica manipulacion prevista es
la realizacion bajo la metrica local de movimiento.

## Metadata schema

Cada familia futura debe conservar como minimo:

```yaml
item_family_id: EXP003-FXX
harmonic_context: "..."
H1_identity: "..."
H2_identity: "..."
R1_pitches: ["...", "...", "...", "..."]
R2_LOW_pitches: ["...", "...", "...", "..."]
R2_HIGH_pitches: ["...", "...", "...", "..."]
voice_count: 4
doubling_pattern: "..."
bass_LOW: "..."
bass_HIGH: "..."
inversion_LOW: "..."
inversion_HIGH: "..."
available_common_tones: ["..."]
retained_common_tones_LOW: ["..."]
retained_common_tones_HIGH: ["..."]
retained_exact_pitches_LOW: ["..."]
retained_exact_pitches_HIGH: ["..."]
retaining_voices_LOW: ["..."]
retaining_voices_HIGH: ["..."]
motion_vector_LOW: [0, 0, 0, 0]
motion_vector_HIGH: [0, 0, 0, 0]
total_motion_LOW: 0
total_motion_HIGH: 0
motion_contrast: 0
max_motion_LOW: 0
max_motion_HIGH: 0
moving_voice_count_LOW: 0
moving_voice_count_HIGH: 0
span_LOW: 0
span_HIGH: 0
register_descriptor_LOW: "..."
register_descriptor_HIGH: "..."
spacing_profile_LOW: [0, 0, 0]
spacing_profile_HIGH: [0, 0, 0]
voice_crossing_LOW: false
voice_crossing_HIGH: false
endpoint_match_status: GOOD
eligibility_status: ELIGIBLE
exclusion_reason: null
```

`motion_vector` conserva signos; `total_motion` es la suma de valores
absolutos. `span` y `spacing_profile` estan expresados en semitonos. Los
descriptores de registro se expresan como `lowest-highest / mean_midi`.

## Historical manual pool (diagnostic only)

Los pitches aparecen en orden `V1, V2, V3, V4`. Cada fila satisface
estructuralmente `A: R1 -> R2_LOW` y `B: R1 -> R2_HIGH` salvo la familia
marcada `INELIGIBLE`.

| ID | Harmonic context | R1 | R2_LOW | R2_HIGH | H2 / doubling | common-tone retention | motion LOW -> HIGH | endpoint / status |
|---|---|---|---|---|---|---|---|---|
| EXP003-F01 | C major I -> G major V | C3 E3 C4 G4 | G2 D3 B3 G4 | G2 B3 D4 G4 | G,B,D,G / G doubled | G4 in V4 -> G4 in V4 | [-5,-2,-1,0] 8 -> [-5,7,2,0] 14 | ACCEPTABLE WITH SCOPE / ELIGIBLE_WITH_CAUTION |
| EXP003-F02 | D minor ii -> A major V | D3 F3 D4 A4 | A2 E3 C#4 A4 | A2 C#4 E4 A4 | A,C#,E,A / A doubled | A4 in V4 -> A4 in V4 | [-5,-1,-1,0] 7 -> [-5,8,2,0] 15 | ACCEPTABLE WITH SCOPE / ELIGIBLE_WITH_CAUTION |
| EXP003-F03 | E minor iii -> B major V | E3 G3 E4 B4 | B2 F#3 D#4 B4 | B2 D#4 F#4 B4 | B,D#,F#,B / B doubled | B4 in V4 -> B4 in V4 | [-5,-1,-1,0] 7 -> [-5,8,2,0] 15 | ACCEPTABLE WITH SCOPE / ELIGIBLE_WITH_CAUTION |
| EXP003-F04 | F major IV -> C major I | F3 A3 C4 A4 | C3 G3 C4 E4 | C3 E3 C4 G4 | C,C,E,G / C doubled | C4 in V3 -> C4 in V3 | [-5,-2,0,-2] 9 -> [-5,-5,0,-2] 12 | ACCEPTABLE WITH SCOPE / ELIGIBLE_WITH_CAUTION |
| EXP003-F05 | G major V -> C major I | G3 B3 D4 B4 | C3 E4 G4 C5 | C3 G3 C4 E4 | C,C,E,G / C doubled | no exact pitch retained in either realization | [-7,1,2,-4] 14 -> [-7,-4,-2,-4] 17 | ACCEPTABLE WITH SCOPE / ELIGIBLE_WITH_CAUTION |
| EXP003-F06 | A minor vi -> F major IV | A3 C4 E4 C5 | F3 C4 F4 A4 | F3 A3 C4 F4 | F,F,A,C / F doubled | low retains C4 in V2; high retains C4 in V3 | [-4,0,1,-3] 8 -> [-4,-3,-4,-3] 14 | POOR / INELIGIBLE |
| EXP003-F07 | G major I -> E major vi | B3 D4 G4 D5 | E3 B3 G#4 E5 | E3 G#3 E4 B4 | E,E,G#,B / E doubled | no exact pitch retained in either realization | [-7,-3,1,2] 13 -> [-7,-6,-3,-3] 19 | ACCEPTABLE WITH SCOPE / ELIGIBLE_WITH_CAUTION |
| EXP003-F08 | C major I -> A major vi | C3 E3 G3 B3 | A3 C#4 E4 E5 | A3 E4 C#5 E5 | A,C#,E,E / E doubled | no exact pitch retained in either realization | [9,9,9,17] 44 -> [9,12,18,17] 56 | ACCEPTABLE WITH SCOPE / ELIGIBLE_WITH_CAUTION |
| EXP003-F09 | D7 ii7 -> G7 V7 | D3 F#3 A3 C4 | G3 B3 D4 F4 | G3 D4 F4 B4 | G,B,D,F / no doubling | no exact pitch retained in either realization | [5,5,5,5] 20 -> [5,8,8,11] 32 | ACCEPTABLE WITH SCOPE / ELIGIBLE_WITH_CAUTION |
| EXP003-F10 | E7 iii7 -> C7 bVI7 | E3 G#3 B3 D4 | C3 G3 Bb3 E4 | C3 E3 G3 Bb3 | C,E,G,Bb / no doubling | no exact pitch retained in either realization | [-4,-1,-1,2] 8 -> [-4,-4,-4,-4] 16 | ACCEPTABLE WITH SCOPE / ELIGIBLE_WITH_CAUTION |
| EXP003-F11 | G7 V7 -> Dm7 ii7 | G3 B3 D4 F4 | D3 A3 C4 F4 | D3 F3 A3 C4 | D,F,A,C / no doubling | no exact pitch retained in either realization | [-5,-2,-2,0] 9 -> [-5,-6,-5,-5] 21 | ACCEPTABLE WITH SCOPE / ELIGIBLE_WITH_CAUTION |
| EXP003-F12 | A major IV -> E7 V7 | A3 C#4 E4 A4 | E3 B3 D4 G#4 | E3 G#3 B3 D4 | E,G#,B,D / no doubling | no exact pitch retained in either realization | [-5,-2,-2,-1] 10 -> [-5,-5,-5,-7] 22 | ACCEPTABLE WITH SCOPE / ELIGIBLE_WITH_CAUTION |

### Historical exact structural metadata

| ID | bass LOW/HIGH | inversion LOW/HIGH | span LOW/HIGH | mean MIDI LOW/HIGH | spacing LOW/HIGH | max motion LOW/HIGH | moving voices LOW/HIGH | crossing LOW/HIGH |
|---|---|---|---|---|---|---|---|---|
| F01 | G2 / G2 | root / root | 24 / 24 | 54.75 / 57.75 | 7,9,8 / 16,3,5 | 5 / 7 | 3 / 3 | false / false |
| F02 | A2 / A2 | root / root | 24 / 24 | 56.75 / 59.75 | 7,9,8 / 16,3,5 | 5 / 8 | 3 / 3 | false / false |
| F03 | B2 / B2 | root / root | 24 / 24 | 58.75 / 61.75 | 7,9,8 / 16,3,5 | 5 / 8 | 3 / 3 | false / false |
| F04 | C3 / C3 | root / root | 19 / 19 | 57.50 / 56.75 | 7,5,7 / 4,8,7 | 5 / 5 | 3 / 3 | false / false |
| F05 | C3 / C3 | root / root | 19 / 19 | 59.75 / 57.50 | 12,4,3 / 7,5,7 | 7 / 7 | 4 / 4 | false / false |
| F06 | F3 / F3 | root / root | 16 / 12 | 61.25 / 60.75 | 7,8,5 / 7,5,5 | 4 / 4 | 3 / 3 | false / false |
| F07 | E3 / E3 | root / root | 24 / 19 | 63.75 / 60.75 | 7,9,8 / 4,8,7 | 7 / 7 | 4 / 4 | false / false |
| F08 | A3 / A3 | root / root | 19 / 19 | 64.50 / 67.50 | 4,3,12 / 7,9,3 | 17 / 18 | 4 / 4 | false / false |
| F09 | G3 / G3 | root / root | 10 / 16 | 60.25 / 63.25 | 4,3,3 / 7,3,6 | 5 / 11 | 4 / 4 | false / false |
| F10 | C3 / C3 | root / root | 16 / 10 | 56.25 / 53.25 | 7,3,6 / 4,3,3 | 4 / 4 | 4 / 4 | false / false |
| F11 | D3 / D3 | root / root | 15 / 10 | 58.00 / 55.00 | 7,3,5 / 3,4,3 | 5 / 6 | 4 / 4 | false / false |
| F12 | E3 / E3 | root / root | 16 / 10 | 60.25 / 57.25 | 7,3,4 / 4,3,3 | 5 / 7 | 4 / 4 | false / false |

## Historical manual eligibility (superseded)

- `ELIGIBLE`: ninguna sin cautela.
- `ELIGIBLE_WITH_CAUTION`: F01-F05 y F07-F12 (11 familias).
- `INELIGIBLE`: F06 (1 familia).

F06 se excluye porque la retencion exacta del common tone C4 cambia de voz
estructural entre condiciones. Las otras 11 familias no presentan ese fallo,
pero todas conservan alguna diferencia de span, centro registral, spacing o
maximo individual que debe ser revisada antes de un item freeze. Ninguna
familia usa una transposicion global de octava como unica fuente del contraste.

El pool contiene 11 familias utilizables en principio, pero ninguna es limpia
sin cautela adicional. Por tanto, la existencia de un pool suficientemente
grande para la prueba primaria es **UNCERTAIN** hasta que el Director revise
las diferencias estaticas y acepte la interpretacion de realizacion
seleccionada, en lugar de un efecto causal puro de motion.

Con estos items, el lenguaje recomendado es: `lower-motion-selected
realization` frente a `higher-motion-selected realization`. No se debe afirmar
que la magnitud analitica de movimiento aislada causa el juicio perceptual.

## Offline validation performed

Se comprobaron conceptualmente y mediante calculo estructural offline:

- un unico `voice_count: 4`;
- `R1` identico entre A/B;
- identidad de pitch classes y multiplicidad de R2;
- bajo e inversion root identicos;
- ausencia de voice crossing;
- correspondencia V1-V4 determinista;
- `total_motion_LOW < total_motion_HIGH` en F01-F05 y F07-F12;
- calculo de vectores, total, maximo y voces moviles;
- span, media registral y spacing de ambos endpoints;
- cumplimiento de Strategy B en las familias no excluidas;
- deteccion manual de la familia F06 por common-tone retention desigual.

Estos son checks estructurales, no validacion perceptual.

## Counterbalancing architecture

No se ejecuta randomizacion. La asignacion conceptual usa dos listas
complementarias sobre las mismas familias:

- `List 1`: familias impares LOW; familias pares HIGH.
- `List 2`: familias impares HIGH; familias pares LOW.

Cada participante recibira una sola condicion por familia y ambas condiciones a
lo largo del experimento. Las transposiciones de una familia no se asignaran a
un mismo participante como si fueran familias nuevas. El orden de trials se
aleatorizara solo en una fase posterior autorizada.

## Freeze state

- `DESIGN FREEZE`: incompleto.
- `ITEM SPECIFICATION`: completada como pool candidato.
- `ITEM FREEZE`: no autorizado.
- `MIDI FREEZE`: no autorizado.
- `AUDIO FREEZE`: no autorizado.
- `PILOT FREEZE`: no autorizado.

No se han generado MIDI, audio, SongPlans ni datos de participantes.

**READY FOR ITEM-FREEZE AUDIT: NO.** El pool es prometedor, pero las once
familias supervivientes requieren revision de sus diferencias estaticas antes
de poder congelarse.

## Reconstructed pool from frozen matched-contrast procedure

Esta seccion es la especificacion operativa posterior a la reconstruccion. La
tabla manual anterior se conserva solo para comparacion diagnostica y no
determina la seleccion.

### Frozen construction space

Para cada familia se conserva el `R1` previamente declarado como parte de la
identidad del item. Se enumeran todas las realizaciones de `R2` que cumplen:

- cuatro pitches ordenados, uno por voz estructural;
- V1 dentro de MIDI `43..59`, V2 `48..67`, V3 `55..76`, V4 `60..81`;
- pitch-class multiplicity de H2 exacta;
- V1 con el pitch class del root de H2, es decir, inversion root;
- spacing adyacente entre `3..19` semitonos y span total entre `12..31`;
- ausencia de crossing;
- igualdad de `moving_voice_count` dentro del par;
- igualdad de common-tone retention, incluyendo voces estructurales.

Los limites son restricciones de construccion para excluir realizaciones
patologicas y desplazamientos globales de octava; no son umbrales perceptuales
ni reglas compositivas.

Los controles anteriores son `HARD MATCH`: identidad armonica, doubling,
bass/inversion, voice count, Strategy B, crossing, rangos de construccion y
`moving_voice_count`. Span, centroide, spacing, maximo individual y patron de
distribucion son `SOFT MATCH DESCRIPTORS`: orientan la seleccion y se registran
como parte del tratamiento, pero no se convierten en igualdad artificial.

### Frozen selection algorithm

Se considero Pareto filtering, pero no se adopta como decision final porque
puede dejar una frontera con multiples pares no ordenados. El procedimiento
seleccionado es lexicografico y deterministicamente tie-broken:

1. enumerar todas las realizaciones del espacio anterior;
2. formar pares con mismo H2, bass pitch class, inversion, common-tone
   retention y `moving_voice_count`;
3. eliminar pares con igual total motion;
4. ordenar por `abs(delta_span)`, `abs(delta_centroid)`,
   `abs(delta_max_adjacent_spacing)`, `abs(delta_min_adjacent_spacing)`,
   `spacing_profile_L1`, `abs(delta_max_motion)`;
5. dentro del primer empate, elegir el mayor `motion_contrast`;
6. resolver cualquier empate restante por la lista MIDI lexicografica de LOW y
   HIGH.

LOW/HIGH son relativos al par seleccionado. No se eligen los extremos globales
de la familia y no se usa ningun score ponderado.

### Enumeration and reconstruction results

`R2 alternatives` es el numero de realizaciones validas antes de formar pares.
`all pairs` es `n*(n-1)/2`. `hard pairs` son los pares restantes tras igualdad
de common-tone retention, moving-voice count y total motion distinto.

| Item | R2 alternatives | all pairs | hard pairs | LOW pitches / total | HIGH pitches / total | contrast | endpoint deltas: span / centroid / max spacing / min spacing / spacing L1 |
|---|---:|---:|---:|---|---|---:|---|
| F01 | 17 | 136 | 83 | G2 G3 D4 B4 / 14 | G2 D3 G4 B4 / 18 | 4 | 0 / 0 / 5 / 3 / 20 |
| F02 | 20 | 190 | 114 | A2 A3 E4 C#5 / 15 | A2 E3 A4 C#5 / 17 | 2 | 0 / 0 / 5 / 3 / 20 |
| F03 | 17 | 136 | 75 | B2 B3 F#4 D#5 / 15 | B2 F#3 B4 D#5 / 17 | 2 | 0 / 0 / 5 / 3 / 20 |
| F04 | 16 | 120 | 64 | C3 C4 G4 E5 / 22 | C3 G3 C5 E5 / 26 | 4 | 0 / 0 / 5 / 3 / 20 |
| F05 | 16 | 120 | 107 | C3 C4 G4 E5 / 18 | C3 G3 C5 E5 / 26 | 8 | 0 / 0 / 5 / 3 / 20 |
| F06 | 9 | 36 | 9 | F3 A3 C4 F5 / 16 | F3 A3 C5 F5 / 20 | 4 | 0 / 3 / 2 / 1 / 24 |
| F07 | 10 | 45 | 34 | E3 E4 B4 G#5 / 19 | E3 B3 E5 G#5 / 25 | 6 | 0 / 0 / 5 / 3 / 20 |
| F08 | 8 | 28 | 12 | A2 C#3 E4 E5 / 32 | A2 C#4 E4 E5 / 38 | 6 | 0 / 3 / 1 / 1 / 24 |
| F09 | 15 | 105 | 97 | G2 B3 F4 D5 / 34 | G2 F3 B4 D5 / 36 | 2 | 0 / 0 / 2 / 3 / 24 |
| F10 | 15 | 105 | 98 | C3 Bb3 E4 G5 / 28 | C3 E3 Bb4 G5 / 36 | 8 | 0 / 0 / 3 / 2 / 24 |
| F11 | 13 | 78 | 58 | D3 C4 F4 F5 / 25 | D3 F3 C5 F5 / 33 | 8 | 0 / 1 / 1 / 4 / 20 |
| F12 | 9 | 36 | 35 | E3 D4 B4 G#5 / 24 | E3 B3 D5 G#5 / 28 | 4 | 0 / 0 / 5 / 3 / 12 |

Hay 12 pares seleccionados despues de hard filtering y 12 despues de la
seleccion lexicografica. La diferencia de motion es siempre positiva, pero
varia entre 2 y 8 semitonos.

### Original manual-pair comparison

- `SAME PAIR`: 0.
- `DIFFERENT PAIR`: 9 (F01-F03, F07-F12).
- `NO ELIGIBLE PAIR`: 3 (F04-F06); las parejas manuales violaban la
  multiplicidad o la igualdad de common-tone retention.

La comparacion es diagnostica: no se modifico el algoritmo para reproducir las
parejas manuales.

### Reconstructed eligibility and pool audit

- `POLICY_ELIGIBLE`: 0.
- `POLICY_ELIGIBLE_WITH_CAUTION`: 12.
- `POLICY_INELIGIBLE`: 0.
- `PURE_MOTION_ELIGIBLE`: 0.
- `PURE_MOTION_INELIGIBLE`: 12.

El tratamiento es reproducible, pero el pool sigue siendo de cautela porque la
seleccion produce perfiles de spacing sistematicamente distintos, aunque span
y centroide quedan igualados en 10 de 12 familias. F06 y F08 tienen una
diferencia de centroide; F08 ademas presenta el contraste de maximo individual
mas alto. No hay una caracteristica sistematica de bass, inversion, doubling o
common-tone retention que se oponga al estimando de politica.

Covariacion del pool reconstruido:

- span: `BALANCED / NONSYSTEMATIC` salvo F06 y F08 con deltas registrados;
- centroid: `MILD DIRECTIONAL COVARIATION`, no una direccion uniforme;
- spacing: `STRONG SYSTEMATIC COVARIATION` en el descriptor de maximo spacing:
  HIGH es mas abierto o irregular en la mayoria de las familias;
- max individual motion: `BALANCED / NONSYSTEMATIC` en el subconjunto
  seleccionado, aunque sigue siendo parte del tratamiento;
- moving voice count: `BALANCED / NONSYSTEMATIC`, igual en las 12 familias;
- motion distribution: `MILD DIRECTIONAL COVARIATION`, HIGH contiene con
  frecuencia un movimiento mas concentrado;
- common-tone realization: `BALANCED / NONSYSTEMATIC`;
- literal bass register: `BALANCED / NONSYSTEMATIC`; ambos endpoints conservan
  el mismo pitch literal de bajo dentro de cada familia reconstruida.

La covariacion fuerte de spacing impide declarar el pool listo para item freeze.
La politica puede estudiarse solo si el Director acepta que spacing forma parte
de la realizacion seleccionada y no se atribuye el resultado a motion aislado.

### Authorization after reconstruction

- `OFFLINE STRUCTURAL ANALYSIS: AUTHORIZED`.
- `ITEM FREEZE: NOT AUTHORIZED YET`.
- `MUSIC-ENGINE: NOT AUTHORIZED`.
- `MIDI: NOT AUTHORIZED`.
- `AUDIO: NOT AUTHORIZED`.
- `PILOT: NOT AUTHORIZED`.
- `EXECUTION: NOT AUTHORIZED`.

**Viable reconstructed policy pool: UNCERTAIN.**

**READY FOR ITEM-FREEZE AUDIT: NO.**

## Historical pre-reconstruction audit (superseded)

The following section records the pre-reconstruction diagnosis. Its counts and
manual-pair classifications are historical only. The authoritative procedure,
pool and reclassification are in **Reconstructed pool from frozen
matched-contrast procedure** above.

### Estimands

- **Estimand A - pure motion effect:** `NOT SUPPORTED` por el pool actual.
  Las realizaciones LOW/HIGH difieren tambien en spacing, distribucion y, en
  varias familias, span o centro registral. No se debe presentar el
  coeficiente de condicion como efecto causal de motion magnitude.
- **Estimand B - lower-motion-selection policy:** `SUPPORTED WITH SCOPE`.
  El pool puede comparar la decision de seleccionar una realizacion con menor
  frente a mayor motion, siempre que el procedimiento de seleccion se congele
  antes de datos y el resultado se interprete como politica de realizacion.

El estimando primario seleccionado es **B**, porque corresponde a la decision
compositiva real: escoger entre realizaciones validas cuando perceived distance
es el criterio activo. Una politica de seleccion puede ser util aunque no
identifique un mecanismo psicoacustico puro, siempre que no se confundan ambos
claims.

### Ancillary delta table

Los deltas son `HIGH - LOW`; los perfiles de spacing se muestran como
`LOW -> HIGH`. `CT equal` significa que la retencion realizada y sus voces son
iguales; F06 no aparece porque es inelegible.

| Item | motion contrast | delta span | delta centroid | spacing LOW -> HIGH | delta max | delta moving voices | CT equal | risk |
|---|---:|---:|---:|---|---:|---:|---|---|
| F01 | 6 | 0 | +3.00 | 7,9,8 -> 16,3,5 | +2 | 0 | yes | SPACING_DIFFERENCE; REGISTER_DIFFERENCE |
| F02 | 8 | 0 | +3.00 | 7,9,8 -> 16,3,5 | +3 | 0 | yes | SPACING_DIFFERENCE; REGISTER_DIFFERENCE |
| F03 | 8 | 0 | +3.00 | 7,9,8 -> 16,3,5 | +3 | 0 | yes | SPACING_DIFFERENCE; REGISTER_DIFFERENCE |
| F04 | 3 | 0 | -0.75 | 7,5,7 -> 4,8,7 | 0 | 0 | yes | SPACING_DIFFERENCE |
| F05 | 3 | 0 | -2.25 | 12,4,3 -> 7,5,7 | 0 | 0 | yes | SPACING_DIFFERENCE; REGISTER_DIFFERENCE |
| F07 | 6 | -5 | -3.00 | 7,9,8 -> 4,8,7 | 0 | 0 | yes | SPAN_DIFFERENCE; REGISTER_DIFFERENCE; SPACING_DIFFERENCE |
| F08 | 12 | 0 | +3.00 | 4,3,12 -> 7,9,3 | +1 | 0 | yes | SPACING_DIFFERENCE; MAX_LEAP_DIFFERENCE |
| F09 | 12 | +6 | +3.00 | 4,3,3 -> 7,3,6 | +6 | 0 | yes | SPAN_DIFFERENCE; REGISTER_DIFFERENCE; MAX_LEAP_DIFFERENCE |
| F10 | 8 | -6 | -3.00 | 7,3,6 -> 4,3,3 | 0 | 0 | yes | SPAN_DIFFERENCE; REGISTER_DIFFERENCE |
| F11 | 12 | -5 | -3.00 | 7,3,5 -> 3,4,3 | +1 | 0 | yes | SPAN_DIFFERENCE; REGISTER_DIFFERENCE; SPACING_DIFFERENCE |
| F12 | 12 | -6 | -3.00 | 7,3,4 -> 4,3,3 | +2 | 0 | yes | SPAN_DIFFERENCE; REGISTER_DIFFERENCE |

### Condition-level covariation

- **Span:** `MILD DIRECTIONAL COVARIATION`; HIGH has smaller span in four
  families and larger span in one, while the rest are equal.
- **Register centroid:** `BALANCED / NONSYSTEMATIC`; six HIGH endpoints are
  higher and five lower, although most absolute deltas are about three MIDI
  units.
- **Spacing:** `MILD DIRECTIONAL COVARIATION`; HIGH frequently redistributes
  spacing into a more uneven profile, but it does not consistently mean only
  close or only open spacing.
- **Maximum motion:** `MILD DIRECTIONAL COVARIATION`; HIGH is never lower and
  is higher in several families. This is partly constitutive of the treatment,
  but remains an ancillary feature to record.
- **Moving-voice count:** `BALANCED / NONSYSTEMATIC`; all surviving families
  have equal counts within A/B.
- **Motion distribution:** `MILD DIRECTIONAL COVARIATION`; HIGH generally has
  larger or more uneven individual moves, but the pool is not uniformly “many
  small vs one enormous leap”.
- **Literal bass register:** `BALANCED / NONSYSTEMATIC`; bass pitch is equal
  within every surviving family.

No surviving item uses a gross octave relocation as the primary construction
trick. Nevertheless, F08-F12 contain larger endpoint or individual-motion
differences and should not be treated as clean pure-motion items.

### Reclassification by estimand

| Item group | Pure motion | Policy |
|---|---|---|
| F01-F05, F07-F12 | `PURE_MOTION_INELIGIBLE` | `POLICY_ELIGIBLE_WITH_CAUTION` |
| F06 | `PURE_MOTION_INELIGIBLE` | `POLICY_INELIGIBLE` |

Thus: `PURE_MOTION_ELIGIBLE = 0`, `PURE_MOTION_INELIGIBLE = 12`,
`POLICY_ELIGIBLE = 0`, `POLICY_ELIGIBLE_WITH_CAUTION = 11`,
`POLICY_INELIGIBLE = 1`.

### Selection procedure audit

The current families were **manually constructed**, not selected by a frozen
enumeration-and-matching algorithm. They must not be frozen as if they were an
unbiased sample of the realization space.

Recommended reproducible procedure for later methodological approval:

1. enumerate valid R2 realizations under the fixed harmonic, voice-count,
   doubling, bass, inversion, crossing and register constraints;
2. calculate the declared motion vector and total for every realization;
3. enforce Strategy B common-tone equality;
4. form LOW/HIGH pairs using a predeclared matched-contrast objective that
   minimizes ancillary endpoint differences while requiring LOW total motion
   below HIGH total motion;
5. record all rejected candidates and reasons before selecting the pool.

The recommended strategy is **MATCHED CONTRAST**, not extreme minimum-versus-
maximum selection. A smaller but better-controlled contrast has more useful
interpretation for the composer decision than a large contrast produced by
gross spacing or register changes. No new selection algorithm is implemented
in this audit.

### Treatment definition

For a future policy experiment:

- `LOW_SELECTED`: the realization selected by the frozen procedure with the
  lower declared motion metric within an eligible family.
- `HIGH_SELECTED`: the matched realization selected by the same procedure with
  the higher declared metric.

The treatment is the complete realization-selection condition. The analysis
may estimate `LOW_SELECTED` versus `HIGH_SELECTED`, but not a causal effect per
semitone or a post-hoc dose-response relationship.

### Gate and authorization result

- Gate B: `PASS WITH SCOPE`; reproducible LOW/HIGH selection still needs to be
  frozen.
- Gate C: `PASS WITH SCOPE` for the policy estimand; insufficient for pure
  motion.
- Gates A, D, E and F: preserved as `PASS`, `PASS WITH SCOPE`, `NOT YET PASS`
  and `PASS WITH SCOPE`, respectively.
- `OFFLINE STRUCTURAL ANALYSIS: AUTHORIZED`.
- `ITEM FREEZE: NOT AUTHORIZED YET`.
- `MUSIC-ENGINE: NOT AUTHORIZED`.
- `MIDI: NOT AUTHORIZED`.
- `AUDIO: NOT AUTHORIZED`.
- `PILOT: NOT AUTHORIZED`.
- `EXECUTION: NOT AUTHORIZED`.

**READY FOR ITEM-FREEZE AUDIT: NO.** Primero debe aprobarse el estimando de
politica y el procedimiento reproducible de seleccion; no se inicia el freeze
automaticamente.

## Item-freeze audit result

### Freeze eligibility

La auditoria del estimando de politica acepta que spacing, span, registro y
distribucion sean atributos correlacionados del tratamiento si permanecen
dentro del mismo dominio de sonoridad de cuatro voces. Los 12 pares cumplen el
espacio de construccion declarado, no usan una reubicacion global de octava y
no contienen una violacion dura.

| Item | Freeze status | Caution reason |
|---|---|---|
| F01 | `FREEZE_ELIGIBLE_WITH_CAUTION` | SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE |
| F02 | `FREEZE_ELIGIBLE_WITH_CAUTION` | SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE; WEAK_MOTION_CONTRAST |
| F03 | `FREEZE_ELIGIBLE_WITH_CAUTION` | SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE; WEAK_MOTION_CONTRAST |
| F04 | `FREEZE_ELIGIBLE_WITH_CAUTION` | SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE |
| F05 | `FREEZE_ELIGIBLE_WITH_CAUTION` | SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE |
| F06 | `FREEZE_ELIGIBLE_WITH_CAUTION` | SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE; CENTROID_DIFFERENCE |
| F07 | `FREEZE_ELIGIBLE_WITH_CAUTION` | SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE |
| F08 | `FREEZE_ELIGIBLE_WITH_CAUTION` | SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE; CENTROID_DIFFERENCE |
| F09 | `FREEZE_ELIGIBLE_WITH_CAUTION` | SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE; WEAK_MOTION_CONTRAST |
| F10 | `FREEZE_ELIGIBLE_WITH_CAUTION` | SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE |
| F11 | `FREEZE_ELIGIBLE_WITH_CAUTION` | SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE |
| F12 | `FREEZE_ELIGIBLE_WITH_CAUTION` | SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE |

Counts: `FREEZE_ELIGIBLE = 0`, `FREEZE_ELIGIBLE_WITH_CAUTION = 12`,
`FREEZE_INELIGIBLE = 0`.

### Hard-control revalidation

All 12 reconstructed pairs pass: identical R1, same H2 identity and
multiplicity, same root/inversion and bass pitch class, four voices, fixed
correspondence, equal moving-voice count, equal Strategy B common-tone
pattern, no crossing and valid construction ranges. The offline correction of
F06 is part of this revalidation; it does not change the selection algorithm.

### Pool-level interpretation

Spacing remains a **STRONG SYSTEMATIC TREATMENT-CORRELATED ATTRIBUTE**, not a
hard validity failure. LOW_SELECTED tends to use a more even spacing profile;
HIGH_SELECTED tends to redistribute the same endpoint pitch classes into a
more uneven profile. This is documented as part of the treatment bundle and
must not be interpreted as evidence for a pure motion effect.

The reconstructed pool has 12 distinct underlying harmonic relations. No
transposition or trivial duplicate was used to inflate that count. The pool is
`PLAUSIBLY SUFFICIENT` for a bounded policy experiment, subject to later
precision/pilot work; this does not establish perceptual adequacy.

### Final audit decision

- Gate B: `PASS` for reproducible LOW_SELECTED/HIGH_SELECTED construction.
- Gate C: `PASS WITH SCOPE` for policy identification; `FAIL` for pure-motion
  identification.
- Gate A: `PASS`.
- Gate D: `PASS WITH SCOPE`.
- Gate E: `NOT YET PASS`.
- Gate F: `PASS WITH SCOPE`.
- `READY FOR ITEM FREEZE: YES`.
- `ITEM FREEZE AUTHORIZED: NO`.
- `MIDI AUTHORIZED: NO`.
- `AUDIO AUTHORIZED: NO`.
- `PILOT AUTHORIZED: NO`.
- `EXECUTION AUTHORIZED: NO`.

**Recommended freeze decision: B - AUTHORIZE ITEM FREEZE WITH CAUTIONS.**

Esta es una recomendacion de auditoria; no ejecuta el freeze.

## Freeze execution record

El pool simbolico fue congelado despues de la validacion estructural final. El
manifiesto authoritative es `experiments/EXP-003/EXP-003-item-freeze-manifest.yaml` y
su SHA-256 esta en `experiments/EXP-003/EXP-003-item-freeze-manifest.sha256`.

- `freeze_status: ITEM_POOL_FROZEN_WITH_CAUTIONS`.
- `freeze_version: EXP003-ITEM-FREEZE-v1`.
- `families_frozen: 12`.
- `hard_validation: PASS`.
- `items_changed_during_freeze: NO`.
- `music_engine_runtime: NOT_AUTHORIZED`.
- `midi: NOT_AUTHORIZED`.
- `audio: NOT_AUTHORIZED`.
- `pilot: NOT_AUTHORIZED`.
- `execution: NOT_AUTHORIZED`.

Tras este punto, cualquier cambio en pitches, etiquetas de tratamiento,
algoritmo de seleccion o reglas hard requiere `UNFREEZE_REVISION` y una nueva
auditoria metodologica. Las cautelas no son exclusiones: spacing permanece
como atributo correlacionado del tratamiento; F02, F03 y F09 conservan
contraste debil; F06 y F08 conservan cautela de centroide.
