---
id: species-plus
name: Species+
description: Use when you have a species name and want its CITES/CMS legal-protection, trade-control and country-distribution status — returns geolocation (range countries) and document-id (listing) leads.
url: https://www.speciesplus.net/species
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Looking up a species' CITES/CMS/EU legal listing, trade restrictions, and range-country distribution.
selectorsIn:
- name
selectorsOut:
- geolocation
- document-id
status: live
pricing: free
costNote: Free public database developed by UNEP-WCMC with the CITES Secretariat; no account needed to search. A free API key is available for programmatic access.
opsec: passive
opsecNote: Fully passive — a public reference database. Searching a species reveals nothing about any person and touches only UNEP-WCMC's servers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official CITES/CMS species portal maintained by UNEP-WCMC; authoritative for legal listing and trade-control status.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Species+
- speciesplus.net
- CITES Species+
tags:
- bellingcat-toolkit
- environment-wildlife
- cites
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# Species+

> The authoritative CITES/CMS species database from UNEP-WCMC — legal protection status, trade controls, and range-country distribution for internationally regulated wildlife.

## When to use
You have a species (common or scientific `name`) — from a seized shipment, a suspect's inventory, an image, or a wildlife-trafficking lead — and need its legal standing: is it CITES-listed (Appendix I/II/III), CMS-listed, or EU-regulated, and what trade restrictions apply. It also gives the species' distribution (range countries), which places a specimen geographically. Core reference for environmental/wildlife-crime investigations; not a people-search tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.speciesplus.net/species.
2. Search by scientific or common name (filters for taxonomy, CITES/CMS/EU listing available).
3. Open the species record: CITES appendix and history, CMS listing, EU regulation status, and the distribution (range countries) tab.
4. For bulk/automated work, request a free Species+ API key and query programmatically.
5. Pivot: range countries → map the legal source/transit geography; listing/appendix → assess whether a trade is illegal and which enforcement regime applies.

## Inputs → Outputs
- **In:** species `name` (common or scientific)
- **Out:** CITES/CMS/EU listing and history (`document-id`-style legal references), trade controls, range-country `geolocation` distribution
- **Empty/negative result looks like:** no match (misspelled/synonym name, or a species not internationally listed) — try the scientific name or a synonym; absence of a listing means it isn't CITES/CMS-regulated, not that it doesn't exist.

## Gotchas & OpSec
- Covers internationally regulated species only; purely domestic-protected species may not appear.
- Taxonomy/synonyms matter — search the accepted scientific name if a common name fails.
- OpSec: fully passive public reference; no exposure.

## Overlaps ("do both")
- Complements GBIF/iNaturalist occurrence data and national wildlife registries — Species+ gives the legal/trade status; occurrence databases give observed locations.

## Trust & verifiability
`trust: trusted` — official UNEP-WCMC/CITES portal; authoritative for legal listing and trade-control status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | species-plus |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | name → geolocation, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
