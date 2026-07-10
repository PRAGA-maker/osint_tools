---
id: sms-receive-net
name: sms-receive.net
description: Use when you have a `phone` number and want to check whether it is a public throwaway SMS-receive number (or need a disposable number yourself) — returns whether the number is a shared/public line and its publicly displayed inbound SMS.
url: https://sms-receive.net/
category: phone
path:
- phone
bestFor: Identifying disposable/public SMS-receive numbers and reading their public inbound message logs.
selectorsIn:
- phone
selectorsOut:
- phone
status: live
pricing: free
costNote: Completely free; no account. Numbers and their received messages are public — anyone can read them.
opsec: passive
opsecNote: Reading the public number pages is passive and touches only sms-receive.net. Do NOT use one of these numbers to register/verify an account tied to your investigation — messages are public and the number is shared, so any OTP or reset code you receive is visible to everyone and the number can be reclaimed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running free public-SMS service; useful and genuine, but numbers rotate and are shared, so treat any account tied to one as disposable/untrustworthy.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SMS Receive
- receive SMS online
tags:
- mobilephone
- Mobile & Phone Related
- disposable-number
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# sms-receive.net

> A free directory of public, shared phone numbers that receive SMS online — use it to flag a number as a disposable throwaway, or to read the public inbound messages on one.

## When to use
Two cases. (1) You have a `phone` number tied to a subject's account and want to test whether it is a **public disposable number** — if it appears here, any account "verified" with it is essentially anonymous/throwaway, not a real identity anchor. (2) You need a burner number yourself to receive a verification SMS without exposing a real line (understanding the code will be public).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sms-receive.net/.
2. To check a number: browse the country lists (UK, USA, France, Germany, Russia, etc.) and see if the target number is listed as one of the public receive lines.
3. To use a number: pick a listed number, use it in a registration flow, then open that number's page to read the incoming SMS (including OTP codes) — publicly visible to all.
4. Pivot: if a subject's number matches a public line, downgrade the trust of any account registered to it and look for the subject's real number elsewhere.

## Inputs → Outputs
- **In:** `phone` (number to test), or none (just pick a disposable number)
- **Out:** whether the `phone` is a public/shared receive number; the publicly logged inbound SMS for that number
- **Empty/negative result looks like:** the target number is not in the list — it is (probably) not one of *this* service's public numbers, but it could still be a burner on a different service, so check other public-SMS sites before concluding it's a personal line.

## Gotchas & OpSec
- Every message on these numbers is public and non-deletable — never send anything sensitive to them.
- Numbers rotate and get blocked by major platforms; a listed number may already be dead for a given service.
- The set here is only one provider's numbers; a "not found" doesn't rule out other disposable-SMS services.

## Overlaps ("do both")
- Pairs with other public-SMS sites (receive-smss, sms-online, etc.) — check several, since each exposes a different pool of shared numbers when testing whether a subject's number is a throwaway.

## Trust & verifiability
`trust: community` — a genuine free public-SMS service. Reliable for its stated purpose; its main OSINT value is negative evidence — proving a number is a shared disposable, not identifying a person.
