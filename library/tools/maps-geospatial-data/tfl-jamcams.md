---
id: tfl-jamcams
name: TfL JamCams
description: Use when you have a London `geolocation` or `address` and want near-live traffic-camera stills plus incidents at that spot — returns geolocation and image observations.
url: https://www.tfljamcams.net
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Checking near-real-time TfL traffic-camera images and live road incidents at a specific London junction, bridge, or road.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free and ad-free; installable as a PWA. Runs on TfL's free Open Data API — no account or payment needed.
opsec: passive
opsecNote: You are viewing public traffic-camera stills; nothing touches the target and no login is required, so this is fully passive. Note the cameras are TfL's own public feed — you are only observing a public place, not surveilling an individual.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party map (built by Jason Brooks, not affiliated with TfL) that surfaces TfL's official Open Data camera feed; the underlying images are authoritative TfL data, the map wrapper is community-made.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- tfljamcams.net
- London JamCams map
tags:
- Maps, Geolocation and Transport
- live-cameras
- london
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# TfL JamCams

> A live map of London's 900+ TfL traffic cameras (plus road incidents and transit departures) — a near-real-time public-camera view of any major London junction, refreshed every few minutes from TfL Open Data.

## When to use
You have a London `geolocation` or `address` — a "last seen" spot, a route a subject or vehicle would take, a junction near an address — and you want to see what a public traffic camera there is showing, or check current road incidents. The cameras update every 2–5 minutes (still images, not continuous video) across all 33 boroughs, so they suit spotting congestion, road closures, or activity at a fixed public point, not tracking an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tfljamcams.net (works in-browser or installable as a PWA).
2. Pan/zoom the map to the target London `geolocation`/`address`, or search the area.
3. Click a nearby camera marker to view its latest still image; note the refresh cadence (2–5 min) and check the live-incidents layer for closures/accidents.
4. Cross-reference the camera's exact position and viewing angle with a base map to understand what stretch of road it covers.
5. Pivot: a confirmed `geolocation` and any `image` observation (a vehicle type, a closure, crowd) feed timeline reconstruction and other mapping/camera tools; incidents corroborate why a route was blocked at a time.

## Inputs → Outputs
- **In:** London `geolocation` or `address` (map area)
- **Out:** `geolocation` (precise camera positions) and `image` (latest camera stills), plus live road-incident data
- **Empty/negative result looks like:** no camera near the point (coverage is TfL's road network, not residential streets), or a stale/blank image — the camera may be offline. Absence of a nearby camera is common; London side-streets are not covered.

## Gotchas & OpSec
- Stills, not live video, refreshed every few minutes — you cannot follow motion, only sample a public scene.
- Coverage is TfL's managed road network (junctions, bridges, tunnels, major roads); most residential and non-TfL roads have no camera.
- Low resolution and traffic-oriented framing — good for road state and vehicle-type-level detail, not for identifying a face or plate.
- Third-party site; if it is down or rate-limited, the same feed is reachable via TfL's Open Data API / the London Datastore.

## Overlaps ("do both")
- Pairs with a general mapping/geolocation tool and other public-webcam directories — JamCams give the live TfL road view, a base map gives the surrounding street context and non-TfL cameras fill the gaps.

## Trust & verifiability
`trust: community` — the map is an independent project, but the camera images and incident data come straight from TfL's official Open Data feed, so the underlying observations are authoritative and verifiable against TfL's own API.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tfl-jamcams |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
