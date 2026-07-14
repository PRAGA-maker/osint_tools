---
id: tweet-binder
name: Tweet Binder
description: Use when you have a `username`, hashtag, or keyword and want to map who is talking about it on X/Twitter — returns social-profile and associate links (top contributors, mentioners, amplifiers).
url: https://www.tweetbinder.com/
category: social-networks
path:
- social-networks
bestFor: Profiling an X/Twitter hashtag, keyword, or account's conversation to surface the top participating accounts and their reach.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: A free report covers up to 200 posts from the last 7 days with no payment. Deeper real-time (next 30 days) and historical reports run up to 35,000 posts on paid plans; the API is a paid add-on.
opsec: passive
opsecNote: You never contact the target account — you query TweetBinder's own index. However, generating a report requires signing in with an X/Twitter account and authorizing the app, so use a sock-puppet X account, not one tied to your real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial social-analytics vendor (clients include Coca-Cola, Google, Disney); reputable but a third-party aggregator, so treat reach/impression figures as estimates.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- tweetdeck
- twitter-advanced-search
aliases:
- TweetBinder
- Twitter hashtag analytics
tags:
- twitter
- social-analytics
- hashtag
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Tweet Binder

> An X/Twitter hashtag & keyword analytics platform, repurposed as a network-mapper: who is participating in a conversation, and which accounts drive it.

## When to use
You have a `username`, hashtag, or keyword tied to your subject — a campaign they ran, an event they attended, a handle they use — and you want to see the cluster of accounts around it: the top contributors, the accounts that mention or amplify them, and rough reach. Good for turning a single lead handle into a web of `associate` accounts to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.tweetbinder.com/ and choose "create free report."
2. Sign in with a sock-puppet X/Twitter account and authorize the app (required to pull posts).
3. Enter the `username` (as `from:handle` or `@handle`), hashtag, or keyword. The free tier returns up to 200 posts from the last 7 days.
4. Read the report: top contributors and most-active accounts (`associate` / `social-profile` leads), influencers by reach, and a timeline. Export to PDF if needed.
5. Pivot: feed newly-surfaced handles into `[[twitter-advanced-search]]` for their own timelines, or into a username tool to check the same handle elsewhere.

## Inputs → Outputs
- **In:** `username` (or hashtag / keyword)
- **Out:** `social-profile`, `associate` (top participating/ amplifying accounts), engagement & reach estimates
- **Empty/negative result looks like:** "no tweets found" for the query, or a report with only a handful of low-signal posts — means the term is dormant in the 7-day free window, not that the account is inactive (history is paywalled).

## Gotchas & OpSec
- Human-in-the-loop: you must OAuth a Twitter/X account to run any report — use a burner, never your investigative identity.
- The free tier is capped at 200 posts / 7 days; anything older or larger needs a paid plan, so absence of results is often just the window, not the truth.
- Reach and impression numbers are modeled estimates, not ground truth.

## Overlaps ("do both")
- Pairs with `[[twitter-advanced-search]]` — TweetBinder finds *which* accounts cluster around a topic; advanced search then pulls each account's raw timeline that TweetBinder samples.

## Trust & verifiability
`trust: community` — a well-established commercial analytics firm with major clients, but it is a third-party aggregator sampling the API, so cross-check specific posts against the live account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tweet-binder |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
