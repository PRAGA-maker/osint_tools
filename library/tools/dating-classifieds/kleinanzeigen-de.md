---
id: kleinanzeigen-de
name: Kleinanzeigen.de
description: Use when a German-speaking subject may post on Germany's largest classifieds site — pivot from name/phone/location to seller listings and contact details.
url: https://www.kleinanzeigen.de/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding a German subject's local-marketplace activity, seller profile, and contact phone via classified listings.
input: Search keywords, category, German city/region
output: Classified listings with seller profiles, contact options, and listing history
selectorsIn: [name, phone, geolocation, image]
selectorsOut: [name, phone, geolocation, image, social-profile]
status: live
pricing: free
costNote: Free to browse and search; account only needed to message a seller or post.
opsec: passive
opsecNote: Browsing/search is passive. Sending a message requires an account and reveals your identity to the seller, so use a sock-puppet account if you must contact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Major, real German marketplace (the former eBay Kleinanzeigen, ~30M+ users); long-listed in OSINT directories. Tool itself unverified for this library but the platform is well established.
missingPersonsRelevance: high
coverage: [de]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: [eBay Kleinanzeigen]
tags: [classifieds, marketplace, germany]
source: arf-seed
lastVerified: ''
enrichment: full
---

# Kleinanzeigen.de

> Germany's dominant local classifieds platform (the rebranded former eBay Kleinanzeigen) — useful for placing a German subject in a city and surfacing a contact phone number.

## When to use
You have a `name`, `phone`, or a German city (`geolocation`) for a subject and want to find their marketplace listings, seller alias, or a contact number. Strong when the subject is known to buy/sell locally, deal in cars/electronics, or rent out rooms. Also useful to confirm a person is/was active in a specific German town.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.kleinanzeigen.de/ and use the search bar; set the location (PLZ/Ort) and radius.
2. Search by keyword, item, or a known seller alias. To find a person, try a phone number, a username they reuse, or distinctive item descriptions.
3. Open a listing to see the seller profile (display name, "active since" date, other live listings, sometimes a partial location). Reveal the phone where the seller exposed it.
4. Pivot: feed a revealed `phone` to phone-OSINT tools, a reused alias to username search, or listing `image`s to reverse-image search.

## Inputs → Outputs
- **In:** `name` / alias, `phone`, German `geolocation`, listing `image`
- **Out:** seller `name`/alias, `phone`, `geolocation` (town/PLZ), `image`, links to a `social-profile`-style seller page
- **Empty/negative result looks like:** no listings for the query, or a generic seller page with no contact and no other ads — does not prove the person is inactive, only that nothing is currently listed.

## Gotchas & OpSec
- Human-in-the-loop: no captcha for browsing; messaging needs an account.
- OpSec: passive while reading. Contacting a seller leaks your account identity — use a sock puppet, never your real account.
- Listings expire and rotate; absence today is not absence historically.

## Overlaps ("do both")
- Pairs with broader EU people-search and reverse-image tools to corroborate a seller's identity beyond the listing.

## Trust & verifiability
`trust: community` — the platform is real, large, and well known; this skill entry is reasoned from the site's known function and not independently re-verified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kleinanzeigen-de |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone, geolocation, image → name, phone, geolocation, image, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
