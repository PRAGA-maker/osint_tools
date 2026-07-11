---
id: south-dakota
name: South Dakota DOC Offender Lookup
description: Use when you have a `name` and want to confirm someone is/was in South Dakota state custody — returns offender records with DOB, ID number, facility/status and offense detail.
url: https://doc.sd.gov/adult/lookup
category: public-records
path:
- public-records
bestFor: Confirming and locating an adult in South Dakota Department of Corrections custody or supervision.
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
opsecNote: This is a public state-government inmate lookup — searching it does not notify the subject and leaves no trace with them. Requests hit a South Dakota state server; use a sock-puppet browser if you don't want your searches logged against your IP. Handle any returned PII in line with your legal basis.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the South Dakota Department of Corrections; an authoritative first-party government record source. Records reflect state custody/supervision only and can lag on recent releases/transfers.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- SD DOC offender lookup
- South Dakota inmate search
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# South Dakota DOC Offender Lookup

> The South Dakota Department of Corrections' public offender search — the authoritative way to check whether a person is in SD state custody or supervision, and where.

## When to use
You have a `name` and reason to think the subject may be incarcerated or under correctional supervision in South Dakota — a missing person who may be jailed, a subject you've lost contact with, or verification of a criminal-history lead. A hit confirms the person is alive, in state custody, and pins a facility/location and an offender ID you can carry to court records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://doc.sd.gov/adult/lookup.
2. Search by `name` (try surname only, and name variants/aliases — spelling in DOC systems varies).
3. Open a matching record: confirm identity via `dob`, note the offender `document-id` (DOC/ID number), current facility or supervision status, and offense/sentence detail.
4. Distinguish your subject from same-name records using DOB and physical description.
5. Pivot: the offender ID and offense feed county court-record searches; the facility gives a physical location and (via facility rules) a way to establish contact.

## Inputs → Outputs
- **In:** `name` (and aliases)
- **Out:** confirmed `name`, `dob`, offender `document-id`, facility/status, offense/sentence
- **Empty/negative result looks like:** no matching offender — the person isn't in SD state custody, is held at the county-jail level (a different system), is a juvenile, or the name is spelled differently. Absence here does not rule out incarceration elsewhere.

## Gotchas & OpSec
- State DOC only: county jail detainees, federal (BOP) inmates and out-of-state custody won't appear — check those systems separately.
- Records can lag recent bookings, releases and transfers by days.
- Common names return multiple people; always disambiguate with DOB/physical detail before acting.

## Overlaps ("do both")
- Pairs with county sheriff/jail inmate rosters, the federal `[[bop-gov]]` inmate locator, and VINELink — each covers a custody layer the others don't, so run all when locating a possibly-incarcerated subject.

## Trust & verifiability
`trust: trusted` — first-party South Dakota government data. Authoritative for state custody; just mind the recency lag and the state-only scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | south-dakota |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
