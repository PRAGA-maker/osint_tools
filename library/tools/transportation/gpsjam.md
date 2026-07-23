---
id: gpsjam
name: GPSJam
description: Use when you have a `geolocation` / region and want to know if it is experiencing GPS/GNSS jamming — returns a daily interference heatmap derived from aircraft navigation data.
url: https://gpsjam.org/
category: transportation
path:
- transportation
bestFor: Checking whether an area shows GPS/GNSS interference on a given day, to explain navigation anomalies or conflict activity.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free public map. No account or API key.
opsec: passive
opsecNote: You browse a public map; nothing is sent to any target and the subject cannot see your query. No login means no account footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by Ian Coleman from ADS-B Exchange aircraft data; a well-known, methodologically transparent resource cited by aviation and conflict analysts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- GPSJam.org
- GPS interference map
tags:
- aviation
- gnss
- interference
- bellingcat-toolkit
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# GPSJam

> A daily world map of where aircraft are losing GPS accuracy — a proxy for GNSS jamming and spoofing hotspots.

## When to use
You have a `geolocation` (a region, a conflict zone, an airport, a coordinate) and want to know whether GPS/GNSS was being jammed there on a specific day. GPSJam aggregates ADS-B navigation-accuracy signals from aircraft: where many planes report degraded accuracy, the map turns red, flagging likely interference. Useful for corroborating claims about electronic warfare, explaining why a device's location data looks wrong, or contextualising conflict events. Its direct missing-persons value is low; it's a geospatial-context tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gpsjam.org/ — it defaults to the most recent complete day's map.
2. Use the date picker (top of page) to select the day of interest; each day is a separate snapshot.
3. Zoom/pan to your `geolocation`. Cells are colour-coded:
   - **Green** — low interference (0–2% of aircraft affected)
   - **Yellow** — medium (2–10%)
   - **Red** — high (>10%)
4. Read the affected region and cross-reference with the event/time you're investigating. Pivot: pair a red zone with ADS-B Exchange flight tracks to see individual aircraft anomalies.

## Inputs → Outputs
- **In:** `geolocation` (region / coordinates) + a date
- **Out:** a `geolocation`-keyed interference intensity (low/medium/high) for that day
- **Empty/negative result looks like:** all-green or a "data for this day is incomplete" banner over the area — means no measured interference OR insufficient aircraft coverage there; sparse-traffic regions (open ocean, low-flight areas) can read green simply from lack of data.

## Gotchas & OpSec
- Resolution depends on air traffic density — remote or no-fly areas have little/no data, so green ≠ confirmed clean.
- The signal is *navigation degradation*, which strongly implies jamming/spoofing but isn't a direct jammer detector.
- Data is daily, not real-time; check the exact date and mind the "incomplete data" warning for recent days.
- OpSec: fully passive public browsing.

## Overlaps ("do both")
- Pairs with ADS-B flight-tracking tools (e.g. ADS-B Exchange, the upstream data source): GPSJam shows *where* interference clusters, flight trackers show *which aircraft* were affected and their tracks.

## Trust & verifiability
`trust: trusted` — an established, openly-documented project derived from real aircraft telemetry; the methodology and its limits (traffic-density dependence) are published by the author.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gpsjam |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
