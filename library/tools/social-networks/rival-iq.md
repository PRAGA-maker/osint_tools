---
id: rival-iq
name: Rival IQ
description: Use when you have a public `social-profile`/`username` and want its cross-platform posting history, engagement metrics and audience behaviour — returns social-profile, associate (linked accounts/competitor set).
url: https://www.rivaliq.com
category: social-networks
path:
- social-networks
bestFor: Analysing a public account's social metrics/history across platforms and comparing it head-to-head with others.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Freemium — free "Head-to-Head" comparison reports and a 14-day trial (no card); the full analytics suite (Instagram/Facebook/X/TikTok/LinkedIn/YouTube) is a paid subscription.
opsec: passive
opsecNote: Analytics are computed from public social data, so a lookup does not notify the account owner. Full access requires an account/trial, tying queries to your identity — use a sock-puppet signup, not a corporate identity, if attribution matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial social-analytics vendor; metrics are computed estimates for marketing use, not investigative ground truth, but the underlying posts/engagement it surfaces are real public data.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
aliases:
- RivalIQ
tags:
- real-time-search-social-media-search-and-general-social-media-tools
- social-analytics
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Rival IQ

> A commercial social-media analytics platform: profile a public account's posting history, engagement, and audience behaviour across the major networks — with a free head-to-head comparison tier.

## When to use
You have a public `username`/`social-profile` (a brand, org, or public figure) and want a data view of its activity: posting cadence, engagement trends, top content, hashtags, and how it compares to peer accounts. Useful to characterise a public-facing subject, establish a baseline of "normal" activity, or spot the competitor/peer set (`associate`) they're grouped with. It's an analytics tool for public accounts — not a private-individual locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.rivaliq.com. Use the free Head-to-Head report for a quick public comparison, or start the 14-day trial for the full suite.
2. Add the target public account(s) across the platforms of interest.
3. Review metrics: posting history/timeline, engagement rates, top posts, hashtag/topic patterns, audience behaviour.
4. Use Head-to-Head to place the account against peers and reveal its competitive/associated set.
5. Pivot: confirmed cross-platform handles feed direct profile OSINT and username enumeration; posting-time patterns can hint at timezone/`geolocation`.

## Inputs → Outputs
- **In:** `username`/`social-profile` (public accounts)
- **Out:** `social-profile` (metrics/history across platforms), `associate` (peer/competitor set, linked accounts), engagement analytics
- **Empty/negative result looks like:** private or very small accounts return little/no data — the platform is built for public, active accounts; absence isn't evidence about the person.

## Gotchas & OpSec
- Human-in-the-loop: full features need an account/trial; only Head-to-Head is truly free.
- Metrics are modelled estimates for marketers — don't cite engagement figures as hard fact.
- Best for public brands/figures; thin for private individuals.
- OpSec: passive to the target; sign up with a sock puppet if your interest must stay unattributed.

## Overlaps ("do both")
- Pairs with [[klear]]-style influencer analytics and direct profile OSINT — Rival IQ characterises public activity; direct scraping/enumeration confirms the handles it surfaces.

## Trust & verifiability
`trust: community` — a real, established analytics vendor; the public posts/engagement it surfaces are genuine, but treat computed metrics as estimates and verify handles directly.
