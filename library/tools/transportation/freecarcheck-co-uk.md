---
id: freecarcheck-co-uk
name: Freecarcheck.co.uk
description: Use when you have a UK `vehicle-plate` and want free vehicle history — returns make/model, MOT & tax status, DVLA history, stolen/plate-change flags.
url: https://www.freecarcheck.co.uk
category: transportation
path:
- transportation
bestFor: Free UK number-plate lookup — MOT/tax status, DVLA history, colour changes, stolen and cloned-plate checks.
selectorsIn:
- vehicle-plate
selectorsOut:
- vehicle-plate
status: live
pricing: freemium
costNote: Core checks (MOT, tax, DVLA history, stolen/plate-change) are free by registration; a full 50+ point report is £9.95.
opsec: passive
opsecNote: Queries official UK vehicle datasets (DVLA/MOT/PND) by plate — the vehicle keeper is not contacted and the lookup isn't tied to the owner. It returns vehicle, not personal, data; nothing identifies the subject to them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregates authoritative UK sources (DVLA, MOT/DVSA, Police National Database, MIB, SMMT); the vehicle data is official, though it does NOT expose the keeper's identity.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Free Car Check
- freecarcheck
tags:
- vehicle
- dvla
- mot
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# Freecarcheck.co.uk

> A free UK number-plate lookup: enter a registration and get the vehicle's DVLA/MOT history, tax status, and stolen/cloned-plate flags — vehicle intelligence, not the owner's name.

## When to use
You have a UK registration mark (`vehicle-plate`) — from footage, a sighting, a document — and want to establish the vehicle behind it: make/model/colour, year, current MOT and tax (VED) status, MOT pass/fail history, recorded colour changes, whether it's flagged stolen, and whether the plate has been changed/cloned. Strong for corroborating a vehicle in a missing-person or incident timeline. Note it returns **vehicle** data, not the registered keeper's identity (DVLA doesn't publish that freely).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.freecarcheck.co.uk.
2. Enter the UK registration (VRM) and click "Check Vehicle".
3. Read the free output: make/model/colour, year, MOT history (passes & failures, mileage at test), tax status, import/export, stolen (PND) flag, plate-change/clone check.
4. For deeper data (finance, write-off, full valuation) a £9.95 premium report is offered — the free tier already covers most OSINT needs.
5. Pivot: MOT mileage over time builds a usage timeline; a colour/plate change or stolen flag is a lead; cross-reference the vehicle in ANPR/insurance context.

## Inputs → Outputs
- **In:** UK `vehicle-plate` (VRM)
- **Out:** vehicle make/model/colour/year, MOT & tax status/history, stolen & plate-change flags
- **Empty/negative result looks like:** "vehicle not found" — the plate is invalid, foreign (foreign plates aren't supported), or newly issued/withdrawn; it does NOT mean the vehicle never existed.

## Gotchas & OpSec
- **No keeper identity:** UK vehicle checks reveal the car, not the owner's `name`/`address` — don't expect personal details from the plate alone.
- UK-only; foreign plates aren't supported.
- The £9.95 upsell is optional; the free checks are the useful OSINT layer.
- OpSec: passive — official-data lookup, nothing signalled to the keeper.

## Overlaps ("do both")
- Pairs with the DVLA's own free MOT-history service and other free reg-checkers (carcheck.co.uk, checkcardetails.co.uk) — cross-check because aggregators occasionally differ on flags; combine with ANPR/insurance sources for movement.

## Trust & verifiability
`trust: trusted` — it surfaces official UK vehicle data (DVLA, DVSA/MOT, PND). The data is authoritative for the vehicle; the limitation is scope (no owner PII), not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | freecarcheck-co-uk |
