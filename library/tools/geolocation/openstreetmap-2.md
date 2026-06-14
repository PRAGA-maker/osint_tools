---
id: openstreetmap-2
name: OpenStreetMap
description: Use when you need a free, detailed, query-able world basemap to identify or confirm a place by its tagged features, POIs, and geometry. (Duplicate of openstreetmap.)
url: https://www.openstreetmap.org/
category: geolocation
path:
- geolocation
bestFor: Open, community-mapped basemap with rich tagged features for confirming and pivoting on a location. (Duplicate entry — see openstreetmap.)
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
opsecNote: Browsing does not contact the subject. Automated tile/Nominatim/API use is rate-limited under fair-use. No target interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdsourced and openly auditable; coverage varies by region. This is a duplicate record of the canonical OpenStreetMap entry.
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
tags:
- geospatial-research-and-mapping-tools
- duplicate
source: arf-seed
lastVerified: ''
enrichment: full
---

# OpenStreetMap

> The free, editable world map with tagged features. This is a duplicate library record — the canonical entry is [[openstreetmap]]; deduplicate when convenient.

## When to use
Identical to [[openstreetmap]]: you have a candidate `geolocation`, `address`, or place `name` and want to identify/confirm a location by its tagged physical features (POIs, buildings, roads). Core to chronolocation and last-known-location work. Use the canonical entry; this record exists only because the harvest produced two.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to openstreetmap.org; search by name/address or pan/zoom to coordinates.
2. Click features to read tags; toggle overlays via the layers control.
3. Match POIs/landmarks/road geometry against your image or lead.
4. Pivot to [[overpass-turbo]] for bulk feature queries and to imagery/street-view tools to confirm.

## Inputs → Outputs
- **In:** `geolocation` / `address` / place `name`.
- **Out:** confirmed `geolocation` + `address` and a structured POI/feature picture.
- **Empty/negative result looks like:** sparse detail in under-mapped regions; absence in OSM is not absence on the ground.

## Gotchas & OpSec
- Duplicate of [[openstreetmap]] — consolidate to avoid double-counting in the index.
- Coverage uneven; verify decisive features against imagery. Respect API/tile rate limits.
- OpSec: passive; no subject contact.

## Overlaps ("do both")
- Same service as [[openstreetmap]]; pairs with [[overpass-turbo]] for programmatic extraction.

## Trust & verifiability
`trust: community` — crowdsourced, openly auditable data. Flagged as a duplicate record for housekeeping.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openstreetmap-2 |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address, name → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
