---
id: bc-assessment
name: BC Assessment
description: Use when you have a British Columbia `address` and want the property's official assessment — returns assessed value, property characteristics and sales history for that `address` (property data, not the owner's identity).
url: https://www.bcassessment.ca
category: people-search
path:
- people-search
bestFor: Looking up a BC property's assessed value and characteristics by civic address.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free public property-assessment search by address, PID, or roll number. No account or payment for the standard property report.
opsec: passive
opsecNote: You query a public property-assessment database by address; no person is searched and nothing reaches any occupant. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: BC Assessment is the official provincial property-assessment authority for British Columbia — authoritative valuation and property data. Note it publishes property/value data, not owner names, so don't expect PII.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- land-registry
aliases:
- BC Assessment
- bcassessment.ca
tags:
- address
- property
- british-columbia
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# BC Assessment

> The official British Columbia property-assessment lookup — enter a BC address and get its assessed value, characteristics, and recent sales history (property data, not the owner's name).

## When to use
You have a British Columbia `address` tied to a subject and want objective context about the property: its assessed value, lot/building size, year built, property class, and recent sale prices/dates. Useful for gauging a subject's circumstances at an address, corroborating a location, or comparing properties — with the important caveat that BC Assessment's public search returns *property* data, not the owner's `name` or contact details.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bcassessment.ca.
2. Search by civic `address` (or PID / roll number, or the map search).
3. Open the property report: assessed value (current and prior years), land/building characteristics, and recent sales history.
4. Use the value/characteristics as context; note there is no owner name here.
5. Pivot: for ownership/title (owner `name`, charges), go to the BC land title registry (`[[land-registry]]`); combine the property picture with people-search to connect an occupant to the address.

## Inputs → Outputs
- **In:** `address` (BC civic address, PID, or roll number)
- **Out:** assessed value, property characteristics, sales history, confirmed `address`
- **Empty/negative result looks like:** no property found — the address is mistyped, outside BC, or newly created. It returns property facts only, so it never confirms who lives there.

## Gotchas & OpSec
- Human-in-the-loop: none; a public property lookup.
- OpSec: **passive** — property-assessment data; no person is queried.
- Key limitation: **no owner identity** in the free public search — this is valuation/characteristics data. For the owner you need the paid land-title registry. Assessed value is an official estimate, not a market price.

## Overlaps ("do both")
- Pairs with the BC land title registry (`[[land-registry]]`) — BC Assessment gives value/characteristics for free; the title registry gives the owner `name` and charges (paid). Use them together to go from an address to both the property's worth and its owner.

## Trust & verifiability
`trust: trusted` — the official provincial assessment authority, so value and property data are authoritative. Just remember its scope is property, not people: pair with the title registry to get ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bc-assessment |
| category | people-search |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
