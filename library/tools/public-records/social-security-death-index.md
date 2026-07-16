---
id: social-security-death-index
name: Social Security Death Index
url: https://stevemorse.org/ssdi/ssdi.html
category: public-records
path:
- public-records
description: Use when you have a US `name` and want to confirm a death — returns death date, birth date (`dob`), and last-residence location from the SSA Death Master File.
bestFor: Confirming whether a US person is deceased and getting their DOB, death date and last-residence area via the SSDI.
selectorsIn:
- name
- dob
selectorsOut:
- dob
- name
- address
status: live
pricing: freemium
costNote: Steve Morse's SSDI search forms are free; they query back-end databases (Ancestry/FamilySearch/etc.) that may themselves require a free or paid account for full record detail.
opsec: passive
opsecNote: A passive search of a public death index; the subject is deceased and no one is notified. The Steve Morse forms run in your browser and pass the query to a chosen backend — standard clean-browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Steve Morse's tools are a respected, long-standing genealogy portal that front-ends official SSA Death Master File data; the underlying index is authoritative for deaths reported to the SSA (roughly 1962 onward).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- SSDI
- SSDI search (Steve Morse)
- Death Master File
tags:
- genealogy
- death-records
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- brooklyn-genealogy
- chicago-cook-county-genealogy
- decoding-social-security-numbers
- encoding-and-decoding-driver-s-license-numbers
- familysearch-s-united-states-record-collections
- new-jersey-voter-records
- new-york-state-prison-records
- new-york-state-voter-records
- street-name-changes
---

# Social Security Death Index

> The SSA Death Master File, searched through Steve Morse's flexible one-step forms — the fastest way to confirm a US death and get the person's DOB, death date and last-residence area.

## When to use
You have a US `name` (optionally an approximate `dob`) and need to know whether the person is deceased. The SSDI records deaths reported to the Social Security Administration (broadly 1962 onward), returning birth date, death date, and the ZIP/state of last residence or last benefit — turning "is this person alive?" into dated facts and helping disambiguate same-name individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Steve Morse SSDI search (https://stevemorse.org/ssdi/ssdi.html).
2. Enter the `name`, using the flexible fields (partial names, date ranges, sounds-like) to handle spelling variation.
3. Choose a backend database and submit; review matches: name, `dob`, death date, last-residence ZIP/state.
4. Note that full record detail on some backends (Ancestry, etc.) may need a free/paid account.
5. Pivot: a confirmed death date feeds obituary/probate and `[[interment]]`/`[[deceasedonline-com]]`; last-residence ZIP feeds address/relatives research.

## Inputs → Outputs
- **In:** `name` (+ optional `dob`/date range)
- **Out:** `dob`, death date, last-residence ZIP/state (`address`-level), confirmed `name`
- **Empty/negative result looks like:** no matching record — meaning the death wasn't reported to the SSA, predates coverage, or is too recent/withheld (recent records are restricted). Absence is NOT proof the person is alive.

## Gotchas & OpSec
- Coverage is US and SSA-reported only; recent deaths are restricted and pre-1962 records are sparse. A miss is inconclusive.
- The Steve Morse form is a front-end — full detail may live behind a backend's login/paywall.
- OpSec: fully passive; the subject is deceased and nobody is notified.

## Overlaps ("do both")
- Pairs with `[[interment]]` and `[[deceasedonline-com]]` (cemetery/burial records) and obituary searches — SSDI confirms the death and date; those add burial location and next-of-kin.

## Trust & verifiability
`trust: community` — Steve Morse's portal is a trusted genealogy resource front-ending authoritative SSA Death Master File data; the index is reliable for reported deaths, with the caveats of US-only scope and restricted recent records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-security-death-index |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → dob, name, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
