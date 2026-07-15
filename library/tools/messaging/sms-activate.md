---
id: sms-activate
name: SMS Activate / PrivatePhoneBot (virtual numbers)
description: Use when you need a disposable `phone` number to receive an SMS/OTP for a sock-puppet account without exposing your own number — rents temporary numbers by country/operator via a Telegram bot.
url: https://t.me/PrivatePhoneBot
category: messaging
path:
- messaging
bestFor: Renting a temporary virtual phone number to receive verification SMS/calls when creating research/sock-puppet accounts.
selectorsIn: []
selectorsOut:
- phone
status: live
pricing: freemium
costNote: "Pay-per-use: you top up a small balance (often crypto/card) and pay cents-to-dollars per number/rental depending on country and target service. No large free tier — budget a few dollars for burner numbers."
opsec: passive
opsecNote: This is OpSec *infrastructure* for you, not a lookup on a target. It protects your identity by keeping your real number off research accounts. Caveats these are shared/recycled numbers (someone else may have used or later use them), the operator sees which services you verify, and some platforms detect and block known virtual-number ranges. Never route anything tied to your real identity through it.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A functioning commercial virtual-number reseller (Telegram front-end to an SMS-Activate-style service); reliable enough for OTP capture but an opaque third party — assume it logs your activity and never handle sensitive verifications through it.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- SMS Activate Bot
- PrivatePhoneBot
- Private Phone
tags:
- telegram
- virtual-number
- sock-puppet
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# SMS Activate / PrivatePhoneBot (virtual numbers)

> A Telegram-based virtual-number service: rent a disposable phone number to receive a verification SMS/OTP, so your real number never touches a sock-puppet account.

## When to use
You are building a research/sock-puppet account (to browse a gated platform, run an account-existence check, or lurk a community) and the platform demands SMS verification. Rather than burn your real `phone`, rent a temporary number here to receive the one-time code. This is tradecraft infrastructure — it does not look anyone up; it protects *your* attribution.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://t.me/PrivatePhoneBot in Telegram (from an account already compartmentalized from your identity) and start the bot.
2. Top up a small balance as instructed (crypto/card).
3. Search for a number by country and operator, and select the target service (WhatsApp, Telegram, Gmail, Twitter, etc.) so you get a number likely to be accepted.
4. Trigger the SMS on the target platform, then read the received code in the bot; resend if needed within the rental window.
5. Record which persona used which number — reused/recycled numbers can collide with other people's accounts.

## Inputs → Outputs
- **In:** (none — you specify a target country/operator/service, not a person)
- **Out:** a disposable `phone` number and the SMS/OTP it receives
- **Empty/negative result looks like:** the target platform rejects the number (known virtual range) or no SMS arrives in the window — try a different country/operator or service-specific number.

## Gotchas & OpSec
- Human-in-the-loop: requires a Telegram account and a funded balance (payment wall).
- Shared/recycled numbers: others may have used the number before (or after) you — never use it for anything you need to keep or that ties to your identity, and expect some platforms to block it.
- OpSec: the point is protecting *your* attribution; the flip side is you trust an opaque operator with your verification activity, so keep it to low-stakes research accounts only.

## Overlaps ("do both")
- Pairs with sock-puppet email providers and browser-isolation/VPN tooling — a research identity needs a burner number, a burner email, and network isolation together; this covers the number.

## Trust & verifiability
`trust: community` — a working but opaque commercial reseller; fine for capturing an OTP on a throwaway account, never for sensitive verifications, and assume the operator logs what you do.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sms-activate |
| category | messaging |
| selectorsIn → selectorsOut |  → phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
