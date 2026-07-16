---
id: what-goes-on-mastodon
name: What goes on Mastodon
description: Use when you want to gauge which Mastodon instances are most active before searching them for a subject — returns instance/domain leads, not a per-person lookup.
url: https://observablehq.com/@mauforonda/what-goes-on-in-mastodon
category: messaging
path:
- messaging
bestFor: Ranking the most active Mastodon instances (by new users/posts) to prioritise which servers to search for a subject.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free public Observable notebook; no account or payment.
opsec: passive
opsecNote: You only view an aggregate real-time visualization; no target interaction and nothing logged against a subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent Observable notebook (by mauforonda) charting public Mastodon activity feeds; an analytics dashboard, not an authoritative registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- what goes on in mastodon
tags:
- mastodon
- social-media
- instance-activity
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- observable
---

# What goes on Mastodon

> A live Observable dashboard of Mastodon activity: how many new users and posts each instance is producing over the last 6h / 24h / 72h / month.

## When to use
This is orientation, not a per-person lookup. When you know your subject is on Mastodon but not which server, this dashboard shows which instances are largest and most active right now — helping you prioritise which `domain`s to search first (large general instances vs niche communities) rather than guessing. It answers "where are people posting," not "where is *this* person."

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://observablehq.com/@mauforonda/what-goes-on-in-mastodon.
2. Pick a time window (6h, 24h, 72h, or the last month).
3. Read the ranked instances by new users / new posts to see which servers are most active.
4. Pivot: take the top/relevant instance `domain`s to a Mastodon profile or handle-search tool and hunt for the subject's username there.

## Inputs → Outputs
- **In:** none per-person — you browse aggregate activity (optionally focusing on a specific instance `domain`)
- **Out:** a ranked/visualised list of active instance `domain`s to prioritise for further search.
- **Empty/negative result looks like:** the notebook not loading, or a flat/stale chart — Observable notebooks depend on a live upstream feed that can lapse.

## Gotchas & OpSec
- It is a statistics dashboard: it will never find or confirm an individual — it only tells you where activity is concentrated.
- Depends on a live data feed; if the source feed breaks, the visualization goes stale or empty.
- Instance popularity shifts; re-check the current window rather than trusting an old snapshot.

## Overlaps ("do both")
- Feeds into `[[followgraph-for-mastodon]]` and Mastodon handle-search tools — this narrows *which servers* to search, those find and expand *the account*.

## Trust & verifiability
`trust: community` — an independent hobby dashboard on public data; fine for gauging relative instance activity, not a source of record about any person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | what-goes-on-mastodon |
| category | messaging |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
