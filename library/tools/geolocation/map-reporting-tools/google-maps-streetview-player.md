---
id: google-maps-streetview-player
name: Google Maps Streetview Player
description: Use when you want to auto-play Street View along a route like a driving video to scan a corridor for landmarks or sightings.
url: https://brianfolts.com/driver/
category: geolocation
path:
- geolocation
- map-reporting-tools
bestFor: Animate Google Street View along a chosen route ("drive" it) to scan a corridor for matching scenery.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free web tool (Brian Folts' "Drive Smart"/Street View player) built on Google Street View.
opsec: passive
opsecNote: Plays Google Street View imagery in your browser; no contact with the target. Google sees the underlying imagery requests.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known independent Street View animation tool by Brian Folts; depends on Google Street View availability and embed terms.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Drive (Brian Folts)
- Street View Player
tags:
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# Google Maps Streetview Player

> An independent web tool that auto-plays Google Street View along a route you pick — like watching a drive — so you can scan a whole corridor instead of clicking frame by frame.

## When to use
You have a `geolocation`/route (a last-known-route, a road a vehicle may have taken, a corridor where a photo could have been shot) and want to review street-level scenery continuously to spot a matching landmark, a building, or signage. It turns Street View into a playback you can watch, which is faster than manually stepping through Street View nodes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://brianfolts.com/driver/.
2. Set a start and end (or a route) on the map.
3. Press play; the tool animates Street View along the path. Adjust speed and pause to inspect.
4. Note coordinates where scenery matches your reference image.
5. Pivot: confirm the exact spot in `[[google-maps]]` Street View, then cross-check aerial in `[[dualmaps]]`/`[[google-earth-pro]]`.

## Inputs → Outputs
- **In:** route endpoints / `geolocation` / `address`.
- **Out:** sequenced Street View `image` playback tied to `geolocation` along the route.
- **Empty/negative result looks like:** gaps where Street View doesn't exist (rural/private roads) — playback skips or stops; switch to aerial.

## Gotchas & OpSec
- Human-in-the-loop: none; no login.
- Depends on Google Street View coverage and embed availability — a third-party tool can break if Google changes terms.
- Imagery may be years old; verify capture dates in `[[google-maps]]` before drawing conclusions.
- OpSec: passive; only Google sees the imagery requests.

## Overlaps ("do both")
- Built on the same data as `[[google-maps]]`; use Maps for pinpoint confirmation and this for fast corridor scanning.

## Trust & verifiability
`trust: community` — a recognized independent Street View utility; it visualizes Google's data, so accuracy and coverage inherit from Street View.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-maps-streetview-player |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
