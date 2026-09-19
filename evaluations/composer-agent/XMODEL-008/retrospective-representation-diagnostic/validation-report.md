# XMODEL-008 — Auditoría de fallos SongPlanV2

## Resultado

**B — SOME ERRORS REQUIRE MUSICAL OR SEMANTIC DECISIONS**

La forma de `time_signature` admite una corrección determinista y sin pérdida.
`effect.position` no tiene representación equivalente en el contrato SongPlanV2
4.0.0; eliminarlo sería una reparación semánticamente no justificada. Además,
la corrección aislada del compás en Attempt 2 expuso un error de escala que no
se alcanzaba durante el parseo inicial.

## Contrato autoritativo

Fuentes:

- `.venv/Lib/site-packages/music_engine/songplan/schemas/songplan-v2.schema.json`
- `.venv/Lib/site-packages/music_engine/songplan/v2/codec.py`
- `.venv/Lib/site-packages/music_engine/domain/time_signature.py`

`$.time_signature` es obligatorio y debe ser una cadena no vacía. El parser usa
`TimeSignature.parse`, que exige `numerator/denominator`, numerador entero mayor
que cero y denominador potencia de dos positiva.

Los eventos `effect` están en:

`$.tracks[i].motifs[j].events[k]`

Requieren `bar` (entero >= 1), `beat` (cadena no vacía) y `duration` (cadena no
vacía). Solo admiten opcionalmente `id`. El tiempo se representa mediante
`bar` + `beat` + `duration`; `position` no es un campo permitido.

## Outputs históricos

### Attempt 1

- `time_signature`: `"4/4"`, correcto.
- `tracks[4]` es `effect`.
- Eventos en `tracks[4].motifs[0..2].events[0]`:
  - `{bar: 1, beat: "1", duration: "4", position: "1.0", duration: "4.0"}`
  - `{bar: 5, beat: "1", duration: "8", position: "5.0", duration: "8.0"}`
  - `{bar: 13, beat: "1", duration: "4", position: "13.0", duration: "4.0"}`
- Error confirmado: `position` no permitido.
- También hay nombres JSON duplicados `duration`; el parser JSON conserva el
  último valor, pero la representación no es canónica.

### Attempt 2

- `time_signature`: `{numerator: 4, denominator: 4}`.
- No contiene track `effect`.
- Error inicial confirmado: el parser exige una cadena.
- En la copia derivada con `"4/4"`, el engine expuso:
  `tracks[0].motifs[0].events[2].pitches[0]` = `F4`, fuera de la escala
  `D ionian`, sin `chromatic: true`.

### Attempt 3

- `time_signature`: `{numerator: 4, denominator: 4}`.
- `tracks[4]` es `effect`.
- Sus eventos contienen:
  - `bar`: `1`, `5`, `13`;
  - `beat`: `"1"`;
  - primera `duration`: `"1/1"`;
  - `position`: `0` en los tres eventos;
  - segunda `duration`: `4`, `8`, `4`.
- Error confirmado: `position` no permitido.
- Las duraciones duplicadas tienen valores diferentes y, por tanto, son una
  ambigüedad adicional. El posible error de escala de `F4` no se alcanzó porque
  el parseo se detuvo antes.

## Correcciones evaluadas

| Error | Corrección lossless | Información perdida | Resultado |
|---|---:|---:|---|
| `time_signature` objeto 4/4 | Sí: `{4,4}` → `"4/4"` | No | Aplicada solo en copias diagnósticas.
| `effect.position` | No | Sí o significado desconocido | No se modificó.
| duraciones JSON duplicadas | No hay elección inequívoca en Attempt 3 | Sí, si se escoge una | No se modificó.
| `F4` fuera de D ionian | No es una corrección de serialización | Requiere decidir escala o cromatismo | No se modificó.

`position` no puede trasladarse automáticamente a `bar`, `beat` o `duration`:
los outputs ya contienen esos campos y el contrato no define qué representa
`position`. En Attempt 1 parece relacionado con el número de compás; en Attempt
3 es siempre cero. Esa diferencia impide una transformación determinista.

## Copias y validación real

Se crearon únicamente:

- `attempt-2-time-signature-only.json`
- `attempt-3-time-signature-only.json`

Ambas están marcadas como **RETROSPECTIVE REPRESENTATION DIAGNOSTIC**.

Resultados con music-engine 4.0.0:

- Attempt 2 derivado: `VALIDATION_FAILURE`; después de corregir el compás,
  aparece `pitch.outside_scale` para `F4`.
- Attempt 3 derivado: `PARSE_FAILURE`; continúa fallando por `position`.

No se generó MIDI. No se aplicaron los mapas ni se modificaron outputs
históricos; la configuración host de PercussionMap previamente validada sigue
siendo compatible con los pares históricos.

## Implicaciones futuras

Stage 3 debería:

1. usar el esquema real del engine, con `time_signature` como string;
2. declarar el evento `effect` con solo `bar`, `beat`, `duration` e `id`;
3. rechazar `position` determinísticamente antes de invocar el engine;
4. detectar nombres JSON duplicados o exigir serialización JSON canónica;
5. devolver diagnósticos con la ruta exacta y no proponer reparaciones musicales.

Esto mejora la transferencia estructural; no demuestra calidad musical.
