---
id: redditvids
name: redditvids
description: Use when you have a Reddit post/video URL and want to view or save the clip with its audio merged — returns a playable/downloadable video file for evidence capture.
url: https://redditvids.com
category: social-networks
path:
- social-networks
bestFor: Viewing and saving a Reddit-hosted video with sound (Reddit stores audio and video separately).
selectorsIn:
- username
selectorsOut:
- image
status: live
pricing: free
costNote: Free web tool; no account or install required.
opsec: passive
opsecNote: You paste a public Reddit URL into a third-party site — the subject is not notified, but the operator sees which post you fetched. Use a sock-puppet browser if the specific post would reveal your investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: One of many interchangeable third-party Reddit video downloaders; unaffiliated with Reddit, so verify the saved file matches the original post and preserve provenance.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- redditvids.com
tags:
- reddit
- video
- evidence-capture
source: osintambition-social
lastVerified: '2026-08-05'
enrichment: full
---

# redditvids

> A web helper for Reddit's split-stream video: Reddit stores a clip's audio and video as separate files, and this stitches them back into one watchable/downloadable file with sound.

## When to use
You have found a Reddit-hosted video tied to your investigation (on a subject's profile, in a relevant thread) and need to preserve it before it is deleted — with audio, which a naive save often drops. Paste the post URL and get a merged, playable/downloadable file. This is an evidence-capture convenience, not a discovery tool: it returns the video, not information about who posted it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Copy the Reddit post URL (the one containing the video).
2. Open https://redditvids.com and paste the URL.
3. Play or download the merged video (audio + video combined).
4. Record provenance: the original post URL, the poster's `username`, the capture date, and a hash of the file.
5. Pivot: the poster's `username` feeds username-hunting; any in-frame detail (location, faces) feeds image/geo tools.

## Inputs → Outputs
- **In:** a Reddit post/video URL (the poster's `username` is visible on the source post)
- **Out:** a merged, playable/downloadable video file (`image`/media)
- **Empty/negative result looks like:** the tool fails on a deleted/removed post, a non-video link, or an externally-hosted (non-Reddit) video — confirm the URL is a live Reddit-hosted clip.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive toward the subject, but you disclose the post you are fetching to a third-party operator — sock-puppet the browser for sensitive captures.
- Interchangeable with many similar downloaders; if one is down or fails on a post, another (e.g. a Reddit video downloader alternative) usually works. Always preserve the original URL and a hash for chain-of-custody.

## Overlaps ("do both")
- Pairs with a full-page capture tool like [[fireshot]] and a public archive — the downloader saves the media, the screenshot/archive preserves the surrounding post context (title, comments, poster); do both for a complete record.

## Trust & verifiability
`trust: unverified` — an unaffiliated third-party utility. Verify the downloaded clip matches the live post and keep provenance (URL, username, timestamp, hash); the Reddit post itself, not this tool, is the primary record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | redditvids |
| category | social-networks |
| selectorsIn → selectorsOut | username → image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
