---
id: gouvernement-du-qu-bec
name: Gouvernement du Québec
description: Use when you have an `employer-org`, `address`, or `geolocation` in Québec and want official open data — returns employer-org, address, and geolocation context from the province's data catalog.
url: https://www.donneesquebec.ca/organisation/gouvernement-du-quebec/
category: public-records
path:
- public-records
bestFor: Finding authoritative Québec government open datasets (business registries, addresses, geospatial, services) for a place or organization.
selectorsIn:
- employer-org
- address
- geolocation
selectorsOut:
- employer-org
- address
- geolocation
status: live
pricing: free
costNote: Free open-data portal (Données Québec); no account required to search or download datasets.
opsec: passive
opsecNote: Browsing and downloading published open datasets; no query concerns an individual and nothing is transmitted about a subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Government of Québec's organization page on Données Québec, the official provincial open-data platform — authoritative first-party government data.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: true
localInstall: false
registration: false
aliases:
- Données Québec
- Government of Quebec open data
tags:
- public-records
- open-data
- government-records
- quebec
source: osint4all
lastVerified: '2026-07-20'
enrichment: full
---

# Gouvernement du Québec

> The Government of Québec's catalog on Données Québec — the official provincial open-data platform, a source of authoritative datasets on businesses, addresses, and geography.

## When to use
Your investigation touches Québec and you need authoritative provincial data rather than a scraper: business/enterprise registers, address and civic-numbering datasets, geospatial layers, licences, or public-service directories. This is a *data-catalog* entry point (French-language) for corroborating an organization, a location, or a jurisdiction — context and verification, not direct person lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.donneesquebec.ca/organisation/gouvernement-du-quebec/ and browse or search the government's published datasets (interface is in French).
2. Filter by theme — enterprises, territory/addresses, transport, health, justice — matching your lead (`employer-org`, `address`, `geolocation`).
3. Open a dataset, read its schema/metadata, and query or download it (many expose an API/CSV/GeoJSON).
4. Extract the fields you need — registered businesses, civic addresses, coordinates.
5. Pivot: an enterprise record feeds the Registraire des entreprises for officers; an address feeds people-search for that locale.

## Inputs → Outputs
- **In:** `employer-org`, `address`, or `geolocation` (Québec context)
- **Out:** `employer-org` (registered entities), `address`, `geolocation` from official datasets
- **Empty/negative result looks like:** no dataset covers your specific query — the catalog holds aggregate/reference data, so individual-level lookups often need the linked source system instead.

## Gotchas & OpSec
- French-language interface and dataset docs; use precise Québec terminology.
- It's an open-data catalog, not a people-search — value is authoritative context on orgs/places, not names.
- Dataset freshness varies; check each dataset's update cadence.
- OpSec: fully passive; public open data.

## Overlaps ("do both")
- Complements Québec's Registraire des entreprises and national corporate registries: this catalogs the datasets, those resolve a company to its directors and filings.

## Trust & verifiability
`trust: trusted` — first-party Government of Québec open data; authoritative, with per-dataset metadata to check currency and scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gouvernement-du-qu-bec |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, address, geolocation → employer-org, address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
