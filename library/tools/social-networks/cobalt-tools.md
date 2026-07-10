---
id: cobalt-tools
name: cobalt.tools
description: Use when you have a `social-profile`/media URL and want to download the video, audio or image cleanly — returns the media file (with its metadata) for offline analysis and preservation.
url: https://cobalt.tools/
category: social-networks
path:
- social-networks
bestFor: Clean, ad-free downloading of social-media videos/audio/images for evidence preservation and analysis.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open-source; no ads, no signup. A public instance runs at cobalt.tools and you can self-host the backend.
opsec: passive
opsecNote: You paste a public media URL; cobalt's backend fetches and returns the file. The target platform sees cobalt's server (or your self-hosted instance), not necessarily you, but the public instance operator sees your requests — self-host for sensitive work. Downloading does not notify the subject. Preserve original files and hashes for evidence integrity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-regarded open-source media downloader (imput/cobalt); no tracking by design, but it is a third-party service unless self-hosted, and platform support shifts as sites change.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- cobalt
- cobalt.tools
tags:
- instagram
- Instagram Related Sites
- media-downloader
- evidence-capture
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# cobalt.tools

> A clean, open-source media downloader: paste a social-media URL and get the underlying video/audio/image file — no ads, no tracking, ideal for preserving evidence.

## When to use
You have a `social-profile` post or media URL (YouTube, Instagram, TikTok, X/Twitter, and many more) and want to save the actual media file for offline analysis, frame-by-frame review, reverse-image search, or evidence preservation — before it is edited or deleted. Reach for it when you need the raw file, not a screenshot, and want it without the malware/ads of typical downloader sites.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cobalt.tools/ (or your self-hosted instance / API).
2. Paste the media/post URL and choose options (quality, audio-only, remux, mute).
3. Download the resulting file.
4. Preserve integrity: record the source URL, download time, and a hash of the file for chain-of-custody.
5. Pivot: the video/image feeds `[[reverse-image-search]]`, frame extraction, and EXIF/metadata inspection; audio can be transcribed; visible detail feeds geolocation.

## Inputs → Outputs
- **In:** `social-profile`/media URL
- **Out:** the downloaded media file and its embedded `metadata-exif` (where present)
- **Empty/negative result looks like:** "unsupported"/error — the platform isn't supported (support changes over time), the content is private/removed, or the URL is wrong. A failure is not proof the media never existed; try again or capture via screen recording.

## Gotchas & OpSec
- **Preservation discipline:** downloading strips it from context — always log the source URL and timestamp and hash the file if it may be evidence.
- Platform support drifts as sites change their delivery; expect occasional breakage on specific sites.
- OpSec: the **public instance** operator sees your requests; self-host the open-source backend for sensitive investigations. The target platform sees cobalt's fetch, not necessarily your IP.

## Overlaps ("do both")
- Pairs with full-page capture/`[[reverse-image-search]]` and frame-analysis tools — cobalt gets the pristine media file; capture tools preserve the surrounding page/context. Do both so you have the file and its provenance.

## Trust & verifiability
`trust: community` — a respected open-source project with no tracking by design; because it's open, you can self-host and audit it. Verify downloaded media against the live source and preserve hashes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cobalt-tools |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
