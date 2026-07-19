---
id: terra-server
name: TerraServer
description: Use when you have a `geolocation`/`address` and want aerial/satellite imagery and topo maps — free to search and view online, paid to download high-res; returns imagery for a location.
url: https://www.terraserver.com
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Viewing aerial photos, satellite images, and USGS topo maps for a location (free online preview; purchase for downloads/prints).
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to search and view imagery online; downloading high-resolution images or prints is paid.
opsec: passive
opsecNote: Passive — you view imagery of a location, not a person; nothing reaches any subject. Buying a download ties a purchase to you; for pure viewing, no account is needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running commercial imagery reseller (since 1997); the imagery is real and sourced, but it is a paid-download vendor — free access is view/preview only.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- TerraServer.com
tags:
- maps
- satellite-imagery
- aerial
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# TerraServer

> A large aerial/satellite imagery and topo-map library — free to search and view a location, paid to download high-resolution copies.

## When to use
You have a `geolocation`/`address` and want to see it from above — aerial photos, satellite imagery, or USGS topo maps — for terrain context, structure/parcel detail, or historical comparison. Free online viewing is enough for most OSINT triage; buy a download only if you need a high-res image or print.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.terraserver.com/.
2. Search by address or coordinates, or navigate the map.
3. View the available imagery/topo layers online for free.
4. Pivot: cross-reference with free mappers (Google Earth, Bing Maps, Sentinel Hub) for current/multi-date coverage; purchase only if a high-res download is essential.

## Inputs → Outputs
- **In:** a `geolocation` / `address`
- **Out:** aerial/satellite imagery and topo maps for that location (view free; download paid)
- **Empty/negative result looks like:** sparse imagery for remote areas, or only a low-res preview — fall back to free global imagery providers.

## Gotchas & OpSec
- **Freemium:** viewing is free, but high-res downloads/prints cost money — use free mappers first.
- Imagery dates vary; check the capture date before drawing conclusions.
- Human-in-the-loop: none for viewing. OpSec: passive.

## Overlaps ("do both")
- Do both with Google Earth / Sentinel Hub — those give free current and multi-date imagery; TerraServer adds an aerial/topo archive and print-quality options.

## Trust & verifiability
`trust: community` — a commercial imagery vendor; the imagery is authentic, but confirm dates/sources and prefer free providers for routine viewing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | terra-server |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
