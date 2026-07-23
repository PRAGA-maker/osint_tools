---
id: transparency-org-corruption-perception-index
name: Transparency.org Corruption Perception Index
description: Use when you need a country's perceived-corruption score as investigative context — returns per-country CPI scores/ranks (0–100) with year-over-year history.
url: http://www.transparency.org/cpi2015
category: public-records
path:
- public-records
bestFor: Benchmarking a country's public-sector corruption level for risk/context in an investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free; the current index and historical data/methodology are freely downloadable from Transparency International (see transparency.org/en/cpi). No account.
opsec: passive
opsecNote: Aggregate country-level index — no personal data, no target interaction; fully passive contextual reference.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published annually by Transparency International, the leading anti-corruption NGO, aggregating multiple independent expert/business surveys per country.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CPI
- Corruption Perceptions Index
- Transparency International CPI
tags:
- public-records
- corruption
- risk
- context
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Transparency.org Corruption Perception Index

> Transparency International's annual scorecard of public-sector corruption — every country rated 0 (highly corrupt) to 100 (very clean), with rank and multi-year history.

## When to use
Not a people-finder — use it for *context* on the jurisdiction behind an investigation: how corrupt its public sector is perceived to be. Helps you calibrate the plausibility of bribery/procurement/sanctions-evasion angles, assess the reliability of that country's official records, and frame risk when a subject or company operates there.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the current index at https://www.transparency.org/en/cpi (the `cpi2015` link is an older edition; the site serves the latest year).
2. Look up the country by score and global rank; open the map and the downloadable data.
3. Compare across years to see whether corruption is worsening or improving.
4. Pivot: a low score raises scrutiny of that country's official filings and increases the value of leak-based sources like `[[occrp-aleph]]` for the same subject.

## Inputs → Outputs
- **In:** a country selection (no personal selector)
- **Out:** CPI score (0–100), global rank, and historical trend for that country
- **Empty/negative result looks like:** a country not scored in a given year (data-availability gaps for very small/closed states) — noted rather than an error.

## Gotchas & OpSec
- It measures *perception* (composite of expert/business surveys), not incident counts — it's a risk indicator, not proof of any specific corruption.
- Scores aren't strictly comparable across older methodologies; use the current series for trends.
- Country-level only — says nothing about a specific person or company.

## Overlaps ("do both")
- Complements `[[occrp-aleph]]` and sanctions/beneficial-ownership tools — CPI frames *how much to distrust official data* for a jurisdiction; those tools do the actual entity-level digging.

## Trust & verifiability
`trust: trusted` — a flagship annual product of Transparency International, methodologically transparent and widely cited; authoritative as a perception index within its stated limits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | transparency-org-corruption-perception-index |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
