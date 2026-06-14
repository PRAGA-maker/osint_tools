---
id: google-maps
name: Google Maps
description: Use when you have an address or coordinate and need Street View, routing, POIs, or to ground-truth a location at street level.
url: https://www.google.com/maps/
category: geolocation
path:
- geolocation
bestFor: Address/coordinate lookup with Street View ground-truthing, routing, and points-of-interest correlation.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
- image
status: live
pricing: freemium
costNote: Free for interactive web use; the Maps Platform API for programmatic access is paid (usage-based).
opsec: passive
opsecNote: Browsing the map and Street View does not contact the target. Google logs queries to your account if signed in — use a research identity or stay signed out for sensitive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google Maps is the de facto standard for consumer geolocation, with the most complete Street View and POI coverage globally.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases: []
tags:
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# Google Maps

> The standard consumer mapping platform — address/coordinate lookup, the world's broadest Street View coverage, routing, and rich points-of-interest data.

## When to use
You have an `address` or `geolocation` and need to ground-truth it: read house numbers and signage in Street View, identify nearby businesses/landmarks (POIs) that corroborate a sighting, measure travel routes/times between a last-known point and destinations, or match a photo's background to street-level imagery. The first stop for confirming "what's actually there."

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.google.com/maps/.
2. Search an address/place or paste coordinates; right-click a point for exact lat/long.
3. Drag the pegman for Street View; use the time control where available to see older Street View captures.
4. Use Directions for routing/ETAs; browse POIs and reviews for corroborating detail.
5. Pivot: deepen with `[[dualmaps]]` (synchronized views), `[[google-earth-pro]]` (historical aerial), or `[[google-maps-streetview-player]]` (drive a route).

## Inputs → Outputs
- **In:** `address` or `geolocation`.
- **Out:** confirmed `geolocation`/`address`, Street View `image`, routes, and POI context.
- **Empty/negative result looks like:** no Street View in rural/restricted areas, or an address that geocodes to the wrong spot — verify against aerial and cross-check the coordinate.

## Gotchas & OpSec
- Human-in-the-loop: none for interactive use; programmatic API access is paid and key-gated.
- Street View capture dates vary; an old capture may not reflect current conditions — check the date stamp.
- OpSec: passive; stay signed out (or use a research account) for sensitive locations since Google logs queries.

## Overlaps ("do both")
- Pairs with `[[dualmaps]]` and `[[google-earth-pro]]` — Maps is the canonical Street View/POI source; those add synchronized and historical views.

## Trust & verifiability
`trust: trusted` — the most complete and current consumer mapping/Street View data available; the main caveat is imagery-capture dates.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-maps |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address, image |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
