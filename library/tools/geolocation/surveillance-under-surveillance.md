---
id: surveillance-under-surveillance
name: Surveillance under Surveillance
description: Use when you have a `geolocation`/`address` and want to know what cameras watch it — returns mapped CCTV, ALPRs, and guards with type and field of view.
url: https://sunders.uber.space/
category: geolocation
path:
- geolocation
bestFor: Mapping surveillance cameras, license-plate readers, and guards at a location using crowdsourced OpenStreetMap data.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open — data comes from OpenStreetMap contributors; no login to browse (an OSM account is needed only to add/edit entries).
opsec: passive
opsecNote: Passive — you're reading a public map layer, contacting no one at the location. It also offers a Tor onion service if you want to browse without exposing your IP. Remember the data is volunteer-contributed and incomplete: absence of a camera on the map is not proof there is none.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdsourced from OpenStreetMap using standardised surveillance tags; coverage is uneven and only as current/accurate as local contributors made it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- kakao-map
aliases:
- SunderS
- sunders
tags:
- surveillance
- cctv
- openstreetmap
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Surveillance under Surveillance

> A crowdsourced OpenStreetMap layer that maps who's watching a place — fixed/dome/panning cameras, automatic licence-plate readers, and guards — with icons for type, coverage area, and field of view.

## When to use
You have a `geolocation` or `address` — a last-known location, a route a subject may have taken, a spot in a photo you're geolocating — and you want to know what surveillance exists nearby. In missing-person work this matters two ways: it tells you where footage might exist to request (which cameras could have captured someone), and it helps reconstruct or corroborate a route. Colour coding distinguishes public-outdoor, private-outdoor, and indoor coverage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sunders.uber.space/ (or its onion service for anonymity).
2. Navigate/zoom the map to your `geolocation`/`address` of interest.
3. Read the markers: icon = camera type (fixed, dome, panning), ALPR, or guard; colour = public outdoor (red), private outdoor (blue), indoor (green).
4. Click a marker for details where tagged: mounting, direction/angle, observation area, height, operator, and reference number.
5. Pivot: identified cameras become footage-request leads (note operator/reference); the coverage geometry helps confirm whether a spot was likely captured.

## Inputs → Outputs
- **In:** `geolocation` or `address`
- **Out:** mapped surveillance points near that location with type, field of view, and (when tagged) operator — a `geolocation`-anchored result
- **Empty/negative result looks like:** a blank area on the map — almost always means no contributor has tagged that place, NOT that the area is camera-free; verify on the ground or with imagery.

## Gotchas & OpSec
- Coverage is patchy and volunteer-maintained: dense in some cities, empty elsewhere; treat it as leads, not a complete inventory.
- Tags can be outdated (cameras added/removed since mapping); confirm before relying on a specific camera.
- Passive and safe to browse; the onion service avoids exposing your IP.

## Overlaps ("do both")
- Pair with a full-imagery map like `[[kakao-map]]` (or Google/Yandex Street View for other regions) — cross-check the mapped camera against actual street-level imagery of the spot.

## Trust & verifiability
`trust: community` — sourced from OpenStreetMap's open, auditable data; every point links back to OSM where you can inspect the tags and edit history, but completeness is not guaranteed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | surveillance-under-surveillance |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
