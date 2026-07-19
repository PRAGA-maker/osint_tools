---
id: map-of-reddit
name: Map of Reddit
description: Use when you have a subreddit or topic and want to discover adjacent communities a subject might frequent — returns an interactive similarity map of subreddits (`social-profile` context).
url: https://anvaka.github.io/map-of-reddit/
category: social-networks
path:
- social-networks
bestFor: Discovering subreddits related to a known one, to widen where a subject might post.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source visualization (Anvaka); runs client-side, no account.
opsec: passive
opsecNote: The map is a static, precomputed visualization served from GitHub Pages — you are not querying Reddit or the subject, so browsing it is entirely passive and leaks nothing about your target. Any pivot into an actual subreddit is a separate step done on Reddit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known open-source project by Andrei Kashcha (Anvaka); the map reflects a past snapshot of subreddit relationships, so it's a discovery aid, not live data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- map-of-github
aliases:
- map of reddit
- anvaka map of reddit
tags:
- social-networks
- reddit
- visualization
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Map of Reddit

> An interactive similarity map that places subreddits near the other communities their users overlap with — a way to expand from one known subreddit to the cluster around it.

## When to use
You know one subreddit a subject engages with (from their `social-profile`, a comment, or an interest) and want to discover the *adjacent* communities they're statistically likely to also frequent. The map clusters subreddits by shared audience, so it turns a single data point into a neighbourhood of places to check for the subject's activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://anvaka.github.io/map-of-reddit/ (give the visualization a moment to load).
2. Search or navigate to the subreddit you already associate with the subject.
3. Read its neighbourhood: nearby dots are communities with overlapping user bases (topics, regions, hobbies, fandoms).
4. Note candidate subreddits, then go to Reddit and search each for the subject's `username` or distinctive content.
5. Pivot: confirmed activity in an adjacent community adds to the `social-profile`; feed the username to a Reddit history tool.

## Inputs → Outputs
- **In:** a known subreddit / topic (`social-profile` anchor)
- **Out:** a cluster of related subreddits to investigate (discovery leads, not confirmed hits)
- **Empty/negative result looks like:** a very isolated or missing subreddit — niche/new/private communities may not appear in the map's snapshot; fall back to Reddit search.

## Gotchas & OpSec
- It's a *static snapshot* of subreddit relationships, not live — very new communities won't be present and clusters may be dated.
- It only suggests *where* to look; it does not tell you the subject is actually in those communities — verify on Reddit.
- OpSec: passive; nothing is sent to Reddit or the subject while browsing the map.

## Overlaps ("do both")
- Pairs with a Reddit user-history tool (e.g. [[chearch]]) — the map tells you *which* communities to check, then the history tool confirms whether the subject actually posts there.

## Trust & verifiability
`trust: community` — a respected open-source visualization, but the underlying data is a periodic snapshot; treat adjacencies as leads and confirm activity on live Reddit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | map-of-reddit |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
