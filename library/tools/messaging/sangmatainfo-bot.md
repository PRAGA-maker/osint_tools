---
id: sangmatainfo-bot
name: SangMataInfo_bot
description: Use when you have a Telegram user (via a forwarded message or numeric ID) and want their history of past display names and usernames — returns name and username history.
url: https://t.me/SangMataInfo_bot
category: messaging
path:
- messaging
bestFor: Revealing a Telegram account's previous display names and usernames — exposing rebrands, aliases and identity changes.
selectorsIn:
- username
selectorsOut:
- name
- username
status: live
pricing: freemium
costNote: Free to query by an account's numeric ID or by forwarding one of their messages; querying directly by @username is a premium feature. You need a Telegram account to use the bot.
opsec: active
opsecNote: You interact with a third-party Telegram bot and hand it the target's message/ID, so the bot operator sees who you're researching and your Telegram account is the one asking. Use a sock-puppet Telegram account (burner number), and remember the bot only knows changes it witnessed in groups it shares with the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, widely used Telegram name-history bot (SangMata family); effective but community-operated and opaque about data handling, so treat its history as observed-changes, not a complete record.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- SangMata
- SangMataInfo
- SangMata_bot
tags:
- telegram
- name-history
- alias-tracking
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# SangMataInfo_bot

> A Telegram bot that has sat in millions of public groups logging every name/username change it sees — forward it a message and it tells you what that account used to be called.

## When to use
You have a Telegram account of interest and want its identity history: the display names and `username`s it used before its current one. This exposes rebrands, aliases and attempts to shed a reputation — invaluable when a subject changed their handle to evade recognition, or when you need to link a "new" account to an older known one. Start from a forwarded message from the target or their numeric ID.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a sock-puppet Telegram account, open the bot at https://t.me/SangMataInfo_bot and start it.
2. Forward a message originally sent by the target account to the bot (or, in a shared group, reply to their message with `/check_name` or `/check_username`).
3. The bot returns the account's logged history of prior display names and usernames, with the numeric user ID.
4. Note the old `name`s/`username`s and the stable numeric ID (the ID persists across renames).
5. Pivot: old usernames feed cross-platform username search and archive lookups; the numeric ID links the account across renames and other Telegram-intel bots.

## Inputs → Outputs
- **In:** a forwarded message from the target, or their Telegram numeric ID (premium: `@username`)
- **Out:** `name` (past display names), `username` (past @handles), plus the persistent numeric user ID
- **Empty/negative result looks like:** "no records" or only the current name — the bot can only report changes it *witnessed* in shared groups; a quiet or newly-seen account will have little/no history, which is not proof it never changed.

## Gotchas & OpSec
- **Observed-only:** Telegram has no username-history API, so SangMata only knows changes seen in groups it was in — coverage is incomplete.
- Free lookup needs a forwarded message or numeric ID; `@username` lookup is premium.
- **Active:** you reveal your research to the bot operator — use a burner Telegram account.

## Overlaps ("do both")
- Pairs with `[[telemetr-io]]` and other Telegram-intel bots — SangMata gives identity/alias history, while channel-analytics tools map the account's public activity; together they build a fuller Telegram picture.

## Trust & verifiability
`trust: community` — an effective, popular bot, but community-run and observation-limited; treat the returned history as real-but-partial and corroborate aliases via other sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sangmatainfo-bot |
| category | messaging |
| selectorsIn → selectorsOut | username → name, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
