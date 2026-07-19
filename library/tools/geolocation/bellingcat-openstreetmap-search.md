---
id: bellingcat-openstreetmap-search
name: Bellingcat OpenStreetMap Search
description: Use when you have a `physical-description` of a scene (several nearby feature types) and want candidate `geolocation`s where they co-occur — returns matching map points, CSV/KML.
url: https://osm-search.bellingcat.com/
category: geolocation
path:
- geolocation
bestFor: Geolocating a photo/video by finding places where several OpenStreetMap features (e.g. a school near a supermarket near a sidewalked street) sit within a set distance of each other.
selectorsIn:
- geolocation
- physical-description
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Completely free with no paid tier. Requires signing in with a Google account to run queries.
opsec: passive
opsecNote: You query OpenStreetMap data, not the target — nothing about your subject leaves your browser. The one exposure is the required Google sign-in, which ties usage to that Google account; use a research/sock-puppet Google account, not your personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by Bellingcat, a well-known open-source investigations organisation; it runs simplified Overpass queries against public OpenStreetMap data.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- bellingcat
- bellingcat-com
- these-are-the-tools-open-source-researchers-say-they-need
- xblog-bellingcat-a-beginner-s-guide-to-flight-tracking-bellingcat
aliases:
- OSM Search
- Bellingcat OSM Search Tool
tags:
- bellingcat-toolkit
- geolocation
- openstreetmap
source: bellingcat-toolkit
lastVerified: '2026-07-19'
enrichment: full
---

# Bellingcat OpenStreetMap Search

> A point-and-click front-end to Overpass that finds every place on Earth where a chosen set of map features cluster together within a chosen distance — a workhorse for geolocating imagery.

## When to use
You have an image or video to geolocate and can list several map-visible features near each other — say a petrol station, a mosque, and a school within 200 m, or a sports pitch beside a river beside a rail line. Enter those features and the tool returns candidate coordinates where all of them co-occur, dramatically narrowing a search region. This is directly relevant to missing-persons work when a subject's photo/video shows identifiable surroundings but no address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osm-search.bellingcat.com/ and sign in with a (sock-puppet) Google account.
2. Zoom/pan the map to bound your search region — smaller areas run much faster.
3. Add the features you can see in your image (amenity types, roads, natural features) and set the maximum distance allowed between them.
4. Run the query (large areas can take up to a minute) and browse the returned points on the map.
5. Verify each candidate: open a point in Google Maps / satellite/street view to confirm it matches your imagery; export results as CSV or KML for the rest of your workflow.

## Inputs → Outputs
- **In:** a bounded map region + a set of OSM feature types and their max mutual distance (i.e. a `physical-description` of the scene translated into features)
- **Out:** candidate `geolocation` points where all features co-occur, viewable on the map or as CSV/KML
- **Empty/negative result looks like:** no points returned — either the feature combination is too specific, the distance too tight, the region too small, or (common) OSM lacks those tags there. Loosen constraints and confirm the features exist in OSM before concluding.

## Gotchas & OpSec
- Only as good as OpenStreetMap's coverage — under-mapped regions yield false negatives; missing tags ≠ missing features on the ground.
- Over-constraining (too many features, too small a distance) returns nothing; start broad, then tighten.
- Human-in-the-loop: a Google sign-in is required — use a dedicated research account.
- OpSec: passive toward the target; you're querying public map data, not their infrastructure.

## Overlaps ("do both")
- Pairs with `[[copernix]]` — this narrows candidate locations by feature clustering; Copernix adds encyclopedic context to confirm a specific landmark once you have candidates.

## Trust & verifiability
`trust: trusted` — a Bellingcat-built tool over public OpenStreetMap/Overpass data. Results are only candidate leads: always confirm each against independent satellite/street imagery before treating a location as identified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bellingcat-openstreetmap-search |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, physical-description → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
