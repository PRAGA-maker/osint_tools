---
id: ais-boatnerd-com
name: Ais.boatnerd.com
description: Use when you have a Great Lakes vessel name/identifier and want its live position and track — returns real-time AIS `geolocation` for ships on the Great Lakes and connecting waterways.
url: https://ais.boatnerd.com/
category: transportation
path:
- transportation
bestFor: Live AIS tracking of commercial vessels on the North American Great Lakes / St. Lawrence Seaway, with a community focus that fills gaps global trackers miss.
selectorsIn: []
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free community map run by BoatNerd (Great Lakes shipping enthusiasts); no account needed to view.
opsec: passive
opsecNote: Purely a read-only map fed by publicly broadcast AIS transponder data — you disclose nothing about any subject, and only your own visit to BoatNerd is logged. Positions come straight from the ships' own AIS broadcasts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by BoatNerd.com, a long-running Great Lakes shipping community, using volunteer/regional AIS receivers — reliable for the Lakes but coverage is regional, not global.
missingPersonsRelevance: low
coverage:
- us
- ca
relatedTools:
- boatnerd-great-lakes-shipping
- marinetraffic
- vesselfinder
auth: none
api: false
localInstall: false
registration: false
aliases:
- BoatNerd AIS map
- boatnerd vessel tracker
tags:
- ais
- vessel-tracking
- great-lakes
- maritime
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Ais.boatnerd.com

> BoatNerd's live AIS map for the Great Lakes and St. Lawrence Seaway — a regional maritime tracker that often shows Lakes freighters more completely than the big global services.

## When to use
Your investigation touches a vessel on the North American Great Lakes or the St. Lawrence Seaway (a freighter, tug, ferry, or the person known to be aboard/employed on it) and you want its current position, heading, speed, and recent track. BoatNerd's regional AIS receiver network frequently has stronger inland-Lakes coverage than MarineTraffic/VesselFinder, so it's the right first stop for Lakes shipping specifically.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ais.boatnerd.com/ — the map loads showing vessels currently broadcasting AIS on the Lakes.
2. Find your vessel: use the search/vessel list to locate it by name, or click its icon on the map.
3. Read the details panel — position (`geolocation`), speed, course, destination, and vessel particulars (type, flag, IMO/MMSI where shown).
4. Follow the track to see where it's been and is heading; correlate with port schedules.
5. Pivot: take the vessel's name/IMO/MMSI to `[[marinetraffic]]` or `[[vesselfinder]]` for global history and photos, and to a vessel-registry lookup for ownership/crew leads.

## Inputs → Outputs
- **In:** a Great Lakes vessel name / MMSI / IMO (selected on the map — there's no formal input field for other selectors).
- **Out:** live `geolocation` (position, course, speed), plus vessel particulars and recent track.
- **Empty/negative result looks like:** the vessel isn't on the map — it may be out of the Lakes region, in port with its transponder off, or simply not covered by BoatNerd's receivers. Absence is not proof it isn't sailing; check a global tracker.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — AIS is publicly broadcast by the ships themselves; viewing the map reveals nothing about you or your subject.
- Coverage is **regional**: excellent on the Lakes/Seaway, sparse or blank elsewhere. AIS can also be switched off or (rarely) spoofed, so treat a position as "last broadcast," not guaranteed truth.

## Overlaps ("do both")
- Pairs with `[[boatnerd-great-lakes-shipping]]` — the wider BoatNerd site adds vessel passages, boat-watching reports and news that contextualize a live position.
- Overlaps with `[[marinetraffic]]` and `[[vesselfinder]]` — use those for global coverage, historical tracks, and photos; use BoatNerd for the best live Lakes picture.

## Trust & verifiability
`trust: community` — a respected volunteer Great Lakes shipping community running regional AIS receivers. Positions are the ships' own broadcasts (verifiable), but coverage is limited to the Lakes region.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ais-boatnerd-com |
| category | transportation |
| selectorsIn → selectorsOut | — → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
