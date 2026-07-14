---
id: aprs-on-google-maps
name: aprs.fi (APRS on Google Maps)
description: Use when you have an amateur-radio callsign or an area and want real-time/historic position tracks — returns map locations, movement history and station metadata.
url: https://aprs.fi/
category: geolocation
path:
- geolocation
bestFor: Tracking the live and historical map position of APRS stations (ham operators, vehicles, boats, weather stations) by callsign or area.
selectorsIn:
- username
- geolocation
selectorsOut:
- geolocation
- device-id
- name
status: live
pricing: free
costNote: Free to search and view on the web; no account needed. A registered account/API key unlocks the data API and some extras.
opsec: passive
opsecNote: You are reading data that APRS stations broadcast publicly over radio and the internet — querying aprs.fi does not touch or alert the operator. The site logs your access; use a VPN for sensitive work. Note the subject is the transmitter — if you track a specific callsign, you are watching a beacon the operator chose to broadcast.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-established, widely-used APRS aggregator fed by the global APRS-IS network; positions are as reported by the transmitting stations themselves.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- aprs.fi
- APRS on Google Maps
- APRS tracking
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- ham-radio
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# aprs.fi (APRS on Google Maps)

> A live map of the global APRS network — enter a ham-radio callsign (or pan to an area) to see where that station is and where it has been.

## When to use
Your subject is (or travels with) an amateur-radio operator, a vehicle/boat carrying an APRS tracker, or a weather station — anything transmitting APRS position beacons. If you have a `username` in the form of a callsign (optionally with an SSID like `-9` for a mobile unit), aprs.fi plots its current location and full movement history on a map. It is a niche but powerful geolocation source because the position data is broadcast openly and archived, giving you a timeline of exactly where a tracked station has been.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://aprs.fi/.
2. Enter the target **callsign** in the search box (try common SSIDs: base `-0`, mobile `-9`, etc.), or pan/zoom the map to an `geolocation`/area of interest.
3. Read the station's marker: current position, last-heard time, speed/heading, and station comment/metadata.
4. Open the track/history to see the route over time — this is the real intelligence: a movement timeline.
5. Pivot: the callsign feeds an FCC/national licence lookup to resolve the operator's `name` and licence address; positions feed mapping/geolocation work.

## Inputs → Outputs
- **In:** a `username`/callsign (with optional SSID), or a map `geolocation`/area to browse
- **Out:** `geolocation` (current + historical positions/track), station `device-id`/callsign metadata, and — via a licence lookup pivot — the operator `name`
- **Empty/negative result looks like:** "no results" for a callsign that has never beaconed to APRS-IS, or a station last heard long ago. Absence means the station isn't transmitting APRS (most people don't), not that the person doesn't exist.

## Gotchas & OpSec
- Only stations that broadcast APRS appear — this is a small, self-selected population (hams, some fleet/marine trackers), so a miss is expected for the general public.
- A callsign's SSID matters: the same operator may run several (`-9` car, `-7` handheld); check them all for the full picture.
- Passive: the data is publicly broadcast, and querying doesn't alert the operator. Still VPN for sensitive work.
- Positions are self-reported by the transmitter and can be stale, spoofed or delayed — corroborate before treating a location as current.

## Overlaps ("do both")
- Pairs with an FCC/national amateur-licence database — aprs.fi gives the callsign + location, the licence lookup gives the operator's real `name` and registered address.
- Complements other geolocation/mapping tools to place and route the reported coordinates.

## Trust & verifiability
`trust: trusted` — aprs.fi is a well-known, stable aggregator of the open APRS-IS feed; the *pipeline* is authoritative, but each position is only as truthful as the station that beaconed it, so verify high-stakes tracks.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aprs-on-google-maps |
| category | geolocation |
| selectorsIn → selectorsOut | username, geolocation → geolocation, device-id, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
