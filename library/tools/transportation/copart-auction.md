---
id: copart-auction
name: copart (auction)
description: Use when you have a `vin` (or Copart lot number) and want the salvage-auction record for that vehicle — returns image, geolocation.
url: https://www.copart.com
category: transportation
path:
- transportation
bestFor: Pulling a wrecked/salvage vehicle's auction listing — photos, damage, odometer, and yard location — from its VIN or lot number.
selectorsIn:
- vin
selectorsOut:
- image
- geolocation
status: live
pricing: freemium
costNote: Browsing and searching listings is free; full VIN, complete photo sets, and sale prices often require a free "Basic" membership, and bidding requires a paid registration/deposit.
opsec: passive
opsecNote: Searching listings is a passive query against a public auction catalog — the vehicle's former owner is not notified. Creating a Copart account exposes your identity to Copart; prefer the free third-party mirror sites for anonymous lookups, and use a sock-puppet if you register.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Copart is a large, legitimate publicly-traded salvage-auction operator; listing data is first-party and reliable, but it only covers vehicles routed through Copart auctions.
missingPersonsRelevance: medium
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Copart
- Copart salvage auction
tags:
- vehicle
- transportation
- salvage-auction
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
---

# copart (auction)

> Global online salvage/insurance vehicle auction: a VIN or lot number returns dated photos, damage, odometer, and the physical yard a wrecked vehicle passed through.

## When to use
You have a subject's `vin` (or a Copart lot number) and want evidence about the vehicle's fate and whereabouts. A hit is powerful in a missing-persons or accident context: it timestamps a vehicle as totaled/salvaged, geolocates it to a specific Copart yard, and provides photographs of its condition (crash damage, contents, plate sometimes visible). It corroborates or contradicts a "the car was written off" claim.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.copart.com and use the vehicle finder / search box; enter the `vin`, lot number, make/model, or year.
2. Open the lot: review the photo gallery, damage type (front/rear/flood/burn), primary/secondary damage, odometer, title type, sale date, and the **yard location** (city/state).
3. For full VIN, all photos, or sale price, sign in with a free Basic account (sock-puppet). For anonymous access, use a free Copart-mirror (e.g. stat.vin, bidfax, bid.cars) that indexes the same lots by VIN/lot without login.
4. Pivot: the yard `geolocation` places the vehicle geographically at a point in time; the sale date bounds the incident; a visible plate feeds plate-OSINT; the VIN feeds title-history tools.

## Inputs → Outputs
- **In:** `vin` (or Copart lot/stock number)
- **Out:** `image` (auction photo set), `geolocation` (Copart yard city/state), plus damage type, odometer, title type, and sale date
- **Empty/negative result looks like:** "no results" — the VIN never went through a Copart auction (it may still appear on IAAI or another auction house; check those separately). It does **not** return the owner's name or home address.

## Gotchas & OpSec
- Human-in-the-loop: full lot detail/photos/price are gated behind a free account (`account-login`); browsing basics is not.
- OpSec: **passive** — no owner notification. Registering ties your identity to Copart; the third-party mirrors avoid that entirely for read-only VIN lookups.
- Copart-only coverage. Always also check IAAI-style auctions before concluding a vehicle was never salvaged.
- Photos are point-in-time (the auction date), not live location.

## Overlaps ("do both")
- Do both with an IAAI/salvage-mirror lookup and a VIN title-history tool — Copart shows this-auction condition and location; title tools show the full ownership/branding timeline.

## Trust & verifiability
`trust: community` — first-party auction listings from a major legitimate operator (reliable within its catalog); the free mirror sites re-index the same data, so cross-check a lot against the official page when it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | copart-auction |
| category | transportation |
| selectorsIn → selectorsOut | vin → image, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
