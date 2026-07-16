---
id: regrid-us-only
name: Regrid (US Only)
description: Use when you have a US `address` or parcel number and want the property's parcel boundary, owner and assessment data — returns owner `name`, mailing `address` and parcel details.
url: https://regrid.com
category: public-records
path:
- public-records
- property-records
bestFor: Looking up a US property's parcel map, recorded owner and assessment data from a nationwide parcel dataset.
selectorsIn:
- address
selectorsOut:
- name
- address
status: live
pricing: freemium
costNote: Free map lets you view parcels and basic info; full owner/assessment fields and bulk/API access require a paid plan. US-only coverage.
opsec: passive
opsecNote: You query a property, not a person by name; the lookup alerts no one and reveals nothing about you to the owner. Passive.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates official county parcel/assessor data into one nationwide layer; source data is authoritative but Regrid's coverage/freshness varies by county.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Regrid
- regrid.com
- Loveland Technologies
tags:
- property-records
- parcel
- real-estate
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# Regrid (US Only)

> A nationwide US parcel map — draw or search a location and get the property boundary, its recorded owner, and assessment data pulled from county records.

## When to use
You have a US `address` (or a parcel/APN, or map coordinates) and want to know who owns that property and its parcel details: recorded owner `name`, the owner's mailing `address` (often different from the property, a strong lead), lot boundary, assessed value and land use. Useful for tying a subject to a residence, or finding where a property owner actually lives.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://regrid.com and open the parcel map.
2. Search by address, parcel number, or navigate the map to the location.
3. Click the parcel to open its record.
4. Read the output: parcel boundary, recorded owner (`name`), owner mailing `address`, assessed value and land-use fields — with the fuller owner/assessment detail gated behind a paid plan in some counties.
5. Pivot: run the owner name through people-search; compare the property vs mailing address; check neighboring parcels for related owners.

## Inputs → Outputs
- **In:** `address` (or parcel number / coordinates)
- **Out:** `name` (recorded owner), `address` (owner mailing address + parcel location), assessment data
- **Empty/negative result looks like:** a parcel with no owner data shown (county not fully covered, or behind the paywall), or no parcel at the searched point.

## Gotchas & OpSec
- **US only**, and the free tier is limited — the map and basic parcel info are free, but complete owner/assessment fields and bulk/API access are paid (partial paywall).
- Data is only as current as each county's feed; recent sales or LLC-held properties may obscure the true individual.
- OpSec: passive; you look up property, not a named person.

## Overlaps ("do both")
- Complements county assessor/recorder sites and people-search: Regrid unifies parcels nationwide for quick lookup, while the county site is the authoritative source and people-search resolves the owner to a person.

## Trust & verifiability
`trust: community` — an aggregator of official county parcel/assessor data. The underlying records are authoritative; verify a specific parcel against the source county when it matters, since coverage and freshness vary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | regrid-us-only |
| category | public-records |
| selectorsIn → selectorsOut | address → name, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
