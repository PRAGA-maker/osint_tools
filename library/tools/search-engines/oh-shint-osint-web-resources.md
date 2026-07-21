---
id: oh-shint-osint-web-resources
name: OH SHINT! OSINT Web Resources
description: Use when you have a case type but not the right tool — returns a curated, categorised directory of OSINT web resources (people, phone, real estate, etc.) to pick your next lookup.
url: https://ohshint.gitbook.io/oh-shint-its-a-blog/osint-web-resources/introduction-to-osint-web-resources
category: search-engines
path:
- search-engines
bestFor: A maintained, topic-organised catalogue of OSINT tools to discover the right resource for a given selector/case type.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public GitBook; downloadable as PDF and importable HTML bookmarks, no account needed.
opsec: passive
opsecNote: A static reading resource — you browse a tool catalogue, so there is no target interaction and nothing to leak. OpSec only matters once you leave here and run the tools it lists; apply each of those tools' own precautions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single practitioner-maintained GitBook (OH SHINT!); it points to third-party tools, so vet each linked resource independently before relying on it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- data-sets-oh-shint
aliases:
- OH SHINT
- ohshint gitbook
tags:
- tool-collection
- gitbook
- methodology
source: ultimate-osint
lastVerified: '2026-07-21'
enrichment: full
---

# OH SHINT! OSINT Web Resources

> A practitioner-maintained GitBook that bundles a large, categorised catalogue of OSINT web resources — a "where do I even start" index for a given case type.

## When to use
You know the selector or case type (a `name`, `phone`, `address`, a real-estate question, a company) but not which site to use, or you want to make sure you haven't missed an obvious resource. Use it as a discovery layer: jump to the relevant category, pick promising tools, then go run them. It's a menu of options, not a lookup itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the GitBook and browse the left-hand category tree (people investigations, phone numbers, real estate, etc.).
2. Skim the "Recently Added Resources" section for newer additions.
3. Shortlist the tools that fit your selector; open them in a research browser.
4. Optionally export the whole set as PDF or import the HTML bookmarks for offline use.
5. Pivot: this feeds you *into* the actual tools — take your selector to the one you picked.

## Inputs → Outputs
- **In:** your case type / selector category (used to navigate)
- **Out:** a curated list of candidate OSINT tools/links for that category — pointers, not data
- **Empty/negative result looks like:** a thin category or dead outbound links (some listed tools may have since died) — treat the catalogue as a starting map, and verify each linked tool is still alive.

## Gotchas & OpSec
- It's an index, not a data source — no results about a subject appear here.
- Curated by one person and not exhaustively pruned; expect some stale/dead links among current ones.
- Last major refresh noted around 2023; cross-check against newer resource lists for anything cutting-edge.

## Overlaps ("do both")
- Pairs with `[[data-sets-oh-shint]]` — the same author's companion collection focused on datasets; use both to cover tools and raw data sources.

## Trust & verifiability
`trust: community` — a well-regarded but single-maintainer catalogue; it earns trust as a discovery aid, while the authority of anything you find still rests on the individual third-party tool you follow it to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oh-shint-osint-web-resources |
| category | search-engines |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
