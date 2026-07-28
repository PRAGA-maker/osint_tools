---
id: fisgonia
name: Fisgonia
description: Use when you have a `geolocation` and want publicly-accessible IP cameras (and other public sensors) plotted on a map of that area — returns geolocation/live camera views.
url: http://www.fisgonia.com/
category: geolocation
path:
- geolocation
bestFor: Finding open/public IP cameras near a location on a world map to get eyes on an area.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: freemium
costNote: Free to browse the map; no account. Availability has been intermittent, so expect the site or individual feeds to be down at times.
opsec: passive
opsecNote: Browsing the map is passive, but opening a camera feed connects you to that device/host, which sees your IP. Use a VPN. View only genuinely public/open cameras; do not attempt access to anything credentialed or clearly private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party (Spanish) aggregator plotting publicly-listed cameras/sensors; coverage, uptime and feed accuracy vary, and listings can be stale.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- fisgonia.com
tags:
- webcams
- surveillance
- geolocation
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Fisgonia

> A map-first directory of publicly-accessible IP cameras (and some other public sensors) — a way to get live eyes on an area, plotted geographically.

## When to use
You have a `geolocation` and want a live public view of that area — to observe current conditions, corroborate a scene, or add real-time context to a location reached through other tools. Fisgonia plots publicly-listed cameras on a world map so you can browse to a region and open nearby feeds. It observes places, not people, and only covers cameras that are already publicly exposed/listed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.fisgonia.com/ (retry if it's temporarily unreachable — uptime is intermittent).
2. Navigate the map to your `geolocation` and look for camera markers nearby.
3. Open a marker to view the feed; match visible landmarks/signage/weather against your other evidence and note the time.
4. Use a VPN when opening feeds so the camera host doesn't log your real IP.
5. Pivot: corroborate the live view against satellite/street imagery and webcam directories for the same spot.

## Inputs → Outputs
- **In:** `geolocation` (map area)
- **Out:** publicly-accessible camera feeds giving live `geolocation` context (scene, weather, activity)
- **Empty/negative result looks like:** no markers near the target, or dead/offline feeds — public-camera coverage is sparse and volatile; fall back to `[[city-webcams-com]]` or imagery tools.

## Gotchas & OpSec
- OpSec: browsing passive; opening a feed exposes your IP to the host — VPN. Stick to genuinely public/open cameras; don't touch anything credentialed or private.
- Uptime is unreliable (marked degraded) and listings go stale — a dead feed or down site is expected.
- Cameras cluster at landmarks/public spaces, not arbitrary addresses — don't expect a view of a specific home.

## Overlaps ("do both")
- Do both with `[[city-webcams-com]]` and satellite/street imagery — Fisgonia and webcam directories each list cameras the other misses, and fixed imagery gives the reference to match a live feed against.

## Trust & verifiability
`trust: community` — a third-party camera aggregator with variable uptime and accuracy; always confirm a feed's location by matching landmarks to a known map before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fisgonia |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
