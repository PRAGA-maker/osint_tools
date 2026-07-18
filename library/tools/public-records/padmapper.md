---
id: padmapper
name: PadMapper
description: Use when you have an `address` or area and want the rental market around it — returns mapped rental listings (price, unit details, location), not personal records.
url: https://www.padmapper.com
category: public-records
path:
- public-records
bestFor: Mapping rental/apartment listings across the US and Canada by location to build property/area context.
selectorsIn:
- address
- geolocation
selectorsOut:
- address
status: live
pricing: free
costNote: Free to search and view rental listings; powered by Zumper. No account needed to browse.
opsec: passive
opsecNote: Passive — you browse an aggregated public listings map; no query is tied to a subject and nothing is sent to anyone. Creating an account or contacting a listing would be an active step done separately.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A rental-listing aggregator powered by Zumper; listings come from many third-party feeds, so accuracy and freshness vary by market and it is not an authoritative property register.
missingPersonsRelevance: low
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- padmapper.com
- Zumper
tags:
- property
- rentals
- real-estate
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# PadMapper

> A map-first rental-listings aggregator (US + Canada, powered by Zumper) — useful for area/property context, not for identifying people.

## When to use
You have an `address` or a target neighborhood and want to understand the rental market there: what units are or were listed, at what price, with what features. Handy for building context around a location in a case — e.g. confirming a building is rental housing, seeing typical unit types, or spotting that a specific address currently has a listing. It returns *property* information, not tenant or owner identities, so treat it as environmental context rather than a person-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.padmapper.com.
2. Search a city/neighborhood/address, or click "Use your current location," to load the listings map.
3. Read pins for price, bed/bath, and unit details; click a listing for photos, description, and the mapped location.
4. Filter by price, size, or property type to narrow the picture.
5. Pivot: a specific listed address feeds a property-records / county-assessor lookup (which *does* carry owner names), or corroborates that an address a subject gave is a real rental unit.

## Inputs → Outputs
- **In:** an `address` or `geolocation` (city/neighborhood/point)
- **Out:** mapped rental listings — `address`, price, unit details, coordinates
- **Empty/negative result looks like:** no pins in an area means no active listings are aggregated there (or coverage is thin), not that no rentals exist; it will never surface a person's name.

## Gotchas & OpSec
- **No people data:** listings describe units, not tenants or owners — pair with a property register to get names.
- Aggregated from third-party feeds via Zumper; listings can be stale, duplicated, or removed, and coverage is uneven outside major metros.
- Reflects *current/recent* market listings, not a historical occupancy record.

## Overlaps ("do both")
- Pairs with county property-records / assessor tools — PadMapper shows the rental unit and its location, and the register ties that address to an owner name.

## Trust & verifiability
`trust: community` — a commercial listings aggregator (Zumper); the data is real market inventory but feed-sourced and variable in freshness, so verify a specific listing against the property record before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | padmapper |
| category | public-records |
| selectorsIn → selectorsOut | address, geolocation → address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
