---
id: nationwide-business-directory-australia
name: Nationwide Business Directory (Australia)
description: Use when you have an `employer-org` or `name` linked to an Australian business and want directory details — returns `employer-org`, `address`, and contact leads.
url: http://www.nationwide.com.au
category: public-records
path:
- public-records
bestFor: Searching an Australian business directory by business name, keyword, or location to confirm a company and pull its address and contacts.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- phone
status: live
pricing: free
costNote: Free to search and browse; listing/registration is free too, with optional paid promotion for businesses.
opsec: passive
opsecNote: Browsing a public business directory is passive and leaks nothing to any subject. Standard web tracking applies; a clean browser suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial Australian directory with largely self-submitted listings; useful for leads but not an authoritative company register.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- nationwide.com.au
tags:
- toddington
- curated-directory
- company-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Nationwide Business Directory (Australia)

> A free Australian business directory searchable by name, keyword and location — a quick first pass to confirm a company exists in Australia and grab its address and contacts.

## When to use
You have an `employer-org` (or a `name` you're trying to connect to a business) with an Australian nexus and want a fast, free read: business name, category, `address`, and phone/contact. Good for early employer research or verifying a trading name before moving to the authoritative ASIC/ABR registers for the legal entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.nationwide.com.au and use the search fields (business name, keyword, and/or location).
2. Open a listing for the address, phone, category, and any website/social links.
3. Note the trading name and locality.
4. Pivot: confirm the legal entity and directors against the ABN Lookup (ABR) / ASIC; feed the address into mapping/records and any person's name into people-search.

## Inputs → Outputs
- **In:** `name` or `employer-org` (+ optional location)
- **Out:** `employer-org` (directory listing), `address`, and `phone`/contact leads.
- **Empty/negative result looks like:** no matching listing — the business never registered here (common); fall back to ABN Lookup or a broader company search.

## Gotchas & OpSec
- Listings are largely self-submitted and can be stale or promotional — corroborate the address/entity against ABR/ASIC before trusting it.
- Coverage is Australia-focused; overseas entities won't appear.
- OpSec: passive public browsing; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with Australia's authoritative registers (ABN Lookup / ASIC) — the directory gives a fast free lead and contacts; the registers give the legal entity, ABN, and officers to confirm it.

## Trust & verifiability
`trust: community` — a commercial self-serve directory; treat entries as starting points and verify against government registers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nationwide-business-directory-australia |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
