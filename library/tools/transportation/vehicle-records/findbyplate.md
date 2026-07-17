---
id: findbyplate
name: FindByPlate
description: Use when you have a US `vehicle-plate` + state and want to decode the vehicle and probe for ownership hints — returns vin and vehicle specs (owner data is paywalled).
url: https://findbyplate.com/
category: transportation
path:
- transportation
- vehicle-records
bestFor: Decoding a US license plate to make/model/year/VIN and surfacing whatever limited ownership hints are offered before a paywall.
selectorsIn:
- vehicle-plate
selectorsOut:
- vin
status: live
pricing: freemium
costNote: Basic plate-to-vehicle decode is free; owner/ownership-history details are teased and gated behind a paid report.
opsec: passive
opsecNote: A standard web lookup against a plate; the vehicle owner is not directly notified. The site is a commercial data broker — use a research browser and do not pay/enter personal details to unlock reports.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial plate-lookup aggregator with bot protection; the free decode is generally reliable, but "ownership" claims are marketing teasers behind a paywall — do not treat them as confirmed.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- findbyplate.com
tags:
- vehicle
- license-plate
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# FindByPlate

> A US license-plate lookup that decodes a plate to the vehicle (and VIN) for free, then upsells gated "ownership" reports.

## When to use
You have a US `vehicle-plate` and state and want to identify the vehicle — make, model, year, and often a decoded `vin` — and see what ownership hints, if any, are surfaced. Use the free decode; treat any owner/history claims as paywalled teasers to be confirmed elsewhere. Relevant when a plate is your only lead on a vehicle tied to a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://findbyplate.com/ (the site uses bot protection; a browser session works best).
2. Enter the plate number and select the state.
3. Read the free result: vehicle make/model/year and, where decoded, the `vin`.
4. Note that fuller "owner"/history data prompts a paid report — stop at the free tier and pivot instead of paying.
5. Pivot: take a recovered `vin` into free VIN decoders (NHTSA vPIC) and title/history/theft checks (NICB VINCheck) for authoritative vehicle data.

## Inputs → Outputs
- **In:** US `vehicle-plate` + state
- **Out:** vehicle make/model/year, decoded `vin`; ownership hints are teased behind a paywall
- **Empty/negative result looks like:** no decode for the plate/state, or a page that only offers a paid report with no free vehicle data — meaning the plate isn't in the free index.

## Gotchas & OpSec
- Owner/ownership data is a **payment-wall teaser**, not a verified result; don't pay and don't trust unconfirmed owner claims.
- Bot protection may throw a challenge; solve it in-browser.
- US-only; accuracy of the free decode varies by state.

## Overlaps ("do both")
- Pairs with NHTSA vPIC (free authoritative VIN decode) and NICB VINCheck — FindByPlate gets you from plate to VIN, those give you the trustworthy vehicle facts for free.

## Trust & verifiability
`trust: unverified` — a commercial aggregator whose paid "ownership" data is unverifiable from outside; use only the free plate→vehicle/VIN step and confirm everything downstream on official sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findbyplate |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → vin |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
