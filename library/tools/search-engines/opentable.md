---
id: opentable
name: OpenTable
description: Use when you have a `name` and want restaurant-review traces — search a diner's public reviews to place them at restaurants/cities and infer routine.
url: https://www.opentable.com
category: search-engines
path:
- search-engines
bestFor: Finding a subject's public restaurant reviews to tie them to locations, dates, and dining patterns.
selectorsIn:
- name
- username
selectorsOut:
- geolocation
- social-profile
status: live
pricing: free
costNote: Free to browse restaurants and public diner reviews; booking requires an account but reconnaissance does not.
opsec: passive
opsecNote: Reading public restaurant listings and diner reviews is passive; the reviewer isn't notified. No login needed to browse. Don't book or message from an identifiable account while investigating.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: OpenTable is a major, legitimate restaurant-reservation platform; diner reviews are real user content but only a weak, indirect people-search signal.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- yelp
- google
aliases:
- opentable.com
tags:
- toddington
- curated-directory
- reviews
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# OpenTable

> A restaurant-reservation platform whose public diner reviews are a minor OSINT breadcrumb — placing a subject at specific restaurants, cities, and dates.

## When to use
A weak, supplementary people-search angle: if a subject writes OpenTable reviews (usually under a first name + last initial), those reviews can place them at particular restaurants and cities on particular dates, hinting at where they live, travel, or dine. Reach for it only when building out a lifestyle/pattern picture or corroborating a location — not as a primary locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Rather than OpenTable's weak on-site search, dork a search engine: `site:opentable.com "First L"` plus a city, or search a `username` a subject reuses.
2. Open restaurant pages and read diner reviews; note reviewer display name, city, and review dates.
3. Match a reviewer to your subject only via corroborating signals (reused handle, consistent city, cross-linked profiles) — first-name-last-initial alone is not enough.
4. Build a rough pattern: which cities/restaurants and when.
5. Pivot: places/dates → timeline corroboration; a reused `username` → cross-platform search; broader review coverage → `[[yelp]]`.

## Inputs → Outputs
- **In:** a `name` or `username`
- **Out:** public restaurant reviews → `geolocation` (cities/venues), dates, a `social-profile`-style reviewer identity
- **Empty/negative result looks like:** no reviews attributable to the subject — most people never review on OpenTable, so a null is expected and near-meaningless.

## Gotchas & OpSec
- Very low signal: reviewer identities are minimal (first name + last initial), so attribution is hard and easily wrong — corroborate heavily.
- Coverage skews to reservation-taking restaurants in certain markets; absence proves nothing.
- Booking/messaging needs an account and would be active — stay in read-only recon.

## Overlaps ("do both")
- Pairs with `[[yelp]]` — Yelp has far more review coverage and richer profiles; OpenTable is a narrow add-on. Check Yelp first for dining/location patterns.
- Pairs with `[[google]]` using `site:` dorks to actually surface the reviews.

## Trust & verifiability
`trust: trusted` — OpenTable is a legitimate major platform and reviews are genuine user content, but as an identity/location signal it's weak and indirect; never attribute a review to a subject without strong corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opentable |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → geolocation, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
