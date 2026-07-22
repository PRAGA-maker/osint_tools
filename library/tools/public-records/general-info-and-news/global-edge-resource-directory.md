---
id: global-edge-resource-directory
name: globalEDGE Resource Directory
description: Use when you have an `employer-org`, industry, or country and want curated international business/trade data sources — returns links to registries, statistics, and reports (`employer-org` context).
url: https://globaledge.msu.edu/global-resources
category: public-records
path:
- public-records
- general-info-and-news
bestFor: A curated directory of thousands of international business, trade, and country-research resources, organized by topic.
selectorsIn:
- employer-org
- geolocation
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free directory hosted by Michigan State University's International Business Center; no account needed.
opsec: passive
opsecNote: A reference directory of external resources; browsing it involves no interaction with any subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Michigan State University (International Business Center); it curates links to third-party sources, so verify each destination's own reliability.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- globaledge
- globaledge-database-of-international-business-statistics
- central-and-eastern-european-business-directory
aliases:
- globalEDGE
- MSU globalEDGE global resources
tags:
- public-records
- business-intelligence
- international-trade
- directory
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# globalEDGE Resource Directory

> A university-curated index of international business and country-research sources — the starting map when your lead crosses a border or an industry.

## When to use
You have a company (`employer-org`), an industry, or a country (`geolocation`) and need authoritative starting points for cross-border research: national company registries, trade statistics, industry reports, country profiles, and reference data. In an investigation this points you to the right foreign registry or statistical source rather than guessing, and provides context on an organization's sector or a country's business environment.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://globaledge.msu.edu/global-resources.
2. Browse by category (Research, Trade, Reference) or by country/industry, or search a topic.
3. Follow the curated links out to the actual data source (e.g. a national registry or statistics office).
4. Use those destinations to research the `employer-org` — corporate filings, ownership, sector data.
5. Pivot: a foreign company registry found here feeds corporate-records lookups; country/industry context frames further searches.

## Inputs → Outputs
- **In:** `employer-org`, industry, or country (`geolocation`)
- **Out:** curated links to registries, statistics, and reports — i.e. routes to `employer-org` and market/country data (this is a directory, not a database of people)
- **Empty/negative result looks like:** it always returns curated links; a "miss" is when no listed resource fits your specific need. It does not itself hold records — every answer lives one hop away at a linked source.

## Gotchas & OpSec
- It's a signpost, not a dataset — the actual data (and its reliability) lives at the linked third-party sources.
- Business-focused: excellent for company/country/trade research, not for locating individuals directly.
- OpSec: passive reference browsing; nothing reaches any subject.

## Overlaps ("do both")
- Pairs with `[[globaledge]]` and `[[globaledge-database-of-international-business-statistics]]` for country statistics, and with corporate-registry tools that the directory points you toward.

## Trust & verifiability
`trust: trusted` — curated by a reputable university center, so the selection is credible; because it aggregates external links, judge each destination's own trustworthiness when you follow it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-edge-resource-directory |
| category | public-records |
