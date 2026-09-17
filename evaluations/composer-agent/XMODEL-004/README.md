# XMODEL-004 — Staged execution (prepared, not executed)

Esta evaluación prueba si los mismos modelos externos pueden aplicar `composer-interface-v1.1` cuando la planificación, la creación de material y la serialización SongPlan se separan mediante gates deterministas.

Estado: `PREPARED_NOT_EXECUTED`.

Modelos previstos:

- `qwen3:14b`
- `ministral:3-14b`

Condición: NO-EXAMPLE, mismo brief artístico de XMODEL-001..003, mismos parámetros de muestreo (`temperature: 0`, `seed: 41`, `top_p: 1`, `top_k: 40`, `repeat_penalty: 1`), `num_ctx: 32768`. El presupuesto de salida se adapta a cada etapa y queda registrado por intento.

La variable principal es `ONE-PASS EXECUTION → STAGED EXECUTION`. No ejecutar hasta autorización explícita.

## Criterio de éxito

Cada modelo debe pasar Stage 1, Stage 2 y Stage 3; producir SongPlanV2 válido; tener RANK no soportado igual a cero, atribución Owner falsa igual a cero, N3-P válido y cero reparación semántica del adaptador. No se evalúa qué modelo compone mejor.
