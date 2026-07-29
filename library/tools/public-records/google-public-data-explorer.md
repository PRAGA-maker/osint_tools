---
id: google-public-data-explorer
name: Google Public Data Explorer (now Data Commons)
description: Use when you need public statistical/demographic data for a place — Google's Public Data Explorer now redirects to Data Commons, which returns aggregated statistics by `geolocation`.
url: http://www.google.com/publicdata/directory
category: public-records
path:
- public-records
bestFor: Exploring and visualizing public statistical datasets (demographics, economics) aggregated by place.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free. The original Public Data Explorer URL now redirects to Google Data Commons (datacommons.org), its successor; the classic Explorer interface has been retired.
opsec: passive
opsecNote: You query aggregate public statistics, never an individual — there is no target-facing footprint and nothing personal is involved.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Google, aggregating datasets from official statistical bodies (World Bank, Eurostat, census agencies); authoritative sources, though it is now branded Data Commons.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Data Commons
- Public Data Explorer
tags:
- statistics
- open-data
- demographics
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Google Public Data Explorer (now Data Commons)

> Google's public-statistics tool — the classic Public Data Explorer directory now redirects to Data Commons, a queryable graph of official demographic and economic data by place.

## When to use
You need *context* data for a place tied to a case — population, demographics, economic indicators, health statistics for a city/region/country (`geolocation`). This is background/base-rate data, not person-level records: use it to understand the environment around a location or to sanity-check a claim ("is that population/income plausible for this town?"), not to find an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the old directory URL — it redirects to Google Data Commons (datacommons.org), the current home.
2. Search for a place or a statistical variable (e.g. a city's population, unemployment, median income).
3. Explore the charts/tables; Data Commons pulls from official sources (World Bank, Eurostat, national census/statistics agencies) and lets you compare places and time series.
4. For bulk/automated use, Data Commons exposes an API and Python client.
5. Pivot: place-level statistics contextualize a `geolocation` lead (is an address in a dense urban area or a remote one?) and feed geospatial analysis — not a direct person pivot.

## Inputs → Outputs
- **In:** a place (`geolocation`) or a statistical variable
- **Out:** aggregated public statistics for that place (time series, comparisons) — `geolocation`-level context
- **Empty/negative result looks like:** no data for a small locality or a niche metric — coverage is best at country/region level; hyper-local stats may be absent.

## Gotchas & OpSec
- Human-in-the-loop: none; open browsing.
- OpSec: fully passive; aggregate public data only, no personal information.
- The classic Public Data Explorer UI is retired — expect the redirect to Data Commons; update bookmarks accordingly (`status: degraded` reflects the migration, not a broken tool).
- This is base-rate/context data, **not** a people-search or public-records lookup for individuals; do not treat it as such.

## Overlaps ("do both")
- Complements official census/statistics portals: Data Commons unifies many of them behind one search/API, so use it to find the right figure fast, then cite the primary statistical agency for the record.

## Trust & verifiability
`trust: trusted` — Google-operated, aggregating authoritative official datasets with sourcing; verify any figure against the named primary source it cites.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-public-data-explorer |
| category | public-records |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
