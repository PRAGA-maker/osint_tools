---
id: aiddata
name: AidData
description: Use when you have an `employer-org`, country, or funder `name` and want to map its international development-finance flows and counterparties — returns linked `employer-org` and `associate` entities.
url: http://aiddata.org
category: public-records
path:
- public-records
bestFor: Tracing who financed what, where, and for whom across global development and Chinese overseas lending.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free public research datasets and dashboards; bulk data downloadable at no cost.
opsec: passive
opsecNote: Queries hit a public academic research portal; no login and nothing about your subject is disclosed to the site. Standard passive research — still browse behind a VPN if the target is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Research lab at William & Mary; datasets are peer-reviewed, methodologically documented, and widely cited in academic and policy work.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- AidData W&M
- China.AidData.org
tags:
- data-and-statistics
- development-finance
- public-records
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# AidData

> A William & Mary research lab publishing granular datasets on international development finance — especially China's ~$2.2T of overseas lending — for mapping money flows between states, funders, and implementing organisations.

## When to use
You are researching an organisation, government body, contractor, or funder and want to know its role in international development finance: who funded it, which projects it ran, in which countries, and which counterparties it worked with. Strong for due-diligence and network-mapping around infrastructure lending, aid, and Chinese state financing; weak for finding individual private persons.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://aiddata.org and choose the relevant portal: China.AidData.org (overseas finance), China-Ports.AidData.org, GeoQuery.org (geospatial), or the China Contracts Search.
2. Search by funder, recipient country, sector, or implementing `employer-org`.
3. Read the project/commitment records: financier, borrower, amount, dates, sector, and named counterparties.
4. Download the underlying dataset (CSV) for bulk analysis when you need to pivot across many records.
5. Pivot: named implementing agencies and contractors (`employer-org`, `associate`) feed corporate-registry and sanctions/PEP checks; project locations feed geospatial follow-up.

## Inputs → Outputs
- **In:** `employer-org`, country, funder, or project `name`
- **Out:** linked `employer-org` (financiers, borrowers, contractors) and `associate` counterparties, with amounts and dates
- **Empty/negative result looks like:** a query with no matching commitments returns an empty result set — the entity simply is not in AidData's tracked finance flows, not proof it has none.

## Gotchas & OpSec
- Scope is development/official finance, not general corporate or personal records — off-topic entities will not appear.
- Data is compiled from public reporting and may lag or under-count opaque lending; AidData documents its confidence levels — read them.
- OpSec: **passive** public research; no account, nothing leaked about your subject.

## Overlaps ("do both")
- Pairs with corporate-registry and sanctions/PEP tools to enrich the organisations AidData names, and with geospatial tools (its own GeoQuery) to ground projects to locations.

## Trust & verifiability
`trust: trusted` — academic lab with documented methodology and citable datasets; each record links to source reporting you can verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aiddata |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
