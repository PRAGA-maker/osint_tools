---
id: satellite-tracking
name: Satellite Tracking
description: Use when you have a satellite name/NORAD ID and want its live position and pass times — returns orbital position, altitude, and when it passes over a `geolocation`.
url: https://www.n2yo.com/
category: transportation
path:
- transportation
bestFor: Real-time satellite position and overhead-pass prediction for a given location.
selectorsIn:
- geolocation
- document-id
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free live-tracking site (N2YO); optional free account/API key for the REST API.
opsec: passive
opsecNote: Uses public orbital element (TLE) data; nothing about a person is queried and no one is alerted. Fully passive. Entering a location only computes passes locally against public orbits.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-standing, widely-used satellite-tracking site built on public NORAD/Celestrak orbital data; positions are computed from authoritative TLEs.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- celestrak
- heavens-above
aliases:
- N2YO
- n2yo.com
tags:
- satellite
- orbital-tracking
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Satellite Tracking

> N2YO's live satellite tracker — where a satellite is right now, and when it passes over a given location, computed from public orbital data.

## When to use
A niche corroboration tool: you want to know whether a specific satellite was overhead a `geolocation` at a certain time — e.g. to reason about when a satellite image of a scene could have been captured, or to verify/debunk a claim involving a satellite pass. Given a satellite name or NORAD ID, N2YO shows its live position and predicts overhead passes for any location. Direct missing-persons relevance is low, but it can support imagery-timing and verification questions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.n2yo.com/ and search a satellite by name or NORAD catalog ID (or browse categories).
2. View its live ground track and current position/altitude/velocity.
3. Use "Passes" and set your location to get predicted overhead pass times (with elevation/azimuth).
4. For imagery reasoning, identify the relevant Earth-observation satellite and check when it was over the area.
5. Pivot: a confirmed pass time → bound when satellite imagery of a scene could exist; cross-check orbital data on `[[celestrak]]`.

## Inputs → Outputs
- **In:** a satellite name or NORAD ID (`document-id`), plus a `geolocation` for pass prediction
- **Out:** live orbital position, altitude, and overhead-pass times for the location (`geolocation`)
- **Empty/negative result looks like:** satellite not found (wrong name/ID or decayed/deorbited object) or no passes in the window — the object isn't overhead that location in the timeframe.

## Gotchas & OpSec
- Accuracy depends on current TLEs; predictions degrade for older element sets or maneuvering satellites.
- Knowing a satellite passed over an area does not mean it imaged it — sensor tasking, swath, and cloud cover all matter; treat passes as necessary-not-sufficient for imagery.
- Fully passive; no exposure.

## Overlaps ("do both")
- Pairs with `[[celestrak]]` — authoritative TLE source; use it to confirm the orbital data behind N2YO's predictions.
- Pairs with `[[heavens-above]]` for an alternative pass-prediction view.

## Trust & verifiability
`trust: trusted` — an established tracker computing from public NORAD/Celestrak orbital data, so positions/passes are reproducible against any other propagator. The inference from "pass" to "image exists" is where care is needed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | satellite-tracking |
| category | transportation |
| selectorsIn → selectorsOut | geolocation, document-id → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
