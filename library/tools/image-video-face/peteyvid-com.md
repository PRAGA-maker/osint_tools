---
id: peteyvid-com
name: Petey Vid
description: Use when you have a `name`, `username` or keyword and want to find videos of the subject across non-YouTube platforms — returns social-profile and image/video leads.
url: https://www.peteyvid.com/
category: image-video-face
path:
- image-video-face
bestFor: Cross-platform video discovery — surfacing clips of a person or event on sites a normal Google/YouTube search misses.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
status: degraded
pricing: free
costNote: Free web search engine and browser extension; no account required. Domain was intermittently unreachable at last check — retry or use the browser add-on.
opsec: passive
opsecNote: Petey Vid advertises that it does not collect, save, or sell user data. You are searching an index, not contacting the subject, so queries are passive; still use a sock-puppet browser as a habit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent, privacy-focused video search engine covering 70+ platforms; results are third-party-hosted videos, so verify each source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- peteyvid
aliases:
- PeteyVid
- Petey Vid video search
tags:
- flickr
- video-search
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Petey Vid

> A privacy-focused video search engine that indexes 70+ platforms — the tool for finding footage of a person or event that lives outside YouTube.

## When to use
You have a `name`, `username`, hashtag, or event keyword and want to find video of the subject. Google and YouTube bias heavily toward YouTube; Petey Vid deliberately pulls from Facebook, Twitter/X, Vimeo, Instagram, Twitch, BitChute, DailyMotion, PeerTube and dozens more, so it surfaces clips those engines bury or omit. High value in missing-persons work where a subject's appearances may be scattered across minor platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.peteyvid.com/ (or install the browser extension if the site is slow to load).
2. Enter the `name`/`username`/keyword; you can search `#hashtags` and `@mentions` to catch social-video posts.
3. Scan results across platforms; each hit links out to the hosting site.
4. Pivot: an identified account or clip feeds `social-profile` enrichment; a video frame feeds reverse-image/face tooling and geolocation from background details.

## Inputs → Outputs
- **In:** `name`, `username`, hashtag or keyword
- **Out:** `social-profile` (accounts hosting the videos), `image`/video frames to analyse
- **Empty/negative result looks like:** few or no hits — common for private individuals with no video footprint; it does not index private/unlisted videos.

## Gotchas & OpSec
- Coverage and freshness vary by platform; a miss here is not proof no video exists. Cross-check with native platform search.
- The domain was intermittently unreachable at last verification — if it fails to load, retry or use the extension before assuming it is down.
- OpSec: passive; you query an index, and the operator states it does not retain user data.

## Overlaps ("do both")
- Pairs with reverse-image/face search — once Petey Vid finds a clip, pull a frame and run it to confirm identity and find stills elsewhere.

## Trust & verifiability
`trust: community` — an independent aggregator, not an authoritative source; every result is a third-party video you must open and verify at its origin.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peteyvid-com |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
