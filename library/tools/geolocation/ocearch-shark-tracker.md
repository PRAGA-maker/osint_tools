---
id: ocearch-shark-tracker
name: OCEARCH Shark Tracker
description: Use when you want a worked example of live animal-telemetry mapping (tagged sharks/marine animals) — returns per-animal tracks; essentially no people-search value, useful mainly as an OSINT teaching/marine-context tool.
url: https://www.ocearch.org/tracker/
category: geolocation
path:
- geolocation
bestFor: Viewing live tracks of tagged sharks and marine animals on a world map — a marine-telemetry dataset, not a people-OSINT lookup.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public tracker from the OCEARCH research non-profit; no account required (paid tiers are for donations/support, not access).
opsec: passive
opsecNote: Fully passive — you view published marine-research telemetry; no person or target is involved. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by OCEARCH, a legitimate marine-research organisation; the tracking data is genuine scientific telemetry — reliable for what it is (animal movement), which is unrelated to investigating people.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OCEARCH tracker
- Shark Tracker
tags:
- Maps, Geolocation and Transport
- Nature
- telemetry
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# OCEARCH Shark Tracker

> A live map of tagged sharks and marine animals — legitimate marine-research telemetry with essentially no people-search value, worth knowing mainly as an example of open tracking data or for niche maritime context.

## When to use
Almost never for investigating people. Reach for it only in narrow situations: a marine/environmental research question, teaching how open telemetry/tracking datasets work, or corroborating marine-animal presence in an area at a time (e.g. context for a coastal incident). It takes a `geolocation`/animal and returns movement tracks — it does not touch human identifiers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ocearch.org/tracker/.
2. Browse the world map or pick a tagged animal to see its name, size, species, and travel log.
3. Filter by region/time to see which animals were tracked where and when.
4. Read a track as scientific telemetry — approximate ping locations, not precise real-time positions.
5. Pivot: none toward people; at most, marine-context data for an environmental/maritime question.

## Inputs → Outputs
- **In:** `geolocation` / an animal of interest
- **Out:** `geolocation` tracks (animal movement logs)
- **Empty/negative result looks like:** no tagged animals in your area/time window — expected, and it never returns anything about a person.

## Gotchas & OpSec
- Zero people-OSINT utility — do not mistake it for a human-tracking tool.
- Pings are approximate and delayed (satellite tag surfacing), not live GPS.
- OpSec: fully passive public science data.

## Overlaps ("do both")
- Complements other open-telemetry/AIS and mapping tools — those track vessels/assets, while OCEARCH tracks tagged wildlife; all are examples of public movement data rather than person lookups.

## Trust & verifiability
`trust: trusted` — a reputable research organisation publishing genuine telemetry; reliable for animal movement, and honestly of negligible relevance to investigating people.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ocearch-shark-tracker |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
