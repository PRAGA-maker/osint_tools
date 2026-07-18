---
id: uky-salaries-2019
name: UKY Salaries 2019
description: Use when you have a `name` and want to confirm someone was a University of Kentucky employee in 2019 — returns their `employer-org` unit and salary.
url: https://c0ect130.caspio.com/dp/c8521000eca729c2125e46c487fd
category: public-records
path:
- public-records
bestFor: Confirming a person's University of Kentucky employment, department, and salary as of September 2019.
selectorsIn:
- name
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free public-records datapage; no account or payment required (a CAPTCHA gates access).
opsec: passive
opsecNote: Passive lookup against a static, publicly published salary dataset — the subject is not notified. The query goes to a third-party Caspio-hosted page, so the host sees your search terms; use a clean browser session if that matters.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A curated Caspio datapage circulated via OSINT resource lists (osint4all); it reflects a real UK public salary disclosure but is a third-party republication, not the university's official portal.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- University of Kentucky Salaries 2019
- UK employee salary database 2019
tags:
- public-records
- salaries
- employment
- kentucky
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# UKY Salaries 2019

> A searchable snapshot of University of Kentucky employee salaries as of September 2019, useful for tying a name to a job, department, and pay figure.

## When to use
You have a `name` and a reason to think the person worked at the University of Kentucky (Lexington, KY) around 2019 — as staff, faculty, or administration — and you want to confirm employment, learn their department/unit, and get a salary figure. It's a single-institution point-in-time record, so treat it as corroboration for a specific person, not a general people search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the datapage URL in a browser.
2. Enter the subject's **last name** in the search field (optionally narrow by department from the dropdown of 500+ UK units).
3. Solve the CAPTCHA and submit.
4. Read the returned rows: employee name, department/unit (`employer-org` context), and annual salary as of 15 Sep 2019.
5. Pivot: a confirmed department/title feeds LinkedIn / university-directory searches and helps place the person geographically in Lexington, KY.

## Inputs → Outputs
- **In:** `name` (last name; optional department filter).
- **Out:** matched employee `name`(s), UK department/unit (`employer-org`), 2019 annual salary.
- **Empty/negative result looks like:** no rows returned for the surname — meaning the person was not an active, paid, non-confidential UK employee on 15 Sep 2019 (students who requested confidentiality and some temp/contract workers are excluded).

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA must be solved to query the database.
- Point-in-time only: this is a **2019** snapshot. Someone who left before or joined after 2019 won't appear; salaries are stale.
- Common surnames return many rows — use the department filter to disambiguate.
- OpSec: passive; the dataset is public and static, so lookups don't alert anyone.

## Overlaps ("do both")
- Pairs with broader public-salary aggregators and university directory lookups — this confirms the specific UK 2019 figure while those give current employer/title.

## Trust & verifiability
`trust: community` — a third-party Caspio republication of a genuine public-salary disclosure; the underlying data is real but confirm against the university's official open-records portal for authoritative/current figures.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uky-salaries-2019 |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
