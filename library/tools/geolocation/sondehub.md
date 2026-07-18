---
id: sondehub
name: SondeHub
description: Use when you have a radiosonde/amateur-balloon serial or a `geolocation` and want live telemetry and predicted landing points — returns `geolocation` tracks, receiver stations, and chase-car positions.
url: https://sondehub.org/
category: geolocation
path:
- geolocation
bestFor: Real-time tracking and landing prediction of weather radiosondes and amateur high-altitude balloons.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Completely free, no login. Optional Patreon/PayPal donations support the project.
opsec: passive
opsecNote: Purely a read/observe map of crowdsourced telemetry — you query SondeHub's database, not any person. No target is notified. The only attribution risk is your own IP hitting the site; use a VPN if the collection itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source community project fed by a global network of volunteer ground-station receivers; telemetry is only as complete as nearby receiver coverage. A homepage banner sometimes flags the version as out of date.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- SondeHub Tracker
- sondehub.org
- SondeHub-Amateur
tags:
- Maps, Geolocation and Transport
- radiosonde
- balloon-tracking
- rf-signals
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# SondeHub

> A live world map of weather radiosondes and amateur high-altitude balloons, built for recovering the payloads after they land.

## When to use
Niche geospatial/RF case work: you have a `geolocation` (an area of interest) or a specific radiosonde/balloon serial and want to see the object's live position, flight path, and predicted landing point. Relevant when an OSINT question involves a launched sonde or amateur balloon — decoding an RF signal in a photo, corroborating a "found a weather balloon" report, or locating downed payload hardware. Not a people-search tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sondehub.org/ (weather radiosondes) or the SondeHub-Amateur tracker for hobby balloons.
2. Zoom the map to your `geolocation` of interest — it renders realtime data when zoomed in.
3. Click an active sonde to read its telemetry: altitude, coordinates, frequency, manufacturer, sonde type, and predicted landing point.
4. Cross-reference receiver-station markers and chase-car positions to see who is already tracking/recovering it, and check recovery reports for found hardware.
5. Pivot: a landing prediction gives a `geolocation` to search on satellite/ground imagery; a frequency/manufacturer detail helps identify hardware seen in a photo.

## Inputs → Outputs
- **In:** `geolocation` (area) or a sonde serial
- **Out:** `geolocation` (live position + flight path + predicted landing), telemetry (altitude, frequency, type, manufacturer), receiver-station and chase-car locations
- **Empty/negative result looks like:** no sondes on the map in your area/timeframe — usually means no active launch nearby or no volunteer receiver coverage there, not that nothing flew.

## Gotchas & OpSec
- Coverage is crowdsourced: sondes only appear where volunteer receivers hear them, so gaps are receiver gaps, not proof of absence.
- Landing points are predictions and drift with wind data — treat as a search area, not an exact point.
- The "out of date version" banner is cosmetic; the live data still loads.

## Overlaps ("do both")
- Complements general mapping/geolocation tools in the [[geolocation]] set — SondeHub supplies the moving-object telemetry, while a base map or imagery tool supplies the ground context for the predicted landing zone.

## Trust & verifiability
`trust: community` — an open-source project run by the radiosonde-hunting community. Telemetry is authoritative where received but sparse where receivers are absent; verify any recovery claim against the on-site recovery reports.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sondehub |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
