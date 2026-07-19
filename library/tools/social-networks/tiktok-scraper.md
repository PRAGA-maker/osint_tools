---
id: tiktok-scraper
name: tiktok-scraper
description: Use when you have a TikTok `username`, hashtag, or music/trend and want to collect its posts and metadata in bulk — returns video posts plus user/video metadata (JSON/CSV) without an API key.
url: https://github.com/drawrowfly/tiktok-scraper
category: social-networks
path:
- social-networks
bestFor: Bulk collection of TikTok user/hashtag/trend/music feeds and metadata, with optional video download, from the CLI or Node.
selectorsIn:
- username
selectorsOut:
- social-profile
- metadata-exif
- image
status: degraded
pricing: free
costNote: Free and open-source (Node.js/TypeScript, MIT). No cost, but it scrapes TikTok's unofficial web endpoints and needs no login.
opsec: active
opsecNote: This makes automated requests directly to TikTok for the target's content; TikTok can see and rate-limit/block the traffic. Use a sock-puppet egress (proxy/VPN), throttle requests, and expect to supply session/signature values as TikTok's anti-bot measures change. Do not run from an attributable IP against a sensitive target.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source scraper (5k+ stars) but last released in 2021; TikTok's frequent changes mean parts break periodically, so treat it as maintained-by-community and verify it still works before relying on a run.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- tiktok-scraper
- drawrowfly tiktok-scraper
tags:
- tiktok
- scraper
- social-media
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# tiktok-scraper

> An open-source Node.js/CLI scraper for TikTok — pull a user's, hashtag's, trend's, or sound's posts and metadata in bulk (JSON/CSV), optionally downloading the videos, without the official API. Powerful but subject to TikTok's anti-bot churn.

## When to use
You have a TikTok `username` (or a hashtag/sound/trend) tied to a subject and want to harvest their content and metadata systematically — post list, captions, timestamps, engagement counts, and the video files — rather than clicking through the app. Good for building a timeline of a subject's TikTok activity, archiving posts before deletion, or pulling a hashtag/sound to find associated accounts.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `npm i -g tiktok-scraper` (or use it as a Node module / Docker).
2. Run a mode, e.g. `tiktok-scraper user <username> -n 50 -t json` (user feed), `tiktok-scraper hashtag <tag>`, `tiktok-scraper trend`, or `tiktok-scraper music <id>`.
3. Add `-d` to download videos, `-t csv` for spreadsheet output; process a list of users/hashtags from a file for batch jobs.
4. If runs return empty/errors, TikTok has likely changed its endpoints/signatures — update the tool, supply required session values, or fall back to manual collection.
5. Pivot: collected usernames, captions, and timestamps feed username-search, timeline-building, and (from any embedded coordinates/mentions) geolocation.

## Inputs → Outputs
- **In:** `username` (or hashtag / sound / trend)
- **Out:** `social-profile` (posts + profile/video metadata), `metadata-exif`-style post metadata (timestamps, counts), and downloaded `image`/video files
- **Empty/negative result looks like:** zero results or auth/signature errors — almost always TikTok anti-bot changes or rate-limiting, not an absent account; verify the account manually and update the tool before concluding.

## Gotchas & OpSec
- Human-in-the-loop: expect **rate-limiting/blocking**; throttle, rotate egress, and be ready to patch/supply signatures as TikTok changes.
- OpSec: **active** — requests go straight to TikTok for the target's content and are visible to TikTok; never run from an attributable IP against a sensitive subject; use a proxy/VPN and a burner posture.
- Maintenance: last release 2021; functionality drifts with TikTok. Confirm a working run before depending on results, and cross-check counts against the live app.

## Overlaps ("do both")
- Pairs with other TikTok OSINT tools and web-based analytics viewers — the scraper is best for bulk export and archiving, while a live viewer confirms current state; combine when the scraper is between breakages.

## Trust & verifiability
`trust: community` — a widely used open-source tool whose code is inspectable, but it depends on unofficial endpoints that change, so outputs should be spot-checked against the live TikTok profile and the tool's currency confirmed before a run.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tiktok-scraper |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, metadata-exif, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (rate-limit) |
