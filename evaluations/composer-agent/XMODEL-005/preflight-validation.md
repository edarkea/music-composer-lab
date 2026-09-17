# XMODEL-005 — Preflight y gates

Estado: `PREPARED_NOT_EXECUTED`.

La asamblea real de Stage 1 para ambos modelos fue ejecutada sin invocar ningún modelo. Cada payload contiene el brief exacto, el contrato de sistema, los registros v1.1 resueltos, el genre pack, N3-P, el esquema de etapa y la instrucción completa. El manifiesto de cada payload conserva la lista y SHA256 de cada registro y el SHA256 del texto que sería transmitido.

Resultado de preflight Stage 1:

- Qwen: PASS; 10 registros resueltos; brief exacto presente; instrucción presente; marcadores de ejemplos compositivos ausentes.
- Ministral: PASS; mismo conjunto y mismos hashes; payload byte-identical bajo la condición simétrica.

Stage 2 y Stage 3 requieren outputs aceptados de la etapa anterior y por eso no se ensamblan en preparación. El harness falla si esos outputs no existen y no los reemplaza por rutas o hashes.

## Gates ejecutables

`integrations/composer-agent/staged_harness.py` implementa `preflight`, `gate` y `can_advance`. Los gates devuelven JSON `pass: true|false`, etapa, errores explícitos y `semantic_repair_performed: false`. Stage 1 comprueba decisiones, N3-P, RANK y atribución; Stage 2 comprueba campos de material, hash congelado y cobertura declarada; Stage 3 comprueba raíz y campos anidados SongPlanV2, referencias, tracks y requisitos de percusión.

Los claims perceptuales, causalidad, suficiencia artística y evidencia semántica que no son representables mecánicamente siguen marcados como **HUMAN AUDIT**. No se presentan como PASS automático.

## Tests sin modelos

`python integrations/composer-agent/test_staged_harness.py -v` ejecuta 11 pruebas sintéticas A–K. Los fixtures no contienen ejemplos compositivos ni soluciones musicales.
