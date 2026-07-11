---
id: twitonomy
name: Twitonomy
description: Use when you have a Twitter/X `username` and want profile analytics — activity patterns, mentions, top interactions, follower analysis — returns social-profile and associate leads.
url: https://www.twitonomy.com/
category: social-networks
path:
- social-networks
- twitter
- analytics
- profile
bestFor: Profile-level Twitter/X analytics — posting patterns, most-mentioned/retweeted accounts, and follower/following breakdowns for behavioral baselining.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: degraded
pricing: freemium
costNote: Free tier with a Twitter/X sign-in for basic analytics; deeper reports/exports are a paid premium plan. Functionality is constrained by X's current API access.
opsec: active
opsecNote: Requires signing into Twitter/X (OAuth) to run analytics — you authorize Twitonomy against an account, so use a sock-puppet X account, never your real one. Reading a public profile's analytics does not notify the target, but the third-party app authorization is tied to whatever account you log in with.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing third-party Twitter analytics service; results reflect X's API-permitted data, which has shrunk over time — treat coverage as partial and possibly stale.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- x0rz-tweets-analyzer
- social-searcher
aliases:
- Twitonomy
- twitonomy.com
tags:
- twitter
- analytics
- behavioral-profiling
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Twitonomy

> A web-based Twitter/X analytics dashboard — enter a username and get posting patterns, most-interacted accounts, and follower/following analysis for behavioral baselining.

## When to use
You have a Twitter/X `username` and want a quick, no-install analytics read: when and how often they post, which accounts they most mention/retweet (`associate` leads), and follower/following breakdowns (including non-mutuals and geographic mapping). Useful for pattern-of-life and network mapping. **Caveat:** X's API restrictions have degraded third-party analytics broadly — expect partial data and verify anything critical on-platform.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.twitonomy.com/ and sign in with a **sock-puppet** Twitter/X account (OAuth authorization required).
2. Enter the target's @username.
3. Read the dashboard: tweet/reply/retweet counts and timing, most-mentioned and most-retweeted users, hashtags, and follower/following analytics.
4. Use premium/export only if you need deeper reports; otherwise triage the free view.
5. Pivot: most-interacted accounts are `associate` leads; posting-time patterns hint at timezone/routine; corroborate with [[x0rz-tweets-analyzer]] or on-platform.

## Inputs → Outputs
- **In:** Twitter/X `username`
- **Out:** `social-profile` analytics (activity timing, hashtags, engagement), `associate` links (most-mentioned/retweeted accounts), follower/following breakdown
- **Empty/negative result looks like:** sparse or missing analytics / API errors — with X's API limits this is common; a thin result often reflects API constraints, not an inactive account.

## Gotchas & OpSec
- **API-dependent and degraded:** X's restrictions have cut what third-party analytics can pull; data may be partial or stale — don't treat gaps as facts.
- Requires OAuth sign-in — authorize only with a burner X account; revoke the app afterward.
- OpSec: **active** in that you authorize a third-party app against an account; keep it segregated from your identity.

## Overlaps ("do both")
- Pairs with [[x0rz-tweets-analyzer]] (CLI behavioral profiling) and [[social-searcher]] (cross-network content) — combine Twitonomy's engagement/network view with content and timing from those.

## Trust & verifiability
`trust: community` — an established third-party analytics service, but limited by X's API and thus partial. Use its outputs as leads and confirm the underlying tweets/relationships directly on X.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitonomy |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
