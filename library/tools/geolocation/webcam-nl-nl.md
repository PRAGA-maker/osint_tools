---
id: webcam-nl-nl
name: Webcam.nl (NL)
description: Use when you have a Dutch `geolocation` or `address` and want live public-camera imagery of that spot — returns `image` (live video stills).
url: https://webcam.nl/live_streaming
category: geolocation
path:
- geolocation
bestFor: Pulling live public webcam views of Dutch beaches, harbours, traffic routes and tourist spots to corroborate a location or last-known-seen area.
selectorsIn:
- geolocation
- address
selectorsOut:
- image
status: live
pricing: free
costNote: Free to view; the operator (Unlimited Visions BV) sells camera hardware/installation but streams are hosted free on YouTube with no login.
opsec: passive
opsecNote: You are watching a public YouTube livestream — nothing is sent to the target and the camera operator cannot tie a view back to you. No sock puppet needed, though a clean browser is still good hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Run by a legitimate Dutch webcam installer (KvK 30163988); streams are genuine live feeds, but framing/coverage is whatever the operator chose to publish — not an official municipal CCTV index.
missingPersonsRelevance: medium
coverage:
- nl
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- webcam.nl
- Unlimited Visions webcams
tags:
- cctv
- webcam
- netherlands
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# Webcam.nl (NL)

> A directory of live 4K public webcams across the Netherlands (beaches, harbours, traffic, nature reserves, tourist sites) streamed free via YouTube.

## When to use
You have a Dutch `geolocation` or `address` — a beach, harbour, motorway junction, town square or nature reserve — and want real-time or recent imagery of that spot: to confirm current conditions, watch a public area where someone may pass, or geolocate/verify a scene against a known live feed. It is a location-imagery tool, not a person-search tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://webcam.nl/live_streaming.
2. Browse the category list (construction, traffic, tourism, beaches, nature, harbours, sports) or scan the map/thumbnails for a camera near your target `geolocation`.
3. Click a camera to open its live YouTube stream; use YouTube's timeline to scrub back over recent footage where available.
4. Read the `image`: note landmarks, signage, vehicles or crowds visible in-frame.
5. Pivot: match visible landmarks to a map, or cross-check against another live-cam index like [[insecam]] or a mapping tool to widen coverage.

## Inputs → Outputs
- **In:** `geolocation` or `address` (Netherlands only)
- **Out:** `image` — live/near-live video of the covered spot
- **Empty/negative result looks like:** no camera exists near your location (coverage is a curated handful of sites, not blanket CCTV), or a stream shows "offline/unavailable" on YouTube — treat as no-data, not as evidence about the location.

## Gotchas & OpSec
- Coverage is sparse and operator-chosen: most Dutch addresses have **no** nearby camera. Absence of a feed tells you nothing.
- Streams are fixed public views; you cannot pan/zoom or request historical footage beyond what YouTube retains.
- OpSec: fully passive — watching a public livestream leaks nothing to the target.

## Overlaps ("do both")
- Pairs with [[insecam]] and other live-camera indexes because each catalogues a different, non-overlapping set of feeds — run several to maximise the chance of a camera near your location.

## Trust & verifiability
`trust: community` — a real Dutch company publishes genuine live feeds, but this is a commercial webcam catalogue, not an authoritative or exhaustive surveillance registry; verify any landmark you rely on against an independent map.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webcam-nl-nl |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
