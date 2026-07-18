---
id: gov-data-canada
name: Open Government Canada
description: Use when you have an `employer-org`, place, or topic and want Canadian federal open data — returns datasets (business registrations, addresses, grants, spending) to mine for records.
url: https://open.canada.ca/data/en/dataset
category: public-records
path:
- public-records
- government-records
bestFor: Searching Canada's official federal open-data catalogue for datasets containing organizations, addresses, grants, and spending records.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free and open (Open Government Licence – Canada); no account needed to search or download.
opsec: passive
opsecNote: You query the Government of Canada's public data portal, never a target. Downloads are anonymous; only the portal's own server sees your IP. Use a research browser if you prefer to keep queries separate from your identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Government of Canada open-data catalogue (open.canada.ca), publishing authoritative federal datasets with provenance and licensing metadata.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- canadian-business-research
- federal-corporation-search-canada
- government-of-canada-open-data
- completed-access-to-information-requests
- canadian-trademarks-database
- canadian-department-of-finance
- canadian-importers-database
- canadian-intellectual-property-office
aliases:
- open.canada.ca
- Government of Canada Open Data
tags:
- canada
- open-data
- government-records
- arf-seed
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Open Government Canada

> Canada's official federal open-data catalogue — thousands of authoritative datasets (corporate registrations, grants and contributions, government spending, facility addresses, licences) searchable by keyword.

## When to use
You're investigating something with a Canadian footprint — an `employer-org`, a person tied to a business or grant, a facility, or a place — and want primary federal data rather than a scraper's copy. The catalogue hosts datasets that can surface a company's registered `address`, federal grants/contributions a person or org received, contract awards, licensed operators, and inspection records. Use it to corroborate an entity, find funding/contract links to a subject, or pull an address list to cross-reference.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://open.canada.ca/data/en/dataset.
2. Search by keyword — an `employer-org` name, a program (e.g. "grants and contributions"), a place, or a record type.
3. Filter by organization (department), format (CSV/JSON/XLS), and topic in the sidebar.
4. Open a dataset to read its description and provenance, then download the data files or query via the CKAN API.
5. Search within the downloaded data for your subject's name/org/address.
6. Pivot: a grant/contract record → the recipient org and its officers (feed to a corporate registry); a registered `address` → property/people search; a program → other beneficiaries as `associate` leads.

## Inputs → Outputs
- **In:** `employer-org` / `name` / place / topic keyword
- **Out:** datasets containing `employer-org`s, `address`es, funding/contract records
- **Empty/negative result looks like:** no datasets match the keyword — the data isn't federally published (it may be provincial/municipal instead); try a broader term or a provincial portal.

## Gotchas & OpSec
- It's a catalogue of *datasets*, not a person-lookup — you often download a file and search inside it, rather than getting a direct hit on a name.
- Federal scope only; provincial/municipal records live on separate portals.
- Dataset freshness varies — check each dataset's last-updated date before relying on it.
- Fully passive and anonymous to use.

## Overlaps ("do both")
- Pairs with `[[federal-corporation-search-canada]]` and `[[canadian-business-research]]` — use those for authoritative company/officer records, and this catalogue for the surrounding funding, contract, and address datasets.

## Trust & verifiability
`trust: trusted` — the authoritative Government of Canada open-data portal with documented provenance and licensing on every dataset, so findings trace back to official federal publishers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-data-canada |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
