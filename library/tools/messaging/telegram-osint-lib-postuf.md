---
id: telegram-osint-lib-postuf
name: Telegram-osint-lib (Postuf)
description: Use when you have a `phone` or `username` and want to enrich it against Telegram programmatically — a PHP library that checks presence, resolves phone→account, and scrapes channel/member data.
url: https://github.com/Postuf/telegram-osint-lib
category: messaging
path:
- messaging
bestFor: Scripted Telegram OSINT — phone-to-account resolution, online-status monitoring, and bulk channel/member/photo collection via the MTProto API.
selectorsIn:
- phone
- username
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free, open-source (GitHub); self-hosted. Requires PHP 7.4+ and your own Telegram API credentials.
opsec: active
opsecNote: ACTIVE — it authenticates a Telegram account and interacts with Telegram's servers to resolve numbers, watch presence, and scrape. Adding a phone to contacts / checking presence can be inferred by Telegram and, in some flows, seen by the target. Use a dedicated research account with a burner number, and never your own; mass activity risks bans.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Actively maintained PHP library by Postuf (~300+ stars, releases through 2023); powerful but unaudited and easy to misuse — review before running. Note the description's "Python" label is wrong; it is PHP.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: true
registration: false
relatedTools:
- telegram-group-joiner
aliases:
- Postuf telegram-osint-lib
tags:
- telegram
- osint
- library
- php
source: osintambition-social
lastVerified: '2026-07-19'
enrichment: full
---

# Telegram-osint-lib (Postuf)

> A PHP library that scripts Telegram OSINT: resolve a phone to an account, watch when a user is online, and drain channel members/photos/history.

## When to use
You have a `phone` number or `username` and want to programmatically ask Telegram what's behind it — does the number map to a Telegram account, when is that account online (a routine/timezone signal), and what channels/members/photos can be pulled. Use it when a single manual check isn't enough and you need automation or monitoring.

## How to use it (`bestInteractionPattern`: cli)
1. Install PHP 7.4+ and clone the repo; install deps (Composer). Docker support is included.
2. Obtain Telegram API credentials (`api_id`/`api_hash`) at my.telegram.org using a dedicated research account (burner number), and authorise it.
3. Use the example scripts/scenarios: resolve a contact by phone, subscribe to presence updates, parse a group's members, or download channel photos.
4. Read the output: account existence, profile fields (`name`, `image`), online-status timeline, member lists. Pivot: feed resolved usernames/photos into face and social tools.

## Inputs → Outputs
- **In:** `phone` or `username`
- **Out:** Telegram `social-profile` (account existence, `name`, bio, `image`), presence timeline, group member lists
- **Empty/negative result looks like:** a phone that resolves to no account (not on Telegram, or privacy settings hide it), or presence hidden by "last seen" privacy — absence isn't proof the person lacks Telegram.

## Gotchas & OpSec
- **Active and account-risky:** presence checks and contact-adds can be surfaced to Telegram/the target; 2FA accounts aren't supported by the lib. Use throwaway research accounts only.
- Unaudited third-party code with broad API power — read it before running against real targets.
- Human-in-the-loop: full account login/authorisation.

## Overlaps ("do both")
- Pairs with `[[telegram-group-joiner]]` — that gets a research account into groups; this scrapes/monitors them and resolves numbers programmatically.

## Trust & verifiability
`trust: community` — popular maintained library, but powerful and unaudited; verify any resolved identity against a second signal and mind Telegram's ToS/local law.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-osint-lib-postuf |
| category | messaging |
| selectorsIn → selectorsOut | phone, username → social-profile, name, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
