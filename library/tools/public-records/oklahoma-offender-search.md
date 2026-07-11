---
id: oklahoma-offender-search
name: Oklahoma Offender Search
description: Use when you have a `name` and want to confirm someone is/was in Oklahoma state custody or supervision — returns offender records with DOB, DOC number, facility/status and offense detail.
url: https://okoffender.doc.ok.gov
category: public-records
path:
- public-records
bestFor: Confirming and locating an adult in Oklahoma Department of Corrections custody, probation or parole.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free public government record search; no account or payment.
opsec: passive
opsecNote: A public Oklahoma DOC lookup — searching does not notify or reach the subject. Requests hit an Oklahoma state server; use a sock-puppet browser if you'd rather your searches not be logged against your IP, and handle returned PII within your legal basis.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Oklahoma Department of Corrections; authoritative first-party government data covering state custody/supervision. Recent bookings, releases and transfers can lag.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Oklahoma DOC offender lookup
- OK DOC inmate search
- okoffender
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Oklahoma Offender Search

> The Oklahoma Department of Corrections' public offender lookup — the authoritative way to check whether a person is in OK state custody or supervision, and where.

## When to use
You have a `name` and think the subject may be incarcerated, on probation or on parole in Oklahoma — a missing person who may be jailed, a subject you've lost contact with, or a criminal-history lead to verify. A hit confirms the person is alive, in the OK correctional system, and gives a facility/location plus a DOC number that carries into court records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://okoffender.doc.ok.gov.
2. Search by `name` (try surname only and known aliases; DOC spelling varies).
3. Open a matching record: confirm with `dob`, note the DOC `document-id`, current facility or supervision status, and offense/sentence detail.
4. Separate your subject from same-name records using DOB and physical description.
5. Pivot: the DOC number and offense feed Oklahoma court-record (OSCN/ODCR) searches; the facility gives a physical location and contact route.

## Inputs → Outputs
- **In:** `name` (and aliases)
- **Out:** confirmed `name`, `dob`, DOC `document-id`, facility/status, offense/sentence
- **Empty/negative result looks like:** no matching offender — the subject isn't in OK state custody, is held at a county jail (separate system), is federal (BOP), or the name is spelled differently. Absence doesn't rule out incarceration elsewhere.

## Gotchas & OpSec
- State DOC only: county jail, tribal, federal and out-of-state custody won't appear here.
- Records lag recent bookings/releases/transfers by days.
- Common names return multiple hits — always disambiguate with DOB/physical detail before acting.

## Overlaps ("do both")
- Pairs with Oklahoma county sheriff jail rosters, court portals (OSCN/ODCR), the federal `[[bop-gov]]` locator and VINELink — each covers a custody/records layer the others miss.

## Trust & verifiability
`trust: trusted` — first-party Oklahoma government data; authoritative for state custody, subject only to recency lag and the state-only scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oklahoma-offender-search |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
