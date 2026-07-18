---
id: wikinearby
name: WikiNearby
description: Use when you have coordinates and want Wikipedia-documented places around them — returns nearby notable geolocation/landmarks to identify or corroborate a location from a photo.
url: https://wikinearby.toolforge.org/?lang=en&q=55.333056%2C+27.248889
category: geolocation
path:
- geolocation
bestFor: Listing Wikipedia-documented landmarks, towns, stations, and features near a set of coordinates, in many languages.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free Wikimedia Toolforge tool; no account, no payment.
opsec: passive
opsecNote: Runs on Wikimedia Toolforge and reads public Wikipedia geodata; you submit coordinates, not anything about a person. Standard web logging only. Safe for routine geolocation work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hosted on Wikimedia's official Toolforge platform and backed by Wikipedia's geotagged-article data; the underlying data is community-maintained Wikipedia.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- wikishootme
aliases:
- wikinearby.toolforge.org
- Wiki Nearby
tags:
- geolocation
- wikipedia
- landmarks
- Maps, Geolocation and Transport
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# WikiNearby

> A Wikimedia Toolforge tool that lists every Wikipedia-documented place near a coordinate — landmarks, towns, stations, monuments — a quick way to name what's in the frame when geolocating.

## When to use
You have narrowed a photo or clue to an approximate `geolocation` (coordinates, or a spot on a map) and want to know which notable, named features sit nearby. WikiNearby returns Wikipedia articles for streets, towns, rail stations, churches, monuments, and other landmarks around that point — candidate identities for a building or landmark visible in an image, and a way to confirm you're in the right area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wikinearby.toolforge.org/ and set the coordinates in the query (e.g. `q=55.333056, 27.248889`) and `lang` (use the local language for better local coverage).
2. Read the ranked list of nearby Wikipedia-documented places with distances and links.
3. Match entries against features in your photo — a named church, station, or monument you can visually confirm.
4. Pivot: open the matching Wikipedia article for exact coordinates and images, then jump to Street View / satellite to ground-truth. Compare with `[[wikishootme]]` for geotagged photos of the same spot.

## Inputs → Outputs
- **In:** `geolocation` (coordinates / map point)
- **Out:** `geolocation` (nearby named landmarks with coordinates and Wikipedia links)
- **Empty/negative result looks like:** few or no articles nearby — normal for rural or sparsely-documented areas; switch to the local-language wiki or widen the radius, and don't read emptiness as "wrong location."

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — you query public geodata, nothing about a subject leaves you beyond coordinates.
- Coverage bias: Wikipedia geotag density is far higher in Western/urban areas. A thin result reflects documentation gaps, not the absence of places. Try `lang=` matching the region.

## Overlaps ("do both")
- Pairs with `[[wikishootme]]` (geotagged Wikimedia photos at a point) and with satellite/Street-View imagery — WikiNearby names the candidate landmarks, the others show you what they look like to confirm the match.

## Trust & verifiability
`trust: trusted` — it is an official Wikimedia Toolforge tool over Wikipedia's geodata; verify any specific landmark by opening its article and checking coordinates/imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikinearby |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
