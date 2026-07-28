---
id: rasp-yandex-ru-map-trains
name: Rasp.yandex.ru/map/trains
description: Use when you have a `geolocation`/region in Russia, Belarus, Ukraine, Kazakhstan or Abkhazia and want live train positions and rail schedules — returns live train `geolocation`.
url: https://rasp.yandex.ru/map/trains
category: transportation
path:
- transportation
bestFor: Yandex's live rail map for Russia and neighbouring CIS countries.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to browse; no Yandex account required to view the map.
opsec: passive
opsecNote: Passive to any subject, but this is a Russian service — Yandex logs your IP. For sensitive Russia/CIS investigations use a sock-puppet/VPN session and do NOT log into a Yandex account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by Yandex; authoritative for CIS rail schedules and positions, but it is a Russian commercial service and should be treated with the corresponding OpSec caution.
missingPersonsRelevance: low
coverage:
- ru
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wordstat-yandex-ru
- yandex-people-search
aliases:
- Yandex Trains Map
- Yandex Rasp trains
tags:
- Maps, Geolocation and Transport
- Railway
- transit
- russia
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Rasp.yandex.ru/map/trains

> Yandex's live rail map — the strongest live-train coverage for Russia and the surrounding CIS region, where Western trackers go blank.

## When to use
Your case has a rail angle inside Russia, Belarus, Ukraine, Kazakhstan, or Abkhazia and you want live/scheduled train movements and station timetables — to place a subject relative to a station, understand what service ran at a time and place, or build a transit-based timeline. This is the go-to where Western live-train maps have no coverage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://rasp.yandex.ru/map/trains (from a sock-puppet/VPN session — see OpSec).
2. Pan/zoom the map to your region; moving markers are trains, and stations show schedule data.
3. Click a train for its route/schedule; click a station for departures/arrivals.
4. Cross-check station timetables in Yandex Raspisaniya (schedules) for planned times.
5. Pivot: station/route context supports or challenges a timeline built from other `geolocation` evidence.

## Inputs → Outputs
- **In:** a `geolocation` / region (navigate the map)
- **Out:** live/scheduled train `geolocation`, routes, and station timetables
- **Empty/negative result looks like:** no trains shown in an area — outside covered networks or a data gap, not proof no service exists; verify against the operator's own schedule.

## Gotchas & OpSec
- **Russian service caution** — Yandex logs your visit; never access it from an attributable session for a sensitive investigation, and never authenticate.
- Coverage and live-position fidelity are strongest for main-line rail; regional/suburban detail varies.
- Interface is primarily in Russian — use browser translation as needed.

## Overlaps ("do both")
- Complements [[live-train-tracker]] (GeOps TRAVIC), which covers Europe/Americas/Australia — use Yandex for the CIS region those miss.

## Trust & verifiability
`trust: community` — authoritative CIS rail data from Yandex, but a foreign commercial platform: rely on it for coverage while keeping the OpSec caveats front of mind.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rasp-yandex-ru-map-trains |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
