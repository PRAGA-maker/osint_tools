---
id: getairplane
name: Getairplane (flight-history bot)
description: Use when you have a `phone` and want to check for associated airline-booking / flight-history records — returns name and geolocation (route) leads from leaked travel data.
url: https://t.me/getairplane_bot
category: messaging
path:
- messaging
bestFor: Reverse-checking a phone number against leaked airline booking data for flight history.
selectorsIn:
- phone
selectorsOut:
- name
- geolocation
status: degraded
pricing: freemium
costNote: Free tier returns a truncated result (about three lines); fuller output is paywalled/credit-gated.
opsec: active
opsecNote: This is a "probiv" bot querying breached/leaked airline data via a Telegram account you control. The query runs through the bot operator, who logs your account and every number you submit; results derive from stolen data, so treat use as legally sensitive. Use a dedicated sock-puppet Telegram account on a burner number over VPN, and confirm you have lawful basis before querying a real person.
humanInLoop: true
humanInLoopReason:
- account-login
- legal-gate
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous Telegram bot trading on breached airline data; no accountable operator, no provenance, and results cannot be independently verified. Data may be stale, partial, or fabricated.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
aliases:
- getairplane_bot
tags:
- telegram
- probiv
- flight-osint
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Getairplane (flight-history bot)

> A Telegram "probiv" bot that reverse-checks a phone number against leaked airline booking data to surface flight history — high-leverage but legally and ethically loaded.

## When to use
You have a `phone` for a subject and, within a lawful investigative context (e.g. a sanctioned missing-persons or law-enforcement workflow), you want to test whether it appears in leaked airline-booking datasets — which can reveal travel routes, dates, and the passenger name tied to the booking. Because the data is breach-sourced, this is a last-resort corroboration tool, not a first move, and only where you have legal authority to use it.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a **dedicated sock-puppet** Telegram account (burner number, VPN), open https://t.me/getairplane_bot and press Start.
2. Send the target `phone` in the format the bot requests (usually full international format).
3. The free response returns a truncated summary (about three lines) — typically a matched passenger name and route fragments; fuller history is credit/paywall-gated.
4. Record what you get as an unverified lead only, then corroborate against a legitimate source before acting on it.
5. Pivot: a returned `name` → identity OSINT; a route/`geolocation` → timeline reconstruction.

## Inputs → Outputs
- **In:** `phone`
- **Out:** `name` (passenger on file), `geolocation` (flight routes/destinations)
- **Empty/negative result looks like:** "no data / нет данных" or a blank result — the number is not in the bot's leaked corpus. This is not proof the person has never flown; it only means this dataset has no hit.

## Gotchas & OpSec
- **Legal-gate:** results come from stolen airline data — querying a real individual may be unlawful depending on jurisdiction and purpose. Confirm authority first.
- **Account-login:** requires a Telegram account, which the operator logs alongside every number you submit — never use a real account.
- **Payment-wall-partial:** only a stub is free; the bot upsells credits for full history.
- Data can be stale, incomplete, or fabricated to drive purchases; treat every field as unverified.

## Overlaps ("do both")
- Pairs with legitimate phone-attribution tools (carrier/HLR lookups, `[[account-live-com]]`-style existence checks) — those confirm the number is real and owned; this bot is the (risky) travel-history angle. Prefer lawful sources first.

## Trust & verifiability
`trust: unverified` — an anonymous breach-data bot with no accountable operator and no way to verify provenance; use only as a lead to corroborate elsewhere, never as standalone evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | getairplane |
| category | messaging |
| selectorsIn → selectorsOut | phone → name, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, legal-gate, payment-wall-partial) |
