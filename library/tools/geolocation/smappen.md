---
id: smappen
name: Smappen
description: Use when you have a `geolocation` (a last-known point) and want to bound where a person could have travelled in a given time by foot/car/bike/train — returns an isochrone catchment area you can overlay on a search grid.
url: https://www.smappen.com/app/
category: geolocation
path:
- geolocation
bestFor: Drawing isochrone (travel-time) and radius catchment areas around a point to bound a plausible search zone.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free tier (account required) allows a limited number of maps/isochrones; paid plans add more computations, layers, and exports. Core isochrone drawing works on the free tier.
opsec: passive
opsecNote: You enter only a point/location into Smappen's own mapping app; nothing is sent to the subject. Your account and inputs are stored on Smappen's servers, so use a research account and avoid embedding identifying case detail in map names.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial map-analytics product (formerly Cartesius/Enghouse-adjacent isochrone tooling); travel-time polygons come from routing engines and are estimates, not guarantees.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- smappen.com
- Smappen isochrone
tags:
- Maps, Geolocation and Transport
- Tools
- isochrone
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Smappen

> A web mapping app that draws isochrones — how far a person could travel from a point within N minutes on foot, by car, bike, train, or truck — turning a last-known `geolocation` into a bounded search area.

## When to use
You have a starting `geolocation` (a last-known location, a home, a transit stop) and a time budget, and you want to reason about how far the subject could realistically have gone — on foot, by car, by bicycle, or by public transport — within that window. The resulting catchment polygon bounds a ground-search or camera-canvassing area, or lets you test whether a claimed destination is even reachable in the stated time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.smappen.com/app/ and sign in (a free account is required).
2. Place a point on the map at the known `geolocation` (search an address or click the map).
3. Create a catchment: choose **travel time** (isochrone) or **distance** (radius), the transport mode (walk / car / bike / public transport), and the duration (e.g. 30 min).
4. Read the generated polygon — it shows the reachable area; add multiple modes/durations as layers to compare scenarios.
5. Optionally overlay population or points-of-interest layers, or export the area (paid tiers) for use in another map.
6. Pivot: intersect the catchment with camera locations, transit lines, or witness sightings to prioritise where to search.

## Inputs → Outputs
- **In:** `geolocation` (a point) + mode + time/distance
- **Out:** `geolocation` (a catchment polygon / bounded area)
- **Empty/negative result looks like:** an implausibly large or small area usually means the wrong mode or duration was set, or the point sits off the routable network (e.g. mid-water) — reposition and recompute.

## Gotchas & OpSec
- Human-in-the-loop: an **account login** is required even for the free tier; free computations are capped.
- OpSec: **passive** — only your map inputs go to Smappen, never the subject. Use a research account and neutral map names; don't store victim PII in the tool.
- Estimates only: isochrones assume typical routing/speeds and current network data; real travel can exceed or fall short of the polygon (traffic, closures, off-road movement). Treat it as a prioritisation aid, not a hard boundary.

## Overlaps ("do both")
- Pairs with radius/ruler tools and mapping suites — Smappen adds *mode-aware travel time* that a plain radius circle can't, so use it when transport realism matters and a simple radius when you only need "within X km."

## Trust & verifiability
`trust: community` — Smappen is a reputable commercial mapping product, but its polygons are model-derived travel-time estimates from routing engines; verify critical assumptions (mode, speed, network currency) rather than treating the boundary as exact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | smappen |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
