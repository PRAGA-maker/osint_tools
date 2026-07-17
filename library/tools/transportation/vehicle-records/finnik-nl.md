---
id: finnik-nl
name: Finnik (NL)
description: Use when you have a Dutch `vehicle-plate` and want its full vehicle record — returns specs, APK (inspection) history, tax/insurance status, and ownership-count history.
url: https://finnik.nl/en
category: transportation
path:
- transportation
- vehicle-records
bestFor: Dutch (Netherlands) license-plate lookups — specs, inspection timeline, and ownership history.
selectorsIn:
- vehicle-plate
selectorsOut:
- vehicle-plate
- vin
status: live
pricing: freemium
costNote: Free tier shows a substantial vehicle summary (specs, APK dates, ownership count); full history/valuation reports and some fields require a paid Finnik report.
opsec: passive
opsecNote: Draws on the Dutch RDW open vehicle register; lookups are user-initiated and the plate owner is not notified. Finnik sees your IP/account; a full report requires registration/payment. No owner name is exposed (Dutch privacy law), so this profiles the vehicle, not the person.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built on the official RDW (Netherlands vehicle authority) open dataset; the underlying registration data is authoritative.
missingPersonsRelevance: medium
coverage:
- nl
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- rdw-open-data
- ovi-rdw
aliases:
- finnik.nl
tags:
- vehicle
- license-plate
- netherlands
- rdw
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Finnik (NL)

> A consumer-facing front-end to the Dutch RDW vehicle register: enter a Netherlands plate and get the car's specs, inspection (APK) timeline, tax status, and how many owners it has had.

## When to use
You have a Dutch `vehicle-plate` (kenteken) seen in a photo, a listing, or CCTV, and you want to characterize the vehicle: make/model/colour/year, when its APK inspection is due, whether it is currently taxed/insured, and its number of prior owners. Dutch privacy law hides the owner's name, so Finnik profiles the *vehicle* — but the specs, colour, and history let you confirm you're tracking the right car and estimate its status.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://finnik.nl/en and enter the Dutch plate (format like `12-ABC-3` / `AB-123-C`).
2. Read the free summary: make/model, first-registration date, colour, fuel/engine, APK expiry, current tax/insurance flags, and owner-count.
3. Cross-check the vehicle's `vin` and technical specs against your source photo/description to confirm identity.
4. For deeper history (mileage/APK detail, valuation), buy the full Finnik report — otherwise stop at the free summary.
5. Pivot: the make/model/colour + APK-due date help place the vehicle; the RDW data can be cross-referenced via `[[ovi-rdw]]` for the raw official record.

## Inputs → Outputs
- **In:** `vehicle-plate` (Dutch kenteken)
- **Out:** `vehicle-plate` confirmation, `vin`, specs, APK/inspection timeline, tax/insurance status, owner count
- **Empty/negative result looks like:** "unknown plate" / no record — not a valid current Dutch plate, or a plate not in the RDW register (e.g. export/scrapped). No owner name is ever shown; that is expected, not an error.

## Gotchas & OpSec
- No personal owner data is available (Dutch RDW withholds it); this is vehicle intelligence only — pair with other selectors to reach a person.
- Free vs paid: the summary is free, but detailed history and valuation are behind a paywall — budget accordingly.
- OpSec: **passive** — the register lookup does not alert the vehicle owner.

## Overlaps ("do both")
- Pairs with `[[ovi-rdw]]` / `[[rdw-open-data]]` (the official RDW interfaces) — Finnik is the friendlier front-end, but cross-checking against the raw RDW record confirms the data and catches fields Finnik summarizes away.

## Trust & verifiability
`trust: trusted` — the data originates from RDW, the Netherlands' official vehicle authority, so specs and registration facts are authoritative; only Finnik's added valuation estimates are third-party.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | finnik-nl |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → vehicle-plate, vin |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
