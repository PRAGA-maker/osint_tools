---
id: whentaken-com
name: whentaken.com
description: Use when you want to practice chronolocation and geolocation — a game that shows a photo and asks you to guess where and when it was taken, sharpening the skills you apply to real evidence photos.
url: https://whentaken.com/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Training your eye for dating and geolocating photographs from visual cues.
selectorsIn:
- image
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free browser game; no account required to play the daily challenge or archive.
opsec: passive
opsecNote: A self-contained browser game; you submit nothing about any real investigation. Purely passive — no target is involved.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent photo-guessing game, not an analytical tool; it produces no data about any real subject, so "trust" applies only to it being a legitimate free training site.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- WhenTaken
- whentaken game
tags:
- mapsandlocationsites
- Maps & Location Related Sites
- training
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# whentaken.com

> A GeoGuessr-style game for *time* as well as place — you're shown a photo and must guess both where and when it was taken. A skill-builder, not an investigative tool.

## When to use
Reach for this to **train**, not to work a case. It has no input for your own evidence photos and returns nothing about a real subject. What it builds is the exact analyst skill of reading a photograph for era (fashion, cars, signage, film grain, architecture) and place (vegetation, road markings, language, sun angle) — the reasoning you then apply for real to a subject's undated, unlocated image. Include it in an OSINT-practice rotation; skip it when you have an actual photo to geolocate (use analytical tools for that).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://whentaken.com/ and start the daily challenge (or the archive of past rounds).
2. Study the photo for temporal cues (vehicles, clothing, signage, media format) and spatial cues (terrain, architecture, language).
3. Drop a pin on the world map for the location and set the year slider (1860–present).
4. Submit and read the scoring, which reveals the true date and place — use the gap between your guess and truth to calibrate.
5. Transfer: apply the same cue-reading discipline to real undated/unlocated evidence images in your casework.

## Inputs → Outputs
- **In:** a game-supplied `image` (you cannot upload your own)
- **Out:** the correct `geolocation` and date of that game photo, plus a score — i.e. feedback, not intelligence about a subject
- **Empty/negative result looks like:** N/A — it always returns the answer for the game round; there is no "result" pertaining to a real investigation.

## Gotchas & OpSec
- **Not an analysis tool.** You cannot submit an unknown photo to have it dated/located; it only quizzes you on its own images. Don't reach for it expecting to geolocate evidence.
- Value is purely educational — treat it as practice, and use dedicated reverse-image/geolocation tools for real photos.
- OpSec: **passive** — nothing about any target leaves your browser.

## Overlaps ("do both")
- Complements real geolocation workflows (reverse-image search, mapping, shadow/sun analysis) by building the underlying visual-forensics intuition those workflows depend on.

## Trust & verifiability
`trust: community` — a legitimate free training game from the OSINT community; it is trustworthy as a game, but produces no verifiable intelligence, so never cite it as a source in a report.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whentaken-com |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | image → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
