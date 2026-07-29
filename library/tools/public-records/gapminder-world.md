---
id: gapminder-world
name: Gapminder World
description: Use when you need free, well-sourced country-level development statistics (health, income, demographics) for context — returns downloadable indicators and interactive charts; aggregate data only.
url: http://www.gapminder.org/data
category: public-records
path:
- public-records
bestFor: Free, attributable world-development indicators and bubble-chart visualisations for background context.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Completely free ("and always will be free"); CSV downloads and online tools, no account.
opsec: passive
opsecNote: A public statistics site — no query concerns any individual. Fully passive background research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: An independent Swedish foundation (Hans Rosling's Gapminder); data is compiled from World Bank/UN/WHO sources with documented methodology and attribution.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Gapminder
- Gapminder World
tags:
- data-and-statistics
- public-records
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Gapminder World

> Hans Rosling's Gapminder: free, well-attributed world-development data and its famous bubble charts — for context, never for finding a person.

## When to use
Purely contextual, not for identifying anyone. Reach for it when a case needs credible country/region development indicators — life expectancy, GDP per capita, fertility, mortality, education — to frame conditions in a place a subject is connected to, or to sanity-check a demographic claim. It holds only aggregate data and returns no OSINT selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.gapminder.org/data.
2. Pick an indicator (or a bulk dataset like Systema Globalis / Fast Track) and a country/year.
3. Read the interactive chart or download the CSV for offline use.
4. Note the documented source and methodology per indicator; attribute Gapminder and the original source.
5. Pivot: use figures as contextual evidence; nothing person-specific to chain onward.

## Inputs → Outputs
- **In:** indicator + country/year (not an OSINT selector)
- **Out:** aggregate statistics, interactive charts, downloadable CSVs
- **Empty/negative result looks like:** gaps/estimates for a country-year — Gapminder interpolates or omits where source data is missing; check the per-indicator notes.

## Gotchas & OpSec
- **Aggregate only** — wrong tool for any individual-level lookup.
- Some values are estimated/interpolated to fill gaps; read the methodology before quoting a figure.
- Attribute both Gapminder and the underlying source (World Bank/UN/WHO).

## Overlaps ("do both")
- Sits alongside `[[who-data]]` and national statistics offices — Gapminder is best for long historical series and quick visual comparison; go to the primary source for the latest single-country detail.

## Trust & verifiability
`trust: trusted` — a respected independent foundation with transparent sourcing and methodology; the compiled data is reliable for context, with primary sources cited per indicator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gapminder-world |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
