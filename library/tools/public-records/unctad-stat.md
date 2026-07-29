---
id: unctad-stat
name: UNCTAD STAT
description: Use when you have a country/economy and want authoritative UN trade, investment, and development statistics for context — returns background economic data.
url: http://unctadstat.unctad.org
category: public-records
path:
- public-records
bestFor: Authoritative UN trade, investment, and development statistics for almost every economy.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free UN data under Creative Commons terms; no account required.
opsec: passive
opsecNote: Passive — public statistics browsing; nothing touches any subject and no query is attributable to a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official statistics from UNCTAD (UN Conference on Trade and Development); authoritative macro-economic and trade data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- UNCTADstat
- UNCTAD Data Hub
tags:
- data-and-statistics
- un
- trade
source: awesome-osint
lastVerified: '2026-07-29'
relatedTools:
- unctad-country-fact-sheets
- unctad-investment-country-profiles
enrichment: full
---

# UNCTAD STAT

> The UN's trade-and-development data hub — 150+ indicators and long time series for almost every economy, useful as authoritative context around a country, sector, or trade flow in an investigation.

## When to use
Your case has an economic or trade dimension — a company's import/export sector, a commodity, a country's investment or maritime-transport profile — and you want **credible baseline numbers** rather than a subject-specific lookup. UNCTADstat provides official time-series data to sanity-check claims, understand the context a business operates in, or corroborate the plausibility of a trade-related story. It is background/context data, not a personal-identifier tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://unctadstat.unctad.org and browse by theme (international trade, economy & finance, maritime, digital economy, population).
2. Pick an indicator and filter by economy and time period.
3. Read or export the time series (datasets are downloadable under CC terms).
4. Pivot: use the figures to frame a company/sector, corroborate a claimed trade relationship, or point to related UNCTAD country profiles for narrative context.

## Inputs → Outputs
- **In:** a country/economy, sector, or trade indicator (no personal selectors)
- **Out:** official economic/trade time series and country statistics for context
- **Empty/negative result looks like:** an indicator with no data for a given economy/year — common for small or non-reporting economies; it's a data gap, not a finding.

## Gotchas & OpSec
- No login; fully public.
- This is **macro data** — it contextualises, it does not identify a person. Don't over-read country aggregates into individual conclusions.
- Figures are periodic and revised; note the release date/vintage when citing.

## Overlaps ("do both")
- Pairs with the linked `[[unctad-country-fact-sheets]]` and `[[unctad-investment-country-profiles]]` — the fact sheets give a narrative country snapshot while UNCTADstat gives the underlying series.

## Trust & verifiability
`trust: trusted` — first-party UN statistics; authoritative for the macro figures, though as with all aggregate data, verify how an indicator is defined before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unctad-stat |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
