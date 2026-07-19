---
id: oodle-online-classifieds
name: Oodle (Online Classifieds)
description: Use when you have a `name`, seller handle, or item and want classified listings across many sites at once — returns aggregated ads for cars, housing, jobs, pets and goods.
url: https://www.oodle.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching aggregated classified listings (autos, housing, jobs, for-sale, pets) from many sources in one place.
selectorsIn:
- name
selectorsOut:
- social-profile
- address
- phone
status: live
pricing: free
costNote: Free to search and browse aggregated listings; no account required to search.
opsec: passive
opsecNote: Searching classified aggregations is passive. Contacting a seller/poster is an active step — do so from a sock-puppet identity, never your own, and never in a way that tips off the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A classifieds aggregator that pulls listings from third-party sites; freshness and dedup vary, and it holds no authoritative record itself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- oodle-classified-advertisements-united-states
tags:
- classifieds
- marketplace
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# Oodle (Online Classifieds)

> A classifieds aggregator that searches many marketplace and listing sites at once — useful for surfacing a subject's for-sale, housing, vehicle, or pet ads and the contact details attached to them.

## When to use
People reveal a lot in classified ads: a phone number, a rough location, a vehicle they're selling, a rental they're offering, an email or handle. When your subject may buy/sell/rent, use Oodle to search across many classifieds sources in one query rather than checking each site, and to catch listings that name them or reuse a known phone/handle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.oodle.com.
2. Search by the subject's `name`, a seller handle, a phone number, or a distinctive item, and set a location if known.
3. Browse aggregated results across categories (autos, real estate, jobs, for-sale, pets, community).
4. Open a listing for details: contact info, posting location, photos (which may carry `metadata-exif` or geolocatable backgrounds), and the source site.
5. Note recurring phone numbers/handles that tie multiple listings to the same person.
6. Pivot: a `phone`/handle → reverse lookups and username checks; listing photos → reverse-image/geolocation; posting location → area narrowing.

## Inputs → Outputs
- **In:** `name`, seller handle, phone, or item keyword (+ location)
- **Out:** aggregated classified listings with `social-profile`/handle, contact `phone`, posting `address`/area, and photos
- **Empty/negative result looks like:** no matching ads, or only stale/duplicate listings — aggregators lag and dedupe imperfectly, so also check the big source sites (Craigslist, Facebook Marketplace) directly.

## Gotchas & OpSec
- Aggregator, not a source of truth: listings can be old, duplicated, or already removed at the origin site; verify against the source.
- Coverage and freshness vary by region and category.
- OpSec: searching is passive, but any contact with a seller must go through a sock-puppet identity so you don't alert the subject.

## Overlaps ("do both")
- Pairs with `[[oodle-classified-advertisements-united-states]]` and direct searches of Craigslist/Marketplace — run the same selector through the aggregator and the major source sites, since each surfaces listings the others miss.

## Trust & verifiability
`trust: community` — an aggregator with no authoritative record of its own; treat every hit as a lead and confirm the listing and its contact details at the original source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oodle-online-classifieds |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name → social-profile, address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
