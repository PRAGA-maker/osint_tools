---
id: geo-search-tool
name: Geo Search Tool
description: Use when you need to find YouTube videos posted near a specific location and time — returns geotagged videos on a map for a place, radius, and date range.
url: https://youtube.github.io/geo-search-tool/
category: image-video-face
path:
- image-video-face
- videos
- search
bestFor: Map-based discovery of YouTube videos by geographic location, radius, keyword, and date range.
selectorsIn:
- geolocation
- address
selectorsOut:
- metadata
- image
status: degraded
pricing: free
costNote: Free; uses the YouTube Data API. May require/consume API quota and can break when API behavior changes.
opsec: passive
opsecNote: Queries the public YouTube API for a location/time; the subject is not contacted. Standard Google API telemetry applies.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: Hosted under youtube.github.io (the official YouTube GitHub org) but it is a developer demo tool; historically prone to breaking with API changes.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- frame-by-frame-for-youtube
aliases:
- YouTube Geo Search
- youtube-dataviewer geo
tags:
- video
- youtube
- geolocation
source: arf-seed
lastVerified: ''
enrichment: full
---

# Geo Search Tool

> A map-based search that surfaces YouTube videos uploaded near a chosen location within a time and keyword window.

## When to use
You know roughly where a missing person was last seen or where an event occurred (`geolocation` / `address`) and want bystander or eyewitness footage from that area and date. Tie-in: input a place + radius + date range, output candidate videos (`metadata`) and their thumbnails (`image`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://youtube.github.io/geo-search-tool/.
2. Enter the location (place name or coordinates), set the radius, optional keyword, and a date range.
3. Browse results on the map/list; open promising videos.
4. Pivot: step through any candidate video frame-by-frame with [[frame-by-frame-for-youtube]] to read signs, plates, or faces; capture stills for reverse search.

## Inputs → Outputs
- **In:** `geolocation` / `address` (+ radius, date, keyword)
- **Out:** `metadata` (video listings), `image` (thumbnails)
- **Empty/negative result looks like:** No results, or an error/blank page — often an API-quota or API-change failure rather than truly "no videos."

## Gotchas & OpSec
- Human-in-the-loop: it depends on the YouTube Data API and has historically broken; you may need a working API key/quota, hence `status: degraded`.
- Geotagging on YouTube is sparse — only videos the uploader location-tagged appear, so coverage is incomplete.
- OpSec: passive — only public API queries; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with [[frame-by-frame-for-youtube]] to extract detail from videos this tool surfaces.

## Trust & verifiability
`trust: community` — hosted on the official youtube.github.io org but a fragile developer demo; verify it still loads/returns before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geo-search-tool |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, address → metadata, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
