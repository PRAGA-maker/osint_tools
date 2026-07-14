---
id: yellow-pages
name: YellowPages.ca
description: Use when you have a Canadian `name`, business, or `phone` and want directory details — returns `address`, `phone`, and business (`employer-org`) listings; its Canada411 sister site handles person lookups.
url: https://www.yellowpages.ca
category: email
path:
- email
bestFor: Finding Canadian businesses (and, via Canada411, people) with addresses and phone numbers, including reverse-phone lookups.
selectorsIn:
- name
- phone
- employer-org
selectorsOut:
- address
- phone
- employer-org
status: live
pricing: free
costNote: Free to search; paid options exist only for businesses buying listings/advertising.
opsec: passive
opsecNote: A public directory search — the business/person is not notified. The site sees your IP/query; a sock-puppet browser suffices for sensitive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The long-established (since 1908) Canadian directory; business listings are reliable, and person lookups run through its sister service Canada411.ca.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- yellowpages.ca
- Canada411
- YP.ca
tags:
- toddington
- curated-directory
- people-search
- telephone-numbers
- canada
source: toddington-resources
lastVerified: '2026-07-13'
enrichment: full
---

# YellowPages.ca

> Canada's long-running directory of businesses, addresses and phone numbers — and, through its Canada411 sibling, a free people finder for Canadian subjects.

## When to use
You have a Canadian subject or business — a `name`, a business/`employer-org`, or a `phone` number — and want an address, phone, or business listing. Use YellowPages.ca for businesses and reverse-business-phone, and its sister site Canada411.ca to search individuals by name (forward and reverse phone). It's a solid free anchor for Canadian geography.

## How to use it (`bestInteractionPattern`: web-manual)
1. For businesses: go to https://www.yellowpages.ca, enter the business/category and a Canadian city.
2. For people: switch to Canada411.ca and search by person name (or reverse a phone number).
3. Read results: `address`, `phone`, hours, and business details.
4. Pivot: an address feeds mapping/streetview and property lookups; a confirmed phone feeds reverse-phone and messaging-app checks; a business ties a person to an `employer-org`.

## Inputs → Outputs
- **In:** `name` / business (`employer-org`) / `phone`
- **Out:** `address`, `phone`, business listing (`employer-org`)
- **Empty/negative result looks like:** no listing — the person is unlisted/ex-directory, the business is closed or not registered here, or the subject is outside Canada; absence is not proof of non-existence.

## Gotchas & OpSec
- Canada-only: use the relevant national directory for subjects elsewhere.
- People searches live on Canada411.ca, not the main YP business site — don't conclude "no person" from the business directory alone.
- OpSec: fully passive; a routine directory lookup.

## Overlaps ("do both")
- Pairs with reverse-phone tools and people-search — YP/Canada411 give the free Canadian baseline; cross-check numbers/names against other sources for currency.

## Trust & verifiability
`trust: trusted` — an established first-party directory; business data is reliable, though personal listings depend on what individuals chose to publish.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yellow-pages |
