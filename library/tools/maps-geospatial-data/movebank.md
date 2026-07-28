---
id: movebank
name: Movebank
description: Use when you have a species, region or research `geolocation` question and want animal-tracking datasets — returns tagged-animal movement tracks with timestamps and coordinates.
url: https://www.movebank.org/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Accessing scientific animal-movement (GPS/telemetry) datasets — useful for environmental investigations and as ground-truth geospatial reference, not for people-finding.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free research platform hosted by the Max Planck Institute of Animal Behavior; a free account is needed to download or contribute data, but many studies are browsable/openly licensed.
opsec: passive
opsecNote: Browsing and querying public datasets is passive and involves no target — this is a scientific data repository, not a surveillance tool. Data owners set access; some datasets require requesting permission.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Max Planck Institute of Animal Behavior with academic partners; datasets are peer/researcher-contributed with documented provenance.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- openaerialmap
aliases:
- Movebank.org
- Movebank animal tracking
tags:
- bellingcat-toolkit
- environment-wildlife
- geospatial
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Movebank

> A free, Max-Planck-run repository of animal-movement data — GPS/telemetry tracks of tagged animals — used in environmental and geospatial investigations, not people-search.

## When to use
This is a niche, subject-matter tool. Reach for it when an investigation has an **environmental or wildlife** dimension — e.g. corroborating a location or timeframe against known animal-migration data, sourcing scientific movement datasets for a story, or using tracked-animal tracks as an independent geospatial reference. It has essentially no role in finding people; keep expectations set to environmental/OSINT-journalism use.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.movebank.org/ and create a free account (needed to download or access restricted studies).
2. Use the map/Search to find studies by species, region (`geolocation`), researcher, or keyword.
3. Open a study to see its metadata: species, tagging period, area, owner, and license/access terms.
4. For open studies, view tracks on the map or download the movement data (timestamped coordinate tracks); for restricted studies, request access from the data owner.
5. Pivot: overlay tracks/timestamps against imagery (`[[openaerialmap]]`) or other geospatial layers to corroborate location/time claims.

## Inputs → Outputs
- **In:** a `geolocation`/region, species, or study keyword
- **Out:** `geolocation` (animal movement tracks: coordinates + timestamps) and dataset `metadata-exif` (provenance, tagging period, owner, license)
- **Empty/negative result looks like:** no studies match the species/region, or matching studies are access-restricted and show only metadata until the owner grants access.

## Gotchas & OpSec
- Human-in-the-loop: an account is required for downloads, and many datasets are permission-gated by the researcher who owns them.
- This is **scientific data about animals**, not people — do not overstate its investigative reach.
- Passive: no target is contacted; you're querying a public research archive.

## Overlaps ("do both")
- Pairs with `[[openaerialmap]]` and other imagery/geospatial layers — Movebank supplies movement tracks, imagery supplies the ground context to interpret them.

## Trust & verifiability
`trust: trusted` — hosted by the Max Planck Institute of Animal Behavior with documented dataset provenance and licensing; individual study quality varies by contributor, so check each study's metadata and terms.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | movebank |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
