---
id: markmap
name: MARKMAP
description: Use when you have investigation notes in Markdown and want to turn them into an interactive mind map to see structure and gaps — an analysis/visualisation aid, not an intelligence source.
url: https://markmap.js.org/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Turning a Markdown outline of findings into an interactive SVG/HTML mind map.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; runs in the browser (also available as a CLI/VS Code extension).
opsec: passive
opsecNote: The web playground renders your Markdown client-side, but treat any hosted instance as untrusted with sensitive case notes — for protected material use the offline CLI/extension so nothing is transmitted. It reveals nothing about a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project (markmap.js.org / gera2ld); transparent, client-side rendering with no data claims of its own.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- markmap.js
tags:
- NOOSINT tools
- mind-map
- visualization
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# MARKMAP

> A Markdown-to-mind-map renderer — feed it a bullet outline of your findings and it produces an interactive, zoomable tree that makes structure and missing branches obvious.

## When to use
You keep case notes as Markdown bullets (subject → identifiers → leads) and want to *see* them as a tree to spot which branches are thin or unexplored. Markmap converts headings/lists into an interactive mind map. It organises what you already know; it collects nothing new.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://markmap.js.org/ and use the live editor (or install the CLI / VS Code extension for offline use).
2. Paste a Markdown outline — headings and nested bullets become branches and leaves.
3. Interact with the rendered map: collapse/expand branches, zoom, and reorganise the source to reflect relationships.
4. Export to SVG/HTML for the case file or a briefing.
5. No pivot — visual gaps tell you which selector/lead to chase next.

## Inputs → Outputs
- **In:** none as a selector — a Markdown outline of your findings
- **Out:** none as a selector — an interactive mind-map visualisation
- **Empty/negative result looks like:** N/A — output mirrors your input; a sparse map means thin notes, not a failure.

## Gotchas & OpSec
- Formatting is deliberately minimal — it visualises hierarchy, not rich diagrams; use a dedicated link-analysis tool for relationship graphs.
- OpSec: prefer the offline CLI/extension for sensitive notes so nothing leaves your machine.

## Overlaps ("do both")
- Complements `[[bubbl-us-online-flow-chart-tool]]` and dedicated graph tools; markmap is fastest when your notes are already in Markdown.

## Trust & verifiability
`trust: community` — open-source, client-side renderer; the map is a faithful transform of your text, nothing more.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | markmap |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
