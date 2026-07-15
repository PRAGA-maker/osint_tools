---
id: gramfeed-com
name: Gramfeed.com
description: Use when you have an Instagram `username` and want a web viewer with map/geo browsing — but the service has shut down, so treat as defunct.
url: http://gramfeed.com
category: social-networks
path:
- social-networks
bestFor: (Defunct) web-based Instagram browsing with search and map view; service discontinued.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
- geolocation
status: down
pricing: free
costNote: Was a free/freemium Instagram web client; it later rebranded to Picodash and has since been discontinued. The domain now returns errors.
opsec: passive
opsecNote: Moot — the service is discontinued. When it operated it was a third-party Instagram client (passive toward the subject).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Was an early third-party Instagram web client (later "Picodash"); shut down after Instagram tightened API access. Opaque ownership and now non-functional.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Picodash
tags:
- instagram
- defunct
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Gramfeed.com

> An early third-party Instagram web client (later rebranded Picodash) that offered search and map/geo browsing — now discontinued.

## When to use
Do not reach for this: `gramfeed.com` no longer serves the tool (it redirects to a dead/erroring host). It once let you browse public Instagram content in a browser, search hashtags/users, and — notably for OSINT — view posts on a map by their attached `geolocation`. That geo-map feature stopped working years ago when Instagram removed public geotag access, and the service later shut down entirely.

## How to use it (`bestInteractionPattern`: web-manual)
1. (Not usable.) The domain returns errors and offers no working search.
2. Instead, for Instagram geolocation use current techniques (EXIF from downloaded media, tagged-location pages viewed directly, or dedicated geo-OSINT tools); for profile browsing use a live Instagram viewer.

## Inputs → Outputs
- **In:** (formerly) `username` / hashtag
- **Out:** (formerly) `social-profile`, `image`, and post `geolocation` on a map
- **Empty/negative result looks like:** the site errors out or fails to load — no working surface remains.

## Gotchas & OpSec
- Status: **down / discontinued** — flag and move on.
- Even when it worked, its geo-map depended on Instagram's old public geotag API, which no longer exists; do not expect that capability from any modern replacement without EXIF.

## Overlaps ("do both")
- Substitute EXIF/geo-OSINT tooling for the map feature and a live Instagram viewer for browsing; confirm any replacement is operational first.

## Trust & verifiability
`trust: unverified` — defunct third-party client. No data obtainable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gramfeed-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, image, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
