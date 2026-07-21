---
id: population-reference-bureau
name: Population Reference Bureau
description: Use when you have a `geolocation`/region and want demographic base-rates (age, migration, household structure) to contextualise a case — returns population statistics, not individual records.
url: https://www.prb.org
category: search-engines
path:
- search-engines
bestFor: Pulling US and international demographic indicators for a country/state/region to frame the population context around a case.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Free non-profit research resource; data sheets and the International/US Data Centers are open. Optional free newsletter subscription.
opsec: passive
opsecNote: A public statistics site — you query aggregate demographic data by place, never a person. No target-side footprint; browsing is anonymous. Nothing here identifies an individual, so there is no subject-alerting risk.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established, widely cited non-profit demographic research organisation; figures are sourced from census bureaus, UN and national statistics agencies.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- population-reference-bureau-data-finder
aliases:
- PRB
- prb.org
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Population Reference Bureau

> A non-profit demographic research hub (World Population Data Sheet plus US and International Data Centers) — reference data for the population context around a case, not a people-finder.

## When to use
You have a `geolocation` (a country, US state, or region relevant to a subject) and need demographic base-rates to reason about a case: age distribution, migration and mobility patterns, household composition, urban/rural split, fertility, mortality. Use it as background/context — for example to gauge how common a subject's demographic profile is in an area, or to sanity-check a lead. It does **not** return information about a specific person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.prb.org.
2. Open the **International Data Center** or **US Data Center** (or the current World Population Data Sheet).
3. Select the country/state/region (`geolocation`) and the indicators you want (population, age structure, migration, etc.).
4. Read off the aggregate figures; export or cite the data sheet.
5. Pivot: use the numbers as framing only, then move to actual person/record tools for the individual — this is context, not a lookup on a subject.

## Inputs → Outputs
- **In:** `geolocation` (country / state / region) + chosen demographic indicator
- **Out:** aggregate demographic statistics (population counts, age/migration/household indicators) — no person-level selectors
- **Empty/negative result looks like:** an indicator not available for a small/obscure geography; the tool works at country/state granularity, so expect gaps below that level.

## Gotchas & OpSec
- No login, no captcha, fully passive — it is a public statistics library.
- This is context data only. Do not expect names, addresses, or any individual record here; treat it as base-rates, not evidence about a person.
- Figures are periodic estimates (annual data sheets); check the edition/year before citing.

## Overlaps ("do both")
- Pairs with `[[population-reference-bureau-data-finder]]` — the same organisation's more granular indicator search; use the data finder to drill into specific metrics once PRB gives you the overview.

## Trust & verifiability
`trust: trusted` — a long-established, frequently cited demographic non-profit sourcing from census bureaus, the UN, and national statistics offices; each indicator carries a documented source and year.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | population-reference-bureau |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
