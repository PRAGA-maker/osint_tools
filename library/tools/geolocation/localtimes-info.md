---
id: localtimes-info
name: localtimes.info
description: Use when you have a `geolocation` (city/country) and want its current local time and UTC offset shown on a world map — returns the local wall-clock time and zone for that place.
url: https://localtimes.info/
category: geolocation
path:
- geolocation
bestFor: A fast visual world-clock read of the current local time and offset for a city or country.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free world-clock/time-zone map. No account, no payment.
opsec: passive
opsecNote: You look up a place's local time; nothing about your subject is disclosed. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A consumer world-clock site; zone/offset values follow the standard tz database and are checkable against any other clock.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- localtimes.info
- Local Times world clock
tags:
- timezones
- Time Zones & Converters
- world-clock
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# localtimes.info

> A world-clock map for reading the current local time and UTC offset of a city or country at a glance.

## When to use
You have a `geolocation` and need the current local time and time-zone offset there — to sanity-check when a subject in that place is likely awake/online, to translate a "posted at" timestamp into their local wall-clock, or to compare the time difference between two locations. It's a quick visual clock; for converting a *specific past* instant with DST handling, a converter like `[[24timezones-com]]` is more precise.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://localtimes.info/.
2. Find the city/country on the world map or list.
3. Read the current local time and UTC offset shown for that location.
4. For a past date, remember this shows *current* time — apply the offset carefully and check whether DST was in effect then (or use a dated converter).
5. Pivot: combine with an epoch decoder (`[[epochconverter-io]]`) and a dated converter to turn a raw timestamp into the subject's local time.

## Inputs → Outputs
- **In:** `geolocation` (city/country)
- **Out:** current local time and UTC offset for that place
- **Empty/negative result looks like:** small towns may only resolve to the nearest listed city in the same zone — pick a same-zone reference rather than assuming no data.

## Gotchas & OpSec
- Human-in-the-loop: none.
- Shows *current* local time; it is not a historical-date converter — for a past event use a tool that applies the correct DST rule for that date.
- Confirm the zone against the IANA tz database for anything legal-grade.

## Overlaps ("do both")
- Pairs with `[[24timezones-com]]` and `[[epochconverter-io]]` — this gives a quick current-time read; those handle dated conversion and raw-timestamp decoding.

## Trust & verifiability
`trust: community` — a consumer world-clock running on standard tz data; every value is independently verifiable, so trust the (checkable) data over the operator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | localtimes-info |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
