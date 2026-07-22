---
id: jsoncrack
name: JSON Crack
description: Use when you have a complex JSON blob (API dump, scraped data) and want to see it as an interactive node graph to trace structure and relationships — a visual JSON explorer.
url: https://jsoncrack.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Visualizing a JSON document as a navigable graph to understand nested structure and spot the fields that matter.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: The web editor is free (open source; self-hostable); a premium/desktop version adds features. Basic visualization needs no account.
opsec: passive
opsecNote: The hosted editor sends your JSON to their service (and can create shareable links). Do NOT paste PII, credentials, or confidential case data — self-host the open-source version or use a local viewer for sensitive material.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project (AykutSarac/jsoncrack.com) with public source; it's a visualizer, so the only real concern is that the hosted version is remote.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- jsonhero
- cyberchef
aliases:
- JSONCrack
- jsoncrack.com
tags:
- Visualization tools
- json
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# JSON Crack

> A JSON-to-graph visualizer — turns a nested blob into an interactive node diagram so you can *see* structure and relationships instead of scrolling raw text.

## When to use
A tool, API, or scrape hands you deeply nested JSON and you need to grasp its shape and find specific values fast. JSON Crack renders the document as a linked node graph (with search), which is especially good for understanding relationships and arrays that a flat text view obscures.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://jsoncrack.com/ (or self-host the open-source build for sensitive data).
2. Paste the JSON, upload a file, or import from a URL.
3. Explore the generated node graph; zoom/pan and use search to jump to a key or value.
4. Collapse/expand branches to isolate the part you care about; export the diagram if useful.
5. Pivot: values you extract (an `email`, `domain`, `geolocation`, ID) feed the matching selector search.

## Inputs → Outputs
- **In:** a JSON document (paste, file, or URL) — non-sensitive only
- **Out:** an interactive graph visualization of the JSON structure
- **Empty/negative result looks like:** invalid JSON won't render — fix the syntax first; a huge document may be slow to graph, so trim to the relevant subtree.

## Gotchas & OpSec
- **Hosted:** the online editor transmits your data and can generate shareable links — never paste PII/credentials; self-host or use a local viewer for confidential payloads.
- It visualizes, it does not decode/transform — pair with a converter for encoded values.

## Overlaps ("do both")
- Overlaps with `[[jsonhero]]` (tree/column explorer) and `[[cyberchef]]` (local decode/transform) — JSON Crack's edge is the relationship graph; use CyberChef locally when the data is sensitive.

## Trust & verifiability
`trust: community` — open source and purely a viewer; the rendered graph reflects exactly the JSON you supplied, so the only consideration is the hosted-vs-local data-handling choice.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jsoncrack |
