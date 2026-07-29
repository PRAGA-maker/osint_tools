---
id: mapmyfitness
name: MapMyFitness
description: Use when a subject may log workouts publicly and you want their routes/start points — a fitness social network whose public activity maps can leak `geolocation` and routines.
url: https://www.mapmyfitness.com
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Finding a person's publicly shared run/ride routes and workout patterns, which can reveal home/work areas and daily routine.
selectorsIn:
- name
- username
selectorsOut:
- geolocation
- social-profile
status: live
pricing: freemium
costNote: Free to create an account and view public profiles/routes; premium (MVP) tiers add training features. Viewing public activity needs no payment.
opsec: active
opsecNote: Browsing public routes is passive, but to see much you often need a logged-in account, and following/friending a target is active and visible. Use a sock-puppet account. Treat any home-location inference from routes as sensitive — this is exactly the Strava-style leak that endangers people, so handle findings carefully.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by Under Armour (MapMyFitness/MapMyRun family); a legitimate platform, but user-shared data is self-published and privacy-setting dependent.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
aliases:
- MapMyRun
- MapMyRide
- Under Armour MapMyFitness
tags:
- fitness
- geolocation
- social-profile
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# MapMyFitness

> A fitness-tracking social network (the MapMyRun/MapMyRide family) — investigatively valuable because public workout routes can betray a subject's home area, routine, and locations.

## When to use
You suspect a subject records runs/rides and shares them publicly, and you want the geographic intelligence that leaks from that: route start/end points (often near home or work), frequented areas, and time-of-day patterns. This is the classic fitness-app location leak — potentially high value for placing someone, when they haven't locked their privacy settings.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a sock-puppet account, search MapMyFitness for the subject's `name`/`username` (cross-reference handles reused on other platforms).
2. Open a matching public profile and view their shared workouts/routes on the map.
3. Note recurring start/end points, common areas, and activity times — these cluster around home/work.
4. Corroborate an inferred location against other sources before treating it as fact.
5. Pivot: an inferred neighbourhood feeds address/people-search; a reused username feeds cross-platform enumeration.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile`, public route `geolocation` (start/end points, frequented areas), activity timing
- **Empty/negative result looks like:** no profile, or a profile with private/hidden activity — many users lock routes, so absence of visible routes is common and not proof of no account.

## Gotchas & OpSec
- **Sensitive by nature**: route data can expose a person's home — handle responsibly and lawfully; this leak is why platforms added privacy zones.
- Privacy settings and "privacy zones" may blur start points; don't over-trust a single route's endpoint.
- Following/friending to see more is active and visible — use a sock puppet and avoid direct contact.

## Overlaps ("do both")
- Pair with other fitness/social geolocation sources (Strava-style route inference) and username-enumeration tools — cross-platform handles confirm identity, and multiple route sources triangulate a location more reliably than one.

## Trust & verifiability
`trust: community` — a legitimate Under Armour platform, but the useful data is user-published and privacy-dependent; verify any location inference against independent evidence before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapmyfitness |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | name, username → geolocation, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
