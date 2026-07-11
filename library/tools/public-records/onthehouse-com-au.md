---
id: onthehouse-com-au
name: OnTheHouse (Australia Property)
description: Use when you have an Australian `address` and want the property's history and value context — returns past sale prices/dates, estimated value, listing history, and property attributes.
url: https://www.onthehouse.com.au/
category: public-records
path:
- public-records
bestFor: Australian property lookups — sale history, value estimates, and listing history from an address.
selectorsIn:
- address
selectorsOut:
- address
- geolocation
status: live
pricing: freemium
costNote: Free to view estimated values, sale history, and property details for most addresses. Fuller property reports and some data are gated/upsold.
opsec: passive
opsecNote: Passive lookup of published property data — no owner is notified. Note owner names are generally NOT shown (unlike a land-titles office); it's property-level data. Standard browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major Australian property portal (CoreLogic data). Sale-history and attribute data are reliable; automated value estimates are approximations, not valuations.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- onthehouse.com.au
- On The House
tags:
- propertysites
- Property Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# OnTheHouse (Australia Property)

> A free Australian property portal — enter an address and get its sale history, estimated value, listing history, and physical attributes, backed by CoreLogic data.

## When to use
You have an Australian `address` and want to understand the property: when it last sold and for how much, its estimated value, past for-sale/for-rent listings, and features (beds/baths/land size). Useful in a missing-person or asset context for confirming a property exists, understanding the household, and building timeline/context around a last-known address. Note it does not publish owner names.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.onthehouse.com.au/ and search the `address` (or browse a suburb).
2. Open the property page: estimated value, sale history (prices + dates), listing history, and property attributes.
3. Note the precise `geolocation` (map pin) and any agent/listing details from past campaigns.
4. Treat estimated values as automated approximations, not formal valuations.
5. Pivot: sale dates anchor a timeline; a listing agent is a contact; the address feeds land-titles/records where owner names are available (paid/official).

## Inputs → Outputs
- **In:** Australian `address` (or suburb)
- **Out:** sale history (prices/dates), estimated value, listing history, property attributes, precise `geolocation`
- **Empty/negative result looks like:** no data / "off market" with sparse history — newer subdivisions or private sales may have thin records; absence of price history isn't proof of anything about occupants.

## Gotchas & OpSec
- No owner names: this is property-level data; to get an owner you need the state land-titles office (usually paid).
- Estimates ≠ valuations: automated value figures can be well off for unusual properties.
- OpSec: passive; nobody is notified.

## Overlaps ("do both")
- Pairs with `[[business-gov-au]]` (if the property is held by a business) and state land-titles searches — OnTheHouse gives the property/market picture, official titles give the owner.

## Trust & verifiability
`trust: community` — a major portal with reliable CoreLogic sale/attribute data; value estimates are approximate, and owner identity must come from an official titles source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onthehouse-com-au |
| category | public-records |
| selectorsIn → selectorsOut | address → address, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
