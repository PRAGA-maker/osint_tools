---
id: leak-osint
name: Leak OSINT
description: Use when you have an `email`, `phone`, `username` or `name` and want to check it against aggregated data-breach dumps via a Telegram bot — returns leaked password, email, phone, address and name fragments.
url: https://telegram.me/Leak_SSINTbot
category: messaging
path:
- messaging
bestFor: Quick breach-data lookups on an email/phone/username from inside Telegram.
selectorsIn:
- email
- phone
- username
- name
selectorsOut:
- password
- email
- phone
- address
- name
status: live
pricing: freemium
costNote: A handful of free lookups; deeper/unmasked results are gated behind paid credits or a subscription bought inside the bot.
opsec: passive
opsecNote: Queries never reach the target, but you are handing the target's PII to an anonymous bot operator who logs every request and could resell it. Run it only from a burner Telegram account on a sock-puppet number, and assume the operator sees exactly what you searched.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous Telegram breach-aggregator bot; source dumps are of unknown provenance and may be stale, partial, or salted with false records. Treat every hit as a lead to verify, not fact.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- avtogram-bot
- datxpert
- discord-sensor
- getchatlist
- getsendgifts
- instabot
- oksearch
- pimeyes
- searchforchats
- spyggbot
- unamer
aliases:
- Leak_SSINTbot
- Leak OSINT bot
tags:
- telegram
- breach-data
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Leak OSINT

> A Telegram breach-lookup bot that matches an email/phone/username against aggregated leak dumps and returns whatever PII co-occurs in those records.

## When to use
You have one selector on a subject — an `email`, `phone`, `username`, or `name` — and want to know what else appears alongside it in historical data breaches: an old password, a linked secondary email, a phone number, or a home address. Useful for corroborating that an account belongs to your subject and for surfacing pivot selectors you didn't have.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a burner Telegram account (Telegram Web works), open https://telegram.me/Leak_SSINTbot and press Start.
2. Send the selector you're investigating (e.g. the email or phone) as a message to the bot.
3. Read the returned records: each hit typically lists the source dump plus co-occurring fields (password, name, address, other emails/phones).
4. Pivot: a leaked secondary email/phone feeds email- and phone-OSINT; a reused password or breach name corroborates account ownership. Free lookups are limited — the bot will prompt for paid credits for more.

## Inputs → Outputs
- **In:** `email`, `phone`, `username`, or `name`
- **Out:** `password`, `email`, `phone`, `address`, `name` fragments drawn from breach records
- **Empty/negative result looks like:** "no results found" or an empty record set — means that selector isn't in the bot's dump set, NOT that the person was never breached (coverage varies wildly between bots).

## Gotchas & OpSec
- Human-in-the-loop: requires a logged-in Telegram account to talk to the bot.
- OpSec: passive toward the target but exposes your query to an untrusted operator — use a burner account/number and never query with your own live selectors mixed in.
- Legal/ethical: handling breach data is regulated in many jurisdictions; confirm your engagement authorizes it.
- Records can be stale or fabricated; always verify a hit against a second breach source before relying on it.

## Overlaps ("do both")
- Run alongside another Telegram OSINT bot such as `[[osint-tool-for-tg]]` or `[[maigret-osint-bot]]` — dump coverage differs bot to bot, so one finds records the other misses.
- Pairs with account-existence checks like `[[account-live-com]]` to confirm a leaked email is still a live account.

## Trust & verifiability
`trust: unverified` — an anonymous aggregator bot with no accountable operator and unaudited dumps; treat output strictly as leads to corroborate elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leak-osint |
| category | messaging |
| selectorsIn → selectorsOut | email, phone, username, name → password, email, phone, address, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
