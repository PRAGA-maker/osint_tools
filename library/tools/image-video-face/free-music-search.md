---
id: free-music-search
name: Free Music Search
description: Use when you need to search for and identify a song or music track by name/artist online — returns links to matching audio/sources; marginal for missing-persons work.
url: http://musgle.com/
category: image-video-face
path:
- image-video-face
bestFor: Web-based music/song search and discovery (musgle.com aggregates music search).
selectorsIn:
- name
selectorsOut:
- metadata
status: degraded
pricing: free
costNote: Free site; an older, possibly intermittently maintained music search front-end.
opsec: passive
opsecNote: Ordinary web search over public music sources; no subject is contacted. Standard browsing telemetry only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: 'Identified only from name/URL (musgle.com = "Google for music"); appears to be a song-search aggregator, not an image/face tool. Miscategorized under image-video-face. Not verified live.'
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Musgle
tags:
- music-search
- audio
source: osint4all
lastVerified: ''
enrichment: full
---

# Free Music Search

> A web front-end (musgle.com) for searching and discovering music tracks — an audio/music search aggregator, not an image or face tool.

## When to use
Rarely, in missing-persons context. If a case involves identifying a song heard in a video or referenced by a subject, you could search the track here by `name`/title. It does not analyze images, faces, or video despite the catalog category it was filed under.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://musgle.com/ and enter a song title or artist (`name`).
2. Read the returned links to matching tracks/sources (`metadata`).
3. Pivot: use any identified track/artist as a lead in broader profile or social searches; otherwise this is a dead-end for image/face work.

## Inputs → Outputs
- **In:** `name` (song/artist title)
- **Out:** `metadata` (links to matching music sources)
- **Empty/negative result looks like:** No results or a non-loading page — the site is old and may be degraded or down.

## Gotchas & OpSec
- Miscategorized: this is a music search engine, not an image/face/video forensics tool — do not expect reverse-image or facial features.
- Reliability is uncertain; the project is dated and may be defunct.
- OpSec: passive web search; nothing leaks to a subject.

## Overlaps ("do both")
- For actual audio/song identification, dedicated services (Shazam-class tools) are more reliable; this entry is retained only as harvested.

## Trust & verifiability
`trust: unverified` — identity inferred from name and URL only; honest description, not verified against a live fetch, and clearly off-category for image/face OSINT.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-music-search |
| category | image-video-face |
| selectorsIn → selectorsOut | name → metadata |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
