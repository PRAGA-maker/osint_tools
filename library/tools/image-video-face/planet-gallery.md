---
id: planet-gallery
name: Planet Gallery
description: Use when you have a `geolocation` and a notable event and want before/after satellite imagery of that place — returns curated Planet satellite `image`s of the location.
url: https://www.planet.com/latest-satellite-imagery-gallery/
category: image-video-face
path:
- image-video-face
bestFor: Browsing curated before/after satellite imagery of locations affected by fires, floods, conflict, and other events.
selectorsIn:
- geolocation
selectorsOut:
- image
status: live
pricing: freemium
costNote: The curated public gallery is free to browse; tasking/monitoring fresh imagery of an arbitrary location is a paid Planet service.
opsec: passive
opsecNote: You browse a public gallery of already-published imagery — no query is tied to a subject and nothing is signalled. It's an area/event tool, not a person lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Planet Labs operates its own satellite constellations; the imagery is first-party and authoritative for the scenes it publishes.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Planet Labs gallery
- Planet satellite imagery gallery
tags:
- satellite
- geolocation
- imagery
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- planet-labs
---

# Planet Gallery

> Planet Labs' curated public showcase of satellite imagery — before/after views of places hit by fires, floods, conflict, and other significant events.

## When to use
You have a `geolocation` tied to a datable event (a fire, flood, military action, construction, environmental change) and want overhead imagery to see the ground truth or the change over time. Good for corroborating that something happened at a place on/around a date, or for orienting a geolocation investigation with recent high-frequency overhead views. It shows *places and events*, not individuals — so it supports location/timeline work rather than identifying a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.planet.com/latest-satellite-imagery-gallery/.
2. Browse the curated entries; find the location/event matching your `geolocation` (the gallery is organised by notable events worldwide).
3. Use the before/after sliders to compare the scene across dates.
4. Read the output: dated satellite `image`s of the location and the change between captures.
5. Pivot: confirmed ground change/timeline feeds mapping and event-verification; for a location NOT in the curated gallery you'll need Planet's paid tasking or a free alternative.

## Inputs → Outputs
- **In:** `geolocation` + an event/date of interest
- **Out:** dated satellite `image`s and before/after comparisons of the area
- **Empty/negative result looks like:** your location/event isn't in the curated set — the free gallery only showcases selected scenes, so absence here doesn't mean no imagery exists (it may be paywalled behind tasking).

## Gotchas & OpSec
- The **free** offering is a *curated gallery*, not on-demand imagery of any coordinate — arbitrary-location, fresh imagery requires a paid Planet account/tasking.
- Coverage and dates are whatever Planet chose to feature; don't expect full historical depth for a specific spot.
- OpSec: fully passive — public published imagery.

## Overlaps ("do both")
- Pairs with free satellite/aerial sources (e.g. Sentinel Hub, Google Earth historical imagery): use those for arbitrary coordinates and history, and this gallery for Planet's high-frequency, event-curated scenes.

## Trust & verifiability
`trust: trusted` — Planet operates the satellites, so the imagery is authoritative first-party data. The caveat is coverage, not authenticity: the free gallery is a selective showcase, so treat gaps as "not published free", not "no data".

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | planet-gallery |
