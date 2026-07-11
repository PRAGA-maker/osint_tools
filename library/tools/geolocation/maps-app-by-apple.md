---
id: maps-app-by-apple
name: Apple Maps
description: Use when you have an `address` or `geolocation` and want to see and verify a location — returns satellite/3-D imagery, street-level "Look Around" panoramas and points of interest.
url: https://www.apple.com/ios/maps
category: geolocation
path:
- geolocation
bestFor: Verifying an address on the ground with Apple's "Look Around" street-level imagery and high-quality 3-D/satellite views.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
- address
- physical-description
status: live
pricing: free
costNote: Free with an Apple device (iPhone/iPad/Mac); a limited web version (maps.apple.com / DuckDuckGo Maps) works cross-platform.
opsec: passive
opsecNote: Viewing a place in Apple Maps does not notify anyone at that location and does not touch the subject. Requests go to Apple; do the browsing on a device/account not tied to your identity if attribution matters. Do not confuse map "Directions" (which uses YOUR location) with looking at a target address — searching a target address leaks nothing about them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: trusted
trustNote: First-party Apple mapping product with independently-captured imagery. Imagery is periodically refreshed, so "Look Around" panoramas may be months to a few years old — date the capture where possible.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Apple Maps
- Look Around
tags:
- toddington
- curated-directory
- geo-location-mapping-tools
- street-view
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Apple Maps

> Apple's mapping app, valuable in OSINT for "Look Around" — a Street-View-equivalent that often has imagery Google Street View lacks, giving a second set of eyes on the ground.

## When to use
You have an `address` or `geolocation` and want to see the place: verify a building exists and matches a description, scout access/parking before a physical check, read house numbers and signage, or corroborate a photo's setting. Apple's "Look Around" and 3-D city models frequently cover spots (or capture dates) different from Google Street View, so it's a complementary confirmation layer for any location.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Open Apple Maps on an iPhone/iPad/Mac (or the limited web map at maps.apple.com / via DuckDuckGo Maps for non-Apple devices).
2. Search the `address` or drop a pin on the `geolocation`.
3. Toggle Satellite/3-D and tap the binoculars **Look Around** icon (where available) for a street-level panorama; walk it to read numbers, businesses, vehicles and layout.
4. Note nearby points of interest and the imagery capture date if shown.
5. Pivot: confirmed `physical-description` of a building feeds a photo-geolocation cross-check; a business POI at the address is an `employer-org` lead. Compare directly against `[[google-street-view]]` for a second date/angle.

## Inputs → Outputs
- **In:** `address` or `geolocation`
- **Out:** verified `geolocation`/`address`, `physical-description` of the site (building, surroundings, nearby POIs)
- **Empty/negative result looks like:** no Look Around coverage for that spot, or satellite imagery too coarse to resolve detail — fall back to Google Street View / Bing / Yandex, which may have imagery Apple doesn't.

## Gotchas & OpSec
- Look Around coverage is narrower than Google Street View outside major cities — absence of a panorama isn't meaningful.
- Imagery is historical (months–years old); a building may have changed. Treat it as "how it looked when captured."
- The best experience needs an Apple device; the web map is feature-limited.

## Overlaps ("do both")
- Pairs with `[[google-street-view]]`, Bing Streetside and Yandex Panoramas — different providers capture different streets on different dates, so cross-checking gives more angles and a rough change-over-time timeline.

## Trust & verifiability
`trust: trusted` — first-party Apple imagery, captured by Apple's own survey fleet. The only caveat is imagery age; note the capture date before relying on a detail.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maps-app-by-apple |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation, address, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | no |
