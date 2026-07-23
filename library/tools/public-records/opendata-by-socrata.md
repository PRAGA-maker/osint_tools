---
id: opendata-by-socrata
name: OpenData by Socrata
description: Use when you have a `name` or `address` and want to mine open government datasets (permits, licenses, salaries, property, inspections) — returns `address`, `employer-org`, and other record fields.
url: https://opendata.socrata.com/
category: public-records
path:
- public-records
bestFor: Cross-searching government open-data portals for records tied to a person, business, or address.
selectorsIn:
- name
- address
selectorsOut:
- address
- employer-org
status: live
pricing: free
costNote: Free to browse and query datasets; a free app token only raises API rate limits and is not needed for manual search.
opsec: passive
opsecNote: You query a public data catalogue, not the subject. No contact with the target; queries may be logged by Socrata/Tyler but reveal only your interest, never the subject's involvement.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Platform operated by Tyler Technologies (Socrata); each dataset is published by a government agency, so accuracy depends on the publishing body, not Socrata.
missingPersonsRelevance: low
coverage:
- global
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- Socrata Open Data
- data.socrata.com
tags:
- public-records
- open-data
- government-datasets
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# OpenData by Socrata

> A catalogue over the many government open-data portals that run on the Socrata platform — one place to full-text search public records without first knowing which agency holds them.

## When to use
You have a `name`, business name, or `address` and suspect it appears in a government dataset — building permits, professional/occupational licenses, public-employee salaries, property/parcel rolls, restaurant or facility inspections, campaign finance, or code-enforcement actions — but you don't know which city, county, or state portal to look in. Socrata's catalogue lets you find and query those datasets in one place.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://opendata.socrata.com/ and use the catalogue search to find datasets by keyword (e.g. "professional licenses Texas", "business permits Chicago").
2. Open a promising dataset and use its column filters / free-text search to query your `name`, business name, or `address`.
3. Read the record: many datasets expose full name, mailing/business `address`, license or permit numbers, dates, and an issuing `employer-org` or agency.
4. Pivot: an address from a permit feeds reverse-address people search; a business name feeds corporate-registry lookups; a license number confirms occupation and jurisdiction.

## Inputs → Outputs
- **In:** `name` or `address` (also business name, license/permit keywords)
- **Out:** `address`, `employer-org`, plus dataset-specific fields (dates, license IDs, amounts)
- **Empty/negative result looks like:** no dataset matches your keyword, or a dataset returns zero rows — this only means that portal has no matching public record, not that the person is absent from government records generally.

## Gotchas & OpSec
- Coverage is uneven: only agencies that chose Socrata appear, and this central catalogue does not index every agency's own Socrata site — search the specific city/county portal directly when you know it.
- Datasets vary widely in freshness; check each dataset's "last updated" metadata before treating an absence as meaningful.
- OpSec: fully **passive** — you query a public catalogue, never the subject.

## Overlaps ("do both")
- Pairs with dataset-specific public-records tools and reverse-address lookups: Socrata finds *which* record exists; those tools resolve the person or property behind it.

## Trust & verifiability
`trust: community` — the Socrata platform is reputable (Tyler Technologies), but every dataset is only as accurate and current as the agency that published it; cite the underlying dataset, not "Socrata".

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opendata-by-socrata |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
