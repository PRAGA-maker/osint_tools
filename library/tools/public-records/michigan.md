---
id: michigan
name: Michigan OTIS (Offender Tracking Information System)
description: Use when you have a `name` and want to check whether someone is or was recently under Michigan corrections supervision — returns name, dob, physical-description, offender number, and facility/location.
url: https://www.michigan.gov/corrections/0,4551,7-119-1409---,00.html
category: public-records
path:
- public-records
bestFor: Locating a person currently in Michigan prison/parole/probation, or discharged within the last 3 years.
selectorsIn:
- name
selectorsOut:
- name
- dob
- physical-description
- document-id
- geolocation
status: live
pricing: free
costNote: Free official state government database (Michigan Department of Corrections). No account or payment.
opsec: passive
opsecNote: A public records query against a state database; the subject is not notified and nothing is sent to them. Standard practice is still to search from a research browser, not an account tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Michigan Department of Corrections; the authoritative source for that state's supervised-offender data (with the state's own disclaimers about currency/completeness).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- OTIS
- Michigan Offender Tracking Information System
- Michigan DOC offender search
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Michigan OTIS (Offender Tracking Information System)

> Michigan's official public corrections database — search a name to see if someone is a current or recently-discharged prisoner, parolee, or probationer, and where.

## When to use
You have a `name` and a reason to think the person may be, or recently was, in the Michigan corrections system. A hit locates them (facility or supervision status) and returns identifying details you can use to confirm you have the right person and to pivot — physical description, date of birth, offender number, offenses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Michigan DOC / OTIS page and launch the offender search.
2. Enter the subject's `name` (last/first); add DOB or offender number to disambiguate common names.
3. Read the record: current status/location, offender number, DOB, race/sex, physical description, offenses, and any photo.
4. Pivot: the offender number (`document-id`) is a stable key; the facility is a current `geolocation`; DOB/physical description corroborate identity against other records.

## Inputs → Outputs
- **In:** `name` (optionally DOB / offender number to narrow)
- **Out:** `name`, `dob`, `physical-description`, offender `document-id`, current facility/supervision `geolocation`, offense history, photo
- **Empty/negative result looks like:** "no records found" — means not currently supervised and not discharged within ~3 years. It does NOT prove no record: county-jail inmates, pre-sentence arrestees, and older discharges are excluded (use Michigan State Police ICHAT for historical criminal history).

## Gotchas & OpSec
- Scope limits: OTIS only covers state prisoners/parolees/probationers and discharges within 3 years — not county jails, not the unsentenced, not old records.
- Common names return multiple hits; confirm with DOB, offender number, or photo before asserting a match.
- OpSec: passive public-records lookup; no notification to the subject.

## Overlaps ("do both")
- Pairs with other states' DOC/inmate locators and the federal BOP locator when you don't know which jurisdiction holds the person — run the same name across each. Historical Michigan criminal history needs ICHAT, not OTIS.

## Trust & verifiability
`trust: trusted` — first-party Michigan Department of Corrections data. Authoritative for what it covers, with the department's standard caveat that entries can be outdated or incomplete; verify a life-affecting conclusion against the official record directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | michigan |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, physical-description, document-id, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
