---
id: eurostat
name: Eurostat
description: Use when you need official EU statistics — demographics, economy, migration, crime, regional data — to build context around a place, sector or population — returns structured datasets.
url: http://ec.europa.eu/eurostat
category: public-records
path:
- public-records
bestFor: Authoritative EU/European statistics (population, economy, migration, regional indicators) for background and base rates.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open; no account to browse, download or use the API.
opsec: passive
opsecNote: Querying published aggregate statistics is passive and anonymous — no login, no target contact. It's macro/background data, not information about individuals.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official statistical office of the European Union; authoritative, methodologically documented data used across policy and journalism.
missingPersonsRelevance: low
coverage:
- eu
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- european-union-open-data-portal
- eu-consolidated-corporate-registers
- e-justice-europa-eu
- eu-sanctions-tool
- europa-eu
- europa-press-releases
- european-commission-home-affairs
- frontex-migratory-map
- inspire-geoportal
- vat-number-validation
aliases:
- Eurostat
- ec.europa.eu/eurostat
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Eurostat

> The EU's official statistics office — authoritative datasets on population, economy, migration, regional indicators and more, for the background and base rates that frame an investigation.

## When to use
You need context rather than a person: how large a demographic is in a region, migration or economic figures for a country, regional crime/health/employment indicators. Eurostat gives methodologically sound EU/European statistics you can cite to frame a claim, sanity-check a narrative, or understand the environment around a place or sector.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ec.europa.eu/eurostat and use the Data Browser or search a theme (population, migration, economy, regions).
2. Open a dataset; filter by country/region, year and dimensions.
3. Read the table/chart and the metadata (definitions, methodology, coverage, last update).
4. Download (CSV/TSV/JSON) or use the REST/SDMX API for programmatic pulls.
5. Pivot: use the figures as context around your subject; combine entity data from `[[european-union-open-data-portal]]` for the specific-record layer.

## Inputs → Outputs
- **In:** a theme/indicator + country/region/year (aggregate query, not a personal selector)
- **Out:** structured statistical datasets (tables, time series) with documented methodology
- **Empty/negative result looks like:** a very granular cut may have suppressed/missing cells (confidentiality or small-sample gaps) — that's a data limitation, not an error; check a broader aggregation.

## Gotchas & OpSec
- It's aggregate statistics, not a person/entity lookup — use it for context and base rates, not to find an individual.
- Definitions and country coverage vary by dataset; read the metadata before comparing across countries/years.
- OpSec: passive, anonymous, no account.

## Overlaps ("do both")
- Pairs with `[[european-union-open-data-portal]]` and national statistics offices — Eurostat gives harmonised EU-wide figures; the open-data portal and national bodies add specific datasets and finer local detail.

## Trust & verifiability
`trust: trusted` — the EU's official statistical authority with documented methodology; figures are citable, though always note the dataset's definitions and reference period.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eurostat |
