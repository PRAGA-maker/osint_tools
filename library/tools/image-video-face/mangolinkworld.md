---
id: mangolinkworld
name: MangolinkWorld
description: Use when you have a `geolocation` and want a live view of it — returns links to public live webcams for cities, beaches, ports, and landmarks worldwide.
url: https://www.mangolinkworld.com/
category: image-video-face
path:
- image-video-face
bestFor: Finding a public live webcam covering a specific place (city, beach, port, landmark) for real-time visual context.
selectorsIn:
- geolocation
selectorsOut:
- image
status: live
pricing: free
costNote: Free directory of publicly-available webcam streams; no account.
opsec: passive
opsecNote: It only links to already-public live webcams — you watch a public feed, touching no target's systems. Nothing is signalled to anyone; standard web logging applies on the aggregator's side.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community webcam-link directory; feeds are third-party and can go offline or be relocated, so verify a given camera is live and points where the listing claims.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Mangolink World
- mangolinkworld.com
tags:
- webcams
- geolocation
- live-cam
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# MangolinkWorld

> A directory of the world's public live webcams — organised by category (beaches, cities, ports, ski slopes, landmarks) to get a real-time view of a place.

## When to use
You have a `geolocation` and want live or near-live visual context of it — to confirm current weather/conditions, watch a public space during a known event window, or corroborate that a scene matches a place. It's a niche, supporting tool: coverage is limited to wherever a public webcam happens to exist, so it helps only when the location of interest has a camera nearby.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.mangolinkworld.com/.
2. Browse by category (Beaches, Urban, Marine, Transport, Sport, Scenery) or region toward your `geolocation`.
3. Open a camera near the target location and watch the public live feed.
4. Compare the feed's landmarks/view to your scene to confirm the place, or observe conditions in real time.
5. Pivot: a confirmed camera viewpoint anchors a geolocation; a live view can corroborate a claimed time/place.

## Inputs → Outputs
- **In:** `geolocation` (a place with a nearby public webcam)
- **Out:** live webcam `image`/stream of the area
- **Empty/negative result looks like:** no camera listed near the location (common for anywhere off the tourist/transport grid), or a dead/relocated feed — absence just means no public cam, not that the place can't be viewed.

## Gotchas & OpSec
- Coverage is sparse and skewed to tourist/scenic/transport spots — most ordinary addresses have no public webcam.
- Feeds are third-party: cameras go offline, move, or get re-aimed; verify a stream is live and framed as the listing claims before relying on it.
- OpSec: fully passive — public feeds only.

## Overlaps ("do both")
- Pairs with dedicated webcam-geolocation platforms (e.g. large global webcam maps) and mapping/Street View — those give broader camera coverage and static ground truth to complement a live feed.

## Trust & verifiability
`trust: community` — a curated link directory to third-party cameras. The feeds are genuine public webcams, but the directory can't guarantee any given camera is live or correctly located, so confirm each one yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mangolinkworld |
