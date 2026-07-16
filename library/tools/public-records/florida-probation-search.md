---
id: florida-probation-search
name: Florida Probation Search
description: Use when you have a `name` and want to check Florida Department of Corrections inmate, probation, or supervision status — returns `name`, `dob`, `document-id` (DC number), custody/supervision status, and location.
url: http://www.dc.state.fl.us/offendersearch/search.aspx
category: public-records
path:
- public-records
bestFor: Confirming whether a person is a Florida DOC inmate, on probation, or under community supervision.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free public government database; no account or payment. (The old dc.state.fl.us host redirects to fdc.myflorida.com.)
opsec: passive
opsecNote: An official public-records lookup — you query the state database, nothing reaches the subject. No login; a sock puppet is optional but tidy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Florida Department of Corrections offender database; authoritative for people under FDC jurisdiction, updated regularly.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Florida DOC offender search
- FDC offender search
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- florida
---

# Florida Probation Search

> The Florida Department of Corrections offender database — confirm whether a person is a Florida inmate, on probation, or under community supervision, with their DC number and location.

## When to use
You have a `name` (or a DC number) and need to establish whether the subject is under Florida DOC jurisdiction — incarcerated, on probation, or on community supervision. A fast way to explain a person's whereabouts, confirm identity via DOB, and (for those in custody) get a facility/mailing location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.dc.state.fl.us/offendersearch/search.aspx (redirects to the current FDC host, fdc.myflorida.com).
2. Search by last/first name, or by DC number; you can filter by status (inmate, supervised/probation, absconder, etc.).
3. Read the results: matched `name`, DC number (`document-id`), `dob`/race/sex, current status, and facility or supervision office.
4. Open a record for offense details, release date, and (for absconders) last-known information.
5. Pivot: use DC number + DOB to disambiguate common names; cross-check county clerk of courts for the underlying case.

## Inputs → Outputs
- **In:** `name` (last/first) or DC number
- **Out:** `name`, `dob`, `document-id` (DC number), custody/supervision status, facility/office location, offense/release detail
- **Empty/negative result looks like:** no match — the person is not (currently) under FDC jurisdiction, or completed supervision. Absence isn't proof of no record; check county jails and court databases too.

## Gotchas & OpSec
- Scope is Florida DOC (state prison + state supervision) — county jails, other states, and federal (BOP) custody are elsewhere.
- Includes an absconder/fugitive category useful when someone has skipped supervision.
- Passive and free.

## Overlaps ("do both")
- Pairs with the federal BOP inmate locator, other states' DOC tools (e.g. `[[idaho]]`), and Florida county clerk-of-court sites — if FDC returns nothing, the subject may be held under a different jurisdiction.

## Trust & verifiability
`trust: trusted` — an official state corrections database, authoritative for current FDC jurisdiction; verify identity via DC number/DOB before acting on a name match.
