---
id: michigan-state-records
name: Michigan State Records
description: Use when you have a `name` and a Michigan connection and want aggregated public records (court, criminal, inmate, property) — returns address, dob-era, and document-id leads.
url: https://michigan.staterecords.org/
category: public-records
path:
- public-records
bestFor: A one-box aggregator of Michigan public records — court, criminal/arrest, inmate, vital, and property — as a starting index before going to official sources.
selectorsIn:
- name
selectorsOut:
- address
- name
- document-id
status: live
pricing: freemium
costNote: Free name search and record-category selection, but full report content is largely gated behind a paid tier. Free official alternatives exist (Michigan DOC offender search, State Police, county courts).
opsec: passive
opsecNote: A privately-owned aggregator (NOT a government site and NOT an FCRA consumer-reporting agency) — do not use results for employment/tenant screening. Queries hit the aggregator's index, not the subject, so no notification reaches them; only the operator sees your search/IP. Use a sock-puppet browser and expect upsell/paywall prompts.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial records aggregator (staterecords.org network), not government-affiliated; coverage is broad but data is second-hand and must be confirmed at the official source.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- state-corrections-links
- familysearch
aliases:
- Michigan StateRecords.org
- staterecords Michigan
tags:
- public-records
- state-records
- michigan
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Michigan State Records

> A privately-run aggregator claiming instant access to Michigan state/county/municipal public records — useful as a broad first index, not as an authoritative source.

## When to use
You have a `name` and a Michigan nexus and want a fast, single-search sweep across many record types at once — court, criminal/arrest, inmate, vital, property, bankruptcy, liens. Treat it as a pointer that tells you *which* record types likely exist for a person, then confirm each at the official government source. Reasonable early-stage move in a Michigan trace when you don't yet know where the subject's records sit.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://michigan.staterecords.org/.
2. Enter the subject's first and last name (city optional) and tick the record categories you want.
3. Run the search; review the returned index of possible matching records.
4. Expect a paywall/upsell for full report content — decide whether to pay or pivot to the free official source.
5. Pivot: confirm criminal/inmate hits via the Michigan DOC offender search (see [[state-corrections-links]]); confirm vital/genealogy via [[familysearch]] or the county clerk; confirm property at the county register of deeds.

## Inputs → Outputs
- **In:** `name` (+ optional city)
- **Out:** index of candidate records → `address` history, case/`document-id` references, record-type existence
- **Empty/negative result looks like:** no matches or only generic upsell cards — absence here is weak evidence; the aggregator's coverage is incomplete, so check the official source before concluding.

## Gotchas & OpSec
- **Not** a government site and **not** FCRA-compliant — never use for hiring/tenant/credit decisions.
- Michigan case law (2021) removed dates of birth from public-record status, so `dob` fields may be absent or stale — don't over-trust them.
- Human-in-the-loop: the useful detail usually sits behind a payment wall; the free tier is mostly an index and teaser.
- OpSec: passive toward the subject; only the operator sees your query.

## Overlaps ("do both")
- Pairs with [[state-corrections-links]] (route to the free official Michigan DOC inmate locator) and [[familysearch]] (free vital records) — use the aggregator to find leads, the official sources to verify.

## Trust & verifiability
`trust: community` — a commercial aggregator with broad but second-hand data. Every hit should be re-verified at the authoritative government source before it's treated as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | michigan-state-records |
| category | public-records |
| selectorsIn → selectorsOut | name → address, name, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
