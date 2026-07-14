---
id: threadster-app
name: threadster.app
description: Use when you have a public Threads (Meta) post `url` from a subject's `social-profile` and want to download its video/photo/GIF for offline capture — returns image, metadata-exif.
url: https://threadster.app/
category: social-networks
path:
- social-networks
bestFor: Downloading media (video/photo/GIF) from a public Threads post for evidence capture and analysis.
selectorsIn:
- social-profile
selectorsOut:
- image
- metadata-exif
status: live
pricing: free
costNote: Completely free, no login, no daily limits (per the site). Offers web access plus mobile apps, a Chrome extension, and a bookmarklet.
opsec: passive
opsecNote: Pasting a public Threads post URL fetches the media server-side, so Meta doesn't see your IP for the pull and the poster isn't notified. It's an unaffiliated third-party downloader — never enter Threads/Instagram credentials, and use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Unaffiliated third-party downloader; works only on public Threads posts. Depends on Threads' markup, so like all such tools its uptime can break when the platform changes.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Threadster
- Threads downloader
tags:
- threads
- Threads Related Sites
- media-download
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# threadster.app

> A free, no-login downloader for Meta's Threads: paste a public post link and save its video, photo, or GIF for offline capture and analysis.

## When to use
You've found a public Threads post on a subject's `social-profile` and need the media saved locally — to preserve it before deletion, examine it, run stills through reverse-image search, or check `metadata-exif`. It works from a post URL, so locate the post first, then bring the link here.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the target's public Threads post and copy its URL.
2. Go to https://threadster.app/ and paste the URL (or use its Chrome extension/bookmarklet).
3. Download the video/photo/GIF. No login is needed.
4. If it fails to resolve, the post is likely private/deleted or the tool has broken against a Threads change — try again later or another downloader.
5. Pivot: stills feed reverse-image/face tools ([[pimeyes-com]]); inspect the file for `metadata-exif`; preserve URL + timestamp for provenance.

## Inputs → Outputs
- **In:** a public Threads post `url` (found via the target's `social-profile`)
- **Out:** the media file (`image`/video/GIF), any embedded `metadata-exif`
- **Empty/negative result looks like:** an error or no download — usually a private/deleted post, a profile URL instead of a post, or the tool broken by a Threads update.

## Gotchas & OpSec
- Public posts only — private content and deleted posts won't resolve.
- Unaffiliated and markup-dependent: uptime can break with Threads changes; keep a fallback.
- Never enter Threads/Instagram credentials — the tool only needs the post URL.
- OpSec: passive (server-side fetch), but preserve provenance if the capture may be evidence.

## Overlaps ("do both")
- Pairs with [[storysaver-net]] / other social-media downloaders and with reverse-image/EXIF tools that consume the media you capture.

## Trust & verifiability
`trust: unverified` — an anonymous third-party downloader; media it returns is authentic Threads content, but the operator is unaccountable and uptime is platform-dependent — verify and preserve provenance yourself.
