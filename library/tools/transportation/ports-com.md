---
id: ports-com
name: Ports.com Sea Route Calculator
description: Use when you have two ports/`geolocation`s and want the optimal sea route and transit time between them — returns a route, distance and seas transited.
url: https://ports.com/sea-route/
category: transportation
path:
- transportation
bestFor: Calculating the sea route, distance and transit time between two ports at a chosen speed.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The sea-route calculator and port directory are free to use in the browser; no account required.
opsec: passive
opsecNote: Passive route calculation; you enter ports, not target data, so nothing about a subject is disclosed. Safe to use without a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party maritime info/route site; route estimates are approximate (great-circle/optimal-path modelling) and not a substitute for navigational charts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ports
aliases:
- ports.com sea route
tags:
- maritime
- transport
- routing
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Ports.com Sea Route Calculator

> A free sea-route planner: pick two ports and it draws the optimal maritime path, the distance, and the transit time at a speed you choose.

## When to use
You're reconstructing a vessel's or cargo's movement and need to know whether a claimed voyage is plausible: how far it is between two ports by sea, which seas/straits a ship would transit, and roughly how long it takes at a given speed (5–40 knots). Useful for sanity-checking AIS gaps, estimating arrival windows, or corroborating a shipping timeline. It reasons about routes/places, not people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ports.com/sea-route/.
2. Set the origin and destination ports (`geolocation`s) on the map/search.
3. Choose a speed (knots); the tool computes the optimal path, total distance and estimated transit time, and lists the seas it passes through.
4. Read the output: use the route and time to test whether a reported voyage/schedule is physically plausible.
5. Pivot: combine with AIS trackers (`[[marinetraffic]]`) and PSC records (`[[tokyo-mou]]`) to place a real vessel on this route with real timestamps.

## Inputs → Outputs
- **In:** two ports / `geolocation`s (+ chosen speed)
- **Out:** an optimal sea route, distance, estimated transit time, and the list of seas transited (`geolocation` context)
- **Empty/negative result looks like:** no route between the chosen points (e.g. an inland or unreachable point selected) — reselect valid ports.

## Gotchas & OpSec
- OpSec: passive; no target data entered.
- Estimates are modelled, not routed by real navigational charts or weather/traffic — treat transit times as approximate.
- It plans routes; it does not track a specific ship. Use AIS tools for actual positions.

## Overlaps ("do both")
- Do both with `[[marinetraffic]]` and `[[tokyo-mou]]` — Ports.com gives the theoretical route/time, AIS gives the actual track, and PSC records tie it to a real, inspected vessel.

## Trust & verifiability
`trust: unverified` — a third-party estimator; route/time figures are approximations to cross-check, not authoritative navigation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ports-com |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
