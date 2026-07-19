---
id: auto-bid-master-auction
name: AutoBidMaster (auction)
description: Use when you have a `vin` and want a salvage/auction history and photos of a specific vehicle — returns listing photos, damage/condition, title status and a VIN history report.
url: http://www.autobidmaster.com
category: transportation
path:
- transportation
bestFor: Pulling salvage-auction listings and VIN history (photos, damage, title status) for a specific vehicle from US public salvage auctions (Copart broker).
selectorsIn:
- vin
selectorsOut:
- image
- physical-description
- document-id
status: live
pricing: freemium
costNote: Browsing/searching current and past salvage listings is free; a full ClearVin vehicle-history report costs from ~$14.99, and bidding requires a (paid-deposit) account. The free listing search alone is often enough for OSINT.
opsec: passive
opsecNote: Searching public auction listings is passive. Registering/bidding requires personal/payment details and identifies you — do not create an account just to look; use the free search. No target is notified by a listing search.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A real, established public-access salvage-auction broker (fronts Copart/IAAI inventory); listing data comes from the auctions, while paid VIN reports are supplied by the ClearVin third party.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- AutoBidMaster
- auto bid master
tags:
- vehicle
- salvage-auction
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# AutoBidMaster (auction)

> A public-access US salvage-auction broker where a `vin` yields listing photos, damage description, title/loss status and (paid) history — useful when a vehicle was wrecked, totalled, or exported.

## When to use
You have a `vin` (or make/model/year and location) for a vehicle tied to your case and want to know whether it passed through a salvage auction — i.e. was in a serious crash, declared a total loss, or is being exported/parted out. Auction listings carry dated photos, odometer, damage type, and title status, which can corroborate an accident, place a vehicle at a point in time, or confirm it's no longer roadworthy.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.autobidmaster.com and use the inventory search; enter the `vin` (or filter by make/model/year).
2. Open the matching listing: review photos, damage description, odometer, title status, and location/sale date.
3. For deeper history (previous owners count, total-loss record), run the ClearVin report — note this is a paid add-on (~$14.99).
4. Do NOT register or bid just to view — the free listing search is usually sufficient.
5. Pivot: photos → `physical-description`/condition evidence; sale location/date → timeline and `geolocation`; title/loss records → insurance and DMV-record follow-up.

## Inputs → Outputs
- **In:** `vin` (or make/model/year + location)
- **Out:** listing `image`s, `physical-description` (damage/condition), title/loss `document-id` status, sale location and date
- **Empty/negative result looks like:** no listing for the VIN — the vehicle simply hasn't gone through this broker's salvage inventory (most vehicles never do). It is not an owner-lookup and will not return a `name`/`address`.

## Gotchas & OpSec
- It is an **auction/vehicle** source, not a registration database — it does not return the owner's identity from a VIN.
- Full history reports are paid (ClearVin); the free tier is search + listing details only.
- OpSec: passive to search; never open an account/deposit merely to view a listing.

## Overlaps ("do both")
- Pairs with VIN decoders and title/insurance-record tools — this shows the auction footprint and photos, while decoders/title tools add specs and ownership-history context.

## Trust & verifiability
`trust: community` — an established, real auction broker; listing facts trace to the underlying auctions, and the paid ClearVin report is a recognised third-party history source. Treat photos/dates as reliable and cross-check any history-report claims.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | auto-bid-master-auction |
| category | transportation |
| selectorsIn → selectorsOut | vin → image, physical-description, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
