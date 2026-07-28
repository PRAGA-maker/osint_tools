---
id: orbtrack
name: OrbTrack
description: Use when you have a `geolocation` and a time and want to know which satellites were overhead — returns satellite pass predictions to reason about possible imagery of a location/event.
url: https://www.orbtrack.org
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Predicting which satellites pass over a given location and when, up to five days ahead.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web tool; uses public orbital data (TLEs) from CelesTrak.
opsec: passive
opsecNote: Fully passive — you compute passes from public orbital elements; nothing about your query reaches any third party of investigative interest. No login.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Hobbyist/educational tracker built on standard CelesTrak TLE data and SGP4 propagation; predictions are physics-based and reliable within TLE accuracy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- orbtrack.org
- OrbTrack satellite tracker
tags:
- maps-and-geospatial
source: metaosint
lastVerified: '2026-07-28'
enrichment: full
---

# OrbTrack

> A free web tracker that predicts the positions and passes of 10,000+ orbiting satellites relative to a location you pick — useful for reasoning about when a place could have been imaged from space.

## When to use
You have a `geolocation` and a time window (past or up to ~5 days ahead) and want to know which satellites were/will be overhead. In OSINT this helps you reason about whether commercial/earth-observation satellites could have captured an event or location, or to interpret a photo of the sky, or simply to track the ISS. It's a supporting geospatial tool, not a person-finder — relevance to missing-persons work is indirect.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.orbtrack.org.
2. Set the observer `geolocation` — click the map or enter latitude/longitude.
3. Browse predicted satellite positions/passes for your location, out to five days.
4. Note which imaging satellites pass over at the time of interest as a lead for seeking imagery.
5. Pivot: use pass windows to prioritize which satellite-imagery archives/providers to check for a given place and date.

## Inputs → Outputs
- **In:** `geolocation` (observer lat/long)
- **Out:** `geolocation` (satellite positions/passes over that point, with times)
- **Empty/negative result looks like:** a time window with no notable imaging-satellite passes — meaning space imagery of that spot at that moment is unlikely from the tracked constellation.

## Gotchas & OpSec
- Predictions are only as accurate as the public TLE data (fine for days ahead, degrading further out); re-check close to the time.
- "A satellite passed over" does NOT mean it imaged the spot — sensor tasking, swath, and weather all matter; treat passes as necessary-not-sufficient.
- Passive and anonymous — pure computation on public data.

## Overlaps ("do both")
- Pairs with satellite-imagery archives (Sentinel Hub, Planet, etc.) and other trackers like Heavens-Above — OrbTrack tells you *when* something was overhead; the imagery providers tell you *what* was actually captured.

## Trust & verifiability
`trust: community` — a hobbyist tracker built on standard CelesTrak orbital data and well-established propagation math; the physics is sound, so predictions are reliable within the accuracy of the input TLEs.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | orbtrack |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
