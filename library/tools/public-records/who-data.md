---
id: who-data
name: WHO Data
description: Use when you need authoritative country-level health statistics for context (mortality, disease, health-system data) — the WHO Global Health Observatory; aggregate data only, no person-level records.
url: http://www.who.int/gho/en
category: public-records
path:
- public-records
bestFor: Official aggregate global/country health indicators for background and context.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-access data portal with a public API; no account.
opsec: passive
opsecNote: Public statistical portal — no query concerns any individual. Entirely passive background research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The World Health Organization's official statistics platform; authoritative for the aggregate health indicators it publishes.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- WHO Global Health Observatory
- GHO
tags:
- data-and-statistics
- public-records
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# WHO Data

> The WHO Global Health Observatory: official, country-level health statistics — useful for context, never for finding a specific person.

## When to use
Purely for background and context, not for identifying or locating anyone. Reach for it when a case needs authoritative aggregate health data about a country or region — mortality, disease prevalence, immunization, health-system capacity — e.g. to sanity-check a claim, understand conditions in an area a subject travelled to, or frame a report. It holds no person-level records and returns no OSINT selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the GHO portal (the URL redirects to WHO's current data site, `who.int/data/gho`).
2. Browse by theme (mortality, HIV/TB/malaria, immunization, NCDs, etc.) or search an indicator.
3. Read country/regional values, view maps and dashboards, or pull data via the GHO API for bulk/automated use.
4. Pivot: use the figures as contextual evidence in analysis; there is nothing person-specific to chain into.

## Inputs → Outputs
- **In:** indicator/theme/country query (not an OSINT selector)
- **Out:** aggregate health statistics, maps, dashboards, API datasets
- **Empty/negative result looks like:** "no data" for an indicator/country — WHO hasn't published that series, common for smaller states or recent years.

## Gotchas & OpSec
- **Aggregate only** — do not expect any individual-level information; wrong tool for people-finding.
- Reporting lags reality; latest years may be estimates or missing.
- Definitions vary by country; compare like-for-like indicators.

## Overlaps ("do both")
- Sits alongside other official statistics portals (national statistics offices, UN data) — use WHO for health specifically and cross-reference national sources for finer local detail.

## Trust & verifiability
`trust: trusted` — a first-party WHO product; the published aggregate data is authoritative, with methodology documented per indicator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | who-data |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
