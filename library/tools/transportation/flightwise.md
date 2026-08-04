---
id: flightwise
name: Flightwise
description: Use when you have a flight number or aircraft tail/N-number and want its position, route, or status — returns live/historical flight tracking and aircraft lookups.
url: http://flightwise.com
category: transportation
path:
- transportation
bestFor: Tracking a specific flight or aircraft (by flight number or N-number) and reading its route/status.
selectorsIn:
- document-id
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free basic flight tracking and N-number lookup; Extended/Premium subscription tiers add features.
opsec: passive
opsecNote: Passive — you query public flight-tracking data; the subject/aircraft owner is not contacted. No case data is submitted beyond the flight/tail number you look up.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running independent aviation-tracking site; coverage/latency vary and it notes some subscriber services are limited. Best treated as one source among several trackers.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- flightwise.com
tags:
- aviation
- flight-tracking
source: metaosint
lastVerified: '2026-08-04'
enrichment: full
---

# Flightwise

> An independent flight-tracking site: look up a flight by number, or an aircraft by its N-number (tail), and get position, route, and status — with a usable free tier.

## When to use
Your case involves a specific aircraft or flight — a subject known to travel on, or own, a particular plane; a tail number seen in a photo; a flight referenced in messages. Flightwise lets you resolve a flight number or N-number into position/route/status. Aviation leads are niche in missing-persons work, so reach for it only when a flight/aircraft is concretely in play.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://flightwise.com.
2. Enter the **flight number** to look up a specific flight, or use **N-Number Lookup** to find an aircraft by its US tail number; you can also list flights by airport/airline.
3. Read the result: current/last position, route, altitude, and status; N-number lookups tie the tail to aircraft details.
4. Cross-check against another tracker — coverage and freshness vary, and some flights (private/blocked) won't appear.
5. Pivot: an N-number ties an aircraft to a registered owner via FAA registry tools; a route/position adds a `geolocation` timeline.

## Inputs → Outputs
- **In:** `document-id` (flight number or aircraft N-number/tail)
- **Out:** `geolocation` (aircraft position/route) plus status and aircraft details
- **Empty/negative result looks like:** no track found — meaning the flight isn't currently tracked, the tail is blocked/foreign, or the number is wrong; absence is not proof the aircraft didn't fly.

## Gotchas & OpSec
- N-number lookup is US-centric (FAA registrations); foreign registrations may not resolve here.
- Blocked/privacy-flagged aircraft and many private flights won't show — use complementary trackers.
- Coverage and latency vary; treat a single tracker's picture as partial.

## Overlaps ("do both")
- Pairs with the FAA aircraft registry and other flight trackers — Flightwise gives position/route, the registry ties an N-number to an owner; cross-tracker checks fill coverage gaps.

## Trust & verifiability
`trust: unverified` — a useful independent tracker but not authoritative; corroborate any critical flight/aircraft fact against a second tracker and the official registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flightwise |
| category | transportation |
| selectorsIn → selectorsOut | document-id → geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
