---
id: you-get
name: you-get
description: Use when you have a media URL (`social-profile` post, video, image gallery) and want to download the original file as evidence — returns the saved `image`/video with its source intact.
url: https://github.com/soimort/you-get
category: evidence-capture
path:
- evidence-capture
bestFor: Command-line downloading of videos/images from YouTube, TikTok and 100+ sites for preservation.
selectorsIn:
- social-profile
- image
selectorsOut:
- image
status: live
pricing: free
costNote: Free and open-source (MIT, soimort); a Python CLI, actively maintained. No account needed for public content.
opsec: active
opsecNote: you-get fetches the media directly from the source platform over your IP, so the download is visible to that platform's logs. Use a sock-puppet IP/VPN and note that logging in for private/age-gated media ties the download to that account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Long-running, popular open-source downloader (56k+ stars); extractor reliability varies as sites change their players.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- soimort/you-get
tags:
- Downloaders
- evidence
- video
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- yt-dlp
- translate-shell
---

# you-get

> Universal media grabber: download the actual video or image file behind a URL — for evidence you control, not a link that may vanish.

## When to use
You've found media that matters to a case — a video on a `social-profile`, a TikTok/YouTube clip, an image gallery — and you need the original file saved before it's edited or deleted. you-get pulls the source media (and can list available qualities) from 100+ Western and Chinese platforms, giving you a local, hashable copy for your evidence set rather than a fragile link.

## How to use it (`bestInteractionPattern`: cli)
1. Install (Python): `pip install you-get`.
2. Inspect first (no download): `you-get -i 'https://www.youtube.com/watch?v=...'` lists available formats/qualities.
3. Download: `you-get 'https://...'` (add `-o DIR` for an evidence folder, `--format=` to pick quality).
4. For images/pages, point it at the media/page URL; it fetches the downloadable content.
5. Preserve: record the URL, timestamp, and a hash of the saved file for chain-of-custody. Pivot: analyse the file's metadata/frames next.

## Inputs → Outputs
- **In:** a media URL (`social-profile` post, video page, `image` gallery)
- **Out:** the downloaded `image`/video file(s), optionally with a format list
- **Empty/negative result looks like:** an extractor error / "can't get video info" — the site changed its player or the media is private/geo-blocked; update you-get, try a login/cookies, or fall back to yt-dlp.

## Gotchas & OpSec
- Extractors break when platforms change; keep it updated and have `[[yt-dlp]]` as a fallback.
- OpSec: **active** — the download hits the source platform from your IP; use a sock puppet, and avoid logging in with an attributable account for private media.
- Capture provenance (URL, time, hash) at download time or the file's evidentiary value drops.

## Overlaps ("do both")
- Pairs with `[[yt-dlp]]` — the two support overlapping but not identical site sets and handle player changes differently; if one extractor fails, the other often succeeds.

## Trust & verifiability
`trust: community` — a mature, widely-used open-source tool; it retrieves the genuine source file, though extractor coverage shifts as target sites evolve.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | you-get |
| category | evidence-capture |
| selectorsIn → selectorsOut | social-profile, image → image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
