---
id: cma-voyage-finder
name: CMA CGM Voyage Finder
description: Use when you have a CMA CGM voyage number or vessel name and want its schedule and port calls — returns the ship's route, ports, and estimated dates (geolocation over time).
url: https://www.cma-cgm.com/ebusiness/schedules/voyage
category: transportation
path:
- transportation
bestFor: Looking up a container-ship voyage's schedule and port rotation by voyage number or vessel name (CMA CGM fleet).
selectorsIn: []
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public schedule lookup on the CMA CGM e-business site; no account needed for basic schedule search.
opsec: passive
opsecNote: You query a public carrier schedule with a voyage/vessel identifier — nothing about a person is submitted. Use normal browsing hygiene (VPN); the search itself is low-risk.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party schedule data published by CMA CGM (a major global container line), so voyage/port data is authoritative for that carrier's fleet.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CMA CGM voyage schedule
- CMA CGM ship schedule
tags:
- maritime
- shipping
- transport
- vessel-tracking
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# CMA CGM Voyage Finder

> The container line CMA CGM's own schedule search — turn a voyage number or vessel name into a route, port rotation, and dates.

## When to use
Your case touches maritime shipping on the CMA CGM fleet: a bill of lading with a voyage number, a container's booking, or a named vessel. The Voyage Finder returns that voyage's port rotation and estimated arrival/departure dates, letting you place a specific ship (and by extension its cargo) at ports over time. Useful for reconstructing shipment movement or corroborating where a vessel was on given dates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cma-cgm.com/ebusiness/schedules/voyage.
2. Search by **voyage number** or **vessel name** (CMA CGM and its subsidiaries' ships).
3. Read the result: the vessel, its port rotation, and estimated dates at each port call.
4. Note the ports and dates — this is your movement timeline for that voyage.
5. Pivot: cross-reference the vessel/date against live AIS trackers to confirm real-time or historical position, and against port records for arrival confirmation.

## Inputs → Outputs
- **In:** a CMA CGM voyage number or vessel name
- **Out:** route/port rotation with estimated dates (a `geolocation`-over-time timeline)
- **Empty/negative result looks like:** "voyage not found" — the identifier is wrong, or the vessel is not in CMA CGM's fleet/schedule window (this tool only covers CMA CGM voyages, not all carriers). A miss here does not mean the shipment doesn't exist elsewhere.

## Gotchas & OpSec
- Human-in-the-loop: none; some deep booking/tracking features may prompt for a login, but schedule search does not.
- OpSec: **passive** — only a voyage/vessel identifier is submitted; no subject data leaks.
- Scope is CMA CGM only. For other carriers use their equivalent schedule tools or a cross-carrier AIS tracker.

## Overlaps ("do both")
- Pairs with a live AIS tracker like `[[marinetraffic]]` — the Voyage Finder gives the *planned* schedule/ports; AIS confirms the vessel's *actual* real-time or historical position.

## Trust & verifiability
`trust: trusted` — first-party data from CMA CGM itself, so voyage and port information is authoritative for that carrier; estimated dates are planning figures, so confirm actual arrivals against AIS or port records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cma-voyage-finder |
| category | transportation |
| selectorsIn → selectorsOut |  → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
