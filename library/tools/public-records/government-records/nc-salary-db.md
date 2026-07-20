---
id: nc-salary-db
name: NC Salary DB
description: Use when you have a `name` and suspect a North Carolina state job — returns confirmed name, job/position title, agency employer-org, and salary from the official state database.
url: https://www.ncosc.gov/public-information/state-employee-salary-database
category: public-records
path:
- public-records
- government-records
bestFor: Confirming that a named person is a North Carolina state employee, with their agency, title, and pay.
input: Employee name, agency
output: Salary, agency, position
selectorsIn:
- name
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free official state publication; no account or payment required.
opsec: passive
opsecNote: Searching an official state salary publication; the employee is not notified. Only your own web request is logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the North Carolina Office of the State Controller (OSC) — an authoritative first-party government source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- openpayrolls-com
aliases:
- North Carolina State Employee Salary Database
- NC OSC salary database
tags:
- public-records
- government-records
- salary-records
- employment
source: arf-seed
lastVerified: '2026-07-20'
enrichment: full
---

# NC Salary DB

> The North Carolina Office of the State Controller's official lookup for active state-employee names, titles, agencies, and salaries.

## When to use
You have a `name` and reason to think the subject works for North Carolina state government. This confirms the employer (agency), position/job title, and salary — anchoring the person to a workplace and time window, and helping disambiguate a common name by agency and locale. As a first-party government source it's more authoritative than third-party salary aggregators.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ncosc.gov/public-information/state-employee-salary-database.
2. Search by employee `name` (and agency if known) in the lookup.
3. Read the returned rows: name, position title, agency, and salary.
4. Use the agency to place the person geographically and to know which other NC records to pull.
5. Pivot: an agency + title feeds professional/LinkedIn searches; confirm/compare against [[openpayrolls-com]] for cross-checking.

## Inputs → Outputs
- **In:** `name` (+ optional agency)
- **Out:** confirmed `name`/title, `employer-org` (agency), salary figure
- **Empty/negative result looks like:** no match — the person isn't an active state employee in the covered set. Note the exclusions below before concluding.

## Gotchas & OpSec
- Excludes county employees, public-school teachers, community-college staff, University of NC system employees, and General Assembly members — a null result doesn't rule out public employment in NC, just this specific HR-Payroll set.
- Only *active* permanent/temporary employees; former staff drop off.
- Updated monthly; very recent hires/departures may lag.
- OpSec: passive; official public data.

## Overlaps ("do both")
- Pair with [[openpayrolls-com]] (national aggregator, includes some NC bodies this excludes): do both to cover teachers/university/county roles the OSC set omits.

## Trust & verifiability
`trust: trusted` — first-party NC Office of the State Controller data; authoritative and current to the last monthly update.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nc-salary-db |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
