---
id: alltrails
name: AllTrails
description: Use when you have a subject's `username`/`name` or a location and want their recorded hikes/runs and photos — returns geolocation (trail activity, GPS routes) and social-profile leads.
url: https://www.alltrails.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Finding a person's public outdoor-activity profile (recorded trails, reviews, photos) and geolocating where they hike/run.
selectorsIn:
- username
- name
- geolocation
selectorsOut:
- geolocation
- social-profile
- image
status: live
pricing: freemium
costNote: Free to browse trails and view public user profiles/activities/reviews. AllTrails+ (paid) adds offline maps, live tracking, and route-building — not needed for OSINT viewing.
opsec: passive
opsecNote: Browsing public profiles, activities, and reviews is passive and doesn't notify the subject. Creating an account to follow a user or comment is active and attributable — use a sock-puppet account. Note recorded activities can reveal a person's home-area trailheads and routine, which is sensitive location data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Large mainstream outdoor platform; profiles and activities are user-generated, so accuracy and privacy settings vary per user.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- alltrails.com
tags:
- outdoor-activity
- gps-tracks
- social-profile
- bellingcat-toolkit
- environment-wildlife
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# AllTrails

> A mainstream hiking/running platform whose public user profiles expose recorded routes, reviews, and photos — a way to geolocate a subject's outdoor habits.

## When to use
Your subject is an outdoors person and you have a `username`/`name` to look for, or a location to canvass. AllTrails users publicly log completed hikes/runs (with GPS routes, dates, and photos) and leave reviews on specific trails. That turns into concrete `geolocation` — the trailheads and areas they frequent, which often cluster near home — plus photos and a linkable `social-profile`. Genuinely useful in missing-persons and pattern-of-life work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.alltrails.com/.
2. Search a trail/park/city relevant to the subject, or search a candidate `username`/`name` to find a matching profile.
3. On a profile, review the public activity list: recorded trails, dates, GPS routes, photos, and reviews (`selectorsOut`).
4. Pivot: recurring trailheads narrow a home area; photos may carry EXIF or backgrounds to geolocate; the username can be cross-checked on other platforms.

## Inputs → Outputs
- **In:** `username`, `name`, or `geolocation` (a place to look for activity)
- **Out:** `geolocation` (recorded routes/trailheads), `social-profile` (AllTrails profile + linked handle), `image` (activity photos)
- **Empty/negative result looks like:** no matching profile, or a profile with activities set private — meaning no public trail data, not that the person doesn't hike.

## Gotchas & OpSec
- Human-in-the-loop: none for viewing public content.
- OpSec: passive while reading; following/commenting requires an account and is attributable — use a sock puppet.
- Privacy varies: many users restrict activities, and displayed routes may be trimmed near "home"; treat a cluster as an area, not an address.

## Overlaps ("do both")
- Pairs with Strava-style activity search and username-enumeration tools — cross-run because an outdoors subject often mirrors the same handle across fitness platforms, and each exposes different routes/photos.

## Trust & verifiability
`trust: community` — a large, legitimate platform, but the profile/activity data is user-generated and privacy-gated; corroborate any location inference with a second source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alltrails |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | username, name, geolocation → geolocation, social-profile, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
