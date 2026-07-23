---
id: zugfinder
name: ZugFinder
description: Use when you have a train number/route/station and want live position and delay history — returns real-time train location, delays, and historical punctuality.
url: https://www.zugfinder.net/en/start
category: transportation
path:
- transportation
bestFor: Live tracking and historical delay/position data for long-distance trains across Germany and neighbouring European countries.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free for live tracking and ~30 days of delay history. "Zugfinder Pro" (paid) unlocks up to 2 years of historical data.
opsec: passive
opsecNote: You read a public train-tracking site; nothing identifies who you're researching and no target is contacted. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent European rail-tracking site fed by public timetable/positioning data; not an official operator source but well-established.
missingPersonsRelevance: low
coverage:
- de
- at
- it
- dk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- zugfinder.net
- Zugfinder Pro
tags:
- railway
- transport
- train-tracking
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# ZugFinder

> Live positions and delay records for European long-distance trains — useful for placing a specific train (and anyone on it) in time and space.

## When to use
You have a train number, route, station, or a `geolocation`/time you're trying to corroborate, and you want to know where a long-distance train actually was, or how a service historically runs. ZugFinder tracks real-time positions and keeps delay/punctuality history across Germany, Austria, BeNeLux, Italy, Denmark, and Slovenia. In an investigation it helps verify travel claims, reconstruct a timeline, or check whether a train was where someone said. Direct missing-persons relevance is low (timeline/alibi corroboration involving rail travel).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.zugfinder.net/en/start (English interface available).
2. Search by:
   - **Train number** — for a specific service's live position and delay detail.
   - **Station** — for live arrivals/departures and historical arrival tables.
   - **Region map** — to see current long-distance train positions.
3. Read live position, current delay, cancellations, and the ~30-day delay history (2 years with Pro).
4. Pivot: a confirmed train time/position anchors a `geolocation`+time in a timeline; combine with station CCTV/records requests or other transport data for the same window.

## Inputs → Outputs
- **In:** train number / station / route (a `geolocation` context)
- **Out:** live train position, delay/cancellation status, historical punctuality (a `geolocation`+time record)
- **Empty/negative result looks like:** no data for a train/route — it's outside the covered countries/network (regional/local services and non-covered countries won't appear), or the historical window exceeds the free tier.

## Gotchas & OpSec
- Scope is **long-distance** trains in a set of Central European countries — regional/commuter services and other regions are largely absent.
- Free history is limited to ~30 days; deeper history is a paid feature.
- It's a third-party aggregator, not the official operator record — treat as strong corroboration, not legal proof.
- OpSec: passive public browsing.

## Overlaps ("do both")
- Complements official operator sites (Deutsche Bahn) and other transport-tracking tools — ZugFinder's strength is its retained delay/position *history* for reconstructing past events, where live-only official tools fall short.

## Trust & verifiability
`trust: community` — a well-established independent tracker built on public data; reliable for what it covers, but confirm anything critical against the operator's own records given its aggregator status and regional scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zugfinder |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
