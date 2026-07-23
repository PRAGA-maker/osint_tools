---
id: container-tracking
name: Container Tracking
description: Use when you have a shipping container or B/L number and want its location and movement across carriers — returns container status, route, and port/vessel details.
url: http://container-tracking.org/
category: transportation
path:
- transportation
bestFor: Looking up a shipping container's current status and route by container/bill-of-lading number across multiple carriers.
selectorsIn:
- document-id
selectorsOut:
- geolocation
- address
status: live
pricing: freemium
costNote: Free lookups by container number for supported carriers; some carriers/bulk features may require the carrier's own account or a paid tier.
opsec: passive
opsecNote: Passive lookup of logistics data by reference number; no subject is contacted. The tracking site (and the carrier it queries) logs your search — use a clean browser for sensitive investigations.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party aggregator that forwards queries to carrier tracking systems; the underlying carrier data is authoritative, the aggregator's coverage and freshness are not guaranteed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- marinetraffic
- vesselfinder
- container-tracking-cargo
aliases:
- container-tracking.org
- Container Tracker
tags:
- shipping
- logistics
- container
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Container Tracking

> A multi-carrier container lookup — feed it a container or bill-of-lading number and it reports where the box is, its route, and the vessel/ports involved.

## When to use
An investigation touches cargo or trade — a seizure, a sanctions/export case, a supply-chain question — and you have a container number (or B/L number) and want to trace it: current status, port history, and the vessel carrying it. This aggregator routes your query to the relevant carrier's tracking system so you don't need to know which line to check first.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://container-tracking.org/.
2. Enter the container number (e.g. `ABCD1234567`) or bill-of-lading number; select the carrier if prompted.
3. Read the returned status: current location/port, movement history, and the vessel/voyage.
4. Note timestamps and ports (`geolocation`/`address`) and the vessel name for the next step.
5. Pivot: the vessel name/IMO → `[[marinetraffic]]`/`[[vesselfinder]]` for live ship position; ports and dates → corroborate a shipment timeline.

## Inputs → Outputs
- **In:** a container number or bill-of-lading number (`document-id`)
- **Out:** container status, route/port history, vessel details, port `geolocation`/`address`
- **Empty/negative result looks like:** "not found" / no data — the number is wrong, the carrier isn't supported by the aggregator, or the record has aged out; try the carrier's own site directly.

## Gotchas & OpSec
- Coverage depends on which carriers the aggregator supports and how fresh their feeds are — if it fails, go straight to the shipping line's own tracker.
- Container numbers have a check digit; a typo yields a false "not found."
- OpSec: passive; the lookup contacts logistics systems, not any person.

## Overlaps ("do both")
- Pairs with `[[marinetraffic]]` and `[[vesselfinder]]` — this resolves the container to a vessel; those track the vessel's live position and history, completing the cargo-to-ship-to-location chain.

## Trust & verifiability
`trust: community` — a third-party aggregator over authoritative carrier systems; the carrier data is reliable, but confirm anything critical against the shipping line's own tracking directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | container-tracking |
| category | transportation |
| selectorsIn → selectorsOut | document-id → geolocation, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
