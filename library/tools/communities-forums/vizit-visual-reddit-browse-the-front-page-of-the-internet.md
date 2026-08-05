---
id: vizit-visual-reddit-browse-the-front-page-of-the-internet
name: Vizit (Visual Reddit)
description: Use when you have a subreddit or community of interest and want to see which other subreddits it connects to (shared users/topics) as an interactive network graph — returns related communities to expand a Reddit investigation.
url: https://redditstuff.github.io/sna/vizit
category: communities-forums
path:
- communities-forums
bestFor: Visualising how subreddits relate to one another as a network to find adjacent communities.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source (CC BY-NC-SA) static web app hosted on GitHub Pages; no account needed.
opsec: passive
opsecNote: A static visualisation of pre-computed subreddit relationships — you query the graph, not Reddit or any user, so it's fully passive and leaks nothing about a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An open-source social-network-analysis project; the graph reflects a past snapshot of subreddit relationships, so treat it as a structural map, not live Reddit data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Vizit Reddit
- Visual Reddit
tags:
- reddit
- social-network-analysis
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Vizit (Visual Reddit)

> An interactive network map of how subreddits connect — a structural view of Reddit's communities to find where a topic's audience also gathers.

## When to use
When a Reddit lead centres on a subreddit/community and you want to know which *other* subreddits it's linked to (through shared users and topic overlap). Vizit renders that as an explorable graph, so you can hop from a known community to adjacent ones a subject is likely also active in — useful for broadening where to search for a `username` or topic.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://redditstuff.github.io/sna/vizit.
2. Use the search to locate a subreddit node, or explore clusters in the network.
3. Follow the edges to see connected communities and their groupings.
4. Note adjacent subreddits worth checking for your subject/topic.
5. Pivot: take those subreddit names into Reddit search/archives and username tools to look for the person's `social-profile` activity there.

## Inputs → Outputs
- **In:** a subreddit/community (and, downstream, a `username` to hunt in the surfaced communities)
- **Out:** a network of related subreddits → new places to look for a `social-profile`
- **Empty/negative result looks like:** a sparsely-connected or missing node — the community may be too small/new for the snapshot, or the graph predates it.

## Gotchas & OpSec
- **Snapshot, not live:** the relationships are pre-computed and may be dated; use it for structure, then verify on current Reddit.
- It maps communities, not individuals — it points you to *where* to look, it doesn't find the person.
- Fully passive; nothing about your query reaches Reddit or any user.

## Overlaps ("do both")
- Pairs with Reddit search, user-history tools, and 4chan/forum archives — Vizit tells you *which* communities to search, the others do the searching.

## Trust & verifiability
`trust: community` — an open-source SNA snapshot; trust it as a structural map of subreddit relatedness, and confirm any lead against live Reddit before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vizit-visual-reddit-browse-the-front-page-of-the-internet |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
