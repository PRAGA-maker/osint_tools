---
id: tempmail-org-bot
name: '@TempMail_org_bot'
description: Use when you (the investigator) need a throwaway email address to register a sock-puppet account or receive a verification code without exposing a real inbox — a Telegram bot that spins up disposable inboxes; returns a temporary email.
url: https://t.me/TempMail_org_bot
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Quickly generating a disposable email inbox from Telegram for sock-puppet registrations.
selectorsIn: []
selectorsOut:
- email
status: live
pricing: free
costNote: Free Telegram bot; you need a Telegram account (ideally a sock-puppet one) to use it.
opsec: passive
opsecNote: This is an opsec convenience for YOUR side — a burner inbox so you never hand a real/attributable email to a site you're investigating or registering on. Assume the temp-mail provider (and Telegram) can read everything that arrives; never use it for anything requiring confidentiality, account recovery, or long-term access. Use a dedicated sock-puppet Telegram account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party disposable-email bot of unknown operator; treat inboxes as fully public and ephemeral, and never rely on message delivery or retention.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- TempMail Telegram bot
- TempMail_org_bot
tags:
- Sock Puppets
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# @TempMail_org_bot

> A Telegram bot that hands you a disposable email inbox on demand — burner addresses for sock-puppet registrations, without touching a real mailbox.

## When to use
Sock-puppet hygiene, not a lookup. When you need to register on a site, receive a one-time verification code, or sign up for a service as part of an investigation and don't want to expose an attributable email, this bot generates a temporary address and shows you incoming mail inside Telegram. It keeps throwaway signups off your real identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://t.me/TempMail_org_bot in Telegram (use a **sock-puppet** Telegram account).
2. Start the bot; it issues a temporary email address.
3. Use that address to register/verify on the target service.
4. Watch the bot for the incoming message/verification code.
5. Discard the inbox when done; generate a fresh one per identity to avoid cross-linking.

## Inputs → Outputs
- **In:** none (you request an inbox)
- **Out:** a temporary `email` address and its incoming messages
- **Empty/negative result looks like:** no mail arriving — the target site may block known disposable-email domains, or the message was delayed/lost (temp providers are unreliable).

## Gotchas & OpSec
- **Assume it's public:** the operator and Telegram can see everything that lands — never use it for sensitive mail or as a recovery address.
- Many services **block disposable-email domains** at signup; have a fallback.
- Ephemeral and unreliable — no retention, no guaranteed delivery; use one inbox per sock puppet to prevent linkage.

## Overlaps ("do both")
- Interchangeable with web temp-mail services (10MinuteMail, temp-mail.org) and SMS-verification burners; pick per what a signup demands (email vs phone), and pair with a sock-puppet browser/VPN.

## Trust & verifiability
`trust: unverified` — an anonymous third-party bot; fine as a disposable burner, but treat every inbox as public, temporary, and non-guaranteed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tempmail-org-bot |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
