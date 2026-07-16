---
id: court-records-directory
name: SearchSystems.net Court Records Directory
description: Use when you have a `name` and a rough US jurisdiction and want to reach the right free official court/criminal record database — returns curated links to `.gov`/county court systems that yield `document-id`, `dob` and case records.
url: http://publicrecords.searchsystems.net/free_public_records_by_type_of_record/court_records
category: public-records
path:
- public-records
bestFor: Finding the correct free, official (non-broker) US court/criminal record database for a given state or county, then searching a name there.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: The directory is free with no account, email or paywall; it links only to free government sources (destinations may themselves charge for copies of documents).
opsec: passive
opsecNote: SearchSystems is just a link directory — searching happens on the official destination site, which sees your IP/query. Use a sock-puppet browser; the subject is not notified.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running (since 1996) curated directory that links directly to .gov/.us/county/court systems — explicitly never to data brokers, scrapers or resold databases.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- tennessee
- county-clerks-recorded-doc-s-by-state
- property-records-public-records-by-state
- search-systems-criminal-records
- search-systems-public-records-us
- searchsystems-birth-records
- searchsystems-death-records
- texas-public-records-search
aliases:
- SearchSystems.net
- Public Records court records directory
tags:
- court
- inmate
- public-records
- directory
source: metaosint
lastVerified: '2026-07-13'
enrichment: full
---

# SearchSystems.net Court Records Directory

> A curated index of tens of thousands of *official* free public-record databases across every US state and county — the fastest way to land on the right court system for a jurisdiction instead of a data broker.

## When to use
You have a `name` and at least a rough US jurisdiction (state, county) and need the authoritative free source — court dockets, criminal records, wanted/inmate databases — rather than a paid aggregator. SearchSystems routes you straight to the relevant `.gov`/county/court portal, which is where you then run the actual name search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the directory (the seeded URL 301-redirects to the current searchsystems.net site).
2. Drill down by record type (court/criminal) and by state → county to the jurisdiction you need.
3. Follow the curated link to the official database and search the `name` there.
4. Read the destination's output: case numbers, filings, dispositions, DOB, party names.
5. Pivot: a case `document-id` and `dob` feed identity confirmation and corrections lookups such as `[[tennessee]]`; party names surface `associate` leads.

## Inputs → Outputs
- **In:** `name` + jurisdiction (you supply the geography to pick the right link)
- **Out:** links to official sources that return `document-id` (case/docket numbers), `dob`, confirmed `name`, and case records
- **Empty/negative result looks like:** the directory has no listed database for that record type in that county (coverage gap), or the destination returns no matching case — SearchSystems only points; it does not itself hold records.

## Gotchas & OpSec
- Human-in-the-loop: you must choose the correct jurisdiction and interpret each destination's results — court systems vary wildly in interface and search fields.
- US-only, and destinations differ in how far back and how completely they index; a null on one county's portal is not a national clearance.
- OpSec: passive; the directory itself collects nothing about the subject.

## Overlaps ("do both")
- Pairs with `[[tennessee]]` and other state corrections/court tools — the directory finds the right jurisdiction's portal; the specific-state tools go deep once you know where to look.

## Trust & verifiability
`trust: trusted` — a long-established curator that links only to official government sources, so the data you ultimately read is first-party; the directory's own risk is stale links, not bad data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | court-records-directory |
