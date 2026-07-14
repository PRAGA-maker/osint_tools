---
id: whereis-com-maps-of-australia
name: Whereis.com (Australia Maps)
description: Use when you have an Australian `address` or place and want to map, verify, and geolocate it (coordinates, directions, nearby context) — returns geolocation and normalised address.
url: http://www.whereis.com
category: geolocation
path:
- geolocation
bestFor: Mapping and verifying Australian addresses/places and getting coordinates, directions, and local context.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free consumer mapping service for Australia; no account required for basic map/search/directions.
opsec: passive
opsecNote: Map/address lookups run against a public mapping service and never touch any person; nothing is disclosed to a target. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running Australian consumer mapping site (Sensis/Yellow-brand heritage); reliable for AU geography, though not an authoritative address register.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- whereis.com
- Whereis Australia maps
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- australia
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Whereis.com (Australia Maps)

> An Australia-focused consumer mapping service: locate, verify, and get directions to Australian addresses, streets, and places.

## When to use
You have an Australian `address` or place name and want to confirm it exists, pin its coordinates (`geolocation`), see its surroundings, or plan/measure routes to it. Useful as an AU-specific complement to global map tools when working a subject's Australian address — for verifying an address is real and well-formed, and for building local geographic context (nearby landmarks, access routes).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.whereis.com.
2. Enter the Australian `address` or place to map it, or use directions between two points.
3. Read the map: pinned location, normalised `address`, coordinates, and surrounding streets/landmarks.
4. Pivot: coordinates feed reverse-geocoding and cross-mapping (compare against Google Maps/Street View for imagery); a verified address feeds AU people/property lookups.

## Inputs → Outputs
- **In:** `address` or place (`geolocation`) in Australia
- **Out:** map location, coordinates (`geolocation`), normalised `address`, directions
- **Empty/negative result looks like:** the address doesn't resolve or maps to the wrong spot — it may be mistyped, very new, rural/unaddressed, or outside AU coverage.

## Gotchas & OpSec
- Coverage is **Australia** — use global map providers for other countries.
- A consumer map is not an authoritative address/occupancy register; it geolocates places, it does not tell you who lives there.
- OpSec: passive; a map lookup with no contact to any person.

## Overlaps ("do both")
- Do both with Google Maps/Street View and reverse-geocoding tools — cross-map the same AU location to get imagery and confirm coordinates from a second source.

## Trust & verifiability
`trust: community` — a reputable Australian consumer mapping service, reliable for AU geography; treat it as a mapping aid, not an official address authority.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whereis-com-maps-of-australia |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
