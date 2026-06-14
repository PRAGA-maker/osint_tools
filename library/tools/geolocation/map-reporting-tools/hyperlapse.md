---
id: hyperlapse
name: Hyperlapse
description: Use when you have a `geolocation` route and want to generate a smoothed Street View "fly-through" video along it (developer/JS library).
url: https://github.com/TeehanLax/Hyperlapse.js
category: geolocation
path:
- geolocation
- map-reporting-tools
bestFor: Producing a smoothed Street View hyperlapse animation along a route for briefing/visualization.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: degraded
pricing: free
costNote: Free open-source code (MIT); relies on the Google Maps/Street View JS API, which now requires an API key and billing.
opsec: passive
opsecNote: Renders public Street View imagery along a route you specify; the target is never contacted. Runs client-side in your own page.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: python-lib
trust: unverified
trustNote: A 2013-era JavaScript library (Teehan+Lax) that is no longer maintained; depends on a deprecated Street View API version and likely needs adaptation to run today.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: true
relatedTools:
- instant-google-street-view
aliases:
- Hyperlapse.js
tags:
- geospatial-research-and-mapping-tools
- map-reporting-tools
source: arf-seed
lastVerified: ''
enrichment: full
---

# Hyperlapse

> Hyperlapse.js — an old open-source JavaScript library that stitches Google Street View panoramas into a smoothed "fly-through" animation along a route.

## When to use
You have a `geolocation` route (e.g., a corridor a missing person may have travelled) and want a moving visual walkthrough — a hyperlapse video — for a briefing or to scan the route for landmarks. This is a developer library, not a point-and-click site; relevance to active casework is low because it produces a visualization rather than new findings, and the underlying API has changed.

## How to use it (`bestInteractionPattern`: python-lib)
1. Clone the GitHub repo (it's JS, embedded in a web page, not Python despite the field — treat it as a developer/library integration).
2. Supply a Google Maps JavaScript API key with Street View enabled (the original used a now-deprecated API version).
3. Define start/end `geolocation` points and animation settings; serve the page to render the hyperlapse.
4. Expect to patch the code for current Google APIs; for a quick manual look, use [[instant-google-street-view]] instead.

## Inputs → Outputs
- **In:** `geolocation` route (start/end coordinates)
- **Out:** a smoothed Street View hyperlapse animation along the route
- **Empty/negative result looks like:** blank frames or API errors — usually because the deprecated Street View API version no longer responds or the key lacks the right product enabled.

## Gotchas & OpSec
- Human-in-the-loop: requires a Google API key with billing; the library is unmaintained (circa 2013) and likely needs code changes.
- OpSec: passive — renders public Street View; the target is not contacted.

## Overlaps ("do both")
- For non-developer use, [[instant-google-street-view]] gives the same Street View access manually without any code.

## Trust & verifiability
`trust: unverified` — historically a real, well-known demo, but now abandoned and dependent on a deprecated API; assume it needs adaptation before it works.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hyperlapse |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | yes |
