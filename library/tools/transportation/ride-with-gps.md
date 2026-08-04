---
id: ride-with-gps
name: Ride With GPS
description: Use when you have a `username`/`name` (a cyclist or runner) and want their public routes, ride history and start locations — returns `geolocation` pattern-of-life data.
url: https://ridewithgps.com/users
category: transportation
path:
- transportation
bestFor: Pulling a subject's public cycling/running routes to map their home area, routines and frequent locations.
selectorsIn:
- username
- name
selectorsOut:
- geolocation
- social-profile
status: live
pricing: freemium
costNote: Free to view public profiles and routes; a paid tier adds planning/navigation features. Investigative viewing is free.
opsec: passive
opsecNote: Browsing public profiles and routes is passive, but a logged-in account leaves a follower/viewer footprint and some social features notify the target. View while logged out (or with a sock-puppet account) and avoid following, liking, or messaging the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A mainstream, reputable cycling/running platform; the route data is user-generated, so accuracy depends on what the subject recorded and chose to make public.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- ridewithgps.com
- RWGPS
tags:
- Maps, Geolocation and Transport
- Routes
- pattern-of-life
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Ride With GPS

> A cycling/running route platform whose public profiles are a rich pattern-of-life source — recorded rides expose where a subject starts, rides and returns.

## When to use
You have a `username` or real `name` for someone who cycles or runs and records it, and you want to map their movements. Public Ride With GPS profiles list a user's rides and planned routes, each with a map — and routes overwhelmingly begin and end at home or work. That makes it a strong pattern-of-life source: frequent start points, regular routes, and ride times/dates can localize a subject and establish routine, which is directly relevant to locating someone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ridewithgps.com/users and use the user search (by `name`/`username`), or navigate directly to `ridewithgps.com/users/<id>` if you already have the profile.
2. Confirm identity from the profile: display name, avatar, bio, and linked social accounts.
3. Open the user's public **Rides** and **Routes** tabs. Each entry has a map — look for the repeated start/finish point (likely home) and clustering of routes in one area.
4. Note timestamps and distances to build a routine (e.g. weekday morning loops from the same corner).
5. Pivot: feed the recurring start `geolocation` into mapping/address tools; feed the `username` and linked socials into cross-platform username searches.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `geolocation` (route start/finish points, ridden areas, timing), `social-profile` (bio, linked accounts)
- **Empty/negative result looks like:** no matching user, or a profile whose rides/routes are set to private (you'll see the profile shell but no maps). Private routes = no geodata, not "no such person."

## Gotchas & OpSec
- Human-in-the-loop: none, but identity disambiguation is manual — common names return multiple users.
- OpSec: **passive** when logged out; a logged-in account can leave viewer traces and social features may alert the subject. Never follow/message the target.
- Route privacy is per-item and users can enable "privacy zones" that blur the true start near home — treat the visible start as approximate when a zone is in use.

## Overlaps ("do both")
- Pairs with Strava-style route/segment OSINT and with username-search tools — Ride With GPS covers users the other platforms miss, and cross-referencing the same routine across platforms strengthens a geolocation.

## Trust & verifiability
`trust: community` — a well-established mainstream platform, but the intelligence value rests on user-generated recordings. Verify a home inference across multiple rides and against independent sources before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ride-with-gps |
| category | transportation |
| selectorsIn → selectorsOut | username, name → geolocation, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
