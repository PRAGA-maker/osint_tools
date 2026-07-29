---
id: transtats-bts-gov
name: Transtats.bts.gov
description: Use when you have a U.S. flight (airline + number, or route + date) and want its actual historical departure/arrival times and delays — returns geolocation.
url: https://transtats.bts.gov/ONTIME/
category: transportation
path:
- transportation
bestFor: Verifying whether a specific U.S. domestic flight operated and its real departure/arrival times.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public U.S. government (Bureau of Transportation Statistics) data; no account or payment.
opsec: passive
opsecNote: Passive — you query a government statistics database; nothing touches the subject and no query is tied to a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official U.S. DOT Bureau of Transportation Statistics data covering the largest U.S. carriers — authoritative for U.S. domestic flight performance.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- BTS TranStats
- TranStats On-Time
tags:
- Maps, Geolocation and Transport
- Aviation
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Transtats.bts.gov

> The U.S. government's on-time flight performance database — decades of actual (not just scheduled) departure and arrival times for U.S. domestic flights, useful for checking a claimed travel timeline against reality.

## When to use
A subject (or a witness account) claims to have been on a particular U.S. flight, or you need to establish when a flight on a given route/date actually departed and arrived. TranStats On-Time lets you confirm **whether that flight operated, was delayed, cancelled, or diverted**, and its real wheels-off/wheels-on times — a concrete way to corroborate or break a stated timeline of movement between two `geolocation`s.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://transtats.bts.gov/ONTIME/ (the On-Time performance query interface).
2. Specify the parameters: airline, flight number, origin/destination airport, and date range.
3. Run the query and read the returned record: scheduled vs actual departure/arrival, departure delay, taxi/airborne times, and cancellation/diversion flags.
4. For bulk work, download the underlying monthly datasets from the wider TranStats site.
5. Pivot: a confirmed/denied flight anchors a movement timeline; airport codes tie to `geolocation`; cross-reference with public flight trackers for the tail number.

## Inputs → Outputs
- **In:** a flight identity — airline + flight number, or origin/destination `geolocation` + date
- **Out:** actual departure/arrival times, delays, cancellation/diversion status for that flight between two `geolocation`s
- **Empty/negative result looks like:** no record for that airline/number/date — the flight didn't operate as described, or it was on a carrier/route outside the covered U.S. domestic set (international and small carriers aren't fully covered).

## Gotchas & OpSec
- No login; fully public.
- Coverage is **U.S. domestic** flights of the larger carriers — it will not have international legs or small regional operators, so absence isn't proof a person didn't fly.
- The data is aggregate flight performance, not passenger manifests — it tells you the flight, never who was on it.

## Overlaps ("do both")
- Pairs with live flight-tracking/history services (tail-number trackers) — those give the specific aircraft's track, while BTS gives the authoritative scheduled-vs-actual performance record.

## Trust & verifiability
`trust: trusted` — first-party U.S. Bureau of Transportation Statistics data; it is the source of record for U.S. domestic flight performance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | transtats-bts-gov |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
