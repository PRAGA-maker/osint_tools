---
id: malfrat-s-osint-map
name: Malfrat's OSINT Map
description: Use when you have a starting selector (`username`/`email`/`phone`/`image`) and need to pick the right tool — an interactive map that branches by selector to curated, current OSINT tools.
url: https://map.malfrats.industries/
category: search-engines
path:
- search-engines
bestFor: Choosing the right OSINT tool for a given lead, via an interactive mind-map branched by selector type, with flags for cost/install/whether a tool alerts the target.
selectorsIn:
- username
- email
- phone
- image
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, community-maintained web resource; no account.
opsec: passive
opsecNote: Browsing the map is passive. Usefully, its legend flags which listed tools may alert the target (an "active" warning) — read those flags before you actually run a downstream tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained interactive OSINT tool map (GitHub/Discord contributions); reputable and kept relatively current, but it is a pointer resource whose links depend on external tools.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- malfrats.industries
- OSINT map
tags:
- tool-collection
- mindmap
- username
- email
- phone
source: ultimate-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Malfrat's OSINT Map

> An interactive, selector-branched map of OSINT tools — start from what you have (a handle, an email, a number, a photo) and it walks you to the tools that work on it.

## When to use
You have a lead but aren't sure which tool fits — you hold a `username`, `email`, `phone`, or `image` and want a current, curated shortlist rather than a stale link dump. Malfrat's Map organises tools as a visual mind-map that branches by selector and marks each tool with flags (needs install, costs money, web-based, alerts the target). Reach for it at the *start* of an investigation to plan your tool path, or when a familiar tool dies and you need a replacement.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://map.malfrats.industries/.
2. Navigate to the branch for your selector (username / email / phone number / image, etc.).
3. Read the emoji legend on each tool: install requirement, cost, web accessibility, docs, and — importantly — whether it may alert the target.
4. Pick a tool and follow its link; apply that tool's own workflow and OpSec.
5. Pivot: as your investigation produces new selectors, return to the map's other branches to pick the next tool.

## Inputs → Outputs
- **In:** a starting selector (`username`/`email`/`phone`/`image`) — used to choose tools
- **Out:** a curated shortlist of tools (many resolving to `social-profile`s and other selectors) with capability/OpSec flags
- **Empty/negative result looks like:** a branch with few/outdated entries — no map is exhaustive; cross-reference `[[molfar-com]]` and other collections to fill gaps.

## Gotchas & OpSec
- It's a chooser, not a search engine: the map points to tools; the actual lookups happen elsewhere.
- Currency: community maps drift — verify a listed tool is still live before relying on it.
- OpSec: passive to browse, and its per-tool "alerts target" flags are a genuine planning aid — heed them.

## Overlaps ("do both")
- Pairs with `[[molfar-com]]` — a second curated directory; different coverage, so use both when scoping tools.
- Pairs with any downstream tool it recommends (e.g. `[[palenath]]`, `[[gitfive]]`, `[[pimeyes]]`).

## Trust & verifiability
`trust: community` — a reputable, actively-contributed tool map; trust its structure and flags, but confirm each linked tool independently since the map doesn't control those external services.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | malfrat-s-osint-map |
