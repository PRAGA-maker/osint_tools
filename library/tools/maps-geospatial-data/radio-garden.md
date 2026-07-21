---
id: radio-garden
name: Radio Garden
description: Use when you have a `geolocation` and want to hear its local live radio — returns location-linked broadcast audio for cultural/language context and chronolocation cues.
url: https://radio.garden
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Listening to live local radio at a specific place on a spinnable globe — useful for language, cultural, and time-of-day context.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to use in-browser; no account. Ad-free listening.
opsec: passive
opsecNote: You listen to a public radio stream selected on a map; nothing is sent to any target. Fully passive. The stream is a third-party broadcast; use a VPN if you want the listening off your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known cultural project mapping thousands of live radio streams to their broadcast locations. Reliable as a listening tool; station geolocation is approximate to the broadcaster's city.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- radio.garden
tags:
- maps
- radio
- geolocation
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Radio Garden

> A spinnable globe of live radio — click any dot to hear what a place is broadcasting right now, mapping location to local sound.

## When to use
You have a `geolocation` and want the ambient, local-media context of that place: what language/dialect is on air, which local stations exist, cultural cues, and time-of-day signals (local news bulletins, ad content, weather/traffic reports that reference nearby places). Niche but genuinely useful for chronolocation and localisation — a station's live local news or a call-in can confirm timezone, weather, or an unfolding local event, and hearing a region's stations helps interpret audio in a video tied there.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://radio.garden and rotate/zoom the globe to your area of interest (or use search).
2. Click a green dot to play that city's live station; browse the multiple stations available for a location.
3. Listen for language/dialect, station IDs, local news/weather/traffic bulletins, and advert content that names nearby businesses or places.
4. Use those cues to confirm timezone/time-of-day, weather, or local events for chronolocation.
5. Pivot: a station ID or named local place feeds mapping/streetview tools; language/dialect narrows a region for other searches.

## Inputs → Outputs
- **In:** `geolocation` (place of interest)
- **Out:** `geolocation` context (local live audio: language, station IDs, local bulletins)
- **Empty/negative result looks like:** no dot/station near your exact point — coverage is by broadcast city, so remote areas may have none; pick the nearest covered city.

## Gotchas & OpSec
- Station geolocation is to the broadcaster's city, which may differ from a transmitter's exact position — treat as approximate.
- It maps *broadcast* audio, not the subject — its value is ambient/contextual, not a direct locator of a person.
- Fully passive; you are just listening to public streams.

## Overlaps ("do both")
- Pairs with chronolocation workflows and webcam tools (`[[skyline-webcams]]`) — radio gives audible local-time/weather/event cues while webcams give the visual; together they tighten a "where and when."

## Trust & verifiability
`trust: community` — a reputable, long-standing project; the streams and their broadcast-city mapping are reliable, though station location is city-level and any locational inference from audio should be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radio-garden |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
