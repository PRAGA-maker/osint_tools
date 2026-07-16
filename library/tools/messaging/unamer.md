---
id: unamer
name: Unamer (Telegram bot)
description: Use when you have a Telegram `username`, `phone`, ID, or forwarded message and want the account's username history and probable registration date — returns social-profile linkage and past usernames.
url: https://telegram.me/unamer_bot
category: messaging
path:
- messaging
bestFor: Resolving a Telegram account's username history (owners of a handle since 2017) and probable registration date from a username, phone, ID, contact, or forwarded message.
selectorsIn:
- username
- phone
- device-id
selectorsOut:
- social-profile
- username
- name
status: live
pricing: freemium
costNote: A few free lookups on entry ('Admit One' tickets); further queries use a fair pay-per-search balance, and you are not charged when nothing is found.
opsec: active
opsecNote: You interact with the bot from a Telegram account, so use a dedicated sock-puppet account and burner number — the bot (and its operator) sees which account is querying and what you search. Querying does not notify the target, but you are trusting an unknown third-party bot with the selectors you submit.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: chrome-mcp
trust: community
trustNote: A well-known Telegram OSINT bot cited across multiple Telegram-OSINT resource lists; data is aggregated from Telegram's public metadata and historical scrapes, so treat historical usernames as strong leads to verify.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- telegram-creation-date-bot
- usersbox
- avtogram-bot
- datxpert
- discord-sensor
- getchatlist
- getsendgifts
- instabot
- leak-osint
- oksearch
- pimeyes
- searchforchats
- spyggbot
aliases:
- unamer_bot
- Unamer bot
tags:
- telegram
- username-history
- account-age
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Unamer (Telegram bot)

> A Telegram-native lookup bot: give it a handle, number, ID, contact, or forwarded message and it returns who has owned that username since 2017 and the account's probable registration date.

## When to use
You have a Telegram identifier for a subject — a `@username`, `phone`, numeric Telegram ID, a shared contact, or a forwarded message — and you want to (a) see the username history (usernames are recycled, so today's owner may not be the historical one) and (b) estimate when the account was created. This is core Telegram tradecraft for confirming whether a handle you found is the same account over time.

## How to use it (`bestInteractionPattern`: chrome-mcp)
1. From a sock-puppet Telegram account (burner number), open https://telegram.me/unamer_bot and start the bot.
2. Send one of: a `@username`, a `phone` number, a Telegram ID, a shared contact, or a forwarded message from the target.
3. Read the response: past owners of the username (history since 2017), the current linkage, and a probable registration/creation date.
4. Note that free 'Admit One' tickets cover initial tests; beyond that a query consumes balance, but only when the bot actually returns data.
5. Pivot: the registration date corroborates account age; historical usernames feed cross-platform `username` searches; a resolved account feeds broader Telegram tooling (see `[[osintme-com]]`).

## Inputs → Outputs
- **In:** `username`, `phone`, Telegram ID (`device-id`), a contact, or a forwarded message.
- **Out:** username history (past + present owners), probable registration date, and current `social-profile`/`name` linkage.
- **Empty/negative result looks like:** "no information found" — the account may be too new, privacy-locked, or absent from the bot's dataset; you are not charged for empty results, and empty is not proof the account doesn't exist.

## Gotchas & OpSec
- You must operate from a Telegram account — always a sock puppet with a burner number, never your real account; the bot operator sees your queries.
- Data provenance is aggregation/scraping of Telegram metadata; historical usernames and dates are strong leads but should be corroborated (e.g. with a second creation-date bot).
- Recycled usernames are the whole point — do not assume the current holder of a handle is the person your older evidence referenced; use the history to check.

## Overlaps ("do both")
- Pairs with `[[telegram-creation-date-bot]]` and `[[usersbox]]` — cross-check the registration date and username history against a second bot, since single-source Telegram bots vary in coverage and accuracy.

## Trust & verifiability
`trust: community` — a widely-referenced Telegram OSINT bot, but of non-transparent data sourcing. Use its username history and dates as investigative leads and verify critical facts with an independent bot or Telegram's own metadata.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unamer |
| category | messaging |
| selectorsIn → selectorsOut | username, phone → social-profile, username, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | chrome-mcp |
| opsec | active |
| human-in-loop | yes |
