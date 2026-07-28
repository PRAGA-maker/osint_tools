---
id: trading-economics
name: Trading Economics
description: Use when you have a country or economic indicator and want reference macro data — returns historical/current stats (GDP, inflation, rates, trade, credit ratings) by country.
url: https://tradingeconomics.com
category: public-records
path:
- public-records
bestFor: A one-stop reference for macroeconomic indicators, markets and credit ratings across ~200 countries — background/context, not people data.
selectorsIn:
- address
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Core indicator pages and charts are free to view; historical data export, API and advanced features require a paid subscription.
opsec: passive
opsecNote: Reading public statistics pages is passive and reveals nothing about any target — this is a reference dataset, not an investigative lookup of a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Widely-cited economic-data aggregator that compiles official sources (central banks, statistics offices); figures are generally reliable but always trace an important number back to its primary source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- unctad-stat
- unstats-social-indicators
aliases:
- tradingeconomics.com
tags:
- data-and-statistics
- economics
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Trading Economics

> A broad macroeconomic reference: current and historical indicators — GDP, inflation, interest rates, trade, employment, credit ratings — for roughly 200 countries in one place.

## When to use
This is **context/background** tooling, not a people-finder. Reach for it when an investigation needs to ground a country or region in economic reality: verifying a claimed statistic, understanding the macro backdrop behind a fraud/scam narrative, checking a nation's credit rating or currency, or sourcing a defensible figure for a report. It aggregates official data so you don't have to visit each central bank/statistics office separately.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tradingeconomics.com.
2. Search or browse by country, or by indicator (e.g. "inflation rate", "government debt").
3. Read the country/indicator page: latest value, historical chart, and the stated source/frequency.
4. For anything you'll cite, click through to the **primary source** (central bank, national statistics office) the figure is drawn from and confirm it there.
5. Pivot: use the macro context to interpret other findings; cross-check specific stats against `[[unctad-stat]]` or `[[unstats-social-indicators]]`.

## Inputs → Outputs
- **In:** a country/region (`address`-level geography) or an economic indicator
- **Out:** reference statistics (values, historical series, ratings) — background `metadata-exif`-style data, not entity records
- **Empty/negative result looks like:** a thin or "N/A" indicator page means the underlying source doesn't publish that series for that country — go to the national statistics office directly.

## Gotchas & OpSec
- It's an **aggregator** — for citation, always trace a figure to its primary official source; aggregated numbers can lag or be revised.
- Free access covers the charts/pages; bulk historical export and the API are paid.
- Not a source of information about individuals — don't expect people/records here.

## Overlaps ("do both")
- Pairs with `[[unctad-stat]]` and `[[unstats-social-indicators]]` — UN sources for trade and social indicators; cross-check macro figures across them and the primary national sources.

## Trust & verifiability
`trust: community` — a reputable, widely-cited aggregator of official economic data; individual figures are as good as the primary source they compile, so verify anything decision-critical at that source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trading-economics |
| category | public-records |
| selectorsIn → selectorsOut | address → metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
