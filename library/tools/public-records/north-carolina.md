---
id: north-carolina
name: North Carolina Offender Search
description: Use when you have a `name` and want to check North Carolina prison/probation/parole records — returns `name`, `dob`, `document-id` (offender number), status and location.
url: https://webapps.doc.state.nc.us/opi/offendersearch.do?method=view
category: public-records
path:
- public-records
bestFor: Confirming and locating a person in the North Carolina state correctional system (prison, probation, parole).
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official state search; no account or payment.
opsec: passive
opsecNote: Official NC Department of Adult Correction database; searching is passive and needs no login. Nothing is sent to the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the NC Department of Adult Correction (formerly under NC DPS); authoritative government correctional record.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NC DPS offender search
- NC DAC Offender Public Information Search
- North Carolina inmate search
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# North Carolina Offender Search

> The NC Department of Adult Correction's Offender Public Information Search: a free, authoritative check on whether a person is (or was) in North Carolina's prison, probation or parole system.

## When to use
You have a `name` and want to establish whether the subject is incarcerated, on probation/parole, or has a NC correctional history — a fast way to explain a disappearance, confirm current custody/location, or corroborate identity via DOB and offender number. The database holds current and historical records back to 1972 (state system only, not county jails).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Offender Public Information Search (the tool moved from ncdps.gov to the NC Department of Adult Correction — https://www.dac.nc.gov/dac-services/criminal-offender-searches, which links the live search app).
2. Enter the subject's last and first name (or offender number if known) and submit.
3. Click an offender number in the results to open the record: status, current facility/location, offense, DOB, and projected release date.
4. Use DOB + offender number to disambiguate common names.
5. Pivot: feed confirmed identity/DOB into other public records; a current facility narrows whereabouts.

## Inputs → Outputs
- **In:** `name` (or offender number)
- **Out:** `name`, `dob`, `document-id` (offender number), custody status, facility/location, offense, release date
- **Empty/negative result looks like:** no match — the person isn't in the NC **state** system; they may be in a county jail (not covered), another state, or federal custody (use those systems instead).

## Gotchas & OpSec
- Covers the NC state correctional system only — **not** county jail inmates; check the relevant county sheriff for those.
- The old ncdps.gov URL now 404s; the search lives under the Department of Adult Correction (dac.nc.gov).
- Common names return many hits — confirm with DOB/offender number before asserting a match.

## Overlaps ("do both")
- Pairs with county sheriff jail lookups and the federal BOP inmate locator — each system covers a different slice of custody.

## Trust & verifiability
`trust: trusted` — an official state correctional database; records are authoritative. Verify identity via DOB/offender number rather than name alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | north-carolina |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
