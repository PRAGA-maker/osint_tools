---
id: bikemap
name: Bikemap
description: Use when you have a `username` or `geolocation` and want user-uploaded cycling routes that can reveal a person's home area and movement patterns — returns geolocation and social-profile leads.
url: https://www.bikemap.net/
category: transportation
path:
- transportation
bestFor: Browsing user-shared cycling routes worldwide; public routes/profiles can leak a rider's home area and habits.
selectorsIn:
- username
- geolocation
selectorsOut:
- geolocation
- social-profile
status: live
pricing: freemium
costNote: Free to browse public routes and profiles; premium unlocks navigation/offline features. A free account is needed to save routes.
opsec: passive
opsecNote: Passive — you browse public routes/profiles that riders chose to share, without contacting them. As with Strava-style data, public routes can inadvertently reveal a rider's home/start point; you are reading, not probing. Use a sock-puppet account if you sign in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established cycling-route community platform; route data is user-generated, so accuracy and completeness vary and only public content is visible.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- bikemap.net
tags:
- Maps, Geolocation and Transport
- Routes
- fitness-app
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Bikemap

> A global cycling-route community — like Strava's map layer for bikes: public user routes that, taken together, can betray where a rider lives and how they move.

## When to use
You have a subject's Bikemap `username` (or a `geolocation` you want to canvass) and want their shared cycling activity: routes they've ridden or created, which reveal frequented areas, likely home/start points (routes often begin/end near home), and travel patterns. This is a fitness-app OSINT angle — the same "activity data leaks location" principle as Strava — useful when a subject cycles and shares routes publicly. Only public content is visible.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bikemap.net/ (sign in only with a sock-puppet if you need saved features).
2. Search a `username` to view a rider's public profile and routes, or browse routes by `geolocation`/area.
3. Open individual routes: start/end points, the full track, distance, and dates.
4. Look for recurring start/end clusters — these often sit near a home or workplace.
5. Pivot: a clustered start point → candidate home area for further address/imagery work; the `username` → search the same handle on Strava/Komoot/social.

## Inputs → Outputs
- **In:** a Bikemap `username` or a `geolocation`/area
- **Out:** public cycling routes with start/end points and tracks (`geolocation` patterns), the rider's public profile (`social-profile`)
- **Empty/negative result looks like:** no public routes for a user, or a private profile — the person doesn't share publicly here, not that they don't cycle; try other fitness platforms.

## Gotchas & OpSec
- Only public routes/profiles are visible; many riders keep activity private.
- User-generated data — dates and tracks vary in accuracy; start points may be intentionally offset.
- OpSec: passive browsing; sock-puppet any login.

## Overlaps ("do both")
- Same technique as Strava/Komoot route analysis — cross-check the handle across fitness platforms; each may expose routes the others don't.

## Trust & verifiability
`trust: community` — reputable route-sharing platform, but data is user-generated and only partially public; corroborate any inferred home/location before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bikemap |
| category | transportation |
| selectorsIn → selectorsOut | username, geolocation → geolocation, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
