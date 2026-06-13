---
id: 2chat
name: 2Chat
description: Use when you have a phone number and need to confirm whether it has an active WhatsApp account.
url: https://2chat.co/tools/whatsapp-checker
category: messaging
path:
- messaging
bestFor: Checking whether a phone number is registered on WhatsApp (single free lookup; bulk via paid API).
selectorsIn:
- phone
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Single-number web checker is free with no login. Bulk verification and API access require a paid 2Chat account (Single Plan or higher) with API credentials.
opsec: active
opsecNote: A WhatsApp registration check probes WhatsApp's infrastructure for the target number. It does not message the subject, but it is a lookup against a live account — avoid high-volume checks that could be rate-limited or flagged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Run by 2Chat (commercial WhatsApp business-API vendor); the free checker is powered by their public API. Reliable for presence checks, but it confirms only existence, not identity.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- 2Chat WhatsApp Checker
tags:
- whatsapp
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# 2Chat

> WhatsApp number checker: enter a phone number and learn whether it has an active WhatsApp account.

## When to use
You have a `phone` number for a missing person (or an associate) and want to confirm it is live on WhatsApp before pivoting — a positive hit tells you the number is in use and worth pursuing through other WhatsApp OSINT (profile photo, about text via the app).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://2chat.co/tools/whatsapp-checker.
2. Select the country code and enter the phone number.
3. Read the result: registered (has WhatsApp) vs. not registered.
4. Pivot: if registered, save the contact on a sock-puppet device to view any public profile photo / about line, then reverse-image the photo.

## Inputs → Outputs
- **In:** `phone`
- **Out:** `social-profile` (boolean WhatsApp presence)
- **Empty/negative result looks like:** "not registered" — the number has no WhatsApp account, or the result is rate-limited; the free checker does not return name or photo.

## Gotchas & OpSec
- The free tool only returns yes/no presence — no profile data, name, or photo.
- OpSec: active in the sense that it queries WhatsApp's live registry. Keep volume low; bulk checks need the paid API and can be throttled.
- Presence ≠ identity: a registered number confirms the line is active, not who holds it.

## Trust & verifiability
`trust: community` — backed by 2Chat's commercial WhatsApp API. The presence result is generally reliable; confirm ownership through independent corroboration before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 2chat |
| category | messaging |
| selectorsIn → selectorsOut | phone → social-profile |
| pricing / cost | freemium (free single check; paid bulk/API) |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
