---
id: getlostgame-app
name: Get Lost (getlostgame.app)
description: Use when you want to train and sharpen geolocation skills on random street-view scenes — a free GeoGuessr-style game; it builds the skill, it does not look up your case.
url: https://getlostgame.app/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Practising photo/street-view geolocation as a skill via a free GeoGuessr-style game — training, not investigative lookup.
selectorsIn:
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free to play; an optional login saves scores but isn't required.
opsec: passive
opsecNote: Fully passive — you play against random street-view panoramas, not any target. Nothing about a real case is submitted. No opsec concern beyond normal browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A GeoGuessr-alternative browser game; legitimate and free, but it is a training/entertainment tool, not a data source — it produces no investigative output.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Get Lost game
- getlostgame.app
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- geolocation-training
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Get Lost (getlostgame.app)

> A free GeoGuessr-style game that drops you into random street-view scenes to guess the location — a way to *train* the geolocation skill, not a tool that looks anything up.

## When to use
When you want to build or keep sharp the core OSINT skill of reading location cues (road markings, signage, vegetation, architecture, sun position) from street-level imagery. Get Lost gives repeated, scored practice at exactly that. Reach for it as skills training between cases — it will not geolocate a real photo for you; it presents random panoramas and asks you to guess.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://getlostgame.app/ and start a round (5 rounds per game).
2. Study the street-view panorama for clues — language on signs, driving side, road paint, flora, terrain, utility styles.
3. Click the map where you think you are; scoring reflects distance to the true location (up to ~5,000/round).
4. Review the reveal to learn which cues you read right or missed.
5. Transfer the practice: apply the same cue-reading discipline to real geolocation using street-view/satellite tools.

## Inputs → Outputs
- **In:** `image` (the game's random street-view scene — not your evidence)
- **Out:** a `geolocation` guess and score — a *learning* signal, not case intelligence
- **Empty/negative result looks like:** N/A — this is a game; it never returns data about a subject or a real investigation.

## Gotchas & OpSec
- Not an investigative tool — it cannot analyse a photo you provide; it only serves random scenes.
- Value is skill-building; don't catalogue its output as evidence.
- OpSec: none beyond normal browsing.

## Overlaps ("do both")
- Complements real geolocation tools (street-view, satellite, cue databases) — this trains the eye, while those do the actual case work.

## Trust & verifiability
`trust: community` — a legitimate, free training game; there's nothing to "verify" because it produces no investigative data — its worth is purely in practising the skill.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | getlostgame-app |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | image → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
