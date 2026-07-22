---
id: autowini-vin-search-international
name: Autowini
description: Use when you want to check whether a specific used vehicle is listed for international export sale — returns marketplace listing details (NOT a VIN-to-owner lookup).
url: http://www.autowini.com
category: transportation
path:
- transportation
bestFor: Browsing Korea-based international used-vehicle export listings to see if a particular vehicle is on the market.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Browsing listings is free; selling requires paid membership tiers and buying involves transaction fees.
opsec: passive
opsecNote: Browsing public listings is passive. Do not register or contact a seller from an attributable account; use a sock puppet if you must inquire.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial used-car export marketplace — despite the harvested "VIN Search" label it offers NO VIN-to-owner lookup; it only lists vehicles for sale.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- autowini.com
tags:
- vehicle
- marketplace
source: metaosint
lastVerified: '2026-07-22'
enrichment: full
---

# Autowini

> A Korea-based international used-vehicle export marketplace — a place to see if a specific car/truck is listed for sale, **not** a VIN or license-plate owner-lookup despite how it was catalogued.

## When to use
You are chasing a specific vehicle (make/model, and ideally photos or a listing hint) and want to check whether it is being offered for export sale. Autowini specializes in Korean used cars, trucks, buses, and equipment shipped worldwide, so it is niche — useful mainly when a vehicle may have entered the Korean export market. It will **not** turn a `vin` or `vehicle-plate` into an owner `name`/`address`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.autowini.com and use the listing search (by make, model, type, year, price).
2. Browse matching listings; each shows vehicle photos, specs, seller/dealer, price, and export/shipping info.
3. Note any identifying details in the photos or description (plates, condition, mileage) to match against your subject vehicle.
4. Pivot: a matched listing gives a seller/dealer to research and a location; there is no lookup that returns the registered owner.

## Inputs → Outputs
- **In:** vehicle make/model/type search terms (no reliable `vin`/`plate` lookup)
- **Out:** marketplace listing details (photos, specs, seller, price, export info) — no owner PII
- **Empty/negative result looks like:** no listings match — expected for any vehicle not currently offered for export via this platform, which is the common case.

## Gotchas & OpSec
- **Name is misleading:** there is no functioning VIN-search / owner-lookup here; do not use it as one.
- Coverage is narrow (Korea-centric export inventory), so absence tells you almost nothing about a vehicle generally.
- Passive to browse; registering or messaging a seller is attributable — use a sock puppet.

## Overlaps ("do both")
- For actual VIN/plate intelligence, use a dedicated vehicle-records or VIN-decoder tool; this marketplace is only for spotting a vehicle that happens to be listed for sale.

## Trust & verifiability
`trust: unverified` — a commercial sales platform; listings are seller-supplied and unverified, and it provides no authoritative vehicle-registration data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | autowini-vin-search-international |
| category | transportation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
