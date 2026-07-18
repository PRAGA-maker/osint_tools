---
id: yelp
name: Yelp
description: Use when you have a business `name`/location or a reviewer `username` and want details or activity — returns business `address`/`phone` and reviewer `social-profile`s that hint at the places a person frequents.
url: https://www.yelp.com
category: search-engines
path:
- search-engines
bestFor: Looking up a business's address/phone/hours, or profiling a Yelp reviewer's location and the venues they visit.
selectorsIn:
- name
- username
- geolocation
selectorsOut:
- address
- phone
- social-profile
status: live
pricing: free
costNote: Free to browse businesses and reviewer profiles; a free account is only needed to post reviews.
opsec: passive
opsecNote: Browsing business pages and public reviewer profiles is passive and unseen by the target. Reviewer profiles are public and often reveal a first name + last initial, a home city, and a trail of visited venues — read, don't interact. Posting or messaging would need a (sock-puppet) account and is active.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Yelp is a large, legitimate reviews platform, but content is user-generated — business details are usually accurate, while reviews and reviewer bios are self-supplied and can be fake or pseudonymous.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- yelp-find-friends
aliases:
- yelp.com
tags:
- toddington
- curated-directory
- specialty-search
- reviews
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Yelp

> A giant crowdsourced directory of businesses and reviews — useful both for business contact/location details and for profiling the people who write the reviews.

## When to use
Two distinct uses. **Business lookup:** you have a business `name` (a subject's employer or a venue) and want its `address`, `phone`, hours, and photos. **Reviewer profiling:** you have a Yelp reviewer `username` (or find your subject reviews on Yelp) and want to map their activity — their public profile shows a first name + last initial, a stated home city, and a chronological trail of **venues they've visited** (restaurants, gyms, clinics, neighbourhoods), which sketches where they live, work and spend time. Review photos can carry location clues too.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.yelp.com/.
2. **Business:** search the `name` + city; read the address, phone, hours, and photos.
3. **Person:** open the reviewer's profile (from a review byline or by searching the handle). Read their location field, the list of businesses reviewed (with dates), uploaded photos, and friends/compliments.
4. Note geographic clustering — a run of reviews in one town/neighbourhood is a strong locality signal.
5. Pivot: business address/phone feed further records work; reviewer location + handle feed geolocation and cross-platform username searches; review photos feed image analysis.

## Inputs → Outputs
- **In:** business `name`/`geolocation`, or reviewer `username`
- **Out:** business `address`, `phone`, hours; reviewer `social-profile` (name+initial, city, venue history, photos)
- **Empty/negative result looks like:** no business match, or a thin/private reviewer profile with few reviews — many users lurk without reviewing, so absence proves little. Common business names need a city to disambiguate.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing.
- OpSec: **passive** while reading; posting/messaging needs a sock-puppet account and is active.
- Reviewer identities are self-supplied and often pseudonymous; a stated city or name+initial is a lead, not proof. Reviews can be fabricated or paid.
- Coverage is strongest in the US and major cities; sparse elsewhere.

## Overlaps ("do both")
- Pairs with `[[yelp-find-friends]]` for the social/friend graph, and with mapping/streetview tools to place the venues a reviewer frequents. Cross-check a handle on other review platforms (Google Maps, TripAdvisor) for a fuller pattern-of-life.

## Trust & verifiability
`trust: community` — a legitimate platform with reliable business data but user-generated, unverified reviews and profiles; treat reviewer-derived location as corroboration to confirm, not fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yelp |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, geolocation → address, phone, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
