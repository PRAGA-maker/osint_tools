---
id: global-fishing-watch
name: Global Fishing Watch
description: Use when you have a vessel name/IMO/MMSI or an ocean area and want its movement, fishing, and port history — returns vessel tracks, port visits, and transshipment/encounter events.
url: https://globalfishingwatch.org/
category: transportation
path:
- transportation
- marine-records
bestFor: Tracking a specific fishing/carrier vessel's AIS movements, port visits, and at-sea encounters over time, worldwide and for free.
selectorsIn:
- vin
- geolocation
selectorsOut:
- geolocation
- vin
status: live
pricing: free
costNote: Free map viewer; a free account unlocks vessel history, analysis layers, and an API. No paid tier required for standard use.
opsec: passive
opsecNote: You query Global Fishing Watch's aggregated AIS/satellite data, never the vessel — nothing you do is visible to the ship or its operator. Advanced features and the API need a free registered account, so those queries are tied to your login; use a research account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Independent nonprofit (founded by Oceana, SkyTruth, and Google) publishing methodology openly; data comes from broadcast AIS plus satellite detection and is used by researchers, journalists, and enforcement agencies.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- globalfishingmap
aliases:
- GFW
tags:
- marine
- vessel-tracking
- ais
- arf-seed
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Global Fishing Watch

> A free, open map of global fishing and carrier-vessel activity — track a named vessel's AIS movements, port visits, and at-sea encounters, or watch an ocean area over time.

## When to use
Your case touches a vessel — a fishing boat, reefer, or carrier — identified by name, IMO, or MMSI, and you want its history: where it has been, which ports it visited, and which other ships it met at sea (transshipment/encounters). For maritime missing-persons, trafficking, or IUU-fishing work, this reconstructs a vessel's timeline and links it to ports and other vessels (`associate` boats). Also useful the other way: monitor an ocean `geolocation` to see what vessels operated there in a date window.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://globalfishingwatch.org/ and launch the Map (create a free account to unlock vessel history and analysis).
2. Search the vessel by name / IMO / MMSI, or pan to an ocean area of interest.
3. Set the date range and read the vessel's track: fishing-effort segments, `geolocation` waypoints, and speed.
4. Open the vessel profile for flag, gear type, registry/authorization records, port visits, and encounter/transshipment events with other vessels.
5. Cross-check identity against the vessel's IMO/MMSI (`vin`-equivalent maritime IDs) in registry layers.
6. Pivot: port visits → shoreside records and crew leads; encounter partners → other vessels/operators; a track gap ("AIS dark" period) → a lead worth explaining.

## Inputs → Outputs
- **In:** vessel name / IMO / MMSI (`vin`-style maritime identifier) or ocean `geolocation` + date range
- **Out:** vessel `geolocation` tracks, port visits, transshipment/encounter events, flag/gear/registry info
- **Empty/negative result looks like:** no track or a vessel that "goes dark" — the ship isn't broadcasting AIS (turned off, out of receiver range, or too small to be required); absence of signal is itself a finding, not proof of no activity.

## Gotchas & OpSec
- Depends on AIS: vessels can disable transponders or spoof positions, and small boats may not carry AIS — gaps and anomalies need interpretation, not literal reading.
- Human-in-the-loop: full vessel history and the API require a (free) account login.
- Fishing-effort is a model/inference layer, not ground truth — treat classifications as estimates.
- Fully passive toward the vessel.

## Overlaps ("do both")
- Pairs with `[[globalfishingmap]]` and general AIS trackers (e.g. MarineTraffic-style tools) — cross-check a vessel's identity and track on a second source, since AIS coverage and interpretation differ.

## Trust & verifiability
`trust: trusted` — a well-established nonprofit with an openly published methodology and data used by academics, journalists, and regulators; identifiers and tracks can be independently corroborated against vessel registries and other AIS providers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-fishing-watch |
| category | transportation |
| selectorsIn → selectorsOut | vin, geolocation → geolocation, vin |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
