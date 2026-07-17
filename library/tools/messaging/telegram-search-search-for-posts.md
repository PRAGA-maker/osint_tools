---
id: telegram-search-search-for-posts
name: Telegram Search. Search for posts
description: Use when you have a `name`, `username`, or keyword and want to find Telegram channels/posts mentioning it — returns matching public channels and messages via TGStat.
url: https://tgstat.com/search
category: messaging
path:
- messaging
bestFor: Keyword-searching public Telegram channels and posts (which Telegram's own app searches poorly) via the TGStat analytics index.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- geolocation
- associate
status: live
pricing: freemium
costNote: Free search with limits; TGStat's deeper analytics, filters, and exports are gated behind paid plans.
opsec: passive
opsecNote: Searches TGStat's index of public channels, not the target's account — channel admins/members aren't notified you searched. Passive. No login for basic search; use a clean browser and don't join/interact with a channel from an identifiable account.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: TGStat is a well-known third-party Telegram analytics service indexing public channels; coverage is broad but it's not affiliated with Telegram and doesn't see private chats.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- tgstat
- telegago
- telemetr-io
aliases:
- TGStat search
- Telegram post search
tags:
- telegram
- messaging
- channel-search
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Telegram Search. Search for posts

> TGStat's public-channel search — find Telegram channels and posts by keyword, filling the gap left by Telegram's weak native search.

## When to use
You want to find Telegram activity mentioning a subject — a `name`, `username`, phone, place, or event — across public channels. Telegram's in-app search is limited to channels you already know, so an external index like TGStat is how you discover *which* public channels/posts reference your term. Useful for finding a subject's own channel, mentions of them, or local/community channels tied to a location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://tgstat.com/search.
2. Enter keywords (name, handle, phone, place) — search posts and/or channels; apply language/category filters where available.
3. Review matching channels and posts; open a channel to read its public content and metadata (subscribers, post history).
4. Free tier caps results/queries — refine terms rather than paging endlessly.
5. Pivot: a subject's channel/handle → `[[tgstat]]` for deeper channel analytics; mentioned places/people → geolocation and associate mapping; cross-check with `[[telegago]]` (a Google-CSE Telegram search) since indexes differ.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** matching public channels and posts → `social-profile`, plus `geolocation`/`associate` leads from content
- **Empty/negative result looks like:** no results — the term isn't in public channels TGStat indexes, it's in private/group chats (invisible to any external tool), or free-tier caps hid it; cross-check another Telegram search.

## Gotchas & OpSec
- Only **public** channels are indexed — private groups, DMs, and secret chats are invisible; absence here says nothing about private activity.
- Freemium caps free results; treat a sparse free-tier result as incomplete.
- Don't join or message a channel from an identifiable account while investigating — that's active and traceable.

## Overlaps ("do both")
- Pairs with `[[tgstat]]` — same provider; use search to find a channel, then TGStat's analytics for its stats/history.
- Pairs with `[[telegago]]` — a Google Custom Search over Telegram; different coverage, so run both to maximize hits.

## Trust & verifiability
`trust: community` — a reputable but third-party analytics index. Any post/channel it returns is verifiable by opening it directly in Telegram; coverage is broad but not exhaustive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-search-search-for-posts |
| category | messaging |
| selectorsIn → selectorsOut | name, username → social-profile, geolocation, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
