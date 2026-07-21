---
id: citysearch
name: Citysearch
description: Use when you have a business `name` or `employer-org` and a `geolocation` and want its listing details — returns `address`, `phone`, and a `domain`.
url: http://www.citysearch.com/world
category: search-engines
path:
- search-engines
bestFor: Looking up a local US business's address, phone, and website from a city guide / yellow-pages-style directory.
selectorsIn:
- name
- employer-org
- geolocation
selectorsOut:
- address
- phone
- domain
status: live
pricing: free
costNote: Free to search and read listings; no account needed to browse (claiming/managing a listing is a separate business-owner flow).
opsec: passive
opsecNote: A public directory lookup that touches only Citysearch's servers; the business/person listed is not notified. No special precautions beyond routine sock-puppet browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-running US local directory; listing data is aggregated and can be outdated or duplicated, so confirm the address/phone against a second source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- citysearch.com
tags:
- toddington
- curated-directory
- specialty-search
- local-business
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Citysearch

> A US local business directory / city guide — useful in people work for tying a subject to a business (their own or their employer) and pulling that business's address, phone, and website.

## When to use
You have a business `name` or `employer-org` linked to the subject (a shop they own, a firm they work at, a venue tied to them) plus a rough `geolocation`, and you want the business's `address`, `phone`, and `domain`. This is a business-not-person directory, so its value in a missing-persons context is indirect: it geolocates a workplace or a family business, giving you a physical place and a phone number to work from.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to citysearch.com (the main directory is at `citysearch.com/directory`; browse city hubs from there).
2. Search the business `name` and set the location to the subject's `geolocation` (city/state).
3. Open the matching listing and read off the `address`, `phone`, category, hours, `domain`/website, and any reviews.
4. Cross-check the listing date/freshness — Citysearch aggregates from multiple feeds and can carry closed or relocated businesses.
5. Pivot: feed the `address` into property/records tools and map tools, the `phone` into reverse-phone lookup, and the `domain` into WHOIS/registrant tools.

## Inputs → Outputs
- **In:** business `name` / `employer-org` + `geolocation`
- **Out:** `address`, `phone`, business `domain`/website, category, reviews
- **Empty/negative result looks like:** no listing for the business in that city — it may be too new, too small, closed, or simply never indexed here; try a general maps directory next.

## Gotchas & OpSec
- Business directory, not people search — it locates workplaces/venues, not individuals directly.
- Data is aggregated and frequently stale or duplicated; always confirm the address/phone against a live source (maps, the business's own site) before acting on it.
- OpSec: passive; nobody is notified.

## Overlaps ("do both")
- Pairs with mainstream maps/local directories and reverse-phone tools — Citysearch may hold an older or differently-sourced record that a current maps listing has dropped, and vice versa.

## Trust & verifiability
`trust: unverified` — a real, long-standing directory, but listing accuracy is aggregator-dependent; treat any address/phone as a lead to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | citysearch |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org, geolocation → address, phone, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
