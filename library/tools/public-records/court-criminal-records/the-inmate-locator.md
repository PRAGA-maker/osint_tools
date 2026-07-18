---
id: the-inmate-locator
name: BOP Inmate Locator
description: Use when you have a `name` (or BOP register number) and want to find someone in U.S. federal prison — returns their facility `geolocation`, register number, and release date.
url: https://www.bop.gov/inmateloc/
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Locating a current or recent U.S. federal inmate and their facility and release date.
selectorsIn:
- name
- document-id
selectorsOut:
- geolocation
- name
- dob
status: live
pricing: free
costNote: Free official U.S. Bureau of Prisons search; no account required.
opsec: passive
opsecNote: Passive — you query the federal government's public inmate database; the subject is not notified. Records are public. Standard federal-site logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official U.S. Bureau of Prisons (Department of Justice) locator; authoritative for federal inmates.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- federal-bureau-of-prisons-inmate-locator-us
- federal-inmate-locator
- sorted-by-birth-date
aliases:
- BOP Inmate Locator
- Federal inmate locator
tags:
- criminal-records
- incarceration
- federal
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# BOP Inmate Locator

> The U.S. Bureau of Prisons' official search for finding a person in federal custody — a direct answer to "is this person in federal prison, and where?"

## When to use
You have a `name` (or a BOP register number, `document-id`) and want to determine whether the subject is or was recently in U.S. federal custody, which facility holds them, and their release date. A high-value missing-persons resource: incarceration is a common, verifiable explanation for someone dropping off the radar, and a facility gives a concrete `geolocation` and a channel (mail/visitation) to reach them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bop.gov/inmateloc/.
2. Search by BOP register number for an exact hit, or by `name` (first/last, with optional age/race/sex to disambiguate).
3. Review results: inmate name, register number, age/`dob`-derived age, current facility (`geolocation`), and projected release date.
4. Pivot: the facility supports mail/visitation follow-up; the register number is a stable `document-id`; release date frames a timeline. Cross-check state systems if not found federally.

## Inputs → Outputs
- **In:** `name` (+ optional age/race/sex) or BOP register number (`document-id`).
- **Out:** inmate `name`, register number, current facility (`geolocation`), age, and release date.
- **Empty/negative result looks like:** "0 results" — the person isn't in the federal system (covers ~1982–present); they may be in **state/county** custody (a different system) or not incarcerated.

## Gotchas & OpSec
- Federal only: this is BOP (federal) — state prisoners and county-jail detainees are in separate state/local systems.
- Coverage window: reliable for inmates from roughly 1982 onward.
- Common names: use age/race/sex filters to disambiguate; confirm identity before asserting a match.
- OpSec: passive; public records, no notification.

## Overlaps ("do both")
- Pairs with `[[federal-inmate-locator]]` (same data, alternate front-ends) and state DOC/county-jail locators — always check state systems too, since most incarceration is non-federal.

## Trust & verifiability
`trust: trusted` — the official DOJ/Bureau of Prisons locator; authoritative for federal custody status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-inmate-locator |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → geolocation, name, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
