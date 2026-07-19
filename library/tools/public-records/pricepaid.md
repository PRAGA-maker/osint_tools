---
id: pricepaid
name: HM Land Registry Price Paid Data
description: Use when you have a UK `address`/postcode and want its property sale history — returns sale prices, dates and property type (no owner names).
url: https://landregistry.data.gov.uk/app/ppd
category: public-records
path:
- public-records
bestFor: Looking up the recorded sale price, date, and type of a UK residential property by address or postcode.
selectorsIn:
- address
selectorsOut:
- address
- document-id
status: live
pricing: free
costNote: Free official HM Land Registry open data; no account. Covers property transactions in England and Wales.
opsec: passive
opsecNote: You query a government open-data property database, not a person — passive, and the target is not notified. Note the data is address/transaction-level and contains no names, so it can't directly identify who bought or lives at a property.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official HM Land Registry Price Paid Data — the authoritative record of registered property sales in England and Wales, published as open government data.
missingPersonsRelevance: low
coverage:
- gb
auth: none
api: true
localInstall: false
registration: false
aliases:
- Price Paid Data
- PPD
- Land Registry Price Paid
tags:
- property
- public-records
- uk
- land-registry
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# HM Land Registry Price Paid Data

> The UK government's authoritative record of property sale prices — search any England/Wales address or postcode for its transaction history (price, date, type), free.

## When to use
You have a UK `address` or postcode connected to a subject and want to establish the property's sale history: when it last changed hands, for how much, whether freehold/leasehold, and the property type. This corroborates timelines (a move date), assesses circumstances, and cross-references an address against a period of interest. Note it does not name owners — pair it with the separate (paid) Land Registry title register for ownership.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://landregistry.data.gov.uk/app/ppd.
2. Search by address components (building name/number, street, town, postcode) and refine by property type, price range, date, and estate type (freehold/leasehold), new-build status.
3. Read the results: each transaction shows the sold price, date of sale, property type, and address — bookmark/share via the result URL.
4. For bulk/automated use, pull the same data via the Land Registry open-data API/downloads.
5. Pivot: a sale date feeds a residence timeline; to get the owner's name, order the official title register separately (paid) — PPD alone won't provide it.

## Inputs → Outputs
- **In:** UK `address` / postcode
- **Out:** sale price(s), sale date(s), property type, estate type for that `address` (transaction `document-id`s)
- **Empty/negative result looks like:** no transactions — the property may not have sold in the covered period, or the address string didn't match; absence is not proof no one lives there.

## Gotchas & OpSec
- No names: PPD is transaction data only — it cannot tell you who owns or occupies a property.
- England & Wales only (Scotland uses Registers of Scotland; Northern Ireland separate).
- Only registered sales appear; inherited/transferred-without-sale properties and some corporate/commercial deals may be absent or differently recorded.
- OpSec: passive government open-data lookup.

## Overlaps ("do both")
- Complements the Land Registry title register (paid) — PPD gives price/date history free; the title register gives the registered owner's name for the same address.

## Trust & verifiability
`trust: trusted` — official government open data, authoritative for registered England/Wales sales. Reliable for price/date/type; just don't infer ownership or occupancy from it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pricepaid |
| category | public-records |
| selectorsIn → selectorsOut | address → address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
