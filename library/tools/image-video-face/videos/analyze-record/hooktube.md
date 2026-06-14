---
id: hooktube
name: Hooktube
description: Use only as historical reference — a now-defunct YouTube proxy/front-end that once let you view and download YouTube videos without the official player; it no longer functions for that purpose.
url: https://hooktube.com/
category: image-video-face
path:
- image-video-face
- videos
- analyze-record
bestFor: (Historical) lightweight YouTube viewing/downloading without the official player — now defunct.
input: A YouTube video URL or ID (historically)
output: (Historically) an embeddable player and direct download links
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
status: down
pricing: free
costNote: Was free; service is no longer operational for its original purpose.
opsec: passive
opsecNote: A YouTube front-end never contacts the channel owner. Historically it routed playback through its own servers; today the site does not provide the original functionality.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: HookTube was a YouTube proxy that was shut down / lost its core functionality after YouTube enforcement years ago. Current status of the domain is unverified; treat as defunct and use a maintained alternative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: true
relatedTools:
- google-videos
aliases: []
tags:
- youtube
- video-download
source: arf-seed
lastVerified: ''
enrichment: full
---

# Hooktube

> A historical YouTube proxy/front-end that once allowed lightweight viewing and downloading of YouTube videos outside the official player — now defunct.

## When to use
Effectively never for live work. HookTube was originally used to play and download YouTube clips (e.g. to preserve a video before it could be deleted) without loading the heavy official player or being logged in. After YouTube enforcement it lost that capability and the service is no longer reliable. Listed here for completeness and to redirect investigators to maintained alternatives.

## How to use it (`bestInteractionPattern`: web-manual)
1. Do not rely on it. If you reach the domain, assume the original download/playback feature is gone.
2. For the actual task — preserving or downloading a YouTube video as evidence — use `yt-dlp` (CLI) or a current video-archiving service instead.
3. To find the video in the first place, use `[[google-videos]]` or native YouTube search.

## Inputs → Outputs
- **In:** (historically) a YouTube `social-profile`/video URL
- **Out:** (historically) a player and download links; `metadata-exif` such as upload date/title from the page
- **Empty/negative result looks like:** site errors, redirects, or a non-functional player — the expected state today.

## Gotchas & OpSec
- Treat as deprecated; functionality has been removed/broken since YouTube enforcement years ago.
- Do not enter accounts or sensitive data into an unmaintained third-party proxy.
- OpSec: passive (you never contact the channel owner), but an abandoned proxy is an untrustworthy intermediary — avoid.

## Overlaps ("do both")
- Superseded by `yt-dlp` for downloading and by `[[google-videos]]`/native YouTube for discovery.

## Trust & verifiability
`trust: unverified` — known historically as a YouTube proxy that was shut down/crippled; current domain behavior not verified in this pass. Honestly flagged as defunct; do not depend on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hooktube |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
