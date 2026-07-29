---
id: nperf-com-map-5g
name: nperf.com/map/5g
description: Use when you have a `geolocation`/`address` and want to know which mobile operators have 5G there — returns crowdsourced 5G coverage by carrier for a location.
url: https://www.nperf.com/en/map/5g
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking crowdsourced worldwide 5G coverage by operator at a given location for connectivity/plausibility context.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The public map is free to view; nPerf's PRO tool with advanced filtering is a paid product aimed at mobile operators, but nothing paid is needed for basic coverage lookups.
opsec: passive
opsecNote: Read-only public map — you query nPerf's servers about a location, not any target, and nothing about your subject is transmitted. No login, no target contact; ordinary web hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: nPerf is an established connectivity-benchmark company; data is crowdsourced from nPerf app users on 5G devices, so coverage reflects where users tested — sparse-user areas are under-represented and "detected" cells may be pre-commercial test signals.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nperf-com-map
aliases:
- nPerf 5G map
tags:
- Maps, Geolocation and Transport
- Communications, Internet, Technologies
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# nperf.com/map/5g

> A worldwide, crowdsourced 5G coverage map broken down by mobile operator — connectivity context for a location, not a people or device lookup.

## When to use
You have a `geolocation` or `address` and want to know whether — and via which carriers — 5G is available there. Useful as supporting context: sanity-checking whether a claimed high-speed mobile connection is plausible at a location, understanding which operator a device in an area is likely on, or profiling the connectivity of a place. It does not identify people or devices; it characterizes the network environment.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nperf.com/en/map/5g.
2. Search or pan/zoom to the target location (city, address, or coordinates).
3. Toggle operators to see each carrier's crowdsourced 5G coverage footprint; the map updates hourly and retains two years of data.
4. Read coverage as a probability, not a guarantee — colored cells mean users tested 5G there, and some "detected" cells are pre-commercial operator tests, not open service.
5. Pivot: combine the likely operator with other location context; for 4G/3G/general mobile coverage use the sibling full map.

## Inputs → Outputs
- **In:** `geolocation` / `address` (a place to inspect)
- **Out:** `geolocation`-scoped 5G coverage by operator
- **Empty/negative result looks like:** no colored coverage at the location — either genuinely no 5G, or simply no nPerf user has tested there (common in rural/low-traffic areas), so absence is weak evidence.

## Gotchas & OpSec
- No login and no target interaction — nothing to leak.
- Crowdsourced: coverage is biased toward where nPerf app users are; sparse-user regions look emptier than reality.
- "5G detected" can mean pre-commercial testing, not consumer availability — don't over-read it.

## Overlaps ("do both")
- Pairs with `[[nperf-com-map]]` (the full multi-technology coverage map) — use this for 5G specifically and the sibling for 3G/4G and general mobile/broadband coverage at the same location.

## Trust & verifiability
`trust: community` — from an established benchmarking firm, but the data is crowdsourced and therefore uneven; treat coverage as an approximate, user-density-biased signal rather than an operator-authoritative map.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nperf-com-map-5g |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
