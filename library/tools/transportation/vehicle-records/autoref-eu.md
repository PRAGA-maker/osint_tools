---
id: autoref-eu
name: AutoRef (EU)
description: Use when you have a European `vehicle-plate` or `vin` and want the vehicle's identity and specification — returns make/model/engine and VIN-linked technical data.
url: https://www.autoref.eu/en
category: transportation
path:
- transportation
- vehicle-records
bestFor: Resolving a European license plate or VIN to the vehicle's make, model, engine and technical profile.
selectorsIn:
- vehicle-plate
- vin
selectorsOut:
- vin
- metadata-exif
status: live
pricing: freemium
costNote: Free tier with query quotas covers basic plate/VIN specification lookups; heavier use or fuller reports require an account/paid credits.
opsec: passive
opsecNote: Queries a vehicle-data service about a plate/VIN, not the owner directly — passive, no subject notification. A free account is needed for repeated use; register with a sock-puppet email to avoid attribution.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party EU vehicle-data aggregator; specification data is generally reliable but it is not an official government registry — corroborate critical facts.
missingPersonsRelevance: medium
coverage:
- eu
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- autoref.eu
tags:
- vehicle-records
- plate-lookup
- vin-lookup
- europe
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# AutoRef (EU)

> A European plate/VIN specification lookup — turn a license plate or VIN into the vehicle's make, model, engine and technical profile for identification and corroboration.

## When to use
You have a European `vehicle-plate` or a `vin` — from a photo, a listing, or a document — and want to identify the exact vehicle and its specification, or run a plate-to-VIN step. AutoRef aggregates EU vehicle data so you can confirm what a vehicle *is* (make, model, year, engine, technical details) to corroborate that a car matches a claim or a subject. It is a **vehicle-identification** source, not an owner registry — it won't name the keeper; national registries and lawful channels do that.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.autoref.eu/en and register a free account (needed for repeat queries within the quota).
2. Enter the European `vehicle-plate` or `vin`.
3. Read the returned specification: make, model, variant, year, engine, and technical/registration profile; note the VIN if you started from a plate.
4. Watch the free-tier quota — space out queries or use the account allowance.
5. Pivot: a resolved VIN → VIN-decoding and history-check services; make/model/year → valuation and the appropriate national registry (where lawful) for keeper data.

## Inputs → Outputs
- **In:** European `vehicle-plate` or `vin`
- **Out:** vehicle `make`/model/engine specification, the linked `vin` (from a plate), technical `metadata-exif`-style profile
- **Empty/negative result looks like:** no match or "not found" — the plate/VIN isn't in coverage (country not supported, mistyped, or non-EU), or the free quota is exhausted; verify the plate country and try again within limits.

## Gotchas & OpSec
- Coverage varies by EU country — some plates return full data, others little or none.
- Free-tier quotas throttle usage; plan queries.
- Returns vehicle identity/specs, **not owner identity** — keeper data requires official registries and a legal basis.
- Human-in-the-loop: account registration required; use a sock-puppet email.
- OpSec: passive toward the subject.

## Overlaps ("do both")
- Pairs with VIN-decoder and vehicle-history services (once AutoRef gives you the VIN) and with national vehicle registries — AutoRef identifies the vehicle, those add history and (lawfully) ownership.

## Trust & verifiability
`trust: unverified` — a third-party aggregator, not a government registry; specification data is usually accurate but should be corroborated against an official source for anything consequential.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | autoref-eu |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, vin → vin, metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
