---
id: advanced-downloader-for-tiktok-addons-mozilla-org
name: Advanced Downloader for TikTok (Firefox add-on)
description: Use when you have a TikTok video `social-profile` URL and want to save the clip for evidence — a Firefox extension returning the downloaded image/video file.
url: https://addons.mozilla.org/en-GB/firefox/addon/advanced-downloader-for-tiktok/
category: social-networks
path:
- social-networks
bestFor: One-click downloading of a TikTok video you are viewing, straight from the browser toolbar.
selectorsIn:
- social-profile
selectorsOut:
- image
status: degraded
pricing: free
costNote: Free Firefox add-on; no account or payment.
opsec: passive
opsecNote: The extension downloads the video you are already viewing on tiktok.com — the capture itself does not notify the creator, but you must load the TikTok page (which TikTok logs against your session). Browse the target's TikTok logged-out / from a sock-puppet before capturing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Unofficial third-party add-on (not affiliated with TikTok/ByteDance), last updated 2021, ~3.1★ with polarised reviews. It works but is stale and unmaintained; grant it no more permission than needed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- Advanced Downloader for TikTok
tags:
- tiktok
- TikTok Related Sites
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Advanced Downloader for TikTok (Firefox add-on)

> A one-click Firefox toolbar extension for saving the TikTok video you are viewing — a capture tool for archiving a subject's clips before they vanish.

## When to use
You are viewing a specific TikTok on a subject's profile (or a hashtag/search hit) and want a durable local copy — to archive it, reverse-image-search a frame, geolocate the background, or read any surviving metadata — before the creator deletes or privates it. It captures the clip currently open in the browser; it does not discover profiles from a `name`/`username`.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the add-on in Firefox from the Mozilla Add-ons page (review its requested permissions first).
2. Open the target's TikTok video on tiktok.com (logged-out / sock-puppet session).
3. Click the extension's toolbar button (or its injected download control) to save the MP4 to disk.
4. If capture fails on a given clip, fall back to a web downloader (paste the video URL) — TikTok changes its page structure often and this stale add-on can break.
5. Pivot: a saved frame → reverse-image / geolocation; the file → `metadata-exif` inspection.

## Inputs → Outputs
- **In:** `social-profile` (the open TikTok video URL/page)
- **Out:** `image` (downloaded video file)
- **Empty/negative result looks like:** the button does nothing, errors, or saves a corrupt/partial file — usually because TikTok changed its markup or the video is from a private account. Try a web-based downloader instead.

## Gotchas & OpSec
- **Stale/unmaintained:** last updated 2021, mixed reviews — expect intermittent breakage; keep a URL-paste downloader as backup.
- Only captures public/viewable videos; private-account content is out of reach.
- Grant minimal permissions; being an unofficial add-on, do not use it in a browser profile holding sensitive logins.
- OpSec: capture is passive, but loading the TikTok page is logged by TikTok — do it from a sock-puppet.

## Overlaps ("do both")
- Pairs with URL-paste web downloaders (same job for TikTok as `[[fastvideosave-net]]` is for Instagram) — use whichever survives TikTok's current page changes.

## Trust & verifiability
`trust: unverified` — unofficial, unmaintained third-party extension; the media it saves is authentic (pulled from TikTok's own stream), but its reliability and permission footprint are not vouched for.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | advanced-downloader-for-tiktok-addons-mozilla-org |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
