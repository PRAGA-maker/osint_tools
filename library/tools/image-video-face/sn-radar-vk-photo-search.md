---
id: sn-radar-vk-photo-search
name: SN Radar VK Photo Search
description: Use when you have a `geolocation` and want VKontakte photos taken there — returns geotagged VK photos and the `social-profile`s that posted them.
url: https://snradar.azurewebsites.net/
category: image-video-face
path:
- image-video-face
bestFor: Finding VKontakte photos posted from a specific location (and the users who posted them) by map/coordinates.
selectorsIn:
- geolocation
selectorsOut:
- image
- social-profile
status: degraded
pricing: free
costNote: Free web tool; no account required to query.
opsec: passive
opsecNote: You query VK's public photo index by location, not any individual — no target is contacted. The tool is hosted on Azure and proxies VK's API; assume your searches are logged by the tool operator, so use a sock-puppet browser/VPN for sensitive locations.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community VK-geo tool relying on VKontakte's photo API and geotags; coverage depends on VK's API remaining open and photos actually carrying location data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SnRadar
- snradar.azurewebsites.net
tags:
- vk
- vkontakte
- geolocation
- photo-search
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- osintdashboard-azurewebsites-net
- snradar
---

# SN Radar VK Photo Search

> A map-based VKontakte photo search: draw a location and it returns geotagged VK photos posted there, plus the accounts behind them.

## When to use
You have a `geolocation` — a last-known location, an incident site, a place a subject frequents — and want to see who posted VKontakte photos from that exact spot and when. Strong for missing-person and event work in Russian-speaking regions where VK is the dominant social network: it turns "who was here" into a list of accounts and images to pursue.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://snradar.azurewebsites.net/ in a browser.
2. Navigate the map to the target `geolocation` (or enter coordinates) and set the search radius.
3. Optionally constrain by date/time window to catch photos from a specific event.
4. Read the output: geotagged VK `image`s pinned on the map, each linking to the `social-profile` that posted it.
5. Pivot: an account that posted from the location feeds VK profile-analysis and username tools; the photo itself feeds reverse-image and EXIF checks.

## Inputs → Outputs
- **In:** `geolocation` (map point / coordinates + radius), optional time window
- **Out:** geotagged VK `image`s and the posting `social-profile`s
- **Empty/negative result looks like:** no pins in the area — meaning no VK photos there carry public geotags for your window, NOT that no one was present (most photos aren't geotagged, and VK API limits reduce coverage).

## Gotchas & OpSec
- Only surfaces photos with **public geotags** and requires VK's photo API to be reachable — the tool is Azure-hosted and can be flaky/rate-limited (marked `status: degraded`); if it 403s or errors, retry later or use a VK-geo alternative.
- Coverage is heavily skewed to VK-heavy regions (Russia/CIS); expect little elsewhere.
- OpSec: passive — you query a location index, not a person; still isolate the session for sensitive targets.

## Overlaps ("do both")
- Pairs with other VK OSINT tools (profile/phone/email analysis): SN Radar finds *which* VK accounts were at a place, then those tools enrich each account. Also run any found `image` through a reverse-image search.

## Trust & verifiability
`trust: community` — an independent tool wrapping VKontakte's own photo/geotag data. The photos and coordinates are VK's genuine metadata, but reliability hinges on VK's API access and the tool's uptime, so treat gaps as coverage limits rather than evidence of absence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sn-radar-vk-photo-search |
