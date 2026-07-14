---
id: receive-sms-free
name: Receive SMS (free)
description: Use when you have a `phone` number and want to check whether it is a public disposable/temp-SMS number (so any account on it is likely throwaway), or need a burner number to receive an OTP — returns disposable-number status and inbound SMS.
url: http://sms.sellaite.com
category: phone
path:
- phone
bestFor: Flagging a number as a known public temp-SMS number, and receiving OTPs on a throwaway number for sock-puppet registrations.
selectorsIn:
- phone
selectorsOut:
- phone
status: live
pricing: free
costNote: Free public disposable-number service (Sellaite SMS receiver); no account needed.
opsec: passive
opsecNote: Any SMS received on these numbers is publicly visible to everyone — never route anything you care about through them. Checking whether a number is listed is passive. Keep these numbers entirely away from your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: One of many interchangeable public temp-SMS sites; the numbers and public inboxes are exactly as advertised, but any specific number's uptime/availability is not guaranteed.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- receive-sms-free-2
- receive-smss-com
aliases:
- Sellaite SMS
- sms.sellaite.com
- disposable phone number
tags:
- phone
- disposable-number
- temp-sms
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Receive SMS (free)

> A public disposable-number service (Sellaite) with two OSINT uses: confirm a number is a shared throwaway, and grab a burner number to receive a one-time code for a sock puppet.

## When to use
Two cases. (1) **Attribution check:** you have a `phone` number tied to an account and want to know if it's a shared public temp-SMS number — if it's listed here (or on sibling sites), the account was almost certainly registered with a disposable number, so the number is not a reliable identity link. (2) **Tradecraft:** you need a throwaway number to receive an OTP during a sock-puppet registration without exposing a real number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://sms.sellaite.com — it lists free public number(s) with live, public inboxes.
2. **To check a number:** search this and other temp-SMS aggregators for the number in question; a hit means it's a known public disposable number.
3. **To receive an OTP:** use a listed public number during the target registration, then read the incoming code in that number's public inbox.
4. Remember the inbox is fully public — anyone can read every message.
5. Pivot: a confirmed disposable number downgrades the trust of any account behind it; a burner number lets sock-puppet OSINT proceed.

## Inputs → Outputs
- **In:** `phone` (to check), or none (to pick a burner)
- **Out:** disposable-number status (is/ isn't a known public number), inbound SMS content on the public number
- **Empty/negative result looks like:** the number isn't listed here — it's either a real/private number or a disposable one from a different provider; check several temp-SMS sites before concluding a number is genuine.

## Gotchas & OpSec
- **Public inbox:** never receive anything sensitive; codes are readable by anyone, and others may hijack an account you register.
- Public numbers are frequently blocked by major services and rotate/disappear — a listed number may be dead or blocked.
- A "not found" is weak evidence a number is real; the disposable-number ecosystem is huge and fragmented.
- OpSec: passive; keep these numbers strictly away from your real identity.

## Overlaps ("do both")
- Pairs with other temp-SMS aggregators like [[receive-sms-free-2]] and [[receive-smss-com]] — which numbers exist differs per site, so to confirm a number is disposable (or to find a working burner) you must check several.

## Trust & verifiability
`trust: community` — the service does exactly what it says (public numbers, public inboxes), but no specific number is guaranteed live or unblocked; cross-check across temp-SMS sites when using it as an attribution signal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | receive-sms-free |
| category | phone |
| selectorsIn → selectorsOut | phone → phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
