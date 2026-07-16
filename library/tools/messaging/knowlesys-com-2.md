---
id: knowlesys-com-2
name: knowlesys.com
description: Use when you have a Telegram `username` and want the stable numeric user ID (which survives username/name changes) — returns a how-to for the @userinfobot technique.
url: https://knowlesys.com/en/articles/social_websites/telegram/how_to_find_a_user_id_in_telegram.html
category: messaging
path:
- messaging
bestFor: Learning how to pull a Telegram account's permanent numeric user ID via @userinfobot.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free tutorial article.
opsec: passive
opsecNote: Reading the guide is passive. The technique — forwarding a target's message to @userinfobot, or querying by username — is low-touch, but interacting with a third-party bot means trusting it; use a burner Telegram account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Knowlesys is an OSINT/monitoring vendor publishing how-to articles; the @userinfobot method it documents is a widely-used, verifiable Telegram technique.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- how to find a user ID in Telegram
- Telegram userinfobot guide
tags:
- telegram
- Telegram
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
relatedTools:
- knowlesys-com
- knowlesys-com-4
---

# knowlesys.com

> A how-to for retrieving a Telegram account's **permanent numeric user ID** — the identifier that stays constant even when a target changes their @username, display name, or photo.

## When to use
You're tracking a Telegram subject who might rename themselves to shake a tail. Usernames and display names are mutable; the numeric user ID is not. Capturing it early gives you a durable anchor: you can recognise the same account after a rename, and correlate it across groups and leaks that store user IDs. This article walks the simplest capture method (@userinfobot).

## How to use it (`bestInteractionPattern`: web-manual)
1. Read https://knowlesys.com/en/articles/social_websites/telegram/how_to_find_a_user_id_in_telegram.html for the steps.
2. On a **burner** Telegram account, start @userinfobot; forward a message from the target (or, where supported, query their username) and read back the numeric user ID plus basic account fields.
3. Record the user ID alongside the current username/display name as your anchor.
4. Pivot: use the ID to spot the same account after renames, and to cross-reference user-ID-indexed group dumps and OSINT bots.

## Inputs → Outputs
- **In:** Telegram `username` or a forwarded message from the target
- **Out:** permanent numeric user ID + basic account fields → durable `social-profile` anchor
- **Empty/negative result looks like:** the bot can't resolve the target (privacy settings, or no forwarded message) — you may need a message from the account rather than just a username.

## Gotchas & OpSec
- Use a **burner** Telegram account; you're handing a message/handle to a third-party bot, and you don't want that tied to you.
- Forwarding requires having a message from the target; a bare username alone doesn't always resolve.
- OpSec: **passive**/low-touch — the target isn't notified, but trust the minimum number of third-party bots.

## Overlaps ("do both")
- Pairs with `[[tginfo-me]]` (phone→profile discovery) — find the account by number, then lock a permanent ID onto it here so a later rename can't lose it.

## Trust & verifiability
`trust: community` — a vendor tutorial, but the @userinfobot method is standard and independently verifiable in-app; just vet any bot you feed data to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | knowlesys-com-2 |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
