---
id: global-forest-watch
name: Global Forest Watch
description: Use when you have a `geolocation`/`address` and want land-cover, deforestation and fire-alert history there — returns dated forest-change and fire data for the spot.
url: https://www.globalforestwatch.org/map/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Checking tree-cover change, recent deforestation and satellite fire alerts at a location to corroborate or date imagery.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and public (World Resources Institute); no account needed to explore the map. A free login only adds saving/subscriptions and custom-area alerts.
opsec: passive
opsecNote: Read-only exploration of satellite-derived public datasets — you query a location, not a person, and nothing reaches any subject. If you subscribe to area alerts you create an account tied to your queries; browse without logging in for a zero-attribution footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the World Resources Institute using established satellite datasets (Hansen/UMD tree cover, NASA FIRMS fire alerts, GLAD deforestation); authoritative, citable environmental data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- merlin
aliases:
- GFW
- globalforestwatch.org
tags:
- bellingcat-toolkit
- environment-wildlife
- geolocation
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# Global Forest Watch

> A free WRI map of the world's forests over time — tree-cover loss/gain, deforestation and satellite fire alerts — usable in imagery forensics to date and locate scenes by land-cover change.

## When to use
You have a `geolocation`/`address` and want to know its environmental history: has forest here been cleared, and when? Were there fire alerts on a given date? Two OSINT uses stand out — (1) **chronolocation**: match visible clearing/burn scars in an image to GFW's dated change data to bracket when a photo was taken; (2) **corroboration**: verify a claim about deforestation, illegal logging, land use, or a wildfire at a specific place and time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.globalforestwatch.org/map/.
2. Search or navigate to the target coordinates/`address`.
3. Enable relevant layers: Tree Cover Loss (by year), Tree Cover Gain, GLAD/integrated deforestation alerts, and VIIRS/MODIS fire alerts (with date filters).
4. Read the timeline: which years show loss at this pixel, and whether fire alerts coincide with your date of interest.
5. Cross-reference with satellite basemap imagery and other terrain cues to confirm the scene and its date.

## Inputs → Outputs
- **In:** `geolocation` / `address` (and optionally a date window)
- **Out:** dated tree-cover-change and fire-alert history at that `geolocation`
- **Empty/negative result looks like:** no loss/gain or fire alerts for the area — either genuinely stable land or outside the datasets' resolution/coverage; absence isn't proof nothing happened.

## Gotchas & OpSec
- Passive; no subject contact. Skip login unless you need saved custom-area alerts.
- Data has spatial (≈30 m) and temporal resolution limits and alert latency — treat dates as brackets, not exact timestamps.
- "Tree cover" ≠ forest (includes plantations); read layer definitions before drawing conclusions.

## Overlaps ("do both")
- Pairs with `[[merlin]]` (species→range) and general satellite-imagery/terrain tools — GFW supplies the dated land-cover change that anchors a chronolocation those tools help place.

## Trust & verifiability
`trust: trusted` — WRI-run and built on peer-reviewed satellite datasets (Hansen/UMD, NASA FIRMS, GLAD); authoritative and citable, within its documented resolution and latency limits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-forest-watch |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
