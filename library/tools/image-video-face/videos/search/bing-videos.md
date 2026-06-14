---
id: bing-videos
name: Bing Videos
description: Use when you have a name, event, or place and want to find video clips that may show a missing person, vehicle, or location.
url: https://www.bing.com/videos
category: image-video-face
path:
- image-video-face
- videos
- search
bestFor: Keyword and topical video search across the open web with strong thumbnail-grid preview.
input: ''
output: ''
selectorsIn:
- name
- geolocation
- address
selectorsOut:
- social-profile
- metadata
status: live
pricing: free
opsec: passive
opsecNote: Searches Microsoft's index; queries are logged by Microsoft but the target is not contacted. Use a clean/sock browser session to avoid tying searches to your identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Microsoft; a mainstream, well-maintained search engine. Results themselves are third-party and must be verified.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# Bing Videos

> Microsoft's web-wide video search — a second engine to run alongside Google/YouTube so you catch clips one index misses.

## When to use
You have a `name`, a place (`geolocation`/`address`), an event, or a phrase from a caption, and you want to surface videos (news footage, social uploads, livestream clips) that might show a missing person, a vehicle, or a last-known location. Particularly useful as a cross-check because Bing indexes some social/regional video that Google ranks differently.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.bing.com/videos and enter your query (name, place, event, or quoted caption text).
2. Use the filter bar (Length, Date, Resolution, Source) to narrow — "Date" is the key OSINT filter for time-bounding around a disappearance.
3. Hover thumbnails for an autoplay preview to triage without opening the host site.
4. Pivot: open promising clips on their host platform (YouTube, TikTok, news site) to read uploader, comments, and posting metadata, which feed `social-profile` leads.

## Inputs → Outputs
- **In:** `name`, `geolocation`, `address` (as keywords)
- **Out:** candidate videos → `social-profile` (uploader accounts), `metadata` (upload date, source platform)
- **Empty/negative result looks like:** generic stock/unrelated clips, no date-relevant hits. Refine with quoted phrases or add location terms.

## Gotchas & OpSec
- No login required; passive. Microsoft logs the query — use a sock/clean session for sensitive work.
- Results are heavily SEO-influenced; rank ≠ relevance. Always open the source to confirm.
- It indexes embeds, so a "Bing video" may just be a page hosting someone else's clip — trace to the true origin.

## Overlaps ("do both")
- Run alongside YouTube search and Google Video; each index ranks regional and social uploads differently, so coverage diverges.

## Trust & verifiability
`trust: trusted` — mainstream Microsoft engine. The engine is reliable; individual results are unverified third-party content you must corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bing-videos |
| category | image-video-face |
| selectorsIn → selectorsOut | name, geolocation, address → social-profile, metadata |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
