---
id: ukraine-live-cams
name: Ukraine Live Cams
description: Use when you have a location in Ukraine and want nearby live webcams plus fire and frontline overlays for geolocation/verification — returns geolocation, image.
url: https://nagix.github.io/ukraine-livecams/#5.5/47.774/31.685/0/45
category: geolocation
path:
- geolocation
bestFor: Finding live public webcams across Ukraine with NASA fire and control-line overlays for conflict/geolocation verification.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free open-source map (GitHub Pages); it aggregates third-party public webcams and open datasets.
opsec: passive
opsecNote: Passive — you view public webcam feeds and open data. Watching a camera sends traffic to that camera's host (a third party), not to any subject; use a VPN if that host's location matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source hobby project by Akihiko Kusanagi aggregating public webcams, NASA FIRMS fire data, and Liveuamap control lines; overlays are third-party and should be corroborated.
missingPersonsRelevance: low
coverage:
- ua
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Ukraine Live Cams
- nagix ukraine-livecams
tags:
- webcams
- geolocation
- ukraine
- conflict
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Ukraine Live Cams

> An interactive map of public webcams across Ukraine, overlaid with NASA fire detections and frontline/occupation lines — a fast way to get live ground-level imagery near a location of interest.

## When to use
You have a `geolocation` in Ukraine and want **live visual context**: nearby public webcams to see current conditions, plus fire (FIRMS) and control-line overlays to understand the situation around that point. Useful for conflict monitoring, corroborating a claimed event/location, or grabbing a live view to compare against other imagery during geolocation work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nagix.github.io/ukraine-livecams/ and pan/zoom the map to your area of interest.
2. Click a camera icon to open its live feed; toggle the NASA FIRMS fire layer and the Liveuamap occupation/frontline overlay.
3. Cross-reference what you see against satellite imagery, other cams, and reports.
4. Pivot: a live webcam view feeds geolocation/chronolocation; fire detections and control lines add situational context to a location or timeline.

## Inputs → Outputs
- **In:** a `geolocation` (area of Ukraine)
- **Out:** nearby live webcam feeds (`image`/video), plus fire and frontline overlays for that `geolocation`
- **Empty/negative result looks like:** no cameras near the point, or dead/offline feeds — coverage is patchy and cams go down; absence of a cam isn't information about the location.

## Gotchas & OpSec
- Feeds are **third-party public webcams** of varying reliability; some are offline, mislabelled, or delayed — verify the camera's actual location before trusting its view.
- Overlays (fire, frontline) come from external sources (NASA FIRMS, Liveuamap) and can lag or err — corroborate.
- Passive to any subject, but each cam host sees your connection; use a VPN for sensitive work.

## Overlaps ("do both")
- Pairs with satellite/aerial imagery and other webcam directories — a live cam gives the current ground view, imagery gives the top-down and history; together they anchor a geolocation.

## Trust & verifiability
`trust: community` — a solid open-source aggregator, but everything it shows is third-party (cams, fire data, control lines); confirm the location and freshness of any feed before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ukraine-live-cams |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
