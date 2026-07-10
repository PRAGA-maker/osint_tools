---
id: exolyt
name: Exolyt
description: Use when you have a TikTok `social-profile`/`username` and want analytics on it — returns posting patterns, engagement, audience geography and growth history.
url: https://exolyt.com/
category: social-networks
path:
- social-networks
bestFor: TikTok account/video analytics — activity timelines, engagement, audience demographics and geographic breakdown.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- metadata-exif
- geolocation
status: live
pricing: freemium
costNote: Freemium — a free trial/limited view exists, but the useful depth (history, audience geography, comparisons) sits behind paid plans.
opsec: passive
opsecNote: Exolyt analyzes TikTok's public data on its own platform, so the target account isn't directly touched or notified. Your account/searches tie to Exolyt; use a work-appropriate account and note it's a third-party analytics vendor.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: An established TikTok analytics vendor; its metrics (engagement, growth) are derived estimates — good for patterns and relative comparison, not exact ground truth.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
relatedTools:
- osintgram
aliases:
- exolyt.com
tags:
- tiktok
- analytics
- social-media
source: kimi-tiktok-snap
lastVerified: '2026-07-10'
enrichment: full
---

# Exolyt

> A TikTok analytics platform — feed it an account and get posting cadence, engagement, growth history and audience geography, useful for building a behavioural/timeline picture of a TikTok subject.

## When to use
You have a TikTok `username`/profile and want more than the app shows: when they post (timeline/cadence that can hint at timezone/routine), engagement trends, follower growth over time, and — importantly for locate work — audience geographic breakdown. It's analytics, not content extraction: use it to understand patterns and reach, and pair it with a content tool to pull the actual posts/media.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at https://exolyt.com/ and enter the target TikTok `username`/profile.
2. Review the analytics: posting frequency/times, engagement rate, growth history, and audience demographics/geography.
3. Note posting-time clusters (possible timezone) and top audience regions as `geolocation` hints.
4. Deeper history/comparisons are paywalled; the free view still gives headline patterns.
5. Pivot: the behavioural picture guides where/when to look; extract the actual content/associates with a TikTok content tool, and cross-reference the handle elsewhere.

## Inputs → Outputs
- **In:** `username` / TikTok `social-profile`
- **Out:** `metadata-exif` (posting cadence, engagement, growth), audience `geolocation` breakdown, and confirmed `social-profile` stats
- **Empty/negative result looks like:** thin/no data for a tiny or private account — analytics need public activity; a sparse result means low activity, not necessarily the wrong account.

## Gotchas & OpSec
- Metrics are **estimates**, best for patterns/comparison, not exact figures.
- Audience geography is *audience*, not the *account owner's* location — a hint, not a fix.
- Human-in-the-loop: registration required and depth is **paywalled**.
- OpSec: passive toward the target; it's a third-party analytics vendor.

## Overlaps ("do both")
- Complements content extractors like `[[osintgram]]` (Instagram analog) and TikTok downloaders — Exolyt gives the analytical/behavioural layer; those give the actual posts, captions and associates. Do both.

## Trust & verifiability
`trust: community` — a legitimate analytics vendor with estimated metrics; treat numbers as directional and confirm any location inference with harder evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exolyt |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile, metadata-exif, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
</content>
