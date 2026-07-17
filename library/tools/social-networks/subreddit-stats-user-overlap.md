---
id: subreddit-stats-user-overlap
name: Subreddit Stats User-Overlap
description: Use when you have a subreddit a subject frequents and want the communities its users also inhabit — returns ranked overlapping subreddits to widen where you look for them.
url: https://subredditstats.com/subreddit-user-overlaps/
category: social-networks
path:
- social-networks
bestFor: Finding which other subreddits overlap in membership with a given subreddit, to map a subject's likely community footprint.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free to use. The maintainer has warned it may shut down due to Reddit's API pricing changes, so treat availability as at-risk.
opsec: passive
opsecNote: You query aggregate community statistics, not any individual account, so nobody is alerted. It reveals nothing about a specific user — only where a community's members tend to cluster.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A hobbyist stats site computing overlap from sampled Reddit activity; the scores are heuristic and depend on Reddit API access that may lapse. Directional, not precise.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- subredditstats user overlap
tags:
- Social Media
- Reddit
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Subreddit Stats User-Overlap

> A "people who post here also post there" map for Reddit — turns one subreddit a subject uses into a ranked list of adjacent communities to check.

## When to use
You've found a subreddit your subject is active in (via their profile, a username hit, or a topic they care about) and you want to broaden the net: which *other* subreddits do that community's members tend to frequent? The overlap ranking points you at the likely neighbouring communities where the same person might also post — useful for expanding a Reddit footprint search or understanding a subject's interests/affiliations.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://subredditstats.com/subreddit-user-overlaps/.
2. Enter a subreddit name (without the `r/`).
3. Read the ranked list: each related subreddit has a "probability multiplier" — e.g. `2` means this community's users are twice as likely as average to be active there; `1` is average; `0` is no overlap.
4. Use the top-ranked subreddits as new hunting grounds: search them (or the subject's known `username`) for the same person, and note interest/location signals.

## Inputs → Outputs
- **In:** a subreddit (community the subject uses) — a `social-profile`-level lead
- **Out:** ranked overlapping subreddits (further `social-profile` communities to search)
- **Empty/negative result looks like:** no/empty overlap list — the subreddit is too small or new to have computed stats, or the dataset is stale. It gives community-level signal only; it will never name or locate an individual user.

## Gotchas & OpSec
- This is aggregate, statistical, and indirect — it tells you where a *community* overlaps, not what any specific person does. Don't over-read it.
- Availability is at risk (Reddit API pricing) and data can be stale; verify the tool still returns results and don't build a workflow that depends on it.
- Passive and privacy-safe — you never query an individual account.

## Overlaps ("do both")
- Do both with a direct Reddit user-history tool and a `site:reddit.com` / Reddit CSE search: this tool tells you *which communities to search*, and those tools then find the subject's actual posts within them.

## Trust & verifiability
`trust: unverified` — a hobbyist analytics site producing heuristic overlap scores from sampled data; useful as a directional map of communities, not as evidence about any individual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | subreddit-stats-user-overlap |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
