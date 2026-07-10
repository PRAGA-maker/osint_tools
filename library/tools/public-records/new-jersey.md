---
id: new-jersey
name: New Jersey DOC Inmate Finder
description: Use when you have a `name` and want to check New Jersey state prison custody — returns inmate status, `document-id` (SBI/ID number), `dob`/age, and facility location.
url: https://www20.state.nj.us/doc_inmate/inmatefinder
category: public-records
path:
- public-records
bestFor: Checking whether a person is or was in New Jersey Department of Corrections custody by name.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official New Jersey Department of Corrections inmate lookup; no account or payment.
opsec: passive
opsecNote: Querying an official government inmate database is passive and does not notify the subject. Standard sock-puppet browsing hygiene applies; the search itself reaches only the state's public system.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party New Jersey Department of Corrections database — the custody data is authoritative for NJ state prisons (it does not cover county jails or federal custody).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- federal-bureau-of-prisons-inmate-locator-us
- offender-tracking-information-system-otis
aliases:
- NJ DOC Inmate Finder
- New Jersey inmate search
tags:
- court
- inmate
- new-jersey
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# New Jersey DOC Inmate Finder

> New Jersey's official state prison inmate locator — check by name whether a person is (or was) in NJ Department of Corrections custody, with ID number, age, and facility.

## When to use
You have a US subject's `name` with a possible New Jersey connection and want to check state-prison custody. A hit both locates the person (facility) and yields corroborating identifiers — an SBI/inmate `document-id`, age/`dob`, and sometimes a photo — that confirm identity and open further record trails. Custody status is directly relevant when a missing person may be incarcerated.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www20.state.nj.us/doc_inmate/inmatefinder.
2. Search by last/first `name` (try name variants and partials for spelling differences).
3. Open a matching record: note current status/facility, SBI/inmate number (`document-id`), age/`dob`, and any physical description/photo.
4. Confirm it is your subject via corroborating detail, not name alone (common names produce false matches).
5. Pivot: if not in NJ state custody, check `[[federal-bureau-of-prisons-inmate-locator-us]]` (federal) and other states' systems; the inmate ID feeds court-record lookups.

## Inputs → Outputs
- **In:** `name`
- **Out:** custody status/facility, `document-id` (SBI/inmate number), `dob`/age, physical description/photo
- **Empty/negative result looks like:** no match — the person isn't in NJ **state** custody, but could be in a county jail, federal custody, or another state; absence here is not proof they're free.

## Gotchas & OpSec
- Covers NJ **state prisons only** — not county jails or federal facilities; a clean result is jurisdiction-limited.
- Name-only matching yields namesakes; always confirm with a second identifier (DOB, photo).
- Historical/released records may be limited; the tool focuses on current/recent custody.
- OpSec: passive; official public database, no notification to the subject.

## Overlaps ("do both")
- Pairs with `[[federal-bureau-of-prisons-inmate-locator-us]]` for federal custody and `[[offender-tracking-information-system-otis]]` (Michigan) — for a thorough custody check, run the relevant state and federal locators, not just one.

## Trust & verifiability
`trust: trusted` — it is the New Jersey DOC's first-party system, so custody data is authoritative for NJ state prisons. Its only limits are jurisdictional scope and name-match ambiguity, both handled by corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-jersey |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
