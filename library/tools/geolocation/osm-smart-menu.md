---
id: osm-smart-menu
name: OSM Smart Menu
description: Use when you have a `geolocation` open in one map/OSM page and want to jump to the same spot in dozens of other maps and OSM tools — a browser extension that carries the current coordinates/zoom (or OSM element) across services in one click.
url: https://chromewebstore.google.com/detail/osm-smart-menu/icipmdhgbkejfideagkhdebiaeohfijk
category: geolocation
path:
- geolocation
bestFor: One-click switching between map services and OpenStreetMap tools while preserving the current location, zoom, or OSM element.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free browser extension (Chrome/Firefox); no account. Developer states no data is sold or transferred.
opsec: passive
opsecNote: The extension reads the map parameters (lat/long/zoom, OSM IDs) from the page you're on and builds links locally; it doesn't transmit your target anywhere. As with any extension, install only from the official store and review its permissions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source OpenStreetMap-community extension (by jgpacker) with a small user base; it manipulates URL parameters locally and is inspectable, but adoption is modest.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- OSM Smart Menu
tags:
- openstreetmap
- maps
- browser-extension
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# OSM Smart Menu

> A small OpenStreetMap-community browser extension that detects the coordinates/zoom (or the node/way/relation) on the page you're viewing and offers one-click links to the same location across dozens of other maps and OSM tools — a time-saver when cross-referencing imagery.

## When to use
You are geolocating and want to view a single `geolocation` across multiple providers fast — comparing the same coordinates in OSM, satellite/aerial layers, historical imagery, and specialist OSM tools without hand-editing URLs or re-typing lat/long each time. It shines during imagery cross-verification, where seeing the exact spot in several map sources quickly confirms or kills a hypothesis.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "OSM Smart Menu" from the Chrome Web Store (link above) or the Firefox add-ons site.
2. Navigate to any supported map page (e.g. openstreetmap.org) centred on your `geolocation`, or an OSM object page.
3. Click the extension icon — it reads the current coordinates/zoom (or the OSM element ID) and shows a menu of related maps and tools pre-loaded to that same location.
4. Pick a service to open the identical spot there; repeat to compare across sources.
5. Pivot: corroborating a location across map/imagery services strengthens a geolocation before you commit to it.

## Inputs → Outputs
- **In:** `geolocation` (coordinates/zoom, or an OSM element) present on the current page
- **Out:** `geolocation` — the same point/element opened in another map or OSM tool
- **Empty/negative result looks like:** an empty or short menu when the current page exposes no recognisable map parameters — navigate to a proper map view first so the extension has coordinates to read.

## Gotchas & OpSec
- Human-in-the-loop: none beyond clicking; it's a convenience layer.
- OpSec: **passive** — it constructs links locally from the page's parameters and doesn't phone home; still, install only the official build and check requested permissions.
- Scope: it's oriented to the OpenStreetMap ecosystem and supported services, not every commercial map; it speeds up switching rather than adding new data.

## Overlaps ("do both")
- Pairs with multi-map geolocation utilities (e.g. map-switcher tools, [[localfocus-nl-geokit]] for coordinate conversion) — this handles fast in-browser hopping between viewers, while coordinate/reprojection tools handle turning raw location data into the values those viewers expect.

## Trust & verifiability
`trust: community` — an open-source, inspectable OSM-community extension of modest adoption; it only rewrites URL parameters you can see, so there's no hidden data-quality risk, though it's a smaller project than the mainstream mapping tools.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osm-smart-menu |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
