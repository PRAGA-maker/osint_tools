---
id: illinois-public-salaries
name: Illinois Public Salaries
description: Use when you have a `name` and want to confirm public-sector employment and compensation in Illinois — returns employer-org (unit of government), job title, and salary/work history.
url: https://c0ctb111.caspio.com/dp/1a7210001e4dbabdb7204962bc03
category: public-records
path:
- public-records
bestFor: Confirming that an Illinois public employee works for a specific government body and viewing their pay and title history.
selectorsIn:
- name
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free searchable database published by the Better Government Association; no account or payment required.
opsec: passive
opsecNote: Queries hit a third-party database, not the subject. Nothing is disclosed to the person being researched. Use a clean browser/IP if you want to keep the search unlinked from your normal browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Compiled by the Better Government Association (BGA) with DataMade from open-records requests to 1,800+ Illinois government units; primary FOIA-sourced data.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- BGA Salary Database
- Illinois Public Salaries Database
- salary.bettergov.org
tags:
- public-records
- salary
- government-employees
- illinois
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Illinois Public Salaries

> The Better Government Association's FOIA-built database of Illinois public-employee pay — turns a name into confirmed government employer, title, and salary history.

## When to use
You have a `name` and suspect the person is (or was) a public employee somewhere in Illinois — state agency, county, municipality, school district, park district, etc. — and you want to confirm the employer, role, and compensation. Useful for corroborating a subject's stated job, establishing which government body and location they are tied to, or spotting a title/agency change over time that indicates a move.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the embedded search (the Caspio table at this URL) or the canonical front end at **salary.bettergov.org**.
2. Enter the subject's `name`. You can also filter by unit of government, job title, or pay range to disambiguate common names.
3. Read the record: each row shows the employee name, the government employer, job title, base pay, and (where available) overtime/bonus broken out separately, plus a work-history view across years.
4. Pivot: a confirmed `employer-org` and location narrows geography and gives you a workplace to cross-reference; a title change across years is a timeline lead.

## Inputs → Outputs
- **In:** `name` (optionally job title / government unit to disambiguate)
- **Out:** `employer-org` (Illinois government body), job title, base + extra pay, multi-year work history
- **Empty/negative result looks like:** no matching employee — the database only covers Illinois public-sector units that responded to open-records requests and is refreshed roughly annually, so absence means "not a covered Illinois public employee in the loaded snapshot," not "not employed."

## Gotchas & OpSec
- Human-in-the-loop: none; open search, no login.
- Coverage is Illinois public sector only; private-sector and federal employees are absent. Data is a periodic snapshot (updated about once a year), so very recent hires/departures may lag.
- Common names produce multiple rows — use employer/title/salary to confirm identity before treating a hit as your subject.
- OpSec: passive; you are reading FOIA-derived public data.

## Overlaps ("do both")
- Complements the Illinois Comptroller's own salary database and the state employee-salary portal — BGA aggregates 1,800+ units into one searchable place, while the state portals are authoritative for the agencies they cover.

## Trust & verifiability
`trust: trusted` — records are obtained through open-records (FOIA) requests and published by the BGA, a long-running Illinois watchdog, with DataMade engineering. Values trace to government responses; the main caveat is snapshot freshness, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | illinois-public-salaries |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
