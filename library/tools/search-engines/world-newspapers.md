---
id: world-newspapers
name: World-Newspapers
description: Use when you have a place (`address`/`geolocation`) and want that region's local newspapers and magazines to search for coverage of a subject — returns links to local news outlets.
url: http://www.world-newspapers.com
category: search-engines
path:
- search-engines
bestFor: Finding the local newspapers/magazines of a country or region so you can search local press for a person or event.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free directory; no account required.
opsec: passive
opsecNote: A link directory — you browse it and then read third-party news sites. Nothing about your subject is submitted here; normal OpSec applies once you follow a link to an outlet's own search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing curated directory of world news outlets; link quality varies and some listed sites may be stale.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- world-newspapers.com
tags:
- news
- newspaper-directory
- local-press
source: awesome-osint
lastVerified: '2026-07-23'
---

# World-Newspapers

> A curated directory of newspapers, magazines, and news sites worldwide, organised by country and language — the starting point for finding which local outlet to search.

## When to use
You know roughly *where* something happened or where a subject lived (`address`/`geolocation`) and want to search **local** press — the small regional papers that carry obituaries, court notices, missing-person appeals, school and community items that never reach national media or generic web search. World-Newspapers helps you find which outlets exist for that place so you can then search each one directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.world-newspapers.com and drill into the target country/region (and language).
2. Note the relevant local newspapers, magazines, and news portals it lists.
3. Follow each link and use that outlet's own search (or a `site:` Google dork against its domain) for your subject's `name`, place, or event.
4. Pivot: a local obituary, notice, or article yields relatives (`associate`), dates (`dob`/death), employers, and photos to follow up.

## Inputs → Outputs
- **In:** a place/region (you supply the geography; the directory has no search box for people)
- **Out:** links to local news outlets to search (which in turn yield `name`, `associate`, dates, photos)
- **Empty/negative result looks like:** thin or dead links for a region — fall back to a national news aggregator or a country-specific media directory.

## Gotchas & OpSec
- It's a directory, not a search engine: it points you to outlets; the actual person-search happens on each outlet's site.
- Some listings are outdated (defunct papers, moved domains) — verify the outlet still exists before relying on it.
- OpSec: **passive** — browsing the directory reveals nothing about your subject.

## Overlaps ("do both")
- Pairs with news aggregators and archive tools — the directory finds the local outlet; archives recover its older articles that are no longer live.

## Trust & verifiability
`trust: community` — a useful curated index; treat any linked outlet's reporting on its own merits and confirm the outlet is current before citing it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-newspapers |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
