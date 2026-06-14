---
id: timeanddate
name: Timeanddate
description: Use when you need precise sunrise/sunset/twilight, timezone, or weather-history facts for a place and date to validate a photo's timestamp or a timeline.
url: https://www.timeanddate.com
category: geolocation
path:
- geolocation
bestFor: Looking up exact sunrise/sunset/twilight times, timezones, and historical day-length for a place and date.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free reference site; ad-supported, optional paid tier removes ads.
opsec: passive
opsecNote: A public reference lookup; you query the site, never the target. No target interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, well-regarded reference site for time/astronomy data; figures are computed and verifiable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- suncalc-2
aliases:
- timeanddate.com
tags:
- geolocation
- chronolocation
source: metaosint
lastVerified: ''
enrichment: full
---

# Timeanddate

> The standard reference for "what time was sunrise/sunset there that day, and what timezone applied" — the lookup half of shadow/timestamp chronolocation.

## When to use
You are validating a photo or testimony timeline. You have a `geolocation`/`address` and a date and need authoritative facts: was it light or dark, when did golden hour fall, what was the local timezone (and DST offset), and what was the weather that day. Use it alongside a sun-geometry tool to confirm or break a claimed `metadata-exif` timestamp.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.timeanddate.com.
2. Use the **Sun & Moon** calculator: enter the city/location and the date to get sunrise, sunset, civil/nautical/astronomical twilight, and day length.
3. Use the **Time Zones** section to confirm the location's UTC offset and DST status for that exact date — the usual source of timestamp errors.
4. Use the **Weather > Past Weather** archive to check conditions (clear/overcast) that would affect whether shadows are even possible.
5. Pivot: combine the sunrise/sunset window with shadow direction from [[suncalc-2]] to pin a time-of-day range.

## Inputs → Outputs
- **In:** `geolocation`/`address` + a date.
- **Out:** sunrise/sunset/twilight times, timezone/DST offset, historical weather (validates `metadata-exif` time; refines `geolocation` plausibility).
- **Empty/negative result looks like:** the claimed timestamp falls in darkness while the photo is clearly daylit (or vice-versa) — the timeline is wrong.

## Gotchas & OpSec
- No login or captcha; fully passive.
- Watch DST transitions and the difference between local time and the EXIF/device time zone — the most common analyst mistake.
- Past-weather coverage is good in populated areas but sparse for remote regions.

## Overlaps ("do both")
- Pairs with [[suncalc-2]]: timeanddate gives the exact times/tables, SunCalc gives the sun's compass direction for matching shadows.

## Trust & verifiability
`trust: trusted` — established, widely cited reference; astronomical values are deterministic and can be cross-checked against any ephemeris.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | timeanddate |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
