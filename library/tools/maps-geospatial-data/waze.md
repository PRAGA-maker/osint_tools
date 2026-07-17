---
id: waze
name: Waze
description: Use when you have a `geolocation` and want real-time, crowd-sourced road conditions there — returns live traffic, incidents, and user reports useful for confirming a scene or planning ground movement.
url: https://www.waze.com/live-map
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Reading live crowd-sourced traffic, incidents, and hazards at a location.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free live map in the browser; the app is free too. No account needed to view the public live map.
opsec: passive
opsecNote: Viewing the public live map is passive — no target is contacted. Note that if you use the Waze app while navigating, you broadcast your own presence/reports; use the browser live-map for read-only OSINT, not the app under your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced by drivers (owned by Google); reports are real user submissions, so they are timely but unverified and can be stale or wrong.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- waze-livemap
aliases:
- Waze Live Map
- waze.com/live-map
tags:
- maps
- traffic
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Waze

> A crowd-sourced live traffic map — drivers report accidents, hazards, closures, and police in real time, which makes it a quiet source for what's happening on the roads at a given place and moment.

## When to use
You have a `geolocation` and want ground-truth road conditions: is there an accident, closure, or reported incident right now near a location of interest? In OSINT this supports corroboration (a claimed traffic incident, a road closure that would affect movement) and situational awareness for ground work. It reports on roads and traffic, not people, so direct person-finding relevance is low; treat it as a real-time environmental layer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.waze.com/live-map in a browser (no login, read-only).
2. Pan/zoom to the `geolocation` of interest.
3. Read the live layers — traffic speed/jams, and pinned reports (crashes, hazards, closures, police) with their icons and timestamps.
4. Click a report for detail and how recently it was posted; treat older reports with caution.
5. Pivot: a confirmed incident + time supports/contradicts a claimed event; road closures inform how someone could have moved through an area.

## Inputs → Outputs
- **In:** a `geolocation` / area to inspect
- **Out:** live traffic conditions and user-reported incidents (`geolocation`) with timestamps
- **Empty/negative result looks like:** a quiet map with no active reports — either genuinely nothing is happening or coverage there is thin (Waze density varies by region/time). Absence of a report isn't proof nothing occurred.

## Gotchas & OpSec
- Reports are **crowd-sourced and unverified** — timely but sometimes wrong, duplicated, or stale; corroborate anything decisive.
- Coverage depends on active Waze users in the area; rural/low-usage regions show little.
- OpSec: use the **browser live map** (read-only). Don't use the app under your real account for investigative viewing — it would report your own location.

## Overlaps ("do both")
- Pairs with [[waze-livemap]] and mainstream mapping (Google Maps traffic) — cross-check the same area, since crowd-sourced coverage and reporting differ between platforms.

## Trust & verifiability
`trust: community` — genuine driver-submitted reports (a Google-owned platform), so data is real and timely but unverified; confirm important claims against another source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | waze |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
