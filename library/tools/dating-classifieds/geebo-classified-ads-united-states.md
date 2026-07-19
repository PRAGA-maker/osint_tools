---
id: geebo-classified-ads-united-states
name: Geebo Classified Ads (United States)
description: Use when a subject may have posted a US classified ad (jobs, vehicles, services, rentals) and you want to find it — returns ads with contact hints, location and item detail.
url: http://geebo.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching a US city-based classifieds site for a subject's ads (items, services, jobs, rentals) and the contact/location hints they contain.
selectorsIn:
- name
- phone
selectorsOut:
- phone
- geolocation
- address
status: live
pricing: free
costNote: Free to browse and search ads and to post; no account required to read.
opsec: passive
opsecNote: Browsing ads is passive. Do not respond to an ad with your real identity — contacting a seller/poster is active and exposes you. Use a sock puppet if you must make contact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A legitimate, safety-focused US classifieds site; ad content is user-submitted and unverified, so treat any contact/location detail as a lead to corroborate.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Geebo
- geebo.com
tags:
- toddington
- curated-directory
- classifieds
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Geebo Classified Ads (United States)

> A US city-based classifieds site — a niche place to catch a subject's ads (selling items, offering services, seeking jobs/rentals) and the contact and location breadcrumbs those ads leak.

## When to use
Your subject may buy/sell or advertise online and you have a `name`, `phone`, or the item/service they're associated with. Classified ads often expose a phone number, a neighbourhood/city, an asking price, photos, and a description that ties to a person — useful for confirming a location, a phone, or an activity, especially when someone avoids mainstream social media but still posts local ads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://geebo.com and select the subject's likely city/region.
2. Browse the relevant category (jobs, merchandise, vehicles, services, real estate, rentals) or use a search engine `site:geebo.com "<name-or-phone>"`.
3. Open matching ads for contact details, location, photos, and item specifics.
4. Reverse-search any phone number and reverse-image any ad photos.
5. Pivot: a `phone` → phone-OSINT and other classifieds; ad photos → reverse-image and EXIF; stated location → mapping.

## Inputs → Outputs
- **In:** `name`, `phone`, or item/service tied to the subject
- **Out:** ads yielding `phone`, `geolocation`/`address` hints, photos, and item detail
- **Empty/negative result looks like:** no ads — the subject hasn't posted here (Geebo is smaller than Craigslist). Absence is expected; also check larger classifieds and marketplaces.

## Gotchas & OpSec
- Smaller reach than major classifieds — a miss here means little; check Craigslist/Facebook Marketplace/OfferUp too.
- Ad data is unverified and can be stale or fake; corroborate contact/location.
- OpSec: browse only; contacting a poster exposes you — use a sock puppet.

## Overlaps ("do both")
- Pairs with larger classifieds/marketplace searches and phone/reverse-image tools — cross-reference multiple ad platforms, then pivot on the phone numbers and photos the ads expose.

## Trust & verifiability
`trust: unverified` — a legitimate site but with user-submitted, unverified ads; use finds as leads and confirm any phone/location through independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geebo-classified-ads-united-states |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone → phone, geolocation, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
