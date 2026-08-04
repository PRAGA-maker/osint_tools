---
id: madeit-australia
name: Madeit (Australia)
description: Use when you have a `name`/`username` of an Australian maker/seller and want their shop profile — returns seller identity, location hints and social/contact links.
url: http://www.madeit.com.au
category: documents-metadata
path:
- documents-metadata
bestFor: Finding an Australian handmade-goods seller's shop page and the maker name, location and contact details attached to it.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- address
- name
status: live
pricing: free
costNote: Free to browse and search seller shops; selling requires a paid account, but buyer-side browsing costs nothing.
opsec: passive
opsecNote: You browse public marketplace listings; the seller is not notified of a view. Avoid contacting or "purchasing" from a subject's shop, which would alert them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A verified-artisan Australian marketplace; shop details are self-published by sellers, so treat maker names and locations as claims to corroborate, not confirmed identity.
missingPersonsRelevance: low
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Madeit
- madeit.com.au
- Madeit Australia
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- marketplace
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# Madeit (Australia)

> Australia's curated handmade-goods marketplace — an Etsy-style site whose seller shops can tie a `name`/`username` to a maker, a rough location and social/contact links.

## When to use
Your subject is (or may be) an Australian crafter, artist or small maker who sells online. Madeit hosts ~850+ verified Australian artisan shops; a seller's storefront often exposes a maker/business name, a state or town, an "about the maker" bio, and links out to their own site or social profiles — all pivots for confirming identity or locating an Australian subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.madeit.com.au and search by shop name, maker name or `username`, or browse categories if you only have a product lead.
2. Open the seller's shop page and read the "about"/maker bio, listed location, and any outbound links (personal site, Instagram, etc.).
3. Note the shop name and maker name as `name` leads and any state/town as an `address` hint.
4. Pivot: take social links into profile searches and the maker/business name into ABN/business-registry and general people-search.

## Inputs → Outputs
- **In:** `name` / `username` (maker or shop) or a product lead
- **Out:** `social-profile` links, maker `name`, and location/`address` hints (usually state/town level)
- **Empty/negative result looks like:** no matching shop, or a shop with a business name but no personal identity/location — common, as sellers control how much they disclose.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; do not message or order from the subject's shop (that would alert them).
- OpSec: passive — viewing a public listing is not visible to the seller.
- Data quality: locations and maker names are self-reported for a storefront and may be a business persona, not a legal identity; corroborate before relying on them.

## Overlaps ("do both")
- Pairs with Australian business-registry (ABN) lookups and social-profile search because the shop gives a business/maker name and social handles that those tools turn into a verified identity.

## Trust & verifiability
`trust: community` — a legitimate curated marketplace, but shop details are seller-authored; treat name and location as leads to confirm against registry and social sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
