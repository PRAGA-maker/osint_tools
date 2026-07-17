---
id: arctic-shift
name: Arctic Shift
description: Use when you have a Reddit `username` or subreddit and want their full historical post/comment history — returns `social-profile` activity, timestamps and associated handles.
url: https://arctic-shift.photon-reddit.com/
category: communities-forums
path:
- communities-forums
- reddit-communities
bestFor: Retrieving a Reddit user's complete comment/post history (including deleted-from-view items) from an archived dataset.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free web search and API; the full dumps are also downloadable. No account required.
opsec: passive
opsecNote: Queries an archived Reddit dataset, not Reddit's live site, so the target's account is not touched and gets no notification. Your queries hit a third-party host; use a clean browser for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run successor to Pushshift (photon-reddit); widely used by researchers, but a third-party archive rather than Reddit itself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- arctic shift
- photon-reddit arctic shift
tags:
- reddit
- reddit-archive
- pushshift-successor
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Arctic Shift

> A community archive of Reddit (the Pushshift successor): give it a `username` or subreddit and get back the full historical stream of posts and comments — including items since deleted or hidden on the live site.

## When to use
You have a Reddit `username` tied to your subject and want their complete footprint: every comment and post with timestamps, the subreddits they frequent, the accounts they reply to, and content they later deleted (which the archive may retain). This reconstructs interests, timezone (from posting times), location clues and social circle far beyond what a live Reddit profile shows. Also use it to pull a subreddit's history for context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://arctic-shift.photon-reddit.com/ and open the Search tool.
2. Query by author (`username`), subreddit, or keyword, with optional date bounds.
3. Read results: each hit is a `social-profile` datapoint — comment/post text, subreddit, exact timestamp, and the parent thread linking to other `associate` accounts.
4. Analyse posting times for a likely timezone and subreddit topics for interests/location.
5. Pivot: run the same `username` through cross-platform username search; feed frequently-referenced other handles into further Reddit queries. For bulk work, use the API or the downloadable dumps.

## Inputs → Outputs
- **In:** `username` (Reddit handle) or subreddit
- **Out:** `social-profile` activity (posts/comments, timestamps, subreddits), `associate` handles from thread context
- **Empty/negative result looks like:** no rows for the handle — the account is very new, was created after the archive's last ingest, or never posted. Gaps can also reflect archive coverage windows, not user inactivity.

## Gotchas & OpSec
- OpSec: **passive** — the archive is queried, not Reddit; the account owner is not alerted.
- Coverage has time boundaries and occasional gaps (ingestion is imperfect); absence of recent activity may be an archive gap.
- Retained deleted content is sensitive; handle per your legal/ethical constraints.

## Overlaps ("do both")
- Pairs with live Reddit and cross-platform username tools — Arctic Shift gives deep history (incl. deleted), the live profile gives current status.

## Trust & verifiability
`trust: community` — a respected community archive. Content originated on Reddit; where it still exists live, confirm archived items against the current site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arctic-shift |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
