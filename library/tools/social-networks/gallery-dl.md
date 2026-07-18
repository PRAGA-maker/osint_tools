---
id: gallery-dl
name: gallery-dl
description: Use when you have a `social-profile` or gallery URL and want to bulk-download all its images/videos with metadata — returns local `image` files plus per-post JSON metadata.
url: https://github.com/mikf/gallery-dl
category: social-networks
path:
- social-networks
bestFor: Bulk-downloading a target's full image/video history (with metadata) from hundreds of supported sites via one CLI.
selectorsIn:
- social-profile
- username
selectorsOut:
- image
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (GPL, Python); install via pip. No account needed for public content.
opsec: active
opsecNote: gallery-dl connects directly to the target platform's servers from your IP to pull the media, so it is active — the site can see and rate-limit/block the download traffic. Route through a VPN/proxy and set rate limits. For login-gated content you supply cookies, which ties the pull to that account — use a sock-puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Actively maintained, very widely used open-source project (mikf/gallery-dl) with thousands of stars and frequent releases; the code is auditable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- gallery-dl
tags:
- Social Media
- Universal
- image-download
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# gallery-dl

> A command-line image/video downloader for hundreds of sites (Instagram, Twitter/X, Flickr, DeviantArt, Reddit, Pixiv, and many more) — grabs a whole gallery or profile plus structured metadata in one run.

## When to use
You've found a subject's `social-profile` or a gallery URL and want the complete set of their public images/videos preserved locally — for reverse-image search, face matching, EXIF/geolocation analysis, or evidence archiving before the account is deleted. gallery-dl is the right tool when point-and-save is too slow (dozens or thousands of posts) or when you want the accompanying JSON metadata (captions, timestamps, tags) alongside each file.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install gallery-dl` (or `pipx install gallery-dl`).
2. Basic pull: `gallery-dl "https://www.instagram.com/<username>/"` — downloads the profile's media into a structured folder tree.
3. Capture metadata too: `gallery-dl --write-metadata "<url>"` writes a `.json` beside each file with caption, timestamp, and tags.
4. For login-gated content, pass cookies: `gallery-dl --cookies cookies.txt "<url>"` (export from a sock-puppet browser session).
5. Throttle to stay under the radar: `--sleep 2` and `--limit-rate 500k`.
6. Pivot: downloaded `image`s → reverse-image and face tools; embedded `metadata-exif`/timestamps → geolocation and timeline building.

## Inputs → Outputs
- **In:** `social-profile` / gallery URL / `username` on a supported site
- **Out:** local `image`/video files, per-post JSON metadata, embedded `metadata-exif` where present
- **Empty/negative result looks like:** "no results"/0 files, or an authentication error — the profile is private/empty, the URL is unsupported, or you need cookies; it does not mean the account has no media.

## Gotchas & OpSec
- **Active**: downloads come straight from the platform to your IP — use a VPN/proxy, rate-limit, and avoid your real account's cookies (use a sock-puppet).
- Site extractors break when platforms change; keep gallery-dl updated (`pip install -U gallery-dl`).
- Many platforms strip EXIF from displayed images, so `metadata-exif` may be sparse — rely on the site-provided JSON timestamps instead.

## Overlaps ("do both")
- Complements reverse-image and face-search tools (feed them what you download) and browser-based single-page savers — gallery-dl scales to full-history bulk pulls those can't.

## Trust & verifiability
`trust: community` — a mature, heavily used open-source project with public code and rapid updates; the tool is trustworthy, but the *content* it fetches is only as reliable as the source platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gallery-dl |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → image, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
