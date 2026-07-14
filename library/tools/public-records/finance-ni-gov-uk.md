---
id: finance-ni-gov-uk
name: Land & Property Services NI — Property Valuation Search
description: Use when you have a Northern Ireland property `address` and want its official valuation/rating record — returns the property's capital value and rating details from the NI valuation list.
url: https://valuationservices.finance-ni.gov.uk/Property/Search
category: public-records
path:
- public-records
bestFor: Confirming a Northern Ireland property exists on the rating list and its official capital value.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free official public valuation search; no account needed.
opsec: passive
opsecNote: Public property-valuation search keyed on address; no living person is queried and no login is required, so it's fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Northern Ireland government service (Land & Property Services, Dept of Finance); authoritative for rating/valuation, but it returns property data, not owner identities.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- LPS NI valuation
- finance-ni valuation services
tags:
- propertysites
- Property Related Sites
- northern-ireland
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Land & Property Services NI — Property Valuation Search

> Northern Ireland's official property valuation/rating search — enter an NI address to confirm the property and pull its capital value and rating record.

## When to use
You have a Northern Ireland `address` linked to a subject and want to corroborate the property and understand it: does it exist on the rating list, what is its official capital value (a proxy for property tier/wealth), and what are its rating details? Useful for grounding an address, assessing a subject's circumstances, and confirming you have the right property before deeper property/ownership work. Note it returns *property* data — not the occupier's or owner's name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://valuationservices.finance-ni.gov.uk/Property/Search.
2. Search by the NI address (postcode/street).
3. Select the matching property and read its capital value and rating details.
4. Use the confirmed property as an anchor; for ownership, follow up with Land Registry NI.
5. Pivot: capital value → wealth/tier context; confirmed address → electoral/other NI records and ownership searches.

## Inputs → Outputs
- **In:** `address` (Northern Ireland property)
- **Out:** confirmed property `address`, official capital value, rating record
- **Empty/negative result looks like:** no matching property — check address formatting/postcode; the list covers domestic NI rateable properties, so unusual premises may not appear as expected.

## Gotchas & OpSec
- Northern Ireland only — not the rest of the UK (England/Wales/Scotland use different systems).
- Returns property/valuation data, NOT owner or occupier names — pair with Land Registry NI for ownership.
- Valuation reflects rating basis, not market price.

## Overlaps ("do both")
- Pairs with Land Registry Northern Ireland (ownership) and the electoral register — this confirms the property and its value; those add who is connected to it.

## Trust & verifiability
`trust: trusted` — an official NI government valuation service; the property/valuation data is authoritative. It simply doesn't include personal identities, so combine it with ownership/occupancy sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | finance-ni-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
