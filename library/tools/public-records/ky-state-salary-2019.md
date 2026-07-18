---
id: ky-state-salary-2019
name: KY State Salary 2019
description: Use when you have a surname and suspect a Kentucky state-government job — returns employer-org (cabinet/department) and 2019 salary to confirm an employment history.
url: https://c0ect130.caspio.com/dp/c8521000065e102da08c40e696ad
category: public-records
path:
- public-records
bestFor: Looking up a Kentucky state-government employee's 2019 salary and department by last name, cabinet, or department.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free searchable public-salary datapage; no account or payment.
opsec: passive
opsecNote: Reads a public salary-transparency dataset; no login and no notification to the subject. It's a third-party-hosted (Caspio) datapage, so treat as normal web logging; use a clean browser for sensitive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Republished public-records salary data on a Caspio datapage; sourced from Kentucky open-records but a single 2019 snapshot by a third party, so verify against the official state source for current data.
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
- Kentucky state salary 2019
- KY employee salary
tags:
- public-records
- salary
- kentucky
- government-employees
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# KY State Salary 2019

> A searchable snapshot of Kentucky state-government employee salaries (2019) — confirm that a named person worked for a specific cabinet/department and see what they were paid that year.

## When to use
You have a `name` and reason to think the subject held a Kentucky state-government job around 2019. Search by last name (optionally narrowed by branch/cabinet or department) to confirm the `employer-org`, disambiguate common names via department/title, and read the 2019 salary — useful for building an employment history and a rough lifestyle/asset picture at that point in time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://c0ect130.caspio.com/dp/c8521000065e102da08c40e696ad.
2. Filter by branch/cabinet, department, and/or last name and run the search.
3. Read the returned rows: employee name, department, and 2019 salary.
4. Pivot: the confirmed department/role anchors identity — cross-reference against LinkedIn, later transparency snapshots, or the official Kentucky open-records portal for current status (a person absent from newer data may have left state service).

## Inputs → Outputs
- **In:** `name` (optionally narrowed by `employer-org`/department)
- **Out:** `employer-org` (cabinet/department), `name` (disambiguated), plus 2019 salary
- **Empty/negative result looks like:** no match — the person wasn't a KY state employee in 2019, worked for a non-covered branch/entity, or is spelled differently; it says nothing about employment before/after 2019.

## Gotchas & OpSec
- Human-in-the-loop: none; simple public search.
- OpSec: passive — public data, no subject notification.
- Snapshot limit: this is a **single 2019** dataset republished on Caspio. It won't reflect current employment or pay; confirm against the official Kentucky transparency/open-records source for anything current.

## Overlaps ("do both")
- Pairs with other states' salary-transparency tools (e.g. `[[ca-salary-db]]`) and the official Kentucky open-records portal — this pins a 2019 KY data point, the others extend coverage across states and years.

## Trust & verifiability
`trust: community` — it republishes public salary records, but as a third-party single-year snapshot; verify names, departments, and figures against the official Kentucky source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ky-state-salary-2019 |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
