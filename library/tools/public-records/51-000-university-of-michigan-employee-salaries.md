---
id: 51-000-university-of-michigan-employee-salaries
name: "University of Michigan employee salaries (MLive database)"
description: Use when you have a `name` believed to work at the University of Michigan and want to confirm employment, title and pay — returns `employer-org`, job title and salary.
url: https://www.mlive.com/news/ann-arbor/2020/12/see-the-2020-salaries-for-all-45000-university-of-michigan-employees.html
category: public-records
path:
- public-records
bestFor: Confirming a person's University of Michigan employment, department, title and salary by name.
selectorsIn:
- name
selectorsOut:
- employer-org
- name
status: degraded
pricing: freemium
costNote: MLive's article and embedded salary lookup are free to read; some MLive content sits behind a metered paywall after a few articles per month. The salary data itself derives from public-records (FOIA) disclosures.
opsec: passive
opsecNote: Passive — you are querying a journalist's static database, not touching the subject or the university. The subject is never notified. Standard sock-puppet browsing is sufficient; no login needed.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: MLive is an established Michigan news outlet; the figures come from University of Michigan public salary disclosures, but this is a 2020 snapshot and may be stale.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- U-M salaries
- University of Michigan salary database
- MLive salary lookup
tags:
- salary
- public-employee-salaries
- public-records
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# University of Michigan employee salaries (MLive database)

> A searchable public-employee salary database published by MLive — look up any University of Michigan employee's title, department and pay by name.

## When to use
You have a `name` and a plausible tie to the University of Michigan (Ann Arbor/Dearborn/Flint) and want to confirm they work there, in what role, and at what salary. Salary/title/department is a strong corroborator of identity and current `employer-org`, and department narrows where to look next (staff directories, campus contacts).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the MLive article at the URL; it embeds a searchable salary table (or links to MLive's salary database hub).
2. Enter the subject's last/first name in the lookup box.
3. Read the row: name, job title, department/campus, and annual salary.
4. If the embedded 2020 table is dated, search MLive for the most recent "University of Michigan salaries" year — MLive republishes annually from fresh FOIA data.
5. Pivot: department + title feeds the U-M staff directory, LinkedIn, and academic-profile searches for contact details.

## Inputs → Outputs
- **In:** `name`
- **Out:** `employer-org` (University of Michigan + department/campus), job title, annual salary
- **Empty/negative result looks like:** no matching row — the person is not in that year's disclosed U-M payroll (could mean not employed there, employed after the snapshot, or a name variant). Try alternate spellings and a newer year before concluding.

## Gotchas & OpSec
- Snapshot data: this URL is a 2020 dataset; pay and even employment may have changed. Prefer the latest annual edition for current facts.
- MLive's metered paywall may block after several page views in a month — this is the rate-limit human-in-the-loop; clear cookies or read from a fresh session.
- Common names produce multiple rows; disambiguate by department/campus.

## Overlaps ("do both")
- Pairs with the University of Michigan staff/faculty directory and LinkedIn — the salary DB confirms role and department; the directory adds email/phone/office.

## Trust & verifiability
`trust: community` — a reputable news outlet republishing genuine public-salary disclosures; the underlying numbers are FOIA-sourced and authoritative for their year, but verify currency against the latest edition.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 51-000-university-of-michigan-employee-salaries |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
