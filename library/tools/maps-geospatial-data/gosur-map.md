---
id: gosur-map
name: Gosur Map
description: Use when you have an `address` or `geolocation` and want satellite/aerial imagery of it with extras like live cams and weather — returns a satellite view for that `geolocation`.
url: http://www.gosur.com/map
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Quick satellite/aerial view of an address, with map-overlay extras (webcams, weather, traffic).
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web map viewer; ad-supported.
opsec: passive
opsecNote: Passive — you look up public map imagery; no subject is notified. It's an ad-supported third-party site fronting satellite imagery providers, so expect ads/trackers; use a hardened browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party map front-end aggregating commercial satellite imagery and overlays; convenient but not an authoritative or first-party mapping source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- gosur.com map
tags:
- maps
- satellite-imagery
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# Gosur Map

> An ad-supported satellite-map front-end for a fast aerial look at an address, with overlays like webcams, weather, and traffic.

## When to use
You have an `address` or `geolocation` and want a quick satellite/aerial look plus contextual overlays (nearby webcams, weather, traffic) in one place. It's a convenience viewer over commercial imagery — useful for a fast visual of a location, but for rigorous imagery analysis prefer first-party providers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.gosur.com/map.
2. Search the `address` or navigate to the `geolocation`.
3. Switch to satellite/aerial view and use overlays (webcams, weather, traffic) as needed.
4. Note nearby live webcams — occasionally useful for real-time context around a location.
5. Pivot: corroborate the imagery in `[[google-earth]]` / a first-party provider and cross-check webcam feeds separately.

## Inputs → Outputs
- **In:** `address` or `geolocation`.
- **Out:** satellite/aerial imagery and map overlays for that `geolocation`.
- **Empty/negative result looks like:** low-resolution or dated imagery for remote areas, or an address that doesn't resolve — fall back to a first-party map.

## Gotchas & OpSec
- Aggregator, not source: imagery comes from third-party providers and may be older/lower-res than first-party maps.
- Ads/trackers: it's ad-supported — use a clean, script-controlled browser.
- Low unique value: mostly a convenience layer over data available elsewhere.
- OpSec: passive; no target notification.

## Overlaps ("do both")
- Pairs with `[[google-earth]]` and other satellite/aerial tools — use Gosur for a fast look and overlays, first-party providers for authoritative, higher-resolution, dated imagery.

## Trust & verifiability
`trust: community` — a third-party front-end; treat its imagery as indicative and verify anything important against an authoritative mapping source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gosur-map |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | address, geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
