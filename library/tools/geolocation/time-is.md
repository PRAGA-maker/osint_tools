---
id: time-is
name: time.is
description: Use when you have a `geolocation` (a city, place, or timezone) and want the exact current local time, UTC offset, and DST state there — returns time/timezone context you can use to reason about photo timestamps, alibis, or when a subject is likely awake.
url: https://time.is/
category: geolocation
path:
- geolocation
bestFor: Getting the exact local time, UTC offset, and DST status for any city or timezone in the world.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free with ads; an optional paid ad-free tier exists. No account needed for any lookup.
opsec: passive
opsecNote: You query time.is, never the subject or their infrastructure. Nothing about your lookup reaches the target. Safe to run without a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, widely-cited atomic-clock reference site; time/offset data is authoritative and independently checkable against any other clock source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- time.is
- Time.is exact time
tags:
- timezones
- Time Zones & Converters
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# time.is

> Atomic-clock reference for the exact current local time, UTC offset, and DST state of any place on earth — a small but essential piece of temporal-context tooling.

## When to use
You have a `geolocation` (a city name, a country, or a timezone) and need to anchor a piece of evidence in time. Typical cases: you have a photo or message with a local timestamp and want to convert it to UTC (or to your own timezone) to check it against other events; you want to know whether it is currently daytime/night where a subject lives before attempting a call-back or a live check; or you are reconstructing a timeline across countries and need each location's correct UTC offset and daylight-saving state on a given date.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://time.is/.
2. Type a city, country, or timezone into the search box (e.g. `Manila`, `America/Denver`) and submit — or append it to the URL, e.g. `https://time.is/Manila`.
3. Read the result: the large clock shows the exact current local time; below it the page states the UTC offset, the timezone abbreviation, whether DST is in effect, and sunrise/sunset for that location today.
4. To compare two places, use `https://time.is/compare/` or the "Time in X vs Y" links to see the offset between them directly.
5. Pivot: use the confirmed offset to normalise a timestamp to UTC before correlating it with EXIF times or other event logs.

## Inputs → Outputs
- **In:** `geolocation` (city / country / timezone)
- **Out:** `geolocation`-anchored time context — exact local time, UTC offset, timezone name, DST flag, sunrise/sunset
- **Empty/negative result looks like:** an ambiguous or misspelled place returns a disambiguation list or a "not found"; pick the correct entry rather than assuming the first hit is right.

## Gotchas & OpSec
- Human-in-the-loop: none — it is a direct, no-login lookup.
- OpSec: fully **passive**; the subject cannot see that you checked the time in their location.
- Historical dates: the front page shows *current* time. For DST state on a past date (which shifts the offset by an hour), verify against the timezone's DST calendar rather than assuming today's offset held then.

## Overlaps ("do both")
- Pairs with EXIF/metadata readers because those give you a *local* capture timestamp with an unknown zone; time.is turns the subject's `geolocation` into the offset you need to convert that timestamp to UTC and place it on a shared timeline.

## Trust & verifiability
`trust: trusted` — time.is is a long-established atomic-clock service; its offsets and DST flags are standard IANA timezone data and can be cross-checked against any other clock, so there is no data-quality risk.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | time-is |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
