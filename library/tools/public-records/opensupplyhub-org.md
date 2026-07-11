---
id: opensupplyhub-org
name: opensupplyhub.org
description: Use when you have a company/brand or factory `name`/`address` and want to map global production facilities and who sources from them — returns facility locations, IDs, and linked contributors.
url: https://opensupplyhub.org/facilities/?sort_by=contributors_desc
category: public-records
path:
- public-records
bestFor: Mapping global production facilities to the brands/organizations that source from them, with addresses and stable facility IDs.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free, open-data platform (a nonprofit); browsing and searching facilities is free, and a free API/account is available for bulk/programmatic access.
opsec: passive
opsecNote: Querying an open public database of facilities; nothing touches any company or individual and there is nothing to alert. Standard clean-browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Nonprofit open-data project (successor to the Open Apparel Registry) that deduplicates contributor-submitted facility data into stable OS IDs; widely used in supply-chain research, though data completeness depends on what contributors have disclosed.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Open Supply Hub
- OS Hub
- Open Apparel Registry
tags:
- companysites
- Company Related Sites
- supply-chain
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# opensupplyhub.org

> An open, deduplicated database of global production facilities — search a factory or a brand and see the facility's address, its stable OS ID, and which contributors (brands, NGOs) have linked it, mapping who makes what and where.

## When to use
You're investigating a company, brand, or a specific factory and want its supply-chain footprint: where facilities are (addresses/geo), what stable identifier ties records together, and which organizations disclose sourcing from a given site. Useful for corporate/associate mapping, verifying a claimed manufacturer, tying an `employer-org` to physical locations, or working from a factory `address` back to the brands connected to it. Reach for it in supply-chain, labor, and corporate-network research.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://opensupplyhub.org/facilities/ (the linked view sorts by number of contributors).
2. Search by facility/company `name` or `address`, or filter by country/sector.
3. Open a facility: read its name(s), address/geo, OS ID, and the list of contributors that have associated it (brands/NGOs sourcing or reporting there).
4. For scale, use the free API/account to pull facility data programmatically.
5. Pivot: contributors → brand/`employer-org` relationships; the facility `address` → maps and local records; the OS ID → a stable key to join with other datasets.

## Inputs → Outputs
- **In:** `name` / `employer-org` (brand or factory) / `address`
- **Out:** `employer-org` (linked contributors/brands), `address` (facility location + OS ID)
- **Empty/negative result looks like:** no facility or no contributors — the site isn't in the dataset or no one has disclosed it. Absence reflects disclosure gaps, not that no facility exists; combine with corporate registries and customs/trade data.

## Gotchas & OpSec
- Human-in-the-loop: none.
- Data is **contributor-dependent** — coverage is strong for apparel/consumer goods where brands disclose, thinner elsewhere; a missing link means "not disclosed here," not "no relationship."
- Names/addresses are normalized but can still carry variants — use the OS ID as the durable key.
- OpSec: passive; open data.

## Overlaps ("do both")
- Pairs with corporate registries (e.g. `[[infoempresa-com]]`, OpenCorporates) and trade/customs-data tools — OSH maps facilities and sourcing links; registries add legal ownership and directors.

## Trust & verifiability
`trust: trusted` — a reputable nonprofit open-data project with transparent, deduplicated, contributor-sourced records; reliable for what's disclosed, with completeness bounded by contributor participation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opensupplyhub-org |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
