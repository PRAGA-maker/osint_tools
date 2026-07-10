---
id: pushshift-api
name: Pushshift API
description: Use when you want archived Reddit posts/comments (including deleted ones) — historically a full Reddit archive, now restricted to Reddit moderators; use PullPush/Arctic Shift as the open alternatives.
url: https://pushshift.io/
category: social-networks
path:
- social-networks
bestFor: Historical Reddit archive access (posts/comments, including deleted/removed) — now gated to moderators after Reddit's API changes.
selectorsIn:
- username
selectorsOut:
- social-profile
- metadata-exif
status: degraded
pricing: free
costNote: Free, but since Reddit's 2023 API changes Pushshift access is restricted to verified Reddit moderators (via a Reddit-sanctioned integration). General/public and third-party querying is no longer available — use PullPush or Arctic Shift instead.
opsec: passive
opsecNote: Querying an archive is passive and does not notify the Reddit user. Access now requires moderator authentication, tying use to a Reddit account; the archived data itself is public Reddit content.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: api
trust: community
trustNote: A historically pivotal Reddit archive; the data is authentic public Reddit content, but access is now heavily restricted, making the open forks the practical route.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- pullpush
- arctic-shift-2
- redarcs
aliases:
- Pushshift
- pushshift.io
tags:
- reddit
- archive
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Pushshift API

> The Reddit archive that defined Reddit OSINT — a searchable store of posts/comments including deleted ones. After Reddit's 2023 API clampdown it's restricted to moderators, so treat the open forks (PullPush, Arctic Shift) as your working tools.

## When to use
You want a Reddit user's full posting history or to recover deleted/removed posts and comments — invaluable for pattern-of-life, interests, timezone, and admissions a user later scrubbed. Historically Pushshift was the way to do this; today, unless you have moderator-gated access, reach straight for the open re-implementations that expose the same archived data.

## How to use it (`bestInteractionPattern`: api)
1. Know the access reality: public/third-party Pushshift querying was shut off after Reddit's 2023 API changes; it now serves verified Reddit moderators via a sanctioned integration.
2. If you are a moderator with access, query the archive by `username`/subreddit/time for posts and comments (including deleted).
3. If not (most cases), use `[[pullpush]]` or `[[arctic-shift-2]]`, which re-expose Pushshift-style Reddit archive data openly.
4. Parse results for the user's post/comment timeline, subreddits, and content.
5. Pivot: active hours reveal timezone; subreddits reveal interests/location; recovered deleted content is often the most revealing.

## Inputs → Outputs
- **In:** Reddit `username` (or subreddit/time window)
- **Out:** archived posts/comments (`social-profile` history) with timestamps/subreddits (`metadata-exif`-style metadata), including deleted items
- **Empty/negative result looks like:** access denied/blocked (you lack moderator access) — not an empty archive; switch to the open forks. A genuinely empty result there means no archived activity for the handle.

## Gotchas & OpSec
- Status **degraded** for general use: direct public access is gone; the open forks are the practical path.
- Archives may lag or have gaps around Reddit's API-change period.
- OpSec: passive toward the user; moderator access ties queries to a Reddit account.

## Overlaps ("do both")
- Superseded for open use by `[[pullpush]]` and `[[arctic-shift-2]]` (Pushshift-style Reddit archives) and `[[redarcs]]` — use those to query Reddit history without moderator gating.

## Trust & verifiability
`trust: community` — the archived data is authentic public Reddit content, but access restrictions make the open forks the reliable route. Verify recovered deleted content against context, since archives can be incomplete around 2023.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pushshift-api |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (account-login) |
