---
id: how-s-my-driving-ny
name: How's My Driving NY
description: Use when you have a `vehicle-plate` (and state) and want its NYC traffic/parking/camera violation history — returns a location-and-time pattern of where the vehicle has been ticketed.
url: https://www.howsmydrivingny.nyc/
category: transportation
path:
- transportation
bestFor: Pulling a plate's NYC parking and camera-violation record to build a where-and-when movement pattern.
selectorsIn:
- vehicle-plate
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free public tool built on NYC Open Data (Open Parking and Camera Violations); no account or payment.
opsec: passive
opsecNote: Queries public NYC violation records; the vehicle owner is not notified and nothing is revealed about you. Returns violations tied to a plate, not an owner name — do not infer identity from the plate alone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built on official NYC Open Data violation datasets; the underlying records are authoritative city data, surfaced by a well-known civic tool.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- howsmydrivingny.nyc
- How's My Driving NY
tags:
- vehicle
- violations
- nyc
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# How's My Driving NY

> A civic tool over NYC Open Data: enter a license plate and state to see that vehicle's parking and traffic-camera violations — each stamped with a location and date.

## When to use
You have a `vehicle-plate` linked to a subject and want to establish a pattern of *where and when* that vehicle has been in New York City. Each violation carries a location and timestamp, so a plate's ticket history can indicate neighborhoods the vehicle frequents (near a home, work, or associate `address`) and periods of activity — useful for corroborating movements or narrowing a search area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.howsmydrivingny.nyc/.
2. Enter the license plate number and select the issuing state.
3. Review the returned violations: type, fine status, and — crucially — the location and date of each.
4. Map the locations and cluster by time to spot recurring areas.
5. Pivot: recurring violation locations → candidate home/work `geolocation`/`address` to check with mapping and people-search tools; timeline → corroborate the vehicle's presence.

## Inputs → Outputs
- **In:** `vehicle-plate` + issuing state
- **Out:** NYC parking/camera violation records with per-violation `geolocation` and dates, hinting at frequented `address`es.
- **Empty/negative result looks like:** no violations found — the vehicle has no NYC ticket history (out-of-area, careful driver, or wrong plate/state); that's a real negative, not an error.

## Gotchas & OpSec
- NYC-only: it reflects violations issued in New York City, nothing elsewhere.
- It returns violations for a plate, **not** the owner's name — identity requires DMV/records channels.
- A clean or empty record doesn't mean the vehicle isn't the subject's; it may simply not have been ticketed in NYC.

## Overlaps ("do both")
- Pairs with a VIN/plate decoder like `[[vin-decoder-and-lookup]]` and mapping tools — this gives the where/when pattern, the decoder confirms what the vehicle is, mapping turns locations into leads.

## Trust & verifiability
`trust: trusted` — built directly on official NYC Open Data violation datasets, so the records are authoritative city data (scope limited to NYC).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | how-s-my-driving-ny |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
