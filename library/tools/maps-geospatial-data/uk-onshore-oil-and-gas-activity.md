---
id: uk-onshore-oil-and-gas-activity
name: UK Onshore Oil and Gas Activity
description: Use when you have a `geolocation`/`address` in Great Britain and want to know the petroleum licences, wells and operators active there — returns licence areas, well sites and the `employer-org`s that hold them.
url: https://www.arcgis.com/apps/webappviewer/index.html?id=29c31fa4b00248418e545d222e57ddaa
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Mapping onshore petroleum licences (PEDLs), wells and their operators across England, Scotland and Wales.
selectorsIn:
- geolocation
- address
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free public map published by the North Sea Transition Authority (NSTA, formerly the Oil & Gas Authority); no account.
opsec: passive
opsecNote: Static government web map served from ArcGIS; browsing it reveals nothing to any subject. Standard ArcGIS/Esri request logging applies but there is no target-side exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official NSTA (UK government regulator) map layer; the licence, well and operator data is authoritative regulatory record.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- NSTA Onshore Oil and Gas Activity
- Onshore Oil and Gas Activity map
tags:
- maps
- energy-infrastructure
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# UK Onshore Oil and Gas Activity

> The NSTA's official interactive map of onshore petroleum licences (PEDLs), wells and operators across Great Britain — who is licensed to explore/produce oil and gas, and where.

## When to use
You are working a case that touches an onshore energy site in England, Scotland or Wales — a `geolocation`/`address` near a well pad, a fracking-protest context, a company you're linking to extraction activity — and you need the authoritative answer to "what petroleum licence covers this ground and which operator holds it." The map ties a physical location to a Petroleum Exploration and Development Licence (PEDL) and the `employer-org` responsible.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the map in a modern browser (the ArcGIS viewer requires Chrome/Firefox/Edge/Safari, not a legacy browser).
2. Pan/zoom to the area of interest, or search an address/place.
3. Toggle layers — licence blocks (PEDLs), well locations, and activity stage — from the layer list.
4. Click a feature to open its pop-up: licence reference, operator name, well status/decommissioning stage.
5. Pivot: the operator `employer-org` feeds a Companies House / corporate-registry lookup; the licence reference feeds NSTA's open-data portal for the full dataset.

## Inputs → Outputs
- **In:** `geolocation` / `address` (an onshore GB location)
- **Out:** overlapping PEDL licence area(s), well site `geolocation`s, and the operator `employer-org`
- **Empty/negative result looks like:** no licence polygon and no wells under the point — meaning no licensed onshore petroleum activity there (a PEDL grants search/extraction rights only in specific Ordnance Survey blocks).

## Gotchas & OpSec
- A PEDL grants the *right* to explore/produce in a block but not automatic permission to drill — actual operations still need Local Authority planning, an Environment Agency permit and HSE scrutiny, so a licence area is not proof of active drilling.
- The ArcGIS viewer is JavaScript-heavy and needs a current browser; it won't render in a headless/legacy fetch.
- OpSec: passive — a public regulator map with no target-side visibility.

## Overlaps ("do both")
- Pairs with a corporate registry (Companies House) — this map names the operator, and the registry turns that `employer-org` into directors, addresses and ownership. Also pairs with NSTA's open-data portal for the raw downloadable dataset behind the map.

## Trust & verifiability
`trust: trusted` — published by the North Sea Transition Authority, the UK's onshore/offshore petroleum regulator, so the licence and operator data is authoritative regulatory record rather than a third-party estimate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uk-onshore-oil-and-gas-activity |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → employer-org, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
