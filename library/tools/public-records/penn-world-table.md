---
id: penn-world-table
name: Penn World Table
description: Use when you need comparable macroeconomic data (GDP, prices, productivity) across countries and years — returns national-accounts indicators for context on a place in an investigation.
url: http://www.rug.nl/research/ggdc/data/pwt/pwt-8.1
category: public-records
path:
- public-records
bestFor: Cross-country, cross-year real GDP / price-level / productivity data for country-level context.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free and open (CC BY 4.0); downloadable as Excel/Stata plus an online data tool. Cite the standard PWT reference when using it.
opsec: passive
opsecNote: Passive — you download aggregate national economic statistics, not anything about a person. Target-neutral background data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A peer-reviewed academic dataset from the Groningen Growth and Development Centre (Feenstra, Inklaar & Timmer), the standard reference for comparable cross-country real income/output; authoritative for macro data with the usual estimation caveats.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- PWT
- Penn World Table
- GGDC PWT
tags:
- data-and-statistics
- macroeconomics
- country-data
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Penn World Table

> The standard academic dataset of comparable cross-country economic data — real GDP, price levels, and productivity for ~180 countries over decades, in one downloadable table.

## When to use
Your investigation needs macroeconomic context for a country tied to a lead — relative income levels, price levels, output, or productivity, comparable across countries and over time. It's background/reference data for framing a place (e.g. plausibility of an economic claim, or conditions in a region), not a person- or company-level record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the PWT page (the old `pwt-8.1` link redirects toward the current release; the latest is **PWT 11.0**, ~185 countries, 1950–2023, at rug.nl/ggdc/productivity/pwt/).
2. Download the dataset in Excel or Stata, or use the online data-access tool.
3. Pick the countries, variables (real GDP variants, price level, capital, employment, productivity), and years you need.
4. Read/compare the values; the online tool and companion charts help quick cross-country comparisons.
5. Pivot: country-level baselines contextualise other findings; combine with World Bank/UN/SESRIC data to corroborate a figure.

## Inputs → Outputs
- **In:** a country/region of interest (`address`-level geography) + variable + year range
- **Out:** comparable macroeconomic indicators by country/year (contextual `address`-level data)
- **Empty/negative result looks like:** a country/year with no value — coverage gaps exist for some economies and the newest years, and very small/new states may be absent. Use the World Bank or national accounts to fill gaps.

## Gotchas & OpSec
- Aggregate national statistics only — never person- or firm-level.
- Values are modelled estimates (PPP-adjusted) with documented methodology; different PWT versions revise figures, so cite the version you used.
- The stub's URL points at an old version (8.1) — always take the current release from the GGDC site.
- OpSec: fully passive, target-neutral.

## Overlaps ("do both")
- Cross-check against World Bank Open Data, IMF, and `[[sesric-databases]]` — sources differ in method and coverage, and agreement across them raises confidence in a country-level figure.

## Trust & verifiability
`trust: trusted` — a peer-reviewed, widely-cited academic dataset; figures are authoritative estimates within their stated methodology, with version revisions as the main thing to track.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | penn-world-table |
