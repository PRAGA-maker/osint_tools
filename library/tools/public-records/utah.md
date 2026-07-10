---
id: utah
name: Utah DOC Offender Search
description: Use when you have a `name` and want to check whether the person is under Utah Department of Corrections supervision — returns name, offender ID, and status/location details.
url: https://corrections.utah.gov/offender-search
category: public-records
path:
- public-records
bestFor: Confirming whether a named person is a current Utah state prison/parole/probation offender.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- address
- physical-description
status: live
pricing: free
costNote: Free, official Utah state government service. No account or payment.
opsec: passive
opsecNote: Public government lookup; the search is anonymous and does not notify the subject. Query from any browser; no sock puppet strictly required, though a clean session is good practice.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Utah Department of Corrections — authoritative first-party government record, not a data broker.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- vinelink
- federal-bureau-of-prisons-inmate-locator
aliases:
- Utah Department of Corrections offender search
- Utah DOC inmate lookup
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Utah DOC Offender Search

> The Utah Department of Corrections' official offender locator — an authoritative check on whether a named person is currently in state custody, on parole, or on probation.

## When to use
You have a `name` and are trying to account for a person's whereabouts in Utah. A hit tells you the subject is under UDC supervision and gives an offender ID plus current status/facility — a definitive "found" for a missing-person case where incarceration is a possibility.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://corrections.utah.gov/offender-search.
2. Enter the subject's name (or offender number if known) and submit.
3. Read the result: matching offender record(s) with name, offender ID, status (incarcerated / parole / probation), and facility or supervising region.
4. Note the scope limit: it covers ONLY people currently under UDC supervision — not pre-trial detainees or those in county jails.
5. Pivot: an offender ID/facility feeds `[[vinelink]]` for custody-status notifications; a no-match sends you to county jail rosters or `[[federal-bureau-of-prisons-inmate-locator]]`.

## Inputs → Outputs
- **In:** `name` (or offender ID)
- **Out:** `name`, `document-id` (offender number), `address` (facility/region), `physical-description` where shown
- **Empty/negative result looks like:** "no records found" — means not currently under UDC supervision. It does NOT rule out county jail, another state, or a past (completed) sentence.

## Gotchas & OpSec
- Human-in-the-loop: none — straightforward public form.
- OpSec: **passive**; the subject is not notified. This is a government record search.
- Scope trap: absence here is weak evidence. Always also check county jails and neighboring states before concluding the person is not incarcerated.

## Overlaps ("do both")
- Pairs with `[[vinelink]]` — VINELink aggregates custody status across many jurisdictions and can notify on changes; use it alongside the authoritative state source.
- Pairs with `[[federal-bureau-of-prisons-inmate-locator]]` — rules in/out federal custody, which the state system won't show.

## Trust & verifiability
`trust: trusted` — first-party Utah government data; a positive match is authoritative. Only caveat is the narrow scope (current UDC supervision only).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | utah |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, address, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
