# XMODEL-009 — Capacidades host visibles

Estas son capacidades técnicas de materialización, no decisiones compositivas.

## `drums`

SongPlanV2 representa un track `drums` con eventos `drum_voice`. El track no
requiere `kit_id` ni `map_id`; durante validación host se usa el mapa aprobado:

```text
DrumExternalMap ID: song001_r1_steven_slate_map
```

Voces disponibles:

```text
kick, snare, rimshot, closed_hat, open_hat, pedal_hat,
low_tom, mid_tom, high_tom, crash, ride, ride_bell, cowbell
```

La asignación aprobada está en `song001_r1_steven_slate_map.yaml` y no se
modifica.

## `percussion`

Un track `percussion` requiere `kit_id`, `map_id` y eventos con
`instrument` + `sounding_articulation`. XMODEL-009 no suministra IDs aprobados
ni un `PercussionMap` aprobado para este propósito. Si el compositor elige
`percussion`, la dependencia host queda explícita y el gate bloquea; no se
convierte automáticamente a `drums`.

La arquitectura N3-P y todos los eventos musicales siguen siendo decisiones del
compositor.
