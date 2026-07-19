---
id: caranalytics-co-uk
name: Caranalytics.co.uk
description: Use when you have a UK `vehicle-plate` and want the car's history and status — returns spec, MOT/tax and (paid) previous-keeper counts and plate-change history.
url: https://www.caranalytics.co.uk
category: transportation
path:
- transportation
bestFor: Checking a UK number plate's vehicle history — make/model, MOT and tax status, mileage, write-off/stolen/finance flags — with a free tier.
selectorsIn:
- vehicle-plate
selectorsOut:
- vehicle-plate
status: live
pricing: freemium
costNote: Free tier returns ~14 data points (spec, MOT history, tax, mileage, recalls, ULEZ). Deeper history — previous-keeper counts, plate-change history, write-off/finance/stolen checks — is paid (from ~£2.99).
opsec: passive
opsecNote: Queries aggregated DVLA/MOT/insurance datasets, not the keeper directly; the owner is not notified. UK keeper personal data (names/addresses) is GDPR-protected and is NOT returned by this or any consumer check.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial reseller of DVLA/MOT/insurance data; the free vehicle facts trace back to official sources, but this is a third-party aggregator, not the DVLA itself.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- caranalytics.co.uk
- Car Analytics UK
tags:
- vehicle
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# Caranalytics.co.uk

> A UK number-plate history check: free basic vehicle facts (spec, MOT, tax, mileage) with paid tiers for keeper counts, plate-change history and write-off/finance/stolen status — but never keeper names.

## When to use
You have a UK `vehicle-plate` and want to profile the **vehicle** (not its owner): confirm make/model/spec, MOT and tax status, recorded mileage, and — on the paid tier — how many previous keepers it has had and its number-plate change history. Useful for corroborating that a car in a photo/record matches a claimed vehicle, or to find an old plate a car previously wore.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.caranalytics.co.uk and enter the registration.
2. Read the free report: brand/model/body, DVLA registration details, MOT history, tax status, mileage, CO2/fuel, recalls, ULEZ, export status.
3. If you need history, buy a Basic/Full check for previous-keeper counts, **plate-change history**, and write-off/finance/stolen flags.
4. Pivot: a plate-change entry links an old mark to the current one — chase the old mark through photos, ANPR-adjacent records or forums; MOT mileage/date gaps can hint at periods of use.

## Inputs → Outputs
- **In:** `vehicle-plate` (UK registration)
- **Out:** vehicle spec + MOT/tax/mileage (free); previous-keeper counts and prior `vehicle-plate` marks (paid). No keeper name/address — that data is protected.
- **Empty/negative result looks like:** "vehicle not found" for an invalid/foreign plate, or a bare record for a very new registration with no MOT history yet.

## Gotchas & OpSec
- **No owner PII.** UK keeper names/addresses are not available to consumer checks; don't expect them here. The OSINT value is vehicle history and old plate marks.
- It's a reseller — the same underlying facts (MOT, tax) are free on the official gov.uk MOT/tax checkers; use those to verify.
- OpSec: passive; nothing reaches the keeper.

## Overlaps ("do both")
- Pairs with the official gov.uk "check MOT history" / "check vehicle tax" services (free, authoritative for those fields) and with European plate-identification references for non-UK marks.

## Trust & verifiability
`trust: unverified` — a commercial aggregator. The vehicle facts originate from DVLA/MOT and are reliable; cross-check the free fields against gov.uk, and treat paid-tier history as accurate-but-third-party.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | caranalytics-co-uk |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → vehicle-plate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
