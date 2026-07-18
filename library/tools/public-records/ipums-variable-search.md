---
id: ipums-variable-search
name: IPUMS Variable Search
description: Use when you need census/survey variables to frame demographic context — a research-data tool, not a person lookup (aggregate, anonymised data only).
url: https://variable-search.ipums.org/#/
category: public-records
path:
- public-records
bestFor: Finding variables across international census/survey microdata (157 countries, 1960–2022) for demographic and contextual research.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to search variables; downloading microdata extracts requires a free IPUMS account and agreement to terms.
opsec: passive
opsecNote: IPUMS data is aggregated and anonymised — it contains NO identifiable individuals. Searching it is passive and cannot expose any specific person; it is for demographic context only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: IPUMS (University of Minnesota) is an authoritative academic data repository; variable metadata is reliable, but the data is statistical, not personal.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- IPUMS
- variable-search.ipums.org
tags:
- census
- survey-data
- demographics
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# IPUMS Variable Search

> A finder for census and survey **variables** across 157 countries — a demographic-research aid, not a people search: the data is aggregated and anonymised, so it never identifies an individual.

## When to use
You need demographic or statistical **context** rather than a specific person — for example, understanding the baseline characteristics of a population, region, or era to frame an inference (how common a name/occupation/migration pattern is, what a survey captured in a country and year). IPUMS harmonises census/survey microdata and this tool locates the relevant variables. It cannot and will not return a named individual — treat it purely as background/context tooling.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://variable-search.ipums.org/#/ and search a concept (e.g. "occupation", "migration", "household size").
2. Filter by country and year to find matching variables and their definitions/coverage.
3. Read the variable metadata to understand what a given census/survey captured.
4. For actual microdata, create a free IPUMS account and build an extract (agreeing to research terms).
5. Pivot: demographic baselines → sanity-check assumptions in a profile (e.g. plausibility of a claimed occupation/region), not to identify anyone.

## Inputs → Outputs
- **In:** (none as a person selector — a demographic concept, country, and year)
- **Out:** survey/census variable definitions and coverage (statistical metadata, no person selectors)
- **Empty/negative result looks like:** no variable matches the concept/country/year — that census/survey didn't capture it; try a related concept or a different sample.

## Gotchas & OpSec
- **Not a people-search tool** — the underlying data is anonymised and aggregated; it can only inform context, never identify a subject.
- Downloading extracts requires a free account and agreement to research-use terms.
- OpSec: passive; no personal data is involved.

## Overlaps ("do both")
- Complements actual public-records and census-name tools — IPUMS gives statistical/demographic context, while name-indexed vital and census records (genealogy databases) are where person-level leads come from.

## Trust & verifiability
`trust: trusted` — an authoritative academic data source; the variable metadata is reliable, but remember its outputs are statistical, so no individual-level claim can or should be drawn from it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipums-variable-search |
| category | public-records |
| selectorsIn → selectorsOut | (none) → (statistical variables) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
