---
id: ohio
name: Ohio
description: Use when you have a `name` and want to locate someone in Ohio state prison custody — returns incarceration status, facility, age/DOB and offender ID from the Ohio DRC offender search.
url: https://appgateway.drc.ohio.gov/offendersearch
category: public-records
path:
- public-records
bestFor: Confirming whether a named person is (or was) in Ohio state prison custody and where they are held.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official state service; no account or payment.
opsec: passive
opsecNote: Read-only search of Ohio's public offender database. The subject is not notified and the state does not tie the query to the searcher. Use a clean session for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Ohio Department of Rehabilitation and Correction (DRC) — the authoritative source for Ohio state-prison custody status.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- california
- indiana-offender-database-search
aliases:
- Ohio DRC Offender Search
- Ohio inmate search
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Ohio

> The Ohio DRC Offender Search — Ohio's official public lookup for people held in state prison, an authoritative "is this person incarcerated in Ohio?" check.

## When to use
You have a `name` (ideally with an approximate age) for someone who may be in Ohio state custody, and you need to confirm incarceration status and location. Incarceration is a common, mundane reason someone becomes unreachable, so a custody hit can quickly resolve a missing-persons lead; it also yields a verified DOB and offender number to anchor further identity work. Scope is **Ohio state prisons only** — not county jail, federal (BOP), or other states.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://appgateway.drc.ohio.gov/offendersearch.
2. Search by `name` (last/first), or by the DRC/offender number if known.
3. Read the result: matching records show name, age/`dob`, offender identification number (`document-id`), and current institution.
4. Disambiguate namesakes using age/DOB; the offender number is a strong unique anchor.
5. Pivot: for other jurisdictions use the matching locator (`[[california]]`, `[[indiana-offender-database-search]]`, or the federal BOP locator); the confirmed identity feeds court-record and people-search tools.

## Inputs → Outputs
- **In:** `name` (or DRC offender number)
- **Out:** `name`, `dob`/age, DRC `document-id`, current institution
- **Empty/negative result looks like:** no match — the person is not in Ohio *state* prison custody (they may be in county jail, federal, or another state, or not incarcerated). Absence only rules out current Ohio DRC custody.

## Gotchas & OpSec
- Scope is Ohio DRC state prisons only — county jails and federal facilities have separate locators.
- Common names return many hits; use age/DOB or the offender number to narrow.
- OpSec: **passive** — a public-records read; the subject is not alerted.

## Overlaps ("do both")
- Pairs with other state and federal custody locators — `[[california]]`, `[[indiana-offender-database-search]]`, and the federal BOP locator each cover a different jurisdiction; run the ones matching the subject's likely location.

## Trust & verifiability
`trust: trusted` — first-party Ohio DRC data; authoritative for Ohio state-prison custody status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ohio |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
