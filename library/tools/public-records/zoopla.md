---
id: zoopla
name: Zoopla
description: Use when you have a UK `address` or postcode and want property details, price/sale history, and estimated value — returns property records, past listings, and photos tied to an address.
url: https://www.zoopla.co.uk/
category: public-records
path:
- public-records
bestFor: Looking up UK property details, sale history, and past sale/rental listing photos by address or postcode.
selectorsIn:
- address
selectorsOut:
- address
- image
status: live
pricing: freemium
costNote: Free to browse property pages, price estimates, and sold-price history. Some agent/valuation features prompt for registration, but the core address/property lookup is free and needs no account.
opsec: passive
opsecNote: You browse a public property portal; no owner or occupant is contacted or notified. Standard commercial-site logging applies — use a VPN for hygiene. Do not create alerts or contact agents from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major UK property portal; listing and sold-price data is aggregated from agents and Land Registry, so it is broadly reliable but is a commercial aggregation, not a primary registry.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- primelocation
aliases:
- Zoopla.co.uk
tags: []
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Zoopla

> A major UK property portal — enter an address or postcode to see property details, sold-price history, and archived sale/rental listings with interior photos.

## When to use
You have a UK `address` (or postcode) and want to characterize the property and its history: bedrooms/type, estimated current value, dates and prices of past sales, and — often the most useful part — old estate-agent listing photos showing the interior and layout at the time of sale. This corroborates a subject's link to an address, establishes when a property changed hands, and can reveal details (renovations, contents, garden, vehicles in driveway) from archived listing imagery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.zoopla.co.uk/ and search the `address` or postcode.
2. Open the specific property page for property type, floor area, and current estimated value.
3. Check the **sold prices** / price history section for dated past sale prices (sourced from Land Registry).
4. Look for archived **for-sale / to-rent listings** on that address — these carry agent photos and descriptions from the time of listing.
5. Pivot: sale dates → registry/electoral-roll timelines; listing photos → geolocation/detail analysis; a linked agent → further context.

## Inputs → Outputs
- **In:** UK `address` or postcode
- **Out:** property details, dated sale/price history (`address`), and archived listing photos (`image`)
- **Empty/negative result looks like:** the address shows only a generic estimate with no sale history or past listings — the property may never have been listed on Zoopla or sold recently. Cross-check [[primelocation]] and Rightmove, which draw on overlapping but not identical agent feeds.

## Gotchas & OpSec
- Data is a commercial aggregation — sold prices trace back to Land Registry (reliable), but estimates and property attributes can be stale or wrong; treat as leads.
- Photos are from the time of the listing, which may be years old; don't assume they reflect the current state or occupant.
- OpSec: **passive** — browsing only. Don't request valuations, save searches, or contact agents from an attributable account.

## Overlaps ("do both")
- Pairs with [[primelocation]] (same owner group, overlapping listings) and with Rightmove; different portals archive different agent listings, so run more than one to recover the fullest photo/price history.

## Trust & verifiability
`trust: community` — a large, reputable UK portal, but a commercial aggregator: sold-price data is Land-Registry-backed and trustworthy, while estimates and attributes should be verified against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zoopla |
| category | public-records |
| selectorsIn → selectorsOut | address → address, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
