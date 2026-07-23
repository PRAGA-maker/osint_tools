---
id: worldcam
name: WorldCam
description: Use when you have a `geolocation`/place and want live public webcams there to verify conditions or activity — returns live streams tied to a stated `address`/coordinates.
url: https://worldcam.eu/
category: geolocation
path:
- geolocation
bestFor: Browsing 30,000+ location-tagged live public webcams by country, city, or category.
selectorsIn:
- geolocation
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free to browse and watch; ad-supported. An optional free sign-up lets you add/broadcast cams but isn't needed to view.
opsec: passive
opsecNote: Passive viewing of public webcam feeds — you observe a place, not a person, and no target is contacted. Standard analytics apply; use a clean browser if the location matters operationally.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large community/commercial webcam directory embedding third-party public streams; individual camera locations and uptime are unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- webcamtaxi
- earthcam
- windy-webcams
aliases:
- World Cam
- worldcam.eu
tags:
- webcams
- live-streams
- geolocation
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# WorldCam

> A big directory of location-tagged live public webcams (30,000+) — use it to put real-time eyes on a place to confirm weather, daylight, crowds, or an event.

## When to use
You have a `geolocation` — a city, beach, airport, landmark — and want a live view to corroborate or challenge a claim: verify current conditions in a photo/video, confirm an event is happening, or check daylight/weather against a claimed timeline. WorldCam organises streams by continent → country → city and by category (beaches, airports, pools), plus sunlight and weather overlays.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://worldcam.eu/.
2. Browse by region or category, or search a place name.
3. Open a camera to watch the live stream; note the stated location/coordinates and any weather/sun overlay.
4. Compare the live view (light, weather, foliage, signage) against the media or claim you're testing.
5. Pivot: confirmed coordinates feed mapping/Street View; the same spot on another provider (`[[webcamtaxi]]`, `[[earthcam]]`, `[[windy-webcams]]`) corroborates it.

## Inputs → Outputs
- **In:** `geolocation` / place name
- **Out:** live webcam streams with a stated `address`/`geolocation`
- **Empty/negative result looks like:** no cameras for the area, or an offline/frozen stream — coverage is patchy and cams die; try another provider or a nearby camera.

## Gotchas & OpSec
- Stated locations are curator-supplied and sometimes wrong/approximate — verify the view against known landmarks before trusting the location.
- Streams freeze, loop, or go dark; check motion/timestamps to confirm it's genuinely live.
- OpSec: passive place-observation; no person is contacted or alerted.

## Overlaps ("do both")
- Pairs with `[[webcamtaxi]]`, `[[earthcam]]`, and `[[windy-webcams]]` — each aggregates different cameras, so a location absent on one often appears on another; Windy also ties cams to live weather.

## Trust & verifiability
`trust: community` — a curated directory of third-party public streams; the feeds are real but their stated locations and uptime are unverified, so corroborate any location-critical observation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | worldcam |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
