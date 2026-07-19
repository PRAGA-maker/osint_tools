---
id: washington-office-of-financial-management
name: Washington Office of Financial Management
description: Use when you have a `name` of a Washington State employee or an agency and want public workforce/salary and demographic data — returns state job-class salaries, workforce data, and population/demographic context.
url: http://www.ofm.wa.gov/
category: search-engines
path:
- search-engines
bestFor: Washington State public workforce and salary data, job-class compensation, and population/demographic research.
selectorsIn:
- name
- employer-org
- geolocation
selectorsOut:
- employer-org
- document-id
status: live
pricing: free
costNote: Free Washington State government site; no account required.
opsec: passive
opsecNote: You browse a state government open-data site; the query is not attributed to any individual and nothing is disclosed. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Washington State Office of Financial Management; salary schedules, workforce data, and demographics are authoritative government figures.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- OFM Washington
- ofm.wa.gov
tags:
- government-data
- salaries
- demographics
- public-records
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- washington
---

# Washington Office of Financial Management

> Washington State's OFM — the authoritative source for state workforce and salary schedules, job-class compensation, and population/demographic data; useful for placing a WA public employee's role and pay, or for demographic context on an area.

## When to use
You are researching a Washington State public employee or agency, or need demographic/population context for a WA location. OFM publishes state job classifications and salary ranges (so you can bound a named employee's likely pay band from their title), state workforce statistics, and county/state population and demographic data. It supports vetting an employment claim ("they say they're a WA state analyst — what does that class pay?") and grounding an investigation in an area's demographics.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ofm.wa.gov/.
2. For pay: use **Compensation & Job Classes** / **Job Classes & Salaries** to look up a state job title and its salary range.
3. For workforce data: **Data & Research → State Employee Workforce** (and the Washington Workforce Analytics reports).
4. For area context: **Population & Demographics** for county/state figures.
5. Use the site search for named reports/briefs.
6. Pivot: a confirmed job class/agency (`employer-org`) plus salary band corroborates an employment claim and feeds people-search; for the specific individual's salary, combine with a state salary-lookup/records-request tool, which OFM's aggregate schedules don't provide per-person.

## Inputs → Outputs
- **In:** `name`/title (job class), `employer-org` (agency), or `geolocation` (WA county/state)
- **Out:** `employer-org`/job-class + salary-range context and `document-id` (reports, workforce and demographic datasets)
- **Empty/negative result looks like:** no matching class/report — OFM publishes *aggregate* schedules and datasets, not a per-person salary directory, so an individual's exact pay won't appear here; that's a scope limit, not a failed search.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully **passive**; a government open-data site.
- Scope: this gives job-class and aggregate workforce/demographic data, not named individuals' salaries. For a specific employee's pay, use a state salary-database/public-records tool; use OFM to interpret and bound what a title should pay.

## Overlaps ("do both")
- Pairs with per-person state salary databases (e.g. public-employee salary lookups) and with U.S. Census/demographic tools — OFM gives the authoritative WA job-class schedules and workforce context; the salary databases give the named individual's figure, and Census tools broaden demographic coverage beyond Washington.

## Trust & verifiability
`trust: trusted` — the Washington State Office of Financial Management is the official source for these figures; salary schedules and workforce/demographic datasets are authoritative government data, published with methodology and citable report identifiers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | washington-office-of-financial-management |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org, geolocation → employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
