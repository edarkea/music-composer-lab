# Research Directory Structure

```
research/
├── ROADMAP.md                 # This roadmap — composition domains, workflow, evidence classes, candidate format
├── domain/                    # Domain-specific research notes (one file per domain/topic)
│   ├── melody/
│   ├── harmony/
│   ├── rhythm/
│   ├── form/
│   ├── development/
│   ├── tension/
│   ├── hooks/
│   ├── texture/
│   ├── cross_domain/
│   └── song_level/
├── sources/                   # Source records (bibliography, corpus notes, interview notes)
│   ├── academic/
│   ├── pedagogical/
│   ├── repertoire/
│   └── empirical/
├── candidates/                # Candidate claims in lightweight YAML format
│   ├── melody/
│   ├── harmony/
│   ├── rhythm/
│   └── ...
└── questions/                 # Research questions, tracked by ID
    ├── RQ-MEL-001.md
    ├── RQ-MEL-002.md
    └── ...
```

## Usage

- **ROADMAP.md** — Master plan. Update when priorities shift or new domains added.
- **domain/** — Working notes per domain. Not polished manual entries.
- **sources/** — Raw source records. Link from candidate claims.
- **candidates/** — Individual candidate claims (YAML). One file per claim or small cluster.
- **questions/** — Research question tracking. One file per question with status, findings, open issues.

## Naming Conventions

- Candidate IDs: `CAND-{DOMAIN}-{NNN}` (e.g., `CAND-MEL-001`)
- Research Question IDs: `RQ-{DOMAIN}-{NNN}` (e.g., `RQ-MEL-001`)
- Source IDs: `SRC-{TYPE}-{NNN}` (e.g., `SRC-ACADEMIC-001`)

## Workflow Reminder

Research → Candidate Claims → Review → Manual/Rules (only after approval)