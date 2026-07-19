---
id: property-value
name: Property Value (Australia)
description: Use when you have an Australian `address` and want its property profile — returns estimated value, sales/listing history and comparables (CoreLogic/Cotality data).
url: https://www.propertyvalue.com.au
category: search-engines
path:
- search-engines
bestFor: Pulling an Australian residential property's estimated value, sales history, and local comparables by address.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: freemium
costNote: Basic property view (estimated value, sales/listing history where available, comparables, suburb stats) is free with no account. Full Property Profile Reports cost ~A$43 each, or a Premium subscription (from ~A$10/week) for unlimited reports.
opsec: passive
opsecNote: You query a commercial property-data site about an address, not a person — passive, no notification to any subject. The free tier needs no login; avoid registering with a real identity if you go premium.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated on CoreLogic/Cotality (RP Data) — the dominant Australian property-data provider. Data is authoritative for AU property; estimated values are modelled figures, not sale prices.
missingPersonsRelevance: low
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- propertyvalue.com.au
- myrp
tags:
- toddington
- curated-directory
- specialty-search
- property
- australia
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Property Value (Australia)

> A CoreLogic/Cotality-powered site giving a free basic profile of any Australian residential property — estimated value, sales history, and local comparables — by address.

## When to use
You have an Australian `address` tied to a subject and want property context: an estimated market value, when it last sold and for how much (where available), listing history, and comparable/suburb data. Useful for corroborating a residence timeline, assessing circumstances, or confirming an address is a real residential property. It's address/property-centric — it does not name owners or occupants.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.propertyvalue.com.au and enter the target `address` or suburb.
2. Read the free basic profile: estimated value, sales/listing history (where available), property attributes, and comparable sold/for-sale properties nearby.
3. Use suburb statistics for market context around the address.
4. Only if you need the full record, buy a one-off Property Profile Report (~A$43) or a Premium subscription — otherwise stay on the free tier.
5. Pivot: a confirmed sale date supports a residence timeline; suburb/comparables inform where else to look. For owner names, use official land-titles services (state-based, usually paid).

## Inputs → Outputs
- **In:** Australian `address` / suburb
- **Out:** estimated value, sales/listing history, property attributes, comparables for that `address`
- **Empty/negative result looks like:** sparse data or "no history available" — common for properties that rarely sell or are newly built; estimated value may show without any sale history. Absence isn't proof about occupancy.

## Gotchas & OpSec
- Australia only; irrelevant elsewhere.
- Estimated values are algorithmic model outputs (AVMs), not actual sale prices — treat as approximate.
- No names: it profiles properties, not people; ownership requires a state land-titles search.
- Freemium: the deep report is paywalled — the free tier is enough for basic OSINT context.
- OpSec: passive address lookup.

## Overlaps ("do both")
- Complements state land-titles registries — Property Value gives free value/history context; the titles office gives the registered owner (paid).

## Trust & verifiability
`trust: community` — a commercial site on authoritative CoreLogic/Cotality data. Sales history is reliable where present; estimated values are modelled and should be treated as ballpark, not fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | property-value |
| category | search-engines |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
