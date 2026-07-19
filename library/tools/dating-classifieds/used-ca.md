---
id: used-ca
name: Used.ca
description: Use when you have a `name`, `username`, `phone` or a BC/Canadian location and want a subject's classified ads — returns seller listings with contact details, photos and area.
url: https://www.used.ca
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding a Canadian (Vancouver Island / BC-heavy) subject's buy/sell/vehicle classified ads and the seller contact info they attach.
selectorsIn:
- name
- username
- phone
- address
selectorsOut:
- phone
- address
- image
- social-profile
status: live
pricing: free
costNote: Free to browse and search all listings; posting is free with optional paid promotion. No account needed to view ads.
opsec: passive
opsecNote: Browsing and searching ads is read-only and does not notify the seller. Replying to an ad (message/phone) would expose you — do that only from a sock puppet. Sellers often post a real phone number, first name and town.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running Canadian classifieds marketplace (strong on Vancouver Island; posting handled via an AdPerfect backend). Listings are user-posted and unverified, but seller-supplied contacts and locations are genuine leads.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Used.ca
- used.ca marketplace
tags:
- toddington
- curated-directory
- classifieds
- canada
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Used.ca

> A popular Canadian classifieds marketplace (rooted on Vancouver Island / BC) — searchable for a subject's ads and the phone number, town and photos they attach to them.

## When to use
You have a Canadian subject's `name`, a reused `username`, a `phone` number, or just a city/region, and want classified ads they have posted. Sellers routinely include a contact number, a first name or handle, a rough location and photos (of goods, vehicles, sometimes their home), so a matched ad can yield a `phone`, an `address`/area and images useful for confirming identity and recent whereabouts — a practical skip-trace lead in Canada, where Used.ca has strong regional penetration.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.used.ca and pick the local area (Victoria, Nanaimo, Saanich, etc.) or browse all cities.
2. Use the search box for the subject's name, handle, or a phone number, and browse relevant categories (motors, home, pets) in their region.
3. Open matching ads to read the seller name/handle, contact number, location and photos.
4. Reverse-image-search ad photos and cross-check the phone number in other tools before assuming a match.
5. Pivot: a seller `phone` feeds phone-OSINT/caller-ID tools; a reused `username` feeds handle sweeps; ad `image`s feed reverse-image/face search.

## Inputs → Outputs
- **In:** `name` / `username` / `phone` / `address` (city or region)
- **Out:** `phone`, `address` (advertised area), `image` (ad photos), `social-profile` (seller handle/ad page)
- **Empty/negative result looks like:** no ads match — the subject may not sell here, may use a different handle, or their listings may have expired. Absence is not disproof.

## Gotchas & OpSec
- Human-in-the-loop: none for searching/viewing; replying to a seller is optional and should only be done from a burner.
- OpSec: **passive** while browsing. Contacting the seller is **active** and self-exposing — avoid it unless part of an authorised, deliberate approach.
- Posting flows route through an AdPerfect-hosted backend; the listing content on Used.ca is the part that matters for OSINT. Listings expire and re-post, so search a number/handle broadly rather than trusting one ad.

## Overlaps ("do both")
- Pairs with phone-lookup and reverse-image tools, which independently verify the seller's number and photos surfaced here; and with other Canadian classifieds (e.g. Kijiji) for wider coverage.

## Trust & verifiability
`trust: community` — a genuine, established Canadian marketplace, but ads are self-posted and unverified; treat contact details as leads to confirm through an independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | used-ca |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username, phone, address → phone, address, image, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
