---
id: youtube-metadata-bulk
name: YouTube Metadata Bulk
description: Use when you have a YouTube channel/playlist (`social-profile`) and want per-video metadata at scale — returns `geolocation` geotags, upload patterns and `metadata-exif`-style details.
url: https://mattw.io/youtube-metadata/bulk
category: social-networks
path:
- social-networks
bestFor: Bulk-extracting metadata, geotags and upload cadence across all of a channel's or playlist's videos.
selectorsIn:
- social-profile
- username
selectorsOut:
- geolocation
- metadata-exif
- social-profile
status: live
pricing: free
costNote: Free browser tool; runs on a shared YouTube Data API quota, so very large channels may hit a rate limit until quota resets (or you supply your own API key).
opsec: passive
opsecNote: Reads public YouTube Data API metadata; the channel owner is not notified. All processing is client-side in your browser. Analysing a channel does not interact with it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open, well-regarded independent tool by mattw.io; it surfaces exactly what the YouTube API returns, so accuracy tracks the platform data itself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- location-search
- search-youtube-by-location
- youtube-metadata
aliases:
- mattw.io YouTube Metadata Bulk
- YouTube Bulk Metadata
tags:
- youtube
- metadata
- geolocation
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# YouTube Metadata Bulk

> Bulk metadata extraction for YouTube — pulls per-video details, geotags, links and upload patterns across an entire channel or playlist in one pass.

## When to use
You have a YouTube channel or playlist (`social-profile`/`username`) and you want to profile it at scale rather than one video at a time: extract every video's metadata, harvest geotags to map where content was filmed, find links buried in descriptions, and chart upload frequency by hour/day to infer the poster's timezone and routine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://mattw.io/youtube-metadata/bulk and paste a channel URL/handle, a playlist URL, or a list of video IDs.
2. Run the extraction — it queries the public YouTube Data API and compiles results in the browser.
3. Review: per-video metadata, tags and geotags, description links, upload-frequency charts (with timezone conversion), and a list of unavailable (deleted/private) videos.
4. Export results as JSON/CSV (optionally with thumbnails as a ZIP) for offline analysis.
5. Pivot: geotags feed the companion YouTube Geofind map view and general `geolocation` lookups; description links feed domain/social OSINT; upload-hour histograms suggest the subject's timezone.

## Inputs → Outputs
- **In:** channel (`social-profile`/`username`), playlist, or list of video IDs
- **Out:** per-video metadata, `geolocation` geotags, description links, `metadata-exif`-style publish details, upload-frequency patterns, deleted/private video detection
- **Empty/negative result looks like:** a channel with no geotagged videos and stripped/minimal descriptions — most creators do not geotag, so absence of location data is the norm, not a signal.

## Gotchas & OpSec
- Human-in-the-loop: none, but very large channels can exhaust the shared API quota; supply your own YouTube Data API key or retry after the quota window resets.
- OpSec: **passive** — client-side, reads only public API data, no notification to the owner.
- Geotags are self-declared by the uploader and can be inaccurate or spoofed; corroborate a location before trusting it.

## Overlaps ("do both")
- Pairs with `[[youtube-metadata]]` (single-video deep view) and `[[search-youtube-by-location]]` / `[[location-search]]` — this one does the whole channel in bulk, the others go deep on one video or search by place.

## Trust & verifiability
`trust: community` — an independent open tool that faithfully mirrors YouTube Data API output; reliability equals the platform's own metadata, with self-declared geotags the main caveat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-metadata-bulk |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → geolocation, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
