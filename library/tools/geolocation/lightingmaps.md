---
id: lightingmaps
name: LightningMaps
description: Use when you have an `image`/video showing a storm or a claimed time+place and want to verify lightning activity there and then — returns real-time and historical strike data for chronolocation.
url: https://www.lightningmaps.org/
category: geolocation
path:
- geolocation
bestFor: Corroborating or debunking the time and place of storm imagery via real-time and archived lightning-strike data.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free access to the live map; historical archive access is free with an account, with some advanced features reserved for contributors.
opsec: passive
opsecNote: Reading a public lightning map discloses nothing about your subject — you're checking weather data, not touching them. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Powered by the Blitzortung.org community lightning-detection network — well-regarded, crowd-run sensor data used widely for storm tracking.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- lightningmaps.org
- Blitzortung map
tags:
- Maps, Geolocation and Transport
- Nature
- chronolocation
- weather
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# LightningMaps

> A live and historical lightning-strike map (Blitzortung network) — a chronolocation tool for confirming whether a storm really happened at a claimed time and place.

## When to use
You have a photo or video showing lightning/a thunderstorm, or a claim that "it was storming here at this time," and you want to verify it. Lightning is precisely timestamped and geolocated by the Blitzortung sensor network, so it's a strong chronolocation check: if the archive shows strikes at that location and time, the claim holds; if the sky was clear, the imagery is misdated or misplaced.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.lightningmaps.org/.
2. For live events, watch the real-time map at the candidate `geolocation`.
3. For a past event, use the historical archive (free account) and set the date/time and location.
4. Check whether strikes are recorded at that place and time; note density and timing.
5. Pivot: a confirmed storm supports the imagery's claimed place/time; a mismatch flags it as misattributed — feed the corroborated `geolocation`/timestamp into your timeline.

## Inputs → Outputs
- **In:** a candidate `geolocation` + a time (from an `image`/claim)
- **Out:** presence/absence of lightning strikes at that place and time (`geolocation`-anchored corroboration)
- **Empty/negative result looks like:** no strikes recorded — either there was no lightning (claim suspect) OR the area/time is outside sensor coverage; check network density before ruling it out.

## Gotchas & OpSec
- Lightning ≠ all storms: rain without lightning leaves no trace here — absence of strikes doesn't prove no weather event.
- Coverage/density varies by region and by how far back the archive goes; sparse-sensor areas are less reliable.
- Timestamps are precise — exploit that for tight chronolocation.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with historical-weather archives and satellite cloud imagery — lightning gives precise strike timing, while those confirm broader cloud/precipitation conditions for the same place and time.

## Trust & verifiability
`trust: trusted` — built on the Blitzortung community sensor network, widely used and cross-checkable against official weather records; accuracy is bounded by regional sensor density.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lightingmaps |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
