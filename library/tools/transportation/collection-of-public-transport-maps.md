---
id: collection-of-public-transport-maps
name: Collection of public transport maps
description: Use when you have a `geolocation`/city and want live public-transport tracking maps for it — returns real-time transit vehicle positions and routes.
url: https://cipher387.github.io/public_transport_maps/
category: transportation
path:
- transportation
bestFor: A curated launcher of ~20 real-time bus/train/tram tracking maps across various countries.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free static link directory; the destination transit maps are free (a few may need registration).
opsec: passive
opsecNote: Passive — you view public transit-operator maps; no subject is contacted. Each destination map sees your visit; use a clean browser for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Curated by cipher387 (CybDetective); the page itself notes it is no longer updated and points to a newer resource, so some links may have rotted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- cipher387 public transport maps
tags:
- Maps, Geolocation and Transport
- Transport
- transit
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Collection of public transport maps

> A curated index of ~20 real-time public-transport tracking maps (buses, trains, trams) for cities and countries worldwide.

## When to use
You have a `geolocation`/city and want to see live public-transport movement there — for example to understand transit options and timings near a last-known location, or to check whether a route/line was running. The page groups links by country (US, Canada, UK, Germany, Netherlands, Finland, Estonia, Ukraine, Australia, NZ, South Korea, Russia, and more).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cipher387.github.io/public_transport_maps/.
2. Find the country/city you need and open its transit map link.
3. On the destination map, watch real-time vehicle positions and routes; check schedules/lines.
4. Note the page is archived — if a link is dead, follow the "newer resource" pointer the author gives, or search for the operator's current live-map URL.
5. Pivot: transit timing/routes support a movement/timeline reconstruction around a location.

## Inputs → Outputs
- **In:** `geolocation`/city of interest
- **Out:** `geolocation` — live transit vehicle positions and routes on the destination map
- **Empty/negative result looks like:** a dead/redirecting link (the list is no longer maintained) or a city with no listed map — fall back to searching the local operator directly.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; destination maps log your visit.
- Status **degraded**: the collection is explicitly no longer updated, so treat it as a starting index, not an authoritative or complete list; verify each link still works.

## Overlaps ("do both")
- Pairs with `[[quick-geolocation-search]]` — use that to fan a point across general maps, this for the specialised live-transit layer of the same area.

## Trust & verifiability
`trust: community` — a community-curated index; authority rests with each transit operator's own map. Because the list is unmaintained, confirm links are live before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | collection-of-public-transport-maps |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
