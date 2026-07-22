---
id: tradingpost-australia
name: Trading Post (Australia)
description: Use when you have a `name`, `username` or `phone` and want to find an Australian seller's classified listings — returns `geolocation` (region), `phone` and item/asset detail.
url: https://www.tradingpost.com.au
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding an Australian person's for-sale classified ads and the region/contact behind them.
selectorsIn:
- name
- username
- phone
selectorsOut:
- geolocation
- phone
- social-profile
status: live
pricing: free
costNote: Free to browse and search listings; posting an ad may require a free account.
opsec: passive
opsecNote: Searching and reading listings is passive. Do not contact a seller from an attributable identity — enquiries are active. If you must contact, use a sock-puppet account/number.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running Australian classifieds brand (now online-only); listing content is seller-supplied and unverified.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
aliases:
- Trading Post
- tradingpost.com.au
tags:
- classifieds
- marketplace
- australia
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Trading Post (Australia)

> Australia's classic classifieds marketplace (cars, goods, services) — a way to tie a subject to for-sale listings, a region and sometimes a contact number.

## When to use
You have an Australian subject and want to see whether they buy/sell through classifieds. A matching listing can reveal the seller's region/suburb (`geolocation`), a contact `phone` or handle, photographs of goods/property, and asset ownership signals (a specific car, tools, equipment). Useful for placing a person geographically, confirming ownership of an item (e.g. a vehicle in a photo), or recovering a phone number tied to a name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tradingpost.com.au and search by keyword — the subject's `name`, seller `username`, a known `phone`, or a distinctive item.
2. Also Google-dork it: `site:tradingpost.com.au "<name or phone>"` to reach older/closed ads.
3. Read matching listings: seller name/handle, region, contact details, photos and item descriptions.
4. Pivot: a `phone` feeds reverse-phone lookups; listing photos feed reverse-image/EXIF; a vehicle for sale feeds plate/VIN checks; the region narrows location.

## Inputs → Outputs
- **In:** `name`, `username`, or `phone`
- **Out:** `geolocation` (seller region/suburb), `phone`, `social-profile`/handle, item photos and detail
- **Empty/negative result looks like:** no matching ads — the person doesn't advertise here, or their listings have expired and dropped from search (try archive/dorks).

## Gotchas & OpSec
- Listings are seller-supplied and transient; expired ads vanish from on-site search, so use dorks/web-archive for history.
- A seller handle/number may be a burner; corroborate before attributing.
- Browsing is passive; making an enquiry is active and attributable — sock puppet only.

## Overlaps ("do both")
- Pairs with Gumtree/Marketplace and reverse-phone tools — cross-referencing the same seller/number across classifieds confirms identity and widens the item/asset picture.

## Trust & verifiability
`trust: unverified` — a legitimate, established classifieds platform, but individual listings are unverified user content; treat seller-stated identity as a lead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tradingpost-australia |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username, phone → geolocation, phone, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
