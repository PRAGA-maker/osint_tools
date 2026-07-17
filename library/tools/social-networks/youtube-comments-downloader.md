---
id: youtube-comments-downloader
name: YouTube Comments Downloader
description: Use when you have a YouTube `social-profile` (video/channel) and want its full comment history exported — returns commenter `username`, `name` and timestamps.
url: https://youtubecommentsdownloader.com/
category: social-networks
path:
- social-networks
bestFor: Bulk-exporting all public comments (and replies) from a YouTube video, channel or playlist for analysis.
selectorsIn:
- social-profile
selectorsOut:
- username
- name
status: live
pricing: freemium
costNote: Free signup grants starter credits (no card); large exports consume credits (roughly 1 credit/comment plus a per-item fee), with paid top-ups for bulk work.
opsec: passive
opsecNote: You export public comment data via a third-party service; the video owner and commenters are not notified. The service sees which video you scrape and requires an account, so use a research-only login. Comments are public, but bulk-collecting them still aggregates personal data — handle accordingly.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Independent commercial scraper; convenient but a third party — the authoritative source is the public YouTube page itself.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- youtubecommentsdownloader.com
tags:
- youtube
- comment-analysis
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# YouTube Comments Downloader

> A web service that bulk-exports every public comment and reply from a YouTube video, channel or playlist into a spreadsheet — turning a video into a list of the people who engaged with it.

## When to use
You have a YouTube `social-profile` (a video, channel, playlist, Short or community post tied to your subject) and want the full comment set rather than the handful the site shows. Comment threads expose commenter handles (`username`), display `name`s, timestamps and reply relationships — a rich pool for finding a subject's own account, their supporters/associates, and recurring interlocutors. Best for engagement mapping and finding a person active in a video's audience.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://youtubecommentsdownloader.com/ and create a free account (starter credits, no card).
2. Paste the target YouTube URL (video, channel, playlist, Short or community post).
3. Start the export; it walks the full thread tree preserving replies, likes and timestamps.
4. Download as CSV/XLSX/JSON and open it: each row gives a commenter `username`/display `name`, their text and when they posted.
5. Pivot: run distinctive commenter handles through username search; a subject who comments from their own account links the video to their broader footprint.

## Inputs → Outputs
- **In:** `social-profile` (a YouTube video/channel/playlist URL)
- **Out:** commenter `username`, display `name`, comment text, timestamps, reply structure
- **Empty/negative result looks like:** an export with zero/near-zero rows — comments are disabled on the video, the content was removed, or the account has no credits left to complete the pull.

## Gotchas & OpSec
- Human-in-the-loop: account login (and credits) are required; the free tier caps volume.
- OpSec: **passive** — no one on YouTube is notified. But you are trusting a third-party scraper with your query and account; keep it research-only.
- Display names and handles are user-chosen and can be recycled/spoofed; confirm identity before attributing a comment to your subject.

## Overlaps ("do both")
- Pairs with YouTube channel/metadata tools — those profile the *creator*, while this harvests the *audience* commenting underneath.

## Trust & verifiability
`trust: community` — a convenient third-party exporter; the ground truth is the public comment on YouTube itself, so spot-check exported rows against the live page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-comments-downloader |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → username, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
