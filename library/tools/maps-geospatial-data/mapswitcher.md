---
id: mapswitcher
name: MapSwitcher
description: Use when you have a `geolocation` open in one map service and want the same spot in 30+ other map providers — returns the same `geolocation` across Google, Bing, OSM, Yandex, Waze and more.
url: https://github.com/david-r-edgar/MapSwitcher
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: One-click pivoting of a map location or coordinates across dozens of mapping providers.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open-source browser extension; install from the Chrome Web Store or build from source.
opsec: passive
opsecNote: The extension reads the current map's coordinates locally and builds URLs for other providers — it phones no home server. But each map you then open is a normal request to that provider from your IP, so keep using a sock-puppet/VPN browser session for map recon.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source, listed in Bellingcat's Online Investigation Toolkit; maintained by David Edgar. Different providers geocode coordinates slightly differently, so expect minor offsets.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Map Switcher
tags:
- bellingcat-toolkit
- maps
- geolocation
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# MapSwitcher

> A browser extension that takes wherever you are on one map and instantly reopens the same point, zoom, and route in 30+ other mapping services.

## When to use
You're geolocating and have a `geolocation` (coords) or `address` displayed in one map provider, and you want to cross-reference the same spot across other imagery and layers — Yandex/Baidu for better coverage in some regions, Bing bird's-eye, Wikimapia labels, OSM detail, Waze for live traffic naming, Street View for ground truth. It removes the copy-paste-coordinates friction of switching between them.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from the Chrome Web Store, or clone `david-r-edgar/MapSwitcher`, run `npm run build`, and load the unpacked extension via `chrome://extensions/`.
2. Open any supported map (Google, Bing, OSM, etc.) and navigate to your point of interest.
3. Click the MapSwitcher toolbar icon — it reads the current centre/zoom (and directions, if set) and lists every other provider it can hand off to.
4. Click a provider to open that same location there in a new tab.
5. Pivot: use the alternate providers' imagery/labels to confirm a `geolocation`, read building/place names, or find higher-resolution or differently-dated satellite views.

## Inputs → Outputs
- **In:** `geolocation` (a map centred on a point) or `address`
- **Out:** the same `geolocation` opened across 30+ map services
- **Empty/negative result looks like:** the current site isn't a recognised source map, so MapSwitcher can't read coordinates — open the location in a supported provider first.

## Gotchas & OpSec
- Coordinate handoff is precise; **directions by address** may shift because providers geocode addresses differently — verify routes by coordinates.
- Not every provider supports directions — some only accept a base-map centre.
- OpSec: passive and local; the extension itself sends nothing, but the maps you open see your IP. Use your usual clean/VPN session.

## Overlaps ("do both")
- Pairs with any single-provider geolocation workflow — MapSwitcher is the connective tissue that lets you check a candidate point against every other provider's imagery in seconds.

## Trust & verifiability
`trust: community` — open-source and Bellingcat-listed; it only reformats coordinates between providers, so the trust question is really about each underlying map's own imagery accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapswitcher |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
