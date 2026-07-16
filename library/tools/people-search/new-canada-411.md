---
id: new-canada-411
name: Canada 411
description: Use when you have a Canadian `name`, `phone` or `address` and want the matching listing — returns name, address, phone and (via same-address) likely associates.
url: https://www.canada411.ca/
category: people-search
path:
- people-search
bestFor: Resolving a Canadian person or number to an address and phone using the national residential/business directory, including reverse lookups.
selectorsIn:
- name
- phone
- address
selectorsOut:
- name
- address
- phone
- associate
status: live
pricing: freemium
costNote: Free people, reverse-phone and reverse-address search. Some enhanced/background features route to paid partners, but core directory lookups are free.
opsec: passive
opsecNote: A directory lookup against published listings; the subject is not notified. No login needed for core searches, so activity is not tied to an account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by Yellow Pages Canada — an established directory publisher. Listings can be stale or ex-directory-suppressed; treat as a strong lead, not proof.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- oldphonebook-com
- canada411
- canada411-advanced-search-whitepages-ca
- canada411-ca
- canada411-ca-2
aliases:
- Canada411
- canada411.ca
tags:
- people-search
- canada
- reverse-lookup
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Canada 411

> Canada's national phone/address directory: resolve a Canadian name, number or address — forward or reverse — to a listing.

## When to use
You are working a Canadian subject and hold a `name`, a `phone`, or an `address` and want the rest. Forward-search a name to find listed number and address; reverse a phone number to identify who holds it; reverse an address to see who is listed there (and, via co-listed people at the same address, likely `associate` links). A core first stop for Canadian people-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.canada411.ca/.
2. Pick the search mode: Find a Person (`name` + city/province), Reverse Phone (`phone`), or Reverse Address (`address`/postal code).
3. Submit and read listings: `name`, `address`, `phone`. Same-address listings suggest household/associate links.
4. Narrow with city/province or postal code when a name is common.
5. Pivot: a confirmed `address` feeds property/records tools; co-listed names become new `name` searches to expand the household graph.

## Inputs → Outputs
- **In:** `name`, `phone`, or `address`
- **Out:** `name`, `address`, `phone`, `associate` (co-listed occupants)
- **Empty/negative result looks like:** "no results." Canadians can be unlisted, mobile-only (mobiles are largely absent from directory data), or opted out — absence is not proof of non-residence.

## Gotchas & OpSec
- Skews to landlines and listed adults; mobile numbers are poorly covered.
- Listings lag moves; confirm currency before relying on an address.
- Canada-only coverage.
- OpSec: passive; no login, no subject notification.

## Overlaps ("do both")
- Pairs with `[[oldphonebook-com]]` — Canada 411 for the current Canadian directory, oldphonebook for historical US listings; together they help build an address timeline across the border.

## Trust & verifiability
`trust: community` — run by Yellow Pages Canada, a long-standing directory publisher, so listings are genuine, but compiled directory data can be stale or suppressed. Verify a current address before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-canada-411 |
</content>
