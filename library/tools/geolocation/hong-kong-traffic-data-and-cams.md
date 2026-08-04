---
id: hong-kong-traffic-data-and-cams
name: Hong Kong Traffic Data & Cams
description: Use when you have a `geolocation` in Hong Kong and want live roadside conditions — returns traffic-camera snapshots and congestion data on an interactive map dashboard.
url: https://www.arcgis.com/apps/dashboards/47be6372a0434beaba99ae9c9f1d598d
category: geolocation
path:
- geolocation
bestFor: Viewing Hong Kong public traffic cameras and congestion data by location.
selectorsIn:
- geolocation
selectorsOut:
- image
- geolocation
status: live
pricing: free
costNote: Free ArcGIS dashboard over public Hong Kong traffic feeds; no account to view.
opsec: passive
opsecNote: Passive — you view public traffic feeds; the subject is not contacted and no case data is submitted. The cameras are official/public, so viewing leaks nothing about your investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-built ArcGIS dashboard aggregating Hong Kong public traffic-camera and speed-map data; unofficial, so feed availability can change.
missingPersonsRelevance: low
coverage:
- hk
auth: none
api: false
localInstall: false
registration: false
aliases:
- HK traffic cameras dashboard
tags:
- traffic-cameras
- geolocation
- hong-kong
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# Hong Kong Traffic Data & Cams

> An ArcGIS dashboard plotting Hong Kong's public traffic cameras and congestion data on one map — near-real-time ground conditions by location.

## When to use
You have a `geolocation`/area in Hong Kong and want current roadside imagery or congestion context — to check conditions at a junction, confirm what a road looks like, or see whether a location is camera-covered. The cameras are wide traffic views for placing a *scene*, not identifying an individual or a plate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the dashboard: https://www.arcgis.com/apps/dashboards/47be6372a0434beaba99ae9c9f1d598d.
2. Pan/zoom to the Hong Kong area of interest, or use the dashboard selectors.
3. Click a camera marker to view its latest public snapshot; read the congestion/speed-map layer for flow context.
4. Note timestamps — snapshots refresh periodically, so treat them as "recent," not live video.
5. Pivot: use a confirmed camera location to ground-truth a road/junction, then corroborate with satellite/street imagery.

## Inputs → Outputs
- **In:** `geolocation` (a Hong Kong location/area)
- **Out:** `image` (traffic-cam snapshots) tied to a `geolocation`, plus congestion data
- **Empty/negative result looks like:** no camera near the point, or a stale/blank snapshot — meaning no coverage or a temporarily down feed, not that the road is clear.

## Gotchas & OpSec
- Hong Kong-only; anywhere else returns nothing.
- Snapshots are low-resolution wide shots that refresh on an interval — not usable to identify people or vehicles.
- Being an unofficial ArcGIS dashboard, its feed set/availability can change without notice.

## Overlaps ("do both")
- Same pattern as other regional traffic-cam tools (e.g. `[[toronto-area-live-traffic-cams]]`) — pick the one covering your region; both pair with satellite/street-view for the fixed layout.

## Trust & verifiability
`trust: community` — an unofficial aggregator of public feeds; the underlying camera data is government-sourced, but freshness and availability depend on this third-party dashboard.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hong-kong-traffic-data-and-cams |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
