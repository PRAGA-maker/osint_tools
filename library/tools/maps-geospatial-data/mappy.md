---
id: mappy
name: Mappy
description: Use when you have an `address`/`geolocation` in France or Western Europe and want an independent map and routing source — returns geolocation, addresses, and route/distance details.
url: http://en.mappy.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: French/Western-European maps, addresses, and route planning as an alternative basemap to Google.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
opsec: passive
opsecNote: Searching a location is a passive map query with no target involvement and no alert. Mappy is a French service (RATP-connected) with strong France/Europe coverage; its data and imagery differ from Google's, which is exactly why it's useful as a second source, but it does not provide user location-history about people.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established French mapping/route service with institutional (RATP) backing; a legitimate independent basemap for France and neighboring countries.
missingPersonsRelevance: low
coverage:
- fr
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Mappy
- mappy.com
tags:
- maps
- routing
- europe
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Mappy

> A French-made map and route service — a strong independent basemap for France and Western Europe, useful for cross-checking an address or location against something other than Google.

## When to use
You have an `address` or `geolocation` in France (or nearby Belgium/UK/Western Europe) and want to verify or enrich it on a non-Google map. Mappy has detailed French cartography, addresses, points of interest, and routing, and because its data sources differ from Google's it can confirm a placement, show a label/road Google renders differently, or give an alternative route/travel-time — valuable for triangulating a European location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://en.mappy.com/ (or mappy.com).
2. Search the `address` or place name, or enter coordinates.
3. Read the result: map placement, address details, nearby POIs, and use Directions for route/distance/time between points (`selectorsOut`).
4. Pivot: cross-check the placement against Google/Bing/Yandex/Geoportail; use routing to estimate travel time between two European locations in a timeline.

## Inputs → Outputs
- **In:** `address` or `geolocation`
- **Out:** `geolocation` (map placement, POIs), `address` (search/reverse), routes/distances
- **Empty/negative result looks like:** a place not found or thin detail outside its core region — Mappy is Europe-focused, so for locations elsewhere fall back to a global map provider.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — a map query, no target involvement.
- Strongest in France/Western Europe; coverage and imagery thin out elsewhere, and street-level photo coverage is limited — always cross-map a critical location.

## Overlaps ("do both")
- Pairs with Google/Bing/Yandex maps, IGN Géoportail (authoritative French imagery), and [[here-wego]] — multi-map cross-referencing is the point, since each provider's data and labels for a European location differ.

## Trust & verifiability
`trust: trusted` — an established French mapping service with institutional backing, so its France/Europe cartography and geocoding are reliable. Differences from Google usually reflect genuine source variation; still confirm a critical location across more than one provider.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mappy |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
