---
id: data-gov
name: Data.gov
description: Use when you need an official US government dataset (federal, some state/local) — a free searchable catalog of 300k+ open datasets by keyword and organisation.
url: https://www.data.gov/
category: public-records
path:
- public-records
bestFor: Finding authoritative US federal (and some state/local) open datasets — geospatial, regulatory, demographic — to corroborate or contextualise an investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free; no registration to search or download.
opsec: passive
opsecNote: A public data catalog — you search datasets, not people. Fully passive with nothing disclosed about any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The US government's official open-data portal; datasets come from federal agencies, so provenance is authoritative (though individual datasets vary in freshness).
missingPersonsRelevance: low
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- data.gov
- US open data catalog
- catalog.data.gov
tags:
- open-data
- government
- public-records
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Data.gov

> The US government's official open-data catalog — 300k+ federal (and some state/local) datasets, searchable and free.

## When to use
You need an authoritative government dataset to support an investigation — geospatial layers, regulatory filings, licensing, demographic or economic data — and want to find it in one catalog rather than agency-hopping. This is a source-of-datasets, not a people-search; its value is corroboration and context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.data.gov/ (catalog at catalog.data.gov).
2. Search by keyword and filter by organisation (agency), format, tags, or geospatial location.
3. Open a dataset for its description, publisher, update cadence and download/API links.
4. Download the data (CSV/GeoJSON/API) and note the agency and last-updated date.
5. Use it to contextualise or verify a claim; for a specific record, follow through to the owning agency's system.

## Inputs → Outputs
- **In:** none (keyword/agency search)
- **Out:** links to official datasets and their download/API endpoints
- **Empty/negative result looks like:** no dataset matches — the data may live only in an agency's own system, or not be published openly; check the agency directly.

## Gotchas & OpSec
- It catalogs datasets, not individual people; it will rarely name a specific person.
- Dataset freshness varies widely — always check the update date and owning agency.
- Coverage is US-centric (federal, with some state/local).

## Overlaps ("do both")
- Overlaps with agency-specific portals and other national open-data catalogs — Data.gov is the front door, but the authoritative live record often lives in the agency's own system.

## Trust & verifiability
`trust: trusted` — official government catalog; provenance is authoritative, though you should confirm each dataset's currency at the source agency.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | data-gov |
