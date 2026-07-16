---
id: shadow-finder
name: Shadow Finder
description: Use when you have an `image` with a measurable shadow and a known object height, date, and time — returns the set of earth locations where that shadow could occur.
url: https://github.com/bellingcat/ShadowFinder
category: geolocation
path:
- geolocation
bestFor: Chronolocation/geolocation — mapping every point on Earth where a shadow of a given length could fall at a specified date and time, given the casting object's height.
selectorsIn:
- image
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free and open source (Bellingcat, on GitHub). Runs as a Python package/CLI locally, or via the hosted Bellingcat web app; no account.
opsec: passive
opsecNote: Analysis runs on your own machine (or Bellingcat's hosted app) from measurements you supply — nothing is sent to the subject and no one is notified. Fully passive. If you use the hosted version, your inputs pass through Bellingcat's server; run the local package to keep everything offline.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: trusted
trustNote: Published and maintained by Bellingcat; open-source, transparent astronomy math, and widely used in verified geolocation investigations.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- instagram-location-search
- auto-archiver
- bellingcat-tiktok-hashtag-analysis
- telegram-phone-number-checker-github-com
- wayback-google-analytics
aliases:
- ShadowFinder
tags:
- bellingcat-toolkit
- geolocation
source: bellingcat-toolkit
lastVerified: '2026-07-16'
enrichment: full
---

# Shadow Finder

> Bellingcat's shadow-based geolocation tool — from a shadow's length, the object's height, and a known date/time, it maps the band of latitudes/longitudes on Earth where that shadow is geometrically possible.

## When to use
You have an outdoor `image` where you can measure a shadow (e.g. a person or pole whose height you can estimate) and you know (or can bound) the date and time — but not the place. Shadow Finder inverts the sun geometry to produce a global heat-line of candidate locations, dramatically narrowing where the photo was taken. It's the counterpart to sun-position tools: those need a location; this one finds it.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install the package (`pip install shadowfinder`) or use Bellingcat's hosted ShadowFinder web app.
2. Measure from the image: the shadow length and the height of the object casting it (same units), and note the date and UTC time.
3. Enter object height, shadow length, and the date/time.
4. Run it — the output is a world map highlighting all points where a shadow of that ratio occurs at that instant.
5. Combine with other clues (hemisphere, landscape, language, `[[instagram-location-search]]` hits) to collapse the band to a specific area.
6. Pivot: the candidate band feeds targeted imagery/streetview checks and cross-references with any independent location clue.

## Inputs → Outputs
- **In:** an `image`-derived shadow length + object height + date/time (optionally an approximate `geolocation` to constrain)
- **Out:** a `geolocation` band — the set of possible latitudes/longitudes consistent with the shadow
- **Empty/negative result looks like:** an implausibly huge band, or none, when the time is wrong/uncertain or measurements are off — garbage-in shows as a uselessly wide result; tighten the time and re-measure.

## Gotchas & OpSec
- Accuracy hinges on precise height, shadow length, and especially the **time** — small time errors smear the band; an unknown time makes it near-useless.
- It returns a line/band, not a point — always fuse with other geolocation evidence to localize.
- Terrain slope and camera perspective distort shadow measurement; measure on flat ground where possible.
- OpSec: passive; run the local package to keep inputs off any server.

## Overlaps ("do both")
- Pairs with sun-position tools (SunCalc, Gaisma) and `[[instagram-location-search]]` — Shadow Finder proposes candidate locations from a shadow; sun-position tools then verify a specific candidate, and location-search tools supply independent place clues.

## Trust & verifiability
`trust: trusted` — Bellingcat-maintained, open-source, and based on transparent astronomical calculation you can reproduce; the method is sound, so reliability depends on your input precision.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shadow-finder |
| category | geolocation |
| selectorsIn → selectorsOut | image, geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
