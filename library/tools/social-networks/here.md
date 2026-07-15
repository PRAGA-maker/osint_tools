---
id: here
name: here
description: Use when you have a Reddit `username` or topic and want to reach Pushshift-based historical Reddit archives — returns `social-profile` history (posts/comments) beyond what Reddit's own search shows.
url: https://www.reddit.com/r/pushshift/
category: social-networks
path:
- social-networks
bestFor: Finding the current, access-approved way into Pushshift-style historical Reddit data (deleted/edited/old posts).
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: The subreddit is free. Pushshift data access itself is now gated — since 2023 Reddit restricted the public API, and full Pushshift access is limited to Reddit-approved moderators; check the subreddit for the current front-ends and terms.
opsec: passive
opsecNote: Reading the subreddit and querying archives is passive — the target is not notified. Do the querying signed out / in a sock account; do not contact the subject.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: r/pushshift is the community hub for the Pushshift Reddit dataset; the data is real archival Reddit content, but availability and front-ends shift as Reddit's API policy evolves.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- r/pushshift
- Pushshift Reddit archive
tags:
- reddit
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# here

> The r/pushshift subreddit — the community hub for the Pushshift Reddit dataset, the canonical way to reach historical, deleted, and edited Reddit content that Reddit's own search hides.

## When to use
You have a Reddit `username` and want their full posting history — including comments they later deleted or edited, or activity too old for Reddit's native search. Pushshift archived Reddit at scale; a subject's deleted comment can reveal a location, a relationship, or a plan. Reddit's 2023 API clampdown broke the old open endpoints, so this subreddit is where you find the *current* sanctioned access path and working front-ends.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.reddit.com/r/pushshift/ and read the pinned/recent posts for the present state of access (endpoints and front-ends change often).
2. Use whatever current tool the community points to (e.g. an approved API, or archive front-ends) to query the target `username`'s post/comment history.
3. Cross-read results for self-disclosed details — city, employer, usernames on other platforms, associates.
4. Pivot: reused handles feed username-search tools; disclosed locations/names feed people-search.

## Inputs → Outputs
- **In:** Reddit `username` (or subreddit/keyword)
- **Out:** historical posts/comments → `social-profile` history, deleted-content recovery, cross-platform handle leaks
- **Empty/negative result looks like:** no archived activity, or an access tool that now 403s — the latter means the front-end is deprecated, not that data is absent; check the subreddit for the working replacement.

## Gotchas & OpSec
- **Access is a moving target**: post-2023, full Pushshift is restricted to Reddit-approved moderators and public front-ends come and go. Always confirm the current method from the subreddit before assuming a tool is dead.
- Human-in-the-loop / **rate-limit**: archive front-ends throttle heavy querying.
- OpSec: **passive** — reading archives never touches the subject.

## Overlaps ("do both")
- Pairs with Reddit-native search and username tools — Pushshift recovers what Reddit deleted/hid; live search shows what's current. Run both to reconstruct a full timeline.

## Trust & verifiability
`trust: community` — the dataset is genuine archived Reddit content maintained by the community, but coverage gaps and shifting access mean you should treat absence as inconclusive and verify recovered deleted content against context.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | here |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
