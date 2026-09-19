# XMODEL-008 — Diagnóstico retrospectivo de representación

Estas copias están derivadas de los outputs Qwen preservados. No son outputs
originales del modelo y no sustituyen los artefactos históricos.

## Corrección aplicada

Solo se aplicó una transformación inequívoca:

```text
{"numerator": 4, "denominator": 4}  ->  "4/4"
```

La transformación conserva exactamente el compás y está exigida por el parser
de music-engine 4.0.0. No se eliminó ni reinterpretó ningún evento `effect`.
