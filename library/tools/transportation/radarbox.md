---
id: radarbox
name: AirNav RadarBox
description: Use when you have a flight number, aircraft registration, or callsign and want live/near-live position and history — returns `geolocation`, aircraft/operator, and route.
url: https://www.radarbox.com/
category: transportation
path:
- transportation
bestFor: Live ADS-B flight tracking and flight/aircraft history — locating an aircraft or reconstructing where a given tail number has flown.
selectorsIn:
- vehicle-plate
- geolocation
selectorsOut:
- geolocation
- employer-org
status: live
pricing: freemium
costNote: Free live map and basic flight/aircraft search; historical playback and extended data are behind a paid subscription (Business plan).
opsec: passive
opsecNote: Querying a flight-tracking site is passive — you observe public ADS-B broadcasts, not the aircraft or its occupants. No account needed for the live map.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major commercial flight-tracking network (rebranded AirNav Radar) fed by crowdsourced ADS-B receivers; live positions are reliable, coverage depends on receiver density.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- RadarBox
- AirNav Radar
- airnavradar.com
tags: []
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# AirNav RadarBox

> A global ADS-B flight-tracking network (now branded AirNav Radar) — track an aircraft live by flight, registration, or callsign, and see where a specific tail number has been.

## When to use
You have a flight number, an aircraft registration (tail number, e.g. `N12345` — the aviation equivalent of a plate), or a callsign and want to (a) see the aircraft's current position and route, or (b) understand its recent movements and operator. Relevant when a subject, a private jet, or an operator of interest is tied to specific flights, or to corroborate travel claims against real flight activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.radarbox.com/ (redirects to airnavradar.com).
2. Search a flight number, registration, or callsign in the search bar, or click an aircraft on the live map.
3. Read the flight panel: current `geolocation`, altitude/speed, origin/destination, aircraft type, and operator (`employer-org`).
4. For history/playback (past flights of a tail number), use the paid tier or cross-check with a free alternative.
5. Pivot: an operator/owner leads to corporate records; a route/timing corroborates a travel timeline.

## Inputs → Outputs
- **In:** flight number, aircraft registration (`vehicle-plate`), callsign, or a map `geolocation`
- **Out:** `geolocation` (live position + route), aircraft type/registration, and operator `employer-org`.
- **Empty/negative result looks like:** aircraft not shown — it isn't broadcasting ADS-B, is out of receiver coverage (oceans/remote areas), or has opted into blocking; absence isn't proof it isn't flying. Deep history needs a subscription.

## Gotchas & OpSec
- Coverage follows the crowdsourced receiver network — gaps over oceans and remote regions.
- Some owners enrol in privacy/blocking programs, hiding registration or position.
- Free tier is live-only; historical playback is paid — pair with a free alternative for history.
- OpSec: fully passive; you're reading public broadcasts.

## Overlaps ("do both")
- Complements other ADS-B trackers (ADS-B Exchange, Flightradar24) — ADS-B Exchange shows aircraft that opt out of blocking on commercial sites, so run it alongside RadarBox when a tail number seems hidden.

## Trust & verifiability
`trust: community` — a commercial network on crowdsourced ADS-B; live positions are trustworthy and cross-verifiable against other trackers, with coverage the main limitation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radarbox |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate, geolocation → geolocation, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
