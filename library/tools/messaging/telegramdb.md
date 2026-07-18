---
id: telegramdb
name: TelegramDB
description: Use when you have a Telegram `username`, keyword, or group name and want to explore public Telegram — returns matching `social-profile` groups/channels and, via its bot, a user's public group footprint.
url: https://www.telegramdb.org/
category: messaging
path:
- messaging
bestFor: Searching an index of public Telegram groups/channels and mapping which public groups a user appears in via its bot.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free tier via the website and Telegram bot with limited queries; heavier use / deeper lookups require a paid plan.
opsec: passive
opsecNote: You query TelegramDB's own index (and its bot), not the target directly, so the person is not notified and you never join their groups. The bot requires a Telegram account — use a sock-puppet Telegram identity, never your real one, since interacting with the bot ties activity to that account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party Telegram indexing service listed in Bellingcat's toolkit; coverage of public groups is partial and membership data can be stale, so treat results as leads to confirm in Telegram.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- telegramdb-org
aliases:
- telegramdb.org
- TGDB
tags:
- bellingcat-toolkit
- telegram
- group-search
source: bellingcat-toolkit
lastVerified: '2026-07-18'
enrichment: full
---

# TelegramDB

> A searchable index of public Telegram groups and channels, with a bot that maps which public groups a given user has appeared in.

## When to use
You have a Telegram `username`, a person's `name`, or a topic/keyword and want to find related public Telegram groups and channels — or you want to see the public-group footprint of a specific user. Useful for discovering a subject's Telegram communities, tracing a handle across groups, or finding channels around a topic without manually browsing Telegram.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.telegramdb.org/ (and/or start its Telegram bot from a sock-puppet Telegram account).
2. Search a `username`, `name`, or keyword to find matching public groups/channels.
3. For a user footprint, query the bot with the username/ID — it returns public groups where that user has been indexed.
4. Read the results: group/channel names, member counts, and links (`social-profile`).
5. Pivot: a discovered group feeds Telegram-native monitoring and [[telemetry]]-style message search; a confirmed handle feeds username OSINT.

## Inputs → Outputs
- **In:** `username`, `name`, or keyword
- **Out:** `social-profile` (public Telegram groups/channels), `username`, and a user's indexed public-group memberships
- **Empty/negative result looks like:** no matching groups or an empty footprint — TelegramDB only sees what it has indexed, so absence means "not in the index," not that the user has no Telegram presence.

## Gotchas & OpSec
- Human-in-the-loop: the bot needs a Telegram account — use a dedicated sock puppet; free queries are rate-limited.
- Coverage is partial and can lag — group memberships are historical/indexed snapshots, not live truth.
- Confirm any membership or channel claim inside Telegram before relying on it.

## Overlaps ("do both")
- Pairs with [[telemetry]] and other Telegram tooling — TelegramDB maps groups and user footprints, while message-search tools surface the actual content within those groups.

## Trust & verifiability
`trust: community` — a third-party indexer in Bellingcat's toolkit. Solid for discovery; verify specific memberships and channel details against live Telegram, since indexed data can be stale.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegramdb |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
