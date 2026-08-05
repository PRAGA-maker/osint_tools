---
id: agoa-data-center
name: AGOA Data Center
description: Use when you have a country or product/company involved in sub-Saharan Africa–US trade and want official AGOA trade statistics, eligibility, and exporter context — returns employer-org and trade-flow data.
url: http://agoa.info
category: public-records
path:
- public-records
bestFor: Looking up African Growth and Opportunity Act (AGOA) trade data, country eligibility, and product/exporter statistics.
selectorsIn:
- employer-org
- geolocation
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free public trade-data portal (agoa.info), run by the tralac trade-law centre; no account needed to browse data.
opsec: passive
opsecNote: A public statistics/reference site — you only read published trade data, disclosing nothing about a target. Standard clean-browser hygiene is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by tralac (Trade Law Centre) as the reference AGOA information hub, drawing on official US/African trade statistics.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- agoa.info
- African Growth and Opportunity Act data
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# AGOA Data Center

> The reference portal for African Growth and Opportunity Act trade data — country eligibility, product categories, and US–sub-Saharan-Africa trade flows.

## When to use
A niche public-records/economic-intelligence source, not a person-finder. Reach for it when an investigation touches sub-Saharan African trade with the US: verifying a country's AGOA eligibility, understanding which products/sectors a country exports under AGOA, or contextualising a company (`employer-org`) that operates in that trade. It answers "what/where does this trade flow," corroborating an organisation's stated business.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://agoa.info.
2. Browse by country (eligibility status, trade profiles) or by product/sector.
3. Read the trade statistics, eligibility timelines, and sector breakdowns.
4. Use company/sector context to corroborate an `employer-org`'s claimed activity or country footprint.
5. Pivot: an organisation confirmed in a trade sector feeds corporate-registry and company-OSINT tooling.

## Inputs → Outputs
- **In:** a country/`geolocation` or an `employer-org`/sector of interest
- **Out:** AGOA eligibility, trade statistics, and sector/company context (`employer-org`-level)
- **Empty/negative result looks like:** a country not covered by AGOA, or a sector with no reported AGOA trade — meaning it's outside AGOA scope, not that no trade exists.

## Gotchas & OpSec
- Scope is strictly AGOA / US–sub-Saharan-Africa trade; it is not a general company database.
- Data is aggregate trade statistics, so it corroborates context rather than identifying individuals.
- OpSec: fully passive public reading.

## Overlaps ("do both")
- Pairs with corporate-registry and company-search tools: AGOA gives the trade/sector context, registries give the legal entity, officers, and addresses.

## Trust & verifiability
`trust: trusted` — it is the established tralac-maintained AGOA information hub built on official trade statistics, so the figures are authoritative for AGOA-scope trade.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | agoa-data-center |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, geolocation → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
