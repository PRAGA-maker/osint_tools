---
id: ins-downloader-addons-mozilla-org
name: Instagram Downloader (addons.mozilla.org)
description: Use when you are viewing an Instagram/Threads profile or post and want to download its photos/videos for offline analysis — a Firefox extension that adds download buttons — returns `image`/video files.
url: https://addons.mozilla.org/en-GB/firefox/addon/ins-downloader/
category: social-networks
path:
- social-networks
bestFor: One-click downloading of Instagram (and Threads) images/videos from the browser for offline evidence and reverse-image analysis.
selectorsIn:
- username
selectorsOut:
- image
status: live
pricing: free
costNote: Free Firefox add-on (MIT-licensed, ~37k users, actively updated). No account or payment.
opsec: active
opsecNote: The extension runs in your logged-in Instagram session and requires access to Instagram/Threads data. Downloading media means you are browsing the target's profile while authenticated — use a sock-puppet Instagram account and a dedicated Firefox profile; a third-party extension can also see your session, so vet it and isolate it.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: A community-maintained browser extension; useful and popular, but a third-party add-on with broad access to your Instagram session — review permissions and run it in isolation.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- ins downloader
- Instagram Downloader Firefox
tags:
- instagram
- Instagram Related Sites
- media-download
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Instagram Downloader (addons.mozilla.org)

> A Firefox extension that adds download buttons to Instagram and Threads — grab a target's photos/videos/stories as files for offline analysis and preservation.

## When to use
You are looking at an Instagram (or Threads) profile/post and need the actual media files — to preserve evidence before it's deleted, run reverse-image/face search, or pull EXIF/context. Rather than screenshotting, this extension lets you download the original image/video directly while browsing.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Instagram Downloader" from https://addons.mozilla.org/en-GB/firefox/addon/ins-downloader/ into a dedicated (sock-puppet) Firefox profile.
2. Log into a sock-puppet Instagram account and open the target `username`'s profile/post.
3. Use the download buttons the extension adds to save photos/videos (and Threads media).
4. Store files with provenance notes (URL, timestamp).
5. Pivot: run downloaded `image`s through reverse-image/face search (`[[faceagle]]`, PimEyes) and EXIF tools; use video for scene/geolocation analysis.

## Inputs → Outputs
- **In:** an Instagram/Threads profile or post you're viewing (target `username`)
- **Out:** downloaded `image`/video files
- **Empty/negative result looks like:** buttons don't appear or downloads fail — Instagram frequently changes its markup, breaking such extensions; the account may also be private (no public media to grab). A failure often means the extension needs updating, not that no media exists.

## Gotchas & OpSec
- **Active/authenticated:** runs in your IG session — sock-puppet account + isolated browser profile only.
- Third-party extension with broad session access — vet permissions; don't install alongside sensitive accounts.
- IG markup changes break these tools periodically; keep a fallback (anonymous-viewer bots/sites).

## Overlaps ("do both")
- Pairs with anonymous Instagram viewers (`[[instaanonym]]`) and `[[mediamister-com]]` — viewers grab public media without your session, this downloads originals while browsing; use whichever matches your OpSec needs.

## Trust & verifiability
`trust: community` — a popular but third-party extension. The files it saves are the real media; the risk is the extension's session access, so isolate it and confirm downloads against the live post.
