---
id: citizen-com
name: Citizen
description: Use when you have a US `geolocation` and time window and want to know what safety incidents (shootings, fires, police activity, missing-person alerts) were reported there — returns dated, mapped `geolocation` incidents with user video.
url: https://citizen.com/explore
category: geolocation
path:
- geolocation
bestFor: Checking real-time and recent safety incidents at a US location, sometimes with on-scene user-submitted video.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to browse the incident map on the web/app; some features and full alerts require the mobile app and an account. A paid tier (Citizen Premium) adds extra features but isn't needed for the map.
opsec: passive
opsecNote: You read a published incident feed; nothing you do here touches a subject. Passive. If you use the app, it will ask for your location and account — use a sock-puppet setup and deny precise location if you only need to browse.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Citizen aggregates emergency-radio scanning and user reports into incident alerts; fast but unofficial and error-prone — incidents are initial reports, not confirmed facts, and user video is unverified.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- crimemapping-com
- global-incident-map
- nyc-crime-map
aliases:
- Citizen
- Citizen App
- citizen.com
tags:
- Maps, Geolocation and Transport
- Politics, conflicts and crisis
- incident-map
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Citizen

> A real-time US safety-incident map built from emergency-radio monitoring and user reports: see what's happening (or just happened) at a place — sometimes with on-scene video.

## When to use
You have a US `geolocation` and a time window and want a fast read on incidents there: shootings, fires, assaults, police activity, road closures, and sometimes missing-person or found-person alerts. Because Citizen scans emergency channels and collects user posts, it can surface events minutes after they occur, occasionally with bystander video that provides scene detail, faces, or vehicles — valuable when a subject was last seen near an incident.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://citizen.com/explore and navigate/zoom to the city and area of interest (coverage is major US metros).
2. Click incident pins to read the alert: type, time, location, status updates, and any attached user photos/video.
3. For a specific time window, scan recent incidents in that radius; note incident IDs and timestamps.
4. Treat every alert as an unconfirmed initial report — corroborate against police blotters, local news, and the linked media before relying on it.
5. Pivot: on-scene video/photos feed geolocation and reverse-image work; a confirmed incident window feeds your timeline and pairs with crime-map tools.

## Inputs → Outputs
- **In:** `geolocation` (a US metro location) + time window
- **Out:** `geolocation` — dated, mapped safety incidents with status updates and user-submitted media
- **Empty/negative result looks like:** no incidents in the area/time — either nothing was reported/scanned there, or the location is outside Citizen's covered metros; absence is not proof nothing happened.

## Gotchas & OpSec
- Unverified and error-prone: alerts are raw, early reports from scanners/users and are frequently wrong, duplicated, or misclassified — never treat one as fact.
- Coverage gaps: mainly major US cities; rural areas have little or nothing.
- App gating: the web map is browsable, but full alerts/notifications push you to the app and an account.
- OpSec: passive to browse; if you install the app, use a sock puppet and limit location permissions.

## Overlaps ("do both")
- Pairs with `[[crimemapping-com]]`, `[[global-incident-map]]`, and `[[nyc-crime-map]]` — Citizen is fastest and sometimes carries video, while the crime-map tools draw on official police data; use Citizen for immediacy and the others for confirmed records.

## Trust & verifiability
`trust: community` — a crowd/scanner-sourced feed: excellent for speed and for surfacing on-scene media, but each incident is an unconfirmed report to verify against official sources before you cite it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | citizen-com |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
