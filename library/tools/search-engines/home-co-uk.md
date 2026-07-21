---
id: home-co-uk
name: Home.co.uk
description: Use when you have a UK `address` or postcode and want property and price history — returns sold-price `address` records, listings and area context (30+ years of data).
url: https://www.home.co.uk
category: search-engines
path:
- search-engines
bestFor: UK property intelligence — sold prices, current/past listings, and area market data by address or postcode.
selectorsIn:
- address
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free to search for buyers/renters/researchers; agents list for free. No account needed for property and sold-price search.
opsec: passive
opsecNote: Searching a property portal transmits your query to Home.co.uk but nothing to any person; the occupant/owner is not notified. Fully passive. Use a VPN if you want the search off your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established UK property portal aggregating agent listings and Land Registry sold-price data. Listing data is agent-supplied; sold prices derive from Land Registry (authoritative), area stats are the portal's own analysis.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Home.co.uk
- home.co.uk
tags:
- toddington
- curated-directory
- specialty-search
- property
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Home.co.uk

> A UK property portal with deep history — search an address or postcode for sold prices, current and past listings, and area market data going back 30+ years.

## When to use
You have a UK `address` or postcode and want to understand the property and its area: what it last sold for and when (Land Registry-derived), whether it's currently or was recently listed for sale/rent, the property type, and neighbourhood price trends. Useful for confirming a subject's link to an address, estimating tenure/means, spotting a recent move (a live listing), and building area context around a location of interest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.home.co.uk and search the postcode, street, or town.
2. Use the sold-price search to pull historical transactions for the address/street (date, price, property type).
3. Check current and archived listings for the property — a live "for sale/rent" listing signals a possible move and often includes interior photos and floor plans.
4. Review the area/market reports for price trends and rental data as context.
5. Pivot: a sold-price date corroborates when someone acquired/left a property; a live listing (with agent) gives new leads; the address feeds electoral-roll and people-search tools.

## Inputs → Outputs
- **In:** `address` / postcode (UK)
- **Out:** `address` sold-price history & listings, `geolocation`/area context
- **Empty/negative result looks like:** no transactions or listings for the address — the property may never have sold in the covered period (e.g. long-held or new-build) or your postcode/street is mistyped. Absence is not proof of anything about the occupant.

## Gotchas & OpSec
- Property data ≠ occupant data: a sold price tells you about the property and transaction, not who currently lives there — confirm occupancy via electoral roll/people-search.
- Listing data is agent-supplied and can be dated; sold prices (Land Registry) are the authoritative element.
- UK-only. Fully passive.

## Overlaps ("do both")
- Pairs with Rightmove/Zoopla (broader current listings) and the Land Registry / electoral-roll tools — Home.co.uk gives history and area context, those confirm current listings and who is registered at the address.

## Trust & verifiability
`trust: community` — a reputable UK portal; sold-price figures trace to Land Registry (authoritative), while listings are agent-supplied and area stats are the site's own analysis, so weight each accordingly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | home-co-uk |
| category | search-engines |
| selectorsIn → selectorsOut | address → address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
