---
id: vin-info
name: Vin-Info
description: Use when you have a `vin` and want a vehicle-history/decoder report — returns technical specs, damage/auction/mileage history and historical photos (with a `geolocation` trail), NOT the current owner's identity.
url: https://www.vin-info.com/en/
category: transportation
path:
- transportation
bestFor: Decoding a VIN and pulling a used-vehicle history report (damage, mileage, auction records, photos).
selectorsIn:
- vin
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Basic VIN decode (factory specs) is typically free; the full multi-source history report (damage, mileage, auction records, photos) is a paid per-report purchase.
opsec: passive
opsecNote: You query an aggregator's databases with a VIN; neither the seller nor any owner is notified. No login is needed for a basic decode. Only Vin-Info sees the VIN you submit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial third-party report aggregator combining many data sources; coverage and accuracy vary by region and vehicle, so treat records as leads, not proof.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- vin-info.com
- uk.vin-info.com
tags:
- vehicle
- vin-decode
source: metaosint
lastVerified: '2026-07-21'
enrichment: full
---

# Vin-Info

> A VIN decoder and used-vehicle history aggregator — feed it a 17-digit VIN and get specs, damage/mileage/auction history and archived photos. It does *not* return the owner's name or address.

## When to use
You have a `vin` (from a vehicle photo, a listing, insurance paperwork, or a windscreen) and want to understand the vehicle's past: make/model/trim decode, recorded damage and accidents, mileage readings over time, theft flags, prior auction listings, and historical photos. In a missing-persons or fraud context this corroborates a vehicle's identity and can place it at past auction/registration locations — but for owner identity you need a DVLA/state-registry or plate lookup, not this.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.vin-info.com/en/.
2. Enter the 17-character `vin` in the lookup box.
3. The free decode returns factory specifications (make, model, year, engine, build). To see the full history (damage, mileage, auction records, photos) you order a paid report.
4. Read the history for OSINT signals: archived photos may carry background/location clues, and auction/registration entries carry dates and `geolocation` hints for where the vehicle has been.
5. Pivot: the decoded make/model corroborates a vehicle description; auction locations feed a movement timeline; photos feed reverse-image and EXIF checks.

## Inputs → Outputs
- **In:** `vin`
- **Out:** vehicle specs, damage/mileage/auction history, archived photos, and an implied `geolocation` trail (auction/registration locations) — **no owner PII**
- **Empty/negative result looks like:** the free decode returns specs but the paid report shows "no history records found" — common for newer vehicles or regions the aggregator doesn't cover. Absence of history ≠ clean vehicle.

## Gotchas & OpSec
- **No owner data:** despite what some directories claim, this returns vehicle facts, not a name or address. Don't expect to identify a person from it.
- The genuinely useful history is behind a **paid per-report** wall; the free tier is just the decode.
- OpSec: **passive** — a VIN lookup notifies no one.

## Overlaps ("do both")
- Pairs with a national plate/registration lookup (for owner identity, which this lacks) and with reverse-image/EXIF tools for the archived photos this surfaces.

## Trust & verifiability
`trust: unverified` — a commercial aggregator of mixed third-party sources. History records are useful leads but coverage is patchy and unverified, so confirm anything critical against a primary registry or the physical vehicle.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vin-info |
| category | transportation |
| selectorsIn → selectorsOut | vin → geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
