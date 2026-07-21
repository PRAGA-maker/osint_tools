---
id: safe-airspace
name: Safe Airspace
description: Use when you have a country/region `geolocation` and want conflict-zone aviation risk intel — warnings, incident history, GPS jamming/spoofing and military-activity alerts — returns a country-by-country risk picture and a `geolocation` hazard map.
url: https://safeairspace.net/
category: geolocation
path:
- geolocation
bestFor: Conflict-zone and aviation-risk intelligence by country, including GPS spoofing/jamming alerts relevant to geolocation work.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: "\"Eternally free\" per the operator; no account or payment required to browse warnings, the map or PDF briefings."
opsec: passive
opsecNote: Reading a public risk database is fully passive and anonymous — no target interaction.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Run by OPSGROUP, an independent aviation-operations membership organization; it aggregates official EASA/FAA/national-CAA warnings plus member incident reports — well-regarded but a curated aggregator, not an issuing authority.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- safeairspace.net
- OPSGROUP conflict zones
tags:
- Maps, Geolocation and Transport
- Politics, conflicts and crisis
- conflict-zones
- gps-spoofing
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Safe Airspace

> OPSGROUP's free conflict-zone risk database — a country-by-country picture of airspace warnings, incidents, military activity and (crucially for OSINT) GPS jamming and spoofing.

## When to use
You're building geopolitical context for a location, or geolocating imagery/tracks from or near a conflict area. Safe Airspace maps, per country, the current airspace restrictions, recent incidents (drone strikes, closures, anti-aircraft threats), and — most useful to a geolocation analyst — **active GPS jamming/spoofing zones**, which can silently corrupt the coordinates in device metadata, flight-tracking and mapping. Use it to understand the risk environment around a location and to sanity-check whether GPS-derived positions in your evidence might be spoofed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://safeairspace.net/.
2. Browse by country (or the live map) to the region you're investigating.
3. Read the country card: current airspace restrictions, operational risks, incident history, and official warnings (EASA/FAA/CAA sources cited).
4. Check specifically for **GPS spoofing/jamming** notes for that area, and generate a PDF briefing if you need a snapshot.
5. Pivot: a GPS-spoofing zone flags that coordinates in imagery/EXIF or ADS-B from that area may be unreliable — cross-check location visually rather than trusting device GPS; incident/closure history dates a conflict timeline.

## Inputs → Outputs
- **In:** `geolocation` (country/region)
- **Out:** `geolocation` risk picture — warnings, incident history, military-activity and GPS jamming/spoofing alerts, plus a hazard map
- **Empty/negative result looks like:** a country with "no current warnings" — no *aviation* risk flagged there now. It covers airspace/conflict risk, not ground crime or general safety, so absence here is narrow.

## Gotchas & OpSec
- It's **aviation-focused**: excellent for conflict/airspace/GPS-integrity context, not a general country-safety or crime source.
- An **aggregator**, not an issuing authority — it cites official warnings but for legal/operational decisions go to the primary EASA/FAA/CAA notice.
- OpSec: **passive** — reading a public database, nothing exposed.

## Overlaps ("do both")
- Pairs with flight-tracking (ADS-B) tools and general geolocation/mapping — Safe Airspace tells you *where GPS data can't be trusted* and where conflict is active, sharpening how you interpret the others.

## Trust & verifiability
`trust: community` — an independent, well-respected aviation-ops organization aggregating official and member-sourced intel. Reliable for situational awareness; confirm any specific restriction against the cited primary authority.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | safe-airspace |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
