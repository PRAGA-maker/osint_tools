---
id: icon-finder
name: Iconfinder
description: Use when you have a small graphic/logo/icon `image` and want to identify or source a matching stock icon — a graphic-asset marketplace, not a reverse image search of people or faces.
url: https://www.iconfinder.com
category: image-video-face
path:
- image-video-face
bestFor: Identifying or sourcing a stock icon/logo graphic; effectively never useful for locating a person.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: freemium
costNote: Free to search and browse; many icons are free, others are paid/licensed. A subset requires a paid plan or per-icon purchase to download.
opsec: passive
opsecNote: Passive stock-asset browsing — no target interaction. Nothing about a subject is queried or revealed. Standard browser hygiene only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established, legitimate icon marketplace. Trusted as a commercial asset library — but it is not an OSINT people-search or face-recognition tool despite its harvested category.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- iconfinder.com
- Icon Finder
tags:
- toddington
- curated-directory
- image-video-multimedia-search
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Iconfinder

> A stock-icon and graphic-asset marketplace — genuinely useful only to identify or source an icon/logo, not to find a person or match a face.

## When to use
Very rarely, in image work: you have a small graphic — an app icon, a UI glyph, a simple logo mark — and want to know if it's a stock asset and where it came from. Iconfinder's search can help identify that a graphic is off-the-shelf (which can debunk a "custom" brand or trace an image's provenance). It performs **no** face recognition or reverse-image search of photographs of people; the stub's `face` selector was mis-harvested. For finding a person from a photo, use a real reverse-image/face tool instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.iconfinder.com and search by keyword describing the graphic (shape, subject, style), or browse by style/collection.
2. Compare candidates visually against your source graphic to spot a match.
3. Read the output: matching stock icons with their designer/collection and license. A match tells you the graphic is a stock asset, not a bespoke identifier.
4. Pivot: if a "brand logo" turns out to be a stock icon, that undercuts claims of a real organization — feed that into your assessment rather than into a people search.

## Inputs → Outputs
- **In:** `image` (a small graphic/icon/logo)
- **Out:** `image` (matching stock icons + source/license), i.e. provenance of the graphic
- **Empty/negative result looks like:** no visually matching stock icon — which means it may be custom, or simply not in this library. It says nothing about any person.

## Gotchas & OpSec
- Wrong tool for people-finding: it does not identify faces or photos of individuals. Do not route a portrait here.
- Some downloads are paid/licensed; searching is free.
- OpSec: passive; no subject is contacted.

## Overlaps ("do both")
- For actual photo/face investigation, use a dedicated reverse-image or facial-recognition tool — Iconfinder only speaks to whether a graphic is stock art.

## Trust & verifiability
`trust: trusted` — a reputable commercial asset marketplace. The rating reflects the service, not investigative value: its usefulness for missing-persons work is marginal and limited to graphic-provenance checks.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | icon-finder |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
