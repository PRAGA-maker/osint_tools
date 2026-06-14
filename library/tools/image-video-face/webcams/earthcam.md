---
id: earthcam
name: EarthCam
description: Use when you have a known location and want a live/archived public webcam view of it — returns geolocation-anchored video/imagery for that place.
url: https://www.earthcam.com/
category: image-video-face
path:
- image-video-face
- webcams
bestFor: Browse a global directory of live public webcams to observe a specific place in real time.
input: ''
output: ''
selectorsIn: [geolocation, address]
selectorsOut: [image, geolocation]
status: live
pricing: freemium
costNote: Public webcam viewing is free; some HD streams, archives, and "Hall of Fame" features sit behind EarthCam's premium/registration tiers.
opsec: passive
opsecNote: You watch a public camera feed; the subject cannot detect your viewing. You only learn what falls in the camera's fixed field of view.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established commercial webcam network; feeds are legitimate but coverage is limited to tourist/landmark/commercial sites it operates or aggregates.
missingPersonsRelevance: high
coverage: [us, global]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: [webcam, livestream, geolocation]
source: arf-seed
lastVerified: ''
enrichment: full
---

# EarthCam

> A directory of live (and archived) public webcams worldwide — useful for putting eyes on a known place without being there.

## When to use
You have a `geolocation` or `address` and there's an EarthCam-covered camera nearby (tourist landmark, city square, beach, transit hub) — you want a live/recent view of who or what is at that spot, or to establish current conditions/time-of-day at a sighting location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site and search/browse by city, landmark, or category.
2. Open the relevant cam; note that views are fixed-angle and may be on a timed rotation.
3. Use any "time-lapse"/archive feature (some require a free or paid account) to look back at a window when a sighting was reported.
4. Pivot: screenshot frames and run reverse-image/geolocation checks; correlate timestamps with other reporting.

## Inputs → Outputs
- **In:** `geolocation`, `address`
- **Out:** `image`, `geolocation` (confirmation of scene/conditions)
- **Empty/negative result looks like:** no camera within useful range of your location — EarthCam covers landmarks and commercial sites, not arbitrary residential streets.

## Gotchas & OpSec
- Human-in-the-loop: none for live viewing; archives/HD may prompt registration or payment.
- OpSec: passive — viewing a public stream is undetectable by the subject. Do not over-trust on-screen clocks; verify timezone/offset before timestamping a sighting.

## Overlaps ("do both")
- Pairs with other webcam aggregators (e.g. Insecam/Windy webcams) because each indexes a different, mostly non-overlapping set of cameras.

## Trust & verifiability
`trust: community` — reputable commercial operator; feeds are real, but treat coverage as sparse and landmark-biased.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | earthcam |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, address → image, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
