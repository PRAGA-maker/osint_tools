---
id: ca-salary-db
name: CA Salary DB
description: Use when you have a name and suspect the subject is a California public employee — returns employer-org, exact salary/benefits, and job title from public payroll records.
url: https://transparentcalifornia.com/
category: public-records
path:
- public-records
- government-records
bestFor: Looking up a named California state/local/school/agency employee's exact pay, benefits, employer, and job title.
input: Name, employer, position
output: Salary, benefits, employer
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free public-records database; no account or payment. Funded by a nonprofit/foundation.
opsec: passive
opsecNote: Reads already-public payroll disclosures; no login and no target notification. Standard web logging only. Use a clean browser for sensitive subjects.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Transparent California compiles official payroll data obtained via California Public Records Act requests; figures trace back to government sources.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Transparent California
- transparentcalifornia.com
tags:
- public-records
- salary
- california
- government-employees
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# CA Salary DB

> Transparent California — the largest public database of California government pay, letting you confirm that a named person works for a specific agency and see exactly what they earn.

## When to use
You have a `name` and reason to think the subject is (or was) a California public employee — state agency, county, city, school district, UC/CSU, police/fire. Transparent California confirms the `employer-org` and job title, pins down which of several same-named people is the right one (via agency + role), and gives exact salary/benefits useful for lifestyle and asset analysis.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://transparentcalifornia.com/ and choose salaries (it also has pensions and vendor payments).
2. Search the person's name; filter by year and by employer/agency if you know it, to disambiguate common names.
3. Read each record: employer, position/title, regular pay, overtime, benefits, and total compensation, per year.
4. Pivot: the confirmed employer/title is a strong identity anchor — cross-reference against LinkedIn, a licensing board, or a union roster; a pension record instead of a current salary suggests retirement/relocation.

## Inputs → Outputs
- **In:** `name` (optionally narrowed by `employer-org`)
- **Out:** `employer-org` (agency + title), `name` (disambiguated to a specific role), plus exact pay/benefits by year
- **Empty/negative result looks like:** no match — the person isn't a covered California public employee (private sector, federal, another state, or a non-disclosing entity), or the name is spelled differently. Absence is not proof of unemployment.

## Gotchas & OpSec
- Human-in-the-loop: none; it is a straightforward public search.
- OpSec: fully passive — the data is already public disclosure and the subject is not notified.
- Scope: California public sector only, and data lags by a year or more. Federal employees, private employees, and other states are out of scope — use the appropriate state transparency site instead.

## Overlaps ("do both")
- Pairs with LinkedIn/employer-verification and other states' transparency portals (e.g. Transparent equivalents) — this pins the California public-sector role with exact pay, while professional profiles add history and contacts.

## Trust & verifiability
`trust: trusted` — figures come from official payroll data obtained under the California Public Records Act; you can request the same source records to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ca-salary-db |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
