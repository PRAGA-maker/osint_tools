---
id: degulesider-mapping-program-for-europe-denmark
name: De Gule Sider Kort (Denmark maps)
description: Use when you have a Danish `address` or `geolocation` and want a street-level map with business/address context and aerial/street imagery — returns geolocation, address and nearby employer-org.
url: http://kort.degulesider.dk
category: geolocation
path:
- geolocation
bestFor: Street-level and aerial mapping of Danish addresses with directory/business overlay.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
- employer-org
status: live
pricing: free
costNote: Free consumer map/directory product from De Gule Sider (the Danish Yellow Pages); no account required.
opsec: passive
opsecNote: Loading a map is passive and does not touch the subject. The tiles are served by a Danish commercial provider; only your IP is exposed. Nothing identifies who you looked up.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial Danish directory/mapping service (Eniro/De Gule Sider); imagery and business listings are generally reliable for Denmark but not an authoritative land/address registry.
missingPersonsRelevance: high
coverage:
- dk
auth: none
api: false
localInstall: false
registration: false
aliases:
- De Gule Sider Kort
- kort.degulesider.dk
- Danish Yellow Pages maps
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# De Gule Sider Kort (Denmark maps)

> The Danish Yellow Pages' mapping product — a local-language map of Denmark that overlays business/address directory data on street and aerial imagery.

## When to use
You are working a Danish `address` or set of coordinates and want to understand the location on the ground: what the street looks like, what businesses sit at or near the address, and how the property is laid out. As a native Danish provider it often has better local business-listing density and place naming for Denmark than global map tools, which helps place a subject or corroborate an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://kort.degulesider.dk in a browser (a Danish-language interface; use your browser's translate if needed).
2. Enter the `address`, place name, or business into the search box, or navigate the map to the coordinates.
3. Read the map: pinned addresses, overlaid business/`employer-org` listings, and available aerial/street imagery. Click a listing for its directory entry.
4. Pivot: a business found at the address feeds Danish company registries (CVR) and people-search; the confirmed `geolocation` feeds cross-referencing against Google/Bing imagery.

## Inputs → Outputs
- **In:** `address` or `geolocation` (Denmark)
- **Out:** `geolocation`, resolved `address`, nearby `employer-org` (business listings)
- **Empty/negative result looks like:** the map centres on Denmark generically with no pin, or "ingen resultater" — the address may be mistyped or outside coverage.

## Gotchas & OpSec
- Denmark-only despite the harvested "Europe" label — do not expect useful coverage elsewhere.
- Danish-language UI; translate to navigate confidently.
- Directory listings are commercial and can be stale; corroborate a business↔address link against CVR.
- Fully passive: only your IP touches the tile server.

## Overlaps ("do both")
- Pairs with global imagery tools (Google/Bing Maps) — cross-check the same coordinates across providers to catch imagery-date differences and confirm ground features.

## Trust & verifiability
`trust: community` — an established commercial Danish directory/mapping service. Reliable enough for orientation and business context, but not an authoritative cadastral/address registry; verify precise ownership elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | degulesider-mapping-program-for-europe-denmark |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
