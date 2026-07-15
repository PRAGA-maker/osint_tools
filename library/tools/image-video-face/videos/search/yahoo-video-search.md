---
id: yahoo-video-search
name: Yahoo Video Search
description: Use when you have a `name`/phrase and want a non-Google video index to find clips featuring a subject or place — returns video results (with `image` thumbnails) that may show a `face` or `geolocation`.
url: https://video.search.yahoo.com/
category: image-video-face
path:
- image-video-face
- videos
- search
bestFor: A second video search engine to surface clips (across hosts) that Google/YouTube search may rank differently or omit.
selectorsIn:
- name
selectorsOut:
- image
- face
- social-profile
status: live
pricing: free
costNote: Free; no account. Aggregates video results (largely via the Bing index) across YouTube, Dailymotion, Vimeo and other hosts.
opsec: passive
opsecNote: Passive search against Yahoo/Bing — the subject is not notified. Clicking through to a host (YouTube etc.) is where you may be observed; do so logged out / sock-puppet. Sensitive queries from a clean session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Yahoo; legitimate aggregated video results (Bing-powered), distinct in ranking from Google/YouTube search.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- yahoo-com
- print-youtube-storyboard-instructions
aliases:
- video.search.yahoo.com
tags:
- video-search
- Video Related Sites
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Yahoo Video Search

> A cross-host video search engine — worth a pass because it indexes and ranks clips differently from Google/YouTube, surfacing videos of a subject, event or place that the majors bury.

## When to use
You want video footage tied to a `name`, event, or `geolocation` and don't want to rely only on YouTube's own search or Google. Yahoo Video Search aggregates results across YouTube, Dailymotion, Vimeo and others, so it can surface a re-upload, a mirror, or a differently-titled clip that a single-platform search misses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://video.search.yahoo.com/ and search the subject name, handle, event, or place (use quotes for exact phrases).
2. Scan the thumbnail grid; hover/preview to judge relevance before clicking through.
3. Filter/sort where offered (duration, recency) to narrow.
4. Open promising clips at their host from a clean session.
5. Pivot: extract frames (pair with `[[print-youtube-storyboard-instructions]]`) for reverse-image/face/geolocation analysis; re-run the same query on `[[yahoo-com]]` and Google for coverage.

## Inputs → Outputs
- **In:** `name` / phrase / event / place term
- **Out:** video results with `image` thumbnails; clips may reveal a `face`, a `geolocation`, or link to a `social-profile`/channel
- **Empty/negative result looks like:** no relevant clips across a few query variants suggests no indexed video under that term — verify on YouTube search and Google Video before concluding none exists.

## Gotchas & OpSec
- Results are Bing-powered, so overlap with Bing Video is high; still distinct from Google/YouTube.
- Thumbnails can be misleading; confirm content by viewing the clip.
- Videos disappear/get re-uploaded — note the host and grab a copy/frames of anything important promptly.

## Overlaps ("do both")
- Run alongside YouTube search, Google Video and Bing Video — different indexes catch different uploads; then use frame-extraction and reverse-image tools on what you find.

## Trust & verifiability
`trust: trusted` — a legitimate major-provider aggregator; the result links are genuine, but verify each clip's content and provenance at the host before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yahoo-video-search |
| category | image-video-face |
| selectorsIn → selectorsOut | name → image, face, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
