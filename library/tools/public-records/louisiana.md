---
id: louisiana
name: Louisiana
description: Use when you have a `name` and want to check whether a person is in Louisiana state prison custody — returns incarceration status, `dob`, and DOC `document-id` (offender number).
url: https://doc.louisiana.gov/imprisoned-person-programs-resources/offender-information
category: public-records
path:
- public-records
bestFor: Confirming Louisiana state DOC custody and pulling an offender's DOC number and facility.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official Louisiana Department of Public Safety & Corrections resource.
opsec: passive
opsecNote: Querying a government inmate resource is passive and not disclosed to the subject. Records are public; still work from a clean browser to avoid tying searches to you.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Louisiana DOC (doc.louisiana.gov); authoritative for state-custody status, though it covers only state DOC facilities, not parish jails or federal custody.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Louisiana DOC offender information
- Louisiana Department of Corrections inmate lookup
tags:
- court
- inmate
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Louisiana

> The Louisiana Department of Public Safety & Corrections offender-information resource — the authoritative check for whether a person is in Louisiana *state* prison custody, and their DOC number and facility.

## When to use
You have a `name` and a possible Louisiana connection, and need to rule in/out state incarceration — a common branch in a missing-persons or locate case (someone who "dropped off the map" may be in custody). A hit confirms the person is alive and located, and yields a DOC offender number (`document-id`) and `dob` to disambiguate namesakes and to request further records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://doc.louisiana.gov/imprisoned-person-programs-resources/offender-information and follow it to the offender lookup / information-request path.
2. Search or request by `name` (and DOB if you have it). Some detail is via an online locator; some requires the DOC's information-request process.
3. Read results: custody status, facility, DOC offender number, and identifying detail.
4. Pivot: the DOC number and confirmed DOB feed court-record and background lookups; the facility tells you where the person physically is.

## Inputs → Outputs
- **In:** `name` (optionally + `dob`)
- **Out:** custody status, facility, DOC `document-id` (offender number), `dob`
- **Empty/negative result looks like:** no match — means not in *state* DOC custody; the person could still be in a parish jail, federal custody, or another state. Absence here is not proof they aren't incarcerated.

## Gotchas & OpSec
- **Scope is state DOC only** — parish/county jails and federal (BOP) custody are separate systems; check those too before concluding.
- Human-in-the-loop / **manual-review**: some records come via a DOC information-request rather than instant lookup; expect a form/wait.
- OpSec: **passive** — inmate records are public and the subject isn't notified.

## Overlaps ("do both")
- Pairs with federal BOP and parish-jail locators — run all custody systems in parallel, since a subject in Louisiana could be in any of them.

## Trust & verifiability
`trust: trusted` — it is the state corrections department's own data, authoritative for state custody; just remember its coverage boundary (state facilities only).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | louisiana |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
