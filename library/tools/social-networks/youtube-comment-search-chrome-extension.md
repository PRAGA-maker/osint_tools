---
id: youtube-comment-search-chrome-extension
name: YCS — YouTube Comment Search (Chrome Extension)
description: Use when you have a YouTube video and a `username`/keyword and want to find matching comments — returns comments by author/content with timestamps.
url: https://chromewebstore.google.com/detail/ycs-youtube-comment-searc/pmfhcilikeembgbiadjiojgfgcfbcoaa
category: social-networks
path:
- social-networks
bestFor: Searching all comments/replies on a YouTube video by author name or content — impossible through YouTube's native UI.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Chrome extension (50k+ users) with no account required; installs into your browser.
opsec: passive
opsecNote: Runs locally in your browser against the video's already-public comments; you are not interacting with or notifying any commenter. The developer states it does not collect user data. Install into a sock-puppet browser profile as good hygiene, but there is no target-facing footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A widely-installed third-party extension (≈50k users, ~3.3★, last updated Oct 2024); it reads public YouTube comment data client-side. Vet the extension's permissions before installing.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- YCS
- YouTube Comment Search extension
tags:
- youtube
- comment-search
- browser-extension
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# YCS — YouTube Comment Search (Chrome Extension)

> A browser extension that makes a single YouTube video's comments fully searchable — by author, by content, by time — so you can find exactly what a given account said, or who said a given thing.

## When to use
You have a YouTube video and want to (a) find every comment a specific `username` left on it, (b) find who said a particular phrase, or (c) mine chat-replay/transcript text. YouTube's native UI has no comment search, so on a video with thousands of comments this is the only practical way to locate a subject's activity or surface commenters tied to a topic.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "YCS — YouTube Comment Search" from the Chrome Web Store into your (sock-puppet) browser profile.
2. Open the target YouTube video; the extension loads/searches its comments, replies, chat replay, and transcript.
3. Search by author (`username`) or by content/keyword; use fuzzy match, emoji, and timestamp filters as needed; export results.
4. Pivot: a matched commenter's channel is a `social-profile` — open it for the handle, other videos, and links; a reused username feeds cross-platform enumeration.

## Inputs → Outputs
- **In:** `username` (or keyword) + a YouTube video
- **Out:** matching comments/replies with author `social-profile` links and timestamps
- **Empty/negative result looks like:** no matching comments — the author didn't comment on this video, or comments are disabled/limited; scope is per-video, not site-wide.

## Gotchas & OpSec
- Scope is a single video at a time — it does not search a user's comments across all of YouTube.
- It can only see comments the video actually loads; heavily-throttled or disabled comment sections limit it.
- OpSec: passive, client-side; no commenter is notified. Review the extension's permissions before install.

## Overlaps ("do both")
- Complements channel/username-enumeration tools — this finds the comment on a specific video, those trace the resulting handle across platforms.

## Trust & verifiability
`trust: community` — a popular but third-party extension reading public data locally; the comments it surfaces are genuine YouTube content, but vet the extension's permissions and keep it in a research browser profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-comment-search-chrome-extension |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
