---
id: windy
name: Windy
description: Use when you need historical/forecast weather for a place and date, or live and recently archived webcams near a location, to validate a scene or get eyes on an area.
url: https://www.windy.com/
category: geolocation
path:
- geolocation
bestFor: Weather conditions for a place/date plus a large network of geolocated webcams (live and recent archive).
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: freemium
costNote: Free web app and webcams; premium tier adds higher-resolution forecast models and history.
opsec: passive
opsecNote: Weather/webcam lookups against Windy's servers; no contact with the target. Webcams are third-party public feeds.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Windy is a well-known meteorological platform; weather data comes from mainstream forecast models, webcams from its public network.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- timeanddate
- suncalc-2
aliases:
- windy.com
tags:
- weather
- webcams
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Windy

> A meteorological mapping platform — and, importantly for OSINT, a huge network of geolocated webcams — for checking conditions and getting live eyes on an area.

## When to use
Two distinct uses:
1. **Weather validation:** you have a `geolocation`/date and need conditions (wind, cloud, precipitation, temperature) to test a photo or testimony — e.g. it was raining, so a clear sunny photo can't be that day.
2. **Webcams:** Windy hosts a large network of public webcams pinned to the map, including live feeds and recent archives — useful to get current eyes on a town, road, beach, or trailhead near a last-known location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.windy.com/.
2. For weather: pan to the location, pick the layer (wind/rain/clouds/temp) and scrub the time slider; premium unlocks finer-grained and historical model data.
3. For webcams: enable the **Webcams** layer (or use the webcams section), click pins near your area, and view the live feed plus the recent timelapse/archive.
4. Note the timezone and capture time shown on webcam frames.
5. Pivot: confirm sunrise/sunset and weather history with [[timeanddate]]; confirm shadow geometry with [[suncalc-2]].

## Inputs → Outputs
- **In:** `geolocation`/`address` + date (weather) or area of interest (webcams).
- **Out:** weather conditions for that place/time; live/archived webcam imagery (validates `metadata-exif`/timeline; gives current `geolocation` views).
- **Empty/negative result looks like:** no webcams near the area (common for remote/inland spots), or forecast-model weather rather than a true station observation for fine-grained past dates.

## Gotchas & OpSec
- Free tier limits how far back/forward and how finely you can scrub weather history; premium needed for detailed past conditions.
- Webcam coverage is dense in scenic/urban areas, sparse elsewhere; feeds belong to third parties and can go offline.
- No login or captcha for basic use; passive throughout.

## Overlaps ("do both")
- Pairs with [[timeanddate]] (sunrise/sunset + past-weather archive) and [[suncalc-2]] (sun direction) to fully reconstruct lighting/weather of a scene.

## Trust & verifiability
`trust: trusted` — established platform using mainstream forecast models; weather is model-derived (note for fine past dates), webcams are timestamped public feeds you can corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | windy |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, metadata-exif |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
