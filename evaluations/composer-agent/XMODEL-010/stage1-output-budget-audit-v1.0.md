# XMODEL-010 - Auditoria offline del presupuesto Stage 1

La captura Qwen Stage 1 de XMODEL-009 (attempt 1) midio `num_predict=4096`, `eval_count=2864`, `prompt_eval_count=16661` y `done_reason=stop`. El payload de XMODEL-009 tenia 65 040 bytes UTF-8 y 64 407 caracteres. XMODEL-010 preparado tiene 65 010 bytes UTF-8; no se tokenizo con un modelo local, pues el preflight es offline. Los tokens por campo no son medibles localmente. La captura previa sirve como evidencia de dimensionamiento, no como medicion exacta de este payload ni garantia estadistica.

La salida sintetica valida mas compacta construida para diagnostico ocupa 743 bytes UTF-8 y contiene solo los campos estructurales minimos exigidos por el gate, sin contenido musical. No es ejemplo compositivo. La salida completa representativa de Qwen XMODEL-009 ocupa 7 697 bytes UTF-8 y uso 2 864 tokens de salida. Bajo `num_predict=4096`, el headroom observado es 1 232 tokens, 30,1%; se utilizo 69,9% del presupuesto. Recomendacion para Qwen XMODEL-010: conservar 4 096 tokens en Stage 1. Stage 2/3 conservan 8 192.

| Contribucion Stage 1 | Bytes UTF-8 |
|---|---:|
| Brief | 1 267 |
| Instruccion Stage 1 | 1 194 |
| Esquema Stage 1 embebido | 4 812 |
| Otros registros requeridos, incluido host | 54 986 |
| Wrappers y separadores | 2 751 |
| **Entrada total preparada** | **65 010** |

## Redundancia y versionado

Hay solapamiento intencional entre system contract, `decision-schema`, `guardrails`, `completion-checklist`, registro N3-P y prompt Stage 1. El esquema Stage 1 se incluye en el texto para que sea visible y tambien se envia por el canal estructurado para restringir serializacion. El brief se repite en cada request para dar contexto autonomo por etapa. No se retiro ninguno: no se demostro reduccion semanticamente equivalente que preserve requisitos y procedencia. No se cambio ningun campo Stage 1 ni la semantica Composer Interface v1.1. El prompt versionado XMODEL-010 conserva el mismo hash que el prompt congelado XMODEL-009 (`73d796fa...fee0af`).

La lista y el tamano individual de los registros estan en `stage1-record-size-audit-v1.0.md`. Sin llamadas a Ollama/tokenizador durante esta preparacion.
