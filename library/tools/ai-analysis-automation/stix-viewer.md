---
id: stix-viewer
name: STIX Viewer
description: Use when you have a STIX threat-intelligence bundle and want to read it as a linked graph of indicators, actors, and relationships — returns a visual map of the CTI objects and their `ip-address`/`domain` indicators.
url: https://stix-viewer.threatlandscape.io/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Visualising STIX 2.x threat-intel bundles as a relationship graph to understand indicators, actors, and TTP links.
selectorsIn:
- document-id
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free web-based viewer; no account required.
opsec: passive
opsecNote: You upload/paste your own STIX bundle to render it — that data goes to the viewer's server, so don't paste sensitive/proprietary intel into a third-party site; for confidential bundles use a local STIX viewer instead. It queries nothing about any subject.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A community CTI utility for rendering the OASIS STIX standard; it visualises what you give it, so accuracy depends entirely on the source bundle.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- STIX bundle viewer
- Threat Landscape STIX Viewer
tags:
- threat-intel
- stix
- cti
- visualization
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# STIX Viewer

> A browser-based renderer for STIX 2.x bundles — turns a wall of CTI JSON into a navigable graph of indicators, threat actors, malware, and the relationships between them.

## When to use
You've obtained a STIX bundle (the OASIS standard format for sharing cyber threat intelligence — from a feed, an ISAC, a vendor report, or a tool export) and need to actually understand it. Raw STIX JSON is unreadable; this viewer lays out the objects and their relationships visually so you can see which `ip-address`es, `domain`s, hashes, and actors are connected. Reach for it when triaging shared threat intel and you want the structure at a glance rather than parsing JSON.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://stix-viewer.threatlandscape.io/.
2. Load your STIX 2.x bundle (upload or paste the JSON).
3. Explore the rendered graph: nodes are STIX objects (indicators, actors, malware, TTPs), edges are their relationships.
4. Drill into indicator nodes to read the concrete `ip-address`/`domain`/hash values and their context.
5. Pivot: extracted indicators feed infrastructure lookups and blocklists; actor/TTP links inform attribution.

## Inputs → Outputs
- **In:** `document-id` (a STIX 2.x bundle)
- **Out:** a relationship graph exposing `ip-address`, `domain`, and other indicators plus actor/TTP links
- **Empty/negative result looks like:** the bundle fails to render or shows isolated nodes — malformed/older STIX (1.x), or a bundle with no relationship objects; validate the STIX version and structure.

## Gotchas & OpSec
- Handles STIX 2.x; older STIX 1.x or malformed JSON won't render — validate first.
- OpSec: it's a third-party site — don't paste confidential/proprietary intel; use a local viewer for sensitive bundles.
- It only visualises; it doesn't enrich or verify the indicators — corroborate them independently.

## Overlaps ("do both")
- Complements indicator-enrichment tools: STIX Viewer shows you the *structure and relationships* in a bundle, while enrichment services (VirusTotal, passive DNS) tell you whether each extracted `ip-address`/`domain` is currently malicious — do both to go from map to actionable intel.

## Trust & verifiability
`trust: community` — a community rendering utility for a standardised format; it faithfully displays whatever bundle you provide, so trust and accuracy rest on the *source* of the STIX, not the viewer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stix-viewer |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | document-id → ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
