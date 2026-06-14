---
id: quikr-india-classifieds
name: Quikr - India Classifieds
description: Use when an India-based subject may buy/sell locally — pivot from name/phone/city to classified listings, a seller profile, and a contact number.
url: https://www.quikr.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Placing an Indian subject in a city and surfacing a seller alias and contact phone via local classified listings.
input: Search keywords, category, Indian city
output: Classified listings with seller profile, contact phone (on reveal), and item details
selectorsIn: [name, phone, geolocation, image]
selectorsOut: [name, phone, geolocation, image, social-profile]
status: degraded
pricing: free
costNote: Free to browse and search; account/payment only for posting or premium ads.
opsec: passive
opsecNote: Browsing is passive; contacting a seller requires an account and may reveal your details. Use a sock-puppet account if you must make contact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Quikr was a major Indian classifieds site but has reportedly declined/restructured in recent years, so live coverage may be reduced — set status degraded and verify before relying on it.
missingPersonsRelevance: high
coverage: [in]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: [classifieds, marketplace, india]
source: arf-seed
lastVerified: ''
enrichment: full
---

# Quikr - India Classifieds

> India-focused local classifieds platform — historically a primary way to tie an Indian subject to a city and a contact phone, though its current activity level is reduced.

## When to use
You have a `name`, `phone`, or an Indian city (`geolocation`) for a subject and want their marketplace listings, seller alias, or a contact number. Useful for confirming presence in a region (cars, real estate, jobs, services) and harvesting listing photos.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.quikr.com/ and select the city; search by keyword/category, or try a known phone/alias.
2. Open a listing to view the seller profile, posting date, and the reveal-on-click phone number.
3. Note the area/locality and harvest any listing images.
4. Pivot: feed a `phone` to India phone-OSINT/truecaller-style lookups, a reused alias to username search, and listing `image`s to reverse-image search.

## Inputs → Outputs
- **In:** `name`/alias, `phone`, Indian `geolocation`, listing `image`
- **Out:** seller `name`/alias, `phone`, `geolocation` (city/locality), `image`, seller `social-profile` page
- **Empty/negative result looks like:** no listings, or sparse stale results — given the platform's decline, absence is weak evidence; cross-check OLX India and other classifieds.

## Gotchas & OpSec
- Human-in-the-loop: no captcha for browsing; contact/posting needs an account.
- OpSec: passive while reading; contacting leaks identity — use a sock puppet.
- Platform activity has reportedly dropped; treat coverage as partial and corroborate elsewhere.

## Overlaps ("do both")
- Pairs with OLX India and Indian phone-lookup tools, which often cover sellers Quikr now misses.

## Trust & verifiability
`trust: community` — real, long-known Indian platform whose current liveness is uncertain; status set to degraded pending verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | quikr-india-classifieds |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone, geolocation, image → name, phone, geolocation, image, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
