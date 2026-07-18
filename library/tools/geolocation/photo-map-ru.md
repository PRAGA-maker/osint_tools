---
id: photo-map-ru
name: Photo-Map.RU
description: Use when you have a `geolocation` in the former USSR and want VK posts taken there — returns geotagged VKontakte photos/posts plotted on a map around a point.
url: http://photo-map.ru/
category: geolocation
path:
- geolocation
bestFor: Finding geotagged VKontakte (VK) photos and posts by location — surfacing who posted from a specific place in Russia/CIS.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- social-profile
- image
status: degraded
pricing: free
costNote: Free to use; depends on VK API access, which has tightened over time, so availability/coverage can be intermittent.
opsec: passive
opsecNote: Passive — you browse geotagged public VK content via the tool; the posters aren't notified. If you then open a VK profile to investigate, do so from a sock-puppet VK session, not an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community geolocation tool listed in Bellingcat's toolkit; it surfaces public VK data via the VK API, so results depend on what users made public and on continued API access.
missingPersonsRelevance: medium
coverage:
- ru
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- photo-map.ru
- VK photo map
tags:
- bellingcat-toolkit
- geolocation
- vkontakte
- russia
source: bellingcat-toolkit
lastVerified: '2026-07-18'
enrichment: full
---

# Photo-Map.RU

> A map of geotagged VKontakte posts — click a location in Russia/CIS and see the public VK photos and posts made there, a location-first way into VK's social graph.

## When to use
You have a `geolocation` or `address` in Russia or the former-USSR sphere and want to know who posted from there on VK — the dominant social network in the region. Instead of starting from a person, you start from a *place*: pull the geotagged VK content around a point to find witnesses, residents, or a subject's own posts tied to a location. Strong for missing-persons and event work where VK coverage beats Western platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://photo-map.ru/ (if it's briefly unavailable, retry — it's VK-API-dependent and can be flaky).
2. Navigate the map to your area of interest and load the geotagged VK posts there.
3. Inspect the pinned photos/posts: content, timestamp, and the VK author behind each.
4. Open promising authors on VK — from a sock-puppet account — to profile them further.
5. Pivot: a geotagged post ties a `social-profile` to a place and time; photos feed reverse-image search; the VK author feeds VK-focused people OSINT.

## Inputs → Outputs
- **In:** a `geolocation`/`address` (map location in Russia/CIS)
- **Out:** geotagged VK posts at that location — `image`s, timestamps, and the posting `social-profile`
- **Empty/negative result looks like:** few or no pins means little public geotagged VK activity there (or the API is limiting results) — VK users increasingly disable geotags, so absence is common and not conclusive.

## Gotchas & OpSec
- **VK-API-dependent and degraded:** VK has tightened API access; the tool can be intermittent or return partial data. Treat gaps as tooling/coverage limits.
- Only sees *public, geotagged* VK posts — a shrinking subset as geotagging declines.
- Investigate discovered VK profiles only from a sock puppet; VK shows profile visitors in some contexts.

## Overlaps ("do both")
- Complements VK-username/people tools and other geolocation sources — Photo-Map.RU works *location→people* on VK, while username tools work *person→accounts*; combine for both directions.

## Trust & verifiability
`trust: community` — a Bellingcat-listed community tool surfacing genuine public VK data via the VK API; results are real but coverage is constrained by user privacy settings and API limits, so corroborate a decisive find on VK directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | photo-map-ru |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
