---
id: maldevel-osint
name: maldevel/osint
description: Use when you want a curated reference of OSINT techniques/scripts/tips — a small GitHub collection of investigation and reconnaissance notes (reference reading, not a live tool).
url: https://github.com/maldevel/osint
category: search-engines
path:
- search-engines
bestFor: A compact reference of OSINT tips, scripts, and reconnaissance techniques to read/borrow from.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free and open source (GPL-3.0) GitHub repository; clone or browse online.
opsec: passive
opsecNote: Passive — it's reference material you read; running any script it contains carries that script's own OpSec (some recon techniques are active). Review a script before executing it against a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small personal collection (~13 stars, only a handful of commits) that appears dormant; useful as reading, but verify any technique/script is still current before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- intelspy
aliases:
- maldevel osint
tags:
- notes
- tips
- collection
source: gh-topic-footprinting
lastVerified: '2026-07-23'
enrichment: full
---

# maldevel/osint

> A small, dormant GitHub collection of OSINT tips, scripts, and reconnaissance notes — reference reading to learn techniques from, not a tool that returns data.

## When to use
You want to read or borrow investigative techniques — information-gathering, enumeration, reconnaissance, network footprinting — organised as a compact reference. Reach for this repo as background/learning material or to lift a script idea, understanding it is a personal, largely inactive collection rather than a maintained toolkit. It takes no selector and returns no lookup result; its value is the knowledge and snippets inside.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/maldevel/osint and browse the topic folders and docs (info-gathering, enumeration, recon, footprinting).
2. Read the notes/tips relevant to your task.
3. If you reuse a script, review it first — check it still works and understand whether it's passive or active before running it.
4. Treat everything as potentially dated (the repo is dormant); cross-check techniques against current sources.
5. Pivot: use the ideas here to inform which live tools you actually run.

## Inputs → Outputs
- **In:** none — it's a reference collection, not a lookup
- **Out:** OSINT techniques, tips, and scripts to read and adapt
- **Empty/negative result looks like:** thin or outdated content on a given topic — with only a few commits, coverage is shallow; use it as a starting idea, not an authority.

## Gotchas & OpSec
- Dormant/personal: minimal maintenance and small scope — don't expect completeness or currency.
- Any bundled script may be active recon — review and understand it before pointing it at a target.
- OpSec: reading is passive; execution carries the script's own exposure.

## Overlaps ("do both")
- Overlaps larger, maintained OSINT tool lists and framework repos — prefer an actively-maintained awesome-list for breadth, and dip into this for its specific notes. Pair conceptual tips here with the live tools elsewhere in this library.

## Trust & verifiability
`trust: community` — a small, unmaintained personal collection; useful as reading, but verify any technique or script against current sources before relying on it, since nothing here is guaranteed up to date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maldevel-osint |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
