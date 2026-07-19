---
id: realtor-com-united-states
name: Realtor.com (United States)
description: Use when you have a US `address` or an agent `name` and want property listing history or a real-estate agent's contact/brokerage — returns address details, agent phone and employer-org.
url: http://www.realtor.com
category: search-engines
path:
- search-engines
bestFor: Pulling a US property's listing/sale history or finding a named real-estate agent's brokerage and contact details.
selectorsIn:
- address
- name
selectorsOut:
- address
- phone
- employer-org
status: live
pricing: free
costNote: Free to browse listings and the agent directory; no account needed for search. Realtor.com monetizes via agent advertising, not user fees.
opsec: passive
opsecNote: Browsing is passive against the subject — you query a public listings portal, not the person. Note the site runs aggressive bot-detection (PerimeterX), so automated scraping trips CAPTCHAs; drive it in a normal browser and it leaks nothing to the target.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Move, Inc. (News Corp) and the official consumer-facing portal affiliated with the National Association of Realtors; listing data is sourced from MLS feeds.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- realtor
aliases:
- realtor.com
- Move Inc listings
tags:
- toddington
- curated-directory
- specialty-search
- real-estate
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Realtor.com (United States)

> The NAR-affiliated US listings portal, useful as a property-history lookup and a searchable directory of real-estate agents with their brokerage and contact details.

## When to use
You have a US `address` and want to know whether it is or was on the market (list price, photos, sale history, beds/baths) to corroborate where someone lives or lived; or you have an agent `name` and want their brokerage (`employer-org`), service area, and business `phone`. It does not expose private owner names — treat it as listing/agent intelligence, not a deed/owner lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.realtor.com in a normal browser session.
2. For a property: enter the `address` in the search bar. Read the listing card — status (for sale / sold / off-market), price history, photos (interior/exterior for geolocation corroboration), and property facts.
3. For an agent: use the "Find a Realtor" / agents directory and search the `name` plus a city. Read the agent's brokerage, phone, recent listings, and areas served.
4. Pivot: photos and sale dates feed `[[realtor]]` and county deed/assessor lookups; an agent's brokerage feeds employer/company OSINT.

## Inputs → Outputs
- **In:** `address` (property) or `name` (agent)
- **Out:** listing history / property facts / photos (for an address); agent `phone`, `employer-org` (brokerage), service area (for a name)
- **Empty/negative result looks like:** "We couldn't find that address" or an off-market property with no history — this means no MLS listing, NOT that the address is invalid; many owner-occupied homes never appear.

## Gotchas & OpSec
- Human-in-the-loop: PerimeterX bot-detection throws CAPTCHAs and blocks headless fetches — use a real browser, not a scraper.
- Off-market homes show sparse data; absence of a listing proves nothing about occupancy.
- Owner identity is not published here; use the county assessor/recorder for that.
- OpSec: passive — the subject is never notified.

## Overlaps ("do both")
- Pairs with `[[realtor]]` — the two cover overlapping MLS feeds; one may carry a listing (and photos) the other has aged out.

## Trust & verifiability
`trust: trusted` — first-party consumer portal fed by MLS data via Move, Inc. (News Corp); listing facts are authoritative, though staleness on off-market records is common.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | realtor-com-united-states |
| category | search-engines |
| selectorsIn → selectorsOut | address, name → address, phone, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
