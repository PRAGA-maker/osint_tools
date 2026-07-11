---
id: vinelink
name: VINELink
description: Use when you have a `name` (or offender ID) of an incarcerated person in the US and want their custody status and facility — returns location/facility (address) and custody-change alerts.
url: https://www.vinelink.com/#state-selection
category: people-search
path:
- people-search
bestFor: Checking whether a person is in US jail/prison custody, where, and getting notified of release/transfer.
selectorsIn:
- name
- dob
selectorsOut:
- address
status: live
pricing: free
costNote: Completely free — funded through corrections agencies via Appriss/Equifax. No account needed to search; free registration only if you want release/transfer notifications.
opsec: passive
opsecNote: Searching the offender database is anonymous and does not alert the subject. Only registering for notifications requires your contact details — use a dedicated contact if you want separation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The national VINE (Victim Information and Notification Everyday) service, operated under contract with state/county corrections agencies; authoritative for custody status where a facility participates.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- VINE
- Victim Information and Notification Everyday
tags:
- people-investigations
- inmate
- corrections
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# VINELink

> The national offender-lookup and victim-notification portal: is this person in custody, where, and tell me if that changes.

## When to use
You have a `name` (ideally plus `dob` or an offender ID to disambiguate) and need to know whether the subject is currently incarcerated in a US jail or prison, at which facility, and their custody status. For a missing-persons workflow this both locates a subject who is in custody and rules incarceration in or out. You can also register to be alerted the moment their status changes (release, transfer, escape).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.vinelink.com/ and select the relevant state.
2. Search by offender `name` (and refine with `dob`/ID where prompted); jurisdictions with many matches will list candidates.
3. Read the record: current custody status (in custody / released), the facility, and available identifiers.
4. (Optional) Register a phone/email/text contact to receive automatic notifications on custody changes.
5. Pivot: a confirmed facility (`address`) narrows the search geographically; a "released" status with a date reframes the timeline and hands off to booking/court records.

## Inputs → Outputs
- **In:** `name` (+ `dob`/offender ID to disambiguate)
- **Out:** custody status, holding facility (`address`), and optional ongoing change notifications
- **Empty/negative result looks like:** "no offender found." This is NOT proof the person was never held — coverage is per-facility (48 states; South Dakota uses SAVIN), some jails don't feed VINE, and spelling/ID mismatches hide records. Treat a miss as inconclusive.

## Gotchas & OpSec
- Coverage is uneven: VINE aggregates ~2,900 agencies but not every jail participates, and data freshness varies by facility.
- Disambiguate common names with DOB/ID; act on the wrong record and the whole timeline is wrong.
- OpSec: **passive** — searching is anonymous; only notification registration exposes a contact.

## Overlaps ("do both")
- Pairs with state DOC inmate locators and county jail booking sites — VINE is the aggregator, but the originating facility's own locator is often more current and detailed; run both when custody is in question.

## Trust & verifiability
`trust: trusted` — an official corrections-partnered service, so a positive custody hit is authoritative; confirm against the specific facility's locator for court-usable detail.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vinelink |
| category | people-search |
| selectorsIn → selectorsOut | name, dob → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
