# EXP-003 — verificación de integración Pavlovia

## Outcome

**B — PAVLOVIA INTEGRATION REQUIRES TECHNICAL REVISION**

La verificación quedó limitada a inspección local porque no hay proyecto Pavlovia/GitLab, credenciales, endpoint ni revisión remota configurados en el entorno. No se presenta evidencia local como evidencia de persistencia server-side.

## Final report

| Campo | Resultado |
|---|---|
| Pavlovia project configured | NO |
| Project private | NO APLICABLE |
| Deployment revision/commit | Working tree local; sin commit de despliegue |
| jsPsych version | 8.2.1 |
| Pavlovia integration plugin/version | No integrado ni probado |
| PILOTING test | NOT NEEDED — no existe proyecto remoto |
| Controlled RUNNING technical test | FAIL — no ejecutable sin proyecto/credenciales |
| Real participants | NO |
| Technical-test sessions only | YES — únicamente dry-run local |
| Normal completion server save | FAIL — no verificable |
| Actual server export retrieved | NO |
| Export format | No disponible |
| Required schema preserved | FAIL — no verificable en export server-side |
| 12 experimental records recoverable | FAIL — sólo demostrado en export local |
| Practice separation | FAIL — sólo demostrado en export local |
| Post-task diagnostic separation | FAIL — sólo demostrado en export local |
| Refresh behavior observed | No observado en Pavlovia |
| Refresh policy | Pendiente; propuesta provisional: refresh invalida la sesión y requiere restart documentado |
| Incomplete/abandon behavior observed | No observado en Pavlovia |
| Incomplete-session policy | Pendiente; no mezclar ni recuperar silenciosamente sesiones parciales |
| Save-incomplete setting | No inspeccionado; proyecto inexistente |
| Periodic save applicable | NO DETERMINABLE |
| Duplicate behavior observed | No observado en Pavlovia |
| Duplicate policy | Pendiente; definir antes de Stage 1 y marcar duplicados explícitamente |
| Restart policy | Pendiente; restart explícito, sin fusionar sesiones |
| Save acknowledgement | FAIL — no verificable sin ruta server-side |
| 24 experimental WAV SHA checks | 24 / 24 PASS expected |
| Blinding | PASS WITH SCOPE — UI local muestra IDs opacos, pero el mapa privado se carga en el cliente y requiere protección de publicación |
| Any canonical asset modification | NO |
| Any methodology change | NO |
| Any new audio | NO durante esta verificación |
| Any new code | NO durante esta verificación |
| Technical-test data isolated | YES — no hubo datos remotos ni participantes |
| deployment-freeze-v2 created | NO |
| deployment-freeze-v2 hash | N/A |
| Pavlovia returned to INACTIVE | NO APLICABLE |
| READY FOR STAGE-1 PILOT | NO |
| PILOT AUTHORIZED | NO |

## Preserved local evidence

El dry-run local previo conserva los seis cells PASS. Este resultado no los reabre ni modifica. El manifest canónico permanece en:

`9B23143B7EEE384E5454056F0617E22DD2242C85848CD62920C109ABB6DDA1F0`

## Required next action

Configurar un único proyecto Pavlovia privado de prueba con credenciales del Project Owner. Después deben ejecutarse T1–T4 como sesiones `TECHNICAL_TEST`, recuperar el archivo real y congelar las políticas observadas antes de crear `deployment-freeze-v2`.
