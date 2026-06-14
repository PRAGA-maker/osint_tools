---
id: corona
name: Corona
description: Use when you need declassified 1960s–70s CORONA spy-satellite imagery of a location for historical landscape analysis — returns georeferenced Cold War-era imagery, not current data.
url: https://corona.cast.uark.edu/
category: geolocation
path:
- geolocation
bestFor: Viewing/downloading georeferenced declassified CORONA satellite imagery for historical terrain analysis.
selectorsIn:
- geolocation
- address
selectorsOut:
- image
- geolocation
status: live
pricing: free
costNote: Free academic atlas (University of Arkansas CAST); registration may be needed to download imagery.
opsec: passive
opsecNote: Public historical imagery archive; querying it touches only the university's server and reveals nothing about any present-day target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: CORONA Atlas is hosted by the University of Arkansas Center for Advanced Spatial Technologies (CAST) — a credible academic source. Imagery is from declassified U.S. reconnaissance programs.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- CORONA Atlas
- CAST CORONA
tags:
- geospatial-research-and-mapping-tools
- historical-imagery
- satellite
source: arf-seed
lastVerified: ''
enrichment: full
---

# Corona

> The CORONA Atlas (University of Arkansas CAST): a georeferenced archive of declassified Cold War–era (circa 1960–1972) CORONA spy-satellite imagery, used mainly for historical landscape and archaeology research.

## When to use
Niche for missing persons. Reach for it only when a case genuinely turns on what a location looked like *decades ago* — e.g. understanding former terrain, structures, or roads at a `geolocation`/`address` that no longer appear on modern maps. For any current missing-persons need (recent imagery, present-day search areas) this is the wrong tool; use current/recent satellite and street imagery instead. Filed under geolocation, but its temporal scope makes day-to-day MP relevance **low**.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://corona.cast.uark.edu/ and use the map interface to navigate to your area of interest (`geolocation` or `address`).
2. Browse available CORONA frames covering that location; the atlas is georeferenced so frames overlay modern coordinates.
3. Register/log in if required to download full-resolution imagery.
4. Read the historical `image` and its acquisition date. Pivot: compare against modern imagery to identify long-vanished features.

## Inputs → Outputs
- **In:** `geolocation` / `address` (an area of interest)
- **Out:** `image` (declassified historical satellite frames) + `geolocation` (frame footprint/date)
- **Empty/negative result looks like:** no CORONA frames cover the queried area, or only low-resolution/cloud-obscured frames exist — coverage is uneven and decades-old.

## Gotchas & OpSec
- Imagery is **historical** (1960s–70s) — it will not show anything about a present-day subject, vehicle, or recent activity.
- Coverage is patchy and resolution is coarse by modern standards; many areas have few or no usable frames.
- Download may require a (free) account.
- OpSec: passive — a public academic archive; your subject learns nothing.

## Overlaps ("do both")
- Complements modern imagery sources (Google Earth historical layer, Sentinel/Landsat) only for the rare case where you need pre-1980 terrain context.

## Trust & verifiability
`trust: community` — a credible university-run archive of genuine declassified U.S. reconnaissance imagery. Trustworthy as a historical source; simply not aimed at current-day person-finding.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | corona |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
