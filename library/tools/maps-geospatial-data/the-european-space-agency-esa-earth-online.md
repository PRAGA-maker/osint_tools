---
id: the-european-space-agency-esa-earth-online
name: The European Space Agency (ESA) - Earth Online
description: Use when you have a `geolocation`/`address` and want satellite Earth-observation imagery and environmental data for that area — returns EO imagery and datasets.
url: https://earth.esa.int/eogateway/tools
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Accessing ESA satellite/Earth-observation imagery and environmental datasets for a location or time window.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free access to a large catalogue of ESA Earth-observation data; a free EO Sign-In account is required to order/download many products.
opsec: passive
opsecNote: You browse ESA's public data portal, not any target — the subject is never contacted. Downloading generally requires a (free) ESA account, so use a research identity if you don't want the activity tied to you.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official European Space Agency portal; the imagery and data are authoritative primary sources from ESA missions.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- ESA Earth Online
- EO Gateway
tags:
- bellingcat-toolkit
- satellite-imagery
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# The European Space Agency (ESA) - Earth Online

> ESA's official Earth-observation portal — browse and download satellite imagery and environmental datasets for anywhere on the planet from an authoritative source.

## When to use
You have a `geolocation` or `address` and need satellite imagery or environmental data for it — to check what a place looked like on/around a date, assess terrain, or corroborate a scene. Strongest for area/scene analysis and disaster/land-change assessment; low direct missing-persons relevance but valuable when a case turns on where something happened rather than who.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://earth.esa.int/eogateway/ and use the EO Gateway catalogue/tools.
2. Search by area of interest (draw a box or enter coordinates/place) and, where offered, a date range and mission/sensor.
3. Browse the matching products (optical, radar, atmospheric, etc.).
4. To order/download, sign in with a free ESA EO account (registration required for many datasets).
5. Pivot: bring downloaded imagery into a GIS/mapping tool to compare dates or measure features.

## Inputs → Outputs
- **In:** `geolocation` / `address` (+ optional date/mission)
- **Out:** satellite/EO imagery and environmental datasets for that area (`geolocation`-referenced)
- **Empty/negative result looks like:** no products for your exact spot/date — coverage, revisit cadence and cloud cover vary by mission; widen the date window or try a different sensor rather than concluding no data exists.

## Gotchas & OpSec
- Human-in-the-loop: a free ESA EO Sign-In account is needed to order/download most products.
- OpSec: **passive** toward any subject; you're pulling public science data. Use a research account for the login.
- Resolution and revisit time are coarser than commercial satellite providers — good for context and change-over-time, not for reading fine detail like faces or plates.

## Overlaps ("do both")
- Complements commercial/basemap imagery services — use ESA for authoritative, dated, free EO layers and pair with a higher-resolution provider when you need finer detail.

## Trust & verifiability
`trust: trusted` — an official ESA portal serving primary mission data; imagery provenance and dating are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-european-space-agency-esa-earth-online |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
