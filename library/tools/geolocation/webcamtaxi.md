---
id: webcamtaxi
name: Webcamtaxi
description: Use when you have a `geolocation`/place and want live public webcams there to confirm current conditions, weather, or activity — returns live streams tied to `address`/coordinates.
url: https://www.webcamtaxi.com/en/
category: geolocation
path:
- geolocation
bestFor: Finding curated live public webcams for a specific city, landmark, or region.
selectorsIn:
- geolocation
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free to browse and watch; the site is ad-supported and embeds publicly available webcam streams.
opsec: passive
opsecNote: Passive viewing of public webcam feeds — you observe a place, not a person, and no target is contacted. The site logs standard analytics; use a clean browser if the location matters operationally.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community/commercial webcam directory embedding third-party public streams; individual cameras' locations and uptime are unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- earthcam
- windy-webcams
- insecam
aliases:
- Webcam Taxi
- webcamtaxi.com
tags:
- webcams
- live-streams
- geolocation
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Webcamtaxi

> A curated directory of live public webcams by location — use it to put eyes on a place in real time to confirm weather, daylight, crowds, or events.

## When to use
You have a `geolocation` — a city, landmark, beach, ski resort, port — and want a live view of it: to verify current conditions in a photo/video, corroborate that an event is happening, cross-check weather/daylight against a claimed timeline, or scout an area before or during fieldwork. Webcamtaxi organises publicly available streams by country and place so you can jump straight to the relevant camera.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.webcamtaxi.com/en/.
2. Browse by continent → country → region/city, or use the site search for a place name.
3. Open a camera to watch the live stream; note the stated location and, where given, the exact spot/coordinates.
4. Compare the live view (weather, light, foliage, signage) against the media or claim you're testing.
5. Pivot: confirmed coordinates feed mapping/Street View; the same landmark on another provider (`[[earthcam]]`, `[[windy-webcams]]`) corroborates the view.

## Inputs → Outputs
- **In:** `geolocation` / place name
- **Out:** live webcam streams with a stated `address`/`geolocation`
- **Empty/negative result looks like:** no cameras listed for the area, or a stream that's offline/frozen — coverage is patchy and cams die; try another provider or a nearby camera.

## Gotchas & OpSec
- Stated camera locations are curator-supplied and occasionally wrong or approximate — verify the view against known landmarks before trusting the location.
- Streams go offline, freeze, or loop; check the timestamp/motion to confirm it's genuinely live.
- OpSec: passive place-observation; no person is contacted or alerted.

## Overlaps ("do both")
- Pairs with `[[earthcam]]`, `[[windy-webcams]]`, and `[[insecam]]` — each aggregates different cameras, so a location absent on one often appears on another; Windy also ties cams to live weather.

## Trust & verifiability
`trust: community` — a curated directory of third-party public streams; the feeds are real but their stated locations and uptime are unverified, so corroborate any location-critical observation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webcamtaxi |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
