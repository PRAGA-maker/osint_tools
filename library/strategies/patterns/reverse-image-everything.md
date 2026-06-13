---
id: reverse-image-everything
name: pattern-reverse-image-everything
description: Use as a reflex — reverse-search every image you touch before reasoning about it; it's seconds of work that can hand you the source, the location, the person, or proof it's a repost.
type: pattern
phase: pivot
pivotFrom:
- image
pivotTo:
- geolocation
- face
- social-profile
- name
platforms:
- any
summary: Reverse image search is the cheapest high-yield move in the toolkit, and the habit is to run it on EVERY image — profile photos, backgrounds, screenshots, memes the subject posted — before doing anything else with them. It can hand you the original source, the location, other copies attached to a name or profile, or the critical negative result that the image is a stock photo or repost and therefore NOT the subject's. Use several engines, because their indexes differ sharply.
missingPersonsRelevance: high
whenToUse: The instant any image enters the case, and again on every new image a pivot produces.
steps:
- Reverse-search every image immediately — before geolocating, face-searching, or building on it.
- Use multiple engines — Yandex (strong on faces/places), Google Lens (text-in-image), Bing — their indexes cover different web.
- Crop and re-search — isolate a distinctive sub-region (a sign, a face, a logo) and search that alone; full-frame and crop return different results.
- Read the negative result — if the image is stock/reposted, it's likely NOT the subject's; that's a finding, not a failure.
- Feed hits onward — a matched source/profile/location becomes a new selector to verify and pivot.
signals:
- An engine returns the original posting context — a source, a date, a profile, or a place.
- Multiple engines independently surface the same source — convergence.
pitfalls:
- Searching only one engine and concluding "nothing" — coverage gaps are huge; always try several.
- Skipping the crop — a busy full frame can bury the one distinctive element that would have matched.
- Treating a visual-similar result as the same image/person without verifying (similarity ≠ identity).
toolsUsed:
- yandex-images
- google-lens
- bing-visual-search
- tineye
evidence: []
trust: trusted
relatedStrategies:
- pivot-image-to-geolocation
- pivot-image-to-face
- pivot-exif-and-chronolocation
- pattern-breadth-before-depth
tags:
- image
- reflex
- high-yield
- cross-cutting
source: ''
---

# Pattern: Reverse-image everything

## The reflex
Before you reason about any image, reverse-search it. Profile photos, backgrounds, screenshots, even a meme the subject reposted — all of it. It costs seconds and routinely returns something that would have taken an hour to derive: the original source, the location, other copies tied to a name or profile, or the negative result that the image isn't even the subject's.

## Why it's the highest cheap-yield move
A reverse search can collapse multiple pivots at once. One hit might give you a **location** (skip manual geolocation), a **profile** (skip enumeration), and a **name** (skip disambiguation) — for free. It also front-runs the more expensive image pivots: there's no point hand-geolocating or face-searching an image that reverse search proves is stock. This is why it belongs to the breadth-first instinct in `[[pattern-breadth-before-depth]]` — it's the cheapest possible edge off an image node.

## Use several engines, and crop
- **Multiple engines.** Yandex is unusually strong on faces and places; Google Lens reads text inside the image; Bing and TinEye cover different corners. Their indexes diverge enormously, so "nothing on Google" means nothing until you've tried the others.
- **Crop and re-search.** A distinctive sub-region — a single sign, a logo, one face — searched alone often matches when the full busy frame doesn't. Full-frame and crop are different queries.

## The negative result is a result
If reverse search shows the image is a stock photo, a reposted celebrity shot, or a years-old viral image, that's a *finding*: it's probably not the subject's, and you've just saved yourself from geolocating or face-searching a decoy. Record it. A "no, it's a repost" is as valuable as a hit.

## Then pivot
Every match is a new selector — source, profile, place, name — and like every selector it's a candidate until `[[phase-verification]]`. Visual similarity is not identity; confirm before you build. From a hit, route into `[[pivot-image-to-geolocation]]` or `[[pivot-image-to-face]]` as appropriate.

---
## Metadata
| field | value |
|---|---|
| type | pattern |
| phase | pivot |
| pivot | image → geolocation, face, social-profile, name |
| MP relevance | high |
| tools | yandex-images, google-lens, bing-visual-search, tineye |
