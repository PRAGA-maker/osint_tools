---
id: gumtree-classified-ads-australia
name: Gumtree Classified Ads (Australia)
description: Use when you have a `name`, `username` or `phone` and want Australian classified-ad activity — returns seller `social-profile`, item photos and rough `geolocation`.
url: http://www.gumtree.com.au
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding a person's buy/sell/rental listings and seller profile on Australia's dominant classifieds site.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free to search and view listings and seller profiles; posting/some features need a free account.
opsec: passive
opsecNote: Browsing listings is passive and doesn't alert the seller. If you MESSAGE a seller you become active and identifiable — use a sock-puppet account and never contact from a personal one during an investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Major, long-running Australian classifieds platform; listing content is user-generated, so treat details as unverified claims.
missingPersonsRelevance: medium
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Gumtree Australia
- gumtree.com.au
tags:
- toddington
- curated-directory
- classifieds
- australia
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Gumtree Classified Ads (Australia)

> Australia's dominant classifieds marketplace — search it to surface a subject's listings (items, cars, rentals, jobs, services), their seller profile, and the suburb/region they operate in.

## When to use
Your subject is likely active in Australia and may buy, sell, rent or advertise services online. Gumtree listings expose a seller `social-profile` (display name, member-since, other active ads), photos of items (which can carry background/location clues), a general `geolocation` (suburb/region), and sometimes a `phone` number in the ad text. This is a strong everyday-footprint source: ordinary people who avoid social media still post classifieds, and cross-referencing their other ads can reveal patterns, assets and locale.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.gumtree.com.au and search by keyword, and/or use a general web `site:gumtree.com.au` query for a `name`/`username`/`phone`.
2. Open a listing: note the seller's display name, member-since date, location (suburb/region) and item photos.
3. Click the seller to see their **other active ads** — the fuller pattern of what they sell and where.
4. Examine photos for identifying background detail (house, street, plates) for geolocation.
5. Pivot: reverse-image search listing photos; run any phone/username through dedicated lookups; treat the suburb as a location lead.

## Inputs → Outputs
- **In:** `name`, `username` or `phone` (via ad text / seller profile)
- **Out:** seller `social-profile`, other active listings, item photos, suburb-level `geolocation`, sometimes `phone`
- **Empty/negative result looks like:** no listings — the person doesn't use Gumtree, posts under a different handle, or ads have expired (listings age out). Absence is weak evidence.

## Gotchas & OpSec
- OpSec: **passive** to browse; **messaging a seller makes you active and identifiable** — always use a sock puppet.
- User-generated content: names, locations and details are self-reported and may be false.
- Listings expire, so a person's history is only partially visible; capture/archive interesting ads promptly.

## Overlaps ("do both")
- Pairs with other classifieds (Facebook Marketplace, Carsales) and reverse-image tools — different marketplaces catch different activity, and image search links a photo across them.

## Trust & verifiability
`trust: community` — a legitimate major platform, but listing content is user-supplied; verify names, numbers and locations through independent sources before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gumtree-classified-ads-australia |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
