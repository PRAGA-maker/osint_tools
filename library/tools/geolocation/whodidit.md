---
id: whodidit
name: WhoDidIt
description: Use when you have a `geolocation` and want the OpenStreetMap editors who changed that area — returns editor usernames and edit dates.
url: https://simon04.dev.openstreetmap.org/whodidit/
category: geolocation
path:
- geolocation
bestFor: Finding which OSM contributors edited a specific map area and when, to attribute or investigate local mapping activity.
selectorsIn:
- geolocation
- username
selectorsOut:
- username
- geolocation
status: live
pricing: free
costNote: Free community OSM tool; no account needed. Data comes from OSM's public changeset feed.
opsec: passive
opsecNote: Passive — you query a public changeset index; OSM editing is public by design, so no one is notified. The usernames it returns are self-chosen OSM handles, already public.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-run OSM changeset analyzer (simon04); it reflects public OSM edit metadata, which is authoritative for who-edited-what but says nothing about the real identity behind a handle.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- openstreetmap
- openstreetmap-overpass-turbo-taginfo-database
aliases:
- WhoDidIt OSM Changeset Analyzer
- whodidit
tags:
- Maps, Geolocation and Transport
- openstreetmap
- changeset
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# WhoDidIt

> An OpenStreetMap changeset analyzer — click an area and see which contributors edited it, and when.

## When to use
You have a `geolocation` and want to know who edited the OpenStreetMap data there — the contributor `username`s and the dates of their changes. Two investigative angles: attributing local mapping activity (who added a building, path, or POI in a specific spot, useful when OSM edits themselves are the subject), and pivoting from a known OSM `username` to the geographic footprint of their edits (where in the world someone maps often clusters around where they live/travel).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://simon04.dev.openstreetmap.org/whodidit/.
2. Navigate/zoom to the area of interest and select a region, or filter by a time window (e.g. last week).
3. Read the returned changesets: each shows the editor's OSM `username`, the date, and the changed features; an RSS feed is available for monitoring.
4. To profile a person, note the clustering of a handle's edits across areas.
5. Pivot: an OSM handle feeds cross-platform username enumeration and the OSM user profile (which sometimes carries a bio, home location, or links); edit clusters suggest a home/activity area.

## Inputs → Outputs
- **In:** `geolocation` (map area) or an OSM `username`
- **Out:** contributor `username`s and edit dates for that `geolocation`
- **Empty/negative result looks like:** no changesets in the area/window — the region simply hasn't been edited in that timeframe; it reflects mapping activity, not the absence of features.

## Gotchas & OpSec
- Usernames are self-chosen OSM handles — they attribute an edit, not a real-world identity; corroborate before linking to a person.
- Only shows OSM edit metadata; it can't reveal anything the editor didn't put into OSM.
- Coverage/timeliness depend on the tool's changeset database refresh; very recent edits may lag.
- OpSec: fully passive; all data is already public in OSM.

## Overlaps ("do both")
- Pairs with `[[openstreetmap]]` (the OSM user profile behind a handle, plus the map itself) and `[[openstreetmap-overpass-turbo-taginfo-database]]` (querying the actual features) — WhoDidIt gives the who/when, those give the who-they-are and what-was-changed.

## Trust & verifiability
`trust: community` — a community tool over authoritative public OSM changeset data; the edit attribution is reliable, but a handle is not an identity, so treat person-level conclusions as leads to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whodidit |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, username → username, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
