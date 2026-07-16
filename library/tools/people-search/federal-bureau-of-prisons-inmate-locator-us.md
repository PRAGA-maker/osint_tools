---
id: federal-bureau-of-prisons-inmate-locator-us
name: Federal Bureau of Prisons — Inmate Locator (US)
description: Use when you have a `name` or BOP register number and want to check US federal custody status — returns name, age/race, location, and release date.
url: https://www.bop.gov/inmateloc/
category: people-search
path:
- people-search
bestFor: Confirming whether a person is (or was) in US federal prison custody and where.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- physical-description
- address
status: live
pricing: free
costNote: Free official US federal government service. No account or payment.
opsec: passive
opsecNote: Official public search; anonymous and does not notify anyone. This is a government record lookup — no sock puppet needed, though a clean session is good practice.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US Federal Bureau of Prisons — authoritative first-party custody record.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- vinelink
- utah
- federal-inmate-locator
- sorted-by-birth-date
- the-inmate-locator
aliases:
- BOP inmate locator
- bop.gov/inmateloc
tags:
- people-investigations
- inmate
- federal
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Federal Bureau of Prisons — Inmate Locator (US)

> The US Bureau of Prisons' official inmate locator — the authoritative check on whether a person is or was in FEDERAL custody, and where.

## When to use
You have a `name` (or a BOP register number) and need to account for a person's whereabouts where federal incarceration is possible. A hit tells you they are/were in federal custody, at which facility, and their release date — a definitive "found" outcome for a missing-person case involving federal charges. Note it covers **federal** inmates only (in custody 1982–present); state prisons and county jails are elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bop.gov/inmateloc/.
2. Search by BOP register number (exact) or by first/last name, optionally narrowing by age, race, and sex.
3. Read the result: name, register number, age, race, and the facility where held (or "released" with a release date).
4. Disambiguate common names using age/race and register number before attributing.
5. Pivot: a facility feeds `[[vinelink]]` for custody-change notifications; a "released" status with a date reframes the timeline; a no-match sends you to state systems like `[[utah]]` and county rosters.

## Inputs → Outputs
- **In:** `name` or BOP register number (`document-id`)
- **Out:** `name`, `physical-description` (age/race/sex), `address` (facility) + release date/status
- **Empty/negative result looks like:** "no matching records" — means not in federal custody since 1982. It does NOT rule out state prison, county jail, immigration detention, or a pre-1982 record.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**; official government search, no notification.
- Scope trap: federal only. Always also check state DOC and county jails before concluding a person isn't incarcerated.

## Overlaps ("do both")
- Pairs with `[[vinelink]]` — custody-status and release notifications across many jurisdictions.
- Pairs with `[[utah]]` and other state DOC locators — cover state custody the federal system won't show.

## Trust & verifiability
`trust: trusted` — first-party federal government data; a match is authoritative, bounded only by its federal-only, 1982-onward scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | federal-bureau-of-prisons-inmate-locator-us |
| category | people-search |
| selectorsIn → selectorsOut | name, document-id → name, physical-description, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
