---
id: ebay
name: eBay
description: Use when you have a `username` and want to research a subject's selling/buying history, feedback, and location hints on the world's largest auction marketplace.
url: https://www.ebay.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Researching a seller/buyer by username — feedback history, listings, and location hints
selectorsIn:
- username
- name
- geolocation
selectorsOut:
- username
- geolocation
- associate
- image
status: live
pricing: free
costNote: Free to browse, search, and view public seller profiles/feedback; account only needed to bid/buy/sell.
opsec: passive
opsecNote: Viewing public profiles, listings, and feedback is passive. Bidding/messaging requires an account and exposes you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: eBay is a major, established marketplace; individual listings/feedback are user-supplied.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags:
- marketplace
- auction
- arf-seed
source: arf-seed
lastVerified: ''
enrichment: full
---

# eBay

> The world's largest auction marketplace — a public seller/buyer profile, feedback log, and listing history that can tie a `username` to interests, location, and timing.

## When to use
Use it when you have a reused `username` and want to profile a subject's selling/buying behavior. A public seller profile exposes feedback history (an activity timeline), item categories (interests), shipping location hints (`geolocation`), and listing photos (`image`, sometimes with recoverable backgrounds). Most useful as a behavioral/interest pivot, not as a primary locator — hence lower MP relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ebay.com/, search the username, or open a profile at `ebay.com/usr/<username>`.
2. Review feedback received/left for dates, frequency, and item types; open the seller's other listings.
3. Note item location, shipping-from region, and listing photos for environment clues.
4. Pivot: the reused `username` feeds cross-platform enumeration; listing photos feed reverse-image search.

## Inputs → Outputs
- **In:** `username`, `name`, `geolocation`
- **Out:** reused `username`, approximate `geolocation`, `associate`/interest signals, listing `image`
- **Empty/negative result looks like:** a private/empty profile or no feedback — many casual users leave almost no public footprint.

## Gotchas & OpSec
- Human-in-the-loop: none for viewing public profiles/feedback.
- OpSec: passive while browsing; bidding/messaging exposes an account, so don't. An API exists (developer key) for structured queries if scaling up.

## Overlaps ("do both")
- Pairs with `[[goofbid]]` (misspelling/typo search of eBay) and username-enumeration tools.

## Trust & verifiability
`trust: trusted` — eBay is an established platform; the accuracy of a given listing or feedback entry is user-supplied and should be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ebay |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name, geolocation → username, geolocation, associate, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
