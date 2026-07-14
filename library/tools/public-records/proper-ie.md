---
id: proper-ie
name: proper.ie
description: Use when you have an Irish `address`/area and want sale-price history from Ireland's public Residential Property Price Register — returns transaction price/date context to corroborate an address timeline.
url: https://proper.ie/
category: public-records
path:
- public-records
bestFor: Checking Irish residential sale prices and history by area from the public Property Price Register.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free to access; built on Ireland's public Residential Property Price Register (PPR) data.
opsec: passive
opsecNote: Reading aggregated public sale data is passive and leaks nothing about the subject. The PPR records transactions, not current occupants — do not infer present residency from a past sale.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party front-end over Ireland's official Residential Property Price Register; the underlying transaction data is authoritative, but proper.ie presents it as market analytics rather than person-level lookup.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- proper.ie
- Irish property price register viewer
tags:
- propertysites
- Property Related Sites
- ireland
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# proper.ie

> A viewer over Ireland's public Residential Property Price Register — sale prices, dates, and area trends, useful to corroborate an address's transaction history (not to name its occupant).

## When to use
You have an Irish `address` or area and want to know its residential sale history: what sold, when, and for how much, drawn from Ireland's official Property Price Register. Use it to corroborate a property-transaction timeline around a subject (e.g. a sale date aligning with a move) or to characterize an area — not as a person-to-address lookup, which the PPR does not provide.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://proper.ie/.
2. Browse/search by county or area to see aggregated price history and sale frequency; drill toward the specific locality.
3. Read the transaction context: sale prices and dates from the PPR, and area-level trends over time.
4. Cross-reference with the official PPR (propertypriceregister.ie) for the raw record when you need the authoritative transaction line.
5. Pivot: a dated sale can anchor a subject's move timeline; combine with people-search/electoral data to link a person to the address (the PPR alone won't name them).

## Inputs → Outputs
- **In:** Irish `address`/area
- **Out:** sale price/date and area trends for that `address`/locality
- **Empty/negative result looks like:** no transactions for the area/period — meaning no *recorded sale* (long-held or rented property), not that no one lives there. The register covers sales, not tenancies or ownership names.

## Gotchas & OpSec
- Transactions, not occupants: the PPR does not list buyer/seller names or current residents — do not over-read a sale as identifying a person.
- proper.ie is analytics-oriented; for a specific transaction line, confirm against the official PPR.

## Overlaps ("do both")
- Complements electoral-roll/people-search tools: proper.ie dates the property transaction, while those sources attempt to attach a person to the address.

## Trust & verifiability
`trust: community` — a third-party viewer over authoritative government PPR data; verify a specific sale against the official register before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | proper-ie |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
