---
id: twitter-analytics
name: X (Twitter) Analytics
description: Use when you operate a sock-puppet X account and want reach/impression data on your own posts — X's native analytics for the logged-in account only.
url: https://analytics.twitter.com
category: documents-metadata
path:
- documents-metadata
bestFor: Measuring impressions/engagement on your own (or a managed sock-puppet's) X posts.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: freemium
costNote: Native analytics moved to x.com/i/account_analytics and now shows data only for the logged-in account; full analytics are increasingly gated behind X Premium.
opsec: active
opsecNote: This works only while logged into an X account, and it reports on THAT account's own posts — you cannot view a third party's analytics. Use it strictly on a sock-puppet account you control (e.g. to gauge an outreach/appeal post's reach); logging in is an authenticated, attributable action, so keep it off any identity-linked account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party X analytics — the numbers are authoritative for the logged-in account, but its scope is limited to your own account, so it is not a tool for investigating others.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- global-terriorism-database
- murph-live
- parrot-security
- tormap
- twitter-advanced-search
- twitter-com
- twitter-date-search
- twitter-image-search
- twitter-x-location-search
aliases:
- Twitter Analytics
- X Analytics
- analytics.twitter.com
tags:
- twitter
- x
- analytics
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# X (Twitter) Analytics

> X's native analytics dashboard — impressions, engagements, and follower trends **for the logged-in account only**. Useful for a sock-puppet you run, not for measuring a target.

## When to use
You control an X account — typically a sock-puppet or a case/appeal account — and want to know how far its posts reached: impressions, engagements, top posts, follower changes. The classic use for missing-persons work is gauging whether a public appeal tweet is actually being seen. It reports only on the account you're signed into, so it is **not** a way to analyze a subject's account.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into the X account you control (sock-puppet / case account) — the old `analytics.twitter.com` now redirects to `x.com/i/account_analytics`.
2. Open the analytics view.
3. Read per-post impressions/engagements and account-level trends; full detail may require X Premium.
4. Use the reach data to decide whether to boost, re-time, or reword an outreach post.

## Inputs → Outputs
- **In:** none beyond being logged in (it reads the account's own posts)
- **Out:** impressions, engagements, top-post and follower trends for that account
- **Empty/negative result looks like:** sparse or gated metrics — a new account has little data, and deeper analytics may be locked behind Premium; it will never show another user's numbers.

## Gotchas & OpSec
- **Own-account only** — cannot be used to investigate a third party's account. Its OSINT value is limited to your own outreach.
- Requires login (`active`/attributable); use only a sock-puppet, never an identity-linked account.
- X has repeatedly changed and gated analytics; expect features to shift and some to sit behind Premium (`status: degraded`).

## Overlaps ("do both")
- For analyzing *someone else's* X presence, use third-party X profile/audience analysis tools instead — this native dashboard only covers accounts you control.

## Trust & verifiability
`trust: trusted` — first-party and authoritative for the logged-in account, but scope-limited; do not mistake it for a competitor/subject analytics tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-analytics |
| category | documents-metadata |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
