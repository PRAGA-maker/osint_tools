---
id: geocreepy
name: Geocreepy (Creepy)
description: Use when you want to aggregate a target's geotagged social-media posts onto a map to infer locations/pattern-of-life — returns `geolocation` points. NOTE largely defunct; the social APIs it relied on are gone.
url: http://www.geocreepy.com
category: social-networks
path:
- social-networks
bestFor: (Historical) mapping a person's geotagged posts from Twitter/Flickr/Instagram to reveal frequented locations and movement patterns.
selectorsIn:
- username
selectorsOut:
- geolocation
status: down
pricing: free
costNote: Free and open-source (ilektrojohn/creepy on GitHub), but effectively non-functional — it depended on Twitter/Flickr/Instagram APIs and geotag access that have since been closed or restricted.
opsec: passive
opsecNote: It analyzed already-public geotagged posts, so it didn't contact the target — passive by design. If a working fork is used, it needs API keys tied to your accounts; use dedicated credentials and note most platforms no longer expose the geodata it needs.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: desktop-app
trust: community
trustNote: A well-known but now-abandoned geolocation OSINT project; the concept is foundational, but modern API/geotag restrictions have broken its data sources.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- Creepy
- cree.py
- geocreepy
tags:
- real-time-search-social-media-search-and-general-social-media-tools
- geolocation
- geotag-mapping
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Geocreepy (Creepy)

> The classic geolocation-OSINT aggregator — it plotted a target's geotagged posts on a map to expose where they'd been. Now largely defunct: the platform APIs and geotags it fed on are gone.

## When to use
The intended use-case is powerful: given a `username`, pull all of that person's geotagged social-media posts and plot them on a map/timeline to reveal home, work, routines, and movement — gold for a missing-persons pattern-of-life. In reality, verify before relying on it: Creepy depended on Twitter/Flickr/Instagram location data that platforms have since removed or locked behind paid/closed APIs, so it typically returns little or nothing today.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Obtain the tool (the `www.geocreepy.com` site is unreliable; the code lives at github.com/ilektrojohn/creepy — archived).
2. Install the desktop app and supply API keys for the sources it supports.
3. Enter the target `username`; it queries the platforms for geotagged posts and plots them.
4. Read the map/timeline for clustered `geolocation` points (frequented places) and outliers.
5. Reality check: expect empty/sparse results due to API/geotag loss — pivot to current geolocation methods (EXIF from images, manual per-post geodata, `[[freemaptools]]` for spatial reasoning).

## Inputs → Outputs
- **In:** `username` (per supported platform)
- **Out:** `geolocation` points (mapped geotagged posts), movement/pattern-of-life visualization
- **Empty/negative result looks like:** no points plotted — now the normal outcome, because platforms stripped public geotags and closed the APIs. Absence here reflects the tool's dead data sources, not the subject's absence.

## Gotchas & OpSec
- **Down/abandoned:** its data sources are broken; do not expect it to work on modern accounts.
- Passive by design (public geotags), but needs your API keys where any source still functions.
- The concept remains valid — apply it manually via image EXIF and per-post location data.

## Overlaps ("do both")
- Pairs with EXIF/geolocation extractors and `[[freemaptools]]` — since Creepy's automation is dead, do the geolocation work manually: harvest per-post/image location data and map it yourself.

## Trust & verifiability
`trust: community` — a foundational but unmaintained project. Any point it does plot comes from a real public geotag; just don't expect coverage, and corroborate every location independently.
