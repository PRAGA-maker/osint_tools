---
id: receive-sms-free-3
name: Receive-SMS (free)
description: Use when you need a disposable `phone` number to receive SMS for a sock-puppet signup, or want to check whether a target's number is a known public/shared burner — returns public inbox messages and number metadata.
url: https://receive-sms.com
category: phone
path:
- phone
bestFor: Provisioning throwaway numbers for investigative signups, and recognising numbers that are public shared-SMS burners.
selectorsIn:
- phone
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free shared public numbers (messages visible to everyone); private, dedicated numbers require an account and payment. The free tier is fine for OpSec-tolerant signups and for the "is this a burner?" check.
opsec: active
opsecNote: Two modes. Using a free number for your own signups is operational, not a query against a target. Free numbers are PUBLIC — anyone can read the SMS, so never send them a real 2FA/reset code tied to your identity. Checking whether a target's number appears here is passive. Buying a private number ties a payment trail to you; use appropriate cover.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Typical public disposable-SMS service; operator anonymous. Reliable for its purpose but treat all free-number traffic as fully public and untrusted.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- fastmail-usa
aliases:
- receive-sms.com
- disposable SMS
tags:
- phone
- disposable-number
- sock-puppet-infrastructure
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Receive-SMS (free)

> Public disposable phone numbers for receiving SMS online — sock-puppet infrastructure, and a way to spot when a target verified an account with a shared burner.

## When to use
Two cases. (1) You need a throwaway `phone` to receive a verification SMS for a sock-puppet account and don't want to burn a real number — pick a free public number here. (2) You have a target's number and want to test whether it's a *known public burner*: if the same number is listed here as a shared receive-SMS line, any account "verified" with it is essentially anonymous, and the public inbox may show which services recently sent it codes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://receive-sms.com and browse the free public numbers by country.
2. To provision: choose a free number, use it at the signup you're seeding, then read its public inbox for the incoming code. (For a private number, register and pay.)
3. To investigate a target number: search whether it appears among the site's public numbers; if so, read the public message log for service names/codes recently received.
4. Pivot: services revealed in a public inbox are `social-profile` leads; pair puppet numbers with a clean mailbox from `[[fastmail-usa]]`.

## Inputs → Outputs
- **In:** `phone` (a target number to check, or your choice of a free number to use)
- **Out:** `social-profile` (public SMS log revealing signups tied to a shared number; number status as public/burner)
- **Empty/negative result looks like:** the target number is not among the public numbers — it's likely a genuine private line, not a known shared burner (though it could still be a private paid number on another service).

## Gotchas & OpSec
- Human-in-the-loop: **account-login** and a **partial payment wall** for private numbers.
- OpSec: free numbers are **public** — never route sensitive codes tied to you through them; assume anyone can read the inbox.
- Detection caveat: a number's absence here doesn't prove it isn't disposable elsewhere; there are many such services.

## Overlaps ("do both")
- Pairs with `[[fastmail-usa]]` — combine a disposable number with a low-attribution mailbox to stand up a complete sock-puppet identity.

## Trust & verifiability
`trust: community` — an anonymous public-SMS service. Its data (the public inbox) is real but shared and manipulable; treat both the numbers and their message logs as untrusted, public infrastructure.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | receive-sms-free-3 |
| category | phone |
| selectorsIn → selectorsOut | phone → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
