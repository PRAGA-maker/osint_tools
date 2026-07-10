---
id: iconosquare
name: Iconosquare
description: Use when you have an Instagram/TikTok `social-profile` and want analytics on it — returns follower trends, posting patterns, hashtags, and engagement for account profiling.
url: http://iconosquare.com
category: social-networks
path:
- social-networks
bestFor: Social-media analytics (Instagram, TikTok, and others) — follower growth, posting cadence, top hashtags, and engagement metrics.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: freemium
costNote: Paid analytics platform (subscription) with a limited free audit/trial. Deep, historical analytics require a paid plan; it is marketed to marketers, not as a free OSINT tool.
opsec: passive
opsecNote: Analysing public account metrics is passive and does not notify the account. A trial/account requires your details — register with a sock-puppet identity; connecting your own accounts is unnecessary for analysing a third party's public metrics.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: An established commercial social-analytics vendor; metrics are derived from public data and generally reliable directionally, but it's a marketing tool, not an identity source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- socialblade
- exolyt
- playboard-co
aliases:
- Iconosquare
- iconosquare.com
tags:
- instagram
- analytics
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Iconosquare

> A commercial social-media analytics platform (Instagram, TikTok, and more) — profile an account's growth, posting rhythm, hashtags, and engagement rather than find a person.

## When to use
Your subject runs a public Instagram/TikTok account and you want behavioural analytics on it: follower-growth trends, when and how often they post (a pattern-of-life/timezone signal), the hashtags and topics they use, and engagement levels. It's a profiling/context tool for content-creator subjects, not a people-finder — hence low direct missing-persons value, but useful for understanding an account's activity and reach.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to iconosquare.com and start a free audit/trial (use a sock-puppet identity).
2. Point the analytics at the target's public `username`/`social-profile`.
3. Read the metrics: follower trends, posting cadence and timing, top hashtags, and engagement.
4. Note posting-time clustering as a timezone/routine clue; deeper history needs a paid plan.
5. Pivot: hashtags/topics feed keyword and image search; posting patterns corroborate other timeline evidence; compare with `[[socialblade]]`/`[[exolyt]]`.

## Inputs → Outputs
- **In:** Instagram/TikTok `username`/`social-profile`
- **Out:** account analytics — follower trends, posting cadence/timing, hashtags, engagement (`metadata-exif`-style behavioural metadata)
- **Empty/negative result looks like:** thin data for a tiny/inactive account, or a paywall on the historical detail — the free audit is shallow.

## Gotchas & OpSec
- Human-in-the-loop: it's a **paid** platform; the free audit/trial is limited.
- Marketing-oriented — great for content behaviour, not for identifying who someone is.
- OpSec: passive toward the target; only your own registration details are exposed. Don't connect your real accounts to analyse a third party.

## Overlaps ("do both")
- Overlaps with `[[socialblade]]`, `[[exolyt]]` (TikTok), and `[[playboard-co]]` (YouTube) — pick the analytics tool matching the platform and cross-check figures.

## Trust & verifiability
`trust: community` — a reputable analytics vendor whose metrics are reliable directionally, but derived and marketing-focused. Treat figures as approximate and confirm account identity on the platform itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iconosquare |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
