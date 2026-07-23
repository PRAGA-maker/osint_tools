---
id: runkeeper
name: Runkeeper (ASICS Runkeeper)
description: Use when you have a subject's `username`/`name` and want their public running/walking activities and routes — returns geolocation (GPS routes, start points) and social-profile leads.
url: https://runkeeper.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Finding a person's public fitness activities and GPS routes to infer home area and routine.
selectorsIn:
- username
- name
selectorsOut:
- geolocation
- social-profile
- image
status: live
pricing: freemium
costNote: Free app/account with public activity feeds and route sharing; ASICS Runkeeper Go (paid) adds coaching/analytics not needed for OSINT viewing.
opsec: passive
opsecNote: Viewing public activities and routes is passive and doesn't notify the subject. Following a user or interacting requires an account and is attributable — use a sock puppet. Fitness routes routinely reveal home/work start points and daily routine, which is highly sensitive; handle a subject's location data carefully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Mainstream ASICS-owned fitness platform; activity data is user-generated and gated by each user's privacy settings.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ASICS Runkeeper
- runkeeper.com
tags:
- fitness-tracking
- gps-routes
- social-profile
- toddington
- curated-directory
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Runkeeper (ASICS Runkeeper)

> A mainstream GPS running app whose public profiles expose activity feeds and route maps — a way to place a subject's runs/walks and infer where they live.

## When to use
Your subject is active on fitness apps and you have a `username`/`name` to check. Runkeeper users can publish activities with GPS route maps, distances, times, and photos. When public, those routes cluster around home/work start points and reveal routine — concrete `geolocation` value for pattern-of-life and missing-persons work, plus a linkable `social-profile`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://runkeeper.com and search for a candidate profile by `username`/`name` (or reach a profile via a shared activity link).
2. If the profile/activities are public, open the activity feed: each entry shows a route map, date/time, distance, and sometimes photos (`selectorsOut`).
3. Read the route maps for recurring start/end points that suggest a home or workplace.
4. Pivot: the username can be enumerated across other fitness/social platforms; route start points narrow a geographic area; photos may add EXIF or scenery to geolocate.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `geolocation` (GPS routes, start points), `social-profile` (Runkeeper profile + handle), `image` (activity photos)
- **Empty/negative result looks like:** no matching profile, or a profile whose activities are set private — meaning no public route data, not that the person doesn't run.

## Gotchas & OpSec
- Human-in-the-loop: none for viewing public content.
- OpSec: passive while reading; following/commenting is attributable — use a sock puppet.
- Privacy settings vary and users can hide start/end zones; treat a route cluster as an area, not a confirmed address.

## Overlaps ("do both")
- Pairs with [[alltrails]] and Strava-style activity search — cross-run because a fitness-minded subject often reuses the same handle across platforms, and each exposes different routes/photos.

## Trust & verifiability
`trust: unverified` — a legitimate mainstream platform, but the data is user-generated and privacy-gated; corroborate any home/area inference with a second source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | runkeeper |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | username, name → geolocation, social-profile, image |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
