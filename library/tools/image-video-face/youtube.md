---
id: youtube
name: YouTube
description: Use when you have a `name`, `username`, `image`, or `geolocation` and want videos, channels, and faces tied to a subject — returns social-profile, face, and geolocation leads.
url: https://www.youtube.com
category: image-video-face
path:
- image-video-face
bestFor: Finding a subject's own channel/videos, or footage that shows them, their location, vehicle, or associates.
selectorsIn:
- name
- username
- image
- geolocation
selectorsOut:
- social-profile
- face
- geolocation
- associate
status: live
pricing: free
costNote: Free to search and watch; a Google account is only needed to comment or subscribe, not to view.
opsec: passive
opsecNote: Searching and watching are passive against the subject. But liking, commenting, subscribing, or viewing while logged in ties the activity to your Google identity and can surface you in the creator's analytics — watch logged-out in a sock-puppet browser. Downloading videos for frame analysis is fine and offline.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google platform; the videos themselves are authentic primary material, though titles/descriptions are creator-supplied and can mislead.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- youtube.com
- YouTube video search
tags:
- video-search-and-other-video-tools
source: awesome-osint
lastVerified: '2026-07-22'
relatedTools:
- youtube-metadata
- youtube-geofind
- youtube-dataviewer-amnesty
---

# YouTube

> The world's largest video platform — searchable for a subject's own channel and for third-party footage that places, shows, or connects them.

## When to use
You have a `name`, `username`, `image`/`face`, or a `geolocation`, and video may hold what a text search cannot: the subject's voice and face on their own channel, a background that geolocates a photo or a "last seen" clip, a vehicle and plate, or the associates around them at an event. High value in missing-persons work because a channel reveals routine, interests, and network, and event/bystander footage can place someone at a time and place.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.youtube.com logged out (or in a sock-puppet session).
2. Search the `name` and reused `username`/handle; open the Channels filter to find a channel they own, then read the About tab, links, and video back-catalogue.
3. Search event/place keywords + date (e.g. `"Camden market" June 2026`) to find bystander footage; use the search filters (upload date, type, duration) to narrow.
4. For a specific frame, screenshot it and run reverse-image/geolocation tools; extract the video with a downloader for frame-by-frame face, plate, and background analysis.
5. Pivot: a channel yields `social-profile` links, an `associate` network (frequent collaborators/commenters), and often a location; a geolocated frame yields `geolocation` to combine with maps tooling. Feed channel/video IDs to `[[youtube-metadata]]` and `[[youtube-geofind]]` for upload timestamps and mapped location clusters.

## Inputs → Outputs
- **In:** `name`, `username`, `image`/`face`, or `geolocation`/place keyword
- **Out:** `social-profile` (channel + linked accounts), `face`, `geolocation`, `associate`
- **Empty/negative result looks like:** no channel and only unrelated videos — common for low-profile subjects. Absence of a channel is not evidence of anything; pivot to the metadata/geofind helpers and to other platforms.

## Gotchas & OpSec
- Titles, descriptions, and upload dates are creator-controlled and can be edited or backdated — corroborate any claimed time/place against the footage itself and external metadata tools.
- Logged-in engagement (view/like/comment/subscribe) is active and can expose you to the creator via analytics/notifications; stay logged out.
- Search personalisation can bias results; a fresh/incognito session gives more neutral output.

## Overlaps ("do both")
- Pairs with `[[youtube-metadata]]` (exact upload timestamp, tags, thumbnails) and `[[youtube-geofind]]` (map videos by location) — YouTube surfaces the video, those extract the forensic detail the UI hides.

## Trust & verifiability
`trust: trusted` — it is Google's first-party platform, so the video files are authentic primary evidence; the surrounding text (title/description/date) is creator-supplied and must be verified against the footage and metadata tools.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username, image, geolocation → social-profile, face, geolocation, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
