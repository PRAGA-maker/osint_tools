---
id: pastvu-com
name: Pastvu.com
description: Use when you have a `geolocation` or an old `image` and want historical photos mapped to that spot — returns dated, geolocated imagery to confirm or refine a location.
url: https://pastvu.com/
category: geolocation
path:
- geolocation
bestFor: Finding historical, geotagged photographs of a specific place to corroborate or refine a geolocation.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free crowdsourced historical-photo archive on an interactive map; no account needed to browse. Registration only to upload/edit.
opsec: passive
opsecNote: Browsing a public photo-map archive is fully passive — no subject interaction, nothing logged against a target. Photos are user-contributed and their placement/dates are community-supplied, so verify before relying on them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large crowdsourced archive of historical photos with community-set coordinates and dates; placements are generally careful but user-supplied, not authoritative.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- PastVu
- pastvu.com
tags:
- maps
- geolocation
- historical-photos
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Pastvu.com

> A map of historical photographs: pan to a location and see old, geotagged photos taken there — invaluable for confirming what a place looked like in the past.

## When to use
A geolocation and corroboration tool. When you're trying to pin down or verify a `geolocation` — matching a landmark in a subject's photo, confirming a building existed at a certain time, or understanding how a place has changed — PastVu overlays historical photos on a map so you can compare period imagery against your target `image`. Especially useful when Street View is too recent or a scene has since been demolished/rebuilt.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://pastvu.com/ and navigate the map to your area of interest (or search a place name).
2. Photo markers show historical images geolocated to that spot; open them to see the photo, its date range, and direction.
3. Compare architectural details, signage, and terrain against the image you're geolocating.
4. Use the year filter to focus on a period matching your evidence.
5. Pivot: a confirmed match refines your `geolocation`; the photo's metadata/date narrows a timeline; combine with satellite/Street View for present-day comparison.

## Inputs → Outputs
- **In:** `geolocation` (map area/place) or a reference `image` to match
- **Out:** dated, geolocated historical photos (`image` + `geolocation`) of that place.
- **Empty/negative result looks like:** no photo markers in the area — the location is under-covered (common outside major cities/regions with active contributors), not that the place doesn't exist.

## Gotchas & OpSec
- Coordinates and dates are crowdsourced — treat placement as a strong lead, not proof; verify with independent landmarks.
- Coverage is uneven; historically photographed urban areas are dense, rural/less-documented places sparse.
- A period match confirms a *place*, not a person — don't over-read who appears in old photos.

## Overlaps ("do both")
- Pairs with satellite/Street View and mapping tools — PastVu shows the *past* of a location while those show the present, and the comparison is what confirms a geolocation.

## Trust & verifiability
`trust: community` — a well-regarded crowdsourced archive; the photos are genuine historical images, but their exact coordinates/dates are user-supplied, so corroborate before treating a match as conclusive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pastvu-com |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, image → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
