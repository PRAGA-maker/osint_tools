---
id: skyscanner
name: Skyscanner
description: Use when you have an origin/destination and dates and want to know which flights, routes, and airlines connect them — returns schedules, carriers, durations, and prices to test whether a claimed journey is feasible.
url: https://www.skyscanner.com/
category: transportation
path:
- transportation
bestFor: Checking which air routes and carriers link two places on given dates, to assess the feasibility of a travel claim or plan a search.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to search flights, routes, and schedules; Skyscanner earns via booking referrals, not from you. No account needed to browse.
opsec: passive
opsecNote: You search public flight availability by route/date — nothing about your subject is entered or disclosed. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-established mainstream flight metasearch aggregating airline and OTA data; route/schedule information is drawn from carriers, so it's reliable for what flies where.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- skyscanner.com
- Skyscanner flights
tags:
- flights
- travel
- transportation
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- skyscanner-travel-search-engine
---

# Skyscanner

> A flight metasearch — see which routes, airlines, and schedules connect two places, to test whether a travel account holds up.

## When to use
You have an origin and destination (`geolocation`) and a date, and you need to know the air-travel reality: is there a direct flight, which carriers fly it, how long it takes, what it costs, and what connections exist. Useful for checking whether a subject's claimed itinerary is even possible ("flew Manchester→Bali that morning"), narrowing likely routes/airports someone would have used, or scoping travel options during a search window.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.skyscanner.com/.
2. Enter origin, destination, and date(s); use "Everywhere" as a destination to see where a budget/route reaches from a given airport.
3. Read the results: carriers, direct vs connecting, durations, typical prices, and which airports are used.
4. Use the flexible-date/month view to see how availability and price shift around a date.
5. Pivot: identified airports/carriers feed flight-tracking (`[[flightaware]]`-style) for actual movements; route feasibility informs which border/transit points to check.

## Inputs → Outputs
- **In:** origin + destination (`geolocation`/airports) + date
- **Out:** `geolocation`-anchored route options — airlines, schedules, durations, connections, indicative prices
- **Empty/negative result looks like:** "no results" for a pair/date means no bookable itinerary was found then (seasonal route, sold out, or no service) — it shows *bookable availability now*, not a definitive history of what flew on a past date; don't read it as proof no flight ever existed.

## Gotchas & OpSec
- Human-in-the-loop: none.
- It reflects *current bookable* flights, not historical operated flights — for what actually flew on a past date, use a flight-tracking/history service.
- Prices and availability are live and volatile; treat a specific fare as a snapshot, and confirm a schedule against the airline for anything decisive.

## Overlaps ("do both")
- Pairs with a flight-tracker (`[[flightradar24]]`/`[[flightaware]]`) — Skyscanner shows what routes *can* be booked; the trackers show what aircraft actually flew and when.

## Trust & verifiability
`trust: trusted` — a mainstream aggregator sourcing schedules from carriers/OTAs; route and schedule data is reliable, with the caveat that it reflects current bookable inventory rather than historical operations.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | skyscanner |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
