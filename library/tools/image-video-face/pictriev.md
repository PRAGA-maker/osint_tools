---
id: pictriev
name: PicTriev
description: Use when you have a face photo and want to find visually similar faces / celebrity lookalikes or compare two faces — returns similar-face matches and a similarity score.
url: http://www.pictriev.com
category: image-video-face
path:
- image-video-face
bestFor: Finding visually similar faces and estimating likeness between two face photos.
selectorsIn:
- face
- image
selectorsOut:
- face
- name
status: live
pricing: free
costNote: Free to use; no account required.
opsec: active
opsecNote: Face images are uploaded to a third-party web service for matching.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing free face-matching/lookalike site widely cited in OSINT lists. Its index leans toward celebrity/public-figure faces, so it is weak at identifying private individuals.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- pictriev.com
tags:
- image-search
- face
- facial-comparison
source: awesome-osint
lastVerified: ''
enrichment: full
---

# PicTriev

> A free face-matching site that finds visually similar faces and compares two photos — handy for likeness checks, but its index favors public figures.

## When to use
You have a `face`/`image` and want to (a) find lookalikes or (b) gauge whether two photos are the same person. In a missing-persons context it is most useful as a quick similarity/comparison check between a known photo and an unidentified one, rather than a tool that names a private individual. Tie-in: `face` in, similar `face` + possibly `name` (if it matches a public figure) out.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.pictriev.com.
2. Upload a clear, front-facing `face` photo (or two, to compare them).
3. Read the similar-face results and/or the similarity percentage.
4. Treat percentages as soft signal — corroborate any "same person" conclusion with other evidence.
5. For real identity search of private individuals, pivot to [[pimeyes-2]].

## Inputs → Outputs
- **In:** `face`, `image`
- **Out:** `face` (similar faces), `name` (only when a public-figure match exists)
- **Empty/negative result looks like:** only loose celebrity lookalikes with no real-world identity — expected for ordinary private subjects.

## Gotchas & OpSec
- Human-in-the-loop: similarity scores require human judgment; do not treat a high percentage as identity confirmation.
- OpSec: active — images are uploaded to a third-party service. Avoid sensitive case photos.
- Index skews to celebrities; poor at finding non-public people. Works best with clear, frontal, well-lit faces.

## Overlaps ("do both")
- Pairs with [[pimeyes-2]] (broad biometric web search) — PicTriev for cheap comparison/lookalike, PimEyes for actual identity discovery.

## Trust & verifiability
`trust: community` — a real, widely-listed face tool, but limited to similarity/lookalike on a celebrity-leaning index; not a substitute for purpose-built face-search engines.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pictriev |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → face, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
