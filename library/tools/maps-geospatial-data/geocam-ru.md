---
id: geocam-ru
name: Geocam.ru
description: Use when you have a `geolocation` (a city or place) and want live public webcam feeds there — returns real-time street/traffic/scenic camera views for ground-truthing weather, activity, or a scene at a location.
url: https://www.geocam.ru/en/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Browsing thousands of live public webcams worldwide by country/city to see current conditions at a location.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free to browse; no account required.
opsec: passive
opsecNote: You view public webcam streams hosted/aggregated by geocam.ru; the subject is not contacted and camera operators do not see you individually. The site is Russian-operated — use a hardened browser and a VPN; don't log in or submit anything.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running webcam aggregator (Russian) indexing public/third-party camera feeds; individual feeds' uptime and true location depend on their operators and can be stale or mislabelled.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- geocam.ru
- Geocam world webcams
tags:
- toddington
- curated-directory
- specialty-search
- webcams
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Geocam.ru

> A global directory of live public webcams organised by country and city — use it to look at what a place looks like *right now* (weather, light, traffic, crowds) or to match a scene to a location.

## When to use
You have a `geolocation` (a country, city, or specific landmark/beach/street) and want current real-world imagery from there: to confirm present conditions (daylight, weather, snow, crowd level) before a ground effort, to establish what a location normally looks like, or to try to match a background in a subject's photo/video against a fixed public camera's view. It is broad rather than deep — strongest where a public camera happens to cover the exact spot you care about.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.geocam.ru/en/.
2. Browse by country → city, use the search, or open the interactive map to find cameras near a `geolocation`.
3. Open a feed; note its stated location and category (city view, traffic, beach, interior). Many are live streams, some are periodic stills.
4. Cross-check the camera's claimed location against a map/landmarks before trusting it — aggregated feeds are sometimes mislabelled or relocated.
5. Pivot: a confirmed live view can time-stamp conditions (compare shadows/weather to a subject's photo), or a matched fixed-camera background can geolocate an image.

## Inputs → Outputs
- **In:** `geolocation` (country / city / place)
- **Out:** `geolocation`-anchored live `image`/video feeds (current scene at that place)
- **Empty/negative result looks like:** no camera listed for the area, or a listed feed that is offline/frozen/redirects — coverage is patchy and feeds die; absence just means no public camera is indexed there.

## Gotchas & OpSec
- Human-in-the-loop: none; browse-only, no login.
- OpSec: **passive** toward the subject. The site is Russia-hosted — access via a hardened browser and VPN, and never submit data or credentials.
- Reliability: feeds belong to third parties; a stream can be down, delayed, or mislabelled. Confirm the real location with independent landmarks before relying on any match.

## Overlaps ("do both")
- Pairs with other live-camera aggregators (EarthCam, Windy Webcams, WorldCam) and with map/imagery tools — coverage differs per aggregator, so if one has no camera for your spot, another might; combine with satellite/street-view imagery to confirm a camera's true vantage point.

## Trust & verifiability
`trust: community` — geocam.ru is a durable but third-party aggregator of feeds it does not own; treat each camera's location and liveness as claims to verify against maps and landmarks, not as established fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geocam-ru |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
