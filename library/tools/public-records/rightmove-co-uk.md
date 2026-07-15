---
id: rightmove-co-uk
name: rightmove.co.uk
description: Use when you have a UK `address`/postcode and want a property's sold-price history and past listing photos — Rightmove's house-price tool returns Land Registry sale prices, dates and interior/exterior images.
url: https://www.rightmove.co.uk/house-prices.html
category: public-records
path:
- public-records
bestFor: Pulling a UK property's sold-price history and archived listing photos/floorplans from an address.
selectorsIn:
- address
selectorsOut:
- address
- image
status: live
pricing: free
costNote: Free to search sold prices and view archived listings; a free account only adds tracking features. No payment needed.
opsec: passive
opsecNote: Looking up a property is a passive, anonymous query against public sold-price data — no signal to any owner or occupier. A normal browser is fine; sign in only if you want tracking, which attaches your identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Rightmove is the UK's largest property portal; its sold-price data comes from HM Land Registry / Registers of Scotland (authoritative), and listing photos are the portal's own archive.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Rightmove house prices
- Rightmove sold prices
tags:
- propertysites
- Property Related Sites
- uk
- property
- sold-prices
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# rightmove.co.uk

> Rightmove's sold-price search — put in a UK address and get its Land Registry sale history *plus* the photos and floorplans from the last time it was listed.

## When to use
You have a UK `address` or postcode tied to a subject and want to understand the property: when it last sold and for how much (a wealth/tenure signal), and — uniquely valuable — archived interior/exterior **photos and floorplans** from past sales listings. Those images can reveal a property's layout, condition, and identifying features, and confirm you have the right place. Note it is address-keyed, not name-keyed: it won't name the owner.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.rightmove.co.uk/house-prices.html and enter the street, town, or postcode.
2. Select the specific property from the list.
3. Read the sold-price history (each sale's date and price, from Land Registry/Registers of Scotland) and open any archived listing for photos and floorplans.
4. Pivot: sale dates bracket when the subject may have moved in/out; images feed property/geolocation verification; the price feeds asset context. Combine with electoral-roll/company data to attach a name.

## Inputs → Outputs
- **In:** `address` / postcode (UK)
- **Out:** sale-price history and dates (property `address` record), archived `image`s (listing photos, floorplans)
- **Empty/negative result looks like:** no sold-price record (never sold in the covered period, new-build not yet registered, or a rental) and/or no archived listing (never marketed on Rightmove). Absence of a sale ≠ absence of the property; there's also a weeks-to-months lag before recent sales appear.

## Gotchas & OpSec
- **No owner names:** Land Registry price-paid data (and thus Rightmove) is address-based — to name the owner you need the Land Registry title register (paid) or electoral/company data.
- Data lags (~weeks–months after sale; Land Registry updates monthly).
- Archived photos reflect the *last listing*, which may predate the current occupant — date them.
- OpSec: passive; sign-in optional and attributable.

## Overlaps ("do both")
- Pairs with the HM Land Registry title/price-paid service, Zoopla (parallel sold-price + its own listing archive), and the electoral roll — Zoopla often has different archived photos; Land Registry title names the owner; the roll ties a name to the address.

## Trust & verifiability
`trust: trusted` — authoritative Land Registry sale data via the UK's leading portal. Prices/dates are reliable; treat archived photos as time-stamped to the last listing, not the present.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rightmove-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | address → address, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
