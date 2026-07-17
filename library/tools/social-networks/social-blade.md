---
id: social-blade
name: Social Blade
description: Use when you have a `username`/channel on YouTube, Twitch, Instagram, TikTok or X and want growth stats and account history — returns `social-profile` metadata and activity trends.
url: https://socialblade.com/
category: social-networks
path:
- social-networks
bestFor: Pulling public follower/subscriber history, growth rate and creation-era signals for a social account.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Core stats are free without login; historical depth, exports and API access require a paid plan or account.
opsec: passive
opsecNote: You query Social Blade's own aggregated dataset, not the target's account; the subject is not notified and no interaction reaches their profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-established third-party analytics aggregator; follower counts are accurate but growth estimates and rankings are their own calculations, not platform-official figures.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- socialblade
aliases:
- SocialBlade
- Social Blade Stats
tags:
- Social Media
- Universal
- analytics
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Social Blade

> Cross-platform social analytics — turns a username into follower history, growth curves and activity trends across YouTube, Twitch, Instagram, TikTok and X.

## When to use
You have a `username` or `social-profile` on a major platform and want to understand the account's scale, age and behaviour: when it grew, whether growth is organic or spiky, subscriber/follower history, and upload cadence. Useful for judging whether an account is real and active, and for corroborating that a handle belongs to a real, sustained persona rather than a throwaway.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://socialblade.com/ and pick the platform (YouTube, Twitch, Instagram, TikTok, X/Twitter), or use the top search.
2. Enter the `username`/channel handle and open its stats page.
3. Read: current follower/subscriber and view counts, daily/weekly/monthly growth, historical charts, estimated ranks, and (YouTube) an estimated creation window and upload frequency.
4. Compare the growth curve — smooth organic climb vs sudden vertical jumps (a bought-followers or viral signal).
5. Pivot: confirmed handle + activity pattern feeds username-enumeration tools and timezone inference from posting times.

## Inputs → Outputs
- **In:** `username` / `social-profile` on a supported platform
- **Out:** follower/subscriber history, growth rate, view totals, estimated ranks and creation-era `social-profile` metadata
- **Empty/negative result looks like:** "user not found" (handle never tracked or private), or a sparse/flat chart for a tiny account — small accounts often have thin history even when they exist.

## Gotchas & OpSec
- Human-in-the-loop: none for basic pages; deep history and CSV export prompt for login/paid plan.
- OpSec: **passive** — data comes from Social Blade's aggregation, so the target is never contacted.
- Figures are Social Blade's estimates; absolute follower counts are reliable, but growth projections and "grades" are heuristic and should not be cited as platform-official.
- Platform API changes (especially X/Twitter) can stale or freeze some feeds — check the "last updated" date on the page.

## Overlaps ("do both")
- Pairs with `[[socialblade]]` — same service, alternate index entry.
- Combine with a username-enumeration tool: Social Blade validates and dates a single known handle, while enumeration finds the same handle across other platforms.

## Trust & verifiability
`trust: community` — a reputable, long-running aggregator; raw counts are trustworthy, but treat growth estimates and rankings as its own computed metrics rather than authoritative platform data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-blade |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
