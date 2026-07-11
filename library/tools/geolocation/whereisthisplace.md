---
id: whereisthisplace
name: WhereIsThisPlace
description: Use when you have an `image` and want an AI's best guess at where it was taken — returns coordinates, a place name and supporting reasoning.
url: https://whereisthisplace.org
category: geolocation
path:
- geolocation
bestFor: Fast first-pass AI geolocation of a photo when you have no obvious landmark to search.
selectorsIn:
- image
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free to use (framed as a free trial / free tier); no install. Heavy or bulk use may hit limits.
opsec: passive
opsecNote: You upload the target's photo to a third-party AI service — that image (and any EXIF it still carries) leaves your control and may be logged or retained by the operator. Strip metadata and crop out sensitive/identifying detail before upload unless you accept exposing it, and use a sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community/indie AI geolocation site with no named accountable operator; it combines vision models, EXIF parsing, OCR and LLM reasoning. Treat its guesses as leads to verify, never as proof.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Where Is This Place
tags:
- kimi-2026
- geolocation
- ai-geolocation
source: kimi-geo
lastVerified: '2026-07-11'
enrichment: full
---

# WhereIsThisPlace

> An AI "guess where this photo was taken" service — a quick automated first pass at geolocating an image before you do manual landmark/shadow analysis.

## When to use
You have an `image` (a photo from a subject's social media, a proof-of-life shot, a scene you need to place) and there is no obvious searchable landmark. WhereIsThisPlace runs computer-vision landmark recognition, EXIF parsing, OCR of any visible text, and LLM reasoning to propose a location and coordinates in seconds — useful to generate a hypothesis you then confirm with street-level imagery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://whereisthisplace.org in a sock-puppet browser.
2. Upload the `image` (or paste a text description of the scene).
3. Read the returned `geolocation` (coordinates), place name and the reasoning/POI context it cites.
4. Treat the guess as a hypothesis — do NOT act on it alone.
5. Pivot: drop the coordinates into `[[maps-app-by-apple]]` / `[[google-street-view]]` and compare the panorama against the photo to confirm or reject; cross-check with a second AI geolocator like GeoSpy.

## Inputs → Outputs
- **In:** `image` (photo) or a scene description
- **Out:** `geolocation` (lat/long), a candidate `address`/place name, and supporting rationale
- **Empty/negative result looks like:** a vague country/region-level guess, low confidence, or an obviously wrong landmark match — generic interiors, plain nature and featureless scenes defeat it. Do not trust a confident-sounding guess without visual corroboration.

## Gotchas & OpSec
- AI geolocators hallucinate plausible-but-wrong places; always verify against real imagery before believing it.
- Uploading exposes the photo (and residual EXIF) to a third party — sanitize first.
- If the image still has GPS EXIF, that metadata is far more reliable than the AI guess — check EXIF yourself first with an EXIF viewer.

## Overlaps ("do both")
- Pairs with `[[maps-app-by-apple]]`, `[[google-street-view]]` and other AI geolocators (GeoSpy, Picarta) — run several, then confirm the consensus against street-level imagery. Each model is trained differently and catches scenes the others miss.

## Trust & verifiability
`trust: community` — an unaffiliated AI service with no accountability guarantee; outputs are probabilistic. Reliable only as a lead generator confirmed downstream.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whereisthisplace |
| category | geolocation |
| selectorsIn → selectorsOut | image → geolocation, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
