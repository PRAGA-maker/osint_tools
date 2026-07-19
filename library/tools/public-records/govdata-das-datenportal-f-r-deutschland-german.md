---
id: govdata-das-datenportal-f-r-deutschland-german
name: GovData — Das Datenportal für Deutschland
description: Use when you have a German place, agency or `employer-org` and want official open datasets — returns administrative, geographic and statistical data with source metadata.
url: https://www.govdata.de/
category: public-records
path:
- public-records
bestFor: Searching Germany's official open-government data portal for administrative, municipal and geographic datasets.
selectorsIn:
- employer-org
- address
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free, openly-licensed government open-data portal; no account needed to search or download (licences noted per dataset).
opsec: passive
opsecNote: Anonymous browsing/downloading of published open-government data. No login, nothing written, no subject notification. This is aggregate/administrative data, not a person-lookup, so re-identification risk is low but check each dataset's licence before republishing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official portal operated for the German federal, state and municipal administrations; datasets are published by government bodies, so provenance is authoritative (individual dataset accuracy still depends on the publishing agency).
missingPersonsRelevance: low
coverage:
- de
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- GovData
- Datenportal für Deutschland
tags:
- open-data
- germany
- government-portal
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# GovData — Das Datenportal für Deutschland

> Germany's official open-government data portal — 150,000+ administrative, geographic and statistical datasets from federal, state and municipal bodies, searchable and free.

## When to use
Your case has a German geographic, municipal, or organizational angle and you need authoritative context: which agency covers an area, municipal registers and planning data, geographic/address reference layers, statistics that frame a location. GovData is a metadata catalog over the whole German administration, so it points you to the primary dataset (and the agency that publishes it). It is aggregate/administrative data — useful for grounding a location or organization, not for looking up a named individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.govdata.de/ and search by keyword, place, or category (or use advanced search and the German-state filter).
2. Filter to the region or theme you need; open a dataset to read its metadata, publisher, licence, and download links.
3. Download the data (or hit the SPARQL/API endpoint for programmatic queries) and note the publishing agency as a lead.
4. Pivot: the responsible agency becomes an `employer-org`/office contact; geographic layers help resolve or confirm an `address`/area.

## Inputs → Outputs
- **In:** a German place, theme, or `employer-org` (agency/municipality)
- **Out:** open datasets + metadata (publisher, licence, geographic coverage) confirming an `employer-org`/`address` context
- **Empty/negative result looks like:** no matching dataset — meaning nothing is published openly for that query, not that the underlying record doesn't exist (many German records sit behind agency-specific request processes).

## Gotchas & OpSec
- Human-in-the-loop: none for search; some datasets link out to agency portals with their own access steps.
- It's a catalog of datasets, not a people-search — do not expect individual PII.
- Interface and most metadata are in German; use category filters and machine translation.
- Check each dataset's licence (`Datenlizenz Deutschland`, CC, etc.) before reuse.

## Overlaps ("do both")
- Pairs with the EU open-data portal and German commercial-register (Handelsregister) tools — this catalogs administrative datasets, those cover EU-wide data and company filings respectively.

## Trust & verifiability
`trust: trusted` — official German government open-data portal; provenance is authoritative, though each dataset's accuracy and freshness depend on its publishing agency.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | govdata-das-datenportal-f-r-deutschland-german |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, address → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
