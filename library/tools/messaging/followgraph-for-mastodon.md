---
id: followgraph-for-mastodon
name: Followgraph for Mastodon
description: Use when you have a Mastodon `username`/handle and want the accounts followed by the people they follow — returns associate and social-profile leads for network mapping.
url: https://followgraph.vercel.app/
category: messaging
path:
- messaging
bestFor: Expanding a Mastodon handle into a ranked list of second-degree accounts to map a subject's network and likely associates.
selectorsIn:
- username
selectorsOut:
- associate
- social-profile
status: live
pricing: free
costNote: Free web tool; no payment. Requires authorizing with your own Mastodon account to read the follow graph via the API.
opsec: active
opsecNote: You must log in with a Mastodon account to run it, and it queries the target's public follow lists via the API — use a sock-puppet Mastodon account, never a real one, since the authorization and API calls originate from whatever account you connect.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Small open-source community tool (hosted on Vercel) that reads public follower/following data through the Mastodon API; unofficial but transparent.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- followgraph
- followgraph.vercel.app
tags:
- mastodon
- social-media
- network-mapping
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- what-goes-on-mastodon
- gitvio
- osint-steam
- section-16-deadline-calculator
- xplore-x-vercel-app
- youtube-lookup
---

# Followgraph for Mastodon

> A second-degree Mastodon network expander: give it a handle and it lists the accounts followed by the people that handle follows, ranked by how many of them follow each one.

## When to use
You have a subject's Mastodon `username`/handle and want to map their social circle. Followgraph surfaces the accounts most commonly followed by the people your subject follows — a strong signal for their community, likely `associate`s, and other `social-profile`s in the same orbit that a flat follower list would miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://followgraph.vercel.app/.
2. Enter your own (sock-puppet) Mastodon instance and authorize the app — it needs API access to read follow graphs.
3. It computes, for the accounts you (or a target handle) follow, the accounts *they* commonly follow, ranked by frequency.
4. Review the ranked list: high-frequency accounts are the community's hubs and your subject's probable associates/interests.
5. Pivot: take notable handles to a Mastodon profile lookup and expand each; cross-reference names/avatars against other platforms.

## Inputs → Outputs
- **In:** Mastodon `username`/handle (and your authorizing account)
- **Out:** ranked second-degree accounts → `associate` and `social-profile` leads.
- **Empty/negative result looks like:** a very short or empty list — the account follows almost no one, is new, or its follows are private/locked, so there is no graph to expand.

## Gotchas & OpSec
- Requires OAuth login with a Mastodon account — always use a throwaway, never a personal/attributable one (`account-login`).
- Locked/private accounts and instances that restrict the API return little; results are only as complete as public follow data.
- "Followed by the people they follow" is an interest/community signal, not proof of a personal relationship — treat as leads.

## Overlaps ("do both")
- Pairs with `[[what-goes-on-mastodon]]` — that tells you which instances are active to search, while Followgraph expands a known handle into its network.

## Trust & verifiability
`trust: community` — an unofficial open-source tool reading the public Mastodon API; the follow data is real and platform-sourced, but the ranking is a heuristic, so verify key associates on their actual profiles.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | followgraph-for-mastodon |
| category | messaging |
| selectorsIn → selectorsOut | username → associate, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
