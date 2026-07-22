---
id: superpages-directory-united-states
name: Superpages Directory (United States)
description: Use when you have a `name` or `employer-org` and want US business and white-pages listings — returns `address`, `phone` and business affiliations.
url: http://www.superpages.com
category: public-records
path:
- public-records
bestFor: Looking up a US business or a person's white-pages listing by name and location.
selectorsIn:
- name
- employer-org
selectorsOut:
- address
- phone
- employer-org
status: live
pricing: free
costNote: Free directory search; the people-search side hands off to a paid third-party white-pages partner for full detail.
opsec: passive
opsecNote: Searching the public directory is passive and does not notify anyone. If you click through to the partnered white-pages/people-search service, you leave that third party's site (and its trackers); treat any paid unlock there as a separate decision.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A legacy US Yellow-Pages-style directory now aggregating listings and monetising a people-search hand-off; listing freshness varies and is not independently verified.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- superpages
- Superpages Yellow Pages
tags:
- toddington
- curated-directory
- company-search
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- superpages-com
- superpages-online-yellow-pages-local-business-directory
---

# Superpages Directory (United States)

> The classic US Yellow-Pages directory: quick free business lookups, plus a white-pages people-search hand-off for names tied to an address or phone.

## When to use
You have a US `name` (person or business) or an `employer-org` and want a starting `address` / `phone`. Best as a first, free pass: confirm a business exists at a location, tie a person to a small business, or pull a listed number before moving to deeper (often paid) people-search tools. Coverage is US-only.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.superpages.com.
2. For a business: enter the category or `employer-org` name plus a city/state and search.
3. For a person: use the "Find People" / white-pages option and enter the `name` and location — this routes to a partnered people-search provider.
4. Read the listing: business results give `address`, `phone`, category and sometimes a website; people results give a name/age/location teaser, with full detail gated behind the partner's paywall.
5. Pivot: a `phone` feeds reverse-phone lookups; a business `address` feeds mapping/registration-record checks; a confirmed employer feeds corporate-records tools.

## Inputs → Outputs
- **In:** `name` or `employer-org` (+ US location)
- **Out:** `address`, `phone`, `employer-org` / business category
- **Empty/negative result looks like:** "no results" for that name/city, or a people-search teaser that reveals nothing without paying — treat the free teaser as "may exist," not confirmation.

## Gotchas & OpSec
- Directory data is aggregated and can be stale — a listing does not prove current occupancy or employment.
- The people-search click-through leaves Superpages for a third-party paid service; don't confuse its paywalled teaser with a verified hit.
- Passive throughout the free directory; no target notification.

## Overlaps ("do both")
- Pairs with `[[superpages-com]]` and other US white-pages/reverse-phone tools — cross-check listings, since each aggregator refreshes on a different schedule and one often has a number the other lacks.

## Trust & verifiability
`trust: unverified` — a legitimate long-standing directory brand, but listings are aggregated third-party data of variable freshness and the people-search side is monetised, so verify hits independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | superpages-directory-united-states |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → address, phone, employer-org |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
