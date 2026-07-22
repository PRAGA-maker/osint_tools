---
id: iowa-cities-police-budgets
name: Iowa Cities police budgets
description: Use when you need Iowa municipal police-budget figures for context or accountability research — returns a published comparison of police spending across Iowa cities.
url: https://public.flourish.studio/visualisation/3168834/
category: public-records
path:
- public-records
bestFor: A published visualization comparing police-department budgets across Iowa cities.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free, publicly published Flourish visualization. No account.
opsec: passive
opsecNote: Viewing a static published chart is passive — it concerns municipal budgets, not individuals, and notifies no one. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A journalist/researcher-published data visualization; useful for context but a single-source snapshot — confirm figures against official city budgets.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- chicago-police-department-demographics
- maine-county-law-enforcement-discipline-chart
- pa-ppp-database
aliases:
- Iowa police budgets chart
tags:
- dataset
- police-budgets
- iowa
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# Iowa Cities police budgets

> A published chart comparing police-department budgets across Iowa cities — a niche accountability/context dataset, not a people-search tool.

## When to use
A very narrow, context-only resource. Reach for it when researching Iowa municipal policing — comparing department budgets across cities for accountability reporting, background on a local force, or civic data journalism. It contains budget figures for public institutions (`employer-org`), not personal data, so its missing-persons value is essentially nil; it's included as a public-records dataset.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Flourish visualization.
2. Read/interact with the chart to compare police budgets across the listed Iowa cities.
3. Note the figures and the period they cover.
4. Confirm any figure you'll cite against the relevant city's official budget document.
5. Pivot: a department's budget/size gives context for institutional research; for the people behind it, use staff directories and public-salary databases.

## Inputs → Outputs
- **In:** an Iowa city / police department (`employer-org`)
- **Out:** that department's budget figure in a cross-city comparison
- **Empty/negative result looks like:** the city/department isn't in the chart, or the visualization has been unpublished — it covers only the cities the author included, for a fixed period.

## Gotchas & OpSec
- Single-source, single-period snapshot — not authoritative; verify against official budgets.
- No personal data — it's institutional budget context only.
- Hosted on Flourish; the publisher can remove or update it.
- OpSec: passive static view.

## Overlaps ("do both")
- Pairs with public-salary databases and official city budget portals — this gives quick cross-city context; the official sources give authoritative, current figures and the individuals employed.

## Trust & verifiability
`trust: community` — a published visualization; treat as contextual and confirm specific numbers against primary municipal records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iowa-cities-police-budgets |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
