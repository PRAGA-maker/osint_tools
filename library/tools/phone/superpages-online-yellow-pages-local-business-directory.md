---
id: superpages-online-yellow-pages-local-business-directory
name: Superpages (Yellow Pages / Find People)
description: Use when you have a US `phone`, `name`, or business and want directory data — returns names, addresses and phone numbers from a live US business + white-pages directory.
url: https://www.superpages.com
category: phone
path:
- phone
bestFor: Free US directory lookups — reverse phone, business listings, and white-pages people search for names, addresses and numbers.
selectorsIn:
- phone
- name
selectorsOut:
- name
- address
- phone
status: live
pricing: free
costNote: Free, ad-supported directory; "full report" links may hand off to paid partners, but the core business/people listings are free.
opsec: passive
opsecNote: You query a public directory, not the subject — no notification is sent. No login required. Use a clean browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established US yellow-pages/white-pages directory (Thryv-operated); strong on business listings, weaker/older on residential people data — corroborate residential hits.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Superpages
- superpages.com
tags:
- phone
- yellow-pages
- white-pages
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Superpages (Yellow Pages / Find People)

> A live US yellow-pages/white-pages directory: reverse a phone, look up a business, or run a people search for names, addresses and numbers — strongest on business listings.

## When to use
You have a US `phone` number (reverse lookup), a `name`, or a business and want directory data: owner/business `name`, `address`, and listed `phone`. Superpages is especially strong for tying a person to a business, a business to a location, or confirming a listed number — a fast free pass alongside residential white-pages sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.superpages.com (no login needed).
2. For a business/service, enter the category or name plus a location. For people, use the "Find People" / white-pages entry; for a number, use reverse-phone search.
3. Read the listing: `name`, `address`, `phone`, category, and any linked business detail.
4. Ignore paid "background report" hand-offs unless you intend to pay; the free listing is the value.
5. Pivot: a business address feeds mapping and company registries; a residential name feeds dedicated people-search aggregators; a number feeds carrier/reverse-phone tools.

## Inputs → Outputs
- **In:** `phone` (reverse) / `name` / business+location
- **Out:** `name`, `address`, `phone`, business category/detail
- **Empty/negative result looks like:** no listing — common for mobile/unlisted numbers and individuals (Superpages skews to businesses); absence isn't proof the person/number is inactive.

## Gotchas & OpSec
- Business-skewed: great for commercial listings, thinner and more dated for residential people — corroborate residential hits elsewhere.
- Human-in-the-loop: none for free listings; only paid partner reports need registration/payment.
- OpSec: fully passive; a public directory lookup that never touches the subject.

## Overlaps ("do both")
- Pairs with `[[infospace]]` and other white-pages aggregators — coverage and freshness differ, so cross-check a name/number across two before trusting it.

## Trust & verifiability
`trust: community` — a real, long-standing directory brand, authoritative for claimed business listings but corroboration-grade for residential data; verify people hits against another source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | superpages-online-yellow-pages-local-business-directory |
| category | phone |
| selectorsIn → selectorsOut | phone, name → name, address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
