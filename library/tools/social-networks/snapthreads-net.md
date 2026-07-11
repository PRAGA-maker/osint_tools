---
id: snapthreads-net
name: SnapThreads
description: Use when you have a public Threads post `social-profile`/link and want to download its video for analysis — returns the MP4 (image/face frames, metadata) without the platform watermark.
url: https://snapthreads.net/
category: social-networks
path:
- social-networks
bestFor: Downloading a public Instagram Threads video by URL for offline review, framing, or reverse-image work.
selectorsIn:
- social-profile
selectorsOut:
- image
- metadata
status: live
pricing: free
costNote: Free online downloader; no account. Ad-supported third-party site.
opsec: passive
opsecNote: SnapThreads' servers fetch the public video, so the download isn't made from your IP against Threads and the poster isn't notified. But you are pasting the target's URL into a third-party site that logs it — use a URL that doesn't reveal your wider investigation, and prefer a clean browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous third-party media downloader. It works for public content but is ad-heavy and unaccountable; don't trust it beyond fetching a public file, and scan downloads before opening.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- snapthreads.net
- Threads video downloader
tags:
- threads
- Threads Related Sites
- video-download
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# SnapThreads

> A free web downloader that saves a public Instagram Threads video as a watermark-free MP4 from its link.

## When to use
You've found a public Threads post from your subject that contains a video, and you want the file itself — to keep as evidence, pull frames for face/reverse-image search, inspect for background/location clues, or check metadata. SnapThreads turns a Threads video URL into a downloadable MP4.

## How to use it (`bestInteractionPattern`: web-manual)
1. On Threads, open the target post and copy its video link.
2. Go to https://snapthreads.net/ and paste the link.
3. Download the MP4 (up to 1080p, watermark removed).
4. Pivot: run frames through reverse-image/face tools; inspect the video for location/identity clues; archive the file with a hash for chain-of-custody.

## Inputs → Outputs
- **In:** `social-profile` — a public Threads post/video URL
- **Out:** downloaded video (`image` frames, embedded `metadata`)
- **Empty/negative result looks like:** an error or no download — the link is to a private/removed post, isn't a video, or is a profile (not a single post). It cannot pull private content or a whole account's videos; public single-video links only.

## Gotchas & OpSec
- Public-only: no private posts, no bulk-account download, no anonymized profile scraping.
- OpSec: passive re: the poster (SnapThreads fetches it), but you disclose the target URL to a third-party ad site — assume it's logged.
- Trust: unaccountable downloader; scan files, don't rely on it for anything but grabbing a public MP4.

## Overlaps ("do both")
- Pairs with reverse-image/face search and video-metadata tools — SnapThreads gets you the file; those extract identity and location signal from it. For other platforms, use the equivalent per-platform downloader.

## Trust & verifiability
`trust: unverified` — anonymous third-party site. Fine as a convenience to fetch a public video, but treat the tool itself as untrusted: clean browser, scan the download, and preserve the original post URL/screenshot as the primary record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snapthreads-net |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → image, metadata |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
