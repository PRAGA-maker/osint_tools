---
id: cardguru
name: CardGuru
description: Use when a sock-puppet signup form demands a card number for format validation — generates Luhn-valid TEST card numbers that carry no funds. Investigator OpSec, not a lookup.
url: https://cardguru.io/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Generating Luhn-valid, non-functional test card numbers to satisfy form-level card validation on throwaway/sock-puppet registrations.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free single and bulk generation plus a validator; exports JSON/XML/CSV. No account.
opsec: passive
opsecNote: These are format-valid TEST numbers (Luhn/MOD-10) with NO funds behind them — they pass a form's syntax check but will never complete a real charge. Use only to get past a validation field on a legitimate sock-puppet signup; do NOT use them to attempt purchases, obtain paid goods/services, or defraud anyone — that is illegal and out of scope.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Simple free test-card generator implementing the public Luhn algorithm; nothing here is a real financial instrument.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- 10minutemail-com
- simplelogin
aliases:
- CardGuru
- cardguru.io
tags:
- Sock Puppets
- opsec
- test-card
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# CardGuru

> A test-card-number generator: Luhn-valid numbers with no funds, used to clear a form's card-format check when building a sock puppet — never for actual payments.

## When to use
You are standing up a sock-puppet/research account and the signup form requires a card number purely to *validate format* (a Luhn check) rather than to charge you. CardGuru produces syntactically valid test numbers for the major networks so the field accepts them. It's investigator OpSec plumbing — it returns no data about any subject, and it explicitly does **not** create usable payment instruments.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cardguru.io/.
2. Pick a card network (VISA/Mastercard/Amex/Discover, optionally by country) and generate a single number or a bulk batch (export JSON/XML/CSV).
3. Paste the number into the signup form's card field to satisfy its format validation.
4. Use the built-in validator to confirm a number is Luhn-valid before submitting.
5. If the form performs a real authorization (not just format validation), stop — a test number will (and should) be declined; that is not a use case for this tool.

## Inputs → Outputs
- **In:** none (you select a card type; you supply nothing about a target)
- **Out:** Luhn-valid **test** card numbers (no funds; not a harvested selector)
- **Empty/negative result looks like:** the target form rejects the number or attempts a real charge and declines it — meaning the form does live authorization, not just format checking; test numbers won't work there by design.

## Gotchas & OpSec
- **Not real money and not for purchases.** These numbers pass syntax checks only; using them to obtain paid goods/services or to deceive a merchant is fraud and out of scope. Keep use to format-validation on legitimate sock-puppet signups.
- Many real payment flows do a live auth, not just Luhn — expect (and accept) declines there.
- Don't pair a test card with your real identity/email; combine with a throwaway inbox and clean profile.

## Overlaps ("do both")
- Pairs with `[[10minutemail-com]]` and `[[simplelogin]]` — together they cover the email and card-field legs of a throwaway registration while keeping your real identity out of it.

## Trust & verifiability
`trust: unverified` — a simple free generator implementing the public Luhn algorithm. There's nothing sensitive to trust: the output is deliberately non-functional test data, useful only for passing format validation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cardguru |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
