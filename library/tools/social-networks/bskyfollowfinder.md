---
id: bskyfollowfinder
name: BskyFollowFinder
description: Use when you have a Bluesky `username`/`social-profile` and want to map its social graph — returns associate accounts that the profile's own follows collectively follow but it doesn't.
url: https://bsky-follow-finder.theo.io/
category: social-networks
path:
- social-networks
bestFor: Surfacing the likely-relevant accounts around a Bluesky profile via mutual-follow graph analysis.
selectorsIn:
- username
- social-profile
selectorsOut:
- associate
- social-profile
status: live
pricing: free
costNote: Free browser tool; reads public Bluesky (AT Protocol) data, no account or API key.
opsec: passive
opsecNote: It queries public AT Protocol data, so you don't follow, message, or otherwise touch the target's account. Nothing notifies the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent tool (theo.io) featured in the Bellingcat toolkit; reads public Bluesky data, results are reproducible from the open network.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- BskyFollowFinder
- Bluesky network analyzer
- bsky-follow-finder
tags:
- bellingcat-toolkit
- other-platforms
- bluesky
- social-graph
source: bellingcat-toolkit
lastVerified: '2026-07-21'
enrichment: full
---

# BskyFollowFinder

> A Bluesky social-graph analyzer: given a handle, it finds the accounts most followed by that person's own follows — the cluster they're embedded in but may not yet follow.

## When to use
Your subject has a Bluesky (`social-profile`) account and you want to map their community and likely associates. BskyFollowFinder aggregates who the subject's follows collectively follow, ranking accounts that are central to their network but that the subject themselves doesn't follow. That reveals the surrounding social cluster — colleagues, group members, alternate accounts — to widen the investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bsky-follow-finder.theo.io/.
2. Enter the target's Bluesky handle (e.g. `name.bsky.social`).
3. Let it pull the public follow graph and read the ranked list of accounts common among the subject's follows.
4. Review high-ranking accounts for likely `associate`s, community hubs, or connected identities.
5. Pivot: promising handles feed profile review, username-reuse checks, and further graph passes.

## Inputs → Outputs
- **In:** a Bluesky `username`/`social-profile` handle
- **Out:** ranked `associate`/`social-profile` accounts central to the subject's follow network
- **Empty/negative result looks like:** few or no results for an account with very few follows, a brand-new account, or a private/blocked graph — sparse output means a thin network, not a tool failure.

## Gotchas & OpSec
- Works on the *public* follow graph; accounts the subject doesn't follow but that are popular in their circle rise to the top — treat these as leads, not confirmed ties.
- Bluesky is smaller than X, so coverage depends on the subject actually being active there.
- OpSec: passive; only public AT Protocol data is read.

## Overlaps ("do both")
- Pairs with general Bluesky profile viewers and cross-platform username search — this maps the graph; those confirm identity and content behind each handle.

## Trust & verifiability
`trust: community` — an independent Bellingcat-listed tool reading open Bluesky data; its ranking is reproducible from the public network.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bskyfollowfinder |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → associate, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
