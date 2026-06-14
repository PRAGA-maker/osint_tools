---
id: kartograph
name: Kartograph
description: Use when you (as a developer) want to render custom interactive SVG maps from your own geodata — a map-making library, not a lookup tool.
url: http://kartograph.org
category: geolocation
path:
- geolocation
bestFor: Building custom interactive SVG maps from your own geospatial data (developer library).
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free and open source (Python + JavaScript libraries).
opsec: passive
opsecNote: Runs locally / in your own page against geodata you supply; nothing is sent to a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: unverified
trustNote: Kartograph (kartograph.py + kartograph.js, by Gregor Aisch) is a real open-source thematic SVG-mapping library, but it is long unmaintained (circa 2014) and may not run on modern toolchains. It is an authoring library, not an OSINT lookup.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- kartograph.py
- kartograph.js
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Kartograph

> An open-source library (Python + JavaScript) for rendering custom, interactive thematic SVG maps from your own geospatial data.

## When to use
Rarely for active casework. Kartograph is a developer tool for designing bespoke interactive maps (e.g., a styled regional map for a report) from shapefiles/geodata you already have. It does not search for people or places — relevance is low. Use it only if you are producing a custom map visualization and have the geodata in hand.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install kartograph.py (generates SVG from shapefiles) — note it targets an old Python 2 / GDAL era and likely needs adaptation.
2. Supply your boundary `geolocation` geodata and a config describing layers/projection.
3. Generate the SVG, then use kartograph.js to make it interactive in a web page.
4. The output is a presentation map; it produces no investigative leads.

## Inputs → Outputs
- **In:** your own `geolocation` geodata (shapefiles) + a layer/projection config
- **Out:** a custom interactive SVG map (`geolocation` visualization)
- **Empty/negative result looks like:** install/build failures on modern systems — the library is unmaintained and dependency-fragile.

## Gotchas & OpSec
- Unmaintained (circa 2014); expect dependency and Python-version issues.
- It is a map-authoring library, not a search/lookup tool — easy to over-rate.
- OpSec: passive and local — your geodata, your machine; nothing reaches a target.

## Overlaps ("do both")
- For no-code mapping use [[google-my-maps]] or [[gpsvisualizer]]; for analysis use [[grassgis]].

## Trust & verifiability
`trust: unverified` — a real, well-known open-source project historically, but abandoned and likely broken on current toolchains; verify it builds before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kartograph |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
