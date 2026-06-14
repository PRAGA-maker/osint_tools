---
id: open-street-map
name: Open Street Map
description: Use when you need a free, detailed, query-able world basemap to identify or confirm a place by its features, POIs, and tags — without vendor lock-in.
url: http://www.openstreetmap.org
category: geolocation
path:
- geolocation
bestFor: Open, community-mapped basemap with rich tagged features (POIs, buildings, paths) for confirming and pivoting on a location.
selectorsIn:
- geolocation
- address
- name
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free and open data (ODbL). No account needed to browse; editing requires a free OSM account.
opsec: passive
opsecNote: Browsing the map does not contact the subject. Heavy automated tile/Nominatim use has rate limits — respect them or self-host to avoid being blocked.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdsourced; coverage and freshness vary by region. Excellent in well-mapped areas, sparse in others — verify critical features.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- openstreetmap
- overpass-turbo
aliases:
- OSM
- OpenStreetMap
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Open Street Map

> The free, editable world map with tagged features — the geolocation analyst's default reference basemap and the data layer behind countless OSINT tools.

> Note: this entry duplicates [[openstreetmap]]; both point at the same service. Prefer one and treat the other as an alias.

## When to use
You have a candidate `geolocation`, an `address`, or a place `name`, and you need to identify or confirm a location by its physical features — building footprints, business POIs, road/path names, amenities. OSM's tagged data lets you match small details (a specific shop, a footbridge, a parking layout) that you see in a photo, making it core to chronolocation and last-known-location work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to openstreetmap.org and search by place name/address, or pan/zoom to coordinates.
2. Click features to read their tags (name, type, operator). Use the layers control for cycle/transport overlays.
3. Match POIs/landmarks/road geometry against your image or lead.
4. Pivot: jump to [[overpass-turbo]] to query "all features tagged X within this area," and cross-check imagery in Google/Bing/[[naver-korean]] satellite and street view.

## Inputs → Outputs
- **In:** `geolocation` / `address` / place `name`.
- **Out:** confirmed `geolocation` + `address` and a structured feature/POI picture of the area.
- **Empty/negative result looks like:** sparse or missing detail in an under-mapped region — absence of a feature in OSM does not prove it isn't there on the ground.

## Gotchas & OpSec
- Data quality is uneven; rural/developing areas may be thin. Cross-verify with imagery.
- Map data may lag reality (new construction, closures). Check the feature's edit history if it matters.
- Automated tile/Nominatim/API hits are rate-limited under fair-use; self-host or use a provider for volume.
- OpSec: passive; no subject contact.

## Overlaps ("do both")
- Pairs with [[overpass-turbo]] (programmatic feature extraction) and street-view tools like [[openstreetcam]] — OSM gives the tags, those give imagery and bulk querying.

## Trust & verifiability
`trust: community` — crowdsourced and openly auditable (every edit is attributed and versioned), but coverage varies, so confirm decisive features against independent imagery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-street-map |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address, name → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
