---
id: idealista-com
name: idealista.com
description: Use when you have an `address` or area and want property listings tied to it in Spain, Italy, or Portugal — returns listing photos, features, price, and the listing agent/contact.
url: https://www.idealista.com/en/
category: public-records
path:
- public-records
bestFor: Researching property listings (photos, features, agent contact) by location in Spain, Italy, and Portugal.
selectorsIn:
- address
- name
selectorsOut:
- address
- image
- phone
status: live
pricing: freemium
costNote: Browsing and searching listings is free; contacting agents needs no payment, but some pro/market-data features and unthrottled use require an account/subscription.
opsec: passive
opsecNote: Searching listings and viewing photos is passive and non-attributable. Contacting an advertiser through the site reveals you to them — use a sock-puppet account and never approach a subject. Note listings show the property as advertised, not verified ownership.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The dominant Spanish (also IT/PT) property portal; listings are advertiser-supplied marketing, so they evidence a property being marketed, not who owns or lives there.
missingPersonsRelevance: high
coverage:
- es
- it
- pt
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Idealista
tags:
- propertysites
- Property Related Sites
- real-estate
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# idealista.com

> The leading property portal for Spain, Italy, and Portugal — use it to pull listing photos, features, prices, and agent contacts for an address or area, useful for property research and interior/exterior imagery.

## When to use
You have an `address` (or a neighborhood) in Spain/Italy/Portugal and want to see property listed there: current or past for-sale/rent listings, with photos of the interior and exterior, floorplans, features, price, and the advertising agent's contact. This helps corroborate a location, obtain imagery of a property (for verification or reverse-image work), estimate value, and identify the estate agent. Reach for it in southern-European locate/asset work — while remembering it shows what's *marketed*, not an ownership record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.idealista.com/en/ and set the country/area or search a specific location/`address`.
2. Filter (sale/rent, price, type) and open matching listings.
3. Read each listing: photos, floorplan, features, price, posting date, and the listing agent/agency contact (`phone`).
4. Cross-reference the imagery and address against your other evidence.
5. Pivot: agent contact → business/people search; property photos → reverse-image; a marketed price/area → asset context. For ownership, go to the official land registry (Registro de la Propiedad / Catastro).

## Inputs → Outputs
- **In:** `address` / area (also agency `name`)
- **Out:** `address` (listed property), `image` (property photos), `phone` (agent contact)
- **Empty/negative result looks like:** no listing at/near the address — the property isn't currently (or wasn't) marketed here. That says nothing about who owns or lives there; use the land registry/Catastro for ownership.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; contacting an agent needs an account and exposes you — sock puppet only, never approach a subject.
- **Listings ≠ ownership.** Idealista evidences marketing, not title or occupancy. Don't infer a person owns/lives at a property from a listing.
- OpSec: passive when searching.

## Overlaps ("do both")
- Pairs with the Spanish land registry / Catastro (ownership) and `[[infoempresa-com]]` (if a company owns it) — Idealista gives imagery and marketing context; those give authoritative ownership.

## Trust & verifiability
`trust: community` — a real, dominant portal, but advertiser-supplied listings; treat photos/details as marketing evidence and confirm ownership/occupancy via official registries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | idealista-com |
| category | public-records |
| selectorsIn → selectorsOut | address, name → address, image, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
