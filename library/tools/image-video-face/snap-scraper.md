---
id: snap-scraper
name: Snap-Scraper
description: Use when you have a `geolocation` (lat/long) and want the public Snapchat media posted there — returns downloaded images/video from Snap Map for that spot.
url: https://github.com/rhematt/Snap-Scraper
category: image-video-face
path:
- image-video-face
bestFor: Pulling geolocated public Snapchat Snap Map media for a set of coordinates, e.g. a last-known location.
selectorsIn:
- geolocation
selectorsOut:
- image
status: live
pricing: free
costNote: Free, open-source tool. No account, API key, or payment; you supply the coordinates from map.snapchat.com.
opsec: passive
opsecNote: You query Snapchat's public Snap Map endpoint, not the target directly, and posters are not notified. Run it from a research machine; downloaded media lands in your Downloads/Snapchat folder, so handle that evidence carefully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small open-source project (~100+ stars) by rhematt. It relies on Snapchat's public Map API, which can change without notice and break the tool.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- SnapScraper
- Snapchat Snap Map scraper
tags:
- snapchat
- snapmap
- geolocation
- media
source: gh-topic-osint-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Snap-Scraper

> A command-line downloader for Snapchat's public Snap Map: give it coordinates, get the public Snaps posted at that place.

## When to use
You have a `geolocation` — precise lat/long — for a place of interest (a last-known location, an incident scene, a venue) and want to harvest the public Snapchat media posted there. Snap Map surfaces user-submitted Snaps by location, so this can put a face, a scene, or a timestamped clip at a specific spot, which is exactly what last-known-location work needs.

## How to use it (`bestInteractionPattern`: cli)
1. Get coordinates: open https://map.snapchat.com, navigate to your area, and read the latitude/longitude (to ~6 decimals) and zoom level (to ~2 decimals) from the URL.
2. Download the latest release from the GitHub repo. It ships as a macOS binary (Windows/Linux would need compiling from source; it depends on the Alamofire networking library).
3. `chmod 755 SnapScraper` and run it.
4. Enter the latitude, longitude, and zoom when prompted.
5. Read output: media metadata prints in the terminal; files download to `~/Downloads/Snapchat`, organized by timestamp and coordinates. Optionally it prints direct media links.
6. Pivot: faces in the media feed face-search tools; scene detail feeds geolocation verification.

## Inputs → Outputs
- **In:** `geolocation` (latitude, longitude, zoom)
- **Out:** `image` / video files of public Snaps at that location, plus metadata
- **Empty/negative result looks like:** no media returned for the coordinates. Snap Map only shows areas with enough public submissions, so quiet/rural spots or a too-tight zoom yield nothing — widen the zoom or re-check the coordinates.

## Gotchas & OpSec
- macOS-first: the prebuilt binary is Mac-only; other platforms require compiling.
- Fragile dependency on Snapchat's unofficial Map API — expect breakage when Snapchat changes it; check the repo's issues if it stops working.
- Only *public* Snaps appear; nothing private is exposed.
- OpSec: passive — you hit Snapchat's public endpoint, not the poster. Store harvested media as sensitive evidence.

## Overlaps ("do both")
- Do alongside other geolocated-media tools (Instagram/TikTok location search) — each platform surfaces different public posts at the same coordinates.

## Trust & verifiability
`trust: community` — an open-source hobbyist tool; the media itself is authentic Snapchat content, but the scraper's reliability tracks Snapchat's undocumented API. Verify each Snap's location/time against the on-screen metadata rather than assuming the coordinates you entered.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snap-scraper |
</content>
