---
id: creationdatebot
name: Creation Date Bot (Telegram)
description: Use when you have a Telegram `username`/account and want to estimate when it was created — returns an approximate account age to judge if it's a fresh throwaway.
url: https://t.me/creationdatebot
category: messaging
path:
- messaging
bestFor: Estimating a Telegram account's creation date/age from its numeric user ID, to gauge how new (throwaway) or established an account is.
selectorsIn:
- username
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free Telegram bot; you need a Telegram account to message it.
opsec: active
opsecNote: You must use a Telegram account to query the bot, and querying by username/ID means the bot operator sees your request. Use a sock-puppet Telegram account, never your primary; avoid actions that would notify the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A community Telegram bot; the creation date is an *estimate* interpolated from Telegram's sequential user IDs (not an official field), and the third-party operator's data handling is opaque — treat the age as approximate.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- telegram-finder
aliases:
- '@creationdatebot'
- Telegram creation date bot
tags:
- telegram
- account-age
- messaging
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Creation Date Bot (Telegram)

> A Telegram bot that estimates when an account was created from its numeric user ID — a quick way to tell a brand-new throwaway from a long-established account.

## When to use
You're investigating a Telegram account and want to know its **age**. Telegram user IDs are roughly sequential, so a rough creation date can be interpolated. A very recently created account interacting in a case is a throwaway/burner signal; a years-old account is more likely a real, established identity. Use it as a credibility/priority signal, not as identity attribution.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a **sock-puppet** Telegram account, open the bot at https://t.me/creationdatebot and start it.
2. Send the target's numeric Telegram user ID (or forward a message from them so the bot can read the ID), per the bot's instructions.
3. Read the estimated creation date/age it returns.
4. Interpret: recent = likely throwaway; old = established. Treat the exact date as approximate.
5. Pivot: pair with `[[telegram-finder]]` (number→account) and normal Telegram profile review to build the fuller picture.

## Inputs → Outputs
- **In:** `username`/numeric Telegram user ID
- **Out:** `metadata-exif` — an estimated account creation date/age
- **Empty/negative result looks like:** the bot can't resolve the ID, or gives a wide/uncertain range — meaning limited data; don't over-rely on a single estimate.

## Gotchas & OpSec
- The date is an **interpolated estimate**, not an official Telegram field — accurate enough for "new vs old," not for exact timing.
- You need the numeric user ID (not just @handle) for a reliable answer.
- OpSec: **active** — you query via a Telegram account and the bot operator sees your request; use a burner account.

## Overlaps ("do both")
- Pairs with `[[telegram-finder]]` — that maps a phone number to an account; this ages the account. Together they help judge whether a Telegram identity is real and worth pursuing.

## Trust & verifiability
`trust: unverified` — a community bot giving an ID-based estimate from an opaque operator; use the age as a directional signal and corroborate account legitimacy through profile/behaviour.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | creationdatebot |
| category | messaging |
| selectorsIn → selectorsOut | username → metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
</content>
