---
id: planet-labs
name: Planet Labs
description: Use when you have a `geolocation` or `address` and want recent, near-daily high-cadence satellite imagery of that spot to confirm activity or change — returns geolocation-anchored imagery.
url: https://www.planet.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Near-daily 3m (and on-demand sub-meter) satellite imagery to detect change at a specific location over time.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Core imagery is a paid commercial subscription. Free access exists only through gated programs — Planet's Education & Research program and, for tropical-forest monitoring, the Norway/NICFI basemaps (free to registered users). No open anonymous imagery browser.
opsec: active
opsecNote: Access requires an account and, for the free programs, an application tied to your identity/affiliation. Your queries and area-of-interest selections are logged against that account. Use an institutional identity you're comfortable attaching to the investigation; do not assume searches are anonymous.
humanInLoop: true
humanInLoopReason:
- account-login
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Planet Labs PBC is a publicly traded, first-party satellite operator; imagery is primary sensor data, not aggregated third-party content.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- planet-gallery
- sentinel-hub
- google-earth-pro
tags:
- bellingcat-toolkit
- satellite-imagery
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Planet Labs

> A first-party satellite operator whose SuperDove/SkySat constellations image the whole Earth near-daily — the go-to when you need *recent* imagery of one place, not just the years-old default in web maps.

## When to use
You have a `geolocation` (or an `address` you can geocode) and need to see what a location looked like on or near a specific date — to confirm a vehicle/structure was present, detect that something changed (new construction, cleared ground, a gathering), or build a dated timeline. Planet's value over free basemaps is temporal: near-daily revisit at ~3 m, plus taskable sub-meter SkySat. Relevance to a single missing-person case is usually low, but high for location-verification and change-over-time questions.

## How to use it (`bestInteractionPattern`: web-manual / api)
1. Get access first: apply to the Education & Research program (students/academics/some journalists) or register for the free NICFI tropical-forest basemaps; otherwise a commercial subscription is required.
2. Log in to Planet Explorer, draw or enter your area of interest (coordinates/address).
3. Filter by date range and cloud cover; browse the image strip to find clear captures near your target date.
4. Compare two dates to spot change; export the scene or pull it via the API/`planet` CLI for analysis.
5. Pivot: a change signature → cross-check with `[[sentinel-hub]]` (free Sentinel-2) for corroboration, or with ground photos/`[[google-earth-pro]]` historical imagery.

## Inputs → Outputs
- **In:** `geolocation` / `address` + a date window
- **Out:** dated, `geolocation`-anchored satellite scenes of that spot
- **Empty/negative result looks like:** every capture in your window is cloud-covered, or your access tier/AOI is outside the licensed coverage — meaning no usable image, not that nothing happened there.

## Gotchas & OpSec
- Not free-to-browse anonymously: the useful workflow requires an account and, for free tiers, an application (`legal-gate` + `account-login`).
- NICFI free basemaps are limited to the tropical-forest belt; Education & Research access has usage terms — read the license before publishing imagery.
- Cloud cover and revisit gaps mean the "near-daily" cadence is best-effort; always check the actual capture date, not just the AOI.

## Overlaps ("do both")
- Pairs with `[[sentinel-hub]]` — Sentinel-2 is fully free but coarser (10 m) and less frequent; use it to confirm/date a change Planet surfaces, or as a no-account fallback.
- Compare against `[[google-earth-pro]]` historical imagery for older baselines, and see `[[planet-gallery]]` for curated Planet examples.

## Trust & verifiability
`trust: trusted` — Planet is the sensor operator, so scenes are primary imagery with reliable capture metadata. The main constraints are access/licensing, not data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | planet-labs |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, legal-gate) |
