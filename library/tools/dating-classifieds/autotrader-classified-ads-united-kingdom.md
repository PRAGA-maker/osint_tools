---
id: autotrader-classified-ads-united-kingdom
name: Auto Trader (United Kingdom)
description: Use when you have a UK `vehicle-plate` or a car for sale and want vehicle/seller detail — returns basic vehicle-check data and, from listings, seller location and contact.
url: http://www.autotrader.co.uk
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching the UK's largest used-vehicle marketplace and running a free basic reg-plate vehicle check.
selectorsIn:
- vehicle-plate
selectorsOut:
- address
- phone
status: live
pricing: freemium
costNote: Free to search listings and to run the basic vehicle check (make/model/year/MOT basics). Full history/valuation reports and selling adverts are paid.
opsec: passive
opsecNote: Browsing listings and the basic reg check are passive — you query Auto Trader, not the seller. Contacting a seller (phone/message form) is an active step that reveals your interest and, if you call, your number; use a research line and a pretext plan before making contact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Auto Trader is the UK's established, publicly listed vehicle marketplace; listing and basic vehicle-check data are reliable, though private-seller ad details are self-reported.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- autotrader.co.uk
- AutoTrader UK
tags:
- toddington
- curated-directory
- specialty-search
- vehicle
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Auto Trader (United Kingdom)

> The UK's largest used-vehicle marketplace, plus a free basic registration-plate check — useful for tying a subject to a car for sale, or decoding a UK plate to make/model/MOT basics.

## When to use
You have a UK `vehicle-plate`, or you know a subject is selling/buying a specific car, and you want vehicle detail or seller leads. Two modes: (1) enter a reg for the free basic vehicle check (make, model, year, colour, basic MOT status); (2) search listings by make/model/postcode to find a car for sale and its seller's town and contact route.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.autotrader.co.uk in a research browser.
2. **Vehicle check:** enter the `vehicle-plate` in the car-check/valuation tool → basic vehicle facts (paid for full history/valuation).
3. **Listings:** search by make/model + postcode/radius to find matching adverts; open a listing for the seller type (dealer vs private), location (town/postcode area), and contact method.
4. Note whether a seller is a dealer (business, traceable) or private (an individual near the subject).
5. Pivot: a dealer name → company records; a private seller's town + car → local records/social; a reg → a fuller vehicle-history service.

## Inputs → Outputs
- **In:** `vehicle-plate` (for the check) or make/model/location (for listings)
- **Out:** basic vehicle facts; from listings, seller location (`address` area) and a contact route (`phone`/message)
- **Empty/negative result looks like:** no matching listing (the car isn't currently advertised here) or a reg that returns no record (foreign/cherished/very new plate) — neither proves the vehicle doesn't exist; try history-specific services.

## Gotchas & OpSec
- Full vehicle-history reports and valuations are paid; only the basic check is free.
- Private-seller details are self-entered and can be pretextual; corroborate.
- Contacting a seller is active — plan your approach and use a research phone/identity, never a personal one.

## Overlaps ("do both")
- Complements dedicated UK vehicle-history/DVLA-based check tools — Auto Trader locates the advert and seller, those return the fuller registration/MOT/ownership history for the same plate.

## Trust & verifiability
`trust: trusted` — an established UK marketplace; listing and basic-check data are dependable, but treat private advert text as a claim and confirm vehicle facts via an official DVLA-based checker.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | autotrader-classified-ads-united-kingdom |
| category | dating-classifieds |
| selectorsIn → selectorsOut | vehicle-plate → address, phone |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
