---
id: email2whatsapp
name: Email2WhatsApp
description: Use when you have an `email` and want to derive the linked WhatsApp `phone` number — exploits partial-number leaks in password-recovery flows — returns candidate `phone`s, WhatsApp `social-profile`s, and `image`s.
url: https://github.com/dsonbaker/email2whatsapp
category: messaging
path:
- messaging
- whatsapp
bestFor: Recovering a target's WhatsApp phone number (and photo) starting from just an email address.
selectorsIn:
- email
selectorsOut:
- phone
- social-profile
- image
status: live
pricing: free
costNote: Free and open-source (Go). `go install github.com/dsonbaker/email2whatsapp@latest`. No paid tiers.
opsec: active
opsecNote: This is intrusive. It probes third-party sites' password-recovery endpoints (PayPal, Mercado Livre, Microsoft, Uber, etc.) for leaked digits and then connects to WhatsApp to validate candidate numbers — actions those services and WhatsApp may log or rate-limit, and which can leave a trace. Run behind a VPN and a sock-puppet WhatsApp account/number; understand the legal/ToS implications before use.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Open-source OSINT tool; the technique is clever but noisy and dependent on target services continuing to leak partial digits, so it breaks as they patch.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
aliases:
- email2whatsapp
- dsonbaker/email2whatsapp
tags:
- whatsapp
- email
- phone
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Email2WhatsApp

> A CLI that reverses an `email` into a WhatsApp `phone` number by assembling partial digits that other services leak in their password-recovery flows, then validating candidates against WhatsApp.

## When to use
You have an `email` for a subject but no phone number, and you need their WhatsApp — a common bridge from an email-only lead to a phone-based one (and to a profile photo). Reach for it when password-recovery pages for services the subject uses reveal masked partial numbers you can stitch together.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install -v github.com/dsonbaker/email2whatsapp@latest` (requires Go).
2. Route traffic through a VPN and have a sock-puppet WhatsApp account ready for the validation step.
3. Run: `email2whatsapp -email target@gmail.com`. The tool scrapes recovery-flow leaks (e.g. PayPal, Magalu) to harvest partial digits and assembles candidate numbers.
4. Optionally brute-force additional confirmations: `email2whatsapp -bruteforce meli` (Mercado Livre), etc.
5. Validate candidates via WhatsApp — the tool outputs folders of valid numbers, profile photos of matches (`image`), and numbers lacking public profiles for further work. Pivot confirmed `phone` into phone-OSINT.

## Inputs → Outputs
- **In:** `email`
- **Out:** candidate/validated `phone` numbers, WhatsApp `social-profile`s, profile `image`s
- **Empty/negative result looks like:** no digits recovered (the email isn't registered on the leaking services, or they've patched the leak) or no valid WhatsApp among candidates. A null is common and does not prove the person has no WhatsApp — it usually means the digit-leak path was unavailable.

## Gotchas & OpSec
- Fragile by design: it depends on third-party services leaking partial numbers; as those are fixed, coverage drops. Expect variable results.
- Noisy and intrusive — recovery-flow probing and WhatsApp validation can be logged/rate-limited and raise ToS/legal issues. Use VPN + sock puppet, and only within authorized work.
- Candidate numbers are guesses until WhatsApp-validated; treat unvalidated ones as unconfirmed.

## Overlaps ("do both")
- Pairs with `[[watools]]` (confirm a number on WhatsApp and grab its photo) and `[[holehe]]` (where else the email is registered) — holehe/recovery leaks feed the digits, email2whatsapp assembles the number, watools confirms and enriches it.

## Trust & verifiability
`trust: community` — open-source and inspectable, but results are inferential (assembled from partial leaks) and must be WhatsApp-validated; false candidates are expected.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email2whatsapp |
| category | messaging |
| selectorsIn → selectorsOut | email → phone, social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
