---
id: nc-state-government-salaries-search-and-report
name: NC State Government Salaries (News & Observer)
description: Use when you have a `name` you think is a North Carolina state employee and want to confirm it — returns their agency (`employer-org`), job title and current base salary.
url: https://b2.caspio.com/dp/96073000345d59bc5b1744109afe
category: public-records
path:
- public-records
bestFor: Confirming a person is an NC state government employee and reading their agency, title and salary.
selectorsIn:
- name
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free public-service database published by The News & Observer; no account needed.
opsec: passive
opsecNote: Searching a public salary database is passive and anonymous; the employee is not notified. You are reading a public record, so no sock puppet is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Compiled by The News & Observer from official North Carolina state payroll data, updated monthly; sourced from public records, so authoritative for the roles it covers.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NC state salaries
- North Carolina government salaries
- News and Observer salary database
tags:
- public-records
- salaries
- us
- government
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# NC State Government Salaries (News & Observer)

> A free, searchable database of North Carolina state government employee salaries — enter a name and confirm the person's agency, job title and current base pay.

## When to use
You have a `name` and a lead that the person works (or worked) for North Carolina state government, and you want to confirm employment and pull their role. Searching by first/last name returns the employee's agency (`employer-org`), job title and current base salary — a strong corroboration of a claimed public-sector job, and a way to place someone geographically and professionally within NC state government.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the database at b2.caspio.com/dp/96073000345d59bc5b1744109afe (linked from The News & Observer).
2. Search by last name and/or first name; narrow with the agency dropdown (40+ departments) or a minimum-salary filter if the name is common.
3. Read the results: employee name, agency, job title, and current base salary (excludes bonuses/overtime).
4. Pivot: the confirmed agency + title feed employer/registry research and professional-network searches; the name+agency match corroborates identity in other public-records work.

## Inputs → Outputs
- **In:** `name` (first/last, optionally agency)
- **Out:** `employer-org` (agency) plus job title and base salary for the matched employee
- **Empty/negative result looks like:** no match — the person isn't a covered NC state employee; note the exclusions (public-school staff, legislators, university-system and UNC Hospital workers are NOT included), so absence here doesn't rule out other public employment.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a public search form.
- Coverage is state-government employees only, updated monthly — recent hires/leavers may lag, and the excluded categories above won't appear.
- Common names produce multiple hits; use the agency filter and corroborate with title before attributing.

## Overlaps ("do both")
- Pairs with other US public-salary databases and professional-network tools — this confirms NC state employment and pay, while a LinkedIn-style search or registry adds tenure, history and colleagues.

## Trust & verifiability
`trust: trusted` — built from official NC state payroll public records by a major newspaper and updated monthly; authoritative for covered roles, though always check the "as of" date and exclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nc-state-government-salaries-search-and-report |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
