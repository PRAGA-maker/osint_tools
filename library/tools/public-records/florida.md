---
id: florida
name: Florida DOC Offender Search
description: Use when you have a `name` (or DC number) and want to check Florida state custody, supervision or release status — returns identity confirmation, dob, offender document-id and physical description.
url: http://www.dc.state.fl.us/offendersearch
category: public-records
path:
- public-records
bestFor: Locating a person in Florida's state prison/supervision system, including current inmates, offenders on supervision, and released offenders.
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
costNote: Free public records search operated by the Florida Department of Corrections; no account or payment.
opsec: passive
opsecNote: A public government database; searching is passive and the subject is not notified. No login required — use a clean browser session as routine hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Florida Department of Corrections (the dc.state.fl.us domain now redirects to fdc.myflorida.com); authoritative first-party government data.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Florida Department of Corrections
- FDC offender search
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Florida DOC Offender Search

> Florida's official offender lookup — confirm whether a named person is in Florida state custody or supervision (and Florida publishes unusually rich offender detail, including photos and release dates).

## When to use
You have a `name` (or a Florida DC number) and need custody status in Florida: currently incarcerated, on community supervision, or released. Florida's system is notably detailed (mugshots, physical description, release/supervision dates), making it strong for identity confirmation and locate work — a reported-missing adult may in fact be in FDC custody or recently released.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.dc.state.fl.us/offendersearch (redirects to the current FDC site at fdc.myflorida.com).
2. Choose the population (inmates, supervised offenders, or released offenders) and enter the subject's name or DC number.
3. Submit and read the returned record(s): identity, dob, photo, physical description, current status/facility, and supervision/release dates.
4. Pivot: a DC number + dob corroborate identity across records; release/supervision status and dates anchor a whereabouts timeline; the photo aids visual ID and reverse-image checks.

## Inputs → Outputs
- **In:** `name` or offender `document-id` (DC number)
- **Out:** confirmed `name`, `dob`, offender `document-id`, `physical-description` (and typically a photo), custody/supervision/release status
- **Empty/negative result looks like:** no matching offender returned — means not in Florida *state* corrections records; it does not rule out county jail, federal (BOP) custody, or another state.

## Gotchas & OpSec
- State DOC scope only: county jails and the federal Bureau of Prisons are separate — a no-hit here is not a clearance.
- Common-name collisions: confirm with dob/DC number before asserting a match.
- OpSec: passive, authoritative government data; no subject notification.

## Overlaps ("do both")
- Pairs with the federal `[[federal-bureau-of-prisons-inmate-locator]]` and other states' DOC searches (`[[maryland]]`, `[[new-mexico]]`, `[[wisconsin]]`) — run the subject against every jurisdiction where they have ties.

## Trust & verifiability
`trust: trusted` — first-party Florida state government source; the records are the department's own custody, supervision and release data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | florida |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, dob, document-id, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
