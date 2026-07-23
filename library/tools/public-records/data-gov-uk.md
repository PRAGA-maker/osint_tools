---
id: data-gov-uk
name: Data.gov.uk
description: Use when you have a UK `name`, `employer-org`, `address` or place and want official open datasets about it — returns government records on companies, property, spending, transport and population.
url: https://data.gov.uk
category: public-records
path:
- public-records
bestFor: Searching UK government open datasets (business, land/property, spending, transport, people).
selectorsIn:
- employer-org
- address
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free under the Open Government Licence v3.0; no account required to search or download most datasets.
opsec: passive
opsecNote: You query a UK government open-data portal, not the subject; nothing about your target is revealed to them. Standard sock-puppet browsing applies. Datasets are official public records, so citations are authoritative.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official UK government open-data portal; datasets are primary-source public records published by departments and public bodies.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: true
localInstall: false
registration: false
aliases:
- data.gov.uk
- National Data Library
tags:
- data-and-statistics
- open-data
- uk-government
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Data.gov.uk

> The UK government's open-data portal: thousands of official datasets on business, land, spending, transport and people, free to search and download.

## When to use
You're working a UK subject or place and want authoritative, citable public data behind it: company/business and economic records, land and property (ownership, planning, addresses), local-government finance and spending, transport, and population/health statistics. Data.gov.uk aggregates datasets published by UK departments and public bodies — the primary-source layer to confirm an `employer-org`, an `address`/property, or the official context around a person or organisation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://data.gov.uk and search by keyword, organisation, or place; or browse the topic collections (Business, Land & property, Government, People, Transport, Environment).
2. Open a dataset to see its publisher, coverage, update frequency, and download formats (CSV, API, etc.).
3. Download or query the data; many datasets expose an API or bulk file for offline analysis.
4. Read the licence (Open Government Licence) — reuse is permitted with attribution.
5. Pivot: a company/property record corroborates an `employer-org`/`address`; combine with Companies House and Land Registry for the full picture.

## Inputs → Outputs
- **In:** a keyword, `employer-org`, `address`/place, or publishing body
- **Out:** official datasets — business/economic records, property/planning, spending, transport, population — as `employer-org`/`address`-linked data
- **Empty/negative result looks like:** no matching dataset — the topic isn't published as open data (much personal-level data isn't, for privacy); absence means "not an open dataset", not "no record exists".

## Gotchas & OpSec
- It's aggregate/organisational open data, not a person-lookup — you won't find individuals directly (by design/privacy).
- Dataset freshness varies widely; check each dataset's last-updated date before relying on it.
- Some entries are metadata pointing to another host — follow through to the actual publisher.
- OpSec: fully passive; no target exposure.

## Overlaps ("do both")
- Pairs with UK company/property registries (Companies House, Land Registry) — data.gov.uk surfaces the datasets and context, while those registries give the authoritative per-entity records.

## Trust & verifiability
`trust: trusted` — the official UK government open-data portal; datasets are primary-source public records, so citations are authoritative (subject to each dataset's stated coverage and update date).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | data-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, address → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
