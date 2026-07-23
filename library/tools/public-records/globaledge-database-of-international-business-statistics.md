---
id: globaledge-database-of-international-business-statistics
name: globalEDGE Database of International Business Statistics
description: Use when you have a country/`geolocation` and want economic/trade indicators — returns comparable international business statistics by country and metric.
url: https://globaledge.msu.edu/tools-and-data/dibs
category: public-records
path:
- public-records
bestFor: Comparable country-level economic, trade, and business statistics for context and cross-country comparison.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Free resource from Michigan State University (globalEDGE). Free registration may be prompted for building custom statistic sets.
opsec: passive
opsecNote: You read public aggregate statistics; no target is contacted and nothing is tied to an individual. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Michigan State University's International Business Center, aggregating data from sources like the World Bank, IMF, and UN; academic, reputable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- globaledge
- global-edge-resource-directory
- central-and-eastern-european-business-directory
aliases:
- globalEDGE DIBS
- Database of International Business Statistics
- MSU globalEDGE
tags:
- data-and-statistics
- economic-indicators
- reference
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# globalEDGE Database of International Business Statistics

> Michigan State University's DIBS: comparable country-level economic and trade indicators, drawn from the World Bank/IMF/UN, ready to compare across countries.

## When to use
You need economic or business *context* for a country tied to an investigation — GDP, trade flows, market indicators, business-environment metrics — or you want to compare several countries on the same measures. globalEDGE DIBS lets you build country-by-metric tables from authoritative underlying sources. It's a reference/context resource, not a people or company lookup; missing-persons relevance is low (framing the economic environment around a case, e.g. a cross-border trade or business dispute).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://globaledge.msu.edu/tools-and-data/dibs.
2. Select the statistic(s)/indicator(s) and the countries you want to compare (you may be prompted for free registration to build/save custom sets).
3. Generate the table/chart; read the comparative figures by country and year.
4. Cross-reference: for a single country, globalEDGE's country pages give a broader profile (economy, trade, risk). Pivot to primary sources (World Bank/IMF) for the deepest breakdowns.

## Inputs → Outputs
- **In:** country / `geolocation` (+ chosen indicators)
- **Out:** comparable country-level economic/trade/business statistics (aggregate; no personal data)
- **Empty/negative result looks like:** a country/indicator with no value — the underlying source lacks that data point for that year; a gap reflects source availability, not a true zero.

## Gotchas & OpSec
- **Aggregate country data only** — never identifies individuals or specific companies.
- Numbers are re-aggregated from third parties (World Bank/IMF/UN) — cite the original source for anything critical, and mind the reference year.
- OpSec: passive public reading.

## Overlaps ("do both")
- Complements `[[undps-human-development-index]]`, World Bank, and UN Data — globalEDGE is convenient for *side-by-side country comparison*, the primary sources for authoritative single-indicator depth. See also `[[globaledge]]` for the broader portal.

## Trust & verifiability
`trust: trusted` — an academic MSU resource aggregating authoritative international datasets; reliable for context, with the standard caveat of tracing figures back to their original source and year.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | globaledge-database-of-international-business-statistics |
| category | public-records |
| selectorsIn → selectorsOut | geolocation → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
