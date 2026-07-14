---
id: shtrafkzbot
name: ShtrafKZBot
description: Use when you have a Kazakhstan national/business ID (`document-id`, ИИН/БИН) or a `vehicle-plate` and want to check that person's/vehicle's outstanding fines, taxes and penalties — a Telegram bot returning penalty records.
url: https://t.me/ShtrafKZBot
category: messaging
path:
- messaging
bestFor: Checking Kazakhstan fines, taxes and traffic penalties tied to a national ID (ИИН), business ID (БИН), or vehicle plate.
selectorsIn:
- document-id
- vehicle-plate
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free Telegram bot. Requires a Telegram account to message it; no payment for basic lookups.
opsec: active
opsecNote: Active and account-bound — you message a third-party Telegram bot with the target's identifiers, so the bot operator sees your query and the ID you submit. Use a dedicated sock Telegram account; never submit your own ИИН or personal data.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A community/third-party Telegram bot querying Kazakh government fine/tax portals. Data may reflect official sources, but the bot itself is unofficial — verify important results against the official e-gov portal.
missingPersonsRelevance: high
coverage:
- kz
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- ShtrafKZ
- Штрафы KZ bot
tags:
- telegram
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# ShtrafKZBot

> A Kazakhstan-focused Telegram bot that checks fines, taxes and traffic penalties by national ID (ИИН), business ID (БИН), or vehicle plate.

## When to use
Your subject is tied to Kazakhstan and you have their individual ID number (ИИН), a company's БИН, or a `vehicle-plate` (plus registration document number for traffic checks). The bot returns outstanding fines, taxes and penalties associated with those identifiers — useful for confirming an identifier is valid and in active use, and for corroborating vehicle ownership/activity in Kazakhstan.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a **sock** Telegram account, open https://t.me/ShtrafKZBot and start the bot.
2. Follow its prompts (interface is in Russian/Kazakh): choose fines/taxes-by-ИИН/БИН, or traffic-fines-by-plate.
3. Submit the `document-id` (ИИН/БИН) or the `vehicle-plate` + vehicle registration document number.
4. Read the output: penalty/tax records tied to that identifier. A populated response confirms the ID/plate is real and links it to fine/tax activity; an empty response means no outstanding penalties (not that the ID is invalid).
5. Pivot: a valid ИИН corroborates identity for other KZ record checks; an active plate feeds vehicle-ownership questions.

## Inputs → Outputs
- **In:** `document-id` (ИИН national ID / БИН business ID) or `vehicle-plate` (+ registration doc no.)
- **Out:** `document-id` (validated identifier) plus associated fine/tax/penalty records
- **Empty/negative result looks like:** "no fines/penalties found" — meaning nothing outstanding, which is distinct from the identifier not existing. A format error means the ID/plate was entered wrongly.

## Gotchas & OpSec
- Interface is Russian/Kazakh; be sure you're submitting the right identifier type.
- Human-in-the-loop: a Telegram account and manual interaction are required.
- OpSec: **active** — the bot operator receives every identifier you send. Use a sock account and only submit target identifiers you're authorized to check. Data is unofficial; confirm against the official Kazakh e-gov portal for anything material.

## Overlaps ("do both")
- Complements other Kazakhstan/CIS record checks — this validates an ИИН/plate via penalty data; pair with official e-gov lookups to confirm ownership and identity.

## Trust & verifiability
`trust: community` — an unofficial third-party bot fronting Kazakh government fine/tax data. Treat hits as leads and verify decisive findings on the official portal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | shtrafkzbot |
| category | messaging |
| selectorsIn → selectorsOut | document-id, vehicle-plate → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
