---
id: creepy
name: Creepy
description: Use when you have a target username and want a map of geolocation data scraped from their social/photo posts — returns plotted coordinates with source links.
url: https://github.com/ilektrojohn/creepy
category: image-video-face
path:
- image-video-face
- images
- tools
bestFor: Aggregate and map geotagged social-media / photo-sharing posts tied to a username.
input: A target username (Twitter/Flickr/Instagram historically)
output: A map of geolocated posts with timestamps and source links
selectorsIn:
- username
- social-profile
selectorsOut:
- geolocation
- metadata-exif
status: degraded
pricing: free
costNote: Free, open-source (Python/Qt desktop app).
opsec: passive
opsecNote: Pulls public posts via APIs/scraping; does not message the target. Historically needed Twitter/Flickr API keys, which are now largely defunct.
humanInLoop: true
humanInLoopReason:
- api-key
- account-login
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-known OSINT geolocation tool, but the upstream repo is effectively unmaintained and broke when Twitter/Instagram locked down their APIs.
missingPersonsRelevance: high
coverage: [global]
auth: api-key
api: false
localInstall: true
registration: false
relatedTools: [current-location, deepfind-me-2]
aliases:
- CreepyAI
- cree.py
tags:
- geolocation
- social-media
source: arf-seed
lastVerified: ''
enrichment: full
---

# Creepy

> A classic desktop geolocation OSINT tool that scraped a username's social/photo posts and plotted their locations on a map — historically powerful, now largely broken by API lockdowns.

## When to use
You have a `username` or `social-profile` and want to reconstruct a person's movement pattern or home-area from the geotags embedded in their public posts. When functional, it clusters locations on a map and exposes routine places (home, work, hangouts) — directly useful for narrowing a missing person's likely area.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Clone the repo and install the Python/Qt dependencies from https://github.com/ilektrojohn/creepy.
2. Configure plugin API keys (Twitter, Flickr, etc.) in the settings.
3. Create a project for the target `username`; let it harvest geotagged posts.
4. Read the map: clustered points reveal frequented `geolocation`s; click a point for the source post and `metadata-exif`/timestamp.
5. Pivot: corroborate clusters with `[[current-location]]` (geotagged photos near a place) and `[[deepfind-me-2]]` (street-view/satellite confirmation).

## Inputs → Outputs
- **In:** `username` / `social-profile`
- **Out:** `geolocation` (mapped post coordinates), `metadata-exif` (post timestamps/source)
- **Empty/negative result looks like:** an empty map — almost always because the platform API is closed or geotagging was disabled, not necessarily because the target has no posts.

## Gotchas & OpSec
- Human-in-the-loop: requires registering and pasting platform API keys; many of the plugins (Twitter/Instagram) no longer work since those platforms restricted access. Expect to fix or replace plugins, or to fall back to the community CreepyAI fork.
- OpSec: passive — reads public data only, no contact with the target. Use API keys tied to a sock account, not your real identity.

## Overlaps ("do both")
- Pairs with `[[current-location]]` and `[[deepfind-me-2]]` for geolocation triangulation; manual review of a profile's own posts often beats the automated harvest now.

## Trust & verifiability
`trust: community` — a well-known, long-standing OSINT project, but `status: degraded`: the upstream `ilektrojohn/creepy` repo is essentially unmaintained and most data-source plugins broke when the underlying social APIs changed. Treat any output as partial and verify each plotted point against the live source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | creepy |
| category | image-video-face |
| selectorsIn → selectorsOut | username, social-profile → geolocation, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes |
