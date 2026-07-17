---
id: keyhole-engelsjk
name: keyhole engelsjk
description: Use when you have a `geolocation` and want to see how it looked in declassified 1960–1984 US spy-satellite imagery — returns historical KH/CORONA satellite photos for that area.
url: https://keyhole.engelsjk.com/
category: image-video-face
path:
- image-video-face
bestFor: Viewing declassified Cold War spy-satellite imagery of a location for historical geospatial context.
selectorsIn:
- geolocation
selectorsOut:
- image
status: live
pricing: freemium
costNote: Free experimental web visualization over publicly declassified USGS/CORONA imagery; no account required.
opsec: passive
opsecNote: You browse historical imagery; no target is contacted. Fully passive. Use a VPN only for general hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A hobby visualization over genuinely declassified US government (KH/CORONA) imagery; the imagery is authoritative, the viewer is an experimental third-party front-end.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- keyhole
- CORONA satellite viewer
- keyhole.engelsjk.com
tags:
- Maps, Geolocation and Transport
- Satellite/aerial imagery
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# keyhole engelsjk

> An experimental map viewer over 1.3M+ declassified US spy-satellite (KEYHOLE/CORONA) images from 1960–1984 — a way to see what a place looked like decades before commercial satellite imagery existed.

## When to use
You have a `geolocation` and need **historical** overhead context that predates Google Earth's timeline: what stood on a site in the 1960s–80s, whether a building/road/feature existed at a certain era, how a landscape has changed. This is a niche historical-geospatial and analysis tool — useful for cold cases, land/property history, and verifying claims about a location's past — not for finding a living person, hence low direct relevance but real value for deep location work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://keyhole.engelsjk.com/ and navigate the map to your `geolocation` of interest.
2. Browse the available declassified satellite frames covering that area and era.
3. Inspect the imagery for features present/absent at the time (structures, roads, land use) and compare against modern imagery.
4. For rigorous work, cross-reference the underlying frames on the USGS EarthExplorer archive (the authoritative source of the declassified imagery).
5. Pivot: a confirmed historical feature supports/undermines a timeline; changes over eras feed broader location analysis.

## Inputs → Outputs
- **In:** a `geolocation` / area to inspect
- **Out:** historical declassified satellite `image`s of that area (1960–1984)
- **Empty/negative result looks like:** no frames covering your exact spot/era — the CORONA program didn't image everywhere uniformly. Fall back to USGS EarthExplorer or other historical imagery for that area.

## Gotchas & OpSec
- **Historical only** (1960–1984) and coverage is uneven; resolution and clarity vary by frame. It won't show anything recent.
- It's an experimental third-party viewer — for citable work, verify frames against the official USGS declassified-imagery archive.
- OpSec: **passive** — browsing archived imagery; no target contact.

## Overlaps ("do both")
- Pairs with USGS EarthExplorer (the authoritative declassified-imagery source) and modern historical-imagery tools (Google Earth timeline) — this viewer is a convenient entry point; the archives are the record.

## Trust & verifiability
`trust: community` — an experimental hobby front-end, but it displays genuinely declassified US government imagery; confirm specific frames against the official USGS archive when a finding matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | keyhole-engelsjk |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation → image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
