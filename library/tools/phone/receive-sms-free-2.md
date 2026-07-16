---
id: receive-sms-free-2
name: Receive SMS (free)
description: Use when you have a `phone` number and want to check whether it is a public disposable/temp-SMS number (not a real person), or need a throwaway number to receive an OTP for a sock puppet — returns disposable-number status and inbound SMS.
url: https://receive-sms-online.com
category: phone
path:
- phone
bestFor: Flagging a number as a known public/temporary SMS number, and receiving OTPs on a throwaway number for sock-puppet registrations.
selectorsIn:
- phone
selectorsOut:
- phone
status: live
pricing: free
costNote: Free public disposable-number service; no account needed. Paid "private number" tiers exist elsewhere but the public numbers are free.
opsec: passive
opsecNote: Anything received on a public number is visible to everyone — never route a message you care about through it. Checking whether a number is on the site is passive. Do not use these numbers for anything tied to your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: One of many interchangeable public temp-SMS sites; the numbers and their public inboxes are exactly as advertised, but the operator and uptime of any given number are not guaranteed.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- receive-smss-com
- sms-activate
- receive-sms-online
aliases:
- receive-sms-online.com
- temporary SMS number
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

> A public disposable-number service with two OSINT uses: confirm a number is a throwaway (so any account on it is likely fake), and grab a burner number to receive an OTP for a sock puppet.

## When to use
Two cases. (1) **Attribution check:** you have a `phone` number tied to an account and want to know if it's a shared public temp-SMS number — if it appears here, the account was almost certainly registered with a disposable number, so the number is not a reliable identity link. (2) **Tradecraft:** you need a burner number to receive a one-time code when registering a sock-puppet account, without exposing a real number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://receive-sms-online.com — it lists free public numbers by country, each with a live public inbox.
2. **To check a number:** search the site (and sibling temp-SMS sites) for the number in question; a hit means it's a known public disposable number.
3. **To receive an OTP:** pick a listed number, use it during the target registration, then open that number's public inbox to read the incoming code.
4. Understand the inbox is fully public — everyone sees every message.
5. Pivot: a confirmed disposable number downgrades the trust of any account behind it; a burner number lets sock-puppet OSINT proceed.

## Inputs → Outputs
- **In:** `phone` (to check), or none (to pick a burner)
- **Out:** disposable-number status (is/ isn't a known public number), inbound SMS content on the public number
- **Empty/negative result looks like:** the number isn't listed here — it's either a real/private number or a disposable one from a different provider; check several temp-SMS sites before concluding it's genuine.

## Gotchas & OpSec
- **Public inbox:** never receive anything sensitive; codes are readable by anyone, and others may hijack an account you register.
- Numbers rotate and get burned/blocked by major services frequently — a listed number may already be dead or blocked by the target site.
- A "not found" here is weak evidence the number is real; the disposable-number ecosystem is huge and fragmented.
- OpSec: passive; keep these numbers strictly away from your real identity.

## Overlaps ("do both")
- Pairs with other temp-SMS aggregators like [[receive-smss-com]] and [[sms-activate]] — coverage of which numbers exist differs per site, so to confirm a number is disposable (or to find a working burner) you must check several.

## Trust & verifiability
`trust: community` — the service does exactly what it says (public numbers, public inboxes), but there's no guarantee a specific number is live or unblocked; cross-check across temp-SMS sites when using it as an attribution signal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | receive-sms-free-2 |
| category | phone |
| selectorsIn → selectorsOut | phone → phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
