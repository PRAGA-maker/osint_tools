---
id: russia-ukraine-monitor-map
name: Russia-Ukraine Monitor Map
description: Use when you have a `geolocation` or `image` from the Russia-Ukraine conflict and want verified, geolocated open-source footage for that area — returns geolocated, source-linked incident records.
url: https://www.info-res.org/map
category: transportation
path:
- transportation
bestFor: Browsing verified, geolocated open-source videos/photos of military activity in Ukraine on an interactive map.
selectorsIn:
- geolocation
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public map by the Centre for Information Resilience (non-profit); no account.
opsec: passive
opsecNote: Passive — you browse a published, curated map; no subject is contacted. Each pin links to already-public source media; still handle graphic conflict footage and any personal details in it responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the Centre for Information Resilience (CIR); entries are analyst-verified and cross-referenced with satellite imagery before mapping.
missingPersonsRelevance: low
coverage:
- ua
- ru
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Eyes on Russia
- CIR Monitor Map
tags:
- Maps, Geolocation and Transport
- Military tracking
- conflict
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Russia-Ukraine Monitor Map

> The Centre for Information Resilience's interactive map of verified, geolocated open-source footage of the war in Ukraine.

## When to use
You are working a Russia-Ukraine conflict lead — a place, an approximate `geolocation`, or an `image`/video you're trying to place — and want to see what verified open-source material exists for that area. Each mapped incident has been geolocated and cross-checked (including against satellite imagery) by CIR analysts, with links to the original source media. Primarily a conflict-monitoring/geolocation resource; direct missing-persons relevance is niche.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.info-res.org/map.
2. Pan/zoom to the area of interest, or filter by date/category to narrow incidents.
3. Click a pin to read the entry: verified location, date, description, and a link to the source video/photo.
4. Use it to corroborate a location or event, or to source verified imagery for your own geolocation work.
5. Pivot: a confirmed coordinate feeds `[[quick-geolocation-search]]` and satellite tools; source media may carry further leads (units, landmarks, timestamps).

## Inputs → Outputs
- **In:** `geolocation`/area or an `image` you're trying to place
- **Out:** `geolocation` — verified, source-linked incident records for that area
- **Empty/negative result looks like:** no pins for a location/time window — the map reflects what analysts have verified and published, so absence isn't proof nothing happened there.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; content is already public. Expect graphic conflict footage; handle any identifiable individuals in source media responsibly.
- Scope is the Ukraine conflict only, and it's a curated verified feed — not an exhaustive or real-time record.

## Overlaps ("do both")
- Pairs with satellite/imagery tools and `[[quick-geolocation-search]]` — the map gives verified ground events; those let you independently re-verify a coordinate.

## Trust & verifiability
`trust: trusted` — CIR is a reputable non-profit and entries are analyst-verified and satellite-cross-referenced; still follow each pin's source link to confirm before citing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | russia-ukraine-monitor-map |
| category | transportation |
| selectorsIn → selectorsOut | geolocation, image → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
