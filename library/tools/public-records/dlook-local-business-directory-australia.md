---
id: dlook-local-business-directory-australia
name: dLook Local Business Directory (Australia)
description: Use when you have a business `name` or `employer-org` in Australia and want its listing — returns the business `address`, `phone`, and category.
url: http://www.dlook.com.au
category: public-records
path:
- public-records
bestFor: Finding Australian business listings by keyword, suburb, or postcode.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- phone
status: live
pricing: free
costNote: Free Australian business directory; no account required to search.
opsec: passive
opsecNote: Passive — you search a public business directory; no individual is notified. Standard site logging applies. Listings are business (not residential) contact details.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial Australian local-business directory; listing data is self/aggregated and unverified, so treat details as leads to confirm.
missingPersonsRelevance: low
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- dlook.com.au
tags:
- toddington
- curated-directory
- company-search
- australia
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# dLook Local Business Directory (Australia)

> An Australian local-business directory searchable by keyword, suburb, or postcode — tie a business name to its address, phone, and category.

## When to use
You have a business `name`/`employer-org` in Australia (or want to find businesses of a type near a location) and need contact and location details: address, phone, and category. Useful for corroborating a subject's employer or self-run business, confirming a business exists at a suburb/postcode, and getting a `phone`/`address` to pursue. Business-level data, not people search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.dlook.com.au.
2. Search by business `name`/keyword, and narrow by suburb or postcode.
3. Review listings: business name (`employer-org`), `address`, `phone`, and category.
4. Pivot: the address anchors a `geolocation`; the business name feeds ASIC/ABN company-registry lookups for owners/officers; the phone is a contact lead.

## Inputs → Outputs
- **In:** business `name`/`employer-org` or keyword + suburb/postcode.
- **Out:** business `employer-org`, `address`, `phone`, and category.
- **Empty/negative result looks like:** no listing for the name/area — the business isn't in dLook's index (unlisted, closed, or elsewhere), not proof it doesn't exist.

## Gotchas & OpSec
- Australia only: for other countries use local directories.
- Unverified listings: directory data can be stale or aggregated — confirm against the official ASIC/ABN registry for authoritative business/owner info.
- Business, not residential: contact details are for the business, not a home address.
- OpSec: passive; public directory.

## Overlaps ("do both")
- Pairs with Australian company-registry tools (ASIC/ABN lookup) — dLook gives contact/location, the registry gives authoritative registration, owners, and status.

## Trust & verifiability
`trust: community` — a commercial directory with self/aggregated listings; treat entries as leads and verify business identity via the official Australian registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dlook-local-business-directory-australia |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
