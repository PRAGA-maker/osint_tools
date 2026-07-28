---
id: obsidian
name: Obsidian
description: Use when you need a local, linked note vault to organise an investigation — entities, timelines, sources — and see relationships in a graph; a case-management/analysis workspace.
url: https://obsidian.md
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Structuring case notes, entities and sources as linked Markdown with a relationship graph, all stored locally.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free for personal use; a paid Commercial licence is required for business use, and Sync/Publish are paid add-ons. Core app is free.
opsec: passive
opsecNote: Vaults are plain local Markdown files — nothing leaves your machine unless you enable Sync/Publish or a plugin that phones home. Keep case vaults on encrypted storage, review community plugins before installing (they run with file access), and avoid cloud sync for sensitive cases.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: A popular, well-regarded local-first notes app; the core is closed-source but data stays in open Markdown files you control. Third-party plugins are community-made — vet them.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Obsidian.md
tags:
- case-management
- notes
- link-analysis
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Obsidian

> A local-first, linked Markdown notebook that doubles as an investigation workspace — capture entities, sources and events as notes, wikilink them, and watch the relationships form a graph.

## When to use
You're running an investigation and need somewhere to organise it: one note per person/entity/place/account, wikilinks between them, a timeline, and citations to sources. Obsidian keeps everything as local Markdown, links notes with `[[wikilinks]]`, and renders the connections as an interactive graph — a lightweight, free alternative to heavyweight link-analysis tools for structuring what you find and spotting relationships. It manages and connects your findings; it doesn't collect data itself.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Obsidian and create a dedicated, encrypted vault per case.
2. Make a note per entity (person, org, address, account); record facts with source links and dates.
3. Wikilink related notes (`[[Jane Doe]]` ↔ `[[Acme Corp]]`); use tags for selector types.
4. Use the graph view to see clusters and unexpected links; build a timeline note.
5. Pivot: the graph surfaces where entities connect — those junctions are the leads to dig into next with the actual OSINT tools.

## Inputs → Outputs
- **In:** n/a — you populate it with findings; it's a workspace, not a lookup.
- **Out:** an organised, linked, graph-visualised case record (no person-level `selectorsOut`).
- **Empty/negative result looks like:** n/a. Its value is structure and recall, not discovery.

## Gotchas & OpSec
- OpSec: local Markdown by default — great for sensitive work; but Sync/Publish and some plugins send data off-device. Keep sensitive vaults off cloud sync and encrypt storage.
- Community plugins run with file access — vet before installing on a case vault.
- It won't find anything; it organises what your other tools return.

## Overlaps ("do both")
- Complements every collection tool here — run your OSINT lookups, then record and link the results in Obsidian so the picture (and its gaps) stays visible across a long case.

## Trust & verifiability
`trust: community` — a widely-used local-first app storing data in open Markdown you control; the core is closed-source, so vet plugins and keep sensitive vaults local.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | obsidian |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
