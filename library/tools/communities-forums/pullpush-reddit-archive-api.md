---
id: pullpush-reddit-archive-api
name: PullPush (Reddit archive API)
description: Use when you have a Reddit `username` (or keyword/subreddit) and want their full comment/post history including deleted/removed content — returns archived Reddit activity.
url: https://pullpush.io/
category: communities-forums
path:
- communities-forums
bestFor: Recovering a Reddit user's complete posting history — including deleted, removed or edited posts and comments — via the Pushshift-successor archive.
selectorsIn:
- username
selectorsOut:
- social-profile
- metadata-exif
- associate
status: live
pricing: free
costNote: Free public JSON API (rate-limited); no account or key required for normal use.
opsec: passive
opsecNote: You query PullPush's archive, not Reddit or the user, so the subject is never notified. Requests go to a third-party archive host; use a clean session but there's no target-side footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: The widely-used successor to Pushshift for Reddit archival; broadly reliable, but coverage can have gaps/lag and archived copies are snapshots — cross-check against live Reddit where possible.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- PullPush
- pullpush.io
- Pushshift successor
tags:
- reddit
- archive
- deleted-content
- pushshift
source: inteltechniques-tools
lastVerified: '2026-07-10'
enrichment: full
---

# PullPush (Reddit archive API)

> The go-to Pushshift successor — pull a Reddit user's entire comment and post history, including content they (or moderators) later deleted or removed.

## When to use
You have a Reddit `username` and want the full picture of their activity: every comment and post with timestamps, subreddits, and — crucially — items removed or deleted from live Reddit. Deleted content is often the most revealing (a location slip, a real name, an admission later scrubbed). Also usable to search by keyword or within a subreddit over a time range. It's a cornerstone for building a Reddit subject's timeline, interests and associates.

## How to use it (`bestInteractionPattern`: api)
1. Query the JSON API directly, e.g. comments: `https://api.pullpush.io/reddit/search/comment/?author=<username>&size=100` (and `.../submission/?author=<username>` for posts).
2. Add filters: `q=<keyword>`, `subreddit=<sub>`, `after=`/`before=` (epoch) to scope by topic/time.
3. Page through results (sort by created_utc) to assemble the full history.
4. Read `body`/`selftext`, subreddit, and timestamps; deleted-on-Reddit items still appear here.
5. Pivot: subreddits reveal location/interests; mentioned usernames are `associate`s; a name/place slip in an old deleted comment feeds people-search.

## Inputs → Outputs
- **In:** `username` (or keyword/subreddit + time range)
- **Out:** archived comments/posts (`social-profile` activity), timestamps/subreddits (`metadata-exif`), and interacted `associate` handles
- **Empty/negative result looks like:** no results for the author — the account is new, was never archived, or the handle is wrong; archive gaps mean absence isn't proof of no activity.

## Gotchas & OpSec
- Archive **snapshots** can lag or miss very recent/very old content; a gap ≠ nothing existed. Cross-check live Reddit where it still exists.
- Rate-limited — batch politely; heavy scraping may be throttled.
- OpSec: passive; the user is never alerted. Handle recovered deleted content ethically/lawfully.

## Overlaps ("do both")
- Complements live Reddit browsing and Reddit-specific analyzers — PullPush recovers what live Reddit hides (deleted/removed); use both to compare current vs. scrubbed history.

## Trust & verifiability
`trust: community` — the de-facto Pushshift replacement, reliable for archival but not official; verify pivotal claims (a name/location in a deleted post) against a second source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pullpush-reddit-archive-api |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, metadata-exif, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
</content>
