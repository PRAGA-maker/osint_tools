---
id: vindecodr
name: VinDecodr
description: Use when you have a 17-character `vin` and want the vehicle's specs — returns make, model, year, engine, body, and recall details.
url: https://vindecodr.com/
category: transportation
path:
- transportation
- vehicle-records
bestFor: Quickly decoding a VIN into make/model/year/engine and recall info.
selectorsIn:
- vin
selectorsOut: []
status: live
pricing: free
costNote: Free VIN decoder; built on public NHTSA vehicle data, no account needed.
opsec: passive
opsecNote: Decodes the VIN's embedded manufacturing data (and public recall records); it doesn't query registration/owner data and no one is notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party decoder front-end over public NHTSA data; spec output is standardized (VIN-encoded), so reliable for make/model/year.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nhtsa-vin-decoder
- vindecoderz
aliases:
- VinDecodr
- vindecodr.com
tags:
- vin
- vehicle-records
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# VinDecodr

> A free VIN decoder — turn a 17-character VIN into the vehicle's make, model, year, engine, and recall history.

## When to use
You have a `vin` (from a photo of a windshield/door jamb, a document, or a record) and want to know exactly what vehicle it is. The VIN encodes manufacturer, year, plant, and specs; VinDecodr parses that plus public recall data. Useful for confirming a subject's vehicle description, matching a VIN to a make/model in an image, or checking recalls. Note it decodes the *vehicle*, not the *owner* — it won't give registration or a name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://vindecodr.com/ and enter the full 17-character VIN.
2. Read the decoded specs: make, model, model year, body style, engine, manufacturing plant/country.
3. Check any listed recall information.
4. Cross-check with the official NHTSA decoder for authoritative confirmation.
5. Pivot: make/model/year → match against a vehicle seen in imagery; for owner/registration you need a licensed DMV/plate service, not a VIN decoder.

## Inputs → Outputs
- **In:** a 17-character `vin`
- **Out:** make, model, year, engine, body, plant, recall info (vehicle identity)
- **Empty/negative result looks like:** invalid/partial VIN error or sparse data — the VIN was mistyped (watch O/0, I/1, Q are not used in VINs), or it's a pre-1981 / non-standard VIN the decoder can't parse.

## Gotchas & OpSec
- Decodes the vehicle only — no owner, no registration, no location. For those you need a licensed records service and legal basis.
- Mostly US/NHTSA-oriented; foreign-market VINs may decode partially.
- VINs never contain the letters I, O, or Q — if you "see" one, it's a misread of 1, 0, or 0.

## Overlaps ("do both")
- Pairs with `[[nhtsa-vin-decoder]]` — the official government decoder; use VinDecodr for a quick read and NHTSA to confirm authoritatively.
- Pairs with `[[vindecoderz]]` as a second free decoder for cross-checking odd VINs.

## Trust & verifiability
`trust: community` — a third-party front-end, but VIN decoding is deterministic from the VIN itself and it draws on public NHTSA data, so make/model/year are reliable; verify against the official NHTSA decoder when it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vindecodr |
| category | transportation |
| selectorsIn → selectorsOut | vin → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
