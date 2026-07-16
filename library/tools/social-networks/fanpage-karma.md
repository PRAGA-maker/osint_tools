---
id: fanpage-karma
name: Fanpage Karma
description: Use when you have a public `social-profile` (page/account) and want its analytics — posting cadence, engagement, follower trends — returns `metadata-exif`-style activity patterns.
url: http://www.fanpagekarma.com
category: social-networks
path:
- social-networks
bestFor: Profiling a public social account's posting patterns, best times, hashtags and engagement metrics.
selectorsIn:
- social-profile
- username
selectorsOut:
- metadata-exif
- social-profile
status: live
pricing: freemium
costNote: Freemium — free public tools (Performance Score, Instagram hashtag research, competition comparison, annual report). Full multi-profile analytics and history require a paid account/trial.
opsec: passive
opsecNote: Analyzes publicly available page data; the target isn't notified. Free tools work without deep access; the paid platform's connect-your-profiles mode is for accounts you own, not a way in to targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established social-analytics vendor; metrics are computed from public data, so they're indicative aggregates rather than authoritative facts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- FanpageKarma
tags:
- facebook
- instagram
- analytics
- social-metrics
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- app-fanpagekarma-com
---

# Fanpage Karma

> A social-analytics platform: point it at a public page/profile and get posting cadence, best-time-to-post, hashtags and engagement trends — behavioural pattern data rather than identity data.

## When to use
You already have a subject's public `social-profile` (Facebook page, Instagram, Twitter/X, YouTube, TikTok) and want to understand *behaviour*: when they post (which can hint at timezone/routine), what hashtags and topics recur, engagement trends and follower growth. Useful for pattern-of-life and timezone inference, or profiling an organisation's account — not for finding or identifying a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.fanpagekarma.com and use a free tool — e.g. the Performance Score, Instagram hashtag research, or the competition/comparison tool — entering the public profile/page.
2. Read the output: posting frequency, best posting times/days, top hashtags, engagement rate, follower trend.
3. For deeper history and multi-profile analysis, start a paid trial (registration required).
4. Note posting-time clusters as a **timezone/routine** signal and recurring hashtags/topics as interests/associates.
5. Pivot: feed inferred timezone into geolocation reasoning; feed recurring tagged accounts into associate mapping.

## Inputs → Outputs
- **In:** a public `social-profile`/`username` (page or account)
- **Out:** `metadata-exif`-style behavioural metrics (posting times, cadence, hashtags, engagement, follower trend)
- **Empty/negative result looks like:** thin/empty analytics — the account is too small/private, or the platform isn't fully supported in the free tool; it computes nothing meaningful from a near-empty profile.

## Gotchas & OpSec
- It profiles **known** accounts — it won't find or identify a person; bring the profile to it.
- Metrics are computed aggregates from public data; treat posting-time/timezone inferences as hints, not proof.
- The richest features are paywalled; free tools are limited in depth/history.

## Overlaps ("do both")
- Pairs with platform-native analytics and other timeline tools — Fanpage Karma's value is the posting-cadence/timezone read that complements content-level review.

## Trust & verifiability
`trust: community` — a legitimate analytics vendor; its numbers are indicative aggregates of public activity, so use behavioural inferences as leads corroborated by content, not standalone facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fanpage-karma |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → metadata-exif, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
