---
id: government-of-canada-open-data
name: Government of Canada Open Data
description: Use when you have a `name`, `employer-org`, or place and want Canadian federal datasets (contracts, grants, spending, ATI summaries) — returns `employer-org`, `address`, and record details.
url: http://open.canada.ca/en
category: public-records
path:
- public-records
bestFor: Searching Canadian federal open datasets — contracts, grants, spending, and access-to-information summaries — for records tied to a person, org, or place.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free official Government of Canada portal; no account required.
opsec: passive
opsecNote: Searches a public federal data portal — no contact with any subject. Queries reveal only your interest to the government's site, not the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Government of Canada open-data portal; datasets are authoritative federal records, though completeness varies by department.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: true
localInstall: false
registration: false
aliases:
- open.canada.ca
- Canada Open Government
tags:
- data-and-statistics
- public-records
- canada
source: awesome-osint
lastVerified: '2026-07-23'
relatedTools:
- canadian-business-research
- canadian-department-of-finance
- completed-access-to-information-requests
- federal-corporation-search-canada
- gov-data-canada
- canadian-intellectual-property-office
- canadian-trademarks-database
- canadian-importers-database
- canadian-copyrights-database
- search-for-a-federal-corporation
---

# Government of Canada Open Data

> Canada's central federal open-data and proactive-disclosure portal — searchable datasets on spending, contracts, grants, and access-to-information requests.

## When to use
You have a `name`, business/`employer-org`, or Canadian place and want federal records: government contracts and grants (which name recipient organisations and amounts), proactive-disclosure spending, Temporary Foreign Worker program data, and summaries of completed access-to-information requests. Useful for tying a person or company to federal money, work, or programs, and for finding an org's addresses and dealings.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://open.canada.ca/en (dataset search at search.open.canada.ca).
2. Search datasets by keyword — a company name, program, or topic — or browse featured sets (contracts >$10k, grants & contributions, ATI summaries).
3. Open a dataset and filter/download it; query for your `name`/`employer-org`.
4. Read the records: recipient org, `address`, amounts, dates, departments.
5. Pivot: a contract recipient feeds corporate-registry lookups; an ATI summary points to a topic to request in full; amounts/dates build a timeline.

## Inputs → Outputs
- **In:** `name` / `employer-org` / keyword (also place)
- **Out:** `employer-org` and `address` details, contract/grant records, ATI summaries
- **Empty/negative result looks like:** no dataset or zero rows for your query — the person/org has no matching federal record here, not that no record exists at provincial/municipal level.

## Gotchas & OpSec
- Federal scope only: provincial and municipal records live on separate portals — this won't have them.
- Dataset freshness and granularity vary by department; check each dataset's metadata.
- OpSec: **passive** — a public-records query, invisible to the subject.

## Overlaps ("do both")
- Pairs with `[[federal-corporation-search-canada]]` and provincial open-data portals — this covers federal spending/ATI; those add corporate officers and sub-national records.

## Trust & verifiability
`trust: trusted` — an authoritative government source; cite the specific dataset and record, and note its department and last-updated date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | government-of-canada-open-data |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
