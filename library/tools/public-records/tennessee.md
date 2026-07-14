---
id: tennessee
name: Tennessee FOIL (Felony Offender Information Lookup)
description: Use when you have a `name` (or TDOC number) and think the subject has been in Tennessee state custody — returns the offender record: photo, status, location/facility, offense, sentence and `dob`.
url: https://www.tn.gov/correction/agency-services/foil.html
category: public-records
path:
- public-records
bestFor: Confirming whether a named person is or was a Tennessee felony offender and reading their custody status, location and sentence.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
- physical-description
status: live
pricing: free
costNote: Free official state service; also available via the free MyTN / TN Felony Offender Search mobile app. No account or payment.
opsec: passive
opsecNote: A read-only search of an official corrections database — the subject is not notified. The State of Tennessee sees your IP/query; use a sock-puppet browser for a sensitive name.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Tennessee Department of Correction system; authoritative for TN state felony custody status (does not cover county jail or out-of-state records).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- court-records-directory
aliases:
- Tennessee FOIL
- TN Felony Offender Information Lookup
- TDOC offender search
tags:
- court
- inmate
- corrections
- tennessee
source: metaosint
lastVerified: '2026-07-13'
enrichment: full
---

# Tennessee FOIL (Felony Offender Information Lookup)

> Tennessee's official offender search — a name (or TDOC number) resolves to a felon's custody status, location, offense, sentence and DOB.

## When to use
You have a `name` and reason to think the subject has been in Tennessee state custody (currently or previously). FOIL confirms the person's existence in the corrections system and returns a photo, status (incarcerated / probation / parole / inactive), current location or supervising office, the offense, sentence details, and `dob` — all strong identity-and-location anchors for a missing-person or background trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tn.gov/correction/agency-services/foil.html (or the MyTN / TN Felony Offender Search app).
2. Search by name, state ID, or TDOC number; a TDOC number pins an exact record.
3. Read the record: photo (`physical-description`), status, facility/location, offense, sentence, parole/release info, and `dob`.
4. Disambiguate a common name using the photo and `dob`.
5. Pivot: the facility/location is a current-whereabouts lead; the offense and `dob` feed court-record and background searches — e.g. `[[court-records-directory]]` for the underlying case.

## Inputs → Outputs
- **In:** `name` or TDOC number
- **Out:** confirmed `name`, `dob`, `document-id` (TDOC number), `physical-description` (photo), status, facility/location, offense, sentence
- **Empty/negative result looks like:** no match — the person was never in TN *state* felony custody. This does not rule out county-jail, out-of-state, or federal custody; check those separately.

## Gotchas & OpSec
- Scope is Tennessee **state** felony offenders only — county jail bookings and other states/federal are not here.
- Historical records persist, so a hit may be years old; read the status/date before treating a location as current.
- OpSec: fully passive; a routine public-records lookup with no subject notification.

## Overlaps ("do both")
- Pairs with `[[court-records-directory]]` — FOIL gives the corrections view (custody, sentence), while the court directory routes you to the underlying case file and other jurisdictions.

## Trust & verifiability
`trust: trusted` — first-party Tennessee DOC data; a match is authoritative for state felony custody status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tennessee |
