---
id: airbnb
name: Airbnb
description: Use when you have a host/guest `name` or profile URL and want their Airbnb presence — returns profile details, reviews, and approximate listing locations.
url: https://www.airbnb.com
category: communities-forums
path:
- communities-forums
bestFor: Locating a subject's Airbnb host or guest profile and the reviews, photos, and area of their listings.
selectorsIn:
- name
- social-profile
selectorsOut:
- social-profile
- geolocation
- associate
status: live
pricing: free
costNote: Browsing profiles and listings is free without an account; messaging or booking requires a free Airbnb account.
opsec: active
opsecNote: Logged-in browsing can leave a footprint — viewing a profile is generally silent, but sending a message or booking request notifies the host. Browse public listing/profile pages in a sock-puppet or logged-out session where possible.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Profile and review content is user-generated; hosts curate what they show, and listing locations are deliberately approximate until booking, so treat details as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- vrbo
- couchsurfing
aliases:
- airbnb.com
tags:
- toddington
- online-communities-blogs
- accommodation
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Airbnb

> The accommodation marketplace as an OSINT surface — a subject's host or guest profile carries a photo, join date, reviews, and the rough location of their listings.

## When to use
You have a subject who may host or travel via Airbnb, or a profile URL/`name` you want to check. An Airbnb host profile exposes a photo, first name, join date, verification badges, a bio, their listings, and reviews — reviews naming other guests/hosts are `associate` leads, and a listing pins a subject to an approximate `geolocation`. Useful for placing a subject who rents out property, or corroborating a travel/residence claim.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.airbnb.com; search a location for listings, or open a known profile URL (`/users/show/…`).
2. Read the profile: photo, first name, join date, verifications, bio, languages, listings, and reviews (both as host and guest).
3. For a listing, note the map — Airbnb shows an approximate circle, not the exact address, until booking.
4. Read reviews for names, dates, and details that place the subject or connect other people.
5. Pivot: the profile photo feeds reverse-image/face tools; the listing area feeds mapping/property tools; reviewer names feed people-search.

## Inputs → Outputs
- **In:** `name` or `social-profile` (Airbnb profile URL)
- **Out:** `social-profile` (profile details), approximate `geolocation` (listing area), `associate` (reviewers/other hosts)
- **Empty/negative result looks like:** no matching profile/listing — the subject may not use Airbnb, may host under a different first name, or the profile is sparse; absence is not proof of no Airbnb activity.

## Gotchas & OpSec
- Airbnb deliberately shows only a first name and an approximate listing location — exact address requires a booking, which is intrusive and out of scope for passive OSINT.
- Profiles are self-curated; reviews are the more candid signal.
- **Active risk:** messaging or booking notifies the host — keep to viewing public pages.
- OpSec: prefer logged-out/sock-puppet browsing; avoid any host contact.

## Overlaps ("do both")
- Pairs with `[[vrbo]]` and `[[couchsurfing]]` — check the other short-let and hospitality platforms too, since a subject often appears on only one.

## Trust & verifiability
`trust: unverified` — user-generated, host-curated content with intentionally coarse location; profile and review details are useful leads that must be corroborated with other sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | airbnb |
| category | communities-forums |
| selectorsIn → selectorsOut | name, social-profile → social-profile, geolocation, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
