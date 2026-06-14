---
id: satellites-pro
name: Satellites Pro
description: Use when you have coordinates or a place and want a quick free web view of satellite imagery and map layers.
url: https://satellites.pro/
category: geolocation
path:
- geolocation
bestFor: Free browser satellite/hybrid map viewer for quickly inspecting a location's imagery and coordinates.
selectorsIn: [geolocation, address]
selectorsOut: [geolocation]
status: live
pricing: free
opsec: passive
opsecNote: Browsing a public map site; you only reveal your own access to the site, nothing about the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Consumer ad-supported satellite-map viewer aggregating provider tiles; fine for quick looks, not an authoritative imagery source.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
aliases: [Satellites.pro]
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Satellites Pro

> A free browser-based satellite and hybrid map viewer for quickly inspecting imagery at a set of coordinates or a named place.

## When to use
You have a `geolocation` (coordinates) or `address` and want a fast, no-install look at satellite/hybrid imagery — to eyeball terrain, buildings, or roads around a last-known location, or to read off coordinates for a place. A lightweight first look before pulling out heavier tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://satellites.pro/ and search the place or pan/zoom to your coordinates.
2. Toggle between satellite, map, and hybrid layers.
3. Read the coordinates and inspect the imagery (`geolocation`).
4. Pivot: for deeper analysis download imagery via `[[sas-planet]]`, compare recent scenes in `[[sentinel-hub]]`, or annotate in `[[scribblemaps]]`.

## Inputs → Outputs
- **In:** `geolocation`, `address`
- **Out:** satellite/map view and coordinates (`geolocation`)
- **Empty/negative result looks like:** stale or low-resolution tiles for the area — imagery freshness varies and is not labeled; do not assume it is current.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully passive; you only touch the map site. The target is never contacted.
- Imagery age is unknown and often dated; treat as orientation, not proof of current state.

## Overlaps ("do both")
- Redundant with mainstream map viewers; pair with `[[sentinel-hub]]` (dated recent scenes) and `[[sas-planet]]` (multi-provider downloads) when you need rigor.

## Trust & verifiability
`trust: community` — a consumer, ad-supported imagery viewer that re-serves provider tiles. Useful for quick looks; not an authoritative or dated imagery source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | satellites-pro |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
