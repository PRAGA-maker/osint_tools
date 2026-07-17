---
id: youtube-metadata
name: YouTube Metadata
description: Use when you have a YouTube video, channel, or playlist URL and want its full metadata — returns upload/publish timestamps, geotags, thumbnails, tags, and comment data.
url: https://mattw.io/youtube-metadata/
category: image-video-face
path:
- image-video-face
bestFor: Extracting hidden/structured metadata (exact publish time, geotag, thumbnails, tags, comment history) from a YouTube video, channel, or playlist.
selectorsIn:
- social-profile
- username
selectorsOut:
- geolocation
- metadata-exif
- name
status: live
pricing: free
costNote: Free web tool; uses the public YouTube Data API. May hit a shared quota — you can supply your own free API key via a userscript to keep going.
opsec: passive
opsecNote: Queries route through the YouTube Data API against public video/channel data; the uploader is not notified and cannot see who looked. No login needed. Your requests are anonymous to the channel owner.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source tool by Matthew Wright (mattw.io); reads directly from the official YouTube Data API, so the metadata is authoritative.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- youtube-metadata-bulk
- youtube-dataviewer
- search-youtube-by-location
- location-search
aliases:
- mattw youtube metadata
- YouTube Metadata tool
tags:
- video-search-and-other-video-tools
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# YouTube Metadata

> A web front-end to the YouTube Data API that dumps everything YouTube knows about a video, channel, or playlist — the exact publish time, geotag, tags, and thumbnails you can't see in the normal UI.

## When to use
You have a YouTube video/channel/playlist link (from a subject's `social-profile` or a `username`) and want the structured metadata behind it: the precise UTC publish timestamp (vs. the vague "3 years ago"), any geotag, the full tag list, all thumbnail resolutions, and comment/engagement data. Useful for verifying when footage was really posted, geolocating a video, or profiling a channel's activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mattw.io/youtube-metadata/.
2. Paste a video URL/ID, channel URL/ID, or playlist URL and submit.
3. Review the parsed panels: video details (published-at, description, tags, category, live-stream times), channel details (creation date, country, stats), geotag if present, and every thumbnail size.
4. If a video is deleted/unavailable, the tool can pull archived data from Filmot and the Wayback Machine.
5. If the shared API quota is exhausted, follow the on-page note to plug in your own free YouTube Data API key via the Tampermonkey userscript, then retry. Export results as a ZIP of JSON + thumbnails.
6. Pivot: geotag → `[[search-youtube-by-location]]` and mapping tools; publish timestamp → build/verify a timeline; channel country/creation date → corroborate identity.

## Inputs → Outputs
- **In:** YouTube video / channel / playlist URL or ID (`social-profile`, `username`)
- **Out:** publish/creation timestamps, geotag (`geolocation`), tags, thumbnails, channel country and stats (`metadata-exif`, `name`)
- **Empty/negative result looks like:** "Video/channel not found" or a private/deleted item — try the Filmot/Wayback fallback; a missing geotag simply means the uploader didn't attach one (most don't).

## Gotchas & OpSec
- Shared API quota is frequently exhausted ("someone" burns it) — expect quota errors and be ready to add your own key.
- Geotags are rare; absence isn't suspicious. When present, they're uploader-supplied and can be spoofed — corroborate.
- Fully passive: the channel owner gets no signal that you queried them.

## Overlaps ("do both")
- Pairs with `[[youtube-metadata-bulk]]` when you need to process many URLs at once instead of one at a time.
- Pairs with `[[search-youtube-by-location]]` — pull a geotag here, then find other videos filmed nearby.

## Trust & verifiability
`trust: community` — a well-regarded open-source tool, but it's a thin viewer over YouTube's official Data API, so the metadata it shows is authoritative straight from Google.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-metadata |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile, username → geolocation, metadata-exif, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
