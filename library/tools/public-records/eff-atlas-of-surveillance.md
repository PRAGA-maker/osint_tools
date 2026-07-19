---
id: eff-atlas-of-surveillance
name: EFF Atlas of Surveillance
description: Use when you have a `geolocation`/`address` (city, county, agency) and want to know what surveillance technology local law enforcement operates there — returns the deploying `employer-org` and tech types.
url: https://atlasofsurveillance.org/
category: public-records
path:
- public-records
bestFor: Mapping which surveillance tech (ALPR, drones, face recognition, ring/cameras) a given US locality's police run — situational awareness for an investigation.
selectorsIn:
- geolocation
- address
- employer-org
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free public database from EFF; no account required. Bulk CSV export available.
opsec: passive
opsecNote: Entirely passive — you query EFF's own database, not any police or target system. Nothing about your subject is transmitted; you are only reading published records about agencies. No footprint reaches the locality.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by the Electronic Frontier Foundation with the University of Nevada Reno's Reynolds School of Journalism, compiled by 1,000+ students/volunteers from public/nonprofit sources; each data point is sourced.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Atlas of Surveillance
- EFF surveillance database
tags:
- surveillance
- law-enforcement
- public-records
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# EFF Atlas of Surveillance

> A sourced, searchable map of what surveillance tech US police departments deploy — so you know what public-safety data trail your locality-of-interest may already capture.

## When to use
You are working a case tied to a US city, county, or specific agency and need context on the surveillance infrastructure there: does the local PD run automated licence-plate readers (ALPR), drones, face recognition, gunshot detection, body cameras, or a Ring/camera-sharing programme? That tells you what official record-holders might exist (e.g. an ALPR hit places a vehicle) and who to approach through lawful channels.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://atlasofsurveillance.org/.
2. Search by city, county, state, or agency name, or explore the interactive map.
3. Read the output: each pin/row lists the agency (`employer-org`), the technology type, and a citation link to the source document.
4. Pivot: use the tech-type + agency to know which official data source might hold a lead (ALPR logs, camera networks), then pursue it via proper legal/records channels; download the CSV for bulk analysis across a region.

## Inputs → Outputs
- **In:** `geolocation` / `address` (city, county, state) or an `employer-org` (agency name)
- **Out:** deploying agencies (`employer-org`), technology categories, locations (`geolocation`), and source citations
- **Empty/negative result looks like:** no entries for a locality means *no documented* deployment — not proof none exists; absence of a record ≠ absence of tech.

## Gotchas & OpSec
- The database is a research snapshot; a deployment may have been added or removed since the last update — treat entries as leads and verify against the cited source.
- Human-in-the-loop: none.
- OpSec: passive. You never touch the agency; you read EFF's compiled records.

## Overlaps ("do both")
- Complements local public-records portals — Atlas tells you *what* tech an agency runs; the records portal is where you'd lawfully request the underlying data.

## Trust & verifiability
`trust: trusted` — EFF/UNR academic project with per-record source citations; the sourcing is the point, so cross-check each data point via its linked citation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eff-atlas-of-surveillance |
| category | public-records |
| selectorsIn → selectorsOut | geolocation, address, employer-org → employer-org, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
