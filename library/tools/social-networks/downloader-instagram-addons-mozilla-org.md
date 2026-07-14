---
id: downloader-instagram-addons-mozilla-org
name: Downloader for Instagram (Firefox add-on)
description: Use when you have a subject's Instagram `social-profile`/post and want to save the original media for analysis — returns downloaded `image`/video files (photos, reels, stories, highlights).
url: https://addons.mozilla.org/en-GB/firefox/addon/downloader-instagram/
category: social-networks
path:
- social-networks
bestFor: Saving full-resolution Instagram photos, videos, reels, stories and highlights locally so they can be reverse-image-searched and archived before they vanish.
selectorsIn:
- social-profile
selectorsOut:
- image
status: live
pricing: free
costNote: Free Firefox extension (v3.1.7, updated Oct 2024; ~22k users, 4.2 stars). No payment.
opsec: active
opsecNote: The extension requires you to be logged into Instagram to work, so downloads happen under whatever account you use — Instagram can associate the viewing/saving with it. Use a sock-puppet Instagram account and browser profile, never your personal login. Stories in particular can register a view.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: A third-party browser extension (not affiliated with Instagram) with a moderate user base and mixed reviews; it reads content you can already see, but as with any extension, review its permissions before installing.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Downloader for Instagram
- downloader-instagram firefox
tags:
- instagram
- Instagram Related Sites
- media-download
- browser-extension
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# Downloader for Instagram (Firefox add-on)

> A Firefox extension that adds a one-click download to Instagram content — the fast way to grab original-resolution photos, reels and (ephemeral) stories before they disappear.

## When to use
You are working an Instagram `social-profile` or specific post and need the media itself — full-resolution stills for reverse-image search and face comparison, videos for frame-by-frame review, or stories/highlights that will expire. Saving the original file (rather than screenshotting) preserves quality and lets you run it through image tooling.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension in Firefox from the Mozilla add-ons page and log into Instagram with a sock-puppet account.
2. Navigate to the target post, reel, story, or highlight.
3. Click the added "Download" button under the content, or right-click → download from the context menu.
4. Save the original image/video file locally.
5. Pivot: run saved stills through reverse-image and face search; check for background/geolocation cues; archive stories before they expire.

## Inputs → Outputs
- **In:** an Instagram `social-profile`/post/reel/story you can view
- **Out:** downloaded original-resolution `image`/video files
- **Empty/negative result looks like:** the download button doesn't appear or fails — you're not logged in, the account is private and you don't follow it, or Instagram changed its markup and broke the extension (check for an update).

## Gotchas & OpSec
- Human-in-the-loop / active: it needs an Instagram login to function, so all activity is attributable to that account — viewing a story can notify the poster. Use a throwaway account.
- Instagram strips EXIF from uploads, so downloaded files won't carry original camera/GPS metadata — geolocation must come from visible content, not EXIF.
- Extension behaviour breaks when Instagram updates; keep it current.

## Overlaps ("do both")
- Pairs with reverse-image/face search and metadata tools — this extension captures the media; those tools then identify and geolocate it.

## Trust & verifiability
`trust: community` — a third-party extension; it only saves content you can already see, but vet its permissions and treat it as an unofficial tool that can break with Instagram changes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | downloader-instagram-addons-mozilla-org |
