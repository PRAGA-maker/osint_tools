---
id: inspire-geoportal
name: Inspire Geoportal
description: Use when you need official EU spatial datasets (boundaries, addresses, land use, transport) for a `geolocation` in a European member state.
url: http://inspire-geoportal.ec.europa.eu
category: geolocation
path:
- geolocation
bestFor: Discovering authoritative EU member-state geospatial datasets for an area.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free EU public-sector portal; no account.
opsec: passive
opsecNote: Searches public government dataset catalogues; nothing is sent to the target and no login is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official European Commission INSPIRE Geoportal aggregating member-state spatial data infrastructures under the INSPIRE Directive.
missingPersonsRelevance: medium
coverage:
- eu
auth: none
api: false
localInstall: false
registration: false
aliases:
- INSPIRE Geoportal
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Inspire Geoportal

> The European Commission's INSPIRE Geoportal — a catalogue of authoritative spatial datasets published by EU member states (boundaries, addresses, land use, transport, hydrography).

## When to use
Your `geolocation` of interest is in Europe and you need official, authoritative spatial reference data — administrative boundaries, address points, land cover, transport networks, protected sites — rather than crowdsourced or commercial maps. Useful for grounding a European search area in government data. Medium relevance: it's reference/context data, not people-finding.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the INSPIRE Geoportal and use the discovery/search to filter by theme (e.g., addresses, transport) and country/region.
2. Browse the catalogued datasets and view available ones in the map viewer.
3. Follow links to the member-state source service to download or query the data.
4. Bring boundary/terrain layers into [[grassgis]] for analysis or overlay them in a case map.

## Inputs → Outputs
- **In:** `geolocation` / `address` and a dataset theme + country filter
- **Out:** authoritative EU spatial datasets and map layers (`geolocation`)
- **Empty/negative result looks like:** themes with no published dataset for a given country, or links pointing to a member-state service that is offline — completeness varies by member state.

## Gotchas & OpSec
- It is a metadata/discovery catalogue; the actual data lives on member-state services of varying quality and availability.
- EU-only coverage.
- OpSec: passive — public dataset catalogues; no login, nothing sent to the target.

## Overlaps ("do both")
- Pairs with [[grassgis]] (analysis of the datasets you retrieve) and [[here-maps]] (interactive cross-check of the same area).

## Trust & verifiability
`trust: trusted` — an official European Commission portal; underlying data is authoritative, though coverage completeness differs by country.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inspire-geoportal |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
