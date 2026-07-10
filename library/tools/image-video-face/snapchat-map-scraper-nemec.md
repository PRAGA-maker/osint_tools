---
id: snapchat-map-scraper-nemec
name: Snapchat Map Scraper (nemec)
description: Use when you have a `geolocation` and want the public Snapchat stories posted there — returns downloaded Snap Map media/stories for the area.
url: https://github.com/nemec/snapchat-map-scraper
category: image-video-face
path:
- image-video-face
bestFor: Harvesting public Snapchat Snap Map stories at a set of coordinates for last-known-location scene review.
selectorsIn:
- geolocation
selectorsOut:
- image
status: live
pricing: free
costNote: Free, open-source script. No account, API key, or payment; you supply the location.
opsec: passive
opsecNote: It pulls from Snapchat's public Snap Map endpoint, not the target directly, so posters are not notified. Run from a research machine and treat harvested media as sensitive evidence.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source Snap Map scraper (nemec) in the Social-Media-OSINT collection. It relies on Snapchat's undocumented public Map API, which can change and break the tool.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- snap-scraper
aliases:
- snapchat-map-scraper
tags:
- snapchat
- snapmap
- geolocation
source: gh-topic-osint-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Snapchat Map Scraper (nemec)

> A command-line Snap Map story harvester: give it coordinates and it pulls the public Snapchat stories posted at that location.

## When to use
You have a `geolocation` (coordinates) for a place of interest and want the public Snapchat stories submitted there — the media that can put a person, vehicle, or scene at a spot and time. Like other Snap Map scrapers, it's built for last-known-location and incident work, harvesting the public Snaps that Snap Map surfaces by location so you can review them offline.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `github.com/nemec/snapchat-map-scraper` and install its dependencies (Python-based; check the repo README for exact setup).
2. Obtain coordinates for the target area (e.g. from map.snapchat.com or a lat/long finder).
3. Run the scraper against those coordinates.
4. Review the downloaded stories/media and their metadata (location, time).
5. Pivot: faces feed face-search; vehicles/plates feed vehicle tools; scene detail feeds geolocation verification. Cross-run with `[[snap-scraper]]` for coverage.

## Inputs → Outputs
- **In:** `geolocation` (coordinates / area)
- **Out:** `image`/video of public Snap Map stories at that location, with metadata
- **Empty/negative result looks like:** no stories returned. Snap Map only shows areas with enough public submissions — quiet locations or an over-tight radius yield nothing; widen the area or re-check coordinates.

## Gotchas & OpSec
- Depends on Snapchat's undocumented Map API — expect breakage when Snapchat changes it; check the repo issues if it stops working.
- Only *public* stories are accessible; private content is not exposed.
- Requires local setup (clone + dependencies) rather than a web UI.
- OpSec: passive — hits Snapchat's public endpoint, not posters. Store harvested media as sensitive evidence.

## Overlaps ("do both")
- Pairs with `[[snap-scraper]]` — two independent Snap Map scrapers; running both improves the chance of catching all public media at a location when one is broken or misses posts. Also do alongside Instagram/TikTok location search for cross-platform coverage.

## Trust & verifiability
`trust: community` — an open-source tool surfacing genuine public Snapchat content; its reliability tracks Snapchat's private API. Verify each story's location/time against its metadata rather than assuming the queried coordinates.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snapchat-map-scraper-nemec |
</content>
