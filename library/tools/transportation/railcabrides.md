---
id: railcabrides
name: Railcabrides
description: Use when you have a rough `geolocation` on or near a railway line and want ground-level video to confirm it — returns cab-view footage as `geolocation` verification.
url: https://railcabrides.com/en/mapsearch
category: transportation
path:
- transportation
bestFor: Ground-truthing a location along a rail line where Street View / Mapillary have no coverage.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to browse the map and watch the linked cab-ride videos; no account required.
opsec: passive
opsecNote: You browse a third-party map and watch YouTube-hosted videos; the target is not contacted and nothing about your query reaches them. Standard sock-puppet browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-built aggregator that maps user-submitted rail cab-ride videos onto the world railway network; coverage depends entirely on whether someone has filmed that line.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- openrailwaymap-2
- mapillary
- kartaview
- googlestreetview
aliases:
- Rail Cab Rides
- railcabrides.com map search
tags:
- Maps, Geolocation and Transport
- Railway
- geolocation-verification
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Railcabrides

> A world map of driver's-eye rail cab-ride videos — ground-level footage for the many places Street View never reached.

## When to use
You have a candidate `geolocation` that sits on or beside a railway line — a photo you are geolocating shows tracks, a station, a level crossing, a trackside building, or terrain a train would pass — and there is no Street View, Mapillary, or KartaView imagery to confirm it. If a cab-ride video exists for that stretch of line, you can watch the exact scene roll past and match landmarks (station names, signals, bridges, mountain profiles) to your candidate point.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://railcabrides.com/en/mapsearch.
2. Find your area on the world map. Railway lines that have at least one cab-ride video are drawn in **orange or red**; click a point on a coloured line.
3. A list of cab-ride videos covering that segment appears — open one and scrub to the timestamp where the train passes your candidate location.
4. Compare fixed features (station signage, platform layout, catenary/pole style, adjacent buildings, hills) between the video frame and your source image to confirm or rule out the location.
5. Pivot: once confirmed, feed the coordinate into `[[openrailwaymap-2]]` for line/station metadata, or cross-check the surrounding area with `[[mapillary]]` / `[[kartaview]]`.

## Inputs → Outputs
- **In:** `geolocation` (a point/segment on a rail line)
- **Out:** `geolocation` confirmation — cab-view video letting you visually match the scene
- **Empty/negative result looks like:** the line at your point is grey (no video), or the click returns no videos. That means no one has filmed that segment — absence of footage, not evidence the location is wrong.

## Gotchas & OpSec
- Coverage is crowd-sourced and heavily skewed toward Europe and enthusiast-filmed lines; large regions have no footage at all.
- Videos are timestamped along a whole journey — you may need to scrub a long ride to reach your segment.
- OpSec: fully passive. You only touch railcabrides.com and the video host; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with `[[openrailwaymap-2]]` — that gives you the rail network's structure and station names, while this gives you the actual ground-level view. Use `[[mapillary]]`, `[[kartaview]]`, and `[[googlestreetview]]` for the road-side angles the rail footage can't show.

## Trust & verifiability
`trust: community` — it is a volunteer aggregator of user-submitted footage, so the map is only as complete as its contributors; the videos themselves are primary evidence you verify frame-by-frame.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | railcabrides |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
