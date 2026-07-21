---
id: osint-essentials
name: OSINT Essentials
description: Use when you have an `image`, `geolocation`, `name`, or `username` and need a curated jump-off list of vetted verification/geolocation/people tools — returns pointers to social-profile and geolocation resources.
url: https://www.osintessentials.com/
category: image-video-face
path:
- image-video-face
bestFor: A curated, verification-focused directory of image/video, geolocation, social-media, and people-search tools for journalists and researchers.
selectorsIn:
- image
- geolocation
- name
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free directory; the linked tools are mostly free (some have optional paid tiers).
opsec: passive
opsecNote: The directory itself is just reading a webpage — no target interaction. OpSec risk lives in the individual tools it links to; assess each one before use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running verification resource curated by Eoghan Sweeney (First Draft lineage); a hand-picked directory, not an automated scraper.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- osintessentials.com
- OSINT Essentials directory
tags:
- verification
- image
- geolocation
- directory
source: ultimate-osint
lastVerified: '2026-07-21'
enrichment: full
---

# OSINT Essentials

> A hand-curated, verification-first directory of the tools working journalists and researchers actually use — strongest for image/video verification and geolocation.

## When to use
You are early in an investigation with an `image`, a suspected `geolocation`, or a `name`/`username`, and you want a vetted shortlist of tools rather than a raw awesome-list dump. Reach for it to pick the right reverse-image engine, metadata viewer, satellite/street-view resource, or people/username tool for the task at hand — especially when verifying or geolocating photos/video that may show a missing person or a location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.osintessentials.com/ and choose the relevant category: Social Media, Geolocation, Video/Photo/Audio, Transportation, People Search, or Website Analysis.
2. Each entry is a short description plus a link to the actual tool. Pick the one that matches your selector (e.g. reverse-image engines for an `image`, mapping/imagery tools for a `geolocation`).
3. Use the linked tool directly; return to the directory to try alternates when one comes up empty.
4. Pivot: it is a launchpad — the outputs come from the tools it points you to (a matched `social-profile`, a confirmed `geolocation`), not from OSINT Essentials itself.

## Inputs → Outputs
- **In:** `image`, `geolocation`, `name`, or `username` (whatever you're trying to work)
- **Out:** curated pointers to tools that yield `social-profile`, `geolocation`, and verification results
- **Empty/negative result looks like:** nothing to "search" here — if a category has no tool fitting your need, it simply isn't listed; this is a directory, not a database.

## Gotchas & OpSec
- Human-in-the-loop: none for the directory itself.
- It is curated by hand, so it lags the bleeding edge and a few links may rot over time — verify a linked tool is still live before relying on it.
- OpSec: passive at the directory level; the real OpSec profile is whatever downstream tool you pick, so read each tool's own considerations.

## Overlaps ("do both")
- Complements broad awesome-lists and other OSINT directories — OSINT Essentials is smaller and vetted for verification work, so use it to choose quality tools and the big lists for breadth.

## Trust & verifiability
`trust: trusted` — a respected, human-maintained resource with First Draft/verification-journalism lineage. It vouches for the tools it lists but is not itself a data source; trust flows to the underlying tools you select.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-essentials |
| category | image-video-face |
| selectorsIn → selectorsOut | image, geolocation, name, username → social-profile, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
