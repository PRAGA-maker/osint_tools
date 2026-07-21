---
id: tiktokapi
name: TikTokApi
description: Use when you have a TikTok username and want to programmatically pull that account's profile and video list — returns social-profile, associate and metadata-exif leads for building a subject's TikTok footprint.
url: https://pypi.org/project/TikTokApi
category: social-networks
path:
- social-networks
bestFor: Scripted collection of a TikTok user's public profile, video list, and engagement data.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- metadata-exif
status: live
pricing: free
costNote: Free, open-source Python library (davidteather). No paid API; you supply your own TikTok `ms_token` cookie from a normal browser session.
opsec: active
opsecNote: This makes real automated requests to TikTok's servers; aggressive scraping can trip rate-limits and get your IP/token flagged. It cannot access anything you couldn't see logged-out. Run from a sock-puppet browser session/IP, throttle requests, and never use authenticated routes against a target.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: python-lib
trust: community
trustNote: Widely-used, actively-maintained open-source library (in Bellingcat's toolkit). Unofficial and unstable by nature — it breaks when TikTok changes its site, so pin versions and expect maintenance.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- TikTok-Api
- davidteather TikTokApi
tags:
- bellingcat-toolkit
- tiktok
- python
- scraper
source: bellingcat-toolkit
lastVerified: '2026-07-21'
enrichment: full
---

# TikTokApi

> Unofficial Python wrapper around TikTok's web API — script the collection of a user's public profile, their videos, and engagement metrics instead of scrolling the app by hand.

## When to use
You have a TikTok `username` and need their public footprint at scale: profile fields, follower/following counts, the full list of their videos with captions and timestamps, hashtags, sounds used, and per-video stats. Doing this programmatically lets you snapshot an account (before it's deleted), enumerate every video, and extract the metadata that reveals interests, activity times (timezone), locations mentioned, and `associate` links (duets/mentions). It is read-only public data — it cannot log in as anyone or reach private content.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install TikTokApi` then `python -m playwright install` (it drives a headless browser).
2. Grab an `ms_token` cookie from a logged-out TikTok.com session and pass it into the API session.
3. In Python, instantiate the API and query by user, e.g. fetch the user object, then iterate their videos to collect captions, timestamps, stats, and sounds.
4. Persist results (JSON/CSV) and mine captions/hashtags for locations, other handles, and `associate` mentions.
5. Pivot: extracted handles/locations feed username-enumeration and geolocation tooling; save video files/metadata for `metadata-exif`-style analysis.

## Inputs → Outputs
- **In:** `username` (TikTok handle).
- **Out:** `social-profile` (profile + video list), `associate` (mentions/duets/follows), video `metadata-exif` (captions, timestamps, sounds, stats).
- **Empty/negative result looks like:** empty video list or an error — a private/suspended account, a stale `ms_token`, or TikTok having changed its API (the usual cause when a previously-working script breaks). Empty ≠ no account.

## Gotchas & OpSec
- Human-in-the-loop: you must supply a valid `ms_token`, and rate-limits/anti-bot measures require throttling and occasional token refresh.
- OpSec: treat as **active** — you are hitting TikTok's infrastructure. Use a sock-puppet session/IP, go slow, and never touch authenticated routes against a subject.
- Unofficial and brittle: pin a version, and expect it to break after TikTok updates — check the repo for a fix before assuming an account is empty.

## Overlaps ("do both")
- Pairs with manual TikTok review and username-enumeration tools — the API bulk-collects and timestamps everything, while a manual pass catches context (comments, visual detail) the API doesn't structure well.

## Trust & verifiability
`trust: community` — a popular, maintained open-source project, but unofficial: it depends on TikTok's undocumented endpoints. Verify any critical datum against the live profile, since scraped fields can lag or break.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tiktokapi |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | python-lib |
| opsec | active |
| human-in-loop | yes (rate-limit) |
