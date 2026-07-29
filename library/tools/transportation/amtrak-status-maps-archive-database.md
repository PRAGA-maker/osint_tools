---
id: amtrak-status-maps-archive-database
name: Amtrak Status Maps Archive Database
description: Use when you have an Amtrak train/station and a past date and want the actual historical arrival/departure times — returns geolocation.
url: https://juckins.net/amtrak_status/archive/html/history.php
category: transportation
path:
- transportation
bestFor: Looking up historical Amtrak arrival/departure times at a station for a past date (data since 2008).
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free community-run archive; no account or payment.
opsec: passive
opsecNote: Passive — querying a historical database; nothing touches any subject and no query is tied to a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running community-maintained archive that has scraped and stored Amtrak status data since 2008; reliable in practice but unofficial (not Amtrak).
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- ASMAD
- Amtrak Status Maps Archive
- juckins Amtrak status
tags:
- Maps, Geolocation and Transport
- Railway
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Amtrak Status Maps Archive Database

> A community archive of Amtrak train status going back to 2008 — look up what time a specific train actually reached a station on a date years in the past, to verify or break a travel timeline.

## When to use
A subject (or account) claims to have taken a particular Amtrak train, or you need to know when a train actually arrived/departed a U.S. station on a **past date**. ASMAD stores historical scheduled-vs-actual status, so you can confirm whether that train ran, its real times, and delays — anchoring a movement timeline between two `geolocation`s the way BTS does for flights.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://juckins.net/amtrak_status/archive/html/history.php.
2. Select the train number and/or station, and the date (or date range) since 2008.
3. Submit and read the returned status: scheduled vs actual arrival/departure and delay for that train at that station.
4. Pivot: a confirmed/denied train run anchors a timeline; station codes tie to `geolocation`; combine with `[[transtats-bts-gov]]` if the itinerary mixed rail and air.

## Inputs → Outputs
- **In:** an Amtrak train number and/or station `geolocation`, plus a past date
- **Out:** historical scheduled vs actual arrival/departure times and delay at that station `geolocation`
- **Empty/negative result looks like:** no record for that train/station/date — the train didn't run as described, or it's outside the archive's coverage (absence isn't proof a person didn't travel).

## Gotchas & OpSec
- No login; free and public.
- **Unofficial** and scraped — reliable in practice but not an Amtrak system of record; note that when using it evidentially.
- It's operational status data, not a passenger manifest — it establishes the train, never who was aboard.

## Overlaps ("do both")
- Pairs with `[[transtats-bts-gov]]` — ASMAD covers U.S. rail while BTS covers U.S. domestic flights; between them you can reconstruct a mixed rail/air timeline.

## Trust & verifiability
`trust: community` — a hobbyist-maintained archive with a strong track record; corroborate any evidentially-critical time against a second source where possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amtrak-status-maps-archive-database |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
