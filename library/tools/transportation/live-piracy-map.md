---
id: live-piracy-map
name: Live Piracy Map (IMB)
description: Use when you have a maritime region/`geolocation` and want reported piracy and armed-robbery incidents against ships — returns incident `geolocation` and details.
url: https://www.icc-ccs.org/piracy-reporting-centre/live-piracy-map
category: transportation
path:
- transportation
bestFor: Viewing ICC-IMB-reported piracy and armed-robbery-at-sea incidents on a live world map.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: The live map is free to view; detailed IMB piracy reports and datasets are a paid product.
opsec: passive
opsecNote: Passive map browsing — queries hit ICC-CCS, nothing touches any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the ICC International Maritime Bureau (IMB) Piracy Reporting Centre — the authoritative clearinghouse for reported maritime piracy incidents.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- imb-piracy-and-armed-robbery-map
aliases:
- IMB Live Piracy Map
tags:
- maritime
- piracy
- incidents
- shipping
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Live Piracy Map (IMB)

> The maritime industry's authoritative map of where ships are being attacked — piracy and armed-robbery incidents plotted as they're reported.

## When to use
Your case has a maritime angle and you want the incident context for a sea region: where piracy/armed-robbery attacks are being reported, of what type, and when. Useful for corroborating a vessel's risk exposure along a route, understanding why a ship diverted, or situating a maritime event geographically.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the IMB Live Piracy Map at https://www.icc-ccs.org/piracy-reporting-centre/live-piracy-map.
2. Pan/zoom to the sea region of interest; each marker is a reported incident.
3. Click a marker for the incident narrative — date, attack type (boarded/attempted/hijacked), vessel status, and location.
4. Filter by year where available to see trends.
5. Pivot: combine incident `geolocation`/timing with vessel-tracking (AIS) data to correlate a specific ship's movements with reported attacks.

## Inputs → Outputs
- **In:** a maritime region / `geolocation` (navigate the map)
- **Out:** reported piracy/armed-robbery incidents with `geolocation`, date, attack type, and narrative
- **Empty/negative result looks like:** no markers in a region/period — no incidents *reported* to the IMB there (under-reporting is common in maritime crime), not proof the waters are safe.

## Gotchas & OpSec
- Shows **reported** incidents only; maritime crime is under-reported, so the map is a floor, not a full count.
- The free map is a summary; granular data and analysis are in IMB's paid reports.
- OpSec: passive; browsing hits ICC-CCS only.

## Overlaps ("do both")
- Pair with AIS vessel-tracking tools and [[imb-piracy-and-armed-robbery-map]] — the map gives incident context, AIS gives specific ship movements to correlate against it.

## Trust & verifiability
`trust: trusted` — the IMB Piracy Reporting Centre is the recognized authority; incidents are vetted reports, though coverage is bounded by what gets reported.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | live-piracy-map |
| category | transportation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
