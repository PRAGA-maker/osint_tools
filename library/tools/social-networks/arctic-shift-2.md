---
id: arctic-shift-2
name: Arctic Shift
description: Use when you have a Reddit `username` (or subreddit/keyword) and want historical Reddit posts and comments Reddit's own search hides — returns `social-profile` activity, timestamps and content as a Pushshift successor.
url: https://github.com/ArthurHeitmann/arctic_shift
category: social-networks
path:
- social-networks
bestFor: Retrieving a Reddit user's full post/comment history (including deleted-from-UI items) via an archive API or bulk dumps — the leading Pushshift replacement.
selectorsIn:
- username
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free and open-source. Web search UI and API are free; bulk data dumps are free downloads (large, .zst-compressed).
opsec: passive
opsecNote: You query an archive, not Reddit, so the target gets no signal. The web API is hosted by the maintainer — assume they can log queries; use the offline dumps or a puppet setup for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: Open-source project by ArthurHeitmann; well-regarded in the Reddit-research community as the maintained successor to Pushshift after Pushshift lost broad access.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- arctic_shift
- Pushshift successor
- arctic-shift.photon-reddit.com
tags:
- reddit
- social-networks
- archive
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Arctic Shift

> The maintained archive of historical Reddit data after Pushshift went dark — pull a user's entire comment/post history by API, web UI, or bulk dump.

## When to use
You have a Reddit `username` and Reddit's native profile view only shows the recent slice (or the account is suspended/deleted and the UI shows nothing). Arctic Shift lets you retrieve the full historical trail — every comment and submission with subreddit, timestamp, and body text — which is where a Reddit user leaks location, routine, relationships, and real-name clues. Also usable to sweep a subreddit or keyword across time.

## How to use it (`bestInteractionPattern`: api)
1. **Fastest:** use the hosted web search at `arctic-shift.photon-reddit.com` — enter a username to pull comments/posts without any download.
2. **Programmatic:** hit the Arctic Shift API (documented in the GitHub repo) for `author=<username>` to page through all items as JSON; good for building a timeline.
3. **Bulk/offline:** download the monthly `.zst` dumps from the repo's linked releases, install the `zstandard` Python lib, and run the provided helper scripts to grep locally — best for large sweeps and for OpSec (no third-party query logging).
4. Read the output: each record gives subreddit, UTC timestamp, score, and text. Build a posting-cadence and topic map.
5. Pivot: subreddits + timestamps → timezone/location inference; usernames reused elsewhere → cross-platform username search; named details → people-search.

## Inputs → Outputs
- **In:** `username` (also subreddit or keyword + date range)
- **Out:** `social-profile` (full comment/post history), `metadata-exif` (timestamps, subreddit, score — the metadata that reveals timezone/activity pattern)
- **Empty/negative result looks like:** API returns an empty array or the web UI shows no rows. For a very new account this may mean the archive hasn't ingested it yet; for a common typo it means the handle is wrong — confirm spelling on Reddit.

## Gotchas & OpSec
- Coverage has gaps around the periods when Reddit restricted archiving; very recent content may lag, and some ranges are incomplete.
- Deleted content: Arctic Shift may retain the pre-deletion text of comments the user later removed — powerful, but treat ethically and verify.
- OpSec: **passive** against the target. The hosted API/web UI is run by the maintainer, so for sensitive investigations prefer the offline dumps.

## Overlaps ("do both")
- Pairs with `[[reddit-comment-history]]` — Arctic Shift supplies the raw archive; the visualizer turns a pulled history into cadence/karma graphs.
- Feed reused handles into username-enumeration tools to find the same person on other platforms.

## Trust & verifiability
`trust: community` — open-source and the de-facto Pushshift replacement, but it is an archive mirror: cross-check any pivotal claim against the live Reddit account or thread when it still exists.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arctic-shift-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
