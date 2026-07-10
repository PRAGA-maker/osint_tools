---
id: reddit-comment-history
name: Reddit Comment History
description: Use when you have a Reddit `username` and want a visual timeline of their comment activity — returns `social-profile` cadence, karma, subreddits and posting-time patterns as charts.
url: https://roadtolarissa.com/javascript/reddit-comment-visualizer/
category: social-networks
path:
- social-networks
- reddit
bestFor: Turning a Reddit user's public comment history into cadence/karma/subreddit visualizations that reveal timezone and routine.
selectorsIn:
- username
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free browser tool; no account or install. Runs client-side against Reddit's public API.
opsec: passive
opsecNote: Pulls only public comment data via Reddit's read API; the target gets no notification. The fetch comes from your browser/IP, so use a puppet connection if you are concerned about Reddit correlating the request.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Personal project by Adam Pearce (roadtolarissa.com); a thin client-side visualizer over Reddit's own API, so accuracy tracks whatever Reddit returns.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Reddit Comment Visualizer
- roadtolarissa reddit
tags:
- reddit
- social-networks
- visualization
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Reddit Comment History

> A client-side visualizer that downloads a Reddit user's public comments and charts them — the fast way to read someone's timezone, routine, and topic focus off their posting pattern.

## When to use
You have a Reddit `username` and want more than a raw list — you want to *see* when they post (which reveals timezone and daily routine), which subreddits dominate (interests, location, employer, relationships), and how activity spikes over time. Ideal early-stage profiling of a Reddit account in a missing-person or identity investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://roadtolarissa.com/javascript/reddit-comment-visualizer/.
2. Enter the target Reddit `username` and let it fetch the comment history via Reddit's public API.
3. Read the summary stats: total comments, karma, character counts, first/last post dates.
4. Explore the charts — histograms of posting time (map to timezone), scatter plots, and a subreddit pie (topic/interest fingerprint). Filter by karma, length, date range, or specific subreddits.
5. Pivot: posting-hour clusters → timezone/geolocation; dominant subreddits → local/city/employer subs, hobbies; named or self-doxxing comments → people-search.

## Inputs → Outputs
- **In:** `username` (Reddit handle)
- **Out:** `social-profile` (comment corpus), `metadata-exif` (timestamps, subreddits, karma — the cadence/timezone signal)
- **Empty/negative result looks like:** no comments load or a "user not found" — the handle is wrong, the account is shadowbanned/suspended, or comments were purged. For deep history that Reddit's API truncates, fall back to `[[arctic-shift-2]]`.

## Gotchas & OpSec
- Reddit's API only serves roughly the most recent ~1000 comments; for older history you need an archive (Arctic Shift).
- It reads comments only, not submissions/posts — combine with a submissions view for the full picture.
- OpSec: **passive** — no target notification; the request originates from your browser, so use a puppet IP for sensitive targets.

## Overlaps ("do both")
- Pairs with `[[arctic-shift-2]]` — this charts the recent API window; Arctic Shift supplies the deep/deleted history that this tool can't reach.
- Feed the discovered timezone and subreddit clues into cross-platform username search.

## Trust & verifiability
`trust: unverified` — a solo hobby project, but it only visualizes data Reddit's own API returns, so the underlying facts are Reddit's. Verify any pivotal comment by opening it directly on Reddit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-comment-history |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
