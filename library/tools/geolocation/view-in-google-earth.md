---
id: view-in-google-earth
name: View in Google Earth
description: Use when you have coordinates or a map view and want to open them in Google Earth (via a generated KML link) for 3D/historical-imagery inspection.
url: http://www.mgmaps.com/kml/#view
category: geolocation
path:
- geolocation
bestFor: Generating a KML/Google Earth link from a map position to inspect a location in 3D and historical imagery.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free utility; Google Earth itself is free.
opsec: passive
opsecNote: A client-side KML/link generator plus Google Earth viewing; no contact with the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Old mgmaps.com utility of uncertain maintenance; the underlying Google Earth handoff is the trustworthy part. Verify the site still loads.
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
- wayback-imagery
- travel-by-drone
aliases: []
tags:
- geospatial-research-and-mapping-tools
- kml
source: awesome-osint
lastVerified: ''
enrichment: full
---

# View in Google Earth

> A small (legacy) bridge utility that takes a map position and opens it in Google Earth via KML — the value is the Google Earth view, not the bridge itself.

## When to use
You have a `geolocation` and want Google Earth's strengths over a flat map: 3D terrain/buildings and, crucially, the historical-imagery timeline. This utility produces a KML/link that drops you onto that spot in Google Earth. In practice, modern Google Earth Web (earth.google.com) often makes this middle step unnecessary, but the page can still be a quick handoff.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.mgmaps.com/kml/#view (confirm it still loads — it is an old site).
2. Navigate/center the embedded map on your coordinates, or supply lat/long.
3. Use the "view in Google Earth" / KML output to launch the location in the Google Earth client or web.
4. In Google Earth, switch on the historical-imagery clock to compare dated overhead views and use 3D to judge terrain and structures.
5. Pivot: for systematic dated change detection use [[wayback-imagery]]; for low-altitude context use [[travel-by-drone]].

## Inputs → Outputs
- **In:** `geolocation` (coordinates / map center).
- **Out:** a KML/Google Earth link to that spot (then 3D + historical imagery in Earth).
- **Empty/negative result looks like:** the mgmaps page fails to load or the KML doesn't open — fall back to pasting coordinates straight into Google Earth Web.

## Gotchas & OpSec
- The host (mgmaps.com) is old and may be unmaintained; status flagged **degraded** — verify before relying on it.
- Requires Google Earth (web or desktop) installed/available to actually view results.
- Fully passive; no login or captcha.

## Overlaps ("do both")
- Largely superseded by pasting coordinates directly into Google Earth Web; pair the historical-imagery view with [[wayback-imagery]] for dated satellite change detection.

## Trust & verifiability
`trust: unverified` — the bridge utility's upkeep is uncertain; the destination (Google Earth) is fully trustworthy. Confirm the link still functions before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | view-in-google-earth |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
