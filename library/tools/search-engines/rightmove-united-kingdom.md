---
id: rightmove-united-kingdom
name: Rightmove (United Kingdom)
description: Use when you have a UK `address` or area and want property listings, sold-price history and interior photos — returns geolocation, physical-description and price/timeline leads.
url: https://www.rightmove.co.uk/
category: search-engines
path:
- search-engines
bestFor: Researching a UK property's listings, sold-price history, and photos from an address or postcode.
selectorsIn:
- address
selectorsOut:
- geolocation
- physical-description
status: live
pricing: free
costNote: Free to browse listings and sold-price data; no account needed. Contacting agents is free but requires submitting your details.
opsec: passive
opsecNote: Browsing listings and sold prices does not alert any owner. Do NOT use the "contact agent"/"request viewing" forms for a target property — that sends your enquiry to an estate agent and exposes your interest. Use a clean browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The UK's largest property portal; current listings come from estate agents and sold-price data derives from HM Land Registry, so it is reliable though listing photos may be dated.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Rightmove
- rightmove.co.uk
tags:
- toddington
- curated-directory
- specialty-search
- real-estate
- uk
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Rightmove (United Kingdom)

> The UK's largest property portal, usable as property intel: an address or postcode gives you current/past listings, sold-price history, and often interior and exterior photos of a home.

## When to use
You have a UK `address` (or postcode/area) for a subject and want to understand the property and its timeline. Rightmove's sold-price history shows when a home last changed hands and for how much (a move-in/out signal), while current or archived listings frequently include floor plans and interior photos that leak a `physical-description` of the property and visible belongings, vehicles, or documents.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.rightmove.co.uk/.
2. For current listings, search the postcode/area; for history, use "House Prices" and enter the street/postcode to see sold prices.
3. Open the property to view price/sold history, floor plan, and photo gallery.
4. Cross-reference sold dates with when your subject was known to be at the address.
5. Pivot: sold-price dates → occupancy timeline; photos → `physical-description` and scene clues; map view → `geolocation`. For owner identity, use HM Land Registry title records (Rightmove does not name owners).

## Inputs → Outputs
- **In:** UK `address` / postcode / area
- **Out:** `geolocation` (map), `physical-description` of the property (photos, floor plan, beds/baths), and sold-price/timeline data.
- **Empty/negative result looks like:** no current listing and no sold-price entry — the property hasn't been marketed/sold recently on the portal; try Zoopla or Land Registry directly.

## Gotchas & OpSec
- Rightmove does not reveal owner names — use HM Land Registry for ownership.
- Listing photos are from the last time the property was marketed and may be years old or show a prior occupier.
- Never trigger agent-contact/viewing-request forms for a target property; that leaks your interest.
- UK-only.

## Overlaps ("do both")
- Pairs with Zoopla and HM Land Registry — Rightmove and Zoopla give listing/photo/price coverage that differs property-to-property, and Land Registry adds authoritative ownership; compare like `[[zillow]]` for the US.

## Trust & verifiability
`trust: trusted` — the dominant UK portal; listings come from agents and sold prices from HM Land Registry, so core facts are reliable, with the usual caveat that photos and Zestimate-style figures can lag reality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rightmove-united-kingdom |
| category | search-engines |
| selectorsIn → selectorsOut | address → geolocation, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
