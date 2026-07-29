---
id: radion-net
name: radio.net (Local Stations)
description: Use when you have a `geolocation` (or a station name heard in audio/video) and want to identify local radio stations there — a geolocation-corroboration aid that ties a broadcast to a place.
url: https://www.radio.net/local-stations
category: communities-forums
path:
- communities-forums
bestFor: Listing/streaming radio stations by location, to match a station heard in media to a region.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to browse and stream stations in-browser; a premium tier removes ads/adds features but isn't needed for lookup.
opsec: passive
opsecNote: Browsing/streaming station listings is passive and reveals nothing about a subject. Purely a reference/corroboration resource.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: radio.net is a large commercial radio-directory/streaming aggregator; station-to-location listings are generally reliable, but it's a directory, not an authoritative broadcast registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- radio.net
- Radion.net
tags:
- TV/Radio
- geolocation-aid
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# radio.net (Local Stations)

> A location-indexed radio directory and streamer — match a station heard in a clip to its city/region, or enumerate the stations broadcasting at a place.

## When to use
Audio or video evidence contains a radio broadcast — a station jingle, call sign, DJ, ad for a local business, or news bulletin — and you want to tie it to a location. radio.net lets you browse/stream stations by place, so you can identify the station heard and confirm the region, or work the other way: list what broadcasts near a known `geolocation` to anticipate what a local recording should sound like. A geolocation corroborator, not a person lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open radio.net/local-stations and browse by country/city, or search a station name/call sign heard in the media.
2. Stream candidate stations to compare jingles, DJ voices, ad reads, or news timing against your clip.
3. Confirm the match, which fixes the broadcast to that station's coverage area.
4. Pivot: the station's city/region tightens `geolocation`; local ads/news mentioned on-air are further place/date anchors.

## Inputs → Outputs
- **In:** a `geolocation`/place, or a station name/call sign heard in media
- **Out:** matching local stations (streamable) → a confirmed `geolocation` region
- **Empty/negative result looks like:** no matching station — it may be a small/unlisted local or internet-only station, or a non-broadcast source; not proof of the wrong region.

## Gotchas & OpSec
- Directory coverage skews to listed/streaming stations; tiny local or pirate stations may be absent — cross-check a national broadcast regulator's station list.
- Syndicated content and networked programming can play across many markets — match on **local** cues (ads, call signs, traffic/weather) not national shows.
- **Passive**: browsing/streaming reveals nothing about your subject.

## Overlaps ("do both")
- Pairs with other geolocation aids (`[[identify-plans]]`, mapping/satellite): the radio match narrows the region, the visual cues pin the exact spot.

## Trust & verifiability
`trust: unverified` — a large commercial directory, generally accurate for station/location but not an authoritative registry; confirm a critical match against a broadcast regulator's records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radion-net |
