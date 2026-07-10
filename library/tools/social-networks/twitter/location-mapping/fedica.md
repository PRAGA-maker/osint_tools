---
id: fedica
name: Fedica
description: Use when you have a public `username`/account and want audience analytics, posting patterns, and follower-location mapping — returns `geolocation` (audience/location distribution), activity patterns, and `social-profile` insights.
url: https://fedica.com/
category: social-networks
path:
- social-networks
- twitter
- location-mapping
bestFor: Cross-platform social analytics — mapping an account's follower locations and analyzing its posting behavior and audience.
selectorsIn:
- username
selectorsOut:
- geolocation
- social-profile
status: live
pricing: freemium
costNote: Freemium — a free tier with limited analyses/history; deeper analytics, larger accounts, and export are paid. Connecting your own account unlocks more; analyzing others is more limited on free.
opsec: active
opsecNote: Fedica (formerly Tweepsmap) is a registered platform that authenticates via your social accounts. Connecting an account exposes it to Fedica and can, for your own account, be visible to the platform; analyzing a third-party public account is less intrusive but still logged. Use a sock-puppet account and never connect a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: An established social-analytics vendor (formerly Tweepsmap); metrics are computed from public/platform data and are reliable in aggregate, though follower-location is inferred, not exact.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Fedica
- Tweepsmap
tags:
- twitter
- x-com
- social-analytics
- audience-mapping
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Fedica

> Cross-platform social analytics (formerly Tweepsmap) — map an account's follower locations and profile its posting patterns and audience.

## When to use
You have a public `username`/account (X and other platforms) and want aggregate intelligence about it: where its followers are geographically, when and how often it posts, engagement patterns, and audience makeup. Useful for characterizing an account's likely region/community and its behavioral rhythm rather than identifying one person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register/log into Fedica with a sock-puppet account (https://fedica.com/).
2. Enter/analyze the target public account (scope depends on your plan; connecting your own account unlocks the deepest analytics).
3. Read the reports: follower-location map (`geolocation` distribution), posting-time patterns, top content, and audience analytics.
4. Pivot: follower-location clusters + posting times hint at the account operator's timezone/region; combine with `[[reddit-metis]]`-style behavioral profiling on other platforms.

## Inputs → Outputs
- **In:** `username`/account (public)
- **Out:** `geolocation` (follower/audience location map), posting-pattern/timezone signals, engagement/audience analytics, `social-profile` insights
- **Empty/negative result looks like:** thin or no analytics — very small/new accounts, private accounts, or platform API limits yield little. Sparse data ≠ tool failure.

## Gotchas & OpSec
- Follower-location is inferred/aggregate — a regional signal, not the operator's exact location.
- Analyzing others is more limited than analyzing a connected account; free tier is capped.
- Active/authenticated — sock-puppet account only; never connect a personal one.

## Overlaps ("do both")
- Pairs with `[[fedica]]`-style analytics on other platforms and behavioral profilers (`[[reddit-metis]]`) — cross-platform patterns and audience geography together sharpen a location/identity hypothesis.

## Trust & verifiability
`trust: community` — an established analytics vendor; aggregate metrics are dependable, but treat inferred follower-location and audience attributes as directional signals, not facts about the operator.
