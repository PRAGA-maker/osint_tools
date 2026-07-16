---
id: turibot
name: TuriBot
description: Use when you have a Telegram numeric user ID and want the current @username / account behind it (or vice-versa) — returns username and social-profile.
url: https://t.me/TuriBot
category: messaging
path:
- messaging
bestFor: Resolving a Telegram numeric user ID to its current @username and account.
selectorsIn:
- social-profile
selectorsOut:
- username
status: degraded
pricing: freemium
costNote: Free Telegram bot for basic ID/username resolution; some Telegram lookup bots gate extended features behind credits. Bot availability is volatile.
opsec: active
opsecNote: You must message the bot from a Telegram account, which reveals your querying account to the bot operator. The target is not notified by a plain ID→username resolution, but do it from a burner Telegram identity on a research device rather than a personal account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A community-listed Telegram OSINT bot; note an unrelated PHP library also uses the name "TuriBot". Confirm you are interacting with the lookup bot and treat resolutions as leads, since usernames change and IDs can be re-pointed.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- TuriBot Telegram
- Telegram ID to username bot
tags:
- telegram
- username-lookup
- account-resolution
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# TuriBot

> A Telegram bot that maps a numeric Telegram user ID to the account's current @username (and back), for attributing anonymous-looking IDs.

## When to use
You have a Telegram numeric user ID — pulled from an export, a forwarded message, another OSINT tool, or a group member list — and need the human-readable @username or account behind it. Telegram hides usernames in many contexts while the stable numeric ID persists, so resolving ID→username lets you tie an otherwise anonymous participant to a searchable handle you can then pivot on. Also useful to confirm a username currently maps to the ID you expect.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a **burner** Telegram account on a research device, open https://t.me/TuriBot and press Start.
2. Send the Telegram numeric user ID (or username) per the bot's prompt.
3. Read the response: the resolved @username / account details, or a "not found" if the ID is invalid or the account is deleted.
4. Pivot: feed a resolved username into username-search and Telegram-profile tools to expand the account's footprint.

## Inputs → Outputs
- **In:** `social-profile` (a Telegram numeric user ID or account reference)
- **Out:** `username` (the current @handle) and associated account details
- **Empty/negative result looks like:** "not found" / no result — the ID may be invalid, the account deleted, or the user has no public username; that is not proof the account never existed.

## Gotchas & OpSec
- Human-in-the-loop: requires a Telegram account to message the bot (account-login).
- OpSec: active — the bot operator sees your querying account. Use a research persona, never a personal Telegram.
- Usernames are mutable and can be dropped/re-registered; treat a resolution as a point-in-time snapshot, not a permanent identity.
- Don't confuse this with the unrelated "TuriBot" PHP Telegram-API library — same name, different thing.

## Overlaps ("do both")
- Pairs with Telegram group/channel and username tools such as `[[getchatlist]]` and `[[searchforchats]]` — those find where an account is active, this attributes an ID to a handle you can search.

## Trust & verifiability
`trust: unverified` — a community-listed bot with no accountability for accuracy or uptime. Cross-check a resolved username directly in Telegram before relying on the attribution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | turibot |
| category | messaging |
| selectorsIn → selectorsOut | social-profile → username |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
