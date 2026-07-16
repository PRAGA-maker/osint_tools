---
id: facebook-live-map
name: Facebook Live Map
description: Use when you want to discover live and recent Facebook Live videos — historically on a world map for geolocation — to find footage from a location or event; returns social-profile video streams.
url: https://facebook.com/live
category: image-video-face
path:
- image-video-face
- videos
- search
bestFor: Finding live/recent Facebook Live broadcasts, useful for footage from an area or event of interest.
input: name/geolocation/event
output: live and recent Facebook Live videos
selectorsIn:
- name
- geolocation
selectorsOut:
- social-profile
- image
status: degraded
pricing: free
costNote: Free. Facebook removed the public world "Live Map" that once plotted streams geographically; the /live hub still surfaces live and recent broadcasts, but map-based geo-discovery is gone.
opsec: active
opsecNote: Meaningful browsing needs a Facebook login — use a sock account, never your own. Watching a stream may register a viewer count but not your identity; do not comment/react, which is attributable.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Facebook surface; the streams are genuine. However the flagship geolocation feature (the Live Map) has been discontinued, so it no longer works as originally catalogued.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- facebook-watch
- facebook
- facebook-ad-s-link
- facebook-com
- facebook-com-2
- facebook-directory-users-by-name
- facebook-photos-by-id
- facebook-profile-directory
- fb-email-search
- fb-identify-requires-logout
- recover-fb-account
aliases:
- facebook.com/live
- FB Live
tags:
- facebook
- video
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Facebook Live Map

> Facebook's live-video hub — once a world map of active streams for geolocation, now a live/recent broadcast feed after Facebook retired the map.

## When to use
You want to find Facebook Live footage tied to a place, event, or person — for example, streams from an area where a subject was last seen, or a subject's own live broadcasts. Historically the "Live Map" let you click a region to see active streams there; Facebook has since removed that map, so today this is best for finding a specific account's or keyword's live/recent streams rather than pure geo-browsing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a **sock** Facebook account and open https://facebook.com/live.
2. Browse featured live/recent broadcasts, or search a `name`/keyword/place to find related streams; on a known profile, check for active or past live videos.
3. Open a stream and scan for location cues, faces, vehicles, and audio/context.
4. Read the output: live or recorded `social-profile` streams and their thumbnails/frames (`image`).
5. Pivot: frames feed geolocation/reverse-image/face tools; the broadcasting account feeds profile and associate mapping; combine with [[facebook-watch]] for the account's non-live video.

## Inputs → Outputs
- **In:** `name`/keyword or `geolocation`/event of interest
- **Out:** `social-profile` (live/recent broadcasts), `image` (thumbnails/frames)
- **Empty/negative result looks like:** no relevant live content — common, since live streams are ephemeral and the geo-map is gone. Absence here is weak evidence.

## Gotchas & OpSec
- The public geo "Live Map" is discontinued — do not expect to click a location and see all streams there. Third-party trackers that mimicked it are mostly dead.
- Live content is transient; timing matters, and most value is in a specific account's past live videos.
- OpSec: **active** (login required); keep the sock session passive — watch, don't interact.

## Overlaps ("do both")
- Pairs with [[facebook-watch]] — Live covers real-time/streamed video, Watch covers the account's uploaded video library. Together they capture a subject's full Facebook video footprint.

## Trust & verifiability
`trust: trusted` — first-party Facebook streams are authentic. The rating is tempered by the loss of the geolocation Live Map, which changes how the tool is used from its original catalog description.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-live-map |
| category | image-video-face |
| selectorsIn → selectorsOut | name, geolocation → social-profile, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
