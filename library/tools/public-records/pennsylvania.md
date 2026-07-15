---
id: pennsylvania
name: Pennsylvania DOC Inmate Locator
description: Use when you have a `name` and want to know if the subject is (or recently was) in Pennsylvania state custody — returns inmate identity, DOB, inmate number and facility from the official PA Department of Corrections locator.
url: http://inmatelocator.cor.pa.gov
category: public-records
path:
- public-records
bestFor: Confirming whether a person is incarcerated or supervised in the Pennsylvania state corrections system and pulling their inmate record.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
- address
status: live
pricing: free
costNote: Free official government inmate locator; no account or payment needed.
opsec: passive
opsecNote: Official public-records search; you query the state database, not the individual, and no notification is sent. No login required. Use a clean session as routine hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Pennsylvania Department of Corrections (cor.pa.gov); records are authoritative for people in PA state custody (note it does not cover county jails or federal prison).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- PA DOC Inmate Locator
- Pennsylvania Department of Corrections locator
- inmatelocator.cor.pa.gov
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Pennsylvania DOC Inmate Locator

> Pennsylvania's official Department of Corrections locator: check whether a person is in state custody and pull their inmate identity, DOB, number and facility.

## When to use
You have a `name` and need to know whether the subject is incarcerated or under supervision in the Pennsylvania *state* corrections system. A hit is a strong locate — it places the person at a specific facility with an inmate `document-id` and confirms `dob`/identity. Valuable in a missing-person case when the explanation may be custody rather than disappearance. Remember it covers PA *state* prisons/parole only, not county jails or federal facilities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://inmatelocator.cor.pa.gov (the "Inmate/Department Supervised Individual Locator").
2. Search by `name` (last/first); some fields allow the inmate number if you already have one.
3. Read the result: full `name`, `dob`, inmate/control number (`document-id`), current facility/`address`, and status (incarcerated / paroled / released where shown).
4. Disambiguate common names by DOB/age and race/sex fields; confirm you have the right individual before relying on it.
5. Pivot: the facility feeds visitation/records requests; the inmate number feeds court-record lookups; confirmed DOB/identity feeds people-search corroboration.

## Inputs → Outputs
- **In:** `name` (or inmate number)
- **Out:** `name`, `dob`, inmate number (`document-id`), facility `address`, custody status
- **Empty/negative result looks like:** no match — meaning the person isn't in PA *state* custody, NOT that they're free (they could be in a PA county jail, federal prison, or another state's system).

## Gotchas & OpSec
- Scope: PA state DOC only — county jails and federal BOP are separate systems; check those too before concluding someone isn't incarcerated.
- Human-in-the-loop: none — open official search.
- OpSec: fully passive; a government public-records lookup that never touches the subject.

## Overlaps ("do both")
- Pairs with the federal BOP inmate locator and county jail rosters — each covers a different custody system, so run all three when you suspect incarceration.

## Trust & verifiability
`trust: trusted` — it is the Pennsylvania DOC's own locator, so records are authoritative for state custody; just remember its coverage boundary (state only) when interpreting a "no match."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pennsylvania |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
