---
id: klear
name: Klear
description: Use when you have an `name`/`username` of a social-media creator and want audience/reach analytics and profile discovery across Instagram, TikTok and YouTube — returns social-profile, associate (audience/brand links).
url: http://klear.com
category: social-networks
path:
- social-networks
bestFor: Influencer/creator discovery and audience analytics across major social platforms.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- associate
status: degraded
pricing: freemium
costNote: Klear has been folded into Meltwater's Influencer Marketing suite; klear.com now redirects to meltwater.com. It is an enterprise, demo-and-quote product with no meaningful self-service free tier — expect a sales gate, not a public lookup box.
opsec: passive
opsecNote: Analytics are computed from public social data, so a lookup does not notify the target. But access requires a corporate account/demo, which ties every query to your organisation's identity — not suitable for covert single-subject work.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Legitimate commercial analytics vendor (now Meltwater), but a marketing product, not an investigative one; figures are modelled estimates ("True Reach", audience demographics), not ground truth.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Meltwater Influencer Marketing
- Klear influencer analytics
tags:
- real-time-search-social-media-search-and-general-social-media-tools
- influencer-analytics
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Klear

> A commercial influencer-analytics platform (now Meltwater) that profiles a creator's reach and audience — powerful for social discovery, but gated behind an enterprise sales wall.

## When to use
You have a creator's `name` or `username` and want to characterise their audience, cross-platform footprint, and engagement — e.g. confirming an account is genuinely active, sizing its reach, or discovering related creators/brands (`associate`). It is a discovery/analytics tool, not a person-locator; reach for it when the subject is a public-facing content creator rather than a private individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Note that http://klear.com now redirects to Meltwater's Influencer Marketing suite (meltwater.com).
2. Access requires an enterprise account or a booked demo — there is no public search box. Request a demo/trial through Meltwater sales if you have a legitimate business account.
3. Inside the suite, search the 30M+ creator database by name/handle or filter by platform, niche, and audience criteria.
4. Read a creator card: linked `social-profile`s across Instagram/TikTok/YouTube, "True Reach", audience demographics, bot-detection flags, and related creators/brands.
5. Pivot: use the confirmed cross-platform handles as `username` seeds for direct, free profile OSINT elsewhere.

## Inputs → Outputs
- **In:** `name` or `username` (creator/handle)
- **Out:** `social-profile` (cross-platform handles), `associate` (audience segments, related creators/brands), modelled reach/engagement metrics
- **Empty/negative result looks like:** the creator isn't in the 30M database (typical for small/private accounts) — absence here says nothing about the person, only that they aren't a tracked influencer.

## Gotchas & OpSec
- Human-in-the-loop: hard sales/paywall gate — no casual anonymous lookups.
- Metrics are estimates, not audited counts; don't cite "True Reach" as fact.
- Best used only when the subject is a public creator; useless for private individuals.

## Overlaps ("do both")
- Pairs with free, no-login discovery tools — use Klear (if you have access) to confirm reach, then pivot the handles it verifies into direct profile scraping and username enumeration.

## Trust & verifiability
`trust: community` — an established commercial vendor, so the platform is real and maintained, but it is marketing analytics: treat all audience/reach figures as modelled estimates.
