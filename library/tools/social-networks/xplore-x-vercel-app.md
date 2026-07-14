---
id: xplore-x-vercel-app
name: xplore-x.vercel.app
description: Use when you have a `geolocation` (a point/area of interest) and want to see live X/Twitter posts from that place — returns geographically-filtered social-profile posts on a map.
url: https://xplore-x.vercel.app/
category: social-networks
path:
- social-networks
bestFor: Surfacing real-time X posts originating near a chosen location via a radius-on-map search.
selectorsIn:
- geolocation
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free web app hosted on Vercel; no account required.
opsec: passive
opsecNote: You browse public X content through a third-party front-end; no target is notified. The app (and its Vercel backend) sees your queries and IP — use a sock-puppet browser. Do not assume displayed post locations are precise; X geotags are coarse and often account-set rather than device-GPS.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small independent hobby project deployed on Vercel; not affiliated with X. Depends on X's data access, which can break without notice.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- twitter-advanced-search
aliases:
- Xplore
- Xplore-X
tags:
- xtwitter
- X / Twitter Related Sites
- geosocial
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# xplore-x.vercel.app

> A map-first X/Twitter explorer: pick a location and radius, see live public posts from that area.

## When to use
You have a `geolocation` — a last-known area, an event site, a landmark in a target's photo — and want to see what X users are posting nearby in near-real-time. Useful for event/scene monitoring and for surfacing local accounts you can then pivot on, rather than starting from a known handle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://xplore-x.vercel.app/ in a sock-puppet browser.
2. Navigate the map to the area of interest and set the search radius (1 km, 5 km, or 50 km).
3. Read the returned live posts pinned geographically; open Advanced Options to refine.
4. Pivot: open a promising post's author on X and run their handle through `[[twitter-advanced-search]]` for keyword/date history, and treat any location as a lead to corroborate, not a fix.

## Inputs → Outputs
- **In:** `geolocation` (map point + radius)
- **Out:** `social-profile` (public X posts and their authors), coarse `geolocation` per post
- **Empty/negative result looks like:** no pins in the radius — either nobody geotagged posts there recently, or X's data feed is unavailable; widen the radius or retry later.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — you're reading public content; no target is alerted. The third-party app sees your IP/queries; use a sock puppet.
- Reliability caveat: it rides on X's data access and can silently break; geotag precision is weak, so never treat a shown location as confirmed device position.

## Overlaps ("do both")
- Pairs with `[[twitter-advanced-search]]` — this finds accounts by *place*, then advanced search profiles a specific account by *keyword and time*.

## Trust & verifiability
`trust: community` — an independent hobby deployment, not an X product. Corroborate any location signal independently before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xplore-x-vercel-app |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
