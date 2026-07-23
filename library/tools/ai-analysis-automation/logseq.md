---
id: logseq
name: Logseq
description: Use when you need to organise an investigation's notes, entities, and links into a connected knowledge graph — a local-first tool for building and analysing case relationships (not a data source).
url: https://logseq.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Local-first note-taking and knowledge-graph building to track entities, links, and findings across an investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Open source and free; the desktop/mobile apps are free. An optional paid sync service exists but is not required.
opsec: passive
opsecNote: Local-first by design — your notes live in plain-text/Markdown files on your own disk, not a vendor cloud (unless you opt into sync). Keep your case notes encrypted at rest; nothing about the subject is transmitted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Popular open-source knowledge-management app (recommended in the Bellingcat toolkit); code is public and data stays local.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- logseq.com
tags:
- bellingcat-toolkit
- data-organization-analysis
- note-taking
source: bellingcat-toolkit
lastVerified: '2026-07-23'
---

# Logseq

> A privacy-first, open-source knowledge base: outliner notes that link into a graph — used in OSINT to organise entities, evidence, and relationships as a case grows.

## When to use
This is investigator tooling, not a data source. Reach for it when a case has enough moving parts — people, aliases, addresses, accounts, dates — that you need a structured, linkable place to hold them. Logseq's `[[page links]]` and block references let you build a connected map of who relates to whom and where each fact came from, and its local-first storage keeps sensitive notes off a vendor's servers.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install the free Logseq desktop (or mobile) app and point it at a local graph folder.
2. Create a page per entity (person, org, address, account) and link them with `[[Entity Name]]` as you write daily journal notes.
3. Attach the source/URL to every fact; use tags/queries to pull all mentions of an entity or all unverified claims.
4. Use the graph view to see clusters and gaps; export Markdown for reporting.
5. Pivot: Logseq doesn't find data — it holds and connects what your other tools produce, surfacing links and gaps that suggest the next lookup.

## Inputs → Outputs
- **In:** your own findings (no subject selector — you enter what you gather)
- **Out:** a linked, queryable case graph and exportable notes
- **Empty/negative result looks like:** not applicable — value is the structure you build; an empty graph just means nothing entered yet.

## Gotchas & OpSec
- It's an organiser, not a collector: it adds no new external data, so garbage in = garbage out; discipline in citing sources is what makes it useful.
- If you enable the paid sync, your notes leave your device — keep case data local or encrypted if that matters.
- OpSec: **passive** — local-first, nothing sent to the subject or a third party by default.

## Overlaps ("do both")
- Pairs with link-analysis/graphing tools (Maltego-style) and every data-source tool in this library — the sources feed facts; Logseq (or a heavier graph tool) structures and connects them.

## Trust & verifiability
`trust: trusted` — open-source, local-first, and recommended by reputable OSINT trainers; it stores your analysis, so verifiability depends on you citing each fact's source inside it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | logseq |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
