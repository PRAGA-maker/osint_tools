---
id: catawiki
name: Catawiki
description: Use when you have a `username` or `name` and want to trace a collectibles seller/bidder or a specific object's sale — returns `social-profile` seller pages and item provenance.
url: https://www.catawiki.com/
category: search-engines
path:
- search-engines
bestFor: Finding a collectibles auction seller's profile, their listed lots, and provenance of a specific object.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free to browse listings and view public seller profiles; only bidding/buying requires an account and payment.
opsec: passive
opsecNote: Browsing listings and public seller profiles is passive. Registering, bidding, or messaging a seller is active and attributable — do that only from a sock-puppet account, never with your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, legitimate European online auction house with expert-vetted lots; seller-supplied listing text and provenance claims are still self-reported and should be corroborated.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- catawiki.com
tags:
- auctions
- marketplace
- seller-search
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Catawiki

> A large curated online auction marketplace for collectibles (art, coins, watches, cars, cards, jewellery) — searchable seller profiles and object provenance make it a niche people/asset-tracing source.

## When to use
You are tracing a person through their collecting or selling activity, or trying to place a specific object. If a subject deals in collectibles, their Catawiki seller profile can reveal a public `username`, a location/country, feedback history, and the catalogue of lots they've sold — a picture of what they own, sell and specialise in. Conversely, if you have a distinctive item (a watch, coin, artwork, classic car), a past listing can surface who sold it and when, aiding provenance and asset-tracing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.catawiki.com/ and search by seller `username`/`name`, or by the object (make, model, distinctive keywords).
2. For a seller: open their public profile for location, join period, feedback and current/past lots.
3. For an object: read listings for photos, expert-appraisal notes, stated provenance and the seller behind it; Google-dork `site:catawiki.com "<term>"` to reach closed/archived lots search misses.
4. Pivot: a reused seller `username` feeds cross-platform enumeration; item photos feed reverse-image/EXIF checks; a location narrows a subject's geography.

## Inputs → Outputs
- **In:** `username` or `name` (seller), or an object description
- **Out:** `social-profile` (seller page), reused `username`, seller location/feedback, and item provenance/date
- **Empty/negative result looks like:** no seller profile and no matching lots — the person doesn't trade here, or their activity was as an anonymous bidder (bidders are not publicly listed).

## Gotchas & OpSec
- Bidders are private; only sellers have discoverable public profiles.
- Closed auctions may drop out of on-site search — use search-engine dorks and web-archive caches to recover old listings.
- Provenance and descriptions are seller-supplied (expert-vetted for authenticity, not for the seller's identity claims) — corroborate.
- Browsing is passive; bidding/messaging is active and attributable — use a sock puppet.

## Overlaps ("do both")
- Pairs with other marketplace/auction seller-search tools (eBay, specialist houses) and with reverse-image tools — cross-listing an item or handle across venues both confirms identity and widens the trail.

## Trust & verifiability
`trust: community` — a reputable auction platform with expert lot vetting; the platform and its listings are genuine, but seller-stated identity, location and provenance are self-reported and need corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | catawiki |
| category | search-engines |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
