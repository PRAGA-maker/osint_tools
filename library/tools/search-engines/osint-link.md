---
id: osint-link
name: Osint.link
description: Use when you need to discover an OSINT tool for a task — returns a categorised directory of OSINT resources (search, social, geolocation, breach, records, etc.).
url: https://osint.link/
category: search-engines
path:
- search-engines
bestFor: A free, browsable portal of OSINT tools and resources organised by investigation category.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open; no account or paywall.
opsec: passive
opsecNote: It's a static directory of links — browsing it reveals nothing about any target. OpSec lives entirely in the destination tools you click through to; assess each on its own before running it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained link portal (associated with @onlineosint / darknessgate); curation is helpful but it's a directory of third-party tools, not a vetted or tested toolset.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- osint.link
- OSINT Link portal
tags:
- directory
- osint-resources
- meta
source: ultimate-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Osint.link

> A categorised portal of OSINT tools and resources — a jumping-off directory when you know the task but not yet the tool.

## When to use
You're deciding *which* tool to use for a step — a reverse-image search, a breach check, a geolocation aid, a public-records lookup — and want a curated menu organised by category. Osint.link is a directory, not an engine: use it to find and reach specialised resources, then go run those. Handy for discovering tools this library may not yet cover, and for orienting a fresh investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.link/.
2. Browse to the category matching your need (search engines, social media, geolocation, technical/footprinting, data breaches, government records, etc.).
3. Click through to the individual tool and evaluate it — check it's live and understand its OpSec before use.
4. Pivot: the destination tool does the actual lookup; return to the portal to find the next step's resource.

## Inputs → Outputs
- **In:** a task/category (not a selector)
- **Out:** links to categorised OSINT tools and resources
- **Empty/negative result looks like:** a category with stale/dead links — like any directory it suffers link rot, so verify each destination is live before relying on it.

## Gotchas & OpSec
- It's a **catalogue**, not a lookup — the "output" is other tools, so budget time to evaluate each destination.
- Curation quality and freshness depend on one maintainer; cross-check against other directories for completeness.
- OpSec: browsing is passive; the linked tools range from passive to active — judge each individually.

## Overlaps ("do both")
- Pairs with other meta-directories (OSINT Framework, awesome-osint lists): different curators surface different tools, so consult more than one when scoping an approach.

## Trust & verifiability
`trust: community` — a single-maintainer link portal. The curation is useful for discovery, but it's a pointer to third-party tools, not a data source; verify each linked tool's status and reliability yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-link |
