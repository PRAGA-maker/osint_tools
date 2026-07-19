---
id: pinkbike
name: Pinkbike
description: Use when you have a `username` or `name` tied to mountain biking and want their profile, posts and marketplace listings — returns social-profile, username and image/location leads.
url: http://www.pinkbike.com
category: communities-forums
path:
- communities-forums
bestFor: Finding a mountain-biking subject's community profile, forum posts, photos and buy/sell listings on the dominant MTB platform.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
- image
status: live
pricing: free
costNote: Free to browse profiles, forums, photos and BuySell listings; an account is only needed to post or message.
opsec: passive
opsecNote: Browsing public profiles/forums/listings is passive. Logging in to view or message ties activity to that account — use a sock puppet if you need to interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, established mountain-bike community platform; profile/forum content is user-generated, so treat identity claims as leads to corroborate.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- pinkbike.com
tags:
- toddington
- curated-directory
- online-communities-blogs
- mountain-biking
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Pinkbike

> The dominant mountain-biking community — search a handle or name to reach a subject's profile, forum posts, photo galleries and BuySell listings, all of which can leak location and identity.

## When to use
Your subject is into mountain biking, or reuses a handle you've seen elsewhere, and you want their footprint on the sport's biggest platform. A Pinkbike profile can expose a real name, location/region, riding photos (backgrounds for geolocation), forum history (interests, associates), and BuySell classifieds (location, contact, gear). Strong for interest-based subjects and for alias correlation when a username carries over from other sites.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try the profile URL directly: `https://www.pinkbike.com/u/<username>/` and use the on-site search for the `username`/`name`.
2. Read the profile: location/region, join date, bio, photos, and activity.
3. Scan their forum posts and comments for personal detail, local trails/events (geolocation), and recurring contacts (`associate`).
4. Check BuySell listings tied to the user — these often include a location and a contact method.
5. Also dork externally: `site:pinkbike.com "<username>"`.
6. Pivot: photos → reverse-image/geolocation; shared handle → username enumeration on other platforms; local trail/event mentions → area narrowing.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile`, confirmed `username`, profile location/region, photos (`image`), forum activity and marketplace listings
- **Empty/negative result looks like:** no profile or only unrelated same-handle users — the subject isn't on Pinkbike or uses a different handle; absence doesn't rule out other cycling communities (Strava, MTBR).

## Gotchas & OpSec
- User-generated: stated names/locations can be aliases or joke entries — corroborate.
- Photos and trail/event mentions are the richest geolocation source here.
- OpSec: passive for browsing; use a sock puppet if you log in to view restricted content or message.

## Overlaps ("do both")
- Pairs with Strava and other cycling/outdoor communities, and with username-enumeration tools — a handle confirmed on Pinkbike is a lead to check across platforms; Strava adds route/location data Pinkbike lacks.

## Trust & verifiability
`trust: community` — a legitimate large community platform; content is authentic user posting, but identity/location claims are self-reported and need corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pinkbike |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, username, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
