---
id: redfin
name: Redfin
description: Use when you have an `address` and want a property's sale history, valuation, and details — returns ownership-history dates, prices, and `geolocation` context.
url: https://redfin.com
category: public-records
path:
- public-records
- property-records
bestFor: Pulling a U.S. property's sale/price history, tax, and listing details from an address.
selectorsIn:
- address
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free to browse property and sale-history data; no account needed for public listing/record pages.
opsec: passive
opsecNote: Passive — Redfin is a public real-estate platform; looking up a property does not notify anyone associated with it. Redfin logs standard web activity; use a clean session for sensitive lookups and avoid saving searches/favorites under a real account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Major licensed U.S. real-estate brokerage; listing and sale-history data are sourced from MLS and public records, making them reliable (though owner names are not shown).
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- zillow
- realtor-com
aliases:
- redfin.com
tags:
- property-records
- real-estate
- public-records
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Redfin

> A free U.S. real-estate platform whose property pages expose sale history, valuations, and details useful for placing a person at an address.

## When to use
You have an `address` linked to a subject and want to learn about the property: when it last sold and for how much, its price/valuation history, tax assessment, size, photos, and neighborhood. Helps corroborate a residence, estimate move-in/move-out timing from sale dates, and add `geolocation` context. Redfin does not publish owner *names*, so use it alongside county assessor/deed records when you need the actual owner.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://redfin.com and search the `address`.
2. Open the property page and review: sale/listing history (dates + prices), current estimate, tax history, beds/baths/size, and photos.
3. Read the sale-history timeline for clues about when the subject may have moved in or out.
4. Note the map location and neighborhood for `geolocation` context.
5. Pivot: sale dates and prices feed county deed/assessor lookups (which carry owner `name`s) and timeline-building; photos aid site verification.

## Inputs → Outputs
- **In:** `address` (or place/neighborhood to browse).
- **Out:** sale/price history, tax assessment, property details, photos, and map `geolocation`.
- **Empty/negative result looks like:** "we don't have information on this home" or off-market with no history — meaning Redfin/MLS lacks data for that parcel, not that the address is invalid.

## Gotchas & OpSec
- No owner names: Redfin shows the property, not who owns it — get names from county deed/assessor records.
- U.S.-only and MLS-dependent: coverage and detail vary by market; some off-market homes have thin data.
- Estimates are modeled: the "Redfin Estimate" is an algorithmic value, not an appraisal.
- OpSec: passive; don't favorite/save under an attributable account.

## Overlaps ("do both")
- Pairs with `[[zillow]]` / `[[realtor-com]]` (cross-check history/estimates) and with county assessor/deed tools that supply the owner `name` Redfin omits.

## Trust & verifiability
`trust: trusted` — a licensed brokerage sourcing from MLS and public records; sale-history facts are reliable, but confirm ownership via the authoritative county record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | redfin |
| category | public-records |
| selectorsIn → selectorsOut | address → address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
