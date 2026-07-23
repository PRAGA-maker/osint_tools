---
id: api-mylnikov-org
name: API mylnikov.org
description: Use when you have a WiFi access point's BSSID (`mac-address`) and want its physical location — a free API that returns `geolocation` (lat/lon + accuracy) from an open WiFi/cell database.
url: https://www.mylnikov.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Geolocating a WiFi access point (or cell tower) from its BSSID/MAC using an open geolocation database.
selectorsIn:
- mac-address
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free API with no stated request limits; open-data queries are MIT-licensed.
opsec: passive
opsecNote: You query a static geolocation database with a BSSID — no contact with the access point or anyone near it. The result places hardware, not necessarily a person; a BSSID can be geolocated without the owner ever knowing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: unverified
trustNote: Independent open-data geolocation API built from openBmap/OpenWifi.su and similar sources; coverage is uneven and the dataset may be stale, so treat hits as approximate leads.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- mylnikov geolocation API
tags:
- Maps, Geolocation and Transport
- Communications, Internet, Technologies
- wifi-geolocation
source: cyb-detective
lastVerified: '2026-07-23'
---

# API mylnikov.org

> A free geolocation API that turns a WiFi access point's BSSID (MAC address) into latitude/longitude — the same wardriving-database trick phones use, exposed as a simple query.

## When to use
You have a WiFi BSSID (`mac-address`) — from a device's known networks, a photo's metadata, a leaked config, or a router — and want to place it on a map. Because access points are largely stationary, geolocating a BSSID can approximate where a device connected, corroborate a claimed location, or point to a home/business network.

## How to use it (`bestInteractionPattern`: api)
1. Query the API with the BSSID, e.g. `https://api.mylnikov.org/geolocation/wifi?bssid=A0:F3:C1:3B:6F:90` (colon or plain-hex format).
2. Read the JSON: `result` code, and on success `data.lat`, `data.lon`, and `range` (accuracy in metres).
3. For better precision, submit multiple nearby BSSIDs (the API supports several at once) to triangulate.
4. Pivot: the coordinates feed mapping/geolocation; a matched home/business network corroborates an `address` hypothesis.

## Inputs → Outputs
- **In:** `mac-address` (WiFi BSSID; optionally several)
- **Out:** `geolocation` (latitude, longitude, accuracy range in metres)
- **Empty/negative result looks like:** a non-200 `result` / no coordinates — the BSSID isn't in the database (common outside well-mapped areas); absence means "not surveyed", not "doesn't exist".

## Gotchas & OpSec
- Coverage is patchy and the dataset can be stale (`status: degraded`): a hit is an approximate lead, and a miss is common — cross-check against another WiFi-geolocation source.
- A BSSID can be spoofed or a router can move; the location is where the AP was last mapped, which may not be current.
- OpSec: **passive** — a database query; nobody is notified.

## Overlaps ("do both")
- Pairs with WiGLE and other WiFi-geolocation databases — coverage differs by region, so query more than one before concluding a BSSID is unknown.

## Trust & verifiability
`trust: unverified` — a useful free open-data API, but coverage and freshness are inconsistent; corroborate any coordinate with a second source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | api-mylnikov-org |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | mac-address → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
