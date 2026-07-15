---
id: tokinsights-com
name: TokInsights
description: Use when you have a TikTok `username`/handle and want historical follower/engagement analytics and tracked account data — returns social-profile stats and growth history.
url: https://tokinsights.com/
category: social-networks
path:
- social-networks
bestFor: In-depth TikTok analytics — tracking an account's follower history, engagement, and video performance from a large scraped TikTok database.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Free tier gives basic insights and account tracking; deeper/market analytics are premium. Its database adds millions of records daily from public TikTok data.
opsec: passive
opsecNote: TokInsights reads public TikTok data from its own database, so looking up a handle does not query TikTok live or notify the subject — passive. Creating a tracking dashboard requires an account; use a sock-puppet email if you don't want the lookups tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party TikTok scraper/analytics service; the numbers derive from public TikTok data but the aggregation is unofficial, so treat metrics as indicative and verify the account on TikTok itself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- exolyt
- urlebird
aliases:
- TokInsights
- tokinsights.com
tags:
- tiktok
- TikTok Related Sites
- analytics
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# TokInsights

> A TikTok analytics service backed by a large scraped database: track a handle's follower history, engagement, and video performance over time.

## When to use
You have a subject's TikTok `username` and want more than the current profile — historical follower growth, engagement trends, and per-video performance — to gauge activity, spot spikes tied to events, or confirm an account is genuinely the subject's. Useful when the live TikTok profile shows only the present state and you need the trajectory.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tokinsights.com/ and search the subject's TikTok `username`/handle.
2. Read the profile analytics: follower count and history, engagement, and video-level stats drawn from the service's database.
3. Optionally register (sock-puppet email) to add the account to a tracking dashboard and watch daily changes going forward.
4. Note growth spikes/drops and dates — they often correlate with real-world events or content that's worth investigating.
5. Pivot: the confirmed handle and linked content feed cross-platform `username` searches; profile images feed reverse-image/face search; bio links feed other `social-profile`s.

## Inputs → Outputs
- **In:** TikTok `username`/handle (or display `name`).
- **Out:** `social-profile` analytics — follower history, engagement, video performance, display `name`.
- **Empty/negative result looks like:** the account isn't in the database or returns no history — it may be new, tiny, private, or simply un-tracked. Absence of analytics is not proof the account is inactive; check TikTok directly.

## Gotchas & OpSec
- Numbers come from an unofficial scrape and may lag or differ from TikTok's own — treat them as indicative, and confirm the account identity on TikTok itself.
- Deeper analytics sit behind a paywall; the free tier is limited.
- Handles can be changed on TikTok; corroborate that the tracked account is still your subject's.

## Overlaps ("do both")
- Pairs with `[[exolyt]]` (another TikTok analytics service) and `[[urlebird]]` (TikTok content viewer) — cross-check metrics across services since each scrapes differently, and use a content viewer to actually read the posts behind the numbers.

## Trust & verifiability
`trust: unverified` — a third-party analytics scraper. The underlying data is public TikTok activity, so it's checkable, but the aggregation is unofficial; verify the account and any decision-driving metric against TikTok directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tokinsights-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
