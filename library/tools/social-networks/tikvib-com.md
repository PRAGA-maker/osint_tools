---
id: tikvib-com
name: tikvib.com
description: Use when you have a TikTok `username` and want to view/download their public videos and profile stats anonymously — returns `social-profile`, `image`, `metadata-exif`.
url: https://www.tikvib.com/
category: social-networks
path:
- social-networks
bestFor: Anonymously viewing and downloading a public TikTok account's videos, stories and profile analytics.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
- metadata-exif
status: live
pricing: free
costNote: Free web tool; no login or payment required to view or download public TikTok content.
opsec: passive
opsecNote: Anonymous by design — you browse via tikvib's servers, not your own logged-in TikTok, so your view does not appear to the target and no account of yours is exposed. Still use a clean browser session; third-party viewers of unknown provenance may log your IP/queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party TikTok scraper of unknown operator; useful but not authoritative, and may break when TikTok changes its site.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- TikVib
tags:
- tiktok
- video-downloader
- anonymous-viewer
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# tikvib.com

> An anonymous TikTok viewer/downloader: pull a public account's videos, stories and growth stats without logging into TikTok or appearing in their view counts.

## When to use
You have a TikTok `username` (handle) and want to review the account's public content and analytics without touching it from your own account. Good for preserving TikTok videos as evidence (download without watermark), profiling posting cadence, and reading follower/like/view trends — all while staying off the target's radar.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tikvib.com/ in a clean browser.
2. Enter the target's TikTok `username` (handle).
3. Browse the returned profile: videos, stories, and statistics (follower growth/decline, average likes/views, estimated earnings per post).
4. Download individual videos (typically without watermark) if you need to preserve them.
5. Pivot: pull captions, tagged locations and other-handle mentions from the videos; feed the handle into cross-platform username enumeration and reverse-image any distinctive video frames.

## Inputs → Outputs
- **In:** `username` (TikTok handle)
- **Out:** `social-profile` (the account), `image`/video content, `metadata-exif`-style stats (post dates, follower/like/view metrics)
- **Empty/negative result looks like:** no data for the handle — the account is private, deleted, renamed, or tikvib's scraper is broken for that account; verify the handle directly on TikTok.

## Gotchas & OpSec
- Works only on **public** accounts; private profiles return nothing (respect that boundary).
- Despite the historical "Instagram" tag on this entry, tikvib is a **TikTok** tool, not Instagram.
- Stats like "estimated earnings" are algorithmic guesses, not real figures.
- Third-party scrapers of unknown ownership can log your queries — assume the operator sees what you look up.

## Overlaps ("do both")
- Pairs with TikTok's own site (for comments/engagement you view logged-out) and any dedicated TikTok download/analytics tool — cross-check because scrapers frequently miss or truncate a catalogue.

## Trust & verifiability
`trust: unverified` — an anonymous third-party scraper; treat downloaded media as genuine (it comes from TikTok) but treat derived stats as estimates and confirm the account identity on TikTok itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tikvib-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, image, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
