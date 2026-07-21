---
id: inmates-plus
name: InmatesPlus
description: Use when you have a `name` and want to check whether someone is or was incarcerated in a US state or county facility — returns `address` (facility), `document-id` (offender ID) and offense/sentencing context.
url: http://www.inmatesplus.com/
category: dark-web
path:
- dark-web
bestFor: Locating an incarcerated person across US state/county corrections systems and finding which facility holds them.
selectorsIn:
- name
selectorsOut:
- address
- document-id
status: degraded
pricing: free
costNote: Free to search and to use the linked official locators. No account required.
opsec: passive
opsecNote: You are searching a public inmate-lookup aggregator; the incarcerated person is not notified and cannot see the query. Fully passive. As with any people-lookup, browse from a sock-puppet session to keep the search off your own footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party aggregator that surfaces and links to official state/county corrections locators; convenient as a hub but not the system of record. Confirm any hit on the actual DOC/sheriff site it links to.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- state-and-county-jail-inmate-locators
aliases:
- Inmates Plus
- inmatesplus.com
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# InmatesPlus

> A US inmate-lookup hub that aggregates state and county corrections records and links out to the official locators — a fast first stop for "is this person in custody, and where?"

## When to use
A subject has gone missing or dropped off the grid and incarceration is a plausible explanation. You have a `name` (ideally plus a state) and want to check whether they are held in a US state prison or county jail, in which facility, and under what offense — a common and highly resolving answer in missing-persons and skip-tracing work, since custody explains sudden silence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.inmatesplus.com/ and select the relevant state (coverage spans all 50 states + DC, though completeness varies by state).
2. Search by the subject's name; review returned records for offender ID, offense description, sentencing, and facility.
3. Follow the link to the authoritative source (the state DOC or county sheriff locator) to confirm the record is current — aggregator data can lag releases/transfers.
4. Note the facility address and offender/booking ID for follow-up (visitation, mail, court records).
5. Pivot: an offender ID feeds official DOC lookups and court-record searches; a facility + sentencing date bounds a timeline; confirmed custody often closes the "where are they" question outright.

## Inputs → Outputs
- **In:** `name` (best with a state)
- **Out:** `address` (holding facility), `document-id` (offender/booking ID), offense & sentencing context
- **Empty/negative result looks like:** no match in the searched state — the person is not in that state's indexed data, may be in a state not covered, in federal custody (use the BOP locator), or simply not incarcerated. Absence is not proof of freedom.

## Gotchas & OpSec
- It is an aggregator, not the system of record — data may be stale (a person shown "in custody" may already be released/transferred). Always confirm on the linked official locator.
- Coverage and freshness vary widely by state; federal inmates require the separate BOP Inmate Locator.
- Fully passive: inmate searches leak nothing to the subject.

## Overlaps ("do both")
- Pairs with `[[state-and-county-jail-inmate-locators]]` — that is the directory of official per-jurisdiction locators; use this aggregator to cast a wide first net, then confirm on the official source it points to.

## Trust & verifiability
`trust: unverified` — a convenience aggregator of public corrections data, not an official source; treat hits as leads to verify against the linked state DOC / county sheriff record before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inmates-plus |
| category | dark-web |
| selectorsIn → selectorsOut | name → address, document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
