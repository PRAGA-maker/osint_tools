---
id: worldwide-osint-tools-map
name: Worldwide OSINT Tools Map
description: Use when you need to discover country-specific OSINT resources (registries, directories, search sites) for the country where a case is located.
url: https://cipher387.github.io/osintmap/
category: geolocation
path:
- geolocation
bestFor: A clickable world map indexing OSINT tools and public resources grouped by country.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Free, open project hosted on GitHub Pages.
opsec: passive
opsecNote: A static directory of links; browsing it contacts only the index, not the target. Each linked tool has its own OpSec profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Curated by cipher387, a well-known OSINT author; it is an index of third-party tools whose links can age — verify each linked resource.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- cipher387 osintmap
- OSINT Map
tags:
- directory
- meta-resource
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Worldwide OSINT Tools Map

> A clickable world map by cipher387 that indexes country-specific OSINT resources — a discovery layer, not a lookup tool itself.

## When to use
Your case has a national/jurisdictional dimension and you don't know what local resources exist — company registries, court/property records, regional people-search, local directories. Click the country to get a curated list of OSINT tools relevant to it. Especially helpful when a missing-persons case crosses into a country whose record systems you don't know. It returns *tools*, not facts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cipher387.github.io/osintmap/.
2. Click the country (or region) of interest on the map.
3. Read the listed resources/tools for that country and open the relevant ones in new tabs.
4. Evaluate each linked tool on its own merits (some links may be stale).
5. Pivot: each linked resource becomes your actual lookup step — apply its own selectors and OpSec there.

## Inputs → Outputs
- **In:** `geolocation` (a country/region you're researching).
- **Out:** a curated list of country-specific OSINT tools/links (no direct selector output; it routes you onward).
- **Empty/negative result looks like:** thin or no entries for a small/less-covered country — fall back to general directories and search.

## Gotchas & OpSec
- It is an **index**: value depends on the maintainer's curation and on links staying alive — expect some dead/outdated entries.
- No login or captcha; browsing the map is passive. The tools it sends you to may not be — check each one.

## Overlaps ("do both")
- Complements broad OSINT directories/awesome-lists; use it specifically when you need the *country* lens.

## Trust & verifiability
`trust: community` — maintained by a respected OSINT author, but it aggregates third-party tools whose reliability and availability vary; verify each linked resource before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | worldwide-osint-tools-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → (directory of tools) |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
