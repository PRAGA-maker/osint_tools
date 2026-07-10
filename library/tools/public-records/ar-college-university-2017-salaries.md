---
id: ar-college-university-2017-salaries
name: Arkansas College/University 2017 Salaries
description: Use when you have a `name` and want to confirm they worked at an Arkansas public college/university in 2017 — returns employer-org, job title, and salary.
url: https://b2.caspio.com/dp.asp?AppKey=883210005c5e51279b424364aab2
category: public-records
path:
- public-records
bestFor: Confirming a person's 2017 Arkansas public higher-ed employer, title, and pay.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free public-records database (Caspio-hosted). No account or payment.
opsec: passive
opsecNote: Static public salary dataset; searching is anonymous and does not alert anyone. Reflects 2017 data only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A Caspio-hosted republication of Arkansas public-employee salary data; source appears to be a transparency/records project rather than the state's own portal, so treat as a secondary copy.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- arkansas-transparency
- linkedin
aliases:
- Arkansas higher education salaries 2017
tags:
- salary
- public-employee
- arkansas
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Arkansas College/University 2017 Salaries

> A searchable database of 2017 salaries for employees of Arkansas public colleges and universities — a way to place a person at a specific institution with a title and pay figure.

## When to use
You have a `name` (or an institution) and want to confirm the person was employed by an Arkansas public college/university in 2017, in what role, and at what salary. Useful for corroborating an employment history, tying a subject to a campus/city, or building out a timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the database at https://b2.caspio.com/dp.asp?AppKey=883210005c5e51279b424364aab2.
2. Filter by institution (dropdown of all Arkansas colleges/universities) and/or salary range.
3. Read the results table: Name, Title, School, Salary.
4. Pivot: an institution + title feeds LinkedIn / faculty-directory searches for current whereabouts; the name + city narrows people-search lookups.

## Inputs → Outputs
- **In:** `name` and/or `employer-org` (institution)
- **Out:** `name`, `employer-org` (school), job title, salary figure
- **Empty/negative result looks like:** no matching row — means not in the 2017 dataset. It says nothing about employment before/after 2017, private institutions, or non-Arkansas schools.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**; anonymous search of a static public dataset.
- Time-boxed: this is a 2017 snapshot only. Do not treat presence/absence as current employment.

## Overlaps ("do both")
- Pairs with `[[linkedin]]` — confirm whether the person is still at that institution and find current role/location.
- Pairs with `[[arkansas-transparency]]` — broader/newer Arkansas public-payroll data to extend the timeline beyond 2017.

## Trust & verifiability
`trust: community` — a third-party republication of public salary records; the underlying data is official but this is a secondary copy, so confirm surprising figures against the primary state source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ar-college-university-2017-salaries |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
