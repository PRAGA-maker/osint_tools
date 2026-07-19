---
id: foxmonitor
name: FoxMonitor
description: Use when you have a `geolocation` (or want live ground truth at a place) and need publicly accessible CCTV/webcam feeds there — returns live camera streams by location.
url: https://www.foxmonitor.com/
category: image-video-face
path:
- image-video-face
bestFor: Browsing freely available live public CCTV/IP-camera streams worldwide by approximate location for real-time ground truth.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free to browse; no account or payment required to view listed streams.
opsec: passive
opsecNote: Viewing an already-public stream through FoxMonitor is passive from the target's perspective. Do not attempt to access any camera that requires a password or is not openly listed — that crosses into unauthorised access. Use a sock-puppet browser and expect the aggregator itself to log your visit.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent volunteer-run directory of open CCTV streams; positions are approximate and listings are community-sourced, so neither location accuracy nor uptime is guaranteed.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Fox Monitor CCTV directory
tags:
- Maps, Geolocation and Transport
- Worldwide street webcams
- cctv
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# FoxMonitor

> An independent directory of freely available live public CCTV/IP-camera streams, browsable by approximate location — a source of real-time visual ground truth.

## When to use
You have a `geolocation` (a city, area, or approximate coordinates) and want to see what a place looks like *right now*, or to establish live conditions — weather, crowds, traffic, whether a location matches a photo. Useful for corroborating a candidate location, watching a public area during a time-sensitive search, or grabbing current imagery a static map can't give you.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.foxmonitor.com/ in a clean/sock-puppet browser.
2. Browse or filter the map/list by region; toggle between active and inactive feeds.
3. Open a live stream near your area of interest and compare the scene (signage, architecture, vehicles, time-of-day light) against your reference material.
4. Note that positions are approximate — use nearby landmarks in the feed itself to refine the true camera location.
5. Pivot: confirmed scene details feed back into `geolocation` reasoning or a reverse-image / mapping tool.

## Inputs → Outputs
- **In:** `geolocation` (place/area of interest)
- **Out:** live `image`/video streams and refined `geolocation` cues from what the camera shows
- **Empty/negative result looks like:** no cameras listed in your area, or a listed feed is offline/moved. Absence of a camera is not evidence of anything; many places have no public feed.

## Gotchas & OpSec
- Camera positions are deliberately approximate for privacy; do not treat the pin as the exact address.
- Only view openly listed, password-free streams — the site excludes password-protected cameras, and you should not seek those out.
- Feeds go up and down constantly; treat uptime as unreliable and re-check.
- OpSec: passive toward the target, but the aggregator sees your traffic — use a sock puppet.

## Overlaps ("do both")
- Pairs with mapping/street-view and reverse-image tools — those give static reference imagery, while FoxMonitor gives a *live* view to confirm current conditions.

## Trust & verifiability
`trust: unverified` — community-maintained directory with approximate positions and volatile uptime; verify any location claim against fixed landmarks visible in the stream rather than trusting the listed coordinates.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | foxmonitor |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation → geolocation, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
