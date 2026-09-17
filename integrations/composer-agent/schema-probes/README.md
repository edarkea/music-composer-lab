# Technical schema probes (no composition)

These fixtures isolate JSON Schema shapes using neutral fields only. They are not XMODEL runs and do not invoke Qwen or Ministral. Local validator results can establish the intended contract; Ollama enforcement remains **INCONCLUSIVE** here until a separate trivial infrastructure probe is authorized.

Probes cover plain `required`, nested `required`, `if/then.required`, `oneOf`, and `additionalProperties: false`.
