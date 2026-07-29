---
id: index-database
name: Index DataBase (IDB)
description: Use when you have satellite/aerial imagery and need the right spectral index — a reference database of remote-sensing indices and the sensors/bands that compute them.
url: https://www.indexdatabase.de/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Looking up remote-sensing spectral indices (e.g. NDVI) and which satellite sensor bands are needed to compute them.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free academic reference database (University of Bonn); open browsing, no account.
opsec: passive
opsecNote: A public reference catalog of formulas and sensors — you look up indices, not a person or place-specific query, so there is zero target-facing footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Academic project (IDB, University of Bonn) cataloging peer-referenced remote-sensing indices; a citations-backed reference, not a data broker.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- IDB
- Index DataBase
- indexdatabase.de
tags:
- remote-sensing
- satellite-imagery
- spectral-index
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Index DataBase (IDB)

> An academic catalog of remote-sensing spectral indices — pick the right index (and the sensor bands it needs) to pull information out of satellite or aerial imagery.

## When to use
You are doing imagery analysis around a `geolocation` — assessing vegetation, water, burn scars, built-up areas, soil — and need to know which spectral index to apply and which satellite sensor/bands compute it. IDB is a lookup you consult *while* analyzing imagery: it tells you, for a given sensor (Landsat, Sentinel, etc.) or a given application, which indices exist and their formulas. It does not process imagery itself; it tells you how.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.indexdatabase.de/.
2. Browse by **application** (e.g. vegetation, water, soil) or by **sensor** (the satellite/instrument whose imagery you have).
3. Open an index entry to see its formula (the band arithmetic), the domain it is used for, and references.
4. Note which sensor bands you need, then apply that formula in your GIS/remote-sensing tool (QGIS, Google Earth Engine, etc.).
5. Pivot: the derived index layer helps interpret the scene at your `geolocation` — corroborating land-use, activity, or change over time relevant to a location-based lead.

## Inputs → Outputs
- **In:** the sensor you have imagery from, or the analytical goal at a `geolocation`
- **Out:** the matching spectral index/indices, their formulas, and required bands (to interpret imagery of that `geolocation`)
- **Empty/negative result looks like:** no index for a niche sensor/application — the instrument may be too new/obscure to be cataloged; fall back to the sensor vendor's technical docs.

## Gotchas & OpSec
- Human-in-the-loop: none; it is a reference you read, then apply elsewhere.
- OpSec: fully passive — a formula catalog, nothing about a target is transmitted.
- It is a *reference*, not an analysis engine: you still need imagery and a GIS/remote-sensing platform to actually compute and view the index.
- Index applicability depends on the sensor's bands — confirm your imagery has the required bands before relying on a formula.

## Overlaps ("do both")
- Complements imagery platforms (Sentinel Hub, Google Earth Engine, QGIS): IDB tells you *which* index and formula to use; those platforms let you compute and visualize it over your area of interest.

## Trust & verifiability
`trust: trusted` — an academic, citation-backed catalog of established indices; formulas are traceable to the literature and reproducible in any remote-sensing tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | index-database |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
