---
id: findstickercreator
name: FindStickerCreator
description: Use when you have a Telegram sticker pack (or a `social-profile` that shared one) and want to de-anonymise its creator — returns the creator's numeric Telegram user ID (a device-id/account pivot).
url: https://t.me/SPOwnerBot
category: messaging
path:
- messaging
bestFor: Revealing the numeric Telegram user ID of whoever created a given sticker pack.
selectorsIn:
- social-profile
selectorsOut:
- device-id
- social-profile
status: live
pricing: free
costNote: Free Telegram bot; no payment. Requires a Telegram account to message it.
opsec: passive
opsecNote: You forward a sticker to a bot — you do NOT contact the pack's creator, so the target is not notified. The bot operator sees your Telegram account and the query; use an investigative Telegram account, not your personal one. Sending a message to any bot exposes your account to that bot.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Community Telegram OSINT bot (the SPOwnerBot / PackOwnerBot family). It decrypts the pack's internal ID via Telegram's MTProto layer to surface the creator's user ID. Operator is anonymous; treat output as a lead.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- telegram-deanon
aliases:
- SPOwnerBot
- PackOwnerBot
- sticker pack owner finder
tags:
- telegram
- deanonymization
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# FindStickerCreator

> A Telegram bot that de-anonymises sticker packs: send it a sticker, get back the numeric Telegram ID of the pack's creator.

## When to use
A target uses a custom or personal Telegram sticker pack, and you want to link that pack to a stable account identifier. Telegram sticker packs embed their creator's account, but the standard Bot API hides the internal ID; this bot extracts the creator's numeric Telegram user ID. That ID is a durable pivot — it survives username and display-name changes — for correlating an account across other Telegram OSINT.

## How to use it (`bestInteractionPattern`: web-manual)
1. From an investigative Telegram account, open the bot: https://t.me/SPOwnerBot.
2. Forward or send it any sticker from the pack you want to attribute.
3. The bot decrypts the pack ID and replies with the creator's numeric Telegram user ID.
4. Pivot: run that numeric ID through other Telegram de-anonymisation resources (e.g. `[[telegram-deanon]]`) to tie it to a username, history, or shared groups.

## Inputs → Outputs
- **In:** a sticker from a pack (tied to a `social-profile` you're investigating)
- **Out:** the creator's numeric Telegram user `device-id`/account ID, a `social-profile` pivot
- **Empty/negative result looks like:** the bot errors or returns nothing — the pack may be an official/default set with no personal creator, or the bot is temporarily down; try a mirror bot in the PackOwnerBot family.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** — you need a Telegram account to message the bot.
- OpSec: **passive** toward the target (they aren't notified), but you expose your querying account to an anonymous bot operator — never use your personal account.
- The creator ID is the *pack's* author, which usually but not always equals the person who sent you the sticker; confirm before attributing.

## Overlaps ("do both")
- Pairs with broader Telegram de-anonymisation (`[[telegram-deanon]]`) — this hands you the numeric ID; those turn the ID into a username, group memberships, and history.

## Trust & verifiability
`trust: community` — an anonymous community bot using a documented MTProto trick. The numeric ID it returns is verifiable Telegram data, but the bot itself is untrusted infrastructure: use a burner account and corroborate the attribution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findstickercreator |
| category | messaging |
| selectorsIn → selectorsOut | social-profile → device-id, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
