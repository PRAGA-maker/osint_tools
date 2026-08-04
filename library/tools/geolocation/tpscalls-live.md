---
id: tpscalls-live
name: tpscalls.live
description: Use when you have a Toronto `geolocation`/address or a time window and want to see what police were dispatched to nearby — returns live/recent incident types, cross-streets and timestamps mapped to `geolocation`.
url: https://www.tpscalls.live/
category: geolocation
path:
- geolocation
bestFor: Mapping recent Toronto Police dispatches by location and time to corroborate an incident.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web map (also free iOS/Android apps); built on Toronto Police public dispatch data.
opsec: passive
opsecNote: You browse a public map of already-published dispatch data — no query touches any subject. Note the feed deliberately excludes sensitive calls (domestic violence, sexual assault, medical) and ongoing operations, so absence of a pin never means nothing happened.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent project (by developer Riley Durant) surfacing Toronto Police Service public dispatch data; reliable for what's published but not an official police source.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- tpscalls
- TPS calls live
tags:
- geolocation
- scanner
- police-calls
- toronto
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# tpscalls.live

> A live map of Toronto Police Service dispatches — incident type, cross-streets and timestamp for each call, with links to nearby city-camera feeds.

## When to use
Your case touches Toronto (GTA) and you have an `address`/`geolocation` and rough time, and want to know whether police were dispatched nearby and for what — an arrest, collision, gun call, assault, dispute. Useful to corroborate a reported incident, place activity at a location/time, or find nearby traffic-camera views for a scene.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tpscalls.live/ (or the iOS/Android app).
2. Pan/zoom the map to your area of interest, or search a location.
3. Read the pins — each shows incident type, nearest cross-streets and a timestamp; tap one for full detail and any linked nearby city-camera feeds.
4. Filter/scan by time to line up dispatches with your window of interest.
5. Pivot: use the cross-streets/`geolocation` and camera links for further geolocation, or corroborate against local news and official police releases.

## Inputs → Outputs
- **In:** Toronto `address` / `geolocation` + time window
- **Out:** mapped incident `geolocation`s with type + timestamp, nearby camera links
- **Empty/negative result looks like:** no pins for your area/time — but the feed **excludes** domestic-violence, sexual-assault and medical calls plus active operations, so an empty map is not proof nothing occurred.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a public map.
- OpSec: **passive** — you view already-public dispatch data; nothing is sent to any subject.
- Coverage is Toronto-only, near-real-time, and deliberately filtered; treat it as a corroboration aid, not an authoritative incident record. Confirm anything consequential with official Toronto Police sources.

## Overlaps ("do both")
- Complements public webcam/traffic-camera tools and local-news search — tpscalls tells you *what* was dispatched *where/when*; cameras and news add visual and narrative confirmation.

## Trust & verifiability
`trust: community` — an independent project mirroring Toronto Police public dispatch data; accurate for published calls but unofficial and filtered, so verify against police/news for legal use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tpscalls-live |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
