---
id: tgstat
name: TGStat
description: Use when you have a Telegram channel/`username` or keyword and want audience and activity analytics or to discover related channels — returns subscriber trends, post stats, rankings, and channel search.
url: https://tgstat.com/
category: messaging
path:
- messaging
- telegram
bestFor: Analysing a Telegram channel's audience/activity and discovering channels by keyword or category.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Public channel stats and search are free to browse; deeper analytics, mentions/keyword monitoring, and the API require an account and/or paid plan.
opsec: passive
opsecNote: Passive — TGStat reads its own index of public Telegram channels; a normal lookup never joins a channel or touches a target. Some features require an account (login is via Telegram, which ties activity to a Telegram identity) — use a sock-puppet Telegram account for those.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: TGStat is the best-known Telegram analytics service (Russian-origin, large index); data covers public channels only and its ranking/metrics are its own estimates.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- TGStat
- tgstat.com
tags:
- telegram
- analytics
- messaging-search
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# TGStat

> The largest Telegram analytics platform — search public channels by keyword/name and pull audience metrics, posting activity, mentions, and rankings for any public channel.

## When to use
You have a Telegram channel, a `username`, or a keyword and want to (a) profile a channel's reach, growth, and posting pattern, or (b) discover which public channels discuss a topic, person, or place. In investigations this maps the Telegram side of a subject's or a community's footprint: finding the channels tied to a handle, gauging a channel's real audience, and spotting where a name/keyword is mentioned.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tgstat.com/ (interface is available in English/Russian).
2. Search a channel `name`/`username`, or use category/keyword search to discover channels; keyword "mentions" search finds where a term appears.
3. Open a channel's page for subscriber trend, average post reach, posting frequency, and ranking.
4. For deeper analytics or mention-monitoring, log in (via a sock-puppet Telegram account) and/or a paid plan.
5. Pivot: discovered channels/admin handles feed username enumeration (`[[snoop]]`, `[[gaddr]]`); combine with `[[telegago]]` (Google-indexed) for content that TGStat's index misses.

## Inputs → Outputs
- **In:** channel `username`/`name` or keyword
- **Out:** subscriber/reach trends, post statistics, category rankings, related-channel and mention lists (`social-profile`/`username` leads)
- **Empty/negative result looks like:** no channel/mention matches — meaning it's not in TGStat's public index (private channels and many small/new ones are absent). Absence isn't proof it doesn't exist on Telegram.

## Gotchas & OpSec
- Covers PUBLIC channels only — private groups and one-to-one activity are invisible.
- Metrics (reach, "ER", rankings) are TGStat's own estimates, not official Telegram figures; treat as indicative.
- Some features gate behind a Telegram-based login — that ties usage to a Telegram account, so use a sock puppet.
- Russian-origin service; consider that in your OpSec/threat model.

## Overlaps ("do both")
- Pairs with `[[telegago]]` — TGStat gives channel analytics and native discovery; Telegago gives free Google-indexed content search. Use both for coverage.
- Feed admin/mention handles into `[[snoop]]`/`[[gaddr]]` and leak databases.

## Trust & verifiability
`trust: community` — the dominant Telegram-analytics service with a large index, but its metrics are estimates and it sees only public channels. Use it for discovery and scale-of-audience context; verify specific claims against the channel itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tgstat |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
