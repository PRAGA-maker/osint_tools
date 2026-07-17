---
id: canpages-search-canada
name: Canpages Search (Canada)
description: Use when you have a Canadian `name`, business, `phone`, or `address` and want directory details — returns business/residential listings, phone numbers, and addresses.
url: http://www.canpages.ca
category: public-records
path:
- public-records
bestFor: Canadian business and reverse phone/address directory lookups.
selectorsIn:
- name
- employer-org
- phone
- address
selectorsOut:
- employer-org
- address
- phone
status: live
pricing: free
costNote: Free online directory (ad-supported); no account needed to search.
opsec: passive
opsecNote: Public directory queries; the listed party is not notified who searched. Fully passive. Use a clean browser for tidy sessions, but there's no target-facing footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running Canadian directory aggregator; listing accuracy varies and residential coverage is thinner than its business data.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- canada411
- yellowpages-ca
aliases:
- Canpages
- canpages.ca
tags:
- toddington
- curated-directory
- company-search
- canada
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Canpages Search (Canada)

> A Canadian online directory — business and reverse phone/address lookups for locating people and companies across Canada.

## When to use
Your subject or a lead is in Canada and you have a `name`, business name, `phone`, or `address` to resolve. Canpages returns directory listings — strongest for businesses (name → address/phone, or reverse phone → business), with some residential coverage. Use it to confirm a Canadian address/number, identify the business behind a phone number, or find a company's location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.canpages.ca.
2. Enter a keyword/name/business and a location (city or postal code), or run a reverse lookup by phone number.
3. Read the listings: business/person name, address, phone, and category.
4. Cross-check anything decisive against a second Canadian directory — listing data is aggregated and can be stale.
5. Pivot: an address → map/street-view and property records; a business name → corporate registry; a phone → `[[canada411]]` for the residential side.

## Inputs → Outputs
- **In:** `name` / `employer-org` / `phone` / `address` (Canada)
- **Out:** matching `employer-org`/person listing, `address`, `phone`
- **Empty/negative result looks like:** no listings — unlisted number, non-Canadian entry, or the person/business simply isn't in the directory; try Canada411 or the Yellow Pages CA.

## Gotchas & OpSec
- Canada-only; useless outside Canada.
- Business coverage is far better than residential — many individuals are unlisted, so a null is weak evidence of absence.
- Aggregated data drifts; verify against a second source before acting on an address/number.

## Overlaps ("do both")
- Pairs with `[[canada411]]` — Canada411 is stronger on residential white-pages listings; Canpages leans business/yellow-pages. Run both for full Canadian directory coverage.
- Pairs with `[[yellowpages-ca]]` for another business-directory cross-check.

## Trust & verifiability
`trust: community` — an established but third-party aggregator; treat individual listings as leads to confirm, not authoritative records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canpages-search-canada |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, phone, address → employer-org, address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
