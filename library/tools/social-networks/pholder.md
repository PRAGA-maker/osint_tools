---
id: pholder
name: Pholder
description: Use when you have a `username`, subreddit, or keyword and want Reddit's images/GIFs for it — returns media posts and the `social-profile`s that posted them.
url: https://pholder.com/
category: social-networks
path:
- social-networks
bestFor: Searching and browsing Reddit media (images/GIFs) by keyword, creator, or subreddit better than Reddit's own search.
selectorsIn:
- username
- image
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free to search and browse; no account required.
opsec: passive
opsecNote: You query Pholder's index of public Reddit media, never the target — no Redditor is notified. Searches hit Pholder's servers; use a clean browser/VPN if the query terms themselves are sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent third-party mirror/aggregator of public Reddit media since 2012; content is genuine Reddit media, but Pholder is not Reddit and its index may lag or omit removed posts.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Pholder Reddit search
tags:
- reddit
- image-search
- social-networks
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Pholder

> A media-focused Reddit search engine and archive: find images/GIFs across Reddit by keyword, creator, or subreddit, with far better recall than Reddit's native search.

## When to use
You are tracing a subject's Reddit footprint and care about the visual side — photos they posted, images tied to a `username`, or media in a subreddit they frequent. Reddit's own search is weak for media; Pholder aggregates and indexes it so you can surface pictures that Reddit buries. Also useful as an extra corpus for reverse-image leads (find the same image's Reddit posting and the account behind it).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://pholder.com/.
2. Search by keyword/tag, by a Reddit `username`, or browse a specific subreddit's media feed.
3. Refine with creator names and specific terms — Pholder rewards precise queries.
4. Read the output: image/GIF posts, each linking back to the source Reddit post and the posting `social-profile`.
5. Pivot: the source account feeds username-search tools; any `image` feeds reverse-image and EXIF checks; the subreddit context hints at interests/location.

## Inputs → Outputs
- **In:** `username`, subreddit, keyword, or an `image` to look for
- **Out:** Reddit media posts, source subreddit, and posting `social-profile`
- **Empty/negative result looks like:** no media returned — meaning nothing matching is in Pholder's index (the account may post only text, the media may be removed, or the term is too narrow), not proof of no Reddit presence.

## Gotchas & OpSec
- Pholder is a **third-party mirror**, not Reddit — deleted/removed posts may linger or, conversely, be missing; confirm live status on Reddit itself before relying on a hit.
- It focuses on media and filters out text posts, so it won't surface a subject's text-only comments/threads — use a Reddit-native tool for those.
- OpSec: passive; no interaction with any Redditor.

## Overlaps ("do both")
- Pairs with a Reddit user-history/comment tool: Pholder covers the *images* a `username` posts, the other covers *text/comments* — together they reconstruct the full Reddit footprint.

## Trust & verifiability
`trust: community` — an independent aggregator of public Reddit media. The images are genuine Reddit content and easy to verify against the linked source post, but Pholder's index completeness and freshness are not guaranteed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pholder |
