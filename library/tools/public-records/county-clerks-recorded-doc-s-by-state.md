---
id: county-clerks-recorded-doc-s-by-state
name: SearchSystems — County Clerk Recorded Documents
description: Use when you have a `name` and a US location and want official recorded-document / public-record databases (deeds, liens, UCC, vital, court) by state and county — returns links to official sources returning address, document-id, and dates.
url: http://publicrecords.searchsystems.net/free_public_records_by_type_of_record/recorded_documents
category: public-records
path:
- public-records
bestFor: Finding the official county-clerk and government databases for recorded documents (deeds, liens, UCC) and other public records by US state/county.
selectorsIn:
- name
selectorsOut:
- name
- address
- document-id
status: live
pricing: free
costNote: Free directory; explicitly no paywall, no account, no email harvesting. It links only to official government sources (some destination records may carry per-copy fees).
opsec: passive
opsecNote: Browsing the directory is passive. The destination government databases may log searches or require login/fees; assess OpSec at each official source you follow.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-running (since 1996) directory that links exclusively to official .gov/.us/court sources rather than data brokers; the directory is reputable and the endpoints are authoritative government records.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- searchsystems.net
- SearchSystems public records directory
tags:
- court
- inmate
- us
- directory
- recorded-documents
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# SearchSystems — County Clerk Recorded Documents

> A free, long-established directory of *official* US public-records databases — county-clerk recorded documents (deeds, liens, UCC) and more — organized by state, county, and record type.

## When to use
You have a subject's `name` and a US location and want to search recorded documents — property deeds, mortgages, liens, UCC filings — or other official records (court, criminal, vital, property) at their authoritative source. SearchSystems indexes ~90,000+ official government databases across all 3,143 counties, so it's the gateway to find *which* county recorder/clerk holds the records and how to search them. Deeds and liens are strong locators: they tie a person to a property `address` and a recorded instrument `document-id`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the recorded-documents directory (https://www.searchsystems.net/us) and navigate by state → county → record type.
2. Follow the link to the county clerk/recorder's **official** search portal.
3. Search the subject's `name` (grantor/grantee) there.
4. Read results: recorded instruments with the `name`, property `address`, instrument `document-id`, and recording dates.
5. Pivot: a property `address` feeds address-based lookups and `[[residential]]`-style property tools; grantor/grantee names are `associate` leads; instrument IDs support full document retrieval.

## Inputs → Outputs
- **In:** `name` (+ US county/state to locate the recorder)
- **Out:** links to official databases returning `name`, property `address`, recorded `document-id`, dates
- **Empty/negative result looks like:** the county isn't online (records only in person), or no instrument under that name — recorded documents only exist where the person transacted, so absence is not proof of no property.

## Gotchas & OpSec
- **It's a directory of links, not a search box** — it never returns records itself; the data is at the official county sources.
- Coverage/searchability varies wildly by county; some are online, many are in-person only, and some official portals charge per copy.
- OpSec: passive at the directory; check each destination portal's login/logging/fees.

## Overlaps ("do both")
- Do both with `[[court-records-directory-2]]` (CourtReference) — both are official-source gateways, but this one is strongest for recorded documents/property/vital records while that one is strongest for court dockets.

## Trust & verifiability
`trust: trusted` — the directory only links to official government sources (no data-broker resells), and those endpoints are authoritative; the directory's own age and reputation are well established.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | county-clerks-recorded-doc-s-by-state |
| category | public-records |
| selectorsIn → selectorsOut | name → name, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
