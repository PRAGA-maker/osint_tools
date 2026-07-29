---
id: passenger-airlines-wiki
name: Passenger Airlines Wiki
description: Use when you have an airline `name`, IATA/ICAO code, or callsign and want to resolve it to its country, hub and operating status — returns geolocation and employer-org context.
url: https://en.wikipedia.org/wiki/list_of_passenger_airlines
category: transportation
path:
- transportation
bestFor: Resolving an airline name/code/callsign to its country of registration, hubs, and active/defunct status.
selectorsIn:
- name
selectorsOut:
- geolocation
- employer-org
status: live
pricing: free
costNote: Free — Wikipedia's list of passenger airlines and the per-airline articles it links to. No account needed.
opsec: passive
opsecNote: Fully passive — reading a public encyclopedia article. Nothing reaches your target. Wikipedia can lag reality (mergers, rebrands, ceased operations), so treat status as indicative and confirm current operating status elsewhere.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Wikipedia — well-sourced and broad, but community-edited; cross-check specifics (codes, hubs, status) against the airline's own site or an aviation registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- List of passenger airlines
- Wikipedia airlines list
tags:
- aviation
source: metaosint
lastVerified: '2026-07-29'
enrichment: full
---

# Passenger Airlines Wiki

> Wikipedia's index of passenger airlines — a fast way to turn an airline name, IATA/ICAO code, or callsign into its country, hubs, and operating status.

## When to use
You have an airline reference — a `name` on a boarding pass or itinerary, an IATA (2-letter) or ICAO (3-letter) code, a flight-number prefix, or an ATC callsign — and need to identify the carrier: what country it's registered in, where it's based/hubs, whether it still operates, and any parent/alliance. Handy for grounding a travel lead before diving into flight-tracking or booking-record work. It's reference data, not a live tracker.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://en.wikipedia.org/wiki/List_of_passenger_airlines.
2. Find the airline by name (or use the browser's find to match a code/callsign in the table).
3. Follow the link to the airline's own Wikipedia article for country, hubs, fleet, IATA/ICAO codes, callsign, parent company, and active/defunct status.
4. Note the code/callsign for use in flight-tracking tools.
5. Pivot: the IATA/ICAO code → flight-tracking and schedule tools; the hub/country → geolocation context for a travel timeline.

## Inputs → Outputs
- **In:** airline `name`, IATA/ICAO code, or callsign
- **Out:** country of registration and hub `geolocation`, operating status, parent/`employer-org`, codes and callsign
- **Empty/negative result looks like:** no entry for a very small, charter, or newly-formed carrier, or an outdated "active" status for one that has since ceased — confirm current status on the carrier's site or an aviation authority.

## Gotchas & OpSec
- Wikipedia lags on mergers, rebrands and shutdowns — verify operating status separately.
- Codes are reused over time (a retired IATA code may be reassigned) — match on name+code, not code alone.
- OpSec: fully passive; no exposure.

## Overlaps ("do both")
- Feeds flight-tracking tools (Flightradar24/ADS-B) — this resolves the carrier identity; the trackers give live/historical flights for that carrier's codes.

## Trust & verifiability
`trust: community` — Wikipedia is broad and generally well-sourced but community-edited; confirm decisive details (codes, status, ownership) against a primary aviation source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | passenger-airlines-wiki |
| category | transportation |
| selectorsIn → selectorsOut | name → geolocation, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
