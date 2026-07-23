---
id: imf-world-economic-outlook-database
name: IMF World Economic Outlook Database
description: Use when you need authoritative country-level macroeconomic figures (GDP, inflation, unemployment) for context in an investigation — returns per-country economic time-series, not person data.
url: http://www.imf.org/external/ns/cs.aspx?id=28
category: public-records
path:
- public-records
bestFor: Pulling authoritative country macroeconomic indicators (GDP, inflation, etc.) for background/context.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: A public reference dataset from the IMF — querying it involves no individual and leaves no target-facing footprint. It contains country-level statistics only; there is nothing here about a person, so it neither exposes you nor identifies a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party International Monetary Fund dataset; the authoritative source for cross-country macroeconomic indicators and forecasts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- international-monetary-fund
aliases:
- IMF WEO
- World Economic Outlook Database
tags:
- economic-data
- country-statistics
- data-and-statistics
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# IMF World Economic Outlook Database

> The IMF's authoritative country-level economic database — GDP, inflation, unemployment, debt and more, by country and year, for background context rather than any person-level lookup.

## When to use
A context/reference tool, not a people-finder. Reach for it when an investigation needs reliable macroeconomic figures for a country — to sanity-check a claimed business scale, understand the economic backdrop of a region, convert or contextualize financial figures, or corroborate country-level claims in a document. It never identifies individuals; it grounds the *setting* an investigation sits in.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the WEO database at https://www.imf.org/en/Publications/WEO/weo-database (pick the latest edition).
2. Select country/countries and the indicators you need (GDP, inflation, unemployment, current account, etc.).
3. Choose the year range and generate the report; view on-screen or export the table.
4. Use the figures as authoritative background; cite the IMF edition/date for provenance.

## Inputs → Outputs
- **In:** none as an OSINT selector — you choose country + indicator + years
- **Out:** country-level macroeconomic time-series and forecasts (no person data)
- **Empty/negative result looks like:** an indicator not reported for a given country/year — coverage gaps exist for some economies; note them rather than inferring a value.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — a public dataset; nothing about a person is queried.
- Contains only aggregate national statistics; some figures are estimates/forecasts (flagged as such) — don't treat a projection as an observed value.

## Overlaps ("do both")
- Complements the broader [[international-monetary-fund]] resources and World Bank / national statistics offices — cross-check figures across sources when precision matters, since methodologies and vintages differ.

## Trust & verifiability
`trust: trusted` — a first-party IMF dataset and the standard reference for cross-country macro data. It's authoritative for context; just distinguish reported actuals from IMF estimates/forecasts and cite the edition used.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | imf-world-economic-outlook-database |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
