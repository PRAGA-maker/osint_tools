---
id: criminal-cop-database-lookup
name: Criminal Cop Database (Bay Area News Group)
description: Use when you have a `name` of a California law-enforcement officer and want to check for a criminal conviction — returns the officer's name, agency, crime, and case context.
url: https://extras.mercurynews.com/criminalcops/database/
category: public-records
path:
- public-records
bestFor: Checking whether a named California police/law-enforcement officer was convicted of a crime, per a large investigative database of ~1,000 cases.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- document-id
status: live
pricing: free
costNote: Free public investigative database published by the Bay Area News Group / Mercury News; no account needed.
opsec: passive
opsecNote: Searching a published journalistic database is passive and leaks nothing about anyone. It reflects a fixed 2019 investigation, so treat it as a historical snapshot, not a live registry.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Compiled by Bay Area News Group / Mercury News reporters from court files across nearly every California county (2019 "Criminal Cops" investigation); professionally sourced from public records.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Criminal Cops
- Mercury News Criminal Cops database
tags:
- police-accountability
- california
- court-records
- investigative-database
source: osint4all
lastVerified: '2026-07-20'
---

# Criminal Cop Database (Bay Area News Group)

> A journalist-built database of California law-enforcement officers convicted of crimes — a name-searchable record of ~1,000 cases pulled from county court files.

## When to use
You have the `name` of a California police officer, deputy, or other law-enforcement employee (or an agency, `employer-org`) and want to check whether they appear among the roughly 1,000 officers the Bay Area News Group / Mercury News found convicted of crimes in their 2019 "Criminal Cops" investigation. It's a niche but authoritative lookup: for the covered population and period, it ties a named officer to a specific crime, agency, and court case. Outside California law enforcement it has no coverage, hence low general missing-persons relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://extras.mercurynews.com/criminalcops/database/ (static journalistic site; may block some automated fetchers — use a real browser).
2. Search or filter by officer `name`, agency, county, or crime.
3. Read the record: officer name, employing agency (`employer-org`), the offense, and case details / `document-id`.
4. Use the case reference to pull the underlying court file from the relevant county court for the primary record.
5. Pivot: the county + case number feed court-record retrieval; the agency corroborates employment.

## Inputs → Outputs
- **In:** `name` (officer) or `employer-org` (agency/county)
- **Out:** conviction record → agency (`employer-org`), crime, case reference (`document-id`)
- **Empty/negative result looks like:** no match — means the officer isn't in this specific 2019 dataset, NOT that they have no record; the database is bounded in time and scope.

## Gotchas & OpSec
- Fixed 2019 snapshot for California only — absence proves nothing beyond "not in this dataset"; newer cases won't appear.
- Confirm identity carefully (name collisions) and pull the primary court file before asserting a conviction.
- OpSec: fully passive; it's a published news database.

## Overlaps ("do both")
- Pairs with California court portals and `[[national-center-for-state-courts-united-states]]` — this flags the case; the court system yields the authoritative primary record.

## Trust & verifiability
`trust: trusted` — a professionally reported database built from public court files; still verify each hit against the original court record and confirm you have the right person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | criminal-cop-database-lookup |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
