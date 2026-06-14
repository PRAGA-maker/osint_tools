---
id: offerup
name: OfferUp
description: Use when a US subject buys/sells locally — pivot from a seller alias or item to a profile with photos, approximate location, ratings, and transaction history.
url: https://offerup.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Linking a US person to a local-marketplace seller profile, their listing photos, approximate area, and reputation history.
input: Item keywords, location, seller profile link
output: Seller listings with photos, pricing, profile ratings, join date, approximate location
selectorsIn: [name, username, geolocation, image]
selectorsOut: [name, username, image, geolocation, social-profile]
status: live
pricing: free
costNote: Free to browse, search, and view seller profiles; account only needed to message or transact.
opsec: passive
opsecNote: Browsing and viewing seller profiles is passive. Messaging a seller requires an account and exposes your identity — use a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: OfferUp is a large, real US local marketplace commonly cited in OSINT directories; entry reasoned from known function, not re-verified.
missingPersonsRelevance: high
coverage: [us]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: [letgo]
tags: [classifieds, marketplace, us, local]
source: arf-seed
lastVerified: ''
enrichment: full
---

# OfferUp

> Major US mobile-first local marketplace (absorbed letgo) — turns a seller alias or a distinctive item into a profile with photos, an approximate area, and a reputation trail.

## When to use
You have a `name`/`username` or know a subject sells specific items, and want a seller profile that shows photos, an approximate city/neighborhood (`geolocation`), join date, and reviews. Useful in missing-persons work to confirm someone is recently active in a region, to harvest face/background photos from listings, or to find a contact channel.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://offerup.com/ and set the location; search by item keyword or open a seller profile link if you have one.
2. On a listing, click the seller to view their profile: display name, photo, "member since", rating/reviews, and their other active listings.
3. Note the approximate location OfferUp shows (it generalizes to an area, not an exact address) and harvest listing photos.
4. Pivot: reverse-image search listing photos (faces, room interiors, vehicles in background), feed a reused alias to username search, or use review text to corroborate identity.

## Inputs → Outputs
- **In:** `name`/`username`, `geolocation` (city), seller profile link, `image`
- **Out:** seller `name`/`username`, profile `image`, approximate `geolocation`, `social-profile` (the seller page), ratings/history
- **Empty/negative result looks like:** no matching seller, or a profile with no active listings and no reviews — does not prove inactivity, listings expire.

## Gotchas & OpSec
- Human-in-the-loop: browsing needs no account; messaging does.
- OpSec: passive while reading. Contacting a seller leaks your identity — use a sock-puppet account.
- Location shown is deliberately approximate; do not treat it as a precise address.

## Overlaps ("do both")
- Pairs with reverse-image search and username-pivot tools; complements regional people-search to attach a real identity to the seller alias.

## Trust & verifiability
`trust: community` — well-known real platform; this entry reasons from its documented behavior rather than fresh verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | offerup |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username, geolocation, image → name, username, image, geolocation, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
