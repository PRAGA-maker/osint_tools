---
id: geoguesser
name: GeoGuessr
description: Use when you want to train geolocation and visual-intelligence skills — a game that drops you in Street View and rewards identifying a place from landmarks, signage and vegetation.
url: https://www.geoguessr.com/
category: training-ctf
path:
- training-ctf
- games
bestFor: Practising the "where was this photo taken?" skill core to image geolocation.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free limited play; a GeoGuessr Pro subscription unlocks unlimited maps/modes. Requires a (free) account to play.
opsec: passive
opsecNote: Training tool, not an investigative one — it only uses public Street View imagery and touches no target. You register an account with GeoGuessr; use a sock-puppet email if you prefer to keep it separate.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial geography game, not an OSINT data source; its value here is skill-building, not evidence.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- geoguessr.com
tags:
- training
- geolocation
- visual-intelligence
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# GeoGuessr

> Geolocation flight simulator: repeatedly guess "where in the world is this?" from Street View, and your eye for place-clues gets sharp fast.

## When to use
You want to build or drill the core geolocation skill — reading a scene for country/region/exact-spot clues: road markings, license plates, signage language, driving side, utility poles, vegetation, sun position, architecture. GeoGuessr is a training environment for exactly the "chase the clues in an image" muscle you use when geolocating a real photo or video in an investigation. Use it to practise, not as an evidence source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free GeoGuessr account at https://www.geoguessr.com/ (sock-puppet email if you like).
2. Start a game — you're dropped into a Street View panorama; pan and look for clues.
3. Reason deliberately: language on signs → country; road/plate style → region; then narrow with terrain and specific landmarks. Place your guess on the map.
4. Review the reveal and your distance/score; note which clue would have narrowed it faster.
5. Transfer: apply the same clue-hierarchy to real casework, and pair with mapping/street-view tools when geolocating an actual image.

## Inputs → Outputs
- **In:** none (a training game — no target selector)
- **Out:** a sharpened ability to infer `geolocation` from visual clues; per-round scoring feedback
- **Empty/negative result looks like:** n/a — this is practice, not a lookup; a low score just marks a skill gap to work on.

## Gotchas & OpSec
- Human-in-the-loop: an account/login is required to play.
- It is not an OSINT data source — never present a GeoGuessr result as investigative evidence; it only trains the analyst.
- Free tier is limited; unlimited modes need Pro.
- OpSec: passive; public imagery only, no target interaction.

## Overlaps ("do both")
- Complements real geolocation tooling — GeoGuessr builds the skill; actual street-view/mapping and reverse-image tools apply it to a real photo.

## Trust & verifiability
`trust: unverified` — a commercial geography game; its worth here is pedagogical, so there's no data-quality question, only the reminder that it produces practice, not evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geoguesser |
| category | training-ctf |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
