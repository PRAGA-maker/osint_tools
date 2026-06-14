---
id: viamichelin
name: ViaMichelin
description: Use when you need driving routes, distances, ETAs, and toll/fuel cost estimates between two places to test whether a journey or timeline is plausible.
url: http://www.viamichelin.com
category: geolocation
path:
- geolocation
bestFor: Route planning and travel-time/distance estimation between locations, with European detail strength.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free consumer maps/routing site, ad-supported.
opsec: passive
opsecNote: A public routing/maps lookup; you query the site, never the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Michelin's established consumer mapping/routing service; routing data is mainstream and reliable, strongest in Europe.
missingPersonsRelevance: medium
coverage:
- eu
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- yandex-maps
- yahoo-maps
aliases:
- Via Michelin
tags:
- geospatial-research-and-mapping-tools
- routing
source: awesome-osint
lastVerified: ''
enrichment: full
---

# ViaMichelin

> Michelin's maps-and-routing site — useful for sanity-checking travel time, distance, and route between two points, with particularly good European coverage.

## When to use
You have two `address`es or `geolocation`s (last-known location and a candidate destination) and need to test a timeline: how far apart are they, how long would the drive take, what route is natural, and roughly what it would cost in tolls/fuel. That answers "could the person plausibly have travelled from A to B in the claimed window?" It is a route/distance tool, not a person lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.viamichelin.com (now viamichelin.com).
2. Enter a start and destination address/place into the route planner.
3. Read the distance, estimated driving time, and toll/fuel cost breakdown; switch route options (fastest/shortest/economical) to see alternatives.
4. Use the map to inspect the actual roads and any waypoints along the way.
5. Pivot: compare ETAs against the case timeline; for regional map detail outside Europe, cross-check with [[yandex-maps]] or general satellite tools.

## Inputs → Outputs
- **In:** start + destination `address`/`geolocation`.
- **Out:** route, distance, travel-time estimate, toll/fuel cost (timeline/plausibility evidence; refined `geolocation` of the path).
- **Empty/negative result looks like:** no road route between the points (e.g. cross-water without ferry) — meaningful in itself for a driving theory.

## Gotchas & OpSec
- No login or captcha; fully passive.
- Strongest detail and accuracy in Europe; coverage thins elsewhere.
- ETAs assume normal conditions and don't model the specific traffic/weather of a past date — treat as approximate.

## Overlaps ("do both")
- Pairs with [[yandex-maps]] (better for Russia/CIS) and general satellite tools for cross-checking the actual roads and terrain.

## Trust & verifiability
`trust: trusted` — Michelin is an established mapping provider; routing math is standard and reproducible against any major maps engine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | viamichelin |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
