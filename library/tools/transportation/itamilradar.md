---
id: itamilradar
name: ItaMilRadar
description: Use when you have a `geolocation` over Italy/the Mediterranean and want to identify military aircraft and naval movements there — returns callsigns, registrations and tracks.
url: https://www.itamilradar.com
category: transportation
path:
- transportation
bestFor: Tracking and identifying military flights and naval activity over Italy and the wider Mediterranean.
selectorsIn:
- geolocation
- vehicle-plate
selectorsOut:
- geolocation
- vehicle-plate
status: live
pricing: freemium
costNote: Free to read the blog and daily tracking posts; a Patreon tier adds early-access alerts and extras. Core content is free.
opsec: passive
opsecNote: You are reading a public tracking blog; nothing you do touches an investigative target. Standard passive browsing, though be aware military-tracking sites can themselves attract attention — use a sock-puppet browser if that matters to your posture.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent enthusiast project reporting from public ADS-B/ship-AIS feeds; well-regarded in the mil-tracking community but not an official source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- itamilradar.com
tags:
- Maps, Geolocation and Transport
- Military tracking
- aviation
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# ItaMilRadar

> An independent military-aviation and naval tracking blog centered on Italy and the Mediterranean — "beyond the track," with identified aircraft, callsigns and context.

## When to use
You have a `geolocation` in or around Italy, the central Mediterranean, or NATO's southern flank and you want to know what military aircraft or vessels were operating there and when. ItaMilRadar curates public ADS-B and AIS activity into daily posts that identify specific airframes (type, registration/`vehicle-plate`, callsign) and narrate the mission context — far more interpretable than raw flight-tracker dots. Use it for geolocation corroboration, event timelines, or identifying a military aircraft seen in imagery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.itamilradar.com in a browser.
2. Browse the reverse-chronological posts, or use the site search / category tags to filter by air force, aircraft type, or region.
3. Read a post to extract the specifics: aircraft type, registration (e.g. `MM62227`), callsign, route endpoints, and date/time.
4. Cross-check a registration or callsign against a live flight tracker or a military-serials database to confirm and extend the track.
5. Pivot: feed the registration/`vehicle-plate` and airbase endpoints into aircraft-registry and airbase-OSINT resources; use the date/time to anchor a broader event timeline.

## Inputs → Outputs
- **In:** `geolocation` (Italy/Mediterranean airspace or waters), or a `vehicle-plate`/callsign to search for
- **Out:** identified aircraft/vessel details — type, registration `vehicle-plate`, callsign, route `geolocation`, timing
- **Empty/negative result looks like:** no post covering the date/area you care about (the site reports notable activity, not every flight), or a post without a firm ID. Absence here means "not reported," not "nothing flew."

## Gotchas & OpSec
- Human-in-the-loop: none for reading; the Patreon tier is optional and only gates early alerts, not the core reporting.
- OpSec: **passive** browsing of a public blog. It reports on aircraft/vessels, not on any private individual.
- It is editorial and Italy/Med-focused: coverage is deep in that theatre and sparse elsewhere, and identifications reflect the author's analysis of public feeds, not official confirmation.

## Overlaps ("do both")
- Pairs with live ADS-B flight trackers and military-serial registries — ItaMilRadar gives the *identified, contextualized* Mediterranean picture; the trackers give raw real-time positions and the registries confirm the airframe.

## Trust & verifiability
`trust: community` — an independent enthusiast project. Its identifications are traceable to public ADS-B/AIS data and stated registrations, so individual claims can be verified, but it carries no official authority.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | itamilradar |
| category | transportation |
| selectorsIn → selectorsOut | geolocation, vehicle-plate → geolocation, vehicle-plate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
