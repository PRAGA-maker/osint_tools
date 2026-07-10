---
id: british-phone-book
name: British Phone Book
description: Use when you have a UK `name` and want a residential landline listing with address — returns address and phone (landline).
url: http://www.britishphonebook.com
category: people-search
path:
- people-search
bestFor: Looking up UK residential landline listings by surname (plus city/postcode) to find an address and phone number.
selectorsIn:
- name
selectorsOut:
- address
- phone
status: degraded
pricing: free
costNote: Free to search. Data is compiled from current and historic phone books, website signups and permissioned sources and is 1–10 years old, so it is dated.
opsec: passive
opsecNote: A directory lookup that does not contact the subject — fully passive. Standard web-server logging by the site applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party UK directory aggregator of unclear provenance; data is old (1–10 years), excludes mobiles, and coverage is partial, so treat listings as leads not confirmations.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- britishphonebook.com
- British Phone Book
tags:
- people-search
- phone-lookup
- uk
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# British Phone Book

> A UK residential landline directory — search a surname (with a city or partial postcode) to pull a listed address and phone number, useful as an older-data anchor.

## When to use
You have a UK `name` and want to check for a residential landline listing that ties them to an `address` and `phone`. Because the data skews old (1–10 years), it is most useful for establishing a *historic* or last-known address and phone, or for corroborating an address you already suspect — not for confirming where someone lives right now.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to britishphonebook.com.
2. Enter the subject's surname, optionally with a city or the first part of a postcode to narrow results.
3. Read the listings: name, address, and landline number.
4. Treat any hit as a dated lead — cross-check the address/number against a current source.
5. Pivot: an address feeds electoral-roll and property records; a landline feeds reverse-number lookups; a historic address helps timeline reconstruction.

## Inputs → Outputs
- **In:** `name` (surname, optionally + city/postcode fragment)
- **Out:** `address` (listed residential address), `phone` (landline)
- **Empty/negative result looks like:** no listing — very common, since the site itself notes "not everyone is listed", it excludes mobiles and ex-directory numbers, and coverage is partial. Absence proves nothing.

## Gotchas & OpSec
- **Dated data:** listings can be up to a decade old; verify currency elsewhere before relying on an address.
- Landlines only — no mobile numbers; declining usefulness as UK households drop landlines.
- Provenance is unclear; corroborate before acting on any listing.

## Overlaps ("do both")
- Pairs with UK electoral-roll tools, `[[thegenealogist-co-uk]]` and 192.com-style directories — run a current source alongside this to distinguish a live address from a stale one.

## Trust & verifiability
`trust: unverified` — an opaque aggregator with old, partial data; use listings as leads and confirm with a primary or current source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | british-phone-book |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
