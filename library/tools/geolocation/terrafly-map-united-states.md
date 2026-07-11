---
id: terrafly-map-united-states
name: TerraFly Map (United States)
description: Use when you have a `geolocation`/`address` and want aerial/satellite imagery plus overlaid local point-data for that spot — returns imagery and `geolocation`/`address` context.
url: http://terrafly.com
category: geolocation
path:
- geolocation
bestFor: Viewing aerial/satellite imagery with overlaid demographic, property, and point-of-interest data for a US location.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free web map/geo-database from Florida International University's research lab; some advanced/bulk features are research- or API-oriented.
opsec: passive
opsecNote: Viewing maps and imagery is passive and reveals nothing to any subject. Standard map-service logging applies to your own queries; use a clean session if a location query is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Academic project (FIU's TerraFly/High Performance Database Research Center); imagery and overlays are aggregated from public/geo sources and may be dated.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- TerraFly
- terrafly.com
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# TerraFly Map (United States)

> An academic geo-database and map viewer — fly over an address with aerial/satellite imagery and toggle overlaid local data (demographics, property, points of interest).

## When to use
You have an `address` or `geolocation` and want to understand the place: what the aerial/satellite imagery shows, and what public point-data (property attributes, demographics, nearby POIs) is associated with it. Useful for scoping a location's physical layout and surroundings in the US — corroborating an address, assessing a rural/urban setting, or spotting features (outbuildings, access roads) relevant to a locate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://terrafly.com and navigate to the `address` or enter/drop a `geolocation`.
2. Pan/zoom the aerial and satellite imagery to inspect the location and surroundings.
3. Toggle the available data overlays (property, demographic, POI) to read local point-data for the spot.
4. Compare TerraFly's imagery date against other providers — imagery can be older than commercial maps.
5. Pivot: coordinates/address feed `[[google-earth]]`/`[[bing-maps]]` for fresher imagery and street-level views; property data feeds county assessor/property records.

## Inputs → Outputs
- **In:** `geolocation` or `address` (US)
- **Out:** aerial/satellite imagery and overlaid local point-data for that `geolocation`/`address`
- **Empty/negative result looks like:** sparse or dated imagery/overlays for the location — expected for rural areas and for a research-project map that isn't refreshed as often as commercial services. Missing overlay data ≠ nothing exists there.

## Gotchas & OpSec
- Imagery may be older than Google/Bing; always cross-date against a commercial provider before drawing conclusions.
- Strength is the *overlaid data*; as a plain map it's outclassed by mainstream services.
- US-focused despite the "worldwide imagery" billing.

## Overlaps ("do both")
- Pairs with `[[google-earth]]`, `[[bing-maps]]`, and county property/GIS portals — TerraFly adds data overlays and an alternate imagery date, while commercial maps give fresher, higher-res, street-level views.

## Trust & verifiability
`trust: community` — a credible academic project, but imagery/overlays are aggregated and can be dated; verify against current commercial imagery and authoritative property records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | terrafly-map-united-states |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
