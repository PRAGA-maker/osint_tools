---
id: watannetwork-com
name: watannetwork.com
description: Use when you have a YouTube video URL/ID and want to see which countries it is available or blocked in — returns geolocation (country allow/block list).
url: https://watannetwork.com/tools/blocked/#search
category: image-video-face
path:
- image-video-face
bestFor: Checking the country-by-country availability of a YouTube video (region-restriction map).
selectorsIn:
- social-profile
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free web tool; no account or payment required.
opsec: passive
opsecNote: You query WatanNetwork's own servers about a public YouTube video ID; the video owner is not notified. Nothing about your subject is submitted — only the video reference. Use a clean browser if you prefer not to associate the lookup with your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party utility run by WatanNetwork; it reports YouTube's own region-restriction metadata but is not affiliated with Google, so treat the map as indicative rather than authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WatanNetwork YouTube region checker
- YouTube blocked-countries checker
tags:
- youtube
- YouTube Related Sites
- geo-restriction
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# watannetwork.com

> A YouTube region-restriction checker: paste a video and see the map of which countries can and cannot watch it.

## When to use
You have a YouTube video (URL or ID) tied to a subject or event and want to understand its geo-restriction footprint — e.g. a video says "the uploader has not made this video available in your country" and you need to know where it *is* viewable, or you want to infer the intended/origin audience of a clip from its allow/block pattern. This is a video-metadata utility, not a people-finder; its missing-persons value is marginal (corroborating where content was meant to circulate).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://watannetwork.com/tools/blocked/#search.
2. Paste a full YouTube URL, a shortened link, or a bare 11-character video ID into the search box and submit.
3. Read the output: an interactive world map plus explicit lists of **allowed** and **blocked** countries.
4. Pivot: an unusual block/allow pattern (e.g. viewable only in one country) can hint at the uploader's region or licensing; combine with channel-level OSINT.

## Inputs → Outputs
- **In:** `social-profile` (a YouTube video URL / video ID / channel link)
- **Out:** `geolocation` (per-country allowed vs blocked list, shown on a map)
- **Empty/negative result looks like:** a video available everywhere returns an all-allowed map with no blocked countries; an invalid/removed ID returns no result — that is not evidence of restriction, just a bad or dead video reference.

## Gotchas & OpSec
- Human-in-the-loop: none; it is a single-field lookup.
- OpSec: passive — you only submit a public video reference, never anything about your subject. The uploader receives no notification.
- The restriction data reflects YouTube's metadata at query time; owners can change availability, so re-check if timing matters.

## Overlaps ("do both")
- Complements general video-download/metadata tooling like `[[tiktok-video-downloader-chromewebstore-google-com]]` — that grabs the media file, this reveals distribution geography.

## Trust & verifiability
`trust: unverified` — an independent third-party utility, not a Google product. It surfaces YouTube's own region-lock metadata, so results are usually accurate, but there is no guarantee of freshness or completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | watannetwork-com |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
