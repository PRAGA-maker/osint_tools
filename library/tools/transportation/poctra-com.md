---
id: poctra-com
name: Poctra.com
description: Use when you have a `vin` or salvage-auction lot number and want a vehicle's past auction record — returns archived Copart/IAAI listing photos, damage, mileage, and bid history.
url: https://poctra.com/
category: transportation
path:
- transportation
bestFor: Retrieving archived salvage-auction photos and history (Copart/IAAI) for a VIN or lot number.
selectorsIn:
- vin
selectorsOut:
- image
- geolocation
status: live
pricing: freemium
costNote: Free to search and view archived auction listings, photos, and basic damage/mileage. Some full-history/report features may be gated or upsold, but the core photo archive lookup is free.
opsec: passive
opsecNote: You query an auction-history archive by VIN/lot; no owner is contacted or notified. Standard commercial-site logging applies; use a VPN for hygiene. The VIN alone carries no owner PII here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial aggregator of Copart/IAAI auction listings; photos and lot data are archived from those auctions and are broadly reliable, but it is a third-party mirror, not the auction house of record.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- free-vin-decoder-vindecoderz
- vin-decoder
aliases:
- Poctra
- poctra.com
tags:
- vehicle
- salvage-auction
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Poctra.com

> An archive of salvage-auction listings (Copart, IAAI and similar) — look up a VIN or lot number and see the vehicle's auction photos, damage, mileage, and sale history.

## When to use
You have a `vin` (or an auction lot number) and want to see whether the vehicle passed through a salvage/insurance auction and what it looked like there. Poctra's archived listings carry multiple photographs of the car, its odometer reading, damage description, sale date, and location — powerful for confirming a vehicle's identity and condition, spotting a written-off/rebuilt title, and extracting geolocation and detail clues from the auction photos (plates, backgrounds, VIN plates).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://poctra.com/ and search by `vin` or by auction lot number.
2. Open the matching archived listing.
3. Review the photo set (often 10+ images), damage description, primary/secondary damage, odometer, and the auction date and location.
4. Zoom the photos for corroborating detail — visible plate, VIN sticker, sale-lot signage, background/geography.
5. Pivot: the VIN → decode specs at [[free-vin-decoder-vindecoderz]] / [[vin-decoder]]; auction photos → reverse-image and geolocation analysis; sale date/location → timeline.

## Inputs → Outputs
- **In:** `vin` or auction lot number
- **Out:** archived auction listing — photos (`image`), damage, mileage, sale date and location (`geolocation`)
- **Empty/negative result looks like:** no listing found — the vehicle never went through a covered salvage auction, or the VIN/lot is mistyped. Try sibling archives (Bidfax, Stat.vin, AutoAstat) which mirror overlapping but not identical data.

## Gotchas & OpSec
- Coverage is limited to vehicles that appeared at salvage/insurance auctions (mostly US Copart/IAAI); a clean-title car that never went to auction won't be here.
- It is a third-party archive; listings can be incomplete or delayed. It returns vehicle data and photos, **not** owner identity.
- OpSec: **passive** — a VIN/lot lookup against an archive; no owner is contacted.

## Overlaps ("do both")
- Pairs with [[free-vin-decoder-vindecoderz]] and [[vin-decoder]] — decode the VIN to specs, then use Poctra for real-world photos and damage/sale history of that specific car.

## Trust & verifiability
`trust: community` — a commercial mirror of genuine Copart/IAAI auction listings; photos and lot data are authentic but second-hand, so cross-check against another auction archive when a detail is decisive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | poctra-com |
| category | transportation |
| selectorsIn → selectorsOut | vin → image, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
