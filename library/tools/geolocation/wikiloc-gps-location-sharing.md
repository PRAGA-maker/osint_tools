---
id: wikiloc-gps-location-sharing
name: Wikiloc
description: Use when you have a `username`/`name` or an area `geolocation` and want user-posted GPS trails (with start points, dates and photos) — returns geolocation, username and name.
url: http://www.wikiloc.com/wikiloc/home.do
category: geolocation
path:
- geolocation
bestFor: Finding the outdoor GPS tracks a person has published, revealing where and when they travel.
selectorsIn:
- username
- geolocation
selectorsOut:
- geolocation
- username
- name
status: live
pricing: freemium
costNote: Free to browse trails, view maps, and see who posted them; a premium tier adds offline downloads/navigation. Viewing user profiles and tracks is free.
opsec: passive
opsecNote: Browsing public trails and profiles is passive and does not notify the uploader. Only your IP touches Wikiloc. If you create an account to follow/message a user, that becomes attributable — stick to anonymous browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, established outdoor-activity community platform; trail data is user-submitted but the GPS tracks, timestamps, and start points are genuine artifacts uploaded by users.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WikiLoc
- wikiloc.com
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- gps-trails
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Wikiloc

> A global community for sharing GPS trails — a surprisingly rich pattern-of-life source when a subject posts their hikes, rides, and runs.

## When to use
You have a subject who is an outdoor enthusiast (hiker, cyclist, runner, climber) and a `username`/`name` to search, or you want to see what tracks have been posted in a specific area (`geolocation`). Wikiloc users upload GPS tracks that carry start/end coordinates, dates, distances, and often photos — which can reveal where someone lives or frequents, their routine, and their appearance/gear in trail photos. Also useful in reverse: identify a location from a matching posted trail.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.wikiloc.com/.
2. Search by a `username`/`name` to find a user's profile, or browse/search by place to find trails in an area (`geolocation`).
3. Open a user's profile to see all their published trails; open a trail for its map, start point, date, distance, and attached photos.
4. Note that trail start points frequently sit at or near a user's home/regular trailhead — cross-reference repeated starts.
5. Pivot: start coordinates feed mapping and address work; trail photos feed reverse-image/face; the `username` feeds cross-site sweeps; dates feed a movement timeline.

## Inputs → Outputs
- **In:** `username`/`name`, or an area `geolocation`
- **Out:** trail `geolocation`s (start points, routes), the poster's `username`/`name`, dates, photos
- **Empty/negative result looks like:** no profile for the handle, or no trails in the area — the person may not use Wikiloc; absence is not meaningful about their movements.

## Gotchas & OpSec
- Users can set privacy on some trails; you only see what's public.
- A repeated trail start is a strong home/base hint but not proof — corroborate with other geo sources.
- Passive: browsing is anonymous and does not alert the user. Avoid following/messaging from a real account.

## Overlaps ("do both")
- Pairs with Strava-style activity OSINT and general mapping — different platforms capture different athletes; cross-reference any home/trailhead hint against imagery and address records.

## Trust & verifiability
`trust: community` — a large user-generated platform. The GPS tracks and timestamps are authentic uploads; interpret home/routine inferences carefully, as start points can be a trailhead rather than a residence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikiloc-gps-location-sharing |
| category | geolocation |
| selectorsIn → selectorsOut | username, geolocation → geolocation, username, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
