---
id: citymapper-mapping-app-mobile-ios
name: Citymapper Mapping App (Mobile – iOS)
description: Use when you have an `address` or `geolocation` in a covered city and want realistic transit/travel options — returns routes, travel times, and reachable-area context.
url: https://apps.apple.com/us/app/citymapper-all-live-transit/id469463298
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Modeling how a person could actually move through a covered metro area — routes, transit times, and plausible travel radius.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free iOS app (in-app Citymapper Club subscription is optional and not needed for routing).
opsec: passive
opsecNote: "Route planning is passive toward any subject — you're querying Citymapper's servers about places, not the person. Citymapper does log your searches and, if you grant location permission, your device location; run it on a burner/investigation device with location sharing off and no personal Apple ID if that matters."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: trusted
trustNote: Citymapper is a well-established multimodal transit app (owned by Via) covering many major world cities; routing data is reliable within its coverage and stale/absent outside it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Citymapper
- Citymapper iOS
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- transit
- geolocation
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Citymapper Mapping App (Mobile – iOS)

> A multimodal transit planner for major cities — useful in investigations for reasoning about how far and by what means a person could realistically travel from a known point.

## When to use
You have an `address` or `geolocation` in a Citymapper-covered metro and want to model movement: what transit lines serve it, how long it takes to reach point B, what's within a plausible travel window. Handy for testing an alibi, bounding a search radius, or understanding the transport context around a last-known location. It is analyst-side context tooling (it tells you nothing about a specific person), so missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Citymapper from the iOS App Store (link above) on an investigation device.
2. Deny always-on location permission unless you need "from my location"; instead type the known `address`/`geolocation` as the start point.
3. Enter the destination and read the route options: walk, bus, metro/rail, bike, rideshare, with door-to-door times and departures.
4. Use the times/lines to estimate a realistic travel radius or to check whether a claimed trip is plausible in the stated window.
5. Corroborate against a general map tool for areas Citymapper doesn't cover.

## Inputs → Outputs
- **In:** `address` / `geolocation` (start and destination)
- **Out:** transit routes, travel times, line/stop detail, implied reachable-area `geolocation`
- **Empty/negative result looks like:** "not available in your area" or missing transit lines — the city isn't covered; Citymapper only supports a curated list of metros, so fall back to Google/Apple Maps outside them.

## Gotchas & OpSec
- Coverage is limited to supported cities; outside them it has no data — do not read absence as "no transit."
- Granting location permission logs your device's position to Citymapper; keep it off and enter locations manually on a burner device.
- Timetables reflect scheduled/live service, which can differ from historical service on a past date you're reconstructing.

## Overlaps ("do both")
- Complements general mapping tools — Citymapper excels at realistic multimodal transit timing inside covered cities, while a general map covers everywhere and provides driving/satellite context. Use the general map for coverage, Citymapper for transit realism.

## Trust & verifiability
`trust: trusted` — an established, widely-used transit app with reliable routing inside its coverage; the only caveat is scope (supported cities) and that live schedules may not match a historical date you're reconstructing.
