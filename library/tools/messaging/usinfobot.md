---
id: usinfobot
name: UsInfoBot (Telegram user-info)
description: Use when you have a Telegram `username` or a forwarded message and want the account's stable numeric Telegram ID, display name and profile picture — an inline Telegram lookup bot.
url: https://t.me/usinfobot
category: messaging
path:
- messaging
bestFor: Resolving a Telegram username (or forwarded message) to the account's persistent numeric ID, current name and profile photo.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free Telegram bot; you only need a Telegram account to use it.
opsec: passive
opsecNote: You query a bot, not the target — resolving a username to an ID does not notify that user. Do it from a sock-puppet Telegram account as hygiene. NOTE This is the benign Telegram user-info bot; do NOT confuse it with criminal "US info"/SSN-lookup Telegram services that resell stolen data-broker access — those are illegal and out of scope.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A widely-used, benign Telegram utility that surfaces only Telegram's own public account metadata; it does not access private data.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- usinfobot
- Inline Info Username
tags:
- telegram
- user-info
- id-lookup
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# UsInfoBot (Telegram user-info)

> An inline Telegram bot that turns a username (or a forwarded message) into the account's stable numeric ID, name and profile photo — the anchor for durable Telegram investigation.

## When to use
You have a Telegram `username` (or a message forwarded from someone) and want the account's persistent numeric Telegram ID plus current display name and profile picture. The numeric ID is the OSINT prize: usernames and display names change freely, but the ID stays constant, so it lets you track an account across renames and confirm that two handles are the same account. It exposes only Telegram's own public metadata — nothing private.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://t.me/usinfobot in Telegram (web/desktop/mobile) with a sock-puppet account.
2. Send (or inline-query `@usinfobot`) the target `username`, or forward a message from the account you want to identify.
3. Read the returned info: numeric Telegram `social-profile`/ID, current display `name`, and profile `image`.
4. Record the numeric ID as your durable anchor; re-query later to detect username/name changes on the same ID.
5. Pivot: the numeric ID feeds group-membership bots like `[[getchatlist]]`; the profile photo feeds reverse-image/face search; the username feeds cross-platform username search.

## Inputs → Outputs
- **In:** Telegram `username` or a forwarded message
- **Out:** numeric Telegram ID (`social-profile`), display `name`, profile `image`
- **Empty/negative result looks like:** the bot can't resolve the username (never existed, deleted, or privacy-restricted) — meaning no public metadata, not proof the person has no Telegram.

## Gotchas & OpSec
- Human-in-the-loop: needs a Telegram account to message the bot; use a sock puppet.
- Scope: it returns only public Telegram account metadata — no phone, no messages, nothing private. Do not expect (or seek) that here.
- Disambiguation: the name "US info" is misleading — this is a Telegram-account utility, not a US person/SSN lookup. Steer clear of criminal SSN-lookup bots with similar names.

## Overlaps ("do both")
- Pairs with `[[getchatlist]]` — this gives you the stable numeric ID, which that bot uses to map the account's groups and associates.

## Trust & verifiability
`trust: community` — a benign, widely-used Telegram utility exposing only first-party public account metadata, so the ID/name/photo it returns are directly checkable in Telegram itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usinfobot |
| category | messaging |
| selectorsIn → selectorsOut | username, social-profile → social-profile, name, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
