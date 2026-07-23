---
id: cites-trade-database
name: CITES Trade Database
description: Use when you have a species, country or `employer-org` in a wildlife-trafficking case and want the official record of legal international wildlife trade — returns permit-level trade records by taxon, country and trader.
url: https://trade.cites.org/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Querying ~23M official records of international wildlife trade (since 1975) by species, country, purpose and trader.
selectorsIn:
- employer-org
selectorsOut: []
status: live
pricing: free
costNote: Free public database managed by UNEP-WCMC for the CITES Secretariat; no account for public queries and CSV downloads.
opsec: passive
opsecNote: Public research database — querying it exposes nothing to any subject. Standard web-server logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official CITES trade record maintained by UNEP-WCMC; the authoritative dataset for reported legal wildlife trade between parties.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- CITES Wildlife Trade Database
- trade.cites.org
tags:
- bellingcat-toolkit
- environment-wildlife
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# CITES Trade Database

> The official ~23-million-record database of reported international trade in CITES-listed species since 1975 — the baseline for any wildlife-trafficking investigation.

## When to use
You're working a wildlife-crime or environmental case and need to know what *legal* trade exists in a species, or between two countries, or involving a named trader. The CITES database records permit-level exports/imports (taxon, quantity, source, purpose, importer/exporter country). It establishes the legitimate baseline — so shipments that don't appear here, or that exceed reported quotas, become red flags for trafficking.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://trade.cites.org/ and use the query interface ("Comparative Tabulations" or the raw-data output).
2. Filter by species/taxon, year range, importing and exporting country, source and purpose codes, and (where recorded) trader.
3. Run the query and read the tabulated trade records, or download the results as CSV for analysis.
4. Compare reported volumes against known seizures/quotas to spot anomalies.
5. Pivot: an exporter `employer-org` or country pattern feeds corporate-registry and shipping/customs research; species+route feeds seizure-database cross-referencing.

## Inputs → Outputs
- **In:** species/taxon, country pair, year range, and optionally trader `employer-org`
- **Out:** permit-level legal-trade records (taxon, quantity, source, purpose, countries) — downloadable as CSV
- **Empty/negative result looks like:** no records for the filter — meaning no *reported legal* trade of that type, which in a trafficking context can itself be the finding (trade that shouldn't exist, or should have been permitted but wasn't).

## Gotchas & OpSec
- It records reported legal trade only — it is a legitimacy baseline, not a seizure or crime database; illegal trade is absent by definition.
- Data is self-reported by parties with reporting lags and gaps; recent years may be incomplete and importer/exporter figures can disagree.
- OpSec: passive — a public research database.

## Overlaps ("do both")
- Pairs with wildlife-seizure databases and customs/shipping records — CITES tells you what trade *should* be legal, and seizure/shipping data reveals what actually moved, so discrepancies surface trafficking.

## Trust & verifiability
`trust: trusted` — the official CITES trade record maintained by UNEP-WCMC on behalf of the Convention Secretariat; authoritative for reported trade, with the inherent caveat of self-reporting completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cites-trade-database |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | employer-org → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
