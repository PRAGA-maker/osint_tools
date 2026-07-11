---
id: propertypriceregister-ie
name: Residential Property Price Register (Ireland)
description: Use when you have an Irish `address` (or area) and want to confirm a residential sale, its date and price — returns the sale date, price and full address for properties sold in Ireland since 2010.
url: https://www.propertypriceregister.ie/website/npsra/pprweb.nsf/PPR?OpenForm
category: public-records
path:
- public-records
bestFor: Confirming that an Irish residential property sold, exactly when, for how much, and at what precise address (2010 onward).
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Official government register, completely free to search and to download (individual records or the full dataset); no account needed.
opsec: passive
opsecNote: This is an official open-data register of transactions, not a person query — searching it is fully passive and notifies no one. It contains no owner names, so it reveals a sale event, not who lives there now.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Ireland's Property Services Regulatory Authority (PSRA) under the Property Services (Regulation) Act 2011; authoritative, though the PSRA does not edit filers' data so occasional entry errors persist.
missingPersonsRelevance: medium
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- PPR Ireland
- Irish Property Price Register
- PSRA property register
tags:
- propertysites
- Property Related Sites
- ireland
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Residential Property Price Register (Ireland)

> Ireland's official record of every residential property sale since 2010 — date, price and exact address, straight from the state regulator.

## When to use
You have an Irish `address` (or you're canvassing a street/area) and want to establish the property's transaction history: did it sell, when, and for how much. This corroborates that an address is a real dwelling, bounds when a subject could have moved in/out (a sale date), and surfaces the price for financial context. Note it does NOT list buyer/seller names, so it is a transaction record, not an ownership lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the register at the URL.
2. Filter by county, and optionally date range, price range, or type; search or browse to the target `address`.
3. Read each matching row: date of sale, price paid, and the full address (some rows are asterisked where the price isn't full market value — e.g. non-arm's-length sales).
4. Download individual records or the whole dataset as CSV for offline cross-referencing.
5. Pivot: a sale date brackets residency timelines; the address feeds electoral-register/Eircode and other Irish records; the price feeds financial-profile reasoning.

## Inputs → Outputs
- **In:** `address` (or county/area + date/price filters)
- **Out:** confirmed `address`, plus sale date and price for each transaction
- **Empty/negative result looks like:** no rows for the address — it hasn't sold since 2010 (long-held, rented, or new-build not yet transacted), or the address is recorded slightly differently; absence is not proof the dwelling doesn't exist.

## Gotchas & OpSec
- No names: the register never contains buyer/seller identities — pair it with the electoral register or Land Registry for people.
- Data quality: PSRA doesn't edit filings, so misspelled/mis-keyed addresses and asterisked (non-market) prices appear — read carefully.
- OpSec: passive open data.

## Overlaps ("do both")
- Pairs with the Irish electoral register / Eircode tools — the PPR gives the sale, those give who is registered there.
- Pairs with `[[github-io]]` genealogy/records when building a family's Irish property history.

## Trust & verifiability
`trust: trusted` — an authoritative first-party government register; the sale facts are reliable, with the only caveat being un-edited filer errors and clearly-flagged non-market prices.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | propertypriceregister-ie |
