---
id: wiman
name: Wiman
description: Use when you have a `geolocation` and want the free public WiFi hotspots there — returns a map of crowdsourced hotspot locations (and sometimes shared network names/passwords).
url: https://www.wiman.me/
category: geolocation
path:
- geolocation
bestFor: Mapping crowdsourced free WiFi hotspots around a location, including community-shared network names.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- device-id
status: live
pricing: freemium
costNote: Free to browse the hotspot map/site; the mobile app is free (ad/community-supported). No payment to view locations.
opsec: passive
opsecNote: Browsing the hotspot map queries only Wiman's own crowdsourced database — no subject is contacted. Note the reverse risk: if you (or a target) ran the Wiman app, your device may have contributed hotspot/location data to this very database, so treat it as a source that can expose device presence at a place.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowdsourced database of 60M+ hotspots; coverage and accuracy vary by area and entries can be stale or user-mislabelled.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Wiman WiFi
- wiman.me
tags:
- wifi
- hotspots
- crowdsourced
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# Wiman

> A crowdsourced world map of free WiFi hotspots — 60M+ community-contributed networks browsable by location.

## When to use
You have a `geolocation` and want to know the public WiFi landscape there: where free hotspots are, which venues offer them, and sometimes the shared network name/SSID. In OSINT this gives location context — plausible places a person with only WiFi could get online, corroboration of a venue's connectivity, or SSID leads that map to specific businesses. It's an environment/context tool, not a people-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.wiman.me/ and navigate to your country/city (URLs like `/united-states/free-wifi-miami` drill into cities).
2. Browse the map/list of hotspots; each pin is a crowdsourced free-WiFi location.
3. Read the venue name, address, and (where shared) the network name — an SSID can tie a hotspot to a specific business (`device-id`-style network identity).
4. Pivot: a hotspot's venue feeds place-based research; an SSID pattern can be cross-referenced with WiFi-geolocation databases (e.g. WiGLE).

## Inputs → Outputs
- **In:** `geolocation` (area/city)
- **Out:** `geolocation` (hotspot pins/venues) and network `device-id`/SSID hints
- **Empty/negative result looks like:** sparse or no pins — thin crowdsourced coverage for that area, not proof no WiFi exists; corroborate with another WiFi map.

## Gotchas & OpSec
- Crowdsourced = uneven: dense in some cities, near-empty elsewhere; entries can be outdated or user-mislabelled.
- Reverse-exposure caveat: the Wiman *app* contributes users' location/hotspot data to this database — relevant both as a source and as a privacy risk to note.
- OpSec: browsing is passive; no login needed for the web map.

## Overlaps ("do both")
- Pairs with `[[wigle-net]]`-style WiFi-geolocation databases: Wiman maps free public hotspots and venues, while WiGLE geolocates specific BSSIDs/SSIDs — do both to move between "what WiFi is near here" and "where is this exact network."

## Trust & verifiability
`trust: community` — a large but crowdsourced dataset; individual pins are user-submitted and unverified, so confirm any venue/SSID lead against the business itself or a second WiFi database.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wiman |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation, device-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
