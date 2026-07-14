---
id: bmi-np-bot
name: MNProbot (phone operator & region lookup)
description: Use when you have a Russian `phone` number and want its current mobile operator and geographic region, accounting for number portability (MNP) — a Telegram bot returning carrier and coarse region.
url: https://t.me/MNProbot
category: messaging
path:
- messaging
bestFor: Identifying the operator and home region of a Russian mobile number, correctly handling ported (MNP) numbers.
selectorsIn:
- phone
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free Telegram bot. Requires a Telegram account to query it; no payment for lookups.
opsec: active
opsecNote: Active and account-bound — you send the target's number to a third-party bot, so the operator sees your query. Use a dedicated sock Telegram account; this only reveals carrier/region, not the subscriber's identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party Telegram bot over Russian numbering/MNP data. Operator/region mapping is generally reliable for planning, but it is unofficial — treat region as coarse, not an address.
missingPersonsRelevance: high
coverage:
- ru
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- bmi_np_bot
- MNProbot
tags:
- telegram
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# MNProbot (phone operator & region lookup)

> A Telegram bot that resolves a Russian mobile number to its current operator and home region, correctly accounting for mobile number portability (MNP).

## When to use
You have a Russian `phone` number and need to know which carrier serves it now and roughly where it originates. Because Russia allows number portability, a naive prefix lookup gives the wrong carrier; this bot factors in MNP to return the *current* operator plus the number's home region. Useful for prioritising which carrier/region records to pursue and for coarse geolocation of a number.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a **sock** Telegram account, open https://t.me/MNProbot and start the bot.
2. Send the target `phone` number in the requested format (Russian numbering).
3. Read the output: the current operator (carrier) and the number's home region (`geolocation`, coarse — an oblast/region, not a street address).
4. Pivot: the region narrows geographic focus; the carrier tells you which provider's data/legal process would apply. Combine with other phone-intel to build a fuller picture.

## Inputs → Outputs
- **In:** `phone` (Russian mobile number)
- **Out:** `geolocation` (home region), current mobile operator/carrier
- **Empty/negative result looks like:** an error or "not found" — usually a malformed number or a non-Russian number outside its coverage. It never returns a subscriber name/address.

## Gotchas & OpSec
- Region is coarse (the number's origin region), not the subscriber's current location — don't overstate it.
- Human-in-the-loop: a Telegram account and manual query are required.
- OpSec: **active** — the bot operator sees each number you submit. Use a sock account; only the carrier/region is revealed, but the query itself is logged by the bot.

## Overlaps ("do both")
- Pairs with broader phone-intelligence tools — this pins the current carrier/region (MNP-aware), while other tools attempt subscriber, breach, or messaging-app links for the same number.

## Trust & verifiability
`trust: community` — an unofficial bot over Russian numbering/MNP data. Carrier/region output is reliable enough for triage, but confirm anything decisive through carrier-level or official processes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bmi-np-bot |
| category | messaging |
| selectorsIn → selectorsOut | phone → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
