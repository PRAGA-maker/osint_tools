---
id: bubbl-us-online-flow-chart-tool
name: Bubbl.us Online Flow Chart Tool
description: Use when you have a set of `associate`/entity links and want to lay them out as a visual link-analysis mind map — an analysis aid that produces a shareable relationship diagram, not new selector data.
url: https://bubbl.us
category: documents-metadata
path:
- documents-metadata
bestFor: Quick browser-based mind-mapping of people/entity relationships for link analysis.
selectorsIn:
- associate
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier allows a small number of saved mind maps; paid plans unlock unlimited maps, image export, and collaboration.
opsec: passive
opsecNote: You type your own findings into a third-party web app, so case data leaves your machine and sits on Bubbl.us servers — keep real names/identifiers out of it (use pseudonyms/codes) for sensitive investigations, and prefer an offline tool for anything protected.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Generic third-party diagramming SaaS; it stores whatever you enter and makes no investigative claims of its own.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Bubbl.us
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- link-analysis
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Bubbl.us Online Flow Chart Tool

> A lightweight browser mind-mapping tool — an investigator's whiteboard for sketching how people and entities connect, not a source of new intelligence.

## When to use
You have gathered a set of entities and relationships (a subject, their `associate`s, employers, addresses) and want to lay them out visually to spot clusters, gaps, and next leads. Bubbl.us gives a fast, low-friction way to draw and share that link-analysis map. It generates no data — it only organises what you already have.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in at https://bubbl.us (free tier requires an account).
2. Create a central bubble for your subject; add connected bubbles for each `associate`, employer, location, or identifier.
3. Colour-code and link bubbles to show relationship types and strength.
4. Export/screenshot the map for the case file (image export may require a paid tier).
5. Pivot: use the visual gaps (an unlinked node, a dangling relationship) to decide which selector to chase next.

## Inputs → Outputs
- **In:** `associate` / entity relationships you have already collected
- **Out:** none as a selector — a visual relationship diagram (analysis artefact)
- **Empty/negative result looks like:** N/A — it reflects exactly what you enter; a sparse map means you have thin data, not a tool failure.

## Gotchas & OpSec
- Human-in-the-loop: account login required (`account-login`).
- OpSec: **passive** toward the target, but your notes are stored on a third-party SaaS — pseudonymise sensitive case data or use an offline mind-mapper instead.
- Free tier caps the number of maps and gates export; plan around it.

## Overlaps ("do both")
- Interchangeable with any diagramming/mind-map tool; for serious link analysis prefer a dedicated graph tool (e.g. Maltego-class) that also ingests and enriches data rather than just drawing it.

## Trust & verifiability
`trust: unverified` — generic SaaS with no investigative content of its own; the map is only as reliable as the data you put into it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bubbl-us-online-flow-chart-tool |
| category | documents-metadata |
| selectorsIn → selectorsOut | associate →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
