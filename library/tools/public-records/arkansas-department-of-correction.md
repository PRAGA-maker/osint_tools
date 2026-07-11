---
id: arkansas-department-of-correction
name: Arkansas Department of Correction
description: Use when you have a `name` of someone who may be incarcerated in Arkansas and want their inmate record — returns `name`, `dob`/age, ADC `document-id`, facility, and status.
url: https://apps.ark.org/inmate_info/index.php
category: public-records
path:
- public-records
bestFor: Confirming whether a person is (or was) an Arkansas state prison inmate and pulling their offender record.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official Arkansas state inmate lookup; no account required.
opsec: passive
opsecNote: Searching a public government inmate database is passive and does not notify anyone. No login is needed; treat the personal/criminal data returned responsibly and lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Arkansas state service (apps.ark.org / Arkansas Division of Correction); the offender data is authoritative public record.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Arkansas Division of Correction inmate search
- ADC inmate lookup
tags:
- court
- inmate
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Arkansas Department of Correction

> Arkansas's official state inmate search — confirm incarceration status and pull an offender's record by name.

## When to use
You are tracing a subject who may be incarcerated in Arkansas state prison, or you want to confirm/explain a person's whereabouts, a custody-related gap, or a criminal history lead. An inmate hit yields the person's name, approximate age/DOB, an ADC offender number, current facility, and sentence/status — a strong locate-and-confirm signal in missing-persons and background work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://apps.ark.org/inmate_info/index.php.
2. Search by `name` (last/first); you can often refine by ADC number if known.
3. Open the matching record: read the inmate `name`, age/`dob`, ADC offender number (`document-id`), housing facility, admission date, and status.
4. Disambiguate common names by age and offense details before trusting a match.
5. Pivot: the ADC number and facility feed court-record and visitation lookups; a confirmed custody status redirects or closes a locate.

## Inputs → Outputs
- **In:** `name` (of a possible Arkansas state inmate)
- **Out:** `name`, age/`dob`, ADC `document-id`, facility, admission/status
- **Empty/negative result looks like:** no match — the person may be in a county jail or federal custody (not ADC), released, or held in another state. Absence here only rules out current Arkansas state-prison custody, not incarceration generally.

## Gotchas & OpSec
- State-prison only: county jail and federal (BOP) inmates won't appear — check those separately.
- Records reflect ADC custody; recently released people may drop off.
- Common names require age/offense disambiguation.

## Overlaps ("do both")
- Pairs with the federal `[[bop-inmate-locator]]` and county jail rosters / `[[vinelink]]` — ADC covers Arkansas state prisons, while those cover federal and local custody the state database omits.

## Trust & verifiability
`trust: trusted` — official Arkansas state government service; offender data is authoritative public record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arkansas-department-of-correction |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
