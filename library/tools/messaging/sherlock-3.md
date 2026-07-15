---
id: sherlock-3
name: Sherlock (Telegram Getcontact-style bot)
description: Use when you have a `phone` number and want the names it is saved as in other people's contacts — a Telegram GetContact-style lookup bot that returns name/tag strings.
url: https://t.me/Getcontact123qwerty_bot?start=_ref_jGW8Sa_iEmG9V
category: messaging
path:
- messaging
bestFor: Reverse phone → name/tag lookup by querying crowdsourced contact-book data via a Telegram bot.
selectorsIn:
- phone
selectorsOut:
- name
status: unknown
pricing: free
costNote: The bot advertises free lookups, typically metered — a few queries then a paywall/credit prompt or a referral requirement.
opsec: active
opsecNote: You hand the target's phone number to an unknown third-party bot operator via your Telegram account, which reveals your Telegram identity/ID to them and logs the number you searched. Use a burner Telegram account, never your real one. Assume the operator harvests every number queried.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: chrome-mcp
trust: unverified
trustNote: An anonymous Telegram bot reached via a referral link — not the official GetContact app. Could be a legitimate data reseller, a scam, or a data-harvesting honeypot; provenance and data quality are unknown.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Getcontact Telegram bot
- phone name lookup bot
tags:
- telegram
- getcontact
- phone-lookup
- caller-id
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Sherlock (Telegram Getcontact-style bot)

> Despite the "Sherlock" label, this is a **Telegram GetContact-style bot**: send it a phone number and it returns the names/tags that number is saved under in crowdsourced contact books.

## When to use
You have a `phone` number and no name, and want to know how that number is labelled in other people's address books — often the person's real name, a nickname, or a business/scam tag ("Mum", "John Plumber", "SCAM"). Crowdsourced caller-ID data can put a name to an otherwise anonymous number, a useful early pivot in missing-persons and fraud work.

## How to use it (`bestInteractionPattern`: chrome-mcp)
1. From a **burner** Telegram account, open the bot link and `/start` it.
2. Send the number in full international format (e.g. `+447700900123`).
3. Read the returned tag list — the names/labels others have saved for that number.
4. Pivot: a returned `name` feeds people-search, social and public-records lookups; a "scam/spam" tag reframes the number as a fraud lead rather than a person.

## Inputs → Outputs
- **In:** `phone`
- **Out:** `name` (crowdsourced contact tags / labels)
- **Empty/negative result looks like:** "no tags found", a paywall/credit prompt before showing results, or a demand to refer others. No tags means the number isn't in the bot's dataset — not that it's unassigned.

## Gotchas & OpSec
- **Unknown, unofficial operator.** This is a referral-link bot, **not** the official GetContact app. Treat it as untrusted infrastructure: it may be a scam, may return fabricated tags, or may exist mainly to harvest the numbers people submit. Prefer the official GetContact app/site where possible.
- **Active exposure:** querying it discloses the target number *and* your Telegram identity to the operator — always use a burner account.
- Tags are crowdsourced and unverified — a name is a lead, never proof; multiple conflicting tags are common.
- Free tier is usually metered; expect a paywall or referral gate after a few lookups.

## Overlaps ("do both")
- Pairs with official caller-ID/number-reputation services and number-to-account checks — those give a more trustworthy read on the same number; use this only to add crowdsourced tags, then corroborate elsewhere.

## Trust & verifiability
`trust: unverified` — an anonymous Telegram bot of unknown provenance. Do not rely on it alone; confirm any name it returns through an independent, trustworthy source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sherlock-3 |
| category | messaging |
| selectorsIn → selectorsOut | phone → name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | chrome-mcp |
| opsec | active |
| human-in-loop | yes (account-login) |
