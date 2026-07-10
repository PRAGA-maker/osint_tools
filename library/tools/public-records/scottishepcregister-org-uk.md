---
id: scottishepcregister-org-uk
name: Scottish EPC Register
description: Use when you have a Scottish `address` or postcode and want the property's Energy Performance Certificate — returns property characteristics and confirmation the dwelling exists.
url: https://www.scottishepcregister.org.uk/CustomerFacingPortal/TermsAndConditions
category: public-records
path:
- public-records
bestFor: Looking up the EPC for a property in Scotland by postcode/address to confirm a dwelling and read its physical characteristics.
selectorsIn:
- address
selectorsOut:
- address
- metadata-exif
status: live
pricing: free
costNote: Free public register operated by Energy Saving Trust on behalf of Scottish Ministers; no account required to search by postcode.
opsec: passive
opsecNote: You query a public property register, not the occupant, so nobody is contacted or alerted. EPCs describe the building, not who lives there — treat it as property intelligence only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Scottish Government-mandated EPC register; the data is authoritative for property energy assessments, though it reflects the dwelling, not current occupancy.
missingPersonsRelevance: medium
coverage:
- gb-sct
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Scottish EPC Register
- scottishepcregister.org.uk
tags:
- propertysites
- property
- scotland
- energy-performance
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Scottish EPC Register

> Scotland's official Energy Performance Certificate register — search a postcode/address to confirm a dwelling exists and read its physical characteristics (type, size, age band, heating).

## When to use
You have a Scottish `address` (or postcode) and want independent confirmation the property exists and what it is like. An EPC records the property type (flat/house), floor area, age band, wall/roof construction, heating and glazing — useful for corroborating an address, sizing a household, or distinguishing multiple units at one postcode. It is the Scottish counterpart to England & Wales EPC registers; it does not name occupants.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.scottishepcregister.org.uk/ and choose **Search EPC by Postcode** (or by RRN reference if you have one).
2. Enter the Scottish postcode; pick the specific address from the returned list.
3. Open the EPC to read property type, floor area, age band, construction, heating and the energy rating.
4. Pivot: the confirmed `address` and dwelling type feed UK people-search/electoral tools (e.g. `[[192]]`) to attach occupants; multiple flats at one postcode help disambiguate which unit a subject occupies.

## Inputs → Outputs
- **In:** `address` / postcode (Scotland)
- **Out:** confirmed `address` and `metadata-exif`-style property characteristics (type, size, age, heating, EPC rating)
- **Empty/negative result looks like:** no EPC lodged for the address (older or never-assessed properties may have none) — absence means "no certificate," not "no property."

## Gotchas & OpSec
- Coverage is **Scotland only**; use the England & Wales EPC register for the rest of the UK.
- An EPC describes the building, never the occupant — do not infer who lives there from it.
- Not every property has a lodged EPC; gaps are common for homes not recently sold, let, or built.
- OpSec: fully passive public-register lookup.

## Overlaps ("do both")
- Pairs with `[[192]]` — the EPC confirms and characterises the dwelling; 192/electoral tools attach names and associates to it. Do both to move from "a property exists" to "who is linked to it."

## Trust & verifiability
`trust: trusted` — statutory Scottish register; data is authoritative for the building's assessed characteristics, with the caveat that it says nothing about occupancy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scottishepcregister-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | address → address, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
