---
id: observer
name: FarEarth Observer
description: Use when you want to watch Landsat satellite imagery being acquired in near real-time — returns a live stream of freshly downlinked scenes by `geolocation`, minutes after capture.
url: https://live.farearth.com/observer/
category: image-video-face
path:
- image-video-face
bestFor: Viewing near-real-time Landsat 8/9 imagery as ground stations downlink it, to see fresh wide-area scenes of a region.
selectorsIn:
- geolocation
selectorsOut:
- image
- geolocation
status: live
pricing: free
costNote: Free public viewer from Pinkmatter Solutions; the same technology powers the USGS EarthNow viewer. No account required.
opsec: passive
opsecNote: Passive — you watch a public satellite-imagery stream; nothing is tied to any subject and nothing leaks. Note this is medium-resolution earth-observation imagery, not people-level detail.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Pinkmatter Solutions and adopted by the USGS (EarthNow) to visualize Landsat acquisition; the imagery is official Landsat data displayed near-live.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- FarEarth Global Observer
- EarthNow
- observer.farearth.com
tags:
- Maps, Geolocation and Transport
- Satellite/aerial imagery
- landsat
- near-real-time
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# FarEarth Observer

> A near-live window on Landsat: watch satellite scenes appear on the map within minutes of the sensor imaging the ground — wide-area situational imagery, not people-level detail.

## When to use
You want the freshest available medium-resolution overhead imagery of a region — to see broad conditions (flooding, fire, snow cover, large-scale change) shortly after a Landsat pass, or to understand what earth-observation coverage of an area looks like. It streams scenes as ground stations downlink them, so it's about *recency and wide-area context*, not zooming to a street or a person. Low direct missing-persons value on its own, but useful for environmental/terrain context around a search area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://live.farearth.com/observer/ (the same engine drives the USGS EarthNow viewer at earthnow.usgs.gov).
2. Watch the globe as newly acquired Landsat 8/9 strips render in near real-time; pan to your region of interest.
3. Note that every point on Earth is imaged roughly every 16 days — use the stream/history to catch a recent pass over your area.
4. Read the scene for wide-area context (weather, water, land cover, large disturbances).
5. Pivot: for archival, date-specific, or higher-resolution needs, move to Landsat/Sentinel archives (USGS EarthExplorer, Sentinel Hub) or commercial imagery.

## Inputs → Outputs
- **In:** a `geolocation` (region to watch)
- **Out:** near-real-time Landsat scene `image`s anchored to a `geolocation`
- **Empty/negative result looks like:** no fresh scene over your exact area right now is normal — a given point is only imaged every ~16 days, so absence of a live pass means "wait or use the archive," not "no data exists."

## Gotchas & OpSec
- **Resolution:** Landsat is ~15–30 m/pixel — good for landscapes and large features, useless for identifying vehicles or people.
- **Near-real-time, not historical:** it shows acquisition as it happens; for a specific past date use an imagery archive instead.
- Cloud cover frequently obscures scenes; a blank/white pass is weather, not a fault.

## Overlaps ("do both")
- Complements archival/high-res imagery tools (USGS EarthExplorer, Sentinel Hub, Google Earth) — Observer gives the freshest wide-area pass, and those give date-specific, higher-detail, or historical views.

## Trust & verifiability
`trust: trusted` — official Landsat data shown via Pinkmatter's FarEarth technology, the same platform the USGS uses for EarthNow; the imagery source is authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | observer |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation → image, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
