---
id: socialbearing
name: Socialbearing
description: Use when you have an X/Twitter `username` and want analytics on their tweets — timeline stats, top tweets, engagement, and posting patterns that build a `social-profile` and activity timeline.
url: https://socialbearing.com/
category: social-networks
path:
- social-networks
bestFor: Analysing a Twitter account's tweet history, engagement, and posting-time patterns at a glance.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: freemium
costNote: Historically free for basic tweet/timeline analytics; heavier use behind account/limits.
opsec: passive
opsecNote: You query the analytics tool, not the target; the subject is not notified. It depends on Twitter/X API access, which is now heavily restricted and paywalled — expect failures.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known third-party Twitter analytics site; reliable historically, but its function hinges on the X API, which has been locked down since 2023 — verify it returns data before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- socialbearing.com
- social bearing
tags:
- twitter
- x
- analytics
- social-media
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Socialbearing

> A Twitter/X analytics dashboard — profile a subject's account by tweet history, engagement, and posting patterns, when the X API cooperates.

## When to use
You have an X/Twitter `username` and want structured analytics rather than a raw scroll: total/average engagement, top and recent tweets, most-used hashtags/mentions, and — valuably for pattern-of-life — *when* the account tends to post (hour/day heatmaps that hint at time zone and routine). Mark it `degraded`: since the 2023 X API lockdown many such tools return partial or no data, so confirm it works for your target before depending on it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://socialbearing.com/ and enter the target `username` (Twitter timeline analysis).
2. Review the dashboards: tweet volume over time, engagement, top tweets, hashtags/mentions, posting-time patterns.
3. Note the posting-hour distribution → likely time zone/routine; frequent mentions → candidate `associate`s.
4. If it returns nothing, fall back to direct X search or another analytics tool (likely an API limitation).
5. Pivot: mentioned handles → their profiles/cross-platform checks; posting patterns → timeline/geolocation reasoning.

## Inputs → Outputs
- **In:** `username` (Twitter/X account)
- **Out:** `social-profile` analytics — engagement, top tweets, hashtags/mentions, posting-time patterns
- **Empty/negative result looks like:** an error or blank dashboard — most often an API-access failure now, not proof the account is empty.

## Gotchas & OpSec
- API-dependent and often degraded post-2023 X changes; verify before citing.
- Reflects only accessible/recent tweets — not necessarily the full history.
- Mentioned users and inferred time zones are leads to corroborate, not facts.

## Overlaps ("do both")
- Pairs with `[[tweet-topic-explorer]]` (topics/associates) and direct X advanced search (exact quotes/dates) — Socialbearing adds the quantitative/temporal view.

## Trust & verifiability
`trust: community` — a reputable third-party analytics tool pulling from the X API; data is genuine when it loads, but confirm it's currently functional and treat inferences as leads.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socialbearing |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
