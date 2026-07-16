---
id: search-youtube-by-location
name: YouTube Geofind
description: Use when you have a `geolocation`/place or a channel/keyword and want geotagged YouTube videos on a map — returns geolocation of videos and the posting social-profile.
url: https://mattw.io/youtube-geofind/
category: image-video-face
path:
- image-video-face
- videos
- search
bestFor: Finding geotagged YouTube videos by location radius, topic keyword, or channel, and plotting them on a map for local/event OSINT.
selectorsIn:
- geolocation
- name
- username
selectorsOut:
- geolocation
- social-profile
status: live
pricing: free
costNote: Free web tool; the operator supplies YouTube Data API access, though heavy use can hit shared quota limits and you may need to supply your own API key.
opsec: passive
opsecNote: Read-only querying of the YouTube API via a third-party front-end; you never contact any uploader, so it is passive. If you supply your own API key, that key (tied to a Google project) is used — use a research Google account, not a personal one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-regarded OSINT utility by Matt Wright (mattw.io), widely referenced in the OSINT community (e.g. Bellingcat); front-end to the official YouTube Data API, so results are as reliable as YouTube's own metadata.
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
- location-search
- youtube-metadata
- youtube-metadata-bulk
aliases:
- YouTube Geofind
- mattw.io geofind
- Geo Search Tool
tags:
- youtube
- geolocation
- location-search
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# YouTube Geofind

> A map-based YouTube search that surfaces geotagged videos by location, topic or channel — turn a place into the videos filmed there and the channels behind them.

## When to use
You have a `geolocation`/place (an address, coordinates, or an area) and want to see what YouTube videos are tagged there — for eyewitness footage of an event, videos filmed at a specific site, or a subject's uploads from a known location. You can also feed a channel (`username`) to list its geotagged uploads, or a keyword (`name`) to search topically within an area. The payoff is video `geolocation` plus the uploading `social-profile`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mattw.io/youtube-geofind/.
2. Choose a mode: **Location** (enter a place + radius, optional keyword and date range), **Topic**, or **Channel** (channel ID/handle/URL) to list its geotagged videos.
3. Run the search; results plot on a map with markers per video.
4. Click markers to open videos; export metadata (videos.json, geotags CSV, channel info) as a ZIP for analysis.
5. Extract each video's coordinates (`geolocation`) and uploader (`social-profile`); pivot channels into channel OSINT and locations into mapping.

## Inputs → Outputs
- **In:** `geolocation`/place (+radius), keyword (`name`), or channel (`username`)
- **Out:** `geolocation` (video locations on a map), `social-profile` (uploading channels)
- **Empty/negative result looks like:** few or no markers — expected, since only a minority of uploads are geotagged; a sparse map means low geotag coverage for that area, not that nothing was filmed there.

## Gotchas & OpSec
- Only geotagged videos appear, and uploaders can set/spoof the tag — treat locations as claims to verify against the footage.
- Shared API quota can throttle busy periods; supplying your own YouTube API key improves reliability.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with the Digital Methods YouTube Data Tools and general YouTube advanced search — Geofind is the location lens; combine with channel/comment analysis to build out an uploader once you've found them.

## Trust & verifiability
`trust: community` — a respected community tool fronting the official YouTube API; data is authoritative to YouTube, but geotags are uploader-supplied, so confirm the actual location from the video content.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-youtube-by-location |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, name, username → geolocation, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
