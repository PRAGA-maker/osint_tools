---
id: irelandhouse-ie
name: Ireland House (Property Price Register)
description: Use when you have an Irish `address`/Eircode (or an area) and want historical property sale prices and dates — returns sale price, date and property address from Ireland's Residential Property Price Register.
url: https://irelandhouse.ie/
category: public-records
path:
- public-records
bestFor: Searching historical residential property sales in Ireland by address/Eircode, county, price and date.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free to search; built on the public Residential Property Price Register (PSRA / Revenue stamp-duty filings).
opsec: passive
opsecNote: Public property-sales data; searching is passive and notifies no one. No login required. Note the register lists sale price/date/address but not buyer/seller names.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party front-end partially based on Ireland's official Residential Property Price Register (PSRA data). The underlying sales data is authoritative; presentation and any derived statistics are this site's own.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- irelandhouse.ie
- Ireland House property register
tags:
- propertysites
- property-records
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Ireland House (Property Price Register)

> A searchable, mapped front-end to Ireland's Residential Property Price Register — look up what a property sold for and when, by address, Eircode, county, price or date.

## When to use
You have an Irish `address`/Eircode (or an area) and want the property's sale history: price and date of past transactions. In an OSINT context this corroborates that a subject bought/sold at an address and roughly when (a timeline anchor and a wealth/asset signal), and helps confirm addresses tied to a person. Note it does not name buyers/sellers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://irelandhouse.ie/.
2. Search by address or Eircode, or filter by county, sale price range, date range, and new-build vs pre-owned.
3. Read the results: property address, sale price, and sale date; use the sale-price map and "IH Sale Statz" for area context.
4. Cross-check against the official Residential Property Price Register (propertypriceregister.ie) for the authoritative record.
5. Pivot: a sale date/price at a subject's suspected address corroborates a residency/ownership timeline; combine with electoral, company (registered-address) and people-search sources to attach names, which this register omits.

## Inputs → Outputs
- **In:** Irish `address` / Eircode (or area filters)
- **Out:** property `address`, sale price, sale date (transaction history)
- **Empty/negative result looks like:** no transactions for the address/area/date filter — the property may not have sold in the covered period (register starts 2010), or your filters are too narrow. Absence of a sale isn't proof of non-ownership.

## Gotchas & OpSec
- **No names:** the Price Register records price/date/address, not buyer or seller identity — you must attach names via other sources.
- Coverage begins in 2010 and reflects filed stamp-duty data; pre-2010 or unrecorded transfers won't appear.
- It's a third-party presentation — confirm critical figures against the official register.
- OpSec: passive, public data.

## Overlaps ("do both")
- Pairs with the official propertypriceregister.ie (authoritative source) and with electoral/company registries that carry names — the register gives the transaction; those attach the person to the address.

## Trust & verifiability
`trust: community` — a convenient third-party layer over authoritative PSRA property-sales data. Verify specific sale figures against the official Residential Property Price Register, and treat the site's derived statistics as its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | irelandhouse-ie |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
