---
id: maersk-tracking
name: Maersk Tracking
description: Use when you have a Maersk container, booking, or bill-of-lading number and want the shipment's current location and movement history — returns port milestones, vessel, and status.
url: https://www.maersk.com/tracking/
category: transportation
path:
- transportation
bestFor: Tracking a specific Maersk container/booking/BL number through its port-by-port journey and current status.
selectorsIn:
- document-id
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public tracking page from Maersk; no account needed for basic container/BL lookups.
opsec: passive
opsecNote: You query Maersk's public tracking with a shipment reference — the parties to the shipment aren't notified. Only Maersk sees your lookup. No subject-side exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Maersk carrier data — authoritative for shipments Maersk carries. Only covers Maersk-line cargo; other carriers need their own portals or an aggregator.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- vesselfinder
- marinetraffic
aliases:
- Maersk container tracking
- maersk.com/tracking
tags:
- shipping
- container-tracking
- logistics
- transport
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Maersk Tracking

> Maersk's first-party shipment tracker: enter a container/booking/bill-of-lading number and follow the cargo's port milestones and current status.

## When to use
Your investigation involves a physical shipment carried by Maersk and you have a reference number — a container number, a booking number, or a bill-of-lading (B/L) number — from a document, invoice, or manifest. Maersk's tracker returns the shipment's route, port-by-port milestones (loaded, departed, arrived, discharged), the carrying vessel, and current location/ETA. It's carrier-specific: it only knows Maersk-line cargo.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.maersk.com/tracking/.
2. Enter the container number, booking number, or B/L number and submit.
3. Read the timeline: origin/destination ports, each transport-plan milestone with dates, the vessel name/voyage, and the latest status/ETA (`geolocation` context).
4. Note the vessel name — that's your bridge from "which box" to "which ship, and where is it now."
5. Pivot: take the vessel name/IMO to `[[vesselfinder]]` or `[[marinetraffic]]` for live AIS position, and the ports/dates to corroborate a person's or company's logistics.

## Inputs → Outputs
- **In:** `document-id` — a Maersk container / booking / B/L number.
- **Out:** `geolocation` — route, port milestones, carrying vessel, current status/ETA.
- **Empty/negative result looks like:** "no results / check the number" — the reference is wrong, isn't a Maersk shipment (try the actual carrier), or is too old to be retained.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — no shipment party is alerted; you touch only Maersk.
- Carrier-scoped: only Maersk (and its sub-brands) cargo. For other lines use their portals or a multi-carrier aggregator.
- Milestones are scheduled/reported events; ETAs shift, and a "discharged" status doesn't tell you where the goods went after the port.

## Overlaps ("do both")
- Pairs with `[[vesselfinder]]` / `[[marinetraffic]]` — Maersk tells you which vessel carries the box; the AIS trackers show that vessel's live position and history. Chain them: container → vessel → live location.

## Trust & verifiability
`trust: trusted` — authoritative first-party carrier data for Maersk shipments. The limitation is scope (Maersk only), not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maersk-tracking |
| category | transportation |
| selectorsIn → selectorsOut | document-id → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
