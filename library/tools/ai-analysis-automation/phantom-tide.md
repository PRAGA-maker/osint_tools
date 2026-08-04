---
id: phantom-tide
name: Phantom Tide
description: Use when you have a `geolocation` or maritime/air area of interest and want to see where vessel, aircraft and signal activity converge — returns scored convergence zones, geolocation and source-attributed intel from open AIS/ADS-B/thermal feeds.
url: https://github.com/tg12/phantomtide
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Fast maritime/airspace situational triage — surfacing where multiple open signals overlap in an area.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- vehicle-plate
status: live
pricing: freemium
costNote: Free to use via the public hosted instance; only public docs and a limited API are open-source (the full application is proprietary).
opsec: passive
opsecNote: You query a hosted analytics platform over open signal feeds; you are not touching any target, but your queries and areas of interest are seen by the hosted service. For sensitive work, prefer the self-host/local API stack over the public instance.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single-maintainer project (tg12); the ranking/analytics are useful but the core app is closed-source, so outputs can't be fully audited.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- phantomtide
tags:
- geoint
- maritime
- airspace
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Phantom Tide

> A geospatial OSINT dashboard that fuses open maritime and airspace signals (AIS, ADS-B, DSC, thermal) and ranks where they converge, so an analyst sees "what deserves attention right now."

## When to use
You have a `geolocation` / area of interest at sea or in the air (a search area, a last-known maritime position, an incident zone) and want a quick read on anomalous or converging activity — overlapping vessel tracks, aircraft, distress comms and thermal detections — rather than reading each feed separately. Situational GEOINT, not person-lookup, so its missing-persons value is indirect (e.g. narrowing a maritime search area).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the public instance (linked from the repo, `phantom.labs.jamessawyer.co.uk`) or stand up the documented Docker Compose stack for the public API locally.
2. Navigate to your area of interest on the map.
3. Read the scored convergence heatmap — zones where multiple sources overlap are ranked highest.
4. Inspect detail panels for source attribution and data freshness; save evidence into the Analyst Notebook.
5. Pivot: a flagged vessel/aircraft gives an identifier (`vehicle`/callsign) and `geolocation` to chase in dedicated AIS/ADS-B trackers.

## Inputs → Outputs
- **In:** `geolocation` / bounded area of interest.
- **Out:** scored convergence zones, `geolocation` of overlapping activity, intel tables (advisories/NOTAMs), and per-source attribution with freshness.
- **Empty/negative result looks like:** a cold heatmap / empty intel tables for the area — genuinely low activity, or feed gaps in that region.

## Gotchas & OpSec
- The core application is **proprietary** — only docs and a limited public API are open; you can't fully audit how convergence is scored.
- Data freshness varies by feed and region; always check the freshness indicators before acting.
- The public instance sees your areas of interest — self-host the API stack for sensitive searches.

## Overlaps ("do both")
- Complements broad geospatial aggregators like `[[shadowbroker]]` — Phantom Tide focuses on maritime/airspace convergence scoring; cross-check flagged tracks in a dedicated vessel/aircraft tracker.

## Trust & verifiability
`trust: community` — a capable single-maintainer project, but the closed core means you should verify any flagged activity against the raw AIS/ADS-B source rather than relying on the convergence score alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phantom-tide |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | geolocation → geolocation, vehicle-plate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
