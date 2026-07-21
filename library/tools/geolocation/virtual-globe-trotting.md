---
id: virtual-globe-trotting
name: Virtual Globetrotting
description: Use when you have `geolocation` coordinates or a landmark/celebrity-home lead and want a labelled satellite/Street View catalogue — returns identified places and `geolocation` for known locations.
url: https://virtualglobetrotting.com/
category: geolocation
path:
- geolocation
bestFor: A crowd-catalogued directory of identified locations (celebrity homes, landmarks, military/abandoned sites) on Google/Bing maps, searchable by name or coordinates.
selectorsIn:
- geolocation
- name
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free to browse and search; an optional free account lets you submit/save places. No cost to view.
opsec: passive
opsecNote: Passive — you browse a public community catalogue of map locations, no target interaction. Note the underlying imagery is Google/Bing Maps; if you follow entries into Street View, standard map-provider logging applies, but nothing is disclosed to any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: User-submitted location catalogue; entries (especially "celebrity home" pins) are crowd-claimed and can be wrong or outdated — always confirm the coordinates against current imagery and independent sourcing.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- virtualglobetrotting-com
aliases:
- VirtualGlobetrotting
- virtualglobetrotting.com
tags:
- Maps, Geolocation and Transport
- Anomalies and "Lost Places"
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Virtual Globetrotting

> A community-built catalogue of identified map locations — celebrity homes, landmarks, military and abandoned sites — pinned to Google/Bing coordinates and searchable both ways.

## When to use
Two directions: (1) you have a `name` or place-type (a public figure, a famous building, a category like "abandoned") and want its mapped location; (2) you have `geolocation` coordinates and want to see whether the community has already identified/labelled that spot. Handy for corroborating a claimed residence, identifying a landmark visible in a photo, or getting a labelled reference for a coordinate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://virtualglobetrotting.com/.
2. Search by `name`/keyword, or browse categories (celebrity homes by profession, landmarks, military, abandoned, natural).
3. Open an entry for its satellite/Street View image, title, submitter, and coordinates/location (`address` area).
4. Click through to Google/Bing/Street View to inspect the actual imagery.
5. Pivot: a confirmed `geolocation` → property/records lookups for that address; a landmark ID → matching it against a photo you're geolocating.

## Inputs → Outputs
- **In:** a `name`/landmark/category, or `geolocation` coordinates
- **Out:** identified place entries with coordinates (`geolocation`) and location/`address` context, plus reference imagery
- **Empty/negative result looks like:** no entry for your subject/coordinate — the community simply hasn't catalogued it (most of the world isn't); absence tells you nothing, and a "celebrity home" pin is a claim, not proof.

## Gotchas & OpSec
- Crowd-sourced and unverified — "celebrity home" locations are frequently wrong, outdated, or the wrong property; never treat a pin as confirmation of where someone lives.
- Imagery is Google/Bing; the site just labels it.
- Passive to browse; only your own map-provider queries are logged.

## Overlaps ("do both")
- Pairs with `[[virtualglobetrotting-com]]` (the same platform) and with direct Street View/satellite tools — use this to find a candidate location, then confirm the exact spot and details in live imagery and property records.

## Trust & verifiability
`trust: community` — a user-submitted catalogue useful as a lead generator; every pin (especially residence claims) must be verified against current imagery and independent sources before being relied upon.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | virtual-globe-trotting |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, name → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
