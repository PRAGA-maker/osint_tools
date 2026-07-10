---
id: socialblade
name: SocialBlade
description: Use when you have a social `username`/channel and want public statistics — follower history, estimated account age, rank, and linked handles — returns social-profile metadata.
url: https://socialblade.com
category: social-networks
path:
- social-networks
bestFor: Pulling growth stats, activity history, and account-age estimates for a YouTube/Twitch/Instagram/X account.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Core statistics are free with no login; deeper history, exports, and API access require a paid plan.
opsec: passive
opsecNote: Reads public platform statistics; the account owner is not notified. You disclose the handle you're researching to SocialBlade.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established analytics aggregator; follower counts are accurate, but growth figures and "estimated" values are modeled, not exact.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- socialblade-2
- x-com
aliases:
- socialblade.com
- Social Blade
tags:
- social-media-analytics
- account-stats
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# SocialBlade

> A statistics aggregator for YouTube, Twitch, Instagram, X, and more — turns a handle into activity history, growth trends, rank, and account-age signals.

## When to use
You have a subject's social `username`/channel and want to characterize the account rather than read its content: how long it has existed, whether it is active or dormant, when growth spikes happened (which can correlate with real-world events), and its scale. Account-age and activity-timeline signals help build a timeline and separate a real long-standing account from a recent throwaway.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://socialblade.com and pick the platform, then search the handle/channel.
2. Read the dashboard: subscriber/follower history, upload/post cadence, rank/grade, and creation or "since" data.
3. Note growth inflection points and periods of inactivity — they map to timeline events.
4. Pivot: activity gaps hint at real-life changes; the confirmed handle feeds cross-platform enumeration; linked channels reveal alternate accounts.

## Inputs → Outputs
- **In:** `username` / channel ID
- **Out:** `social-profile` (follower history, cadence, rank, age/activity signals)
- **Empty/negative result looks like:** "not tracked yet" for small/new accounts — SocialBlade may need a manual add and some history won't backfill. Absence of stats isn't absence of the account.

## Gotchas & OpSec
- Human-in-the-loop: none for basic stats; exports/history are paywalled.
- OpSec: **passive**; no owner alert.
- Modeled numbers: growth and "estimated" earnings/values are computed, not authoritative — use them as indicators.

## Overlaps ("do both")
- Pairs with `[[x-com]]` — read the actual content behind the statistics you see here.
- Pairs with `[[socialblade-2]]` — alternate entry point / cached views for the same analytics.

## Trust & verifiability
`trust: community` — a reputable, long-running aggregator; raw follower counts are reliable, but treat modeled/estimated figures as approximations to corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socialblade |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
