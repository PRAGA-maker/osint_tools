---
id: globalfishingmap
name: GlobalFishingMap
description: Use when you have a `geolocation` or vessel and want maritime activity there — returns fishing effort, vessel tracks, and identities from Global Fishing Watch's AIS data.
url: https://globalfishingwatch.org/map/
category: geolocation
path:
- geolocation
bestFor: Mapping vessel activity and fishing effort in an ocean area, and tracking a specific vessel's AIS history globally.
selectorsIn:
- geolocation
- name
selectorsOut:
- geolocation
- name
status: live
pricing: freemium
costNote: Free interactive map and (with a free account) data downloads/API; no paid tier needed for core use.
opsec: passive
opsecNote: Reads public AIS broadcasts aggregated by Global Fishing Watch; the vessel/crew aren't notified. Passive. A free account is needed for downloads/API but only ties the download to your account, not to any target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Global Fishing Watch is a respected nonprofit (backed by Oceana, SkyTruth, Google) publishing AIS-derived vessel activity; data is authoritative for AIS-equipped vessels.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- global-fishing-watch
- marinetraffic
- vesselfinder
aliases:
- Global Fishing Watch
- globalfishingwatch.org
tags:
- Maps, Geolocation and Transport
- Nature
- vessel-tracking
- ais
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# GlobalFishingMap

> Global Fishing Watch's map — global vessel activity and fishing effort from AIS data, with per-vessel tracks going back years, all free.

## When to use
You need maritime activity for an ocean area or the movement history of a specific vessel. Where live trackers show *now*, Global Fishing Watch offers *historical* AIS-derived tracks and fishing-effort heatmaps worldwide. Relevant to a missing-persons case only when a subject is tied to a fishing/commercial vessel — reconstructing where a boat operated, when it was last active, or which vessels were in an area at a time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://globalfishingwatch.org/map/.
2. Search a vessel by name/MMSI, or navigate to an ocean area and click to read fishing-effort/activity at that point.
3. Open a vessel to see its AIS track over time, flag, gear type, and identity details.
4. Adjust the date range to reconstruct historical movements.
5. Create a free account to download data or use the API for bulk analysis.
6. Pivot: a vessel identity/MMSI → cross-check live position on `[[marinetraffic]]`/`[[vesselfinder]]`; a track's ports → harbour records and arrivals.

## Inputs → Outputs
- **In:** a `geolocation`/ocean area, or a vessel `name`/MMSI
- **Out:** fishing-effort/activity data, vessel AIS tracks, and vessel identity (`geolocation`, `name`)
- **Empty/negative result looks like:** no activity/track — the vessel had AIS off, is too small/non-commercial to broadcast, or is outside coverage; absence isn't proof of no presence.

## Gotchas & OpSec
- Only AIS-broadcasting vessels appear — small craft and boats that disable AIS are invisible.
- AIS can be spoofed or gapped ("going dark"); treat tracks as strong leads, not certainty.
- Great for commercial/fishing vessels specifically; not a general people-finder (hence low MP relevance).

## Overlaps ("do both")
- Pairs with `[[marinetraffic]]` and `[[vesselfinder]]` — those give current position and port calls; GFW gives long historical tracks and fishing behavior. Run the MMSI on all.

## Trust & verifiability
`trust: trusted` — a well-regarded nonprofit publishing AIS-derived data with transparent methodology. Vessel tracks are authoritative for AIS-equipped ships; verify identity via MMSI across other trackers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | globalfishingmap |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, name → geolocation, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
