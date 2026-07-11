---
id: dolphin-radar
name: Dolphin Radar
description: Use when you have a public Instagram `username` and want to monitor its behaviour over time — returns tracked follows/unfollows, likes, engagement patterns and downloaded stories/highlights.
url: https://www.dolphinradar.com/web-viewer-for-instagram
category: social-networks
path:
- social-networks
bestFor: Longitudinal tracking of a public Instagram account's activity — who it starts following, what it likes, and its posting/engagement patterns — without logging into Instagram.
selectorsIn:
- username
- social-profile
selectorsOut:
- associate
- social-profile
- image
status: live
pricing: freemium
costNote: A limited free/preview view exists, but meaningful continuous tracking and full analytics are paywalled behind paid plans; treat it as a paid monitoring service with a teaser tier.
opsec: passive
opsecNote: Dolphin Radar analyses only publicly-available data from its own infrastructure, so your identity is not exposed to the target and no viewer trace is left. Ethically/legally, persistently tracking an individual's activity can cross into stalking — use only with proper authority and case justification.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial third-party Instagram-monitoring product; it infers activity from public signals, so results are estimates and coverage depends on Instagram's evolving anti-scraping defences.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
aliases:
- dolphinradar.com
- Dolphin Radar Instagram tracker
tags:
- instagram
- monitoring
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Dolphin Radar

> A paid Instagram-monitoring service that watches a public account for you — new follows, likes and story activity over time — surfacing the relationships and routines a single snapshot misses.

## When to use
You have a public Instagram `username` and need *change over time*, not just the current profile: who the account newly follows (candidate new `associate`s/contacts), what it likes, when it's active, and its stories/highlights captured before they expire. This is powerful for a subject actively using Instagram — the follow/like trail can reveal a new partner, location, or social circle. Use it when persistent behavioural monitoring is justified and authorised.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.dolphinradar.com/ and add the target public `username` to track (registration required; paid plan for full data).
2. Let it accumulate history; then review the activity feed: new follows/unfollows, likes, engagement trends.
3. Pull captured stories/highlights and profile media for offline analysis.
4. Note new accounts the target follows — these are fresh leads.
5. Pivot: newly-followed handles feed associate mapping and `[[toutatis]]`; captured story imagery feeds `[[pimeyes]]`/geolocation.

## Inputs → Outputs
- **In:** a public Instagram `username`/`social-profile`
- **Out:** tracked `associate` signals (new follows), engagement patterns, `social-profile` activity timeline, downloaded story/highlight `image`s
- **Empty/negative result looks like:** little or no data — the account is private (nothing trackable), newly created, or Instagram has throttled the scrape; a private target yields nothing here.

## Gotchas & OpSec
- Paywall: the free view is a teaser; real monitoring costs money.
- Estimates, not ground truth: activity is inferred from public signals and can lag or miss events — corroborate before drawing conclusions.
- **Ethics/legality**: continuous tracking of a private individual can constitute stalking/harassment — proceed only with lawful authority and documented justification.
- OpSec: passive to the target (their servers do the fetching).

## Overlaps ("do both")
- Pairs with `[[toutatis]]` — Dolphin Radar shows behaviour over time; Toutatis extracts the account's hidden contact data.
- Pairs with `[[publer-io]]`/`[[inflact-com-5]]` — those grab public media on demand; Dolphin Radar watches the account continuously.

## Trust & verifiability
`trust: community` — a commercial monitoring vendor inferring activity from public data; treat outputs as leads to verify, since accuracy and coverage shift with Instagram's countermeasures.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dolphin-radar |
