---
id: radar-interference-tracker-rit
name: Radar Interference Tracker (RIT)
description: Use when you have a `geolocation`/`address` and want to detect active military radar near it — returns the coordinates of radar systems from Sentinel-1 interference streaks.
url: https://ollielballinger.users.earthengine.app/view/bellingcat-radar-interference-tracker
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Pinpointing active ground/air-defense radar installations from the interference they leave in Sentinel-1 satellite radar imagery.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free Google Earth Engine web app from Bellingcat; no account or payment required to view.
opsec: passive
opsecNote: You browse pre-processed satellite imagery in a public Earth Engine app; nothing is sent to any subject or installation. Standard clean-browser hygiene is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by Ollie Ballinger and published through Bellingcat; the underlying Sentinel-1 SAR data is from ESA/Copernicus and the method is documented, so results are reproducible.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- RIT
- Bellingcat Radar Interference Tracker
tags:
- bellingcat-toolkit
- satellite-imagery
- sar
- conflict-monitoring
source: bellingcat-toolkit
lastVerified: '2026-08-04'
enrichment: full
---

# Radar Interference Tracker (RIT)

> Bellingcat's Earth Engine app that reads the bright interference streaks active radar leaves in Sentinel-1 satellite imagery — a way to locate operational military radar and air-defense systems from space.

## When to use
You are doing conflict, military-site or infrastructure geolocation and want to know whether an active radar is operating at or near a `geolocation`/`address`. Ground- and ship-based radars emit in the same band as the Sentinel-1 SAR satellite, producing distinctive coloured streaks across the radar image that point back to the emitter — RIT surfaces these so you can pin the radar's location and see how activity changes over time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the app URL (it loads a global Sentinel-1 composite in Google Earth Engine).
2. Navigate to your area of interest by panning/zooming or entering coordinates.
3. Look for the characteristic radar-interference streaks (rainbow/coloured lines); trace a streak to its origin to locate the emitting radar.
4. Use the date/layer controls to compare passes and judge whether a radar was active on a given period.
5. Pivot: take the derived `geolocation` into optical satellite imagery and mapping tools to identify the installation and corroborate the find.

## Inputs → Outputs
- **In:** `geolocation` / `address` (area to inspect)
- **Out:** `geolocation` of active radar emitters, plus a rough activity timeline across satellite passes
- **Empty/negative result looks like:** no streaks in the area — meaning no radar detected in that band during available passes, not proof no radar exists (it may have been off, or out of the satellite's swath).

## Gotchas & OpSec
- Human-in-the-loop: none; it is a view-only Earth Engine app (may be slow to load large areas).
- OpSec: passive — you only view pre-processed public imagery; there is no interaction with any site or subject.
- Interpretation: streaks only appear when the radar was emitting during a Sentinel-1 pass, so absence is inconclusive; confirm the emitter against optical imagery before reporting.

## Overlaps ("do both")
- Pairs with optical satellite/mapping tools because RIT tells you *where* an active radar is but not *what* it is; optical imagery identifies the installation the streak points to.

## Trust & verifiability
`trust: trusted` — an open, documented Bellingcat method over ESA Sentinel-1 data; anyone can reproduce a detection from the same public imagery, so findings are verifiable rather than proprietary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
