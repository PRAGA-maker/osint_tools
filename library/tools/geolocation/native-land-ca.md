---
id: native-land-ca
name: Native-land.ca
description: Use when you have a `geolocation` and want the Indigenous nations, languages and treaties historically tied to that point — returns territorial/cultural context for the location.
url: https://native-land.ca/
category: geolocation
path:
- geolocation
bestFor: Adding Indigenous-territory, language and treaty context to a set of coordinates or a place — background enrichment, not a legal boundary source.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Completely free; the operator (a Canadian non-profit) also publishes GeoJSON and a free public API.
opsec: passive
opsecNote: Read-only map lookup of a location; nothing is disclosed to any subject and no target infrastructure is touched. Safe from any browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by Native Land Digital, a non-profit, with community-sourced boundaries; the site explicitly states its maps are not official or legal boundaries — use as context, not authority.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Native Land Digital
- native-land.ca
tags:
- Maps, Geolocation and Transport
- Politics, conflicts and crisis
- indigenous
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Native-land.ca

> A community-mapped atlas of Indigenous territories, languages and treaties — click a point and learn whose ancestral land it is.

## When to use
You have a `geolocation` (coordinates or a place) and want cultural/territorial context: which Indigenous nation(s) the land is associated with, what language was spoken there, and which treaties apply. Relevant when a case touches Indigenous communities or remote ancestral lands, or when you need to understand the human geography behind a location. This is enrichment/context, not a lookup that returns a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://native-land.ca/ and use the Classic, Placenames or Reciprocity map.
2. Search a place or click the point of interest on the map.
3. Read the overlaid layers: Indigenous territory/nation, language, and treaty for that location, each linking to more detail.
4. For automation, pull the free GeoJSON layers or query the public API to resolve coordinates → territory/language/treaty programmatically.
5. Pivot: use the named nation/community to find local contacts, band offices, or region-specific resources; contact the nation directly for authoritative boundaries.

## Inputs → Outputs
- **In:** `geolocation` (point or place)
- **Out:** associated Indigenous nation(s), language(s) and treaty context for that `geolocation` (contextual, with links)
- **Empty/negative result looks like:** an area with no mapped layer, or overlapping/ambiguous territories — meaning the community-sourced data is incomplete there, not that no nation is associated.

## Gotchas & OpSec
- The maps are **explicitly not official or legal boundaries** — the operator says to contact nations directly for definitive information.
- Data is community-contributed, so completeness and precision vary by region.
- It returns cultural/geographic context, not personal selectors — treat it as background enrichment.

## Overlaps ("do both")
- Pairs with mainstream mapping/geocoding tools — those give the physical/administrative location, while Native-land adds the Indigenous-territory layer they omit.

## Trust & verifiability
`trust: community` — a respected non-profit with crowd-sourced boundaries that it openly labels as non-authoritative; excellent for context, but verify any boundary claim with the relevant nation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | native-land-ca |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
