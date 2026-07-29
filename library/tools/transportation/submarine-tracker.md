---
id: submarine-tracker
name: Submarine Tracker
description: Use when you have a vessel `name`/hull and want the last-known AIS position of submarines and naval vessels on a live map — returns geolocation.
url: https://www.marinevesseltraffic.com/submarine-vessels-tracking-map
category: transportation
path:
- transportation
bestFor: Locating the last-known AIS position of submarines and naval vessels on a live map.
selectorsIn:
- name
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free live AIS map; deeper history and features on the wider MarineVesselTraffic/MarineTraffic ecosystem may require payment.
opsec: passive
opsecNote: Passive — you read public AIS broadcasts; no vessel is contacted. Note that most military submarines run AIS dark, so a blank map is expected, not evidence of absence.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party AIS aggregator; positions are only as current and complete as vessels choose to transmit, and naval vessels routinely suppress AIS.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Submarine Tracker
- MarineVesselTraffic submarines
tags:
- maritime
- ais
- vessel-tracking
source: osint4all
lastVerified: '2026-07-29'
relatedTools:
- military-ship-tracker
enrichment: full
---

# Submarine Tracker

> A live AIS map filtered to submarines and naval vessels — shows the last-broadcast position of any such vessel that is transmitting AIS.

## When to use
You have a vessel `name` or hull/pennant number (a research submersible, a tourist submarine, a naval vessel referenced in an investigation) and want its **last-known position and recent track**. It reads the public AIS feed and plots vessels on a world map with fleet lists by country and type. Best understood as "where was this vessel last seen broadcasting," not a real-time military intelligence feed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.marinevesseltraffic.com/submarine-vessels-tracking-map for the live submarine/naval map.
2. Search by vessel name or hull number, or browse the fleet lists (by country, type, class).
3. Read the vessel's last AIS position, timestamp, speed/course, and destination if reported.
4. Cross-check the same vessel on a second AIS site (MarineTraffic, VesselFinder) to confirm the last position.
5. Pivot: the position (`geolocation`) ties to a port/region for further ground-level OSINT; the vessel's declared destination narrows where it's headed.

## Inputs → Outputs
- **In:** vessel `name` or hull/pennant number
- **Out:** last-known AIS `geolocation` (map position + timestamp), speed/course, declared destination
- **Empty/negative result looks like:** no position, or a stale timestamp — the vessel is AIS-dark (normal for military submarines), out of receiver range, or transmitting under a different name.

## Gotchas & OpSec
- Passive; you're reading broadcast AIS, not pinging anything.
- **AIS is voluntary/spoofable for warships** — submarines usually transmit nothing while operational, so this tool mostly catches civilian/research subs and surfaced or in-port naval vessels. Never infer a vessel's true location from AIS silence.
- Coverage depends on terrestrial/satellite receiver reach; mid-ocean gaps are common.

## Overlaps ("do both")
- Pairs with `[[military-ship-tracker]]` and mainstream AIS trackers — running more than one aggregator catches receivers and vessels each one misses.

## Trust & verifiability
`trust: community` — a third-party AIS re-broadcaster; positions are as reliable as the vessel's own transmissions, which for naval/submarine targets are frequently absent or deliberately false. Corroborate before relying on any position.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | submarine-tracker |
| category | transportation |
| selectorsIn → selectorsOut | name → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
