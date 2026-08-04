---
id: mapa-sk
name: Mapa.sk (Zoznam)
description: Use when you have a Slovak `address` or `geolocation` and want to locate it on a detailed local map — returns coordinates, place context, and routing.
url: http://mapa.sk/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Pinpointing and contextualizing an address, street, or place inside Slovakia with local-quality map detail.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free public mapping portal from Zoznam; no account or payment required.
opsec: passive
opsecNote: You query Zoznam's map servers, not the subject — the target is never contacted. Standard web-request logging applies to you; use a VPN/sock-puppet browser if you want to avoid linking the lookup to your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by Zoznam.sk, a major Slovak web portal; map data is authoritative for Slovakia but the UI is Slovak-language.
missingPersonsRelevance: low
coverage:
- sk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- mapa.zoznam.sk
- Zoznam Mapy
tags:
- maps
- slovakia
- geolocation
source: bellingcat-toolkit
lastVerified: '2026-08-04'
enrichment: full
---

# Mapa.sk (Zoznam)

> Slovakia's local map portal — the country-specific equivalent of a national mapping service, with detailed city maps, routing, and coordinate lookup.

## When to use
Your investigation touches Slovakia and you have a Slovak `address`, street name, or `geolocation` you need to place on a map with better local detail than a global provider offers. Useful for confirming an address exists, reading the surrounding street layout, measuring distances/areas, and pulling precise coordinates for a place in a Slovak city.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://mapa.sk/ (it redirects to https://mapa.zoznam.sk/).
2. Type the `address` or place name into the search box — autocomplete suggests Slovak streets, cities, and points of interest (e.g. `Košice, ulice`).
3. Read the pin location and surrounding context; use the toolbar for the GPS-coordinate finder to extract a precise `geolocation`, or route planning / distance and area measurement tools.
4. Pivot: feed the extracted coordinates into a global imagery/street-level tool for cross-referencing, or the confirmed address into people/records searches.

## Inputs → Outputs
- **In:** `address` or `geolocation` (Slovakia)
- **Out:** `geolocation` (coordinates), confirmed `address`, place context, routes
- **Empty/negative result looks like:** no autocomplete match / an empty map view — means the address string is wrong or the place is outside Slovakia's coverage, not that the location doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none; no login required.
- Language: the interface is Slovak — use browser translation if needed, but enter Slovak street/city names for best autocomplete results.
- OpSec: **passive** — this never contacts the subject; only your own request is logged by Zoznam.
- Coverage is Slovakia-focused; for cross-border areas fall back to a global map provider.

## Overlaps ("do both")
- Pairs with a global satellite/street-view provider — Mapa.sk gives authoritative local addressing and routing while the global tool gives imagery and street-level views; run both to confirm a Slovak location.

## Trust & verifiability
`trust: community` — data comes from Zoznam, a mainstream Slovak portal, so it is reliable for Slovakia; verify anything border-adjacent against a second map.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapa-sk |
