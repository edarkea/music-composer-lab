# Resultado de sondeos técnicos de JSON Schema

Estos sondeos están aislados de la composición y no constituyen una ejecución XMODEL.

| Construcción | Resultado |
|---|---|
| `required` plano | INCONCLUSO para Ollama; el validador local cubre la restricción |
| `required` anidado | INCONCLUSO para Ollama; el validador local cubre la restricción |
| `if/then.required` | INCONCLUSO para Ollama; XMODEL-006 mostró que no debe asumirse su aplicación |
| `oneOf` (estrategia candidata) | INCONCLUSO para Ollama; el esquema candidato y el gate local lo expresan explícitamente |
| `additionalProperties: false` | INCONCLUSO para Ollama; el gate local rechaza rutas N3-P no canónicas |

No se invocó Qwen ni Ministral como agente compositor. No se toma una conclusión general sobre Ollama a partir de XMODEL-006: únicamente queda establecido que la construcción condicional usada allí no proporcionó una garantía observable para esas salidas.

