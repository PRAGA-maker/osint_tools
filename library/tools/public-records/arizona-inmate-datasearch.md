---
id: arizona-inmate-datasearch
name: Arizona Inmate Datasearch (ADCRR)
description: Use when you have a `name` and want to check Arizona state prison custody — returns inmate records with ADC number, DOB, status and facility location.
url: https://corrections.az.gov/public-resources/inmate-datasearch
category: public-records
path:
- public-records
bestFor: Confirming whether a person is or was in Arizona Department of Corrections custody and pulling their inmate record.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
- physical-description
status: live
pricing: free
costNote: Free public search operated by the Arizona Department of Corrections, Rehabilitation & Reentry (ADCRR); no account required.
opsec: passive
opsecNote: You query an official public corrections database, not the subject, so nobody is alerted. Records are public but sensitive — use them lawfully and avoid re-publishing personal data unnecessarily.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Arizona state corrections record system; authoritative for Arizona DOC custody, though it covers only Arizona state prisons (not county jails or federal/BOP custody).
missingPersonsRelevance: high
coverage:
- us-az
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- court-electronic-records-pacer
aliases:
- ADCRR inmate search
- Arizona DOC inmate datasearch
tags:
- court
- inmate
- corrections
- arizona
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Arizona Inmate Datasearch (ADCRR)

> Arizona's official state-prison inmate lookup — search by name or ADC number to confirm custody and read the inmate record (DOB, status, facility, physical description).

## When to use
You have a `name` (or an ADC number) and want to know if the person is, or has been, in Arizona state prison custody. Custody status can explain a person's whereabouts in a missing-person or locate case, and the record adds corroborating identifiers (date of birth, physical description, admission/release dates, current facility). It is Arizona-only and covers state prisons, not county jails or federal custody.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://corrections.az.gov/public-resources/inmate-datasearch.
2. Search by last/first `name` (or ADC inmate number if known).
3. Open the matching record: ADC number (`document-id`), `dob`, status (in custody / released / community supervision), facility/location, and physical description.
4. Use DOB and description to disambiguate same-name matches.
5. Pivot: a release date/location narrows a whereabouts timeline; for federal matters check `[[court-electronic-records-pacer]]`, and use county jail rosters for pre-conviction custody.

## Inputs → Outputs
- **In:** `name` (or ADC number)
- **Out:** `name`, `dob`, `document-id` (ADC number), custody status, facility, and `physical-description`
- **Empty/negative result looks like:** no match — the person isn't in Arizona *state* custody (they may be in a county jail, another state, or federal custody, or never incarcerated); absence isn't proof of anything beyond ADCRR.

## Gotchas & OpSec
- **Arizona state prisons only** — not county jails, not federal BOP; check those separately.
- Same-name collisions happen; confirm with DOB/description before attributing.
- OpSec: passive public-record query; handle the personal data responsibly.

## Overlaps ("do both")
- Complements `[[court-electronic-records-pacer]]` (federal cases) and county jail/other-state DOC lookups — do the relevant ones to cover all custody layers.

## Trust & verifiability
`trust: trusted` — authoritative Arizona corrections data; the only caveat is scope (Arizona state prisons), so pair with other custody sources for a complete picture.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arizona-inmate-datasearch |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
