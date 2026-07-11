---
id: new-mexico
name: New Mexico Corrections Offender Search
description: Use when you have a `name` (or offender number) and want to check whether someone is in New Mexico state custody or has absconded — returns identity confirmation, dob and offender document-id.
url: https://search.cd.nm.gov
category: public-records
path:
- public-records
bestFor: Locating a person in the New Mexico state prison / probation / parole system, including absconders.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- dob
- document-id
- physical-description
status: live
pricing: free
costNote: Free public records search operated by the New Mexico Corrections Department; no account or payment.
opsec: passive
opsecNote: This is a public government database and searching it is passive — the state logs the query but the subject is not notified. No login, so use a clean browser session as routine hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the New Mexico Corrections Department (nm.gov); an authoritative first-party government source.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NMCD Offender Search
- New Mexico Corrections Department
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# New Mexico Corrections Offender Search

> The State of New Mexico's official offender lookup — confirms whether a named person is (or was) in NM prison, on probation/parole, or listed as an absconder.

## When to use
You have a `name` (or a known NMCD offender number) and need to establish custody status in New Mexico: is the person currently incarcerated, released, supervised, or absconded? Directly relevant to missing-persons work — a "missing" adult is sometimes simply in custody, and an absconder flag is a strong lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search.cd.nm.gov.
2. Enter the subject as "Last Name, First Name" or, if known, the offender number.
3. Optionally narrow with status (active / inactive / absconders only), region, and age range — the "Absconder Only" filter runs with no other input.
4. Submit and read the returned records — matching offenders with identity and status details.
5. Pivot: an offender number and dob corroborate identity for other public-records checks; a release/parole status feeds a last-known-location timeline; an absconder listing is itself a missing-person signal.

## Inputs → Outputs
- **In:** `name` (Last, First) or offender `document-id` (offender number)
- **Out:** confirmed `name`, `dob`, offender `document-id`, custody/supervision status, and typically `physical-description` fields
- **Empty/negative result looks like:** no matching offender rows returned — means not in NM state custody records; it does not rule out county jail, federal (BOP), or another state's system.

## Gotchas & OpSec
- State DOC only: this covers New Mexico *state* corrections, not county jails or the federal Bureau of Prisons. A no-hit here is not a clearance.
- Name searches can collide on common names — always corroborate with dob/offender number before asserting a match.
- OpSec: passive, first-party government data. No notification to the subject.

## Overlaps ("do both")
- Pairs with the federal `[[federal-bureau-of-prisons-inmate-locator]]` and other state DOC searches — jurisdiction matters, so run the person against the systems where they have ties.

## Trust & verifiability
`trust: trusted` — authoritative government source maintained by the New Mexico Corrections Department; the records are the state's own custody data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-mexico |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, dob, document-id, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
