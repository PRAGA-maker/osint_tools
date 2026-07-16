---
id: yasiv-youtube
name: YASIV YouTube
description: Defunct — was a YouTube related-video graph visualiser; the underlying API was shut down in 2020, so it no longer functions.
url: https://yasiv.com/youtube/
category: image-video-face
path:
- image-video-face
- videos
- analyze-record
bestFor: (Historic) visualising the graph of related YouTube videos around a seed video. No longer operational.
selectorsIn:
- username
selectorsOut:
- social-profile
status: down
pricing: free
costNote: Was free; now non-functional, so there is nothing to pay for or use.
opsec: passive
opsecNote: Not applicable — the tool no longer works. If it did, it would have been passive (read-only visualisation of public YouTube relationships).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Defunct project; the visualiser stopped working when Google revoked its API access in July 2020. Source code remains on GitHub but the hosted tool is dead.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: true
relatedTools:
- reddit-visualization
aliases:
- YASIV
- Youtube Related Videos Visualization
tags:
- youtube
- defunct
- deprecated
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# YASIV YouTube

> **Defunct.** YASIV was a graph visualiser for YouTube's "related videos" — enter a video and see its web of connections. Google shut off the API it relied on in July 2020, and the hosted tool no longer works.

## When to use
Do not rely on this for live investigations — it is dead. It is documented here so an agent recognises the name and doesn't waste time trying to use it. Historically you would seed it with a YouTube video to explore adjacent/related content and channels; today that capability is gone.

## How to use it (`bestInteractionPattern`: web-manual)
1. There is no working hosted tool — https://yasiv.com/youtube/ will not return useful results.
2. If you must reproduce the concept, the source code remains on GitHub, but it requires a YouTube "related videos" API that Google no longer provides, so it cannot be revived as-is.
3. For live YouTube relationship/analytics work, use maintained alternatives instead (see Overlaps).

## Inputs → Outputs
- **In:** (historic) a YouTube video/`username`
- **Out:** (historic) a `social-profile`/related-video graph — currently none
- **Empty/negative result looks like:** a non-loading or empty visualisation — the expected state now, because the backend API is permanently gone.

## Gotchas & OpSec
- **Deprecated:** treat any reference to YASIV as a dead end and substitute a live tool.
- The GitHub source is of historical/reference interest only.

## Overlaps ("do both")
- Use maintained YouTube tooling instead — the Digital Methods YouTube Data Tools and mattw.io utilities like `[[search-youtube-by-location]]` cover channel/related-content and geotag analysis that YASIV once approximated.

## Trust & verifiability
`trust: unverified` — the hosted tool is defunct; this record exists to mark it dead so it isn't mistaken for a working resource.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yasiv-youtube |
| category | image-video-face |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
