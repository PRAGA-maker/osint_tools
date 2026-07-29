---
id: gmapcatcher
name: gmapcatcher
description: Use when you have a `geolocation` and want to download and cache map tiles (Google/OSM/Bing) for offline browsing and archiving — returns image (map tiles) leads.
url: https://github.com/heldersepu/gmapcatcher
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Downloading and caching map tiles from multiple providers for offline map viewing and archiving.
selectorsIn:
- geolocation
selectorsOut:
- image
status: live
pricing: free
costNote: Free and open source; the README states it "is free and will always be." Python 2.7 + PyGTK.
opsec: passive
opsecNote: Downloading tiles fetches imagery from the map providers over your IP like any map user. Bulk downloads can trip provider rate limits and may breach a provider's terms of service — throttle, and prefer OSM tiles for unrestricted use. Local caching means you can then work offline with no further network exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Mature open-source project (heldersepu) with a long commit history, but built on Python 2.7/PyGTK — expect setup friction on modern systems.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- GMapCatcher
tags:
- offline-browsing
- maps
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# gmapcatcher

> An offline map viewer that downloads and caches tiles from Google/OSM/Bing and others — for browsing (and preserving) map imagery of an area without a live connection.

## When to use
You have a `geolocation` / area of interest and want a local, offline copy of its map imagery — to work in the field without connectivity, to archive how an area looked at collection time, or to batch-download tiles across a bounding box. Useful when you need map data to persist (providers change/remove imagery) or when your investigation must run air-gapped after collection. It caches tiles; it is not a live tracker or satellite-analysis tool.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Python 2.7 + PyGTK and clone the repo (or use a pre-built installer).
2. Launch the GUI: `python maps.py`, choose a tile provider (OSM/Google/Bing), and pan/zoom to your `geolocation`.
3. Enable "Force update" to refresh tiles older than 24h; tiles are cached locally as you browse.
4. For batch pulls, use the CLI `download.py` to fetch tiles across a region/zoom range without the GUI.
5. Pivot: archived tiles → offline field reference; compare cached imagery across dates to spot change.

## Inputs → Outputs
- **In:** a `geolocation` / bounding box + zoom range
- **Out:** cached map tiles (`image`) viewable offline
- **Empty/negative result looks like:** blank/missing tiles for an area — the provider has no tiles there at that zoom, or the download was rate-limited/blocked; retry with OSM or a lower zoom.

## Gotchas & OpSec
- Python 2.7/PyGTK stack — expect dependency friction on current OSes; consider a container/VM.
- Respect provider ToS — mass-downloading Google/Bing tiles may violate terms; OSM is the safe default.
- OpSec: passive but not invisible — downloads hit providers from your IP; throttle bulk jobs.

## Overlaps ("do both")
- Complements online mapping/satellite tools — gmapcatcher's niche is offline caching/archiving; use live web maps for current interactive work.

## Trust & verifiability
`trust: community` — mature, genuinely free open-source project; dated tech stack, so verify it installs cleanly before relying on it operationally.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gmapcatcher |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | geolocation → image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
