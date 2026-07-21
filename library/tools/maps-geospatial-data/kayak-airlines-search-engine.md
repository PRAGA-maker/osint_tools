---
id: kayak-airlines-search-engine
name: Kayak Airlines Directory
description: Use when you have an airline name or IATA code and want its official identifier and contact line — returns the airline's name, two-letter code and customer/contact phone number.
url: https://www.kayak.com/airlines
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: A quick global directory mapping airline names to IATA codes and contact phone numbers.
selectorsIn:
- employer-org
selectorsOut:
- phone
status: live
pricing: free
costNote: Free reference directory; no account required.
opsec: passive
opsecNote: A static reference page — passive and anonymous, with no target interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Convenience directory on a commercial travel-metasearch site (Kayak); useful for airline code/contact lookup, not a data source about individuals.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- kayak-travel-search-engine
aliases:
- Kayak airlines list
- kayak.com/airlines
tags:
- toddington
- curated-directory
- specialty-search
- aviation
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Kayak Airlines Directory

> A simple global airline directory — look up a carrier's two-letter IATA code and customer-contact phone. A reference aid, not a people-search tool.

## When to use
You're working an aviation thread — a boarding pass, a flight number, an itinerary, a carrier mentioned in records — and need to resolve an airline name to its official IATA code, or find the airline's contact number to make a records/verification inquiry. It's a lookup aid for grounding aviation references, not a source of personal data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.kayak.com/airlines.
2. Find the carrier in the alphabetical list (or via your browser's in-page find).
3. Read the entry: airline name, two-letter IATA code, and a customer/contact phone number.
4. Use the IATA code to decode flight numbers/boarding passes and the phone number to reach the carrier directly.
5. Pivot: a decoded flight number + carrier feeds flight-tracking and schedule tools; the contact line supports a legitimate records inquiry to the airline.

## Inputs → Outputs
- **In:** airline name or IATA code (`employer-org`)
- **Out:** airline name, IATA code, and contact `phone`
- **Empty/negative result looks like:** a small/regional or defunct carrier not listed — cross-check with a dedicated IATA/ICAO airline code database instead.

## Gotchas & OpSec
- **Thin data:** the page gives only name, code and phone — no routes, hubs or fleet detail despite older descriptions; use an aviation database for those.
- It's a commercial travel site; expect marketing/booking links around the directory.
- OpSec: **passive** — a static reference, no target interaction.

## Overlaps ("do both")
- Pairs with `[[kayak-travel-search-engine]]` and dedicated flight-tracking/airline-code databases — this resolves the carrier identity; those handle routes, schedules and live tracking.

## Trust & verifiability
`trust: unverified` — a convenience directory on a commercial travel site. Codes and contact numbers are generally reliable but confirm a critical airline code against an authoritative IATA/ICAO source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kayak-airlines-search-engine |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | employer-org → phone |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
