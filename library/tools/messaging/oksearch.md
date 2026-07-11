---
id: oksearch
name: OkSearch (Telegram bot)
description: Use when you have a `name`/`username`/keyword and want to find Telegram channels, groups, and posts mentioning it — returns social-profile leads (Telegram channels/groups).
url: https://telegram.me/OkSearchBot
category: messaging
path:
- messaging
bestFor: Discovering which Telegram channels/groups a person, handle, or topic appears in.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: The channel/content search described is free to use inside Telegram. Some Telegram OSINT bots gate deeper lookups behind payment; only the keyword/channel search is confirmed here.
opsec: active
opsecNote: You query it from inside your own Telegram account, so the bot operator (an unknown third party) sees your search terms and your account. Use a dedicated sock-puppet Telegram account with a burner number, never your real one, and assume every query is logged.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party Telegram bot with a sizeable user base; confirmed as a channel/group/content search assistant. Any capability beyond keyword/channel discovery is unverified — don't assume phone/breach lookups.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- OkSearchBot
tags:
- telegram
- channel-search
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# OkSearch (Telegram bot)

> A Telegram search assistant bot: give it a keyword, name, or handle and it surfaces channels, groups, and content across Telegram.

## When to use
You're working a subject who may be active on Telegram and you want to find *where* — which channels they run or post in, which groups discuss them, or where a handle/topic shows up. Telegram's built-in search is weak across public channels, so a discovery bot fills that gap and turns a `name`/`username` into `social-profile` leads to investigate.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a **sock-puppet** Telegram account (web.telegram.org, Desktop, or mobile), open the bot at https://telegram.me/OkSearchBot and press Start.
2. Send your search term — a `username`, `name`, or topic keyword.
3. Read the returned channel/group/content matches.
4. Pivot: open each returned channel/group, verify it's your subject, and pull member lists / pinned posts / linked accounts from there.

## Inputs → Outputs
- **In:** `username`, `name`, or keyword
- **Out:** `social-profile` links — matching Telegram channels/groups and content references
- **Empty/negative result looks like:** "no results" or generic/unrelated channels — the term isn't indexed or the subject isn't publicly on Telegram under that spelling; try handle variants.

## Gotchas & OpSec
- Human-in-the-loop: you must have a Telegram account to message the bot (account-login).
- OpSec: **active** — the bot's operator sees your queries and account. Sock-puppet account + burner number only; never search from an account tied to you.
- Scope: treat it as a *discovery* aid. Its results are index-quality, not authoritative; confirm any hit by opening the actual channel.

## Overlaps ("do both")
- Pairs with other Telegram-oriented lookups in the messaging category — a discovery bot like this finds the channels, while dedicated Telegram analysis tools enumerate members and history once you know where to look.

## Trust & verifiability
`trust: community` — a popular but third-party Telegram bot. The channel/content search is confirmed; anything more (personal-data lookups) is unverified, so don't rely on it for that and don't feed it sensitive queries from a real account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oksearch |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
