---
id: virtualvacation-us
name: virtualvacation.us
description: Use when you want to train street-level geolocation skills — a free GeoGuessr-style game (City Guesser) that drops you into a random location's video/street view and asks where you are.
url: https://virtualvacation.us/guess
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Practicing the environmental-clue reading that underpins real photo/video geolocation.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free browser game (City Guesser); no account required for the core modes.
opsec: passive
opsecNote: A self-contained browser game; you submit nothing about any real investigation. Purely passive — no target is involved.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A legitimate free GeoGuessr-style training game; it produces no intelligence about a subject, so "trust" applies only to it being a genuine practice tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whentaken-com
aliases:
- City Guesser
- virtualvacation.us
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- training
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# virtualvacation.us

> "City Guesser" — a free GeoGuessr-style game that immerses you in a random location's street video and asks you to place it. A skill-builder for real geolocation, not an analysis tool.

## When to use
Use it to **train**, not to work a case. It won't accept your own evidence and returns nothing about a subject. What it develops is the core street-level geolocation skill: reading vehicles, license-plate styles, road markings, signage language, flags, vegetation, and architecture to pin a location — exactly the reasoning you apply to a subject's real photo or video. Keep it in an OSINT-practice rotation; for an actual image, use analytical geolocation tools instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://virtualvacation.us/guess and pick a mode (Worldwide, a specific country, "No Moving", or a time-limit challenge).
2. Observe the immersive video/street scene — note cars, plates, signs, driving side, flora, and building styles.
3. Place your guess on the map and submit.
4. Read the reveal (true location + distance) and, importantly, note which clues you missed — that gap is the lesson.
5. Transfer: apply the same clue-reading discipline to real undated/unlocated evidence in casework.

## Inputs → Outputs
- **In:** a game-supplied scene (you cannot submit your own `geolocation`/media)
- **Out:** the correct `geolocation` for that round plus a score — feedback, not intelligence about a subject
- **Empty/negative result looks like:** N/A — it always reveals the round's answer; there is no result pertaining to a real investigation.

## Gotchas & OpSec
- **Not an analysis tool.** You cannot feed it an unknown photo to geolocate; it only quizzes you on its own scenes.
- Value is purely educational — use dedicated reverse-image, mapping, and shadow-analysis tools for real evidence.
- OpSec: **passive** — nothing about any target leaves your browser.

## Overlaps ("do both")
- Pairs with [[whentaken-com]] (guess *when* as well as *where*) — together they train both the geolocation and the chronolocation halves of photo analysis.

## Trust & verifiability
`trust: community` — a legitimate free training game; trustworthy as practice, but it yields no verifiable intelligence, so never cite it as a source in a report.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | virtualvacation-us |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
