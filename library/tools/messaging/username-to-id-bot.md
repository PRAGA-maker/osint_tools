---
id: username-to-id-bot
name: username_to_id_bot (Telegram)
description: Use when you have a Telegram `username` (or forwarded message) and want the stable numeric user/group/channel ID behind it — returns a device-id-style Telegram numeric ID for tracking across handle changes.
url: https://t.me/username_to_id_bot
category: messaging
path:
- messaging
bestFor: Resolving a Telegram @username to its permanent numeric ID (and the reverse for groups/channels).
selectorsIn:
- username
- social-profile
selectorsOut:
- device-id
- username
status: live
pricing: free
costNote: Free Telegram bot; no payment. Requires a Telegram account to message the bot.
opsec: active
opsecNote: You must query the bot from a Telegram account, so use a sock-puppet account — not your real one. The bot operator can see who queries it and which usernames you look up. The target is not notified when you resolve their ID, but forwarding one of their messages to the bot reveals metadata to a third party you don't control.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: chrome-mcp
trust: community
trustNote: A popular community Telegram utility bot widely cited in OSINT lists; it works reliably but is operated by an unknown third party, so treat it as untrusted infrastructure for anything sensitive.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- username_to_id_bot
- Telegram username to ID
tags:
- telegram
- id-resolver
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# username_to_id_bot (Telegram)

> A Telegram bot that turns a @username into the account's permanent numeric ID — the identifier that survives handle changes and lets you track a target even after they rename.

## When to use
You have a Telegram `username` and want the underlying numeric user ID, because usernames can be changed or dropped but the numeric ID is permanent. Essential for durable tracking: if you only record `@handle`, you lose the subject when they rename; the numeric ID is your anchor. Also resolves group/channel IDs.

## How to use it (`bestInteractionPattern`: chrome-mcp)
1. From a **sock-puppet** Telegram account, open https://t.me/username_to_id_bot and start the bot.
2. Send the target `@username` (without needing them to be a contact) — the bot replies with the numeric user ID.
3. For a group/channel, send its @username or forward a message from it; the bot returns the corresponding ID.
4. Record the numeric ID alongside the handle in your case notes.
5. Pivot: the numeric ID feeds Telegram intelligence tools that key off IDs (membership/history search bots), and lets you detect when a renamed account is the same person.

## Inputs → Outputs
- **In:** Telegram `username`/handle or a forwarded message
- **Out:** the permanent numeric Telegram ID (a `device-id`-style stable account identifier), plus confirmation of the current `username`
- **Empty/negative result looks like:** the bot reports it can't find the username (never existed, was deleted, or is not resolvable) — a non-result, not proof the person left Telegram.

## Gotchas & OpSec
- Human-in-the-loop: you need a Telegram account to talk to the bot — use a research account.
- OpSec: **active.** The bot's operator sees your queries and can log which usernames you resolve. Forwarding a target's message to the bot hands their message metadata to an unknown third party — prefer sending just the @username.
- Third-party bot: don't feed it anything sensitive; it is convenient infrastructure you do not control.

## Overlaps ("do both")
- Pairs with `[[telegram-finder-telegram-finder-io]]` and other Telegram-ID-keyed search tools — this bot gets you the stable ID those tools need to search history and group membership.

## Trust & verifiability
`trust: community` — a widely used, reliable utility bot, but operated anonymously. The numeric ID it returns is verifiable (it's Telegram's own identifier) even though the operator is not vetted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | username-to-id-bot |
| category | messaging |
| selectorsIn → selectorsOut | username, social-profile → device-id, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | chrome-mcp |
| opsec | active |
| human-in-loop | yes (account-login) |
