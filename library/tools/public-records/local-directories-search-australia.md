---
id: local-directories-search-australia
name: Local Directories Search (Australia)
description: Use when you have an Australian business `name`/type and a location and want listings — now Localsearch; returns local `employer-org`s with `address` and `phone`.
url: https://www.localsearch.com.au/
category: public-records
path:
- public-records
bestFor: Finding Australian businesses/tradespeople by name/category and suburb, with address and phone.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- phone
status: live
pricing: free
costNote: Free to search listings; paid tiers exist for business owners (premium profiles/marketing).
opsec: passive
opsecNote: Passive — you browse a public Australian business directory, transmitting nothing about a personal target. Only relevant when a subject is tied to an AU business/trade.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major Australian local-business directory (localdirectories.com.au now redirects to Localsearch); reliable for business listings, not personal records.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Localsearch
- localdirectories.com.au
tags:
- toddington
- company-search
- australia
- local-business
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Local Directories Search (Australia)

> Australia's Localsearch directory — find a business or tradesperson by name/category and suburb, with address and phone.

## When to use
Your subject is linked to an Australian business or trade and you want the listing: the business `address`, `phone`, hours, and category. It's a business/occupation lens for AU — bridge business→person yourself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.localsearch.com.au/ (localdirectories.com.au redirects here).
2. Enter a business `name` or category (e.g. plumber, cafe) plus a suburb/region.
3. Read the output: matching AU `employer-org`s with `address`, `phone`, hours, and reviews.
4. Pivot: use a business address/phone to link it to the person, then cross-reference ASIC/ABN registries and people-search.

## Inputs → Outputs
- **In:** a business `name`/category + Australian location
- **Out:** local `employer-org` listings with `address` and `phone`
- **Empty/negative result looks like:** no listings for a name+suburb means it's not in this directory — try a broader area or the ABN/ASIC registers.

## Gotchas & OpSec
- Australia-only; surfaces businesses, not people directly.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Pairs with Australian company/ABN registers — this gives the local listing; those give registered ownership/officers.

## Trust & verifiability
`trust: community` — commercial directory; verify business details against the official ABN/ASIC register or the business's own site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | local-directories-search-australia |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
