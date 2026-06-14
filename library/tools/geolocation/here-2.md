---
id: here-2
name: Here
description: Use when you have an `address`/`geolocation` and want maps, routing, and location context from HERE's mapping platform (alternative basemap to Google).
url: http://here.com
category: geolocation
path:
- geolocation
bestFor: Cross-checking an address/route against a non-Google mapping provider.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Consumer maps are free; the developer/API platform is freemium with paid tiers.
opsec: passive
opsecNote: You query map data, not the target; nothing is sent to the person of interest. Use a research account if you sign in to the developer platform.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: HERE Technologies is a major commercial mapping provider; this is its corporate/landing domain (redirects to wego.here.com / developer.here.com).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- HERE Technologies
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Here

> The landing domain for HERE Technologies, a major commercial mapping provider offering maps, routing, and place data as a non-Google alternative basemap.

## When to use
You have an `address` or `geolocation` and want a second mapping opinion — HERE's basemap, satellite, and routing sometimes differ from Google/OSM in coverage, place names, and road detail, which helps confirm or challenge a lead. Also the entry point if you need the developer API for geocoding at scale.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open here.com (it routes to the HERE WeGo consumer map or the developer portal).
2. Search the `address`/place or enter `geolocation` coordinates to view the location and surroundings.
3. Use routing to estimate travel time/paths between two points of interest.
4. For automation, register on developer.here.com for an API key; pivot ground-level checks into [[instant-google-street-view]].

## Inputs → Outputs
- **In:** `address` or `geolocation`
- **Out:** map/satellite view, routing, and place context (`geolocation`)
- **Empty/negative result looks like:** an address that won't geocode or resolves to a region centroid — cross-check in [[here-maps]] or [[gpsvisualizer]].

## Gotchas & OpSec
- Consumer use needs no login; the developer API requires registration and a key.
- OpSec: passive — querying basemap data only; the target is not contacted.

## Overlaps ("do both")
- Essentially the same provider as [[here-maps]] (maps.here.com). Pair with Google/OSM-based tools to catch coverage gaps one map misses.

## Trust & verifiability
`trust: trusted` — HERE is an established commercial mapping vendor; the data source is reputable even though this specific URL is just the corporate front door.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | here-2 |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
