---
id: citymapper-mapping-app-mobile-android
name: Citymapper Mapping App (Mobile – Android)
description: Use when you have an `address`/`geolocation` in a supported city and want realistic transit routing — returns door-to-door routes, timings and transport options for feasibility/timeline analysis.
url: https://play.google.com/store/apps/details?id=com.citymapper.app.release
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Detailed multimodal transit routing in major cities — testing how (and how long) someone could travel between two points using real public-transport data.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free app (also usable at citymapper.com); optional paid "Club" tier isn't needed for routing.
opsec: passive
opsecNote: Planning a route is passive and involves no target — you are querying a transit-routing service about places, not people. Don't enable location sharing / trip logging on a research device if you want no local trace.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: trusted
trustNote: Established transit-routing app using official transport-agency data for its supported cities; routing and timings are reliable within covered metros.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- google-maps
aliases:
- Citymapper
tags:
- toddington
- transit
- routing
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Citymapper Mapping App (Mobile – Android)

> A precise public-transit router for major cities — used in investigations to reality-check how someone could get between two locations and how long it would take.

## When to use
You have two points in a supported metro (an `address`/`geolocation` origin and destination) and need a realistic **movement/timeline** assessment: could the subject plausibly travel A→B in the available window, by which modes, and along what route? Citymapper's strength over generic maps is granular multimodal transit — buses, metro, rail, bike, walk, ride-hail — with accurate timings, which helps confirm or break an alibi/timeline and map likely routes and interchange points.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Open the app (or citymapper.com) — no login needed for routing.
2. Confirm the city is supported (Citymapper covers major metros, not everywhere).
3. Enter the origin and destination (`address`/`geolocation`).
4. Read the route options: each shows total time, modes, exact lines/stops, walking segments and departure timing.
5. Pivot: use the routes/interchanges to identify likely CCTV points, transit stops or timings to corroborate; feed the geography into mapping/imagery tools.

## Inputs → Outputs
- **In:** origin + destination (`address` / `geolocation`) in a supported city
- **Out:** `geolocation` routing — door-to-door routes, modes, timings, stops/interchanges
- **Empty/negative result looks like:** "not available in this area" (city unsupported) or no viable transit route — fall back to Google Maps for wider coverage.

## Gotchas & OpSec
- **City-limited:** only works well in the metros Citymapper covers; outside them use a broader router.
- Timings assume normal service — strikes, closures and off-hours change real feasibility; treat outputs as planning estimates.
- Passive: you're querying routing about places, not contacting anyone. Keep trip history off on a research device.

## Overlaps ("do both")
- Pairs with `[[google-maps]]` — Google covers far more places and driving; Citymapper gives richer transit detail where supported. Cross-check timings and routes across both for a timeline/feasibility question.

## Trust & verifiability
`trust: trusted` — a well-established transit app built on official agency data; routing and timings are reliable inside covered cities. Verify a decisive timeline against live service status and a second router.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | citymapper-mapping-app-mobile-android |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | address, geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | no |
