---
id: sangmata-beta
name: SangMata (beta)
description: Use when you have a Telegram user (a `username` or forwarded message) and want their history of past names and usernames — returns prior `name`/`username` aliases.
url: https://t.me/SangMata_beta_bot
category: messaging
path:
- messaging
bestFor: Revealing a Telegram account's past display names and usernames (alias history) via a logging bot.
selectorsIn:
- username
selectorsOut:
- name
- username
status: live
pricing: free
costNote: Free to query by an account's numeric ID or by forwarding one of their messages; no payment. Requires a Telegram account.
opsec: passive
opsecNote: Passive to the target — SangMata reports from its own historical log; the subject is not notified when you query. But you must operate from a Telegram account (use a sock-puppet), and forwarding a target's message to the bot means you already had access to it. The bot operator sees what you query.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A widely-used community Telegram OSINT bot that has logged name/username changes across public groups for years; coverage depends on the account having been seen in groups the bot inhabits.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SangMata
- SangMata_bot
- SangMataInfo_bot
tags:
- telegram
- alias-history
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# SangMata (beta)

> A Telegram bot that has silently logged members' name and username changes across millions of public groups — query it to reveal an account's alias history.

## When to use
You have a Telegram user (identified by numeric ID, `username`, or a message you can forward) and want their **history of past display names and usernames**. Because Telegram's numeric ID is permanent while names/handles change, alias history is a powerful identity pivot — it can reveal a real name someone later hid, a previous handle reused elsewhere, or a pattern of identity changes in a missing-persons or fraud investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a sock-puppet Telegram account, open the SangMata bot — the main bots are @SangMata_bot / @SangMataInfo_bot (the beta bot at the listed URL is one of the family).
2. Query it: forward a message from the target user to the bot, or send the account's numeric ID.
3. The bot returns the logged history of past `name`s and `username`s for that account (if it has ever seen the account in a group it inhabits).
4. Note prior handles/names as pivots.
5. Pivot: an old `username` feeds `[[sherlock]]`/`[[namechk]]` cross-platform; a revealed real `name` feeds people-search.

## Inputs → Outputs
- **In:** a Telegram account's numeric ID, `username`, or a forwarded message
- **Out:** historical list of past display `name`s and `username`s
- **Empty/negative result looks like:** "no data" — the account was never seen in a group the bot monitors, or has never changed its name/handle. Absence of history isn't proof the account is new.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** — you need a Telegram account; use a puppet.
- OpSec: **passive** to the target (log-based, no notification), but the bot operator sees your queries; forwarding implies you had access to the message.
- Coverage is limited to accounts the bot has encountered in shared/public groups; bot handles in the SangMata family change over time — pick a currently-live one.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`/`[[namechk]]` (reuse of a revealed handle) and `[[osint-github-com]]` (messaging attack-surface) — SangMata surfaces the alias history; the others spread those aliases across platforms.

## Trust & verifiability
`trust: community` — a popular, long-running community bot. Its logs are a strong lead to a person's alias history, but confirm any revealed real name/handle against an independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sangmata-beta |
| category | messaging |
| selectorsIn → selectorsOut | username → name, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
