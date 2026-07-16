---
id: inmate-locator-us
name: Inmate Locator (US)
description: Use when you have a `name` and want to find where a US inmate is incarcerated by routing to the right federal/state/ICE locator — returns confirmed name, inmate ID and facility/dob leads.
url: https://www.theinmatelocator.com
category: public-records
path:
- public-records
bestFor: Finding the correct US federal, state, or ICE inmate-search system to locate an incarcerated person.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free directory; the official locators it links to (BOP, state DOCs, ICE) are also free public systems.
opsec: passive
opsecNote: Searching official inmate locators is passive — the incarcerated person is not notified. Use a sock-puppet browser as good practice; the underlying government sites log queries.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party directory that aggregates links to official inmate-search systems; the directory is a signpost — the authoritative data is on the government locator it sends you to.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- The Inmate Locator
- theinmatelocator.com
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- us-inmate-locator
---

# Inmate Locator (US)

> A free directory that points a name at the right US inmate-search system — federal BOP, any state DOC, or ICE — so you don't have to know which of 50+ locators to try.

## When to use
You have a `name` and reason to think a US subject may be (or have been) incarcerated, and you need to find *which* correctional system holds them. The hard part of US inmate search is jurisdiction fragmentation; this directory routes you to the federal Bureau of Prisons, the correct state Department of Corrections, or the ICE detainee locator, where you run the actual search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.theinmatelocator.com.
2. Choose the jurisdiction: federal (BOP), a specific state DOC, or ICE — pick based on where you suspect custody, or check the federal BOP and likely states.
3. Follow the link to the official locator and search by `name` (and DOB/ID if known) there.
4. Read the record: the official locator confirms name, inmate/register number (`document-id`), facility, and often DOB and release/custody status.
5. Pivot: a facility + inmate number anchors location and timeline; the confirmed identity feeds court-records and people-search work.

## Inputs → Outputs
- **In:** `name` (+ known state/DOB to disambiguate)
- **Out:** confirmed `name`, inmate/register number (`document-id`), facility, `dob`/custody status (from the official locator)
- **Empty/negative result looks like:** no match in the searched system — which means not in *that* jurisdiction's current population, not that the person was never incarcerated; several states aren't covered/available, and historical custody may not appear.

## Gotchas & OpSec
- It's a directory, not a database: it holds no inmate data itself and disclaims accuracy — always run and cite the official locator.
- Coverage gaps: some states/territories lack an online locator; note absence ≠ evidence.
- Same-name risk: confirm with DOB/ID before attributing custody to your subject.

## Overlaps ("do both")
- Pairs with `[[the-law-pages]]` (UK court records) and `[[state-public-records-laws]]`: inmate status is one facet; court and records tools give the case behind it.

## Trust & verifiability
`trust: community` — a third-party signpost to authoritative government systems; verification comes from the official locator it links to, not from the directory.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inmate-locator-us |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
