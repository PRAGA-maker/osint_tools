---
id: greater-sacramento-area-public-salaries
name: Greater Sacramento Area Public Salaries
description: Use when you have a `name` of a public employee in the Sacramento region and want to confirm their employer and pay — returns `employer-org` and salary/compensation.
url: https://b2.caspio.com/dp/c48210000605c38aa22f4080a1be
category: public-records
path:
- public-records
bestFor: Confirming a Greater Sacramento public employee's agency and compensation by name.
selectorsIn:
- name
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free searchable database (hosted on Caspio); no account or payment. Data derives from published California public-employee compensation disclosures.
opsec: passive
opsecNote: Searching a public-salary database queries the host, not the employee, so there is no subject-side footprint. This is published public-records data; looking it up is unremarkable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community/third-party republishing of official California public-salary disclosures; the underlying data is public record, but verify specific figures against the authoritative source (Transparent California / the agency).
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- govsalaries
- illinois-public-salaries
aliases:
- Greater Sacramento Area Public Salaries
- Sacramento public salaries
tags:
- public-records
- salary-database
- california
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Greater Sacramento Area Public Salaries

> A searchable database of public-employee pay across the Sacramento region — turn a name into their agency and compensation.

## When to use
Your subject is (or claims to be) a public employee in the Greater Sacramento area — Sacramento, Elk Grove, Roseville, Folsom, and surrounding counties (Sacramento, Placer, Yolo, El Dorado). Searching their `name` confirms the employing agency (`employer-org`), job title, and reported compensation. This corroborates employment claims, ties a person to a specific department/location, and — because pay data is dated — helps anchor a timeline of where they worked and when.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the database at https://b2.caspio.com/dp/c48210000605c38aa22f4080a1be.
2. Enter the subject's First and/or Last name; optionally filter by agency/employer.
3. Read the returned rows: name, agency, job title, and salary/total compensation for the covered year(s).
4. Disambiguate common names using the agency and title, and confirm figures against the authoritative source (Transparent California or the agency's own disclosure).
5. Pivot: the confirmed `employer-org` and title feed workplace/associate mapping and can corroborate an address region.

## Inputs → Outputs
- **In:** `name` (a Sacramento-region public employee)
- **Out:** `employer-org` (agency), job title, and salary/total compensation
- **Empty/negative result looks like:** no match — the person isn't a covered public employee in this dataset's years/geography, works in the private sector, or is listed under a different name; not proof they never held a public job.

## Gotchas & OpSec
- Scope-bound: only Greater Sacramento public agencies, and only the years this dataset covers — a snapshot, not a live payroll.
- Common-name collisions: use agency + title to disambiguate; a bare name match is a lead, not an identification.
- Third-party republish: confirm specific figures against the official California disclosure before relying on them.
- OpSec: fully passive; the employee is not notified.

## Overlaps ("do both")
- Pairs with `[[govsalaries]]` (nationwide public-salary aggregator) and other state datasets like `[[illinois-public-salaries]]` — cross-check the broader aggregators, and verify against Transparent California for the authoritative California record.

## Trust & verifiability
`trust: community` — the source data is genuine public record, but this is a third-party republishing on a hosted app; treat matches as strong leads and confirm exact compensation figures at the official source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | greater-sacramento-area-public-salaries |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
