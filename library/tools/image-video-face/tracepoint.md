---
id: tracepoint
name: TracePoint
description: Use when you have an `image` with visible directional features and want to triangulate where the camera stood — returns an estimated `geolocation`.
url: https://kluter.github.io/TracePoint/
category: image-video-face
path:
- image-video-face
bestFor: Manually triangulating a photo's camera position by drawing rays from landmarks onto a map.
selectorsIn:
- image
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, open, static web app hosted on GitHub Pages; no account, no server-side upload.
opsec: passive
opsecNote: The tool runs entirely in your browser (GitHub Pages static site) — the image is not uploaded to a third-party server, so analysis leaks nothing about the target. It uses a web map tile provider, so the map areas you pan to are visible to that provider's servers; that reveals your area of interest, not the target.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source hobby/geolocation tool by an individual (kluter); the math is transparent, but accuracy depends entirely on the analyst's landmark identification.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- kluter TracePoint
- photo triangulation tool
tags:
- image-analysis
- geolocation
- geoint
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# TracePoint

> A browser-based triangulation aid: draw sight-lines from features in a photo onto a real map, and it estimates where the camera was standing — no EXIF required.

## When to use
You have an `image` (of a missing person's last-known location, a ransom/proof-of-life photo, a vehicle, a landscape) with **no GPS EXIF**, but it shows features you can identify on a map — a road heading a known direction, a distinctive building edge, a mountain, a shadow. You want to convert that visual geometry into a `geolocation` for the camera. It complements, and is used when you lack, automated geolocation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://kluter.github.io/TracePoint/ and load your image into the app.
2. Identify a feature in the photo whose real-world location you can find on the map (e.g. a church spire, an intersection).
3. Draw a line in the photo aligned to that feature's bearing, then place the corresponding reference point on the integrated map.
4. Repeat for at least two or three distinct features; the intersection of the rays triangulates the camera position, and with 3+ rays the tool draws a confidence ellipse.
5. Read the estimated `geolocation`; pivot the coordinates into a map/street-view check or a public-records address lookup.

## Inputs → Outputs
- **In:** `image` + your own map/landmark knowledge (`geolocation` reference points)
- **Out:** estimated camera `geolocation` with a confidence ellipse
- **Empty/negative result looks like:** rays that don't converge (a huge or empty ellipse) — your landmark identifications are inconsistent or the photo lacks enough separated, identifiable features. Re-examine the image.

## Gotchas & OpSec
- Human-in-the-loop: **yes, heavily** — this is a manual-review tool. It does no automatic recognition; every ray depends on you correctly matching a photo feature to a map location. Garbage in, garbage out.
- OpSec: **passive** — image analysis is client-side; nothing about the target leaves your machine. The base-map tile provider sees which map areas you browse.
- It estimates the *camera* position, not the subject's position; account for the distance between photographer and subject.

## Overlaps ("do both")
- Pairs with `[[publer-io-3]]` — archive a video/photo first, then triangulate a still frame here.

## Trust & verifiability
`trust: community` — open, transparent triangulation math from an individual developer. The result is an analyst-driven estimate; corroborate the coordinates with satellite/street imagery before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tracepoint |
| category | image-video-face |
| selectorsIn → selectorsOut | image, geolocation → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
