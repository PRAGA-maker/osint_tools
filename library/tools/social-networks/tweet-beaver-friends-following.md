---
id: tweet-beaver-friends-following
name: TweetBeaver — Friends/Following
description: Use when you have two Twitter/X `username`s and want to see the accounts they both follow or that follow both — returns the overlapping `social-profile` connections between them.
url: https://tweetbeaver.com/friendsfollowing.php
category: social-networks
path:
- social-networks
bestFor: Finding the mutual connections between two Twitter/X accounts (who they both follow / who follows both) to map relationships.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: freemium
costNote: Free to use the basic tools; you must sign in with a Twitter/X account. Functionality is constrained by X's API restrictions.
opsec: active
opsecNote: TweetBeaver requires you to authorize it with a Twitter/X account, so all queries run through — and are visible to — that account. Always connect a dedicated sock-puppet account, never your own.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-standing third-party Twitter-tools site; useful when it works, but its capabilities have been cut back by X's API lockdown, so verify current behavior.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- tweetbeaver
aliases:
- TweetBeaver friends following
tags:
- Social Media
- Twitter
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# TweetBeaver — Friends/Following

> A relationship-mapping tool for Twitter/X — feed it two handles and it shows the accounts they have in common, exposing the link between two people.

## When to use
You have two Twitter/X `username`s and want to know how they are connected: the accounts they both follow, or the accounts that follow both of them. Mutual connections are strong evidence of a real-world or online relationship — useful for confirming an association or finding the shared circle around a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://tweetbeaver.com/ and sign in with a **sock-puppet** Twitter/X account (required).
2. Open the Friends/Following comparison tool.
3. Enter the two `username`s to compare.
4. Read the output: the overlapping accounts (`social-profile`) — common follows and/or common followers between the two.
5. Pivot: investigate the shared connections as `associate` leads; run each on other social tools.

## Inputs → Outputs
- **In:** `username` × 2 (Twitter/X handles)
- **Out:** `social-profile` (accounts in common between the two handles)
- **Empty/negative result looks like:** no overlap returned — the accounts share no visible connections, OR (increasingly common) X API limits blocked the query; distinguish the two before concluding.

## Gotchas & OpSec
- **Status: degraded** — X's API restrictions since 2023 have curtailed these third-party tools; expect partial results, rate limits, or failures, and confirm it's working before relying on it.
- Requires authorizing a Twitter/X account — **active and attributable**; use a throwaway, never a personal login.
- Only public relationships are visible; very large accounts may not fully process.

## Overlaps ("do both")
- Pairs with `[[tweetbeaver]]` (its other lookups) and native X search — do both, since API limits mean any single tool may return incomplete connection data.

## Trust & verifiability
`trust: unverified` — a third-party tool dependent on X's API; results are only as complete as the API currently allows, so treat overlaps as leads and confirm on X directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tweet-beaver-friends-following |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
