---
id: idaho
name: Idaho (IDOC Offender Search)
description: Use when you have a `name` and want to check Idaho Department of Correction custody/probation/parole status — returns `name`, `document-id` (IDOC number), custody status, location, and felony listing.
url: https://www.idoc.idaho.gov/content/prisons/offender_search
category: public-records
path:
- public-records
bestFor: Confirming whether a person is currently incarcerated, on probation, or on parole under Idaho DOC jurisdiction.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- address
status: live
pricing: free
costNote: Free public government database; no account or payment required.
opsec: passive
opsecNote: An official public-records lookup — you query the state database, nothing reaches the subject. No login, so no attribution beyond your IP; a sock puppet is optional but tidy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Idaho Department of Correction system; authoritative for people currently under IDOC jurisdiction, updated daily.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Idaho Department of Correction offender search
- IDOC offender search
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Idaho (IDOC Offender Search)

> The Idaho Department of Correction's public offender lookup — confirm whether a person is incarcerated, on probation, or on parole in Idaho, with their DOC number and location.

## When to use
You have a `name` (or an IDOC number) and need to establish whether the subject is currently under Idaho DOC jurisdiction — a fast way to explain a person's whereabouts (a missing adult may be in custody), confirm identity via DOB/felony listing, or obtain a mailing address for someone in custody.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.idoc.idaho.gov/content/prisons/offender_search.
2. Search by last name (min 2 chars) + optional first name, or by IDOC number (min 3 digits).
3. Read the results: matched `name`, IDOC number (`document-id`), current custody status and facility/location, and the felony listing for those serving time.
4. For people in custody, note the provided mailing `address`.
5. Pivot: use the DOC number and DOB to disambiguate common names; cross-check court-records tools for the underlying case.

## Inputs → Outputs
- **In:** `name` (last + optional first) or IDOC number
- **Out:** `name`, `document-id` (IDOC number), custody status, facility/location, felony listing, mailing `address` (once in custody)
- **Empty/negative result looks like:** no match — the person is not currently (and may never have been) under IDOC jurisdiction, OR they completed their sentence (past offenders can appear but their convictions are hidden). Absence is not proof of no record; check court databases too.

## Gotchas & OpSec
- Scope is Idaho DOC only — county jails, other states, and federal (BOP) custody are elsewhere.
- People who finished their sentences may show with convictions suppressed; a bare name with no detail can still be a real prior offender.
- Updated daily but may lag real-time status.

## Overlaps ("do both")
- Pairs with the federal BOP inmate locator and other state DOC/VINELink tools — if Idaho returns nothing, the subject may be held under a different jurisdiction.

## Trust & verifiability
`trust: trusted` — an official state corrections database, authoritative for current IDOC jurisdiction; treat historical/completed-sentence entries with the noted suppression caveats.
