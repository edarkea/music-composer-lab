# Stage 2/3 hardening candidate

Cambios exclusivamente t?cnicos: aclaraci?n de serializaci?n, validaci?n local, enforcement estructural y diagn?sticos de retry.

- Cambios sem?nticos: 0
- Decisiones musicales del adaptador: 0
- Stage 2 `format`: desactivado.
- Stage 3 `format`: schema derivado de la rama existente `songplan_candidate`.
- Autoridad final: contrato `datasets/composer-interface-v1.1/songplan-v2-contract.yaml` y gate local.
- Wrappers Markdown/prosa: siguen siendo FAIL; no se eliminan autom?ticamente.

## Derivaci?n Stage 3

Fuente: `datasets/composer-interface-v1.1/output-schema.json`
Fuente SHA256: `7d334387404bd312a300460d2986e7e19ad8d885e842701a219ee91d935e332b`
Schema derivado: `stage-3-songplan-format-schema-v1.1.json`
Schema derivado SHA256: `7e5de52624b5d14fd6d2638ec6d941c060505ece50c2bfe598bb867134dd615e`
M?todo: extracci?n mec?nica de `properties.songplan_candidate.oneOf[0]`, serializada sin a?adir campos.
