---
id: gun-dealer-inspections-the-trace
name: Gun Dealer Inspections (The Trace)
description: Use when you have a US gun-dealer business `name` or `address`/`geolocation` and want its ATF inspection/disciplinary history — returns `employer-org`, `address`, and violation outcomes.
url: https://projects.thetrace.org/inspections/
category: public-records
path:
- public-records
bestFor: Looking up whether a specific federally licensed US gun dealer was inspected, cited, or had its license revoked (2015–2017 dataset).
selectorsIn:
- name
- address
- geolocation
selectorsOut:
- employer-org
- address
- document-id
status: live
pricing: free
costNote: Free public-interest project; the full dataset is browsable on the map and downloadable as CSV, no account required.
opsec: passive
opsecNote: You browse a static published dataset hosted by The Trace; no query reaches the dealer or ATF, so nobody is notified. Ordinary browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by The Trace (an established nonprofit newsroom) from ATF inspection records obtained via FOIA; sourcing is documented and the raw data is downloadable for verification.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- The Trace ATF inspections
- gun dealer inspection database
tags:
- public-records
- firearms
- atf
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Gun Dealer Inspections (The Trace)

> A searchable/mappable database of ~2,000 ATF inspection reports (2015–2017) for federally licensed US gun dealers, showing who was cited, warned, settled, or had a license revoked.

## When to use
You have a US federal firearms licensee (FFL) tied to your subject — a gun shop they own, work at, or are associated with — and want to know its regulatory track record: was it inspected, what violations were found, and did ATF take action. In a missing-persons or associate-mapping context this places a business (and by extension its owners/employees) at a documented `address`, and a revocation/settlement can corroborate a timeline or explain a business closure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://projects.thetrace.org/inspections/.
2. Explore the interactive map or filter by state, inspection outcome (revocation, warning, settlement), and violation type.
3. Search for the dealer by `name`/location and open the individual licensee record for the inspection outcome and violation detail.
4. Use the CSV download if you need to search the full dataset offline or cross-reference many dealers at once.
5. Pivot: take the confirmed business `address` into property/records tools and the `employer-org` into corporate-registry lookups to reach the human owners.

## Inputs → Outputs
- **In:** gun-dealer business `name`, `address`, or `geolocation` (state/area)
- **Out:** `employer-org` (the FFL business), its `address`, inspection outcome, violation type, licensee record (`document-id`)
- **Empty/negative result looks like:** no matching dealer — the business either wasn't in the 2015–2017 inspection set, isn't an FFL, or is outside the dataset's window; absence is not proof of a clean record.

## Gotchas & OpSec
- **Historical snapshot:** the data covers inspections from 2015–2017 only; it will not reflect a dealer's current status or newer businesses.
- US-only, firearms-licensee-only — narrow scope by design.
- OpSec: fully passive; a published dataset with no live target query.

## Overlaps ("do both")
- Pairs with corporate-registry and property-records tools — this confirms the FFL and its address; those reach the owners, officers, and real estate behind it.

## Trust & verifiability
`trust: trusted` — a documented FOIA-sourced dataset from a reputable newsroom, with the raw CSV downloadable so any record can be independently checked.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gun-dealer-inspections-the-trace |
| category | public-records |
| selectorsIn → selectorsOut | name, address, geolocation → employer-org, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
