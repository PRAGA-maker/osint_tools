---
id: tgstat-ru
name: TGStat.ru
description: Use when you have a Telegram channel/`username`, `name` or keyword and want to find and analyze public Telegram channels and posts — returns matching channels and their `social-profile` analytics.
url: https://tgstat.ru
category: messaging
path:
- messaging
bestFor: Searching and analyzing public Telegram channels/groups and their posts, with especially deep coverage of Russian-language and post-Soviet channels.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Core catalog and channel search are free; detailed analytics and some metrics require the premium tier. Basic browsing needs no account.
opsec: active
opsecNote: A third-party Russian analytics service. Searching for a channel/keyword is a query to a foreign platform that may log it — use a sock-puppet browser/IP. Do NOT join or interact with channels through your real Telegram; TGStat only reads public data.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Widely used Telegram-analytics catalog (referenced in Bellingcat's toolkit); a large aggregator of public channel data, but a commercial third party, not an official Telegram source.
missingPersonsRelevance: medium
coverage:
- RU
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- telegram-analytics
aliases:
- Tgstat RU
- TGStat
tags:
- telegram
- analytics
- russia
source: osintambition-social
lastVerified: '2026-07-16'
enrichment: full
---

# TGStat.ru

> The largest public Telegram channel/group catalog and analytics engine — search 2.7M+ channels and tens of billions of posts, with unmatched depth on Russian-language channels.

## When to use
You have a Telegram `username` (channel/@handle), a `name`, or a keyword/phrase and want to (a) find the public channels or posts that match it, or (b) profile a known channel — its subscriber growth, reach, posting frequency and who cites it. Strongest when the subject or event sits in the Russian-speaking / post-Soviet Telegram sphere, but coverage is global.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tgstat.ru (English UI at https://tgstat.ru/en) in a sock-puppet browser.
2. To find channels: use the channel search with filters (country, language, category). To find posts/messages: use the post search with your keyword and date filters.
3. Open a channel's page to read its analytics (`social-profile`): subscriber count and growth rate, reach, citation index, posting cadence.
4. Read the output: matching channels/posts and, per channel, its public metrics. Deeper metrics prompt for the premium tier.
5. Pivot: take channel admins/usernames into other Telegram and cross-platform username lookups; use cited/mentioning channels to map a network.

## Inputs → Outputs
- **In:** `username` (channel/@handle), `name` or keyword
- **Out:** `social-profile` (matching channels and their subscriber/reach/citation analytics; matching public posts)
- **Empty/negative result looks like:** no channels/posts returned for the query — the channel may be private, deleted, or simply not indexed; absence here is not proof it doesn't exist.

## Gotchas & OpSec
- Public data only — private channels and DMs are invisible.
- Free browsing is generous but the site rate-limits heavy use and gates advanced analytics behind premium.
- OpSec: **active** — treat every search as logged by a foreign commercial service; use a throwaway browser/IP and never cross the streams with your real Telegram account.

## Overlaps ("do both")
- Pairs with `[[telegram-analytics]]` — run both; the two catalogs index overlapping-but-different sets of channels, so one often surfaces what the other misses.

## Trust & verifiability
`trust: community` — a large, widely-cited third-party aggregator (used in Bellingcat's toolkit). Metrics are derived from public channel data; corroborate specific figures against the channel itself where it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tgstat-ru |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (rate-limit) |
