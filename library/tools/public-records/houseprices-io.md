---
id: houseprices-io
name: houseprices.io
description: Use when you have a UK `address`/postcode and want the property's sold-price history and transaction dates from Land Registry data — returns address, sale history (no owner names).
url: https://houseprices.io/
category: public-records
path:
- public-records
bestFor: Looking up UK (England & Wales) sold-price history and transaction dates for an address/postcode.
selectorsIn:
- address
- geolocation
selectorsOut:
- address
status: live
pricing: free
costNote: Free to search; presents official Land Registry "price paid" data (Jan 1995–present) for England & Wales. No account needed.
opsec: passive
opsecNote: Read-only lookup of official public price-paid records; the subject is not notified and nothing is disclosed. No login. Note the data does NOT include owner names — it's property transactions, not people.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A convenient front-end over official HM Land Registry Price Paid Data; the underlying transaction records are authoritative, though this third-party site's freshness lags the official feed.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- houseprices.io
- UK sold prices
tags:
- propertysites
- Property Related Sites
- land-registry
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# houseprices.io

> A fast, free front-end to UK (England & Wales) Land Registry sold-price data: enter an address or postcode and get the property's full transaction history — dates and prices, not owners.

## When to use
You have a UK `address` or postcode and want the property's sale history: when it last sold, for how much, and its transaction record back to 1995. Useful for corroborating how long someone may have been at an address, dating a move, gauging affluence, or confirming a property exists as described. Set expectations: it gives *property transaction* data, not owner names.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://houseprices.io/ and search by `address` or postcode (or browse a street/postcode).
2. Open the property; read its price-paid history — each row is a sale date, price, and full address.
3. Use the timeline: the most recent sale roughly bounds when the current occupant may have arrived.
4. Cross-reference the address with people-search/electoral data to attach names — houseprices.io alone won't.
5. Pivot: sale date/price feeds affluence and timeline inferences; the confirmed address feeds electoral roll and reverse-address people-search.

## Inputs → Outputs
- **In:** UK `address` or postcode (`geolocation`)
- **Out:** property `address` with sold-price history (transaction dates + amounts)
- **Empty/negative result looks like:** no transactions listed — the property may never have sold since 1995, be new-build not yet recorded, or be outside England & Wales (Scotland/NI use different registries).

## Gotchas & OpSec
- No owner names — UK price-paid data is property-level, not people-level; you must pivot to electoral/people data for names.
- England & Wales only; Scotland (ScotLIS) and Northern Ireland use separate registries.
- Third-party front-end — for authority, cross-check against the official HM Land Registry Price Paid service.
- OpSec: fully passive, public records.

## Overlaps ("do both")
- Pairs with electoral-roll/people-search (to put names to the address) and the official HM Land Registry Price Paid Data (authoritative source); also with [[hauziz]]-style reverse-address tools for non-UK.

## Trust & verifiability
`trust: community` — a convenience layer over authoritative Land Registry data; the transactions are official, but verify against the primary Land Registry service and remember it carries no owner identities.
