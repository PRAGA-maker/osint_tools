---
id: hawaii-traffic-cameras
name: Hawaii Traffic Cameras
description: Use when you have a `geolocation` in Hawaii and want live public traffic-camera views and road conditions to confirm real-time activity at a location — returns image and geolocation confirmation.
url: http://goakamai.org/home
category: geolocation
path:
- geolocation
bestFor: Live Hawaii DOT traffic cameras and road/incident conditions across Oahu, Maui, Kauai, and Hawaii Island.
selectorsIn:
- geolocation
selectorsOut:
- image
- geolocation
status: live
pricing: free
costNote: Free public service operated for the Hawaii Department of Transportation; no account required.
opsec: passive
opsecNote: Fully passive — you are viewing a public government traffic-camera portal. Nothing you do reaches or reveals your target. Cameras are low-resolution road overviews, not identifying surveillance, so treat any "sighting" as corroboration, not proof.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official GoAkamai traffic portal for the Hawaii DOT; camera feeds and incident data are first-party government sources.
missingPersonsRelevance: low
coverage:
- us
aliases:
- GoAkamai
- Hawaii DOT traffic
tags:
- traffic-cameras
- hawaii
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
---

# Hawaii Traffic Cameras

> Hawaii DOT's public GoAkamai portal — live traffic cameras, road conditions and incident reports across the main Hawaiian islands.

## When to use
You have a `geolocation` in Hawaii (a highway, intersection, or corridor on Oahu, Maui, Kauai, or Hawaii Island) and want to see current conditions there — traffic flow, weather on the road, an active incident, or simply confirm a route is passable at this moment. Useful for corroborating that a location is real and accessible, timing patterns of activity on a route, or situational awareness during a time-sensitive search. Cameras are wide road views, so they establish conditions, not identities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://goakamai.org/home.
2. Use the island tabs / map to navigate to your area of interest.
3. Click a camera icon to view its live still/refresh feed; check the incidents and road-conditions layers for events near your location.
4. Note the camera location and timestamp for your record.
5. Pivot: confirmed road conditions/incidents → correlate with a subject's known route/timeline; a camera location → map it precisely for a search grid.

## Inputs → Outputs
- **In:** a Hawaii `geolocation` (road/corridor/island)
- **Out:** live camera `image`/refresh feed, road-condition and incident data confirming `geolocation`
- **Empty/negative result looks like:** a camera marked offline/"no image", or no cameras in that area — coverage is limited to state highways, so rural/side-road locations often have none.

## Gotchas & OpSec
- Coverage is state-highway-focused; many locations have no camera.
- OpSec: fully passive public government portal — zero exposure.
- Feeds are periodic stills, low resolution, and not archived here — capture what you need when you see it.

## Overlaps ("do both")
- Complements other live-camera/geolocation resources; use alongside general traffic-cam aggregators when your area of interest spans beyond Hawaii state highways.

## Trust & verifiability
`trust: trusted` — official Hawaii DOT traffic portal; camera and incident feeds are first-party government data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hawaii-traffic-cameras |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → image, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
