---
id: send-text-free
name: Send text free
description: Use when you need to send an SMS to a `phone` number without exposing your own number during sock-puppet contact — a free web SMS sender, not a lookup.
url: https://globfone.com/send-text/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Sending a one-off SMS to a phone number from the web without revealing your personal number.
selectorsIn:
- phone
selectorsOut: []
status: live
pricing: free
costNote: Free web SMS (ad-supported); premium tiers exist for calling. Now requires account "credibility" verification to send.
opsec: active
opsecNote: This SENDS a message to a target's `phone` — an active, intrusive contact that the recipient sees and can report; it is not passive research. Delivery is not truly anonymous (the service now requires verification and logs sending). Only use for authorised pretext contact, from a sock-puppet identity, and understand the message is attributable to the platform.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running free web-communications service (Globfone); reliable for sending, but message delivery/anti-abuse behaviour is opaque and it is not anonymous.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Globfone Send Text
tags:
- sms
- burner
- opsec
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Send text free

> A free web SMS sender (Globfone) — lets you text a number from the browser without using your own phone, for authorised pretext/sock-puppet contact. It is an *outbound-contact* tool, not passive OSINT.

## When to use
Rarely, and only in an active, authorised context: you must send an SMS to a subject or contact (a pretext message, a controlled outreach) and do not want to expose your personal number. This is an intrusive step — it reaches out and touches the target — so it sits well outside passive collection.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://globfone.com/send-text/ in a sock-puppet browser session.
2. Complete the required verification/"credibility" step the service now enforces against abuse.
3. Enter the destination `phone` number and your message; send.
4. Expect no reply channel and no delivery guarantee — it is one-way and best-effort.
5. No pivot — this is an outbound action, not a source of new selectors.

## Inputs → Outputs
- **In:** `phone` (destination number) + message text
- **Out:** none as a selector — a sent (or failed) SMS
- **Empty/negative result looks like:** send blocked by verification/anti-abuse, or silently undelivered — treat non-delivery as likely, not exceptional.

## Gotchas & OpSec
- **Active/intrusive and legally sensitive:** contacting a subject can taint an investigation, violate law, or tip off the target — get authorisation first.
- Not anonymous: the service verifies senders and logs activity; do not assume untraceability.
- Human-in-the-loop: the verification/credibility gate (`manual-review`) must be cleared before sending.

## Overlaps ("do both")
- For passive phone research (which is what most cases need), use phone-lookup/enumeration tools instead; reach for a sender like this only when controlled outbound contact is genuinely part of an authorised plan.

## Trust & verifiability
`trust: community` — established free service, but delivery and anti-abuse handling are opaque; never rely on it for guaranteed or anonymous delivery.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | send-text-free |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | phone →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (manual-review) |
