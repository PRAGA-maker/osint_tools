---
id: regional-municipality-of-durham
name: Regional Municipality of Durham — Open Data
description: Use when a case touches Durham Region (Ontario, Canada) and you need geospatial/municipal context — returns open datasets (boundaries, facilities, addresses) as `geolocation`/`address` context.
url: https://opendata.durham.ca/
category: public-records
path:
- public-records
bestFor: The Durham Region (Ontario) open-data portal — municipal and geospatial datasets (boundaries, facilities, transit, addresses) for local context and mapping.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free open-government data portal; download/API access open, no account required for public datasets.
opsec: passive
opsecNote: Passive — you download aggregate municipal/geospatial datasets, not individual person records. No target interaction and no subject-alerting. This is context data (facilities, boundaries, infrastructure), not a personal-record lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official open-data portal of the Regional Municipality of Durham; datasets are government-published, though coverage is municipal/geospatial rather than personal.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: true
localInstall: false
registration: false
aliases:
- Durham Region open data
- opendata.durham.ca
tags:
- open-data
- geospatial
- canada
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Regional Municipality of Durham — Open Data

> Durham Region's (Ontario, Canada) open-government data portal — municipal and geospatial datasets for grounding a case in local geography, not a people-search.

## When to use
Your case touches Durham Region (Oshawa, Whitby, Ajax, Pickering, and surrounding municipalities east of Toronto) and you need geographic or municipal context: administrative boundaries, address points, facilities and services, transit, parks, infrastructure. Use it to map an area, locate the nearest facilities to an `address`, or understand the geography around a lead — it returns datasets, not individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://opendata.durham.ca/ and browse or search the dataset catalogue.
2. Pick a relevant layer (e.g. address points, ward/boundary layers, facilities, transit).
3. View it on the map, or download (CSV/GeoJSON/Shapefile) or hit the dataset API for analysis.
4. Overlay with your own coordinates/`address` to derive context (jurisdiction, nearby services).
5. Pivot: an `address` confirmed to a municipality → that municipality's/county's property and records systems; boundary data → correct jurisdiction for further requests.

## Inputs → Outputs
- **In:** a Durham-area `geolocation`/`address` (to contextualise), or a dataset of interest
- **Out:** geospatial/municipal datasets — boundaries, address points, facilities (`geolocation`/`address` context)
- **Empty/negative result looks like:** no dataset for what you want — open-data portals publish selected layers only; personal records (owners, residents) are deliberately not here. Absence of a layer isn't a dead end; go to the relevant records office.

## Gotchas & OpSec
- **Not a personal-records source** — it holds aggregate/geospatial data, no owner or resident lookups.
- Region-scoped to Durham; neighbouring regions have their own portals.
- Datasets have publish/update cycles; check each layer's currency.

## Overlaps ("do both")
- Complements Ontario land-registry and municipal property tools — this gives the geographic/jurisdictional context, those return the person-level property records for the same location.

## Trust & verifiability
`trust: trusted` — official government open data; datasets are authoritative and citable, with the caveat that this is context, not individual records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | regional-municipality-of-durham |
| category | public-records |
| selectorsIn → selectorsOut | geolocation, address → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
