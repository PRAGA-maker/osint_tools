---
id: lost-places-map
name: Lost places map
description: Use when you have an `image` or `geolocation` of an abandoned/urbex site and want to identify or locate it — returns mapped `geolocation`s of documented "lost places".
url: https://www.google.com/maps/d/viewer?mid=1M6OeH-DCWCLHGLQ2_CiGPd0aO7IjPHqo&hl=de&ll=50.06460483234834%2C8.681870511153518&z=10
category: geolocation
path:
- geolocation
bestFor: Matching a photo of an abandoned/derelict location (mostly German-speaking Europe) to a mapped, documented urban-exploration site.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public Google My Maps layer curated from a "Lost Places" urbex community; no account to view.
opsec: passive
opsecNote: Viewing a shared Google map is anonymous. Note the underlying reports originate from a Facebook community — following links there is account-linked, so use a sock puppet if you go deeper.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A crowd-curated hobbyist map of abandoned sites; locations are community-reported and unverified, and the layer persists only while its creator maintains it.
missingPersonsRelevance: medium
coverage:
- de
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Lost Places Google Map
- Verlassene Orte Karte
tags:
- Maps, Geolocation and Transport
- Anomalies and "Lost Places"
- urbex
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Lost places map

> A community-curated Google My Maps layer of abandoned and derelict "lost places" — useful for matching a photo of a ruin to a documented, mapped location.

## When to use
You have an `image` of an abandoned building, industrial ruin or derelict site (a common backdrop in urbex photos and, occasionally, casework), and you want to identify or place it. This map plots urban-exploration reports — mostly across the German-speaking region — so you can compare features and read the community's notes to pin a `geolocation`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the map at the URL and pan/zoom to a candidate region, or scan the pinned sites.
2. Click pins to read each site's description, photos and any linked report.
3. Compare your `image`'s distinctive features (architecture, signage, machinery, surroundings) against mapped entries.
4. Pivot: once you have a candidate location, confirm with satellite/street imagery and the historical map layers ([[map-view-ngmdb]] for the US; national mapping elsewhere), then geolocate precisely.

## Inputs → Outputs
- **In:** `image` of an abandoned site and/or an approximate `geolocation`
- **Out:** `geolocation` of matching documented lost places, with community notes
- **Empty/negative result looks like:** no pin matches — the site isn't in this community's coverage (heavily DE/Central-Europe biased) or isn't documented here. Absence is expected outside the region; try other urbex maps and reverse-image search.

## Gotchas & OpSec
- **Regional bias:** coverage skews to German-speaking Europe; it is not a global urbex index.
- Community-reported and unverified — a pin's location/description can be wrong or deliberately vague to deter trespass.
- OpSec: viewing the map is passive; the source Facebook community is account-linked if you dig into it.

## Overlaps ("do both")
- Pairs with reverse-image search and satellite/street imagery for confirmation, and with historical map tools for reading a site's past use.

## Trust & verifiability
`trust: community` — a hobbyist crowd-sourced map. Treat locations as leads and confirm any identification independently with imagery before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lost-places-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
