---
id: openstreetmap
name: OpenStreetMap
description: Use when you need a free, detailed, query-able world basemap to identify or confirm a place by its tagged features, POIs, and geometry.
url: https://www.openstreetmap.org/
category: geolocation
path:
- geolocation
bestFor: Open, community-mapped basemap with rich tagged features (POIs, buildings, roads) for confirming and pivoting on a location.
selectorsIn:
- geolocation
- address
- name
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free and open data (ODbL). Browsing needs no account; editing requires a free OSM account.
opsec: passive
opsecNote: Browsing does not contact the subject. Automated tile/Nominatim/API use is rate-limited under fair-use; respect limits or self-host. No target interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdsourced and openly auditable (versioned, attributed edits); coverage and freshness vary by region, so verify decisive features against imagery.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- overpass-turbo
- openstreetcam
- openinfrastructuremap
aliases:
- OSM
tags:
- geospatial-research-and-mapping-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# OpenStreetMap

> The free, editable world map with tagged features — the analyst's default reference basemap and the data layer behind much of the OSINT geo toolchain.

> Note: duplicated by [[open-street-map]] and [[openstreetmap-2]]; all point to the same service. Prefer this canonical entry.

## When to use
You have a candidate `geolocation`, an `address`, or a place `name`, and need to identify or confirm a location by its physical features — building footprints, business POIs, road/path names, amenities. OSM's tagging lets you match fine details (a specific shop, a footbridge, a parking layout) seen in a photo, making it core to chronolocation and last-known-location work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to openstreetmap.org and search by name/address, or pan/zoom to coordinates.
2. Click features to read tags (name, type, operator); use the layers control for transport/cycle overlays.
3. Match POIs, landmarks, and road geometry against your image or lead.
4. Pivot: use [[overpass-turbo]] to query "all features tagged X in this area," and cross-check imagery in satellite/street-view tools ([[openstreetcam]], [[naver-korean]] for Korea).

## Inputs → Outputs
- **In:** `geolocation` / `address` / place `name`.
- **Out:** confirmed `geolocation` + `address` and a structured feature/POI picture of the area.
- **Empty/negative result looks like:** sparse detail in an under-mapped region — absence of a feature in OSM does not mean it isn't there on the ground.

## Gotchas & OpSec
- Data quality is uneven; rural/developing areas can be thin. Cross-verify with imagery.
- Map data may lag reality (new construction, closures); check a feature's edit history when it matters.
- Automated API/tile/Nominatim hits are rate-limited under fair-use; self-host for volume.
- OpSec: passive; no subject contact.

## Overlaps ("do both")
- Pairs with [[overpass-turbo]] (programmatic feature extraction), [[openstreetcam]] (ground imagery), and [[openinfrastructuremap]] (infrastructure layer).

## Trust & verifiability
`trust: community` — crowdsourced but fully auditable (every edit attributed and versioned); confirm decisive features against independent imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openstreetmap |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address, name → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
