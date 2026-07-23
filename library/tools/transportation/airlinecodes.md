---
id: airlinecodes
name: Airlinecodes
description: Use when you have an airline/airport code or `name` from an itinerary and want to decode it — returns the airport `geolocation` (city/country) or airline behind an IATA/ICAO code.
url: http://www.airlinecodes.co.uk/aptcodesearch.asp
category: transportation
path:
- transportation
bestFor: Decoding IATA/ICAO airport and airline codes into real names and locations when reading tickets, itineraries, or booking references.
selectorsIn:
- name
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public reference database; no account.
opsec: passive
opsecNote: A static reference lookup — you enter a code, not anything about the subject, so it exposes nothing about your investigation beyond a code to the site's own logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running enthusiast-maintained aviation code database; accurate for the standardised IATA/ICAO codes it lists, though not an official IATA source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- airlinecodes.co.uk
- airport code search
tags:
- aviation
- reference
source: metaosint
lastVerified: '2026-07-23'
enrichment: full
---

# Airlinecodes

> A plain-and-fast airport/airline code decoder — turn the cryptic letters on a boarding pass or itinerary into the actual airport, city, country, or carrier.

## When to use
You're reading travel evidence — a ticket, a booking confirmation, a bag tag, a leaked itinerary, EXIF or a social post mentioning a flight — and hit codes like `LHR`, `EGLL`, `BA`, or `BAW`. This decodes IATA (3-letter airport / 2-letter airline) and ICAO (4-letter airport / 3-letter airline) codes into the real place or carrier, letting you reconstruct where a subject flew from/to.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.airlinecodes.co.uk/ and pick the relevant search (airport codes vs airline/designator codes).
2. Enter the code or the `name` (airport, city, or airline) to search either direction.
3. Read the result: airport code → airport name, city, country (`geolocation`); airline code → carrier name and country.
4. Combine several codes from one itinerary to map a route (origin → connections → destination) and infer timing.
5. Cross-check anything decision-critical against the official IATA code search.

## Inputs → Outputs
- **In:** an IATA/ICAO code or an airport/airline `name`
- **Out:** the decoded airport `geolocation` (city/country) or airline identity
- **Empty/negative result looks like:** "no match" — a mistyped code, a private/military designator not in the DB, or a very new code; verify against the official IATA directory.

## Gotchas & OpSec
- **IATA vs ICAO differ** — `LHR` (IATA) and `EGLL` (ICAO) are the same airport; know which code you have so you search the right field.
- It's an enthusiast database, not the official IATA registry — authoritative for common codes, but confirm edge cases officially.
- Fully passive reference lookup; no subject data involved.

## Overlaps ("do both")
- Complements flight-tracking and booking-reference tools: decode the codes here first, then feed the resolved airports/airline/date into a flight tracker to reconstruct the actual movement.

## Trust & verifiability
`trust: community` — a stable, well-known hobbyist aviation reference; reliable for standard IATA/ICAO codes, with the official IATA search as the tiebreaker for anything unusual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | airlinecodes |
| category | transportation |
| selectorsIn → selectorsOut | name → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
