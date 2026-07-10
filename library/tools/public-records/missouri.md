---
id: missouri
name: Missouri (DOC Offender Search)
description: Use when you have a `name` and want to check whether a subject is in Missouri Department of Corrections custody or supervision — returns offender record with DOC ID, status, and location.
url: https://web.mo.gov/doc/offsearchweb
category: public-records
path:
- public-records
bestFor: Confirming Missouri DOC incarceration/supervision status and DOC number for a named person.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- physical-description
- address
status: live
pricing: free
costNote: Free official public offender search operated by the Missouri Department of Corrections; no account or payment.
opsec: passive
opsecNote: Passive — you query a state corrections public-records system, not the subject. The offender is not notified. Standard government-site logging applies; use a clean browser if you want to avoid attributing the query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Missouri Department of Corrections — authoritative for offenders in MODOC custody/supervision; scope is MODOC only, not county jails or full criminal history.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Missouri DOC offender search
- MODOC offender web search
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Missouri (DOC Offender Search)

> The Missouri Department of Corrections' public offender web search — check a name against people in MODOC custody or under supervision and pull their DOC number, status, and location.

## When to use
You have a `name` and a Missouri nexus and need an authoritative check on whether the subject is in Missouri state prison custody or on probation/parole. It confirms and enriches a lead surfaced by a commercial aggregator like `[[state-and-county-jail-inmate-locators]]`, and the DOC number anchors identity for further records work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://web.mo.gov/doc/offsearchweb.
2. Search by last + first `name` (or by DOC number `document-id` if known).
3. Open a matching record to read: offender `name`, DOC ID, custody/supervision status, and facility or supervising district (`address`/location).
4. Match on name plus available detail (DOB/physical description) — common names collide.
5. Pivot: the facility/district gives a location; the DOC number is a stable identifier for records requests; status tells you whether the person is reachable via a parole office.

## Inputs → Outputs
- **In:** `name` (or DOC number)
- **Out:** offender `name`, DOC ID (`document-id`), custody/supervision status, facility/district (`address`), `physical-description`
- **Empty/negative result looks like:** "no records found" — meaning not in MODOC custody/supervision. This does NOT cover Missouri county jails, out-of-state prisons, or full criminal history; a clean result here isn't a clean record overall.

## Gotchas & OpSec
- Scope is Missouri state DOC only — for county detention check the county sheriff; for other states use their DOC (e.g. `[[kansas]]`, `[[colorado]]`, `[[oregon-offender-search]]`).
- Data can lag between updates — a recently released/admitted person may be briefly out of sync.
- Confirm identity with the DOC number/details before acting; name-only matches are unreliable.
- Passive and free; no login.

## Overlaps ("do both")
- Confirms hits from `[[state-and-county-jail-inmate-locators]]` (aggregator → authoritative source).
- Parallel to `[[kansas]]`, `[[colorado]]`, `[[oregon-offender-search]]` for other states, and `[[sex-offender-search]]` for the registry angle.

## Trust & verifiability
`trust: trusted` — it is the Missouri DOC's own public system, authoritative for who is in MODOC custody/supervision. Its limits are scope (MODOC only) and update lag, not authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | missouri |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, physical-description, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
