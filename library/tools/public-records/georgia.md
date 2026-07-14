---
id: georgia
name: Georgia DOC Offender Query
description: Use when you have a `name` (or GDC ID) and want to locate someone in Georgia state prison custody — returns current facility/status plus dob, physical-description, and image (mugshot).
url: http://www.dcor.state.ga.us/gdc/offender/query
category: public-records
path:
- public-records
bestFor: Locating and confirming a person in Georgia Department of Corrections custody by name or offender ID.
selectorsIn:
- name
selectorsOut:
- dob
- physical-description
- image
- name
status: live
pricing: free
costNote: Free public record search operated by the Georgia Department of Corrections; no account or payment.
opsec: passive
opsecNote: A read-only query against a government public-records site; the subject is not notified and no login is required. Ordinary passive browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Georgia Department of Corrections offender database; authoritative for state-prison custody, though GDC itself disclaims completeness and advises written verification for legal use.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- vinelink
- bop-inmate-locator
aliases:
- Georgia Department of Corrections offender search
- GDC inmate locator
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Georgia DOC Offender Query

> The Georgia Department of Corrections' public offender locator — the authoritative "is this person in Georgia state prison, and where" lookup.

## When to use
A missing or sought person may be incarcerated in Georgia state custody. You have a `name` (or a GDC offender ID / case number) and want to confirm custody, find the current facility, and pull identifying details — DOB/age, physical description, and often a photo. A confirmed hit both locates the person and gives corroborating identity data; it also explains a sudden disappearance from normal life.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the offender query (current endpoint: https://services.gdc.ga.gov/GDC/OffenderQuery/jsp/OffQryForm.jsp; the legacy http://www.dcor.state.ga.us/GDC/Offender/Query still redirects there).
2. Search by `name` — or by GDC ID / case number for an exact match. Narrow common names with age/race filters.
3. Read the record: current status and facility, GDC ID, DOB/age, race/sex, physical description, sentence, and mugshot where available.
4. Empty result → not currently in GDC state custody (could still be in a county jail, federal custody, or another state).
5. Pivot: confirmed custody + DOB feeds identity confirmation; for release notification, register the person on `[[vinelink]]`.

## Inputs → Outputs
- **In:** `name` (or GDC ID / case number)
- **Out:** `name`, `dob`, `physical-description`, `image` (mugshot), current facility & sentence status
- **Empty/negative result looks like:** "no records found" — means not in Georgia *state prison* custody; check county jails and the federal BOP separately.

## Gotchas & OpSec
- Scope is Georgia **state** prisons only — county jail detainees and federal inmates are elsewhere (use the county sheriff's roster or `[[bop-inmate-locator]]`).
- GDC disclaims accuracy/completeness and advises written verification before treating data as fact for any consequential decision.
- Fully passive; no login or CAPTCHA in the normal flow.

## Overlaps ("do both")
- Pairs with `[[vinelink]]` (custody status + release/transfer alerts across states) and `[[bop-inmate-locator]]` (federal) — run these together to cover the custody blind spots this state-only tool leaves.

## Trust & verifiability
`trust: trusted` — first-party state government database, authoritative for GA state custody. Honor GDC's own caveat and confirm in writing for anything legally consequential.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | georgia |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, physical-description, image, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
