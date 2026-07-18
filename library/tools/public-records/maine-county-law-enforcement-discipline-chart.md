---
id: maine-county-law-enforcement-discipline-chart
name: Maine County Law Enforcement Discipline Chart
description: Use when you have a `name` of a Maine law-enforcement officer and want any recorded discipline — returns officer, agency and disciplinary detail.
url: https://public.flourish.studio/visualisation/4443849/
category: public-records
path:
- public-records
bestFor: Checking whether a named Maine law-enforcement officer appears in a compiled discipline record, with their agency.
selectorsIn:
- name
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free public data visualisation; no account needed to view.
opsec: passive
opsecNote: A static, publicly published chart. Viewing it sends nothing to any subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A journalist-compiled Flourish visualisation (2020), not an official state registry; treat entries as a reporting artifact to corroborate against primary agency records.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- chicago-police-department-demographics
- iowa-cities-police-budgets
- george-floyd-where-black-people-are-most-disproportionately-killed-by-police
aliases:
- Maine LE Discipline Chart
tags:
- public-records
- law-enforcement
- maine
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Maine County Law Enforcement Discipline Chart

> A narrow, journalist-compiled table of disciplinary records for Maine law-enforcement officers — useful only when your subject is a Maine officer.

## When to use
Very specific: your subject is (or is claimed to be) a law-enforcement officer in Maine, and you want to know whether they appear in a compiled disciplinary record and with which `employer-org` (agency). This is a single static dataset, so it is a niche corroboration source — reach for it when a Maine LE name comes up, not as a general people search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://public.flourish.studio/visualisation/4443849/.
2. Use the table's search/filter box to look up the officer's `name`.
3. Read the matching row: officer name, agency, and the disciplinary detail recorded.
4. Pivot: a hit is a lead, not proof — confirm against the officer's agency, state POST/certification board, or court records before relying on it.

## Inputs → Outputs
- **In:** `name` (Maine law-enforcement officer)
- **Out:** `employer-org` (agency) plus the recorded disciplinary detail
- **Empty/negative result looks like:** no matching row — the officer isn't in this particular compilation, which does not mean no record exists; the chart is limited in scope and date.

## Gotchas & OpSec
- This is one compiled chart from ~2020, not a live or official registry — it will miss recent cases and officers, and may contain reporting errors.
- Scope is Maine only; irrelevant for any other state.
- OpSec: passive; viewing a public chart alerts no one.

## Overlaps ("do both")
- Sits alongside other compiled police-accountability datasets like `[[chicago-police-department-demographics]]`; for authoritative status always go to the officer's agency and the state certification board.

## Trust & verifiability
`trust: community` — a journalist-compiled artifact, valuable as a pointer but not a system of record; verify every hit against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maine-county-law-enforcement-discipline-chart |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
