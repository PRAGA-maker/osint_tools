---
id: pictriev-2
name: Pictriev
description: Use when you have a `face`/`image` and want to find celebrity or public-figure lookalikes and an age/gender estimate — returns similar known faces (weak identity lead).
url: http://pictriev.com/
category: image-video-face
path:
- image-video-face
bestFor: Finding celebrity/public-figure lookalikes for a face and estimating apparent age/gender.
selectorsIn:
- face
- image
selectorsOut:
- physical-description
status: degraded
pricing: free
costNote: Free to use; no account. The site has long carried an "under construction" notice and can be flaky.
opsec: passive
opsecNote: You upload a face image to a third-party server. Do not upload a photo you don't want retained; strip metadata first. Use a sock-puppet browser. It matches against celebrities/public figures, not private individuals.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing hobbyist face-matching site; matches are against a celebrity dataset, so results are entertainment-grade leads, not identifications.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- pimeyes
- facecheck-id
aliases:
- PicTriev
- pictriev.com
tags:
- face-search
- face-recognition
- image-analysis
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Pictriev

> A lightweight face-matching toy: upload a face and it returns celebrity lookalikes plus an apparent age/gender read — useful as a weak corroborator, not an identifier.

## When to use
You have a `face` or `image` and want a quick apparent-age/gender estimate, or to test whether a face strongly resembles a known public figure (e.g. checking if a profile photo is a lifted celebrity/stock image). PicTriev matches against a celebrity dataset, so it will not identify a private individual — treat it as a first, low-cost sanity check before reaching for a true face-search engine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://pictriev.com/ (expect an "under construction"/dated interface; it can be flaky).
2. Upload a frontal JPG under ~200 KB — best results need the gap between the eyes wider than ~80 px.
3. Read the output: an apparent gender (masculine/feminine) and age estimate, plus ranked celebrity lookalikes with similarity scores.
4. Interpret: a very high match to a specific celebrity suggests the photo may be that celebrity (or a stock/borrowed image); a spread of weak matches means nothing conclusive.
5. Pivot: for actual identification of a non-celebrity, move to a real face-search engine like [[pimeyes]] or [[facecheck-id]].

## Inputs → Outputs
- **In:** `face` / `image` (frontal, well-lit, small JPG)
- **Out:** `physical-description` (estimated age/gender) and celebrity lookalike ranking
- **Empty/negative result looks like:** no confident matches, an error, or the page failing to process — common given its degraded state; don't infer anything from a non-result.

## Gotchas & OpSec
- **Celebrity-only dataset** — it cannot find a private person; a lookalike is not the same person.
- Degraded/"under construction" for years; expect intermittent failures and switch tools if it won't process.
- Age/gender estimates are rough — corroborate, never rely.
- OpSec: you upload a face to a third party; strip EXIF and use a sock puppet.

## Overlaps ("do both")
- Pairs with [[pimeyes]] and [[facecheck-id]] — those search the open web/faces for the actual person; use PicTriev only for the cheap age/gender/celebrity-lookalike read, then a real engine for identification.

## Trust & verifiability
`trust: community` — a hobbyist tool matching against celebrities; outputs are entertainment-grade leads. Never treat a PicTriev result as an identification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pictriev-2 |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → physical-description |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
