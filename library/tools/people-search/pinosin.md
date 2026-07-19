---
id: pinosin
name: pinosin
description: Use when you want a self-hosted framework to organise a person investigation and track its progress — a Go case-management tool; you feed it `name`/`username`/`email`/`phone` and record findings (`social-profile`, `associate`).
url: https://github.com/vvspower/pinosin
category: people-search
path:
- people-search
bestFor: Structuring and tracking the investigation of a specific individual (case notes/progress), rather than automatically pulling new data about them.
selectorsIn:
- name
- username
- email
- phone
selectorsOut:
- social-profile
- associate
status: degraded
pricing: free
costNote: Free, open-source (Apache-2.0), self-hosted; you build and run it yourself.
opsec: passive
opsecNote: Passive by nature — it is a local case-tracking framework, so nothing leaves your machine unless a module actively queries an external source. Any lookups you record are only as safe as the tools/queries you ran to get them; the framework itself sends nothing to the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small, early-stage GitHub project (vvspower, ~18 stars) the author describes as on standby; usable but unaudited and not actively maintained — treat as experimental.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases: []
tags:
- person-investigation
- case-tracking
- osint-framework
source: gh-topic-osint-framework
lastVerified: '2026-07-19'
enrichment: full
---

# pinosin

> A self-hosted Go framework for running and *tracking* an investigation into one individual — a case organiser, not an automated data-puller.

## When to use
You want structure around a person-centric investigation: a place to enter known selectors (`name`, `username`, `email`, `phone`), record what you find, and track progress across a case — conceptually aligned with missing-persons workflows. Reach for it as an organisational layer, not as a tool that will fetch new intelligence on its own.

## How to use it (`bestInteractionPattern`: cli)
1. Ensure Go is installed. Clone: `git clone https://github.com/vvspower/pinosin`.
2. Build/run per the repo (`go build` / `go run`); consult the README, as setup docs are thin and the project is early-stage.
3. Create a case for your subject, entering the known selectors.
4. Record findings and track progress as you work other tools; use it to keep a coherent picture of the investigation.

## Inputs → Outputs
- **In:** known selectors for one person (`name`, `username`, `email`, `phone`)
- **Out:** an organised case record — logged `social-profile`s, `associate`s, and progress notes you enter
- **Empty/negative result looks like:** the framework holds only what you put in — a sparse case reflects sparse inputs, not a tool failure; it does not auto-discover data.

## Gotchas & OpSec
- **Early-stage / on standby:** the author has paused development; expect rough edges, missing docs, and possible build issues. Verify it runs before relying on it for real casework.
- It is organisational — pair it with actual OSINT lookup tools that generate the findings you record.
- Human-in-the-loop: none intrinsically. OpSec: passive (local); your recorded lookups carry whatever footprint the underlying tools did.

## Overlaps ("do both")
- Complements the rest of this library — use dedicated people/username/email tools to *gather*, and pinosin (or any case tracker) to *organise* what they return.

## Trust & verifiability
`trust: community` — a small unaudited personal project; review the code before running, and never treat the framework itself as a source — evidentiary weight comes from the tools you fed it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pinosin |
| category | people-search |
| selectorsIn → selectorsOut | name, username, email, phone → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
