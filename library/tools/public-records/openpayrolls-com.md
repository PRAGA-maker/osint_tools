---
id: openpayrolls-com
name: OpenPayrolls.com
description: Use when you have a `name` and want a subject's public-sector salary, job title, and employer — returns employer-org, address (locale), and confirmed name/title from ~200M government payroll records.
url: https://openpayrolls.com/
category: public-records
path:
- public-records
bestFor: Confirming that a named person works (or worked) for a U.S. government or publicly funded employer, plus their title and pay.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- address
status: live
pricing: freemium
costNote: Free to search and view names, employers, job titles, and salary figures; the site monetizes via ads and optional premium/background-report upsells, but the core payroll lookup needs no payment.
opsec: passive
opsecNote: You are searching an aggregator's copy of published FOIA payroll data — the subject is never contacted or notified. Standard web logging applies to you, not to the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party aggregator of genuine public-records payroll disclosures; underlying data is authoritative FOIA-released government payroll, but freshness and completeness vary by employer.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Open Payrolls
- OpenPayrolls
tags:
- public-records
- salary-records
- employment
- government-records
source: osint4all
lastVerified: '2026-07-20'
enrichment: full
---

# OpenPayrolls.com

> A free, searchable index of ~200 million U.S. public-employee salary records (federal, all 50 states, counties, cities, schools) from 1999–2024.

## When to use
You have a `name` and suspect the subject is or was a government or publicly funded employee — teacher, police officer, university staff, city/county worker, federal employee. OpenPayrolls confirms the employer, job title, work location, and compensation, which anchors a person to a place of work and a time window. Useful for verifying identity, building a timeline, or narrowing a common name to the right individual by employer/geography.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://openpayrolls.com/ and use the employee search (https://openpayrolls.com/search/employees).
2. Enter the target `name`; optionally narrow by state or employer to cut down common-name noise.
3. Read the result rows: full name, employer/agency, job title, year, and salary/compensation. Click a row for the detail record.
4. Cross-reference the employer's location (city/state) to establish where the subject worked and when.
5. Pivot: an employer + title feeds LinkedIn/[[idealist]]-style professional searches; a work city feeds people-search and address tools.

## Inputs → Outputs
- **In:** `name` (+ optional `employer-org`, state)
- **Out:** confirmed `name`/title, `employer-org`, `address` (employer locale — city/state, not home address)
- **Empty/negative result looks like:** "No results found" — means no matching *public-sector* payroll record; private-sector workers simply won't appear, so absence says nothing about employment generally.

## Gotchas & OpSec
- Only public/government employers are covered — a null result never means "unemployed", just "not on a published government payroll".
- The `address` is the employer's location, not the subject's home; don't conflate them.
- Data lags — records run to ~2024 and some employers report years late; a current job may not yet appear.
- OpSec: passive; the subject is never notified.

## Overlaps ("do both")
- Pairs with [[idealist]] for the nonprofit-employment angle that OpenPayrolls (government-only) misses, and with broader people-search tools that turn an employer + city into a home address.

## Trust & verifiability
`trust: community` — a third-party aggregator, but sourced from authoritative FOIA-released government payroll disclosures. Verify a specific figure against the originating agency's own transparency portal when precision matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openpayrolls-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
