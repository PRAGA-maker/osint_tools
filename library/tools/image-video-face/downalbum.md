---
id: downalbum
name: DownAlbum
description: Use when you have a public `social-profile` and want to bulk-download its photo albums for offline analysis — returns image sets from Facebook, Instagram, Pinterest, Twitter and more.
url: https://chromewebstore.google.com/detail/downalbum/cgjnhhjpfcdhbhlcmmjppicjmgfkppok
category: image-video-face
path:
- image-video-face
bestFor: Bulk-grabbing all photos from a social profile/album in one pass for offline review, reverse-image search and EXIF checks.
selectorsIn:
- social-profile
selectorsOut:
- image
status: live
pricing: free
costNote: Free Chrome extension; no account or payment for the extension itself (you still need access to view the target profile).
opsec: active
opsecNote: DownAlbum works from YOUR logged-in browser session — it downloads what your account can see, so viewing/scraping a profile is tied to whatever account is logged in. Use a sock-puppet social account, and note that platforms may rate-limit or flag bulk media access.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A long-standing third-party Chrome extension (~100k users); it does what it claims, but as an unaffiliated extension with broad page access, vet permissions before installing.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Down Album
- DownAlbum Chrome extension
tags:
- pinterest
- facebook
- media-download
- chrome-extension
source: osintambition-social
lastVerified: '2026-07-19'
enrichment: full
---

# DownAlbum

> A Chrome extension that bulk-downloads every photo in a social profile's albums (Facebook, Instagram, Pinterest, Twitter, Weibo, Ask.fm) in one click — for offline analysis, reverse-image search and EXIF review.

## When to use
You've found a subject's public `social-profile` with many photos and want them all locally instead of saving each by hand. Pulling the full album set at once lets you run every image through reverse-image search, check for EXIF/`metadata-exif`, spot backgrounds for geolocation, and build a face set — far faster than one-by-one. Best when you already have visibility into the profile and just need efficient collection.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the DownAlbum extension from the Chrome Web Store.
2. Log into a **sock-puppet** account on the target platform in that browser profile.
3. Navigate to the target's album/photos page.
4. Click the DownAlbum toolbar button, choose the album/scope, and let it collect the media into a download page; save the images.
5. Pivot: run the downloaded set through reverse-image tools, EXIF viewers, and face-comparison — the images are the raw material for geolocation and identity work.

## Inputs → Outputs
- **In:** a viewable `social-profile`/album URL
- **Out:** a bulk set of `image`s (album photos/videos) saved locally
- **Empty/negative result looks like:** few or no images pulled — the profile/album is private to your account, the platform changed its markup (extension needs an update), or the content is behind infinite-scroll you didn't fully load.

## Gotchas & OpSec
- Only grabs what your logged-in session can see — private albums stay private; visibility depends on the account you use.
- Platform markup changes periodically break scrapers; a stale extension version may miss newer layouts.
- Human-in-the-loop: you must be logged into the platform (use a sock puppet), and bulk access can trigger rate limits/flags.
- OpSec: treat as **active** — collection is tied to your browsing account; vet the extension's permissions before installing.

## Overlaps ("do both")
- Feeds reverse-image and EXIF tools — DownAlbum does the collection; those do the analysis. Pair with dedicated Instagram/Facebook OSINT tools when a profile is partially locked.

## Trust & verifiability
`trust: unverified` — a popular but third-party extension; it reliably downloads what's visible, yet grants itself broad page access, so install with caution and confirm images against the live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | downalbum |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile → image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
