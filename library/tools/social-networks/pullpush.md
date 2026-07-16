---
id: pullpush
name: PullPush
description: Use when you have a Reddit `username`, subreddit or keyword and want to search historical Reddit comments/submissions Reddit's own search buries — returns `social-profile` activity, content and `metadata-exif` timestamps via a free API.
url: https://pullpush.io/
category: social-networks
path:
- social-networks
bestFor: Searching and retrieving historical Reddit comments and submissions by author, subreddit, keyword, or date via a free Pushshift-style API — including content deleted from Reddit's UI.
selectorsIn:
- username
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free public API and web search; no account or key. You must accept the Terms of Service; heavy use is rate-limited.
opsec: passive
opsecNote: You query an archive, not Reddit, so the target gets no signal. Requests go through pullpush.io's servers, which can log them — use a puppet IP for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: Community-run Pushshift successor built on Watchful1's Reddit torrent archives; widely used in Reddit research, though it is a third-party mirror, not Reddit itself.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- pullpush.io
- Pushshift successor
- PullPush API
tags:
- reddit
- social-networks
- archive
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- pullpush-reddit-archive-api
---

# PullPush

> A free Pushshift-style Reddit API: search anyone's historical comments and submissions by author, subreddit, keyword, or date — including items later deleted from Reddit's UI.

## When to use
You have a Reddit `username` and Reddit's native profile only shows a recent slice (or the account is suspended and shows nothing), or you want to sweep a subreddit/keyword across time. PullPush retrieves the full historical trail — comments and posts with subreddit, timestamp, and body — where Reddit users leak location, routine, relationships, and real-name clues. This is the go-to programmatic Reddit-history source after Pushshift lost public access.

## How to use it (`bestInteractionPattern`: api)
1. **Web:** use the search UI at pullpush.io for quick, no-code lookups.
2. **API:** call the endpoints directly —
   - comments: `https://api.pullpush.io/reddit/search/comment/?author=<username>`
   - submissions: `https://api.pullpush.io/reddit/search/submission/?author=<username>`
   Add `subreddit=`, `q=<keyword>`, `after=`/`before=` (epoch), `size=`, and `sort=` to filter.
3. Parse the JSON: each record has subreddit, UTC `created_utc`, score, and text. Build a timeline and subreddit histogram.
4. Read the metadata: posting-hour clusters → timezone; dominant subreddits → interests/location/employer.
5. Pivot: timezone/subreddit clues → geolocation; reused handles → cross-platform username search; self-doxxing text → people-search.

## Inputs → Outputs
- **In:** `username` (also subreddit, keyword, date range)
- **Out:** `social-profile` (full comment/post history), `metadata-exif` (timestamps, subreddits, scores — the timezone/cadence signal)
- **Empty/negative result looks like:** an empty `data` array — the handle is wrong, the account is too new to be in the archive, or the date filter excludes everything. Empty ≠ "no such user"; confirm spelling on Reddit.

## Gotchas & OpSec
- It's a **mirror of torrent archives**, so recent content lags and some ranges are incomplete; for the freshest data check Reddit directly.
- Rate limits apply — batch and back off; don't hammer the endpoint.
- Deleted content may persist here (pre-deletion text); powerful but handle ethically.
- OpSec: **passive** against the target.

## Overlaps ("do both")
- Near-duplicate of `[[arctic-shift-2]]` (both are Pushshift successors) — query both, since their archive coverage and uptime differ.
- Feed a pulled history into `[[reddit-comment-history]]` to visualize cadence, and reused handles into username search.

## Trust & verifiability
`trust: community` — a well-used third-party archive, but a mirror nonetheless; cross-check any pivotal comment against the live Reddit thread when it still exists.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pullpush |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
