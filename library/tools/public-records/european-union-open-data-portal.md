---
id: european-union-open-data-portal
name: European Union Open Data Portal
description: Use when you need official EU datasets — sanctions lists, company/funding records, statistics, geospatial data — for a subject or entity — returns structured open data.
url: http://open-data.europa.eu/en/data
category: public-records
path:
- public-records
bestFor: Searching 1.5M+ official EU datasets (sanctions, CORDIS funding, statistics, geospatial) from one portal.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Completely free; no account needed to search or download (optional EU Login for extras).
opsec: passive
opsecNote: Querying a public open-data portal is passive and anonymous — no login required and the subject is not contacted. Standard browser hygiene (VPN/puppet) suffices for sensitive research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official portal managed by the Publications Office of the European Union; datasets are authoritative primary sources from EU institutions and member states.
missingPersonsRelevance: low
coverage:
- eu
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- e-justice-europa-eu
- eu-consolidated-corporate-registers
- eu-sanctions-tool
- europa-eu
- europa-press-releases
- european-commission-home-affairs
- eurostat
- frontex-migratory-map
- inspire-geoportal
- vat-number-validation
aliases:
- data.europa.eu
- EU Open Data Portal
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# European Union Open Data Portal

> The official EU open-data hub (data.europa.eu) — 1.5M+ datasets from EU institutions and 36 countries, including sanctions lists, research funding, corporate and statistical records.

## When to use
You're researching a person, company or funding trail with a European dimension and need authoritative, citable data: EU financial-sanctions lists, CORDIS records of who received EU research grants, corporate/VAT references, statistics, and geospatial datasets. This portal federates them so you can search across catalogues instead of hunting each institution's site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://data.europa.eu/en.
2. Use quick search, or advanced/geospatial/SPARQL search, to query by `name`, `employer-org`, keyword, country, or theme.
3. Filter by catalogue, country, format and theme to narrow to the authoritative dataset.
4. Open the dataset page for its description, provenance, and download/API links (CSV, JSON, RDF, SPARQL endpoint).
5. Pivot: an org in a funding or sanctions record (`employer-org`, `address`) feeds corporate-registry and sanctions tools like `[[eu-consolidated-corporate-registers]]` and `[[eu-sanctions-tool]]`.

## Inputs → Outputs
- **In:** a `name`, `employer-org`, keyword, country or theme
- **Out:** structured datasets — sanctioned entities, funded organisations (`employer-org`, `address`), statistics, geospatial layers
- **Empty/negative result looks like:** a niche query may match no dataset, or match dataset *metadata* rather than a record about your subject — the portal indexes datasets, so you often download a dataset and search within it.

## Gotchas & OpSec
- It's a catalogue of datasets, not a person-search: results point you to a dataset you then open/filter, not to a ready answer about an individual.
- Data currency varies by publisher; check each dataset's last-update and provenance.
- OpSec: passive and anonymous — no login needed.

## Overlaps ("do both")
- Pairs with `[[eu-sanctions-tool]]`, `[[eu-consolidated-corporate-registers]]` and `[[eurostat]]` — this portal is the broad index; those are the specialist front-ends for sanctions, company filings and statistics respectively.

## Trust & verifiability
`trust: trusted` — an official EU government portal aggregating primary-source datasets from EU institutions and member states, each with documented provenance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | european-union-open-data-portal |
