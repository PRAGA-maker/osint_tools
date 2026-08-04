---
id: shippingexplorer
name: ShippingExplorer
description: Use when you have a vessel `name`/IMO/MMSI and want its position and voyage history — returns live-ish AIS `geolocation`, ship details and port calls.
url: https://www.shippingexplorer.net/en/map
category: transportation
path:
- transportation
bestFor: Tracking a named vessel on an AIS map and reading its type, flag, and recent positions.
selectorsIn:
- name
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free web access with positions delayed up to ~72 hours ("Demo Mode"); real-time data, history and desktop/mobile apps require a paid ShippingExplorer subscription.
opsec: passive
opsecNote: You query ShippingExplorer's aggregated AIS feed, not the vessel — the ship broadcasts AIS publicly and is unaware of the lookup. Free-tier positions are stale by up to 72h, so do not treat a shown position as the vessel's current location.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running commercial AIS aggregator; coverage depends on terrestrial/satellite receiver density and vessels can disable or spoof AIS, so positions are indicative not guaranteed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Shipping Explorer
- shippingexplorer.net
tags:
- vessel-tracking
- ais
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# ShippingExplorer

> A live AIS vessel-tracking map — locate a ship by name/IMO/MMSI and read its type, flag, destination and recent track (free tier delayed up to ~72 hours).

## When to use
An investigation touches a specific vessel — you have its `name`, IMO or MMSI and want to know where it is or has been, its type and flag state, or its recent port calls. Useful for maritime, cargo, sanctions-adjacent and yacht/owner leads where the ship is the pivot; the vessel's registered details can then feed ownership/company work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.shippingexplorer.net/en/map.
2. Use "Ship Search" to enter the vessel `name` (or IMO/MMSI); you can also filter the map by ship type and navigational status.
3. Open the vessel card: type, flag, dimensions, destination, speed/course, and last reported position on the map.
4. Note the delay banner — the free map is "Demo Mode" with positions up to ~72h old.
5. Pivot: flag + IMO feed ship-registry/ownership lookups; a destination port feeds port-call and logistics leads.

## Inputs → Outputs
- **In:** vessel `name` (or IMO / MMSI)
- **Out:** `geolocation` (last reported position/track), plus vessel type, flag, dimensions and destination
- **Empty/negative result looks like:** no match for the name/number, or a vessel with no recent position — the ship may be out of receiver range, in port with AIS off, or deliberately dark; absence ≠ location unknown forever.

## Gotchas & OpSec
- **Free positions are delayed up to ~72 hours** — never present a demo-mode position as real-time.
- AIS can be switched off or spoofed; a plausible track is not proof of actual location.
- Real-time data, historical voyages and the apps are the paid tier — the free map is deliberately limited.

## Overlaps ("do both")
- Cross-check with other AIS aggregators (MarineTraffic, VesselFinder) — coverage of any single vessel varies by which receiver network saw it, so a ship missing on one may appear on another.

## Trust & verifiability
`trust: community` — a mature commercial AIS aggregator, but the underlying signal is self-reported by the vessel and coverage is receiver-dependent; corroborate a critical position across a second tracker.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shippingexplorer |
| category | transportation |
| selectorsIn → selectorsOut | name → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
