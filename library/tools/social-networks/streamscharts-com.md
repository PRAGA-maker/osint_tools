---
id: streamscharts-com
name: streamscharts.com
description: Use when you have a Twitch/Kick streamer `username` and want their stable numeric user ID plus channel analytics — returns the ID and public streaming stats as a social-profile.
url: https://streamscharts.com/tools/convert-username
category: social-networks
path:
- social-networks
bestFor: Converting a Twitch username to its permanent numeric user ID and pulling public channel analytics.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: The username→ID converter and basic channel stats are free with no account; deeper historical analytics are paid.
opsec: passive
opsecNote: You query a third-party analytics site, not Twitch, so the streamer is not notified. StreamsCharts logs your queries/IP; use a sock-puppet browser. Only public streaming data is exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established Twitch/Kick analytics platform. Data is derived from public streaming activity; figures are third-party estimates, generally reliable for IDs and broad stats.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- twitch-username-and-user-id-addons-mozilla-org
- twitch-followage-tool
aliases:
- StreamsCharts
- streamscharts convert username
tags:
- twitch
- Twitch Related Sites
- kick
- streaming-analytics
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# streamscharts.com

> A Twitch/Kick analytics site whose username→ID converter yields a streamer's permanent numeric ID, plus public channel stats.

## When to use
You have a Twitch (or Kick) `username` and want (a) the account's **numeric user ID** — the durable identifier that survives username changes, so you can re-find a renamed channel — and/or (b) public analytics: when they stream, viewership trends, games/categories, and recent activity. Good for confirming an account is active, spotting rename history, and building a behavioural picture of a streaming subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://streamscharts.com/tools/convert-username in a sock-puppet browser.
2. Enter the Twitch username to get its numeric user ID (and vice versa).
3. Visit the channel's StreamsCharts page for public stats — stream schedule, average/peak viewers, categories, recent streams.
4. Pivot: the numeric ID lets you track the account across renames and query Twitch tooling like `[[twitch-username-and-user-id-addons-mozilla-org]]`; activity times/games are lifestyle-pattern leads.

## Inputs → Outputs
- **In:** `username` (Twitch/Kick handle)
- **Out:** `social-profile` — numeric user ID + public channel analytics (schedule, viewership, categories)
- **Empty/negative result looks like:** "user not found" — the handle is misspelled, never streamed, or is too new/small to be indexed; absence of analytics isn't proof the account doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — the streamer isn't alerted; the analytics site sees your query, so sock-puppet it.
- Analytics are third-party estimates; the numeric ID is exact, but viewership figures are approximations.

## Overlaps ("do both")
- Pairs with `[[twitch-username-and-user-id-addons-mozilla-org]]` — both resolve usernames↔IDs; StreamsCharts adds the analytics/history layer for behavioural profiling.

## Trust & verifiability
`trust: community` — a reputable independent analytics platform built on public streaming data. Treat the numeric ID as authoritative and viewership stats as estimates.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | streamscharts-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
