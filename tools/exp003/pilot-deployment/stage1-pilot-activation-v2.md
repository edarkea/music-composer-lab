# EXP-003 — Stage-1 allocation freeze v2

## Estado

**EXP-003 PAUSED — READY TO RESUME**

Este registro sucede a `stage1-pilot-activation-v1.md` y congela exclusivamente la asignación nominal de Stage 1. No habilita entradas piloto ni modifica la metodología.

## Allocation

| Participant | Cell |
|---|---|
| P001 | A-O1 |
| P002 | B-O1 |
| P003 | A-O2 |
| P004 | B-O2 |
| P005 | A-O3 |
| P006 | B-O3 |
| P007 | A-O1 |
| P008 | B-O1 |
| P009 | A-O2 |
| P010 | B-O2 |
| P011 | A-O3 |
| P012 | B-O3 |

Verificación: 12/12 IDs, dos participantes por cada celda operativa, sin duplicados y sin celdas ausentes. La asignación es declarativa y no depende de ratings, resultados ni respuestas.

## Entry status

Los 12 tokens de participante están presentes en `server/private-stage1-allocation.json` y permanecen `enabled: false`. No se habilitó ningún token piloto. El token técnico separado no forma parte de esta asignación participante.

## Estado de proyecto

- Institutional/ethical prerequisite: **UNRESOLVED**.
- Pilot entry: **DISABLED**.
- Real participants: **NONE**.
- Scientific evidence: **NONE**.
- Pilot authorized: **NO**.

