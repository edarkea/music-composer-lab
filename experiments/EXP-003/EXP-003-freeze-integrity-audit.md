# EXP-003 - Reauditoría forense de integridad del freeze

## Corrección aritmética de la auditoría

La transcripción anterior del LOW de F11 como `D,C,F,F` era incorrecta.
`81 mod 12 = 9 = A`, por lo que `[50,60,65,81]` implica `D,C,F,A`.

En este manifiesto, `doubling_pattern` debe interpretarse como multiconjunto
de chord members y multiplicidades esperadas, no como una tupla ordenada por
V1--V4. El orden estructural lo determinan las listas MIDI. Por tanto:

- LOW almacenado: identidad **PASS**, doubling/multiplicidad **PASS**.
- HIGH almacenado `[50,57,72,81]` → `D,A,C,A`: identidad **FAIL**,
  doubling/multiplicidad **FAIL**.
- HIGH recomputado `[50,53,72,81]` → `D,F,C,A`: identidad **PASS**,
  doubling/multiplicidad **PASS**.

Esta corrección sustituye cualquier afirmación posterior de este documento que
describa el LOW como `D,C,F,F` o lo clasifique como fallo.

## Alcance y autorización

Esta auditoría revisa exclusivamente la integridad simbólica del freeze de
EXP-003, con atención especial a `EXP003-F11`. Se inspeccionaron `EXP-003.md`,
`EXP-003-item-specification.md`,
`EXP-003-item-freeze-manifest.yaml` y `EXP-003-rendering-spec.md`.

No se modificó el manifiesto congelado. No se generaron SongPlans, MIDI ni
audio, y no se invocó `music-engine`.

## Integridad histórica

El hash SHA-256 del manifiesto antes de la auditoría es:

`AE1C5A93C57469CB72C95775A7ED11916A7599729F10EA0B94D4659CA6B8A093`

El hash permanece idéntico después de la auditoría. El archivo se trata como
versión histórica congelada con un defecto de integridad conocido, no como
versión válida para materialización.

## Contrato de representación

`H2_identity` funciona como etiqueta descriptiva de la selección armónica
(raíz, calidad y, cuando se declara, duplicación). No es una lista ordenada de
alturas MIDI. `doubling_pattern` es la representación ordenada por voces de la
multiconjunto de pitch classes esperado en R2; sus posiciones corresponden a
V1--V4.

El invariante determinista requerido para cada condición LOW y HIGH es:

1. el multiconjunto de `R2_*_pitches_midi[i] mod 12` debe ser exactamente el
   multiconjunto de `doubling_pattern`;
2. el conjunto resultante debe coincidir con el contenido de pitch classes
   declarado por `H2_identity`;
3. V1 debe tener `bass_pitch_class` y `inversion` debe seguir siendo `root`;
4. LOW y HIGH deben conservar la misma identidad armónica y el mismo patrón de
   multiplicidad dentro de la familia.

La etiqueta de acorde y la multiplicidad no deben inferirse una de otra sin
comprobar este contrato explícito.

### Regla ejecutable requerida

Para cada familia y para `LOW` y `HIGH`, un validador debe ejecutar, como
mínimo, la siguiente lógica y producir un resultado por campo:

```text
actual_pcs = [pitch % 12 for pitch in R2_condition_pitches_midi]
assert set(actual_pcs) == declared_H2_pitch_class_set
assert Counter(actual_pcs) == Counter(doubling_pattern)
assert R2_condition_pitches_midi[0] % 12 == bass_pitch_class
assert ordered_pitches_are_non_crossing_and_in_declared_ranges
assert spacing_and_span_are_in_declared_bounds
assert LOW.H2 == HIGH.H2
assert Counter(LOW.actual_pcs) == Counter(HIGH.actual_pcs)
assert LOW.moving_voice_count == HIGH.moving_voice_count
```

El validador debe detener la elegibilidad ante cualquier fallo y conservar los
valores calculados, no únicamente un `PASS` agregado.

## Reconstrucción determinista de F11

Se reenumeró el espacio declarado: rangos por voz, cuatro voces ordenadas,
pitch-class multiplicity, bajo raíz, spacing adyacente, span, ausencia de
crossing y retención común estructural. Después se formaron pares con igual
retención, igual `moving_voice_count` y movimiento total distinto, y se aplicó
el orden lexicográfico `span`, `centroid`, spacing máximo, spacing mínimo,
`spacing_profile_L1` y movimiento máximo; el desempate posterior fue por mayor
contraste y listas MIDI lexicográficas.

Resultado reproducido:

| condición | pitches recomputados | motion vector | total motion | spacing | centroid |
|---|---|---|---:|---|---:|
| LOW | `[50, 60, 65, 81]` | `[-5, 1, 3, 16]` | 25 | `[10, 5, 16]` | 64 |
| HIGH | `[50, 53, 72, 81]` | `[-5, -6, 10, 16]` | 37 | `[3, 19, 9]` | 64 |

El par seleccionado por el procedimiento es, por tanto, `SAME SELECTED LOW /
DIFFERENT SELECTED HIGH`. El contraste recomputado es 12 semitonos.

El LOW almacenado coincide con la recomputación. El HIGH almacenado
`[50,57,72,81]` no coincide y además implica pitch classes `D,A,C,A`, no
`D,F,A,C`.

## Resultado del invariante en las 12 familias

| familia | LOW | HIGH | resultado |
|---|---|---|---|
| F01 | PASS | PASS | PASS |
| F02 | PASS | PASS | PASS |
| F03 | PASS | PASS | PASS |
| F04 | PASS | PASS | PASS |
| F05 | PASS | PASS | PASS |
| F06 | PASS | PASS | PASS |
| F07 | PASS | PASS | PASS |
| F08 | PASS | PASS | PASS |
| F09 | PASS | PASS | PASS |
| F10 | PASS | PASS | PASS |
| F11 | PASS | FAIL | FAIL (stored HIGH only) |
| F12 | PASS | PASS | PASS |

En F11, LOW `[50,60,65,81]` implica `D,C,F,A` y pasa identidad y
multiplicidad como multiconjunto. HIGH `[50,57,72,81]` implica `D,A,C,A` y
falla ambas comprobaciones. El HIGH recomputado `[50,53,72,81]` implica
`D,F,C,A` y pasa ambas comprobaciones.

## Clasificación de causa raíz

**F — MULTIPLE_ERRORS.** Hay dos componentes distinguibles:

- **PITCH_DATA_ERROR:** el HIGH almacenado no es el resultado de la selección
  determinista y no respeta el multiconjunto declarado.
- **VALIDATOR_ERROR / coverage gap:** la validación previa informó `PASS`, pero
  no ejecutó o no registró una comprobación general que comparase los pitch
  classes exactos de cada endpoint con `doubling_pattern` y `H2_identity`.

No se encontró código offline de enumeración o validación en el repositorio. El
`validation.result: PASS` del manifiesto y la descripción de “offline
validation” son metadatos/documentación, no evidencia de una implementación
reproducible de ese invariante.

## Tratamiento y severidad

La corrección propuesta conservaría R1, H2, raíz/inversión, cuatro voces,
`moving_voice_count = 4`, retención común vacía, crossing, rangos y reglas de
construcción. LOW seguiría siendo LOW y HIGH seguiría siendo HIGH. Sin
embargo, el endpoint HIGH y el par seleccionado cambian al rerunear el
procedimiento.

Por ello no es una reparación metadata-only:

- cambio de asignación LOW/HIGH: **NO**;
- cambio del algoritmo: **NO**;
- cambio del par seleccionado: **SÍ**;
- severidad: **LEVEL 3 — SELECTION REVISION**.

Puede repararse sin cambiar la definición científica del tratamiento, pero no
sin una revisión formal del freeze y una nueva versión del manifiesto.

## Consecuencia y plan histórico

`E1 = BLOCKED` y `Gate E = BLOCKED UPSTREAM` hasta que exista un manifiesto
autoritativo revisado y pase el invariante para las 12 familias.

El SHA histórico debe conservarse como:

```text
freeze_v1
SHA-256: AE1C5A93C57469CB72C95775A7ED11916A7599729F10EA0B94D4659CA6B8A093
status: INVALIDATED_BY_INTEGRITY_AUDIT
```

Una revisión posterior deberá crear `freeze_v2` y un SHA nuevo, sin sobrescribir
la historia. En esa revisión deberá incorporarse el chequeo general de
identidad/multiplicidad para ambas condiciones de cada familia.

## Estado de autorización

## Reauditoría de freeze-v2

El validador ejecutable `tools/exp003/validate-exp003-freeze-v2.py` produce:

- freeze-v1: 11 PASS, F11 HIGH FAIL;
- freeze-v2: 12 PASS, 0 FAIL.

El procedimiento de selección permanece sin cambios y vuelve a seleccionar
F11 LOW `[50,60,65,81]` y HIGH `[50,53,72,81]`. Las etiquetas
`LOW_SELECTED` y `HIGH_SELECTED` y el estimando de política no cambian.

La revisión de pool muestra:

- motion contrast: rango `2..12` (antes `2..8`);
- span: diferencia cero en las 12 familias;
- centroide: F11 pasa a diferencia cero; solo F06 y F08 conservan diferencia
  de centroide;
- maximum motion: sin cambio estructural relevante; F11 conserva `16/16`;
- spacing: F11 pasa a spacing L1 `28`; la covariación sistemática de spacing
  sigue presente y continúa siendo un atributo del tratamiento, no un efecto
  puro de motion.

No aparece un régimen registral, de span, de voz o de spacing nuevo que sea
patológico dentro del espacio declarado. F11 queda `FREEZE_ELIGIBLE_WITH_CAUTION`
por `SPACING_SYSTEMATIC_TREATMENT_ATTRIBUTE`.

La transferencia a rendering queda bloqueada únicamente por la resolución
pendiente del renderer/asset; la obstrucción de integridad simbólica upstream
ha sido eliminada para v2.

## Estado de autorización

- `READY TO AUTHORIZE FREEZE REVISION: YES` — solo para preparar/revisar una
  propuesta; no para aplicarla automáticamente.
- `TECHNICAL CANARY: NOT AUTHORIZED`
- `MIDI: NOT AUTHORIZED`
- `AUDIO: NOT AUTHORIZED`
- `PILOT: NOT AUTHORIZED`

## Recommended next step

Freeze-v2 ha sido creado y validado. El siguiente trabajo autorizado es fijar
renderer, asset y settings para retomar Gate E; no se debe renderizar todavía.
