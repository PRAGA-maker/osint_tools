---
id: the-directory-area-code-listings-worldwide
name: The Directory Area Code Listings (Worldwide)
description: Use when you have a North American `phone` number and want the fine-grained rate-center location behind its prefix — returns the `geolocation`/`address`-level city/region tied to the area code + exchange.
url: http://www.thedirectory.org
category: phone
path:
- phone
bestFor: Mapping a US/Canada/Caribbean area code + prefix to its detailed rate-center locality.
selectorsIn:
- phone
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free reference site. No account, no payment, no API key.
opsec: passive
opsecNote: You browse a static prefix/area-code reference; nothing is sent to the subscriber or their carrier. Fully passive — the target sees nothing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running third-party telephone-prefix reference. Prefix-to-location data can lag portability and reassignments, so treat locality as an original-allocation prior, not proof of where the holder lives now.
missingPersonsRelevance: high
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nanpa-area-code-query
aliases:
- thedirectory.org
- Area Code Listings
tags:
- toddington
- curated-directory
- telephone-numbers
- area-code
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# The Directory Area Code Listings (Worldwide)

> A detailed reference for North American telephone prefixes — drill from area code to the specific rate-center city a prefix was allocated to, finer than a plain state-level area-code lookup.

## When to use
You have a `phone` number in the North American Numbering Plan and want a *locality*-level read on where its **area code + exchange prefix** was assigned — down to the rate-center city/region, not just the state. Useful for narrowing a landline number's likely origin, distinguishing which part of a multi-city area code a number belongs to, and building a `geolocation` prior around a subject's number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.thedirectory.org.
2. Navigate to the target's area code (listings are organised by US region/state, Canadian province, Caribbean/US territory).
3. Drill into the prefix (NXX) to read the detailed location/rate-center information for that block.
4. Note the city/region the prefix maps to as your locality estimate.
5. Pivot: confirm the allocation against `[[nanpa-area-code-query]]`, then combine with carrier/HLR lookups; treat the locality as a lead to corroborate with other `address` evidence.

## Inputs → Outputs
- **In:** `phone` (area code + exchange prefix)
- **Out:** `geolocation`/`address`-level rate-center city/region for that prefix
- **Empty/negative result looks like:** the prefix isn't listed or maps only to a broad region — the block may be newer than the reference's data, non-geographic, or ported. Fall back to NANPA and carrier lookups.

## Gotchas & OpSec
- Human-in-the-loop: none; a static reference you read.
- OpSec: **passive** — no contact with subscriber or carrier.
- Number portability and mobile assignment badly erode prefix-to-location accuracy: the holder may live nowhere near the original rate center. Use as a weak prior, never as a located address.

## Overlaps ("do both")
- Pairs with `[[nanpa-area-code-query]]` — NANPA is the authoritative source for the area-code allocation, while this adds finer prefix/rate-center locality. Cross-check one against the other before trusting a city-level guess.

## Trust & verifiability
`trust: community` — a useful, detailed independent reference, but not an official registry and subject to staleness. Its locality output is an original-allocation signal, so corroborate before treating it as where the person actually is.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-directory-area-code-listings-worldwide |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
