# EXP-003 — Auditoría de representabilidad temporal MIDI

## What I changed

Se añadió este informe técnico de auditoría. No se modificaron el manifiesto
canónico de ítems, el render spec congelado, el renderer, el `music-engine`, el
SongPlan fallido ni los artefactos de canary. No se generaron MIDI/WAV y no se
repitió el canary.

## Key findings

### PPQ efectivo y comportamiento del motor

- El `Song` del `music-engine` 4.0.0 tiene `ppq=960` como valor por defecto.
- El writer MIDI acepta un PPQ entero positivo y limita el valor a `32767`.
- El SongPlan 2.0 no contiene un campo PPQ.
- El subcomando `songplan render` no expone una opción `--ppq`.
- La API de dominio permite configurar PPQ al construir un `Song`, pero la
  materialización normal de SongPlan crea el `Song` con el valor por defecto.
- La conversión es exacta, no aproximada: si posición o duración producen una
  fracción de tick, el writer lanza `cannot be represented exactly at the
  selected PPQ`.

### Matemática de la duración

A 120 BPM, un beat de negra dura 0,5 s y una redonda dura 2 s. Por tanto:

`0,48 s = 0,96 beats = 24/25 beats = 6/25 whole notes`.

Los ticks de duración son `PPQ × 24/25`. Con PPQ 960 se obtienen `921,6`
ticks; por eso la materialización falla antes de escribir MIDI.

Para los landmarks canónicos, expresados como tiempos absolutos, los ticks son:

| tiempo | beats desde cero a 120 BPM | ticks a PPQ 1000 |
|---:|---:|---:|
| 0,25 s | 1/2 | 500 |
| 0,73 s | 73/50 | 1460 |
| 0,75 s | 3/2 | 1500 |
| 1,23 s | 123/50 | 2460 |

El PPQ mínimo que representa exactamente todos los landmarks y la duración
es **50**. La condición de la duración exige múltiplo de 25; los offsets y
finales de las notas exigen múltiplo de 50. Cualquier múltiplo entero de 50
hasta 32767 es representable. PPQ 1000 es una opción práctica compatible con
el límite del writer y conserva los ticks indicados arriba.

### Error de offset absoluto del SongPlan fallido

En el modelo del motor, `beat: "1"` en el compás 1 significa tiempo cero y
`beat: "2"` significa 0,5 s a 120 BPM. El SongPlan fallido, por tanto, produce
onsets 0,00 s y 0,50 s.

El evento congelado exige onsets 0,25 s y 0,75 s. La discrepancia es de 250 ms
para ambos grupos. Es un **ABSOLUTE ONSET FIDELITY FAIL**, independiente del
fallo de PPQ.

Para representar los offsets en SongPlan manteniendo 120 BPM, el adaptador
debe mapearlos a posiciones relativas al compás `beat: "3/2"` y
`beat: "5/2"`, no a `"1"` y `"2"`. El codec acepta beats fraccionarios como
`Fraction` exactos.

### Veredicto de opciones

#### Opción A — Mantener tempo 120 y cambiar PPQ

**Recomendada.** Es exacta, mantiene el tempo y la interpretación científica
del freeze, y no requiere cambiar el renderer ni el `music-engine`. Requiere un
adaptador o ruta de exportación que construya el `Song` con PPQ 1000 (o, como
mínimo matemático, 50). También requiere corregir el mapeo de onsets a `3/2` y
`5/2`. Es una remediación de integración, no un cambio del timing canónico.

#### Opción B — Mantener PPQ 960 y cambiar tempo a 125 BPM

Matemáticamente puede hacer exacta la duración, porque 0,48 s es una negra a
125 BPM. Sin embargo, obliga a codificar los onsets absolutos mediante beats
fraccionarios distintos (`73/48` y `41/16` en compás 1) y cambia el metadata de
tempo del render. Es más frágil como representación y requiere una enmienda
técnica explícita del render spec; no es la solución primaria.

#### Opción C — Aproximar a PPQ 960

No recomendada. Si se redondearan endpoints al tick más cercano, el error
máximo de los landmarks no exactos sería `0,4/1920 s`, aproximadamente
**0,2083 ms**. Pero el writer actual no redondea: rechaza la fracción. Definir
una política de redondeo cambiaría la semántica de verificación y no está
autorizado en este canary.

#### Opción D — Bypass MIDI

Puede permitir una comprobación del renderer WAV, pero deja sin resolver E2
(representabilidad MIDI) y no satisface el objetivo de validar el pipeline
congelado. No se recomienda como remediación.

## Counterexamples / Risks

- Cambiar solamente PPQ no corrige el offset absoluto de 250 ms.
- PPQ 50 es exacto para este conjunto de landmarks, pero ofrece una resolución
  temporal más baja que PPQ 1000; por eso se recomienda 1000 sin convertirlo en
  requisito universal.
- Cambiar a 125 BPM puede conservar tiempos físicos, pero el metadata MIDI y la
  representación del SongPlan ya no coincidirían con una especificación que
  exija tempo 120.
- El análisis de aproximación supone redondeo al tick más cercano; esa política
  no existe actualmente en el motor.

## Uncertainties

- Debe confirmarse en una futura prueba controlada que la ruta adaptadora elegida
  conserva PPQ 1000 hasta `write_midi` y serializa los beats fraccionarios sin
  transformación adicional.
- Esta auditoría no autoriza ni ejecuta esa prueba, porque el encargo prohíbe
  reintentar el canary y generar nuevos medios.

## Questions for the Music/Methodology Director

Ninguna decisión metodológica es imprescindible para corregir el fallo
técnico: la recomendación conserva el timing canónico. La aprobación necesaria
es operativa: autorizar una futura remediación del adaptador de exportación.

## Recommended next step

Implementar y revisar un adaptador de exportación MIDI que use PPQ 1000 y mapee
los onsets canónicos a `beat: "3/2"` y `beat: "5/2"`, sin alterar el freeze ni
el renderer; después solicitar una nueva autorización independiente para el
canary.

## Clasificación de cambios

- T1 — Adaptador / mapeo SongPlan: **necesario**.
- T2 — Metadata MIDI / PPQ: **necesario en la ruta adaptadora**; no en el
  artefacto canónico.
- T3 — Cambio del `music-engine`: **no necesario**.
- T4 — Timing científico canónico: **prohibido / sin cambios**.

Impacto previsto: item freeze **NO**; acoustic spec **NO**; renderer **NO**;
`music-engine` **NO**; sección técnica de verificación MIDI del render spec:
**debe enmendarse únicamente para documentar que la ruta de exportación fija
PPQ 1000 y el mapeo de offsets**, sin modificar los landmarks científicos.
