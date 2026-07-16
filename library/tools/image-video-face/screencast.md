---
id: screencast
name: Screencast
description: Use when you have a `name`/`username` and want to find screen recordings, tutorial videos, or captured images a subject has published — returns hosted media and profile links.
url: https://www.screencast.com
category: image-video-face
path:
- image-video-face
bestFor: Locating publicly shared screen captures and videos hosted on TechSmith's Screencast platform.
selectorsIn:
- name
- username
selectorsOut:
- image
- social-profile
status: live
pricing: freemium
costNote: Free tier hosts and shares content with storage/expiration limits; paid Pro ($9.99/mo or $99.99/yr) removes limits. Viewing/searching public content is free.
opsec: passive
opsecNote: Viewing a public Screencast collection or watch page is passive browsing over HTTPS and does not notify the uploader. Signing in or commenting would attach your identity — stay logged out and use a sock-puppet browser if you must interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by TechSmith (makers of Snagit/Camtasia); first-party hosting platform, not a scraper — content is what the uploader chose to publish.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- TechSmith Screencast
- screencast.com
tags:
- toddington
- curated-directory
- image-video-multimedia-search
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Screencast

> TechSmith's hosting service for screen recordings and captured images — an occasional home for a subject's tutorials, gameplay clips, or how-to videos.

## When to use
You have a `name` or `username` and suspect the subject produced instructional or screen-capture content (software tutorials, recorded walkthroughs, annotated screenshots). Screencast is where Snagit/Camtasia users park and share that media, so a hit can surface video, imagery, and links back to other profiles the person controls.

## How to use it (`bestInteractionPattern`: web-manual)
1. Screencast has no strong site-wide search, so pivot from a link instead: run a search-engine query like `site:screencast.com <username>` or `site:app.screencast.com <name>` in a sock-puppet browser.
2. Open any hit — content now lives at `app.screencast.com` collection or watch pages (www.screencast.com 301-redirects there).
3. Read the media and collection metadata: title, description, upload date, and any author display name/avatar (`selectorsOut`: image, social-profile).
4. Pivot: an AI-generated or user-written caption may name software, employers, or collaborators; the display name feeds username-search tools.

## Inputs → Outputs
- **In:** `name` or `username` (used in an external site-scoped search)
- **Out:** hosted `image`/video, uploader display name, `social-profile` link
- **Empty/negative result looks like:** no indexed `screencast.com`/`app.screencast.com` pages for the selector — the subject simply hasn't published here (common; Screencast is a niche host).

## Gotchas & OpSec
- No public directory or reverse search on-site; you rely on external search-engine indexing, which misses unlisted/private collections.
- OpSec: passive viewing is safe; do not sign in or comment.
- Free-tier content can expire or be deleted — a cached copy in a search engine may outlive the live page.

## Overlaps ("do both")
- Pairs with a general video/multimedia search because Screencast only covers TechSmith-hosted media — the same person may have uploaded elsewhere (YouTube, Vimeo) that Screencast will never show.

## Trust & verifiability
`trust: trusted` — first-party TechSmith platform; the content is authentic uploader material, though captions may be AI-generated and should be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | screencast |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → image, social-profile |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
