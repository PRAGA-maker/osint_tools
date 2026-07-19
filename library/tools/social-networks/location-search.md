---
id: location-search
name: YouTube Geofind — Location Search
description: Use when you have a `geolocation` and want videos filmed there — returns YouTube videos geotagged near a point, with uploader channels and coordinates.
url: https://mattw.io/youtube-geofind/location
category: social-networks
path:
- social-networks
bestFor: Finding YouTube videos geotagged near a specific location to surface footage and channels tied to a place.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- social-profile
status: live
pricing: free
costNote: Free, browser-based, no login; it uses the public YouTube Data API (the site supplies the quota).
opsec: passive
opsecNote: You query the public YouTube API via a third-party front-end; no uploader is notified and you only see public, geotagged uploads. Use a research browser profile; nothing about your subject is submitted beyond the location you search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known independent OSINT tool (mattw.io by Matthew Wright) over the official YouTube API; results are real public videos, though only those the uploader chose to geotag appear.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- search-youtube-by-location
- youtube-metadata
- youtube-metadata-bulk
aliases:
- YouTube Geofind
- Geofind Location Search
tags:
- YouTube
- geolocation
- video
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# YouTube Geofind — Location Search

> Drop a pin and get the YouTube videos filmed near it — a fast way to surface local footage, and the channels behind it, tied to a specific place.

## When to use
You have a `geolocation` or `address` and want eyes on the ground: videos geotagged near that point can show a location as it was, reveal locals who film there, or capture an event/scene relevant to a case. In a missing-persons or incident investigation this can surface footage a subject uploaded near a last-known location, or channels of people in the area worth contacting. It only finds videos the uploader chose to geotag, so it's a targeted supplement, not exhaustive coverage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mattw.io/youtube-geofind/location and enter a place or coordinates; set the search radius and (optionally) a keyword/date range.
2. Run the search; results plot on a map with each video's channel, upload date, and coordinates.
3. Open relevant videos and their channels; note uploaders active in the area.
4. Pivot: an uploader `social-profile`/channel feeds YouTube-metadata tools and cross-platform handle checks; the coordinates refine your geolocation.

## Inputs → Outputs
- **In:** `geolocation`/`address` (+ optional keyword/date)
- **Out:** geotagged YouTube videos near the point → uploader `social-profile`s and precise `geolocation`
- **Empty/negative result looks like:** few or no geotagged videos — normal for rural or low-activity areas, since most uploads carry no location tag.

## Gotchas & OpSec
- Human-in-the-loop: none; if results stop, the tool's shared API quota may be exhausted — retry later.
- Only geotagged uploads appear — absence doesn't mean nothing was filmed there.
- Geotags can be set inaccurately by uploaders; confirm the actual location from video content.

## Overlaps ("do both")
- Pairs with `[[youtube-metadata]]`/`[[youtube-metadata-bulk]]` — this finds videos by place; those extract full upload metadata from the videos you find.

## Trust & verifiability
`trust: community` — a respected independent OSINT front-end over the official YouTube API; results are genuine public videos, bounded to those uploaders geotagged.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | location-search |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation, address → geolocation, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
