---
id: govsalaries
name: GovSalaries
description: Use when you have a `name` (and ideally a US state/employer) and want to confirm public-sector employment and pay — returns `employer-org`, job title, salary and work location.
url: https://govsalaries.com/
category: public-records
path:
- public-records
bestFor: Confirming that a US public employee works for a given government body, with their title, salary and location.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- geolocation
status: live
pricing: freemium
costNote: Free to search and view salary records; funded by ads. No account needed for the core lookup.
opsec: passive
opsecNote: Reads a republished public-payroll dataset — you never touch the subject or their employer, so the lookup is invisible to them. GovSalaries logs your visit like any site; a clean session suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates official US government payroll disclosures (~150M records from 60k+ public sources); data is authoritative at source but can lag a year or two and may include stale/duplicate rows.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- GovSalaries.com
- government salaries database
tags:
- public-records
- salary-transparency
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# GovSalaries

> A free, name-searchable database of US government payroll disclosures — turn a name into confirmed public-sector employer, job title, salary and location.

## When to use
You have a `name` and suspect the subject works (or worked) for a US federal, state, county, city, school district or university employer, and you want to confirm it. A hit places the person at a specific `employer-org` in a specific city/agency with a job title and pay figure — strong corroboration of identity and current whereabouts, and a lead on where they physically work. Especially useful when the subject has a distinctive name or you already know the rough state/employer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://govsalaries.com/.
2. Search the subject's `name`; narrow with state or `employer-org` if the name is common.
3. Read each result row: full name, **employer/agency**, **job title**, **annual (and sometimes monthly) salary**, **year**, and location.
4. Disambiguate: use employer + location to separate namesakes; note the data **year** — older rows may be a past job.
5. Pivot: the employer + city feeds workplace/geolocation follow-up; the job title feeds professional-network and licensing searches.

## Inputs → Outputs
- **In:** `name` (+ optional state/`employer-org` to disambiguate)
- **Out:** `employer-org`, job title, salary, data year, and work `geolocation` (city/agency)
- **Empty/negative result looks like:** no matching rows — the person may be private-sector, in a non-disclosing jurisdiction, below a reporting threshold, or listed under a variant name. Absence is not proof of no public employment.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — a read of republished public records; the subject and employer are not notified.
- US-only, and coverage varies by jurisdiction (some states/agencies disclose fully, others not at all). A blank for one state means nothing about another.
- Records lag and can duplicate; always check the **year** and treat an old row as a *former* position until corroborated.

## Overlaps ("do both")
- Cross-check against other payroll aggregators (OpenPayrolls, FederalPay, state "sunshine" sites) — coverage differs by source, so a name missing from one often appears in another.

## Trust & verifiability
`trust: community` — an ad-funded aggregator sitting on official government payroll disclosures; the underlying figures are authoritative but may be dated, so verify the year and, for anything consequential, trace back to the originating agency's disclosure.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | govsalaries |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
