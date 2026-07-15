---
id: seeallthethings
name: SeeAllTheThings
description: Use when you have a US `geolocation`/`address` and want public webcam feeds covering that area — this GitHub directory returns curated links to publicly available traffic/tourism cams organised by state.
url: https://github.com/baywolf88/seeallthethings
category: image-video-face
path:
- image-video-face
- webcams
bestFor: Finding publicly available live webcam feeds (DOT traffic, tourism cams) for a US area, organised by state.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- image
status: live
pricing: free
costNote: Free, open GitHub repository; no account needed to browse the links.
opsec: passive
opsecNote: Browsing the repo and viewing officially public webcam feeds (DOT/tourism) is passive. The author stresses the links are from publicly available sources — do not use it to reach non-public/unauthorised feeds, which crosses into illegal access.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small community-maintained link directory (a handful of commits). Links are curated public sources but may age; verify each feed is still live and genuinely public before relying on it.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- see all the things
- baywolf88/seeallthethings
tags:
- webcams
- publiccams
- curated-directory
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# SeeAllTheThings

> A GitHub-hosted directory of publicly available US webcam feeds, sorted by state — a fast way to find live eyes on an area a subject was last associated with.

## When to use
You have a US location — a state, city, highway corridor, or landmark tied to a case (a last-known area, a route someone may have travelled) — and you want to see whether there are publicly available live webcams (state DOT traffic cameras, tourism/scenic cams) covering it. It is a curated set of public feeds, useful for real-time or recent visual context on a place.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/baywolf88/seeallthethings and browse the state folders / README.
2. Navigate to the state (and sub-area, e.g. "DC Area") relevant to your location.
3. Open the listed feed links — mostly DOT traffic cameras and tourism cams — and confirm each is still live.
4. Use the live view for situational context (weather, road conditions, activity at a location); capture stills where appropriate for your file.
5. Pivot: combine with mapping tools to fix exact coordinates, and cross-check official DOT camera portals directly for the fullest current coverage.

## Inputs → Outputs
- **In:** a US `geolocation`/`address` (which state/area you care about)
- **Out:** links to public live webcam feeds (`geolocation`-tagged), from which you can capture `image` stills
- **Empty/negative result looks like:** a state/area with no listed cams (the directory is incomplete), or dead links where a feed has moved — absence here does NOT mean no public cam exists; go to the state DOT site directly.

## Gotchas & OpSec
- **Public feeds only** — the author explicitly warns against accessing feeds without authorization; never use it as a jumping-off point to unsecured private cameras (that is illegal).
- Coverage is partial and US-centric, and links age; treat it as a starting index, not a complete map — official DOT portals are more current.
- OpSec: **passive** for genuinely public feeds.

## Overlaps ("do both")
- Complements direct state DOT camera portals and mapping tools: use this to discover candidate feeds quickly, then verify and supplement from the authoritative official sources.

## Trust & verifiability
`trust: community` — a small volunteer link collection. The sources are public and legitimate, but the list is incomplete and can go stale; confirm each feed is live and public at the official source before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seeallthethings |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, address → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
