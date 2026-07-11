---
id: pibuzz
name: Pibuzz
description: Use when you have a `name` (or `employer-org`) and want to find where a US public-sector subject works and what they earn — returns a directory of government salary/employee-name databases keyed by state and agency.
url: http://pibuzz.com/
category: public-records
path:
- public-records
bestFor: Locating the government salary/employee database for a given US state so you can confirm a public employee's agency, job and pay.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free directory/blog; the linked salary databases are themselves free public records.
opsec: passive
opsecNote: Pibuzz is a link directory — you leave it to query third-party salary databases, each of which is a passive public-records search that does not notify the subject. No account needed. As always, run searches from a sock-puppet browser to avoid tying your investigative sessions together.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running private-investigator blog that curates links to legitimate government salary databases compiled by news orgs, watchdogs and agencies. Pibuzz itself hosts no data; verify each downstream source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Private Investigator Blog
- Pibuzz government salaries
tags:
- toddington
- curated-directory
- specialty-search
- government-employees
- salaries
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Pibuzz

> A private-investigator blog that indexes US federal/state/county/municipal government salary-and-employee-name databases — the fastest way to find "which public database lists this state's employees."

## When to use
You have a `name` you suspect works in the US public sector (teacher, cop, city/county/state worker, university staff) or an `employer-org` that is a government body, and you want to confirm employment, agency, job title and pay. Government salary disclosures are strong location-of-employment signals — useful for confirming a subject is alive and working, for judgment/asset work, and for pinning down where to physically find someone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://pibuzz.com/ and open the government-salaries / government-employees section.
2. Navigate to the relevant state (Texas, New York, Ohio, etc.) or the federal page.
3. Follow the link to the actual salary/employee-name database (run by a newspaper, watchdog or the agency).
4. Search that database by `name` (or browse by agency) to confirm employer, title and compensation.
5. Pivot: a confirmed `employer-org` gives you a physical work location and phone-directory lead; the salary record confirms the person is currently employed and where.

## Inputs → Outputs
- **In:** `name` and/or `employer-org` (must be US public sector for a hit)
- **Out:** `employer-org` (agency), job title, salary, and thereby a work `address`/location
- **Empty/negative result looks like:** the subject isn't a public employee, the state has no published database, or the linked source has moved — Pibuzz is only a signpost, so a dead link means check the source's current URL, not that the record is gone.

## Gotchas & OpSec
- Pibuzz hosts nothing itself; data quality and freshness depend entirely on each linked database — always cite the underlying source.
- Coverage is US-only and public-sector-only; private-sector employment won't appear.
- Some linked databases lag a year or more, and common names return many matches — corroborate with a location or agency.

## Overlaps ("do both")
- Pairs with mainstream people-search and LinkedIn — salary databases confirm current government employment and pay, which private people-search often gets wrong or omits.

## Trust & verifiability
`trust: community` — a reputable PI-community blog curating links to legitimate, independently-published public-records databases. Trust the named downstream sources; treat Pibuzz as a maintained index that can go stale.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pibuzz |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
