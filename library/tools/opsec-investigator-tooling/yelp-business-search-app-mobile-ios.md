---
id: yelp-business-search-app-mobile-ios
name: Yelp Business Search App (Mobile – iOS)
description: Use when you have a business `name`, `address` or `geolocation` and want its listing and reviewer activity — returns address, phone, hours, photos and reviewer profiles.
url: https://apps.apple.com/us/app/yelp-food-services-around-me/id284910350
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Locating a business by name/area and mining its Yelp listing and reviews for contact details, photos, and the profiles of people who reviewed or work there.
selectorsIn:
- name
- address
- geolocation
selectorsOut:
- address
- phone
- social-profile
status: live
pricing: free
costNote: Free app and free web equivalent (yelp.com); no account needed to browse listings and reviews.
opsec: passive
opsecNote: Browsing listings and reviews is passive and does not notify anyone. If you log in and interact (follow, message, review), that is visible — browse logged-out for reconnaissance. The reverse also holds: a subject's own reviews leak their locations and timeline.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: trusted
trustNote: Official Yelp app; listing and review data are first-party. Reviews are user-generated, so individual claims are unverified, but the aggregate footprint is genuine.
missingPersonsRelevance: medium
coverage:
- us
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- google-maps
aliases:
- Yelp
- Yelp app
tags:
- toddington
- business-search
- reviews
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Yelp Business Search App (Mobile – iOS)

> Yelp used as an OSINT source: find a business by name or area, then mine its listing and reviews for contact details, interior/exterior photos, and the reviewer/owner profiles attached to it.

## When to use
Two use cases. **Business lookup:** you have a business `name`, `address` or a `geolocation`/area and want its contact info, hours, photos and public profile. **People pivot:** a subject leaves Yelp reviews — those reviews leak where they've been and when, and their reviewer profile (photo, city, review history) is a rich pattern-of-life source. Also useful to identify who reviews or is associated with a specific business.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Open the Yelp app (or yelp.com for the same data on desktop) — no login needed to browse.
2. Search the business `name`, or search a category near a `geolocation`/`address`.
3. Open the listing: read address, phone, hours, website, and scroll the user-contributed photos (often reveal interiors, staff, vehicles, signage).
4. Open the reviews; click through to individual reviewer profiles to see their other reviews (a map/timeline of places they frequent), photo and stated city.
5. Pivot: a reviewer's history geolocates their habits; business phone/address feed reverse-phone and mapping tools; photos feed reverse-image search.

## Inputs → Outputs
- **In:** business `name`, `address`, or `geolocation`
- **Out:** `address`, `phone`, hours/website, photos, and reviewer `social-profile`s (with their review history)
- **Empty/negative result looks like:** no listing (business unclaimed or closed), or a listing with no reviews/photos — try Google Maps, which often has a parallel profile.

## Gotchas & OpSec
- Reviews are user-generated — individual claims can be fake/planted; use the aggregate and the metadata (dates, locations), not any single review, as evidence.
- Reviewer "city" is self-set and review timestamps are approximate — treat as leads.
- Passive while browsing; only logged-in interactions are visible to others.
- Strongest coverage in the US; sparser elsewhere.

## Overlaps ("do both")
- Pairs with `[[google-maps]]` — the same business usually has a Google profile with different photos, reviews and reviewer accounts; cross-reference both for fuller coverage and to corroborate contact details.

## Trust & verifiability
`trust: trusted` — the official Yelp app, so listings and the review corpus are genuine first-party data. Individual reviews are unverified user content; verify contact details against the business's own site and a second maps source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yelp-business-search-app-mobile-ios |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name, address, geolocation → address, phone, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | no |
