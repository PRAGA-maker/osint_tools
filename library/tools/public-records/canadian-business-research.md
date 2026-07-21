---
id: canadian-business-research
name: Canadian Business Research
description: Use when you have a Canadian company or business `name` and want the official research gateway — returns links to federal corporation search, financial benchmarks and industry data (`employer-org`, `address`).
url: https://www.canada.ca/en/services/business/research.html
category: public-records
path:
- public-records
bestFor: The Government of Canada's hub page linking corporate registry, financial-performance and market-research tools for researching a Canadian business.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free official Government of Canada portal; the tools it links (Corporations Canada search, Statistics Canada data) are free.
opsec: passive
opsecNote: A public government gateway — you read reference links and, from them, query official registries about a company, not a person. No subject-side footprint and no login for the public tools; browsing is anonymous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Government of Canada (canada.ca) page linking authoritative federal registries and Statistics Canada; the downstream data is primary-source.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- federal-corporation-search-canada
- canadian-department-of-finance
- completed-access-to-information-requests
- gov-data-canada
- government-of-canada-open-data
- canadian-intellectual-property-office
- canadian-trademarks-database
- canadian-importers-database
- canadian-copyrights-database
aliases:
- Canada.ca business research
- Government of Canada business research
tags:
- company-research
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Canadian Business Research

> The Government of Canada's official "research a business" hub — a signposted gateway to federal corporation search, financial benchmarks, and Statistics Canada data for Canadian entities.

## When to use
You have a Canadian company or business `name` (or a director/business tied to a subject) and want the authoritative starting point: confirm incorporation and status, find officers/registered addresses, benchmark financials, or pull industry/market data. It is a **gateway** — it routes you to the specific federal tools rather than returning records itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.canada.ca/en/services/business/research.html.
2. For a specific entity, follow **"Search for a federal corporation"** (Corporations Canada) and query the company `name` → status, directors, registered office (`address`).
3. For context, use the linked financial-performance data (industry benchmarks) and Statistics Canada portal.
4. For provincial entities, note that provincial registries are separate — this covers federal incorporation; follow through to the relevant province if needed.
5. Pivot: officer names/addresses → people-search and property records; corporate number → IP/trademark databases via the related tools.

## Inputs → Outputs
- **In:** a Canadian business/company `name` (or industry/sector for context data)
- **Out:** links to corporation status, directors, registered `address` (`employer-org` records), plus financial/industry statistics
- **Empty/negative result looks like:** no hit in the federal corporation search often means the entity is provincially (not federally) incorporated, dissolved, or a trade name — check the province's registry rather than concluding it doesn't exist.

## Gotchas & OpSec
- Federal vs provincial: Corporations Canada only holds federally incorporated companies; many businesses are provincial.
- This page is an index — the actual lookups happen on the linked registry/StatCan tools.
- Passive and login-free for public searches.

## Overlaps ("do both")
- Pairs with `[[federal-corporation-search-canada]]` (the actual registry lookup this page links to) and `[[canadian-trademarks-database]]`/`[[canadian-intellectual-property-office]]` for IP tied to the same entity.

## Trust & verifiability
`trust: trusted` — an official canada.ca gateway to primary federal registries and Statistics Canada; every record you reach is government-sourced and citable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-business-research |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
